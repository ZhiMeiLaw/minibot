"""
Calf Tube (Carbon Fiber)
Mini-Atlas V6 Alpha
OD10 x ID8 x 150mm (120mm visible) | Ref: CDS-04B, ECO-001
"""
import FreeCAD as App
import Part
import Mesh
import MeshPart
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import STL_DIR
import config_params as P

doc = App.newDocument("CalfTube")

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeCylinder(P.CARBON_OD / 2, P.CARBON_LENGTH_TOTAL)

bore = Part.makeCylinder(P.CARBON_ID / 2, P.CARBON_LENGTH_TOTAL + 2)
body.Shape = body.Shape.cut(bore)

doc.recompute()
out = os.path.join(STL_DIR, "calf_tube.stl")
mesh = Mesh.Mesh()
MeshPart.meshFromShape(body.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] calf_tube.stl -> {out}")