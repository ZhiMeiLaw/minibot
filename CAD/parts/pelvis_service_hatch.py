"""
Pelvis Service Hatch (PSH-001)
Mini-Atlas V6 Alpha
Rear removable cover for battery/XT30/fuse access
Ref: MDS-04 §14

Features:
  - 4 x M3 mounting holes
  - XT30 connector port cutout
  - Power switch access slot
  - Fuse holder slot
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

doc = App.newDocument("PelvisServiceHatch")

W, D, H = P.PELVIS_W, P.PELVIS_D, P.PELVIS_H
wall_t = P.PELVIS_WALL_T

# ── Hatch Plate ────────────────────────────────────────
hatch_w = W - 20  # Slightly smaller than pelvis width
hatch_d = 8.0     # Thickness
hatch_h = D - 20  # Slightly smaller than pelvis depth

hatch_plate = doc.addObject("Part::Feature", "HatchPlate")
hatch_plate.Shape = Part.makeBox(hatch_w, hatch_d, hatch_h,
                                  App.Vector(0, D / 2 - hatch_d / 2, 0))

# ── XT30 Port Cutout ───────────────────────────────────
xt30_w = 16.0
xt30_h = 12.0
xt30_cut = Part.makeBox(xt30_w, hatch_d + 2, xt30_h,
                         App.Vector(-xt30_w / 2, D / 2 - hatch_d / 2, 0))
hatch_plate.Shape = hatch_plate.Shape.cut(xt30_cut)

# ── Power Switch Slot ──────────────────────────────────
switch_w = 20.0
switch_h = 10.0
switch_cut = Part.makeBox(switch_w, hatch_d + 2, switch_h,
                           App.Vector(0, D / 2 - hatch_d / 2, -hatch_h / 2 + 15))
hatch_plate.Shape = hatch_plate.Shape.cut(switch_cut)

# ── Fuse Holder Slot ───────────────────────────────────
fuse_w = 12.0
fuse_h = 8.0
fuse_cut = Part.makeBox(fuse_w, hatch_d + 2, fuse_h,
                         App.Vector(0, D / 2 - hatch_d / 2, hatch_h / 2 - 15))
hatch_plate.Shape = hatch_plate.Shape.cut(fuse_cut)

# ── Mounting Holes (4 x M3) ───────────────────────────
m3_drill = 3.2
mount_holes = [
    (-hatch_w / 2 + 6, hatch_h / 2 - 6),
    (hatch_w / 2 - 6, hatch_h / 2 - 6),
    (-hatch_w / 2 + 6, -hatch_h / 2 + 6),
    (hatch_w / 2 - 6, -hatch_h / 2 + 6),
]
for mx, mz in mount_holes:
    mh = Part.makeCylinder(m3_drill / 2, hatch_d + 4,
                           App.Vector(mx, D / 2 - hatch_d / 2, mz))
    hatch_plate.Shape = hatch_plate.Shape.cut(mh)

# ── Latch Tab (front face, snaps into pelvis frame) ───
latch_tab = Part.makeBox(12, 4, 6,
                          App.Vector(0, D / 2 + 2, 0))
hatch_plate.Shape = hatch_plate.Shape.fuse(latch_tab)

doc.recompute()
out = os.path.join(STL_DIR, "pelvis_service_hatch.stl")
mesh = Mesh.Mesh()
MeshPart.meshFromShape(hatch_plate.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
mesh.write(out)
_app_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_app_name)
print(f"[OK] pelvis_service_hatch.stl -> {out}")
