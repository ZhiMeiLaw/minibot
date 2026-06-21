"""
Hip Roll Base (V6-PRT-0001)
Mini-Atlas V6 Alpha
70 x 60 x 42 mm | U-shape frame | 688-2RS x2, spacing 20mm | Side Mount (ECO-003)
Hip Roll axis: X (roll around X)
Bearing axis: X direction, spacing along Y
Ref: CDS-03A, ECO-003
"""
import FreeCAD as App
import Part
import Mesh
import MeshPart
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import STL_DIR
import config_params as P

doc = App.newDocument("HipRollBase")

W, D, H = P.HIP_ROLL_BASE_W, P.HIP_ROLL_BASE_D, P.HIP_ROLL_BASE_H
brg_d = P.POCKET_D_HIP_ROLL
brg_depth = P.POCKET_DEPTH_HIP_ROLL
spacing = P.BEARING_SPACING_HIP_ROLL

body = doc.addObject("Part::Feature", "Body")
box = Part.makeBox(W, D, H)
body.Shape = box

x_ctr = W / 2
z_ctr = H / 2
y_ctr = D / 2

for dy in [-spacing / 2, spacing / 2]:
    pocket = Part.makeCylinder(brg_d / 2, brg_depth + 2,
                                App.Vector(x_ctr, y_ctr + dy, z_ctr), App.Vector(1, 0, 0))
    body.Shape = body.Shape.cut(pocket)

shaft_bore = Part.makeCylinder(P.SHAFT_D / 2 + 0.1, W + 4,
                                App.Vector(x_ctr - W/2 - 2, y_ctr, z_ctr), App.Vector(1, 0, 0))
body.Shape = body.Shape.cut(shaft_bore)

servo_gap = 0.5
sw = P.SERVO_POCKET_W + 2 * servo_gap
sh = P.SERVO_POCKET_H + 2 * servo_gap
sd = P.SERVO_POCKET_D + 2 * servo_gap
servo_box = Part.makeBox(sd, sw, sh,
                          App.Vector(W - sd, (D - sw) / 2, (H - sh) / 2))
body.Shape = body.Shape.cut(servo_box)

m2_5_d = 2.7
m2_5_depth = 5.0
bc_d = 34.0
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = (W - sd) + bc_d / 2 * math.cos(ang)
    by = y_ctr + bc_d / 2 * math.sin(ang)
    bh = Part.makeCylinder(m2_5_d / 2, m2_5_depth + 2, App.Vector(bx, by, (H - sh) / 2 - 1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(bh)

pelvis_bolt_d = 3.2
pelvis_pcd_x = 30.0
pelvis_pcd_y = 30.0
for dx in [-pelvis_pcd_x / 2, pelvis_pcd_x / 2]:
    for dy in [-pelvis_pcd_y / 2, pelvis_pcd_y / 2]:
        pbolt = Part.makeCylinder(pelvis_bolt_d / 2, D + 4,
                                    App.Vector(dx, -2, z_ctr + dy), App.Vector(0, 1, 0))
        body.Shape = body.Shape.cut(pbolt)

wire_channel = Part.makeBox(6, D - 4, 8, App.Vector(x_ctr - 3, 2, H - 5))
body.Shape = body.Shape.cut(wire_channel)

rib_t = 3.0
rib_len = 15.0
for dy_sgn in [-1, 1]:
    dy = dy_sgn * (spacing / 2 + brg_d / 2)
    rib = Part.makeBox(rib_t, rib_len, H * 0.6,
                        App.Vector(x_ctr - rib_t / 2, y_ctr + dy - rib_len / 2, 4))
    body.Shape = body.Shape.fuse(rib)

tool_hole = Part.makeCylinder(4, 15, App.Vector(W - 2, y_ctr, 15), App.Vector(1, 0, 0))
body.Shape = body.Shape.cut(tool_hole)

doc.recompute()
out = os.path.join(STL_DIR, "hip_roll_base.stl")
mesh = Mesh.Mesh()
MeshPart.meshFromShape(body.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] hip_roll_base.stl -> {out}")