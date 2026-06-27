"""
Hip Roll Torque Module (V6-PRT-0003)
Mini-Atlas V6 Alpha
Double clamp hub | 4x M3 bolt pattern | PCD 18mm
Ref: CDS-03C, ECO-001
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

doc = App.newDocument("HipRollTorqueModule")

hub_od = 28.0
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
dz_clamp = 3.0
for dz in [-dz_clamp, dz_clamp]:
    sc = Part.makeCylinder(m3_clamp_d / 2, hub_od + 4,
                            App.Vector(hub_od / 2, 0, dz), App.Vector(1, 0, 0))
    body.Shape = body.Shape.cut(sc)

pcd = 18.0
m3_d = 3.2
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = pcd / 2 * math.cos(ang)
    by = pcd / 2 * math.sin(ang)
    bh = Part.makeCylinder(m3_d / 2, hub_th + 4, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(bh)

doc.recompute()
out = os.path.join(STL_DIR, "hip_roll_torque_module.stl")
mesh = Mesh.Mesh()
tess = body.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] hip_roll_torque_module.stl -> {out}")