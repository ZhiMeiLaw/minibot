"""
Leg Assembly (Single Leg)
Mini-Atlas V6 Alpha
HipRoll + HipPitch + Knee + Calf + Wheel Hub + Wheel Adapter
ECO-001, ECO-002
Coordinate: X+ Forward, Y+ Left, Z+ Up (CDS-03A, ECO-002)
Hip Roll center = origin (0, 0, 0) in this assembly's local frame.
"""
import FreeCAD as App
import Part
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import FCSTD_DIR
import config_params as P

doc = App.newDocument("LegAsm")

hr_h = P.HIP_ROLL_BASE_H     # 42mm
hp_h = P.HIP_PITCH_BASE_H    # 35mm
kn_h = P.KNEE_BASE_H         # 35mm
calf_l = P.CARBON_LENGTH_VISIBLE  # 120mm

# ── Hip Roll Base ──────────────────────────────────────
hr_base = doc.addObject("Part::Feature", "HipRollBase")
hr_base.Shape = Part.makeBox(P.HIP_ROLL_BASE_W, P.HIP_ROLL_BASE_D, P.HIP_ROLL_BASE_H)
hr_base.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

# ── Hip Pitch Base ─────────────────────────────────────
hp_z = hr_h + hp_h / 2
hp_base = doc.addObject("Part::Feature", "HipPitchBase")
hp_base.Shape = Part.makeBox(P.HIP_PITCH_BASE_W, P.HIP_PITCH_BASE_D, P.HIP_PITCH_BASE_H)
hp_base.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, hp_z),
    App.Rotation(0, 0, 0))

# ── Knee Base ──────────────────────────────────────────
kn_z = hp_z + hp_h / 2 + kn_h / 2
kn_base = doc.addObject("Part::Feature", "KneeBase")
kn_base.Shape = Part.makeBox(P.KNEE_BASE_W, P.KNEE_BASE_D, P.KNEE_BASE_H)
kn_base.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, kn_z),
    App.Rotation(0, 0, 0))

# ── Calf Tube (hollow carbon fiber, OD10 x ID8) ────────
calf_z = kn_z + kn_h / 2 + calf_l / 2
calf_outer = doc.addObject("Part::Feature", "CalfTubeOuter")
calf_outer.Shape = Part.makeCylinder(P.CARBON_OD / 2, calf_l)
calf_bore = doc.addObject("Part::Feature", "CalfTubeBore")
calf_bore.Shape = Part.makeCylinder(P.CARBON_ID / 2, calf_l + 2)
calf.Shape = calf_outer.Shape.cut(calf_bore.Shape)
calf.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, calf_z),
    App.Rotation(0, 0, 0))

# ── Wheel Adapter Plate ────────────────────────────────
# 4 x M3 bolt pattern (per CDS-06 §5: 4xM3 rigid mount)
wheel_z = calf_z + calf_l / 2 + P.WHEEL_DIAMETER / 2
wheel_adapter = doc.addObject("Part::Feature", "WheelAdapter")
wheel_adapter.Shape = Part.makeCylinder(P.WHEEL_DIAMETER / 2 + 5.0, 15.0)
hub_cyl = Part.makeCylinder(8.0, 18.0)
wheel_adapter.Shape = wheel_adapter.Shape.cut(hub_cyl)
bolt_circle_d = 30.0
bolt_d = 3.0
for i in range(4):
    ang = i * math.pi / 2
    bx = bolt_circle_d / 2 * math.cos(ang)
    by = bolt_circle_d / 2 * math.sin(ang)
    bh = Part.makeCylinder(bolt_d / 2, 20.0, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
    wheel_adapter.Shape = wheel_adapter.Shape.cut(bh)
wheel_adapter.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, wheel_z),
    App.Rotation(App.Vector(1, 0, 0), 90))

# ── Wheel Hub (press-fit to motor shaft, clamp screw) ──
# CDS-06 §7: ID=20mm, OD=32mm, H=18mm
hub_h = 18.0
wheel_hub = doc.addObject("Part::Feature", "WheelHub")
wheel_hub.Shape = Part.makeCylinder(32.0 / 2, hub_h, App.Vector(0, 0, 0))
shaft_bore = Part.makeCylinder(20.0 / 2, hub_h + 2, App.Vector(0, 0, -1))
wheel_hub.Shape = wheel_hub.Shape.cut(shaft_bore)
# Anti-slip teeth (6 grooves)
groove_depth = 1.0
groove_width = 2.0
for i in range(6):
    angle = i * 2 * math.pi / 6
    gx = (10.0 - groove_depth / 2) * math.cos(angle)
    gy = (10.0 - groove_depth / 2) * math.sin(angle)
    groove = Part.makeBox(groove_width, groove_width, hub_h + 2,
                          App.Vector(gx - groove_width / 2, gy - groove_width / 2, -1))
    wheel_hub.Shape = wheel_hub.Shape.cut(groove)
# Clamp screw holes (2 x M3, side clamping)
for dy in [-8, 8]:
    screw_hole = Part.makeCylinder(3.2 / 2, hub_h + 4, App.Vector(0, dy, 0), App.Vector(0, 1, 0))
    wheel_hub.Shape = wheel_hub.Shape.cut(screw_hole)
# Ridge on outer face for wheel centering
ridge = Part.makeCylinder(28.0 / 2, 2.0, App.Vector(0, 0, hub_h / 2 - 1.0))
wheel_hub.Shape = wheel_hub.Shape.fuse(ridge)
wheel_hub.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, wheel_z + 15.0),
    App.Rotation(App.Vector(1, 0, 0), 90))

# ── Assemble Leg ───────────────────────────────────────
leg_shape = hr_base.Shape.fuse(hp_base.Shape).fuse(kn_base.Shape).fuse(calf.Shape).fuse(wheel_adapter.Shape).fuse(wheel_hub.Shape)
leg_asm = doc.addObject("Part::Feature", "LegAsm")
leg_asm.Shape = leg_shape

doc.recompute()
out = os.path.join(FCSTD_DIR, "leg_asm.fcstd")
doc.saveCopy(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] leg_asm.fcstd -> {out}")
