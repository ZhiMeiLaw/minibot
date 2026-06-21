"""
FreeCAD Common Function Library
Mini-Atlas V6 Alpha
"""
import FreeCAD as App
import Part
import Mesh
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config_params as P


def new_doc(name):
    if App.ActiveDocument:
        App.closeDocument(App.ActiveDocument.Name)
    doc = App.newDocument(name)
    return doc


def bearing_pocket(doc, label, center, diam, depth, bore_diam=None, parent_shape=None):
    """Create a bearing pocket (cylindrical recess) and cut from parent if provided."""
    pocket = doc.addObject("Part::Feature", label)
    cyl = Part.makeCylinder(diam / 2, depth, center, App.Vector(0, 0, 1))
    pocket.Shape = cyl
    if bore_diam:
        bore = Part.makeCylinder(bore_diam / 2, depth + 2, center, App.Vector(0, 0, 1))
        pocket.Shape = cyl.cut(bore)
    if parent_shape is not None:
        parent_shape.Shape = parent_shape.Shape.cut(cyl)
        return parent_shape
    return pocket


def servo_pocket(doc, label, pos, w, h, d, parent_shape=None):
    """Create a rectangular servo pocket (recess)."""
    box = Part.makeBox(w, h, d, pos)
    obj = doc.addObject("Part::Feature", label)
    obj.Shape = box
    if parent_shape is not None:
        parent_shape.Shape = parent_shape.Shape.cut(box)
        return parent_shape
    return obj


def fork_ear_cut(doc, label, center_y, total_d, gap, arm_t, height, axis="y"):
    """Create cutout shapes for fork ears (gap between two arms)."""
    cuts = []
    if axis == "y":
        y1 = center_y - gap / 2 - arm_t
        y2 = center_y + gap / 2
        c1 = Part.makeBox(999, arm_t, height, App.Vector(-500, y1, -1))
        c2 = Part.makeBox(999, arm_t, height, App.Vector(-500, y2, -1))
        cuts = [c1, c2]
    else:
        x1 = center_y - gap / 2 - arm_t
        x2 = center_y + gap / 2
        c1 = Part.makeBox(arm_t, 999, height, App.Vector(x1, -500, -1))
        c2 = Part.makeBox(arm_t, 999, height, App.Vector(x2, -500, -1))
        cuts = [c1, c2]
    return cuts


def clamp_cut(doc, label, center_y, total_d, gap, arm_t, height, screw_diam=3.0, screw_count=2):
    """Create one half of a split clamp cutout (for both halves = full clamp)."""
    import math
    cuts = fork_ear_cut(doc, label, center_y, total_d, gap, arm_t, height)
    for c in cuts:
        pass
    half_gap = gap / 2
    y_a = center_y - half_gap - arm_t / 2
    y_b = center_y + half_gap + arm_t / 2
    screw_positions = []
    x_s = 0
    z_step = height / (screw_count + 1)
    for i in range(screw_count):
        z = -height / 2 + z_step * (i + 1)
        screw_positions.append(App.Vector(x_s, y_a, z))
        screw_positions.append(App.Vector(x_s, y_b, z))
    for sp in screw_positions:
        screw_hole = Part.makeCylinder(screw_diam / 2, arm_t + 2, App.Vector(sp.x, sp.y, sp.z), App.Vector(0, 1, 0))
        cuts.append(screw_hole)
    return cuts


def servo_flange(doc, label, pos, w, h, d, bore_d=8.0, parent_shape=None):
    """Create a servo flange with center bore."""
    box = Part.makeBox(w, h, d, pos)
    bore = Part.makeCylinder(bore_d / 2, d + 2, App.Vector(pos.x, pos.y, pos.z - 1), App.Vector(0, 0, 1))
    obj = doc.addObject("Part::Feature", label)
    obj.Shape = box.cut(bore)
    if parent_shape is not None:
        parent_shape.Shape = parent_shape.Shape.cut(obj.Shape)
        return parent_shape
    return obj


def export_stl(doc, obj, filepath):
    """Export a single object to STL via mesh conversion."""
    import MeshPart
    mesh = Mesh.Mesh()
    MeshPart.meshFromShape(obj.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
    mesh.write(filepath)


def close_and_export(doc, obj, stl_path):
    """Export object to STL and close document."""
    doc.recompute()
    export_stl(doc, obj, stl_path)
    App.closeDocument(doc.name)
    print(f"[OK] {os.path.basename(stl_path)} -> {stl_path}")