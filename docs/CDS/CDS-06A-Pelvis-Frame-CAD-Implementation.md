# CDS-06A-Pelvis-Frame-CAD-Implementation.md

Version: 1.0

Status: RELEASED

Subsystem:

Pelvis Frame

Document Type:

CAD Design Specification

Reference Documents:

* MDS-04A Interface Freeze
* MDS-04B Lower Body Envelope Freeze
* ECO-001 Lightweight Architecture Migration
* ECO-002 Coordinate System Freeze

Purpose:

Define the complete CAD implementation requirements for the Pelvis Frame Generator (PF-001.py).

---

# 1. Scope

This document defines:

* Pelvis frame geometry
* Structural interfaces
* Mounting interfaces
* Carbon tube interfaces
* Electronics interfaces
* Fastener interfaces

This document does not define manufacturing procedures.

Manufacturing procedures are defined in MP-series documents.

---

# 2. Coordinate Reference

Coordinate System:

PCS (Pelvis Coordinate System)

Reference:

ECO-002

Origin:

Midpoint between left and right Hip Roll axes

Coordinates:

(0,0,0)

---

# 3. Outer Envelope

## Frozen Dimensions

Pelvis Span (X)

120 mm

---

Pelvis Depth (Y)

70 mm

---

Pelvis Height (Z)

60 mm

---

Envelope Status

Frozen

---

# 4. Structural Layout

Pelvis frame shall be composed of:

* left side plate
* right side plate
* front cross member
* rear cross member
* electronics deck

---

# 5. Wall Thickness

Nominal:

4.0 mm

Material:

PETG

Tolerance:

±0.2 mm

---

# 6. Hip Roll Mounts

## Quantity

2

---

## Axis Locations

Left:

(-50,0,0)

Right:

(+50,0,0)

---

## Bearing

688

Dimensions:

8×16×5 mm

---

## Bearing Pocket

Nominal Bore:

16.0 mm

Pocket Depth:

5.2 mm

Fit:

Light Press Fit

---

# 7. Hip Pitch Mounts

## Quantity

2

---

## Axis Locations

Left:

(-50,+15,0)

Right:

(+50,+15,0)

---

## Bearing

698

Dimensions:

8×19×6 mm

---

## Bearing Pocket

Nominal Bore:

19.0 mm

Pocket Depth:

6.2 mm

Fit:

Light Press Fit

---

# 8. Carbon Tube Interfaces

## Tube Standard

OD10 × ID8

---

## Quantity

2

---

## Insertion Depth

15 mm minimum

---

## Retention

Double Clamp

M3 Fasteners

---

# 9. Electronics Deck

Location:

Upper Pelvis Interior

Reserved Volume:

80 mm × 50 mm

---

## Components

ESP32

IMU

Power Distribution Board

UART Servo Hub

---

# 10. Fastener Standard

Primary Fastener:

M3 Socket Head Cap Screw

---

Insert Type:

M3 Brass Heat Set Insert

---

Supported Lengths:

6 mm

8 mm

12 mm

---

# 11. Wiring Requirements

Minimum Wiring Channel Width:

8 mm

---

Servo Cable Routing:

Internal

---

Power Routing:

Separated from signal routing

---

# 12. Serviceability

Servo Replacement Time:

< 5 minutes

---

Bearing Replacement Time:

< 10 minutes

---

Carbon Tube Replacement Time:

< 5 minutes

---

# 13. Printer Constraints

Target Printer:

Bambu A1 Mini

---

Maximum Part Size:

180 × 180 × 180 mm

---

Pelvis Frame:

Single Print

No Segmentation Allowed

---

# 14. CAD Parameter Mapping

PF-001.py shall expose:

PELVIS_SPAN

PELVIS_DEPTH

PELVIS_HEIGHT

HIP_CENTER_DISTANCE

HIP_PITCH_OFFSET

WALL_THICKNESS

TUBE_OD

TUBE_ID

---

# 15. Deliverables

The following outputs shall be generated:

PF-001.FCStd

PF-001.step

PF-001.stl

---

# 16. Verification

Verification Documents:

VAL-001

VAL-002

VAL-004

---

# 17. Approval

Status:

RELEASED

Authority:

Mini-Atlas Mechanical Architecture

---

END OF DOCUMENT
