"""
Full Body Assembly
Mini-Atlas V6 Alpha
Pelvis (120x80x60) + 2x Leg (100mm hip center distance) + 2x Wheel
ECO-001, ECO-002
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

    # Calf tube: hollow carbon fiber tube (OD10 x ID8), for wire routing
    l_calf_outer = Part.makeCylinder(P.CARBON_OD / 2, calf_l)
    l_calf_bore = Part.makeCylinder(P.CARBON_ID / 2, calf_l + 2)
    l_calf = l_calf_outer.cut(l_calf_bore)

    # Wheel adapter plate: 4 x M3 bolt pattern (per CDS-06 §5)
    l_wheel = Part.makeCylinder(P.WHEEL_DIAMETER / 2 + 5.0, 15.0)
    hub = Part.makeCylinder(8.0, 18.0)
    l_wheel = l_wheel.cut(hub)
    bolt_circle_d = 30.0
    bolt_d = 3.0
    for i in range(4):
        ang = i * math.pi / 2
        bx = bolt_circle_d / 2 * math.cos(ang)
        by = bolt_circle_d / 2 * math.sin(ang)
        bh = Part.makeCylinder(bolt_d / 2, 20.0, App.Vector(bx, by, -2), App.Vector(0, 0, 1))
        l_wheel = l_wheel.cut(bh)

    # Wheel Hub: press-fit to motor shaft, clamp screw secures to wheel
    # CDS-06 §7: ID=20mm, OD=32mm, H=18mm
    hub_h = 18.0
    l_wheel_hub = Part.makeCylinder(32.0 / 2, hub_h)
    shaft_bore = Part.makeCylinder(20.0 / 2, hub_h + 2, App.Vector(0, 0, -1))
    l_wheel_hub = l_wheel_hub.cut(shaft_bore)
    # Anti-slip teeth (6 grooves)
    for i in range(6):
        angle = i * 2 * math.pi / 6
        gx = (10.0 - 0.5) * math.cos(angle)
        gy = (10.0 - 0.5) * math.sin(angle)
        groove = Part.makeBox(2.0, 2.0, hub_h + 2, App.Vector(gx - 1.0, gy - 1.0, -1))
        l_wheel_hub = l_wheel_hub.cut(groove)
    # Clamp screw holes (2 x M3)
    for dy in [-8, 8]:
        screw_hole = Part.makeCylinder(3.2 / 2, hub_h + 4, App.Vector(0, dy, 0), App.Vector(0, 1, 0))
        l_wheel_hub = l_wheel_hub.cut(screw_hole)
    # Ridge for wheel centering
    ridge = Part.makeCylinder(28.0 / 2, 2.0, App.Vector(0, 0, hub_h / 2 - 1.0))
    l_wheel_hub = l_wheel_hub.fuse(ridge)

    # Corrected Y: flip sign (full_body Y is opposite of leg local Y)
    base_y = y_offset

    # Z reference: z_hr = center of Hip Roll base (hip roll axis)
    z_hr = P.PELVIS_H + hr_h / 2

    # Corrected Z stacking: use joint H (height), not D (depth)
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
    hub_pl = App.Placement(App.Vector(P.HIP_PITCH_FORWARD_OFFSET, base_y + P.HIP_PITCH_LATERAL_OFFSET,
                                       z_wheel + 15.0), App.Rotation(App.Vector(1, 0, 0), 90))

    return Part.Compound([
        l_hr.transformed(hr_pl.toMatrix()),
        l_hp.transformed(hp_pl.toMatrix()),
        l_kn.transformed(kn_pl.toMatrix()),
        l_calf.transformed(calf_pl.toMatrix()),
        l_wheel.transformed(wh_pl.toMatrix()),
        l_wheel_hub.transformed(hub_pl.toMatrix()),
    ])

# ECO-002: Hip Roll center at Y=±50mm (hip center distance = 100mm)
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
