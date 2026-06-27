"""
Calf Tube (Carbon Fiber)
Mini-Atlas V6 Alpha
OD10 x ID8 x 150mm (120mm visible) | Ref: CDS-04B, ECO-001
"""
import FreeCAD as App
import Part
import Mesh
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

# Export STEP
step_out = os.path.join(os.path.dirname(STL_DIR), "step", "calf_tube.step")
Part.export([body.Shape], step_out)
print(f"[OK] calf_tube.step -> {step_out}")

# Export STL via tessellation (MeshPart.meshFromShape is broken in FreeCAD 1.1.1)
tess = body.Shape.tessellate(0.05)
verts = tess[0]
tris = tess[1]
mesh = Mesh.Mesh()
for tri in tris:
    mesh.addFacet(verts[tri[0]], verts[tri[1]], verts[tri[2]])

out = os.path.join(STL_DIR, "calf_tube.stl")
mesh.write(out)
print(f"[OK] calf_tube.stl -> {out} ({mesh.CountFacets} facets, {mesh.CountPoints} points)")

_app_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_app_name)
