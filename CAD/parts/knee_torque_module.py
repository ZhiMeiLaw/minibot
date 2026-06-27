"""
Knee Torque Module / Enhanced Double Clamp Hub (V6-PRT-0022)
Mini-Atlas V6 Alpha
Enhanced: M3 x4 clamp screws | anti-slip serration | 300k cycles
Ref: CDS-05C, ECO-001
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

doc = App.newDocument("KneeTorqueModule")

hub_od = 30.0
hub_th = 10.0

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeCylinder(hub_od / 2, hub_th)

horn_pocket = Part.makeCylinder(25.5 / 2, 3.5, App.Vector(0, 0, -0.5), App.Vector(0, 0, 1))
body.Shape = body.Shape.cut(horn_pocket)

center_bore = Part.makeCylinder(P.SHAFT_D / 2 + 0.5, hub_th + 2, App.Vector(0, 0, -1), App.Vector(0, 0, 1))
body.Shape = body.Shape.cut(center_bore)

clamp_gap = 2.0
gap_cut = Part.makeBox(clamp_gap, hub_od + 4, hub_th + 4,
                        App.Vector(-clamp_gap / 2, -hub_od / 2 - 2, -2))
body.Shape = body.Shape.cut(gap_cut)

m3_clamp_d = 3.2
for i in range(P.CLAMP_SCREW_COUNT_KNEE):
    ang = i * math.pi / 2
    dx = hub_od / 2 + 2
    cx = dx * math.cos(ang)
    cy = dx * math.sin(ang)
    sc = Part.makeCylinder(m3_clamp_d / 2, 20.0,
                            App.Vector(cx, cy, -5), App.Vector(math.cos(ang), math.sin(ang), 0))
    body.Shape = body.Shape.cut(sc)

inner_r = hub_od / 2 - 2.0
n_teeth = 60
tooth_depth = 0.4
for i in range(n_teeth):
    ang = i * 2 * math.pi / n_teeth
    tx = inner_r * math.cos(ang)
    ty = inner_r * math.sin(ang)
    tooth = Part.makeCylinder(tooth_depth, hub_th + 2, App.Vector(tx, ty, -1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(tooth)

pcd = 18.0
m3_d = 3.2
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = pcd / 2 * math.cos(ang)
    by = pcd / 2 * math.sin(ang)
    bh = Part.makeCylinder(m3_d / 2, hub_th + 4, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(bh)

rib_t = 3.0
for i in range(6):
    ang = i * math.pi / 3
    rib = Part.makeBox(rib_t, hub_od / 2 - 4, hub_th,
                        App.Vector(inner_r + 0.5, -rib_t / 2, 0))
    rib_rot = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0, 0, 1), ang * 180 / math.pi))
    rib_shape = rib.transformed(rib_rot.toMatrix())
    body.Shape = body.Shape.fuse(rib_shape)

doc.recompute()
out = os.path.join(STL_DIR, "knee_torque_module.stl")
mesh = Mesh.Mesh()
tess = body.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] knee_torque_module.stl -> {out}")