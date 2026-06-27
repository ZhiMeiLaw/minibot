"""
Pelvis Battery Bay (PB-001)
Mini-Atlas V6 Alpha
Bottom compartment for 3S2P battery slide-in tray
Ref: MDS-04 §3, CDS-06A §9

Dimensions:
  Fits inside pelvis frame (120 x 80 x 60mm)
  Battery volume: ~80 x 60 x 25mm (3S2P 18650 layout)
  Slide-in tray with rear latch
  XT30 connector port on rear face
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

doc = App.newDocument("PelvisBatteryBay")

W, D, H = P.PELVIS_W, P.PELVIS_D, P.PELVIS_H
wall_t = P.PELVIS_WALL_T

# ── Battery Bay Base (bottom 25mm of pelvis) ──────────
battery_h = 25.0  # Height of battery compartment
battery_w = W - 2 * wall_t - 4  # Leave room for walls
battery_d = D - 2 * wall_t - 4

# Main bay body
bay_body = doc.addObject("Part::Feature", "BayBody")
bay_body.Shape = Part.makeBox(battery_w + 2 * wall_t, battery_d + 2 * wall_t, battery_h)

# ── Battery Tray ───────────────────────────────────────
# Slide-in tray that holds 3S2P (6 cells in 2x3 grid)
# Cell size: 18.5 x 65mm, 2x3 grid = 37 x 195mm (too long)
# Better: 3S2P = 3 cells in series, 2 parallel strings
# Layout: 2 rows x 3 cols = 37mm x 55.5mm footprint

tray_w = 55.0   # 3 x 18.5mm cells side by side
tray_d = 38.0   # 2 x 18.5mm cells front to back
tray_h = 60.0   # 18650 cell height
tray_gap = 2.0  # Gap between cells

tray_body = doc.addObject("Part::Feature", "TrayBody")
tray_body.Shape = Part.makeBox(tray_w, tray_d, tray_h)

# Cell dividers (cross-hatch pattern for 2x3 grid)
# Horizontal dividers
for i in range(1, 3):
    div = Part.makeBox(tray_w, tray_gap, tray_h + 1,
                       App.Vector(-tray_w / 2, -tray_d / 2 + i * tray_d / 3, 0))
    tray_body.Shape = tray_body.Shape.cut(div)

# Vertical divider
mid_div = Part.makeBox(tray_gap, tray_d, tray_h + 1,
                       App.Vector(0, -tray_d / 2, 0))
tray_body.Shape = tray_body.Shape.cut(mid_div)

# ── XT30 Port Cutout (rear face) ───────────────────────
xt30_w = 16.0
xt30_h = 12.0
xt30_cut = Part.makeBox(xt30_w, xt30_h, wall_t + 4,
                        App.Vector(-xt30_w / 2, D / 2 - wall_t / 2 - xt30_h / 2, -battery_h / 2))
bay_body.Shape = bay_body.Shape.cut(xt30_cut)

# ── Battery Latch Tabs (front face) ────────────────────
# Two small tabs that snap into the main pelvis frame
for dy in [-15, 15]:
    tab = Part.makeBox(8, 4, 3,
                       App.Vector(-4, D / 2 + 1.5, -battery_h / 2 + dy))
    bay_body.Shape = bay_body.Shape.fuse(tab)

# ── Wire Pass-through Hole ─────────────────────────────
wire_hole = Part.makeCylinder(4.0, battery_h + 2,
                             App.Vector(0, 0, battery_h / 2 + 1))
bay_body.Shape = bay_body.Shape.cut(wire_hole)

# ── Assemble ───────────────────────────────────────────
bay_body.Shape = bay_body.Shape.fuse(tray_body.Shape)

doc.recompute()
out = os.path.join(STL_DIR, "pelvis_battery_bay.stl")
mesh = Mesh.Mesh()
MeshPart.meshFromShape(bay_body.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
mesh.write(out)
_app_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_app_name)
print(f"[OK] pelvis_battery_bay.stl -> {out}")
