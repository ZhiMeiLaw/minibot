# ECO-002-Coordinate-System-Freeze.md

Version: 1.0

Status: APPROVED

Subsystem:

Mini-Atlas V6 Alpha

Category:

Mechanical Coordinate Definition

Purpose:

Freeze all coordinate systems used by CAD, Assembly, Firmware, Simulation, and Manufacturing.

This document becomes the single authoritative coordinate reference for the project.

---

# 1. Scope

Applies to:

* MDS Documents
* CDS Documents
* DR Documents
* FreeCAD Models
* STEP Files
* STL Files
* URDF Models
* Firmware Kinematics
* Simulation Models

---

# 2. Global Coordinate System

Robot Coordinate System (RCS)

Right-Hand Coordinate System

Definition:

X Axis

Left ↔ Right

Positive Direction:

Robot Right

Negative Direction:

Robot Left

---

Y Axis

Front ↔ Back

Positive Direction:

Robot Front

Negative Direction:

Robot Rear

---

Z Axis

Up ↔ Down

Positive Direction:

Up

Negative Direction:

Ground

---

# 3. Robot Origin

Reference Name:

RCS_ORIGIN

Location:

Midpoint between left and right Hip Roll axes.

Projection:

Located on Hip Roll axis plane.

Coordinates:

(0,0,0)

Status:

Frozen

---

# 4. Pelvis Coordinate System

Reference Name:

PCS

Origin:

Same as RCS_ORIGIN

Axis Alignment:

PCS == RCS

No rotation allowed.

Status:

Frozen

---

# 5. Hip Roll Axis Definition

Left Hip Roll Axis:

X = -50 mm

Y = 0 mm

Z = 0 mm

---

Right Hip Roll Axis:

X = +50 mm

Y = 0 mm

Z = 0 mm

---

Hip Center Distance:

100 mm

Status:

Frozen

---

# 6. Hip Pitch Axis Definition

Reference:

Hip Roll Axis

Offset Direction:

+Y

Offset Distance:

15 mm

Coordinates:

Left Hip Pitch:

(-50, +15, 0)

Right Hip Pitch:

(+50, +15, 0)

Status:

Frozen

---

# 7. Thigh Coordinate System

Reference:

Hip Pitch Axis

Primary Direction:

-Z

Meaning:

Thigh extends downward from Hip Pitch.

Status:

Frozen

---

# 8. Knee Axis Definition

Reference:

End of Thigh Module

Axis Direction:

Parallel to Hip Pitch Axis

Status:

Frozen

---

# 9. Shank Coordinate System

Reference:

Knee Axis

Primary Direction:

-Z

Meaning:

Shank extends downward toward Foot.

Status:

Frozen

---

# 10. Foot Coordinate System

Origin:

Center of Foot Contact Patch

X:

Left ↔ Right

Y:

Toe ↔ Heel

Positive Y:

Toe Direction

Z:

Up

Status:

Frozen

---

# 11. Carbon Tube Direction Convention

All structural tubes:

Primary Axis:

-Z

Insertion Reference:

Parent Joint

Direction:

Toward Ground

Status:

Frozen

---

# 12. FreeCAD Mapping Rules

FreeCAD Model Origin:

Must match PCS origin.

Part Placement:

Relative to PCS.

No arbitrary local coordinate definitions allowed.

Status:

Mandatory

---

# 13. URDF Mapping Rules

URDF Base Link:

Pelvis Frame

URDF Origin:

PCS Origin

All joint transforms shall reference PCS.

Status:

Mandatory

---

# 14. Assembly Rules

Master Assembly Origin:

PCS Origin

Allowed Reference Features:

* Hip Roll Axis
* Hip Pitch Axis
* Carbon Tube Centerline

No other datum may be used as assembly master reference.

Status:

Mandatory

---

# 15. ECO Control

Any modification to:

* Axis location
* Axis orientation
* Coordinate definitions

Requires:

* ECO approval
* DR review
* CDS update
* URDF update

---

# 16. Approval

Document:

ECO-002

Status:

FROZEN

Authority:

Mini-Atlas Mechanical Architecture

Effective Immediately

---

END OF DOCUMENT
