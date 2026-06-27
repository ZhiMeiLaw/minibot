"""
Pelvis Electronics Deck (PE-001)
Mini-Atlas V6 Alpha
Top compartment for ESP32, PDB, Buck converters, IMU
Ref: MDS-04 §4, §5, §6

Layout:
  Top Cover (removable, 4x M3)
    |
  Electronics Plate (ESP32 standoff mount)
    |
  Battery Bay (below)
"""
import FreeCAD as App
import Part
import Mesh
# MeshPart.meshFromShape is broken in FreeCAD 1.1.1; use tessellate
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import STL_DIR
import config_params as P

doc = App.newDocument("PelvisElectronicsDeck")

W, D, H = P.PELVIS_W, P.PELVIS_D, P.PELVIS_H
wall_t = P.PELVIS_WALL_T

# ── Electronics Deck Plate ─────────────────────────────
# Flat plate at top of pelvis interior
deck_h = 8.0  # Thickness of mounting plate
deck_w = W - 2 * wall_t - 10  # Leave margin
deck_d = D - 2 * wall_t - 10

deck_plate = doc.addObject("Part::Feature", "DeckPlate")
deck_plate.Shape = Part.makeBox(deck_w, deck_d, deck_h,
                                 App.Vector(0, 0, H / 2 - deck_h / 2))

# ── ESP32 Mounting Points (4-point standoff) ───────────
# ESP32 DevKitC: ~57 x 22mm, 4 mounting holes
esp32_w = 57.0
esp32_d = 22.0
esp32_holes = [
    (-esp32_w / 2 + 4, -esp32_d / 2 + 4),
    (esp32_w / 2 - 4, -esp32_d / 2 + 4),
    (-esp32_w / 2 + 4, esp32_d / 2 - 4),
    (esp32_w / 2 - 4, esp32_d / 2 - 4),
]

for hx, hy in esp32_holes:
    hole = Part.makeCylinder(2.7 / 2, deck_h + 4,
                             App.Vector(hx, hy, H / 2 - deck_h / 2))
    deck_plate.Shape = deck_plate.Shape.cut(hole)

# ── Standoff Bosses (M3 Nylon standoff, 10mm height) ───
standoff_h = 10.0
standoff_od = 6.0
for hx, hy in esp32_holes:
    boss = Part.makeCylinder(standoff_od / 2, standoff_h,
                              App.Vector(hx, hy, H / 2 + standoff_h / 2))
    deck_plate.Shape = deck_plate.Shape.fuse(boss)

# ── Buck Converter Mounting Slots ──────────────────────
# Two slots for DROK 20A Buck and MP1584EN
slot_w = 25.0
slot_d = 15.0
slot_h = 5.0
for sx, sy in [(-20, -15), (20, -15)]:
    slot = Part.makeBox(slot_w, slot_d, slot_h,
                         App.Vector(sx - slot_w / 2, sy - slot_d / 2, H / 2 - slot_h / 2))
    deck_plate.Shape = deck_plate.Shape.cut(slot)

# ── IMU Mounting Point (center) ────────────────────────
imu_boss = Part.makeCylinder(8.0, 6.0, App.Vector(0, 0, H / 2 + 3))
deck_plate.Shape = deck_plate.Shape.fuse(imu_boss)

# ── Top Cover Mounting Holes ───────────────────────────
cover_hole_r = 1.6
cover_holes = [
    (-W / 2 + 10, -D / 2 + 10),
    (W / 2 - 10, -D / 2 + 10),
    (-W / 2 + 10, D / 2 - 10),
    (W / 2 - 10, D / 2 - 10),
]
for cx, cy in cover_holes:
    ch = Part.makeCylinder(cover_hole_r, H + 4, App.Vector(cx, cy, 0))
    deck_plate.Shape = deck_plate.Shape.cut(ch)

# ── Wire Pass-through ─────────────────────────────────
wire_pass = Part.makeCylinder(6.0, deck_h + 2,
                              App.Vector(0, -D / 4, H / 2))
deck_plate.Shape = deck_plate.Shape.cut(wire_pass)

doc.recompute()
out = os.path.join(STL_DIR, "pelvis_electronics_deck.stl")
mesh = Mesh.Mesh()
tess = deck_plate.Shape.tessellate(0.05)
mesh = Mesh.Mesh()
for tri in tess[1]:
    mesh.addFacet(tess[0][tri[0]], tess[0][tri[1]], tess[0][tri[2]])
mesh.write(out)
_app_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_app_name)
print(f"[OK] pelvis_electronics_deck.stl -> {out}")
