"""
Pelvis Main Frame (PF-001A)
Mini-Atlas V6 Alpha
120 x 80 x 60 mm | hollow box frame, wall 4mm | Hip Mount Ear (ECO-003)
Ref: MDS-04, MDS-04B, ECO-003

This is the structural backbone of the pelvis.
Modular design:
  - Main Frame (this file): box structure + Hip Roll ears
  - Battery Bay: slide-in tray (pelvis_battery_bay.py)
  - Electronics Deck: ESP32/PDB mounting (pelvis_electronics_deck.py)
  - Service Hatch: rear removable cover (pelvis_service_hatch.py)
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

doc = App.newDocument("PelvisMainFrame")

W, D, H = P.PELVIS_W, P.PELVIS_D, P.PELVIS_H
wall_t = P.PELVIS_WALL_T
ear_ext = P.HIP_EAR_EXTENSION
ear_th = P.HIP_EAR_THICKNESS
root_fillet = P.HIP_EAR_ROOT_FILLET
rib_t = P.HIP_EAR_RIB_THICKNESS

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeBox(W, D, H)

# ── Hollow interior ────────────────────────────────────
inner_w = W - 2 * wall_t
inner_d = D - 2 * wall_t
inner_h = H - 2 * wall_t
inner_cut = Part.makeBox(inner_w, inner_d, inner_h, App.Vector(wall_t, wall_t, wall_t))
body.Shape = body.Shape.cut(inner_cut)

# ── Hip Roll Mount Ears (left + right) ─────────────────
for y_sign in [-1, 1]:
    y_start = D / 2 if y_sign > 0 else -D / 2
    ear = Part.makeBox(ear_th, ear_ext, H, App.Vector(W / 2 - ear_th / 2, y_start, 0))
    body.Shape = body.Shape.fuse(ear)

    rib = Part.makeBox(rib_t, ear_ext + 5, H - 2,
                        App.Vector(W / 2 - rib_t / 2, y_start - y_sign * 2.5, 1))
    body.Shape = body.Shape.fuse(rib)

    y_ear_center = y_sign * (D / 2 + ear_ext / 2)
    brg_pocket = Part.makeCylinder(P.POCKET_D_HIP_ROLL / 2, P.POCKET_DEPTH_HIP_ROLL + 2,
                                    App.Vector(W / 2 - ear_th / 2 - 1, y_ear_center, H / 2),
                                    App.Vector(1, 0, 0))
    body.Shape = body.Shape.cut(brg_pocket)

    for dz in [-5, 5]:
        insert_hole = Part.makeCylinder(1.6, ear_th + rib_t + 4,
                                         App.Vector(W / 2 + ear_th / 2 + rib_t / 2,
                                                    y_ear_center,
                                                    H / 2 + dz),
                                         App.Vector(1, 0, 0))
        body.Shape = body.Shape.cut(insert_hole)

# ── Hip Roll Bearing Bosses (front face) ───────────────
for dy in [-D / 2 - ear_ext / 2, D / 2 + ear_ext / 2]:
    boss = Part.makeCylinder(11, H, App.Vector(W / 2, dy, 0))
    body.Shape = body.Shape.fuse(boss)

# ── Hip Roll Mounting Bolts (vertical through-bolts) ───
m3_d = 3.2
for dy in [-45, 45]:
    pbolt = Part.makeCylinder(m3_d / 2, H + 4,
                               App.Vector(W / 2, dy, H / 2 - 2), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(pbolt)

# ── Wire Channel (internal, top rear) ──────────────────
wire_cut = Part.makeBox(20, inner_d - 10, 8, App.Vector(W / 2 - 10, wall_t + 5, H - 12))
body.Shape = body.Shape.cut(wire_cut)

# ── Hatch Mounting Holes (rear face, 4 x M3) ───────────
hatch_mount_holes = [
    (-W / 2 + 12, D / 2 - 4),
    (W / 2 - 12, D / 2 - 4),
    (-W / 2 + 12, -D / 2 + 4),
    (W / 2 - 12, -D / 2 + 4),
]
for hx, hy in hatch_mount_holes:
    hm = Part.makeCylinder(1.6, H + 2, App.Vector(hx, hy, 0), App.Vector(0, 1, 0))
    body.Shape = body.Shape.cut(hm)

# ── Battery Bay Retention Grooves (front face) ─────────
# Snap-fit tabs that hold the battery bay in place
for dy in [-15, 15]:
    groove = Part.makeBox(8, 3, 4,
                           App.Vector(W / 2 + 1, dy, -H / 4))
    body.Shape = body.Shape.fuse(groove)

doc.recompute()
out = os.path.join(STL_DIR, "pelvis_main_frame.stl")
mesh = Mesh.Mesh()
tess = body.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_app_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_app_name)
print(f"[OK] pelvis_main_frame.stl -> {out}")
