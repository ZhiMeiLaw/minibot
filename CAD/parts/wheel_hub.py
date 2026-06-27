"""
Wheel Hub
Mini-Atlas V6 Alpha
Press-fit to motor shaft, clamp screw secures to wheel
Ref: CDS-06 §7

Dimensions:
  ID: 20 mm (matches GB37-520 motor shaft)
  OD: 32 mm
  Height: 18 mm
  Clamp Screw: M3 x 2 (side clamping to motor shaft keyway)
  Anti-slip Teeth: inner wall micro-grooves for grip

Assembly:
  1. Hub press-fit onto motor shaft (20mm bore)
  2. M3 clamp screws secure to motor keyway/shaft
  3. Wheel slides onto hub OD
  4. Wheel clamped by outer plate
"""
import FreeCAD as App
import Part
import Mesh
import MeshPart
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import STL_DIR
import config_params as P

doc = App.newDocument("WheelHub")

# ── Parameters ──────────────────────────────────────────
hub_od = 32.0       # Outer diameter (CDS-06 §7)
hub_id = 20.0       # Inner bore for motor shaft
hub_h = 18.0        # Hub height
clamp_screw_d = 3.2 # M3 drill diameter
groove_count = 6    # Anti-slip teeth count

# ── Hub Body ───────────────────────────────────────────
hub_body = doc.addObject("Part::Feature", "HubBody")
hub_body.Shape = Part.makeCylinder(hub_od / 2, hub_h, App.Vector(0, 0, 0))

# ── Motor Shaft Bore ───────────────────────────────────
shaft_bore = doc.addObject("Part::Feature", "ShaftBore")
shaft_bore.Shape = Part.makeCylinder(hub_id / 2, hub_h + 2, App.Vector(0, 0, -1))
hub_body.Shape = hub_body.Shape.cut(shaft_bore.Shape)

# ── Anti-slip teeth (inner wall grooves) ───────────────
# 6 circumferential grooves for grip on motor shaft
groove_depth = 1.0
groove_width = 2.0
for i in range(groove_count):
    angle = i * 2 * math.pi / groove_count
    gx = (hub_id / 2 - groove_depth / 2) * math.cos(angle)
    gy = (hub_id / 2 - groove_depth / 2) * math.sin(angle)
    groove = Part.makeBox(groove_width, groove_width, hub_h + 2,
                          App.Vector(gx - groove_width / 2, gy - groove_width / 2, -1))
    hub_body.Shape = hub_body.Shape.cut(groove)

# ── Clamp Screw Holes (side clamping to motor shaft) ───
# Two M3 holes on opposite sides, drilling radially into the hub
for dy in [-hub_id / 2 + 2, hub_id / 2 - 2]:
    screw_hole = Part.makeCylinder(clamp_screw_d / 2, hub_h + 4,
                                    App.Vector(0, dy, 0), App.Vector(0, 1, 0))
    hub_body.Shape = hub_body.Shape.cut(screw_hole)

# ── Wheel Mounting Face (outer side, flat with ridge) ──
# Small ridge on outer face to help center the wheel
ridge_od = hub_od - 4
ridge_h = 2.0
ridge = Part.makeCylinder(ridge_od / 2, ridge_h, App.Vector(0, 0, hub_h / 2 - ridge_h / 2))
hub_body.Shape = hub_body.Shape.fuse(ridge)

# ── Export ─────────────────────────────────────────────
doc.recompute()
out = os.path.join(STL_DIR, "wheel_hub.stl")
mesh = Mesh.Mesh()
MeshPart.meshFromShape(hub_body.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
mesh.write(out)
_app_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_app_name)
print(f"[OK] wheel_hub.stl -> {out}")
