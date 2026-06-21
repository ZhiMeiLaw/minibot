"""
Hip Roll Output / Fork (V6-PRT-0002)
Mini-Atlas V6 Alpha
50 x 50 x 35 mm | fork type | shaft Ø8.10mm slip fit | clamp gap 2mm
Hip Roll axis: X direction
Ref: CDS-03B, ECO-003
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

doc = App.newDocument("HipRollOutput")

# Main body - fork structure
W, D, H = P.HIP_ROLL_OUTPUT_W, P.HIP_ROLL_OUTPUT_D, P.HIP_ROLL_OUTPUT_H
x_ctr = W / 2
z_ctr = H / 2

body = doc.addObject("Part::Feature", "Body")
body.Shape = Part.makeBox(W, D, H)

# Fork cuts - create gap for rotation around X axis
gap = P.CLAMP_GAP
arm_t = 4.0

# Create two arms (top and bottom) with gap in between
# The fork allows rotation around X axis
y1 = -H/2 + gap/2
y2 = H/2 - gap/2

# Cut material to create fork gap
cut1 = Part.makeBox(W, arm_t, H + 2, App.Vector(-W/2, y1, -1))
cut2 = Part.makeBox(W, arm_t, H + 2, App.Vector(-W/2, y2, -1))
body.Shape = body.Shape.cut(cut1).cut(cut2)

# Shaft hole - along X axis (roll axis)
shaft_d = P.SHAFT_D + 0.1  # Slip fit
shaft_hole = Part.makeCylinder(shaft_d / 2, W + 4, App.Vector(-2, 0, z_ctr), App.Vector(1, 0, 0))
body.Shape = body.Shape.cut(shaft_hole)

# Carbon tube clamp - along Z- direction (downward)
clamp_w = 18.0
clamp_d = P.CARBON_OD + 4 * 2
clamp_h = P.CARBON_LENGTH_VISIBLE + 15

# Position at bottom of part, extending downward
clamp = Part.makeBox(clamp_w, clamp_d, clamp_h, 
                      App.Vector(x_ctr - clamp_w/2, -clamp_d/2, -clamp_h))
body.Shape = body.Shape.fuse(clamp)

# Carbon tube insert hole - along Z direction
carbon_insert = Part.makeCylinder(P.CARBON_OD / 2 + 0.2, P.CARBON_LENGTH_VISIBLE + 20,
                                   App.Vector(x_ctr, 0, -P.CARBON_LENGTH_VISIBLE - 5), 
                                   App.Vector(0, 0, 1))
body.Shape = body.Shape.cut(carbon_insert)

# Clamp split gap
clamp_split = Part.makeBox(P.CLAMP_GAP, clamp_d + 4, clamp_w + 4,
                            App.Vector(x_ctr - P.CLAMP_GAP/2, -clamp_d/2 - 2, -clamp_h/2))
body.Shape = body.Shape.cut(clamp_split)

# Clamp screws - M3
m3_d = 3.2
for dy in [-5, 5]:
    sc = Part.makeCylinder(m3_d / 2, 25,
                            App.Vector(x_ctr + clamp_w/2, dy, -clamp_h/2), App.Vector(1, 0, 0))
    body.Shape = body.Shape.cut(sc)

# Brass insert holes for torque module connection
brass_insert_d = 4.4
brass_depth = 5.0
pcd = 18.0
for i in range(4):
    ang = math.pi / 4 + i * math.pi / 2
    bx = pcd / 2 * math.cos(ang)
    by = pcd / 2 * math.sin(ang)
    ins = Part.makeCylinder(brass_insert_d / 2, brass_depth + 2, 
                             App.Vector(x_ctr + bx, by, z_ctr - 1), App.Vector(0, 0, 1))
    body.Shape = body.Shape.cut(ins)

# Structural ribs
rib_t = 3.0
for dy_sgn in [-1, 1]:
    dy = dy_sgn * 12
    rib = Part.makeBox(rib_t, 15, H * 0.5,
                        App.Vector(x_ctr - rib_t/2, dy - 7.5, H * 0.25))
    body.Shape = body.Shape.fuse(rib)

doc.recompute()
out = os.path.join(STL_DIR, "hip_roll_output.stl")
mesh = Mesh.Mesh()
MeshPart.meshFromShape(body.Shape, LinearDeflection=0.05, AngularDeflection=0.05, mesh=mesh)
mesh.write(out)
_doc_name = doc.Name if hasattr(doc, 'Name') else doc.Label
App.closeDocument(_doc_name)
print(f"[OK] hip_roll_output.stl -> {out}")