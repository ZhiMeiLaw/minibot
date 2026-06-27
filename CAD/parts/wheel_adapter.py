"""
Wheel Adapter
Mini-Atlas V6 Alpha
80mm wheel rigid mount | Ref: DR-011, PR-001
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

doc = App.newDocument("WheelAdapter")

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeCylinder(P.WHEEL_DIAMETER / 2 + 5.0, 15.0)

hub_cyl = Part.makeCylinder(8.0, 18.0)
body.Shape = body.Shape.cut(hub_cyl)

bolt_circle_d = 30.0
bolt_d = 3.0
for i in range(4):
    ang = i * math.pi / 2
    bx = bolt_circle_d / 2 * math.cos(ang)
    by = bolt_circle_d / 2 * math.sin(ang)
    bh = Part.makeCylinder(bolt_d / 2, 20.0, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(bh)

doc.recompute()
out = os.path.join(STL_DIR, "wheel_adapter.stl")
mesh = Mesh.Mesh()
tess = body.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] wheel_adapter.stl -> {out}")