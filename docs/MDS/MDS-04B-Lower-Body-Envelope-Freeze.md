# MDS-04B-Lower-Body-Envelope-Freeze.md

Version: 1.0

Status: FROZEN

Subsystem:

Mini-Atlas V6 Alpha Lower Body

Purpose:

Define the geometric envelope, packaging constraints, center-of-mass targets, and assembly clearances for all lower-body modules before CAD implementation.

---

# 1. Scope

This document freezes:

* Pelvis envelope
* Hip module envelope
* Thigh envelope
* Knee envelope
* Shank envelope
* Foot envelope
* Electronics volume allocation
* Mass distribution targets

This document does NOT define detailed CAD geometry.

Detailed geometry shall be defined in CDS documents.

---

# 2. Design Constraints

Reference:

MDS-04A Interface Freeze

Frozen Interfaces:

* 688 Bearing
* 698 Bearing
* Ø8 Shaft
* OD10 × ID8 Carbon Tube
* Hip Center Distance = 100 mm
* Hip Pitch Offset = 15 mm
* Wall Thickness = 4 mm

---

# 3. Overall Lower Body Envelope

Robot Configuration:

Mini-Atlas V6 Alpha

Target Height:

550 mm

Configuration:

Wheel Assisted Biped

Lower Body Total Height:

380 mm

Tolerance:

±10 mm

---

# 4. Pelvis Envelope

Envelope Type:

Outer Bounding Box

Dimensions:

Length (X):

120 mm

Width (Y):

70 mm

Height (Z):

60 mm

Status:

Frozen

---

# 5. Hip Roll Geometry

Left Hip Roll Axis

Right Hip Roll Axis

Center Distance:

100 mm

Tolerance:

±0.5 mm

Axis Height Reference:

Pelvis Mid Plane

Status:

Frozen

---

# 6. Hip Pitch Geometry

Axis Offset:

15 mm

Reference:

Hip Roll Axis

Direction:

Forward

Status:

Frozen

---

# 7. Thigh Envelope

Structure:

Carbon Tube + Printed End Connectors

Carbon Tube:

OD10 × ID8

Nominal Length:

120 mm

Envelope:

140 mm × 40 mm × 40 mm

Status:

Frozen

---

# 8. Knee Module Envelope

Envelope Type:

Bounding Box

Dimensions:

50 mm × 40 mm × 50 mm

Bearing:

688 × 2

Output Shaft:

Ø8 mm

Status:

Frozen

---

# 9. Shank Envelope

Structure:

Carbon Tube + Printed End Connectors

Carbon Tube:

OD10 × ID8

Nominal Length:

120 mm

Envelope:

140 mm × 40 mm × 40 mm

Status:

Frozen

---

# 10. Foot Envelope

Dimensions:

Length:

100 mm

Width:

60 mm

Height:

25 mm

Ground Contact Area:

100 mm × 60 mm

Status:

Frozen

---

# 11. Electronics Envelope

Location:

Inside Pelvis

Available Volume:

112 mm × 62 mm × 52 mm

Reserved Components:

* ESP32
* IMU
* Servo Bus Interface
* Power Distribution Board

Battery:

External Backpack Mount

Status:

Frozen

---

# 12. Center of Mass Targets

Static CoM Target:

5 mm anterior to Hip Roll centerline

Lateral Offset:

0 mm

Vertical Target:

30 mm above Hip Roll axis

Purpose:

Improve passive stability

Status:

Frozen

---

# 13. Assembly Clearance Rules

Minimum Bearing Clearance:

1.0 mm

Minimum Servo Clearance:

2.0 mm

Minimum Wiring Channel Width:

8.0 mm

Minimum Fastener Access Gap:

6.0 mm

Status:

Frozen

---

# 14. Printer Constraints

Target Printer:

Bambu A1 Mini

Build Volume:

180 × 180 × 180 mm

Requirement:

All individual printed parts must fit inside build volume without segmentation.

Status:

Frozen

---

# 15. Future ECO Control

Changes to any frozen envelope dimensions shall require:

* ECO approval
* DR review
* BOM impact assessment
* CDS update

---

# 16. Downstream Dependencies

This document is the sole dimensional authority for:

* CDS-06A Pelvis Frame CAD
* CDS-06B Pelvis Assembly
* PF-001.py
* PF-002.py
* Lower Body Assembly Models
* BOM Mechanical Packaging

---

# 17. Approval

Status:

FROZEN

Release:

Mini-Atlas V6 Alpha

Document Authority:

MDS-04B

---

END OF DOCUMENT
