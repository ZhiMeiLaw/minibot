"""
Full Body Assembly
Mini-Atlas V6 Alpha
Pelvis (120x80x60) + 2x Leg (100mm hip center distance) + 2x Wheel
ECO-001
Coordinate: X+ Forward, Y+ Left, Z+ Up (CDS-03A, ECO-002)
Origin: Pelvis bottom-center (z=0 at ground contact level)
Hip center distance: 100mm (Y: left=-50, right=+50) — ECO-002
"""
import FreeCAD as App
import Part
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import FCSTD_DIR
import config_params as P

doc = App.newDocument("FullBodyAsm")

pelvis = doc.addObject("Part::Feature", "Pelvis")
pelvis.Shape = Part.makeBox(P.PELVIS_W, P.PELVIS_D, P.PELVIS_H)
pelvis.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

hr_h  = P.HIP_ROLL_BASE_H
hp_h  = P.HIP_PITCH_BASE_H
kn_h  = P.KNEE_BASE_H
calf_l = P.CARBON_LENGTH_VISIBLE
wheel_r = P.WHEEL_DIAMETER / 2

def make_leg(doc, y_offset, leg_name):
    leg = doc.addObject("Part::Feature", f"Leg_{leg_name}")

    l_hr  = Part.makeBox(P.HIP_ROLL_BASE_W, P.HIP_ROLL_BASE_D, P.HIP_ROLL_BASE_H)
    l_hp  = Part.makeBox(P.HIP_PITCH_BASE_W, P.HIP_PITCH_BASE_D, P.HIP_PITCH_BASE_H)
    l_kn  = Part.makeBox(P.KNEE_BASE_W, P.KNEE_BASE_D, P.KNEE_BASE_H)
    # Solid calf tube (not hollow)
    l_calf = Part.makeCylinder(P.CARBON_OD / 2, calf_l)
    # Wheel: matching wheel_adapter geometry (OD+5, hub bore)
    l_wheel = Part.makeCylinder(P.WHEEL_DIAMETER / 2 + 5.0, 15.0)
    hub = Part.makeCylinder(8.0, 18.0)
    l_wheel = l_wheel.cut(hub)
    bolt_circle_d = 30.0
    bolt_d = 3.0
    for i in range(6):
        ang = i * math.pi / 3
        bx = bolt_circle_d / 2 * math.cos(ang)
        by = bolt_circle_d / 2 * math.sin(ang)
        bh = Part.makeCylinder(bolt_d / 2, 20.0, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
        l_wheel = l_wheel.cut(bh)

    # Corrected Y: flip sign (full_body Y is opposite of leg local Y)
    base_y = y_offset

    # Z reference: z_hr = center of Hip Roll base (hip roll axis)
    # = pelvis top surface + hr_h/2
    # = PELVIS_H + HIP_ROLL_BASE_H/2  (hip roll axis at midpoint of hip roll base)
    z_hr = P.PELVIS_H + hr_h / 2

    # Corrected Z stacking: use joint H (height), not D (depth)
    # hip pitch base is stacked ABOVE hip roll center, not beside it
    z_hp   = z_hr + hr_h / 2 + hp_h / 2
    z_kn   = z_hp  + hp_h / 2 + kn_h / 2
    z_calf = z_kn  + kn_h / 2 + calf_l / 2
    z_wheel = z_calf + calf_l / 2 + wheel_r

    hr_pl = App.Placement(App.Vector(0, base_y, z_hr - hr_h / 2), App.Rotation(0, 0, 0))
    hp_pl = App.Placement(App.Vector(P.HIP_PITCH_FORWARD_OFFSET, base_y + P.HIP_PITCH_LATERAL_OFFSET,
                                       z_hp - hp_h / 2), App.Rotation(0, 0, 0))
    kn_pl = App.Placement(App.Vector(P.HIP_PITCH_FORWARD_OFFSET, base_y + P.HIP_PITCH_LATERAL_OFFSET,
                                       z_kn - kn_h / 2), App.Rotation(0, 0, 0))
    calf_pl = App.Placement(App.Vector(P.HIP_PITCH_FORWARD_OFFSET, base_y + P.HIP_PITCH_LATERAL_OFFSET,
                                         z_calf - calf_l / 2), App.Rotation(0, 0, 0))
    wh_pl = App.Placement(App.Vector(P.HIP_PITCH_FORWARD_OFFSET, base_y + P.HIP_PITCH_LATERAL_OFFSET,
                                       z_wheel), App.Rotation(App.Vector(1, 0, 0), 90))

    return Part.Compound([
        l_hr.transformed(hr_pl.toMatrix()),
        l_hp.transformed(hp_pl.toMatrix()),
        l_kn.transformed(kn_pl.toMatrix()),
        l_calf.transformed(calf_pl.toMatrix()),
        l_wheel.transformed(wh_pl.toMatrix()),
    ])

# ECO-002: Hip Roll center at Y=±50mm (hip center distance = 100mm)
# Y+ = Left, so left leg at Y=-50, right leg at Y=+50
leg_left  = make_leg(doc, -P.HIP_CENTER_DISTANCE / 2, "Left")
leg_right = make_leg(doc,  P.HIP_CENTER_DISTANCE / 2, "Right")

asm_obj = doc.addObject("Part::Feature", "FullBodyAsm")
asm_obj.Shape = Part.Compound([pelvis.Shape, leg_left, leg_right])

doc.recompute()
out = os.path.join(FCSTD_DIR, "full_body_asm.fcstd")
doc.saveCopy(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] full_body_asm.fcstd -> {out}")