"""
Knee Output / Fork (V6-PRT-0021)
Mini-Atlas V6 Alpha
50 x 60 x 35 mm | fork type | shaft Ø8.10mm slip fit | clamp gap 2mm
Knee axis: Y direction
Ref: CDS-05B, ECO-003
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

doc = App.newDocument("KneeOutput")

W, D, H = P.KNEE_OUTPUT_W, P.KNEE_OUTPUT_D, P.KNEE_OUTPUT_H
gap = P.CLAMP_GAP
arm_t = 4.0
x_ctr = W / 2
z_ctr = H / 2

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeBox(W, D, H)

# Fork cuts for rotation around Y axis
# Fork arms are in the XZ plane
y1 = -D/2 + gap/2
y2 = D/2 - gap/2
cut_front = Part.makeBox(W, arm_t, H + 2, App.Vector(-W/2, y1, -1))
cut_back = Part.makeBox(W, arm_t, H + 2, App.Vector(-W/2, y2, -1))
body.Shape = body.Shape.cut(cut_front).cut(cut_back)

# Shaft hole - along Y axis (knee axis)
shaft_d = P.SHAFT_D + 0.1
shaft_hole = Part.makeCylinder(shaft_d / 2, D + 4, App.Vector(x_ctr, -2, z_ctr), App.Vector(0, 1, 0))
body.Shape = body.Shape.cut(shaft_hole)

# Bearing bosses (for 698 bearings, on Y axis)
boss_d = 24.0
boss_h = 5.0
for dy in [-P.BEARING_SPACING_KNEE/2, P.BEARING_SPACING_KNEE/2]:
    boss = Part.makeCylinder(boss_d / 2, boss_h, App.Vector(x_ctr, D/2 + dy, z_ctr), App.Vector(0, 1, 0))
    body.Shape = body.Shape.fuse(boss)

# Carbon tube clamp - along Z- direction (downward)
clamp_w = 18.0
clamp_d = P.CARBON_OD + 4 * 2
clamp_h = P.CARBON_LENGTH_VISIBLE + 15

# Clamp at bottom, extending downward
clamp = Part.makeBox(clamp_w, clamp_d, clamp_h,
                      App.Vector(x_ctr - clamp_w/2, -clamp_d/2, -clamp_h))
body.Shape = body.Shape.fuse(clamp)

# Carbon tube insert hole - along Z direction
carbon_insert = Part.makeCylinder(P.CARBON_OD / 2 + 0.2, P.CARBON_LENGTH_VISIBLE + 20,
                                   App.Vector(x_ctr, 0, -P.CARBON_LENGTH_VISIBLE - 5),
                                   App.Vector(0, 0, 1))
body.Shape = body.Shape.cut(carbon_insert)

# Clamp split gap for carbon tube
clamp_split = Part.makeBox(P.CLAMP_GAP, clamp_d + 4, clamp_w + 4,
                            App.Vector(x_ctr - P.CLAMP_GAP/2, -clamp_d/2 - 2, -clamp_h/2))
body.Shape = body.Shape.cut(clamp_split)

# Clamp screws - M3
m3_d = 3.2
for dy in [-5, 5]:
    sc = Part.makeCylinder(m3_d / 2, 25,
                            App.Vector(x_ctr + clamp_w/2, dy, -clamp_h/2), App.Vector(1, 0, 0))
    body.Shape = body.Shape.cut(sc)

# Brass insert holes for lower leg adapter
brass_ins_d = 4.4
pcd_leg = 30.0
for dx in [-pcd_leg/2, pcd_leg/2]:
    for dy in [-pcd_leg/2, pcd_leg/2]:
        ins = Part.makeCylinder(brass_ins_d / 2, 7, 
                                 App.Vector(x_ctr + dx, dy, -1), App.Vector(0, 0, 1))
        body.Shape = body.Shape.cut(ins)

# Torque module connection (M3 x4)
pcd = 18.0
m3_d = 3.2
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = pcd / 2 * math.cos(ang)
    by = pcd / 2 * math.sin(ang)
    ins = Part.makeCylinder(m3_d / 2, 8,
                             App.Vector(x_ctr + bx, D/2 + by, -1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(ins)

# Structural ribs
rib_t = 3.0
for dx_sgn in [-1, 1]:
    dx = dx_sgn * 12
    rib = Part.makeBox(18, rib_t, H * 0.5,
                        App.Vector(x_ctr + dx - 9, -rib_t/2, H * 0.25))
    body.Shape = body.Shape.fuse(rib)

doc.recompute()
out = os.path.join(STL_DIR, "knee_output.stl")
mesh = Mesh.Mesh()
tess = body.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] knee_output.stl -> {out}")