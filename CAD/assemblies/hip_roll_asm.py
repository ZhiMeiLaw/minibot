"""
Hip Roll Assembly
Mini-Atlas V6 Alpha
Base + Output + 2x688-2RS + Shaft (45mm) + TorqueModule
Hip Roll axis: X direction (robot rolls left/right)
Ref: MDS-03, CDS-03A, CDS-03B, ECO-001
"""
import FreeCAD as App
import Part
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import FCSTD_DIR
import config_params as P

doc = App.newDocument("HipRollAsm")

W, D, H = P.HIP_ROLL_BASE_W, P.HIP_ROLL_BASE_D, P.HIP_ROLL_BASE_H
x_ctr = W / 2
y_ctr = D / 2
z_ctr = H / 2

hr_base = doc.addObject("Part::Feature", "HipRollBase")
hr_base.Shape = Part.makeBox(W, D, H)

brg_d = P.POCKET_D_HIP_ROLL
brg_depth = P.POCKET_DEPTH_HIP_ROLL
spacing = P.BEARING_SPACING_HIP_ROLL
for dy in [-spacing / 2, spacing / 2]:
    pocket = Part.makeCylinder(brg_d / 2, brg_depth + 2,
                                App.Vector(x_ctr, y_ctr + dy, z_ctr), App.Vector(1, 0, 0))
    hr_base.Shape = hr_base.Shape.cut(pocket)

servo_box = Part.makeBox(P.SERVO_POCKET_D + 1, P.SERVO_POCKET_W + 1, P.SERVO_POCKET_H + 1,
                          App.Vector(W - P.SERVO_POCKET_D - 0.5, y_ctr - P.SERVO_POCKET_W / 2 - 0.5,
                                     z_ctr - P.SERVO_POCKET_H / 2 - 0.5))
hr_base.Shape = hr_base.Shape.cut(servo_box)

oW, oD, oH = P.HIP_ROLL_OUTPUT_W, P.HIP_ROLL_OUTPUT_D, P.HIP_ROLL_OUTPUT_H
o_x_ctr = oW / 2
o_z_ctr = oH / 2

hr_out = doc.addObject("Part::Feature", "HipRollOutput")
hr_out.Shape = Part.makeBox(oW, oD, oH)

gap = P.CLAMP_GAP
arm_t = 4.0
y1 = -oH / 2 + gap / 2
y2 = oH / 2 - gap / 2
hr_out.Shape = hr_out.Shape.cut(Part.makeBox(oW, oD + 2, arm_t, App.Vector(-oW / 2, -1, y1)))
hr_out.Shape = hr_out.Shape.cut(Part.makeBox(oW, oD + 2, arm_t, App.Vector(-oW / 2, -1, y2)))
hr_out.Shape = hr_out.Shape.cut(Part.makeCylinder(P.SHAFT_D / 2 + 0.1, oD + 4,
                                                    App.Vector(o_x_ctr, -2, o_z_ctr), App.Vector(0, 1, 0)))

hr_out.Placement = App.Placement(App.Vector(0, y_ctr, z_ctr), App.Rotation(0, 0, 0))

hr_torque = doc.addObject("Part::Feature", "HipRollTorque")
hr_torque.Shape = Part.makeCylinder(14, 10, App.Vector(0, 0, 0), App.Vector(0, 0, 1))
hr_torque.Shape = hr_torque.Shape.cut(Part.makeCylinder(P.SHAFT_D / 2, 12, App.Vector(0, 0, -1), App.Vector(0, 0, 1)))
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = 9.0 * math.cos(ang)
    by = 9.0 * math.sin(ang)
    hr_torque.Shape = hr_torque.Shape.cut(Part.makeCylinder(1.6, 12, App.Vector(bx, by, -1), App.Vector(0, 0, 1)))
hr_torque.Placement = App.Placement(App.Vector(x_ctr, y_ctr, z_ctr), App.Rotation(0, 0, 0))

shaft = doc.addObject("Part::Feature", "Shaft")
shaft.Shape = Part.makeCylinder(P.SHAFT_D / 2, 45.0, App.Vector(x_ctr, y_ctr - 22.5, z_ctr), App.Vector(0, 1, 0))

b1 = doc.addObject("Part::Feature", "Bearing1")
b1.Shape = Part.makeCylinder(P.BEARING_HIP_ROLL["od"] / 2, P.BEARING_HIP_ROLL["th"],
                               App.Vector(x_ctr - 2.5, y_ctr - spacing / 2, z_ctr), App.Vector(1, 0, 0))
b2 = doc.addObject("Part::Feature", "Bearing2")
b2.Shape = Part.makeCylinder(P.BEARING_HIP_ROLL["od"] / 2, P.BEARING_HIP_ROLL["th"],
                               App.Vector(x_ctr - 2.5, y_ctr + spacing / 2, z_ctr), App.Vector(1, 0, 0))

asm_shape = hr_base.Shape.fuse(hr_out.Shape).fuse(hr_torque.Shape).fuse(shaft.Shape).fuse(b1.Shape).fuse(b2.Shape)
asm = doc.addObject("Part::Feature", "HipRollAsm")
asm.Shape = asm_shape

doc.recompute()
out = os.path.join(FCSTD_DIR, "hip_roll_asm.fcstd")
doc.saveCopy(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] hip_roll_asm.fcstd -> {out}")
