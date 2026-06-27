"""
Generate STL from a FreeCAD Part shape using tessellation (works in FreeCAD 1.1.1
where MeshPart.meshFromShape may return empty meshes).

Usage: freecadcmd generate_stl.py <shape_object> <output_stl_path> [tessellation_quality]
  tessellation_quality: 0.05 (default) or 0.1 for coarser mesh
"""
import FreeCAD as App
import Part
import Mesh
import os
import sys

# Get shape and output path from arguments
if len(sys.argv) < 3:
    print("Usage: freecadcmd generate_stl.py <shape_var_name> <output_path>")
    sys.exit(1)

shape_var_name = sys.argv[1]
output_path = sys.argv[2]
quality = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05

# Get the shape from the document
doc = App.ActiveDocument
shape_obj = getattr(doc, shape_var_name, None)
if shape_obj is None:
    # Try to find by label
    for obj in doc.Objects:
        if obj.Label.lower().replace(" ", "_") == shape_var_name.lower():
            shape_obj = obj
            break
        if hasattr(obj, "Shape"):
            shape = obj.Shape
            if shape:
                break

# Use the first object with a valid Shape if shape_var_name not found directly
if shape_obj is None or not hasattr(shape_obj, "Shape"):
    for obj in doc.Objects:
        if hasattr(obj, "Shape") and obj.Shape:
            shape_obj = obj
            break

if shape_obj is None or not hasattr(shape_obj, "Shape") or not shape_obj.Shape:
    print(f"[ERROR] No shape found for '{shape_var_name}'")
    sys.exit(1)

shape = shape_obj.Shape
if not shape.Solid:
    # Compound or shell - try to tessellate anyway
    pass

# Tessellate
tess = shape.tessellate(quality)
verts = tess[0]
tris = tess[1]

# Build mesh
mesh = Mesh.Mesh()
for tri in tris:
    p1 = verts[tri[0]]
    p2 = verts[tri[1]]
    p3 = verts[tri[2]]
    mesh.addFacet(p1, p2, p3)

print(f"Tessellated: {len(tris)} triangles, {len(verts)} vertices")

# Write STL
out_dir = os.path.dirname(output_path)
if out_dir:
    os.makedirs(out_dir, exist_ok=True)
mesh.write(output_path)
print(f"[OK] {output_path} ({mesh.CountFacets} facets, {mesh.CountPoints} points)")
