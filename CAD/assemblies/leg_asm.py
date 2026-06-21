"""
Leg Assembly (Single Leg)
Mini-Atlas V6 Alpha
HipRoll + HipPitch (35mm lateral, 15mm forward) + Knee + Calf + Wheel
ECO-001
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

hr_base = doc.addObject("Part::Feature", "HipRollBase")
hr_base.Shape = Part.makeBox(P.HIP_ROLL_BASE_W, P.HIP_ROLL_BASE_D, P.HIP_ROLL_BASE_H)
hr_base.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

# ECO-002: Hip Pitch offset 35mm lateral (Y+), 15mm forward (X+)
# Corrected Z stacking: use joint H (height) not D (depth)
hp_z = hr_h + hp_h / 2
hp_base = doc.addObject("Part::Feature", "HipPitchBase")
hp_base.Shape = Part.makeBox(P.HIP_PITCH_BASE_W, P.HIP_PITCH_BASE_D, P.HIP_PITCH_BASE_H)
hp_base.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, hp_z),
    App.Rotation(0, 0, 0))

# Knee: stacked on top of Hip Pitch base
kn_z = hp_z + hp_h / 2 + kn_h / 2
kn_base = doc.addObject("Part::Feature", "KneeBase")
kn_base.Shape = Part.makeBox(P.KNEE_BASE_W, P.KNEE_BASE_D, P.KNEE_BASE_H)
kn_base.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, kn_z),
    App.Rotation(0, 0, 0))

# Calf tube: solid cylinder (not hollow), center at kn_z + kn_h/2 + calf_l/2
calf_z = kn_z + kn_h / 2 + calf_l / 2
calf = doc.addObject("Part::Feature", "CalfTube")
calf.Shape = Part.makeCylinder(P.CARBON_OD / 2, calf_l)
calf.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, calf_z),
    App.Rotation(0, 0, 0))

# Wheel: center at calf_z + calf_l/2 + WHEEL_DIAMETER/2 (corrected: use radius not hardcoded +5)
wheel_z = calf_z + calf_l / 2 + P.WHEEL_DIAMETER / 2
wheel = doc.addObject("Part::Feature", "WheelAdapter")
wheel.Shape = Part.makeCylinder(P.WHEEL_DIAMETER / 2 + 5.0, 15.0)
hub = Part.makeCylinder(8.0, 18.0)
wheel.Shape = wheel.Shape.cut(hub)
bolt_circle_d = 30.0
bolt_d = 3.0
for i in range(6):
    ang = i * math.pi / 3
    bx = bolt_circle_d / 2 * math.cos(ang)
    by = bolt_circle_d / 2 * math.sin(ang)
    bh = Part.makeCylinder(bolt_d / 2, 20.0, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
    wheel.Shape = wheel.Shape.cut(bh)
wheel.Placement = App.Placement(
    App.Vector(P.HIP_PITCH_FORWARD_OFFSET, P.HIP_PITCH_LATERAL_OFFSET, wheel_z),
    App.Rotation(App.Vector(1, 0, 0), 90))

leg_shape = hr_base.Shape.fuse(hp_base.Shape).fuse(kn_base.Shape).fuse(calf.Shape).fuse(wheel.Shape)
leg_asm = doc.addObject("Part::Feature", "LegAsm")
leg_asm.Shape = leg_shape

doc.recompute()
out = os.path.join(FCSTD_DIR, "leg_asm.fcstd")
doc.saveCopy(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] leg_asm.fcstd -> {out}")