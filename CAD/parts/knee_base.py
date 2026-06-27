"""
Knee Base (V6-PRT-0020)
Mini-Atlas V6 Alpha
50 x 60 x 35 mm | 698-2RS x2, spacing 18mm
Knee axis: Y direction
Ref: CDS-05A, ECO-001
"""
import FreeCAD as App
import Part
import Mesh
# MeshPart.meshFromShape is broken in FreeCAD 1.1.1; use tessellate
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import STL_DIR
import config_params as P

doc = App.newDocument("KneeBase")

W, D, H = P.KNEE_BASE_W, P.KNEE_BASE_D, P.KNEE_BASE_H
brg_d = P.POCKET_D_HPK
brg_depth = P.POCKET_DEPTH_HPK
spacing = P.BEARING_SPACING_KNEE

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeBox(W, D, H)

x_ctr = W / 2
z_ctr = H / 2

for dx in [-spacing / 2, spacing / 2]:
    pocket = Part.makeCylinder(brg_d / 2, brg_depth + 2,
                                App.Vector(x_ctr + dx, D / 2, z_ctr), App.Vector(0, 1, 0))
    body.Shape = body.Shape.cut(pocket)

shaft_bore = Part.makeCylinder(P.SHAFT_D / 2 + 0.1, W + 2,
                                App.Vector(-1, D / 2, z_ctr), App.Vector(1, 0, 0))
body.Shape = body.Shape.cut(shaft_bore)

servo_gap = 0.5
sw = P.SERVO_POCKET_W + 2 * servo_gap
sh = P.SERVO_POCKET_H + 2 * servo_gap
sd = P.SERVO_POCKET_D + 2 * servo_gap
servo_box = Part.makeBox(sd, sw, sh,
                          App.Vector(W - sd, (D - sw) / 2, (H - sh) / 2))
body.Shape = body.Shape.cut(servo_box)

m2_5_d = 2.7
bc_d = 34.0
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = (W - sd) + bc_d / 2 * math.cos(ang)
    by = D / 2 + bc_d / 2 * math.sin(ang)
    bh = Part.makeCylinder(m2_5_d / 2, 7, App.Vector(bx, by, (H - sh) / 2 - 1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(bh)

brass_ins_d = 4.4
brass_depth = 5.0
hp_pcd = 30.0
for dx in [-hp_pcd / 2, hp_pcd / 2]:
    for dy in [-hp_pcd / 2, hp_pcd / 2]:
        ins = Part.makeCylinder(brass_ins_d / 2, brass_depth + 2,
                                 App.Vector(x_ctr + dx, D / 2 + dy, H - 1), App.Vector(0, 0, 1))
        body.Shape = body.Shape.cut(ins)

brg_cover_pcd = 30.0
for i in range(2):
    ang = i * math.pi
    bx = x_ctr + spacing / 2 + brg_cover_pcd / 2 * math.cos(ang)
    by = D / 2 + brg_cover_pcd / 2 * math.sin(ang)
    ins = Part.makeCylinder(brass_ins_d / 2, brass_depth + 2, App.Vector(bx, by, H - 1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(ins)

for i in range(2):
    ang = i * math.pi
    bx = x_ctr - spacing / 2 + brg_cover_pcd / 2 * math.cos(ang)
    by = D / 2 + brg_cover_pcd / 2 * math.sin(ang)
    ins = Part.makeCylinder(brass_ins_d / 2, brass_depth + 2, App.Vector(bx, by, H - 1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(ins)

wire_hole = Part.makeCylinder(4, 15, App.Vector(W - 5, D / 2, 10), App.Vector(1, 0, 0))
body.Shape = body.Shape.cut(wire_hole)

tool_hole = Part.makeCylinder(4, 15, App.Vector(W - 2, D / 2, 10), App.Vector(1, 0, 0))
body.Shape = body.Shape.cut(tool_hole)

rib_t = 3.0
for dx_sgn in [-1, 1]:
    dx = dx_sgn * (spacing / 2 + brg_d / 2)
    rib = Part.makeBox(15, rib_t, H * 0.6,
                        App.Vector(x_ctr + dx - 7.5, D / 2 - rib_t / 2, 4))
    body.Shape = body.Shape.fuse(rib)

doc.recompute()
out = os.path.join(STL_DIR, "knee_base.stl")
mesh = Mesh.Mesh()
tess = body.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] knee_base.stl -> {out}")