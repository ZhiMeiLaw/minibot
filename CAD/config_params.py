"""
Mini-Atlas V6 Alpha — Frozen Design Parameters
Source: docs/ECO/ECO-001, CDS-02A, MDS-03, DR-012, ECO-003
Coordinate system: X+ Forward, Y+ Left, Z+ Up (ECO-002)
"""

MM = 1.0
DEGREE = 1.0

# ── Bearing System ──────────────────────────────────────────────────────────────
BEARING_HIP_ROLL = {"id": 8, "od": 16, "th": 5, "name": "688-2RS"}
BEARING_HIP_PITCH = {"id": 8, "od": 19, "th": 6, "name": "698-2RS"}
BEARING_KNEE = {"id": 8, "od": 19, "th": 6, "name": "698-2RS"}

POCKET_DEPTH_HIP_ROLL = 5.2
POCKET_DEPTH_HPK = 6.2
POCKET_D_HIP_ROLL = 16.05
POCKET_D_HPK = 19.05

# ── Shaft ──────────────────────────────────────────────────────────────────────
SHAFT_D = 8.0
SHAFT_TOL = "h7"  # Shaft tolerance chosen as h7 (machine-fit). Example for Ø8: h7 ~ 0 / -0.017..-0.020 mm (document in MP)
SHAFT_MATERIAL = "GCr15"

# ── Bearing Spacing ───────────────────────────────────────────────────────────
# ── Bearing Spacing (frozen per DR-012) ───────────────────────────────────────
# Engineering decision: set bearing spans to 30 mm.
# Rationale: With Ø8 shafts and 688/698 bearing family, 30 mm span:
#  - reduces shaft bending stress,
#  - increases torque-path stability,
#  - reduces micro-oscillation amplification in printed parts,
#  - better suits DR-012 high-utilization design.
BEARING_SPACING_HIP_ROLL = 30.0
BEARING_SPACING_HIP_PITCH = 30.0
BEARING_SPACING_KNEE = 30.0

# ── Hip Pitch Offset (from Hip Roll axis) ──────────────────────────────────────
# NOTE: Documentation (MDS-04B and CDS files) specify 15 mm as the hip pitch
# lateral offset (authoritative). Set to 15.0 to keep CAD assemblies consistent
# with interface freeze documents.
HIP_PITCH_LATERAL_OFFSET = 15.0
HIP_PITCH_FORWARD_OFFSET = 15.0

# ── Hip Roll Motion Range ─────────────────────────────────────────────────────
HIP_ROLL_RANGE_MIN = -25.0 * DEGREE
HIP_ROLL_RANGE_MAX = 25.0 * DEGREE
HIP_PITCH_RANGE_MIN = -30.0 * DEGREE
HIP_PITCH_RANGE_MAX = 60.0 * DEGREE
KNEE_RANGE_MIN = 0.0 * DEGREE
KNEE_RANGE_MAX = 120.0 * DEGREE

# ── Carbon Tube ────────────────────────────────────────────────────────────────
CARBON_OD = 10.0
CARBON_ID = 8.0
CARBON_LENGTH_TOTAL = 150.0
CARBON_LENGTH_VISIBLE = 120.0

# ── Servo (STS3046) ───────────────────────────────────────────────────────────
SERVO_NAME = "STS3046"
SERVO_POCKET_W = 48.0
SERVO_POCKET_H = 26.0
SERVO_POCKET_D = 37.0
SERVO_SCREW = "M2.5"
SERVO_SCREW_COUNT = 4

# ── Clamp ─────────────────────────────────────────────────────────────────────
CLAMP_GAP = 2.0
CLAMP_SCREW = "M3"
CLAMP_SCREW_LEN = 16.0
CLAMP_SCREW_COUNT_STD = 2
CLAMP_SCREW_COUNT_KNEE = 4

# ── Frame / Pelvis ─────────────────────────────────────────────────────────────
PELVIS_W = 120.0
PELVIS_D = 80.0
PELVIS_H = 60.0
PELVIS_WALL_T = 4.0

# ── Hip Mount Ear (ECO-003) ───────────────────────────────────────────────────
HIP_EAR_EXTENSION = 12.0
HIP_EAR_THICKNESS = 6.0
HIP_EAR_ROOT_FILLET = 3.0
HIP_EAR_RIB_THICKNESS = 4.0

# ── Hip Roll Joint ─────────────────────────────────────────────────────────────
HIP_ROLL_BASE_W = 70.0
HIP_ROLL_BASE_D = 60.0
HIP_ROLL_BASE_H = 42.0
HIP_ROLL_OUTPUT_W = 50.0
HIP_ROLL_OUTPUT_D = 50.0
HIP_ROLL_OUTPUT_H = 35.0

# ── Hip Pitch Joint ────────────────────────────────────────────────────────────
HIP_PITCH_BASE_W = 50.0
HIP_PITCH_BASE_D = 60.0
HIP_PITCH_BASE_H = 35.0
HIP_PITCH_OUTPUT_W = 50.0
HIP_PITCH_OUTPUT_D = 55.0
HIP_PITCH_OUTPUT_H = 35.0

# ── Knee Joint ─────────────────────────────────────────────────────────────────
KNEE_BASE_W = 50.0
KNEE_BASE_D = 60.0
KNEE_BASE_H = 35.0
KNEE_OUTPUT_W = 50.0
KNEE_OUTPUT_D = 60.0
KNEE_OUTPUT_H = 35.0

# ── Wheel ──────────────────────────────────────────────────────────────────────
WHEEL_DIAMETER = 80.0

# ── Materials ─────────────────────────────────────────────────────────────────
MATERIAL_FRAME = "Al7075-T6"
MATERIAL_SHAFT = "GCr15"
MATERIAL_BEARING = "SUJ2"
MATERIAL_CARBON = "CarbonFiber"
MATERIAL_SERVO = "STS3046"

# ── tolerances ──────────────────────────────────────────────────────────────────
## ── Tolerances ───────────────────────────────────────────────────────────────
# Default linear tolerance for FDM printed parts. Critical/ machined holes must
# explicitly use MACHINED_LINEAR_TOL or a tighter tolerance and be flagged for
# machining/reaming in manufacturing docs.
LINEAR_TOL = 0.20
MACHINED_LINEAR_TOL = 0.05
MACHINED_LINEAR_TOL_MAX = 0.10
ANGLE_TOL = 0.5

# ── Full Body ─────────────────────────────────────────────────────────────────
HIP_CENTER_DISTANCE = 100.0
