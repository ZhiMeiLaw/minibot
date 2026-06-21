"""
Knee Assembly
Mini-Atlas V6 Alpha
Base + Output + 2x698-2RS + Shaft (38mm) + Enhanced TorqueModule (M3x4)
Knee axis: Y direction
Ref: MDS-03, CDS-05A, CDS-05B, CDS-05C, ECO-001
"""
import FreeCAD as App
import Part
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import FCSTD_DIR
import config_params as P

doc = App.newDocument("KneeAsm")

W, D, H = P.KNEE_BASE_W, P.KNEE_BASE_D, P.KNEE_BASE_H
x_ctr = W / 2
y_ctr = D / 2
z_ctr = H / 2

kn_base = doc.addObject("Part::Feature", "KneeBase")
kn_base.Shape = Part.makeBox(W, D, H)

brg_d = P.POCKET_D_HPK
brg_depth = P.POCKET_DEPTH_HPK
spacing = P.BEARING_SPACING_KNEE
for dx in [-spacing / 2, spacing / 2]:
    pocket = Part.makeCylinder(brg_d / 2, brg_depth + 2,
                                App.Vector(x_ctr + dx, y_ctr, z_ctr), App.Vector(0, 1, 0))
    kn_base.Shape = kn_base.Shape.cut(pocket)

servo_box = Part.makeBox(P.SERVO_POCKET_D + 1, P.SERVO_POCKET_W + 1, P.SERVO_POCKET_H + 1,
                          App.Vector(W - P.SERVO_POCKET_D - 0.5, y_ctr - P.SERVO_POCKET_W / 2 - 0.5,
                                     z_ctr - P.SERVO_POCKET_H / 2 - 0.5))
kn_base.Shape = kn_base.Shape.cut(servo_box)

oW, oD, oH = P.KNEE_OUTPUT_W, P.KNEE_OUTPUT_D, P.KNEE_OUTPUT_H
o_x_ctr = oW / 2
o_z_ctr = oH / 2

kn_out = doc.addObject("Part::Feature", "KneeOutput")
kn_out.Shape = Part.makeBox(oW, oD, oH)

gap = P.CLAMP_GAP
arm_t = 4.0
y1 = -oH / 2 + gap / 2
y2 = oH / 2 - gap / 2
kn_out.Shape = kn_out.Shape.cut(Part.makeBox(oW, oD + 2, arm_t, App.Vector(-oW / 2, -1, y1)))
kn_out.Shape = kn_out.Shape.cut(Part.makeBox(oW, oD + 2, arm_t, App.Vector(-oW / 2, -1, y2)))
kn_out.Shape = kn_out.Shape.cut(Part.makeCylinder(P.SHAFT_D / 2 + 0.1, oW + 4,
                                                    App.Vector(-2, oD / 2, o_z_ctr), App.Vector(1, 0, 0)))

kn_out.Placement = App.Placement(App.Vector(x_ctr, y_ctr, z_ctr), App.Rotation(0, 0, 0))

kn_torque = doc.addObject("Part::Feature", "KneeTorque")
kn_torque.Shape = Part.makeCylinder(15, 10, App.Vector(0, 0, 0), App.Vector(0, 0, 1))
kn_torque.Shape = kn_torque.Shape.cut(Part.makeCylinder(P.SHAFT_D / 2, 12, App.Vector(0, 0, -1), App.Vector(0, 0, 1)))
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = 9.0 * math.cos(ang)
    by = 9.0 * math.sin(ang)
    kn_torque.Shape = kn_torque.Shape.cut(Part.makeCylinder(1.6, 12, App.Vector(bx, by, -1), App.Vector(0, 0, 1)))
kn_torque.Placement = App.Placement(App.Vector(x_ctr, y_ctr, z_ctr), App.Rotation(0, 0, 0))

shaft = doc.addObject("Part::Feature", "Shaft")
shaft.Shape = Part.makeCylinder(P.SHAFT_D / 2, 38.0, App.Vector(x_ctr - 19, y_ctr, z_ctr), App.Vector(1, 0, 0))

b1 = doc.addObject("Part::Feature", "Bearing1")
b1.Shape = Part.makeCylinder(P.BEARING_KNEE["od"] / 2, P.BEARING_KNEE["th"],
                               App.Vector(x_ctr - spacing / 2, y_ctr - 3, z_ctr), App.Vector(0, 1, 0))
b2 = doc.addObject("Part::Feature", "Bearing2")
b2.Shape = Part.makeCylinder(P.BEARING_KNEE["od"] / 2, P.BEARING_KNEE["th"],
                               App.Vector(x_ctr + spacing / 2, y_ctr - 3, z_ctr), App.Vector(0, 1, 0))

asm_shape = kn_base.Shape.fuse(kn_out.Shape).fuse(kn_torque.Shape).fuse(shaft.Shape).fuse(b1.Shape).fuse(b2.Shape)
asm = doc.addObject("Part::Feature", "KneeAsm")
asm.Shape = asm_shape

doc.recompute()
out = os.path.join(FCSTD_DIR, "knee_asm.fcstd")
doc.saveCopy(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] knee_asm.fcstd -> {out}")
