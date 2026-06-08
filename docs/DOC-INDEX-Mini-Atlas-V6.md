# Mini-Atlas V6

# DOC-INDEX-Mini-Atlas-V6

Version: 1.0

Status: Alpha Complete

Last Update:

After VAL-009 Beta Release Review

---

# 1. Project Overview

Project Name

Mini-Atlas V6

---

Platform

Hybrid Wheel-Leg Humanoid

---

Height

55 cm

---

Target Weight

4~5 kg

---

Primary Controller

ESP32

---

Actuator

STS3046 UART Servo

---

Manufacturing

FDM 3D Printing

---

Status

Alpha Complete

Beta Ready

---

# 2. Document Status Legend

| Status    | Meaning             |
| --------- | ------------------- |
| DRAFT     | Under Development   |
| REVIEW    | In Review           |
| APPROVED  | Approved            |
| FROZEN    | Frozen              |
| VALIDATED | Verified by Testing |

---

# 3. Mechanical Design Specifications

Directory

```text
/MDS
```

| Document                    | Status |
| --------------------------- | ------ |
| MDS-001 System Requirements | FROZEN |
| MDS-002 Joint Requirements  | FROZEN |

---

# 4. Electrical Design Specifications

Directory

```text
/EDS
```

| Document                       | Status  |
| ------------------------------ | ------- |
| EDS-01 Electrical Architecture | FROZEN  |
| EDS-02 Power Budget            | UPDATED |
| EDS-03 Servo Bus Architecture  | FROZEN  |
| EDS-04 Power Architecture      | UPDATED |

---

# 5. Design Reviews

Directory

```text
/DR
```

| Document                                  | Status   |
| ----------------------------------------- | -------- |
| DR-001 System Architecture Review         | APPROVED |
| DR-002 Actuator Selection Review          | APPROVED |
| DR-003 Joint Architecture Review          | APPROVED |
| DR-004 Hip Architecture Review            | APPROVED |
| DR-005 Servo Capability Review            | APPROVED |
| DR-006 Bearing and Shaft Review           | APPROVED |
| DR-007 Manufacturing Strategy Review      | APPROVED |
| DR-008 Printable Design Review            | APPROVED |
| DR-009 Knee Architecture Review           | APPROVED |
| DR-010 Leg Subsystem Review               | APPROVED |
| DR-012 Leg Kinematics & Torque Validation | APPROVED |

---

# 6. CAD Design Specifications

Directory

```text
/CDS
```

## Standard Library

| Document                                 | Status |
| ---------------------------------------- | ------ |
| CDS-02A Standard Component Library Rev A | FROZEN |

---

## Hip Roll

| Document                                          | Status |
| ------------------------------------------------- | ------ |
| CDS-03 Hip Roll Joint CAD Design                  | FROZEN |
| CDS-03A HipRoll Base CAD Design                   | FROZEN |
| CDS-03B HipRoll Output CAD Design                 | FROZEN |
| CDS-03C HipRoll Torque Transfer Module CAD Design | FROZEN |
| CDS-03D Hip Roll Assembly Verification            | FROZEN |

---

## Hip Pitch

| Document                                           | Status |
| -------------------------------------------------- | ------ |
| CDS-04 HipPitch Joint CAD Design                   | FROZEN |
| CDS-04A HipPitch Base CAD Design                   | FROZEN |
| CDS-04B HipPitch Output CAD Design                 | FROZEN |
| CDS-04C HipPitch Torque Transfer Module CAD Design | FROZEN |
| CDS-04D HipPitch Assembly Verification             | FROZEN |

---

## Knee

| Document                                       | Status |
| ---------------------------------------------- | ------ |
| CDS-05 Knee Joint CAD Design                   | FROZEN |
| CDS-05A Knee Base CAD Design                   | FROZEN |
| CDS-05B Knee Output CAD Design                 | FROZEN |
| CDS-05C Knee Torque Transfer Module CAD Design | FROZEN |
| CDS-05D Knee Assembly Verification             | FROZEN |

---

## System Integration

| Document                               | Status |
| -------------------------------------- | ------ |
| CDS-06 Wheel Module Architecture       | FROZEN |
| CDS-07 Full Leg Subsystem Integration  | FROZEN |
| CDS-08 Dual Leg and Pelvis Integration | FROZEN |
| CDS-09 Full Body Integration           | FROZEN |

---

# 7. System Reviews

Directory

```text
/SR
```

| Document                       | Status   |
| ------------------------------ | -------- |
| SR-001 System Weight Budget    | APPROVED |
| SR-002 Real World Power Budget | APPROVED |

---

# 8. Manufacturing

Directory

```text
/MP
```

| Document                             | Status |
| ------------------------------------ | ------ |
| MP-001 Manufacturing Package Release | FROZEN |

---

# 9. Firmware

Directory

```text
/FW
```

| Document                     | Status |
| ---------------------------- | ------ |
| FW-001 Firmware Architecture | FROZEN |
| FW-002 Servo Bus Driver      | FROZEN |
| FW-003 IMU Driver            | FROZEN |
| FW-004 Wheel Control         | FROZEN |
| FW-005 Gait Engine           | FROZEN |
| FW-006 Safety Manager        | FROZEN |
| FW-007 Telemetry & Logging   | FROZEN |
| FW-008 Bring-Up Software     | FROZEN |

---

# 10. Validation

Directory

```text
/VAL
```

| Document                         | Status    |
| -------------------------------- | --------- |
| VAL-001 Mechanical Validation    | VALIDATED |
| VAL-002 Electrical Validation    | VALIDATED |
| VAL-003 Power System Validation  | VALIDATED |
| VAL-004 Servo System Validation  | VALIDATED |
| VAL-005 Gait Validation          | VALIDATED |
| VAL-006 Safety System Validation | VALIDATED |
| VAL-007 Endurance Test           | VALIDATED |
| VAL-008 Battery Life Test        | VALIDATED |
| VAL-009 Beta Release Review      | VALIDATED |

---

# 11. Prototype Releases

Directory

```text
/PR
```

| Document                       | Status   |
| ------------------------------ | -------- |
| PR-001 Alpha Prototype Release | RELEASED |

---

# 12. Beta Program

Directory

```text
/BETA
```

| Document                           | Status  |
| ---------------------------------- | ------- |
| BP-001 Beta Prototype Release      | PLANNED |
| BP-002 Beta Manufacturing Plan     | PLANNED |
| BP-003 Beta Assembly Guide         | PLANNED |
| BP-004 Beta Bring-Up Procedure     | PLANNED |
| BP-005 Beta Test Plan              | PLANNED |
| BP-006 Beta Issue Tracking         | PLANNED |
| BP-007 Beta Freeze Review          | PLANNED |
| BP-008 V1.0 Release Recommendation | PLANNED |

---

# 13. Alpha Completion Summary

Mechanical Architecture

COMPLETE

---

Electrical Architecture

COMPLETE

---

Firmware Architecture

COMPLETE

---

CAD Design

COMPLETE

---

Manufacturing Package

COMPLETE

---

Validation Package

COMPLETE

---

Alpha Status

COMPLETE

---

Beta Status

READY

---

# 14. Next Milestone

Next Document

```text
BP-001-Beta-Prototype-Release.md
```

Purpose

Transition From

Alpha Validation

↓

Beta Engineering Verification
