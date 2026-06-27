# Mini-Atlas V6

# DOC-INDEX Mini-Atlas V6

Version: 1.1

Status: Alpha Complete (Corrected)

Last Update: 2026-06-27 (ECO-002 Documentation Consistency Fix)

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

< 4 kg

---

Primary Controller

ESP32

---

Actuator

STS3046 UART Servo (6 units)

---

Wheel Motor

GB37-520 (2 units)

---

Battery

3S2P Samsung 30Q (3000mAh / 33.3Wh)

---

Manufacturing

FDM 3D Printing (PETG)

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
| RELEASED  | Released for Build  |
| PLANNED   | Scheduled, Not Yet Started |

---

# 3. Mechanical Design Specifications

Directory

```text
/MDS
```

| Document                                | Status   |
| --------------------------------------- | -------- |
| MDS-01 System Architecture              | APPROVED |
| MDS-02 Detailed Joint Design            | APPROVED |
| MDS-03 Assembly Specification           | APPROVED |
| MDS-04 Pelvis & Electronics Assembly    | APPROVED |
| MDS-04A Interface Freeze Specification  | APPROVED |
| MDS-04B Lower Body Envelope Freeze      | APPROVED |
| SR-001 System Weight Budget             | APPROVED |
| SR-002 Real World Power Budget          | APPROVED |

> **ECO-002 变更**：编号由 MDS-001/002 修正为 MDS-01/02（与文件名一致）；SR-001/002 从 /SR 目录移至 /MDS 目录。

---

# 4. Electrical Design Specifications

Directory

```text
/EDS
```

| Document                                     | Status   |
| -------------------------------------------- | -------- |
| EDS-01 System Electrical Architecture        | APPROVED |
| EDS-02 Power Budget and Current Analysis     | APPROVED |
| EDS-03 Power Distribution and Protection     | APPROVED |
| EDS-04 Power Hardware Selection              | APPROVED |
| EDS-05 Communication and Control Architecture| APPROVED |

> **ECO-002 变更**：EDS-03 标题由 "Servo Bus Architecture" 修正为 "Power Distribution and Protection Design"；添加 EDS-04 Power Hardware Selection。

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
| DR-009A Knee Servo Orientation Review     | APPROVED |
| DR-010 Leg Subsystem Review               | APPROVED |
| DR-011 Ankle Architecture Review          | APPROVED |
| DR-012 Leg Kinematics & Torque Validation | REVIEW   |

---

# 6. CAD Design Specifications

Directory

```text
/CDS
```

## Standard Library

| Document                                 | Status |
| ---------------------------------------- | ------ |
| CDS-01 CAD Design Specification          | APPROVED |
| CDS-02 Standard Component Library        | APPROVED |
| CDS-06A Pelvis Frame CAD Implementation  | APPROVED |

---

## Hip Roll

| Document                                          | Status |
| ------------------------------------------------- | ------ |
| CDS-03 Hip Roll Joint CAD Design                  | APPROVED |
| CDS-03A HipRoll Base CAD Design                   | APPROVED |
| CDS-03B HipRoll Output CAD Design                 | APPROVED |
| CDS-03C HipRoll Torque Transfer Module CAD Design | APPROVED |
| CDS-03D Hip Roll Assembly Verification            | APPROVED |

---

## Hip Pitch

| Document                                           | Status |
| -------------------------------------------------- | ------ |
| CDS-04 HipPitch Joint CAD Design                   | APPROVED |
| CDS-04A HipPitch Base CAD Design                   | APPROVED |
| CDS-04B HipPitch Output CAD Design                 | APPROVED |
| CDS-04C HipPitch Torque Transfer Module CAD Design | APPROVED |
| CDS-04D HipPitch Assembly Verification             | APPROVED |

---

## Knee

| Document                                       | Status |
| ---------------------------------------------- | ------ |
| CDS-05A Knee Base CAD Design                   | APPROVED |
| CDS-05B Knee Output CAD Design                 | APPROVED |
| CDS-05C Knee Torque Transfer Module CAD Design | APPROVED |
| CDS-05D Knee Assembly Verification             | APPROVED |

---

## System Integration

| Document                               | Status |
| -------------------------------------- | ------ |
| CDS-06 Wheel Module Architecture       | APPROVED |
| CDS-07 Full Leg Subsystem Integration  | APPROVED |
| CDS-08 Dual Leg and Pelvis Integration | REVIEW |
| CDS-09 Full Body Integration           | REVIEW |

---

## CAD Documentation (FreeCAD Automation)

| Document                                                 | Status |
| -------------------------------------------------------- | ------ |
| CAD-001 FreeCAD Project Architecture                     | APPROVED |
| CAD-002 Standard Part Library                            | APPROVED |
| CAD-003 Robot Parameter System                           | APPROVED |
| CAD-004 Naming and Module Convention                     | APPROVED |
| CAD-005 Assembly and Build System                        | APPROVED |
| CAD-006 FreeCAD Python Kernel Implementation             | APPROVED |
| CAD-007 First End-to-End HipPitch Generation             | APPROVED |
| CAD-008 Automated Multi-Module Generation                | APPROVED |
| CAD-009 Full Lower Body Assembly Validation              | APPROVED |
| CAD-010 Full Body Dynamic Integration Readiness          | APPROVED |
| CAD-011 Dynamic Walking Pre-Architecture                 | PLANNED |
| CAD-012 Actuator Torque and Gait Feasibility             | PLANNED |
| CAD-013 Optimization and Redesign Loop                   | PLANNED |
| CAD-014 Walking Gait Prototype Design                    | PLANNED |
| CAD-015 Control System Architecture PreDesign            | PLANNED |
| CAD-016 Sensor and Feedback System Design                | PLANNED |
| CAD-017 Real Time Control Loop Integration               | PLANNED |
| CAD-018 System Simulation and Digital Twin               | PLANNED |
| CAD-019 Gait Optimization and Closed Loop Tuning         | PLANNED |
| CAD-020 Hardware Deployment and Physical Prototype Plan  | PLANNED |
| CAD-021 Prototype Build and Real World Test Protocol     | PLANNED |
| CAD-022 First Walking Event Analysis                     | PLANNED |
| CAD-023 Stable Walking Convergence                       | PLANNED |
| CAD-024 Robust Walking and External Disturbance Handling | PLANNED |
| CAD-025 System Integration and Field Deployment          | PLANNED |
| CAD-026 System Lifecycle and Iteration Framework         | PLANNED |
| CAD-027 Autonomous Design Optimization System            | PLANNED |
| CAD-028 Reinforcement Learning Gait and Structure Co-Optimization | PLANNED |
| CAD-029 Multi Robot Cooperative Learning System          | PLANNED |
| CAD-030 Full Autonomous Robotic Ecosystem Architecture   | PLANNED |

---

# 7. System Reviews

> **ECO-002 变更**：SR-001/002 已从 /MDS 目录下的独立文件移动到与 MDS 同级索引。

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

| Document                             | Status   |
| ------------------------------------ | -------- |
| MP-001 Manufacturing Package Release | RELEASED |

---

# 9. Firmware

Directory

```text
/FW
```

| Document                     | Status   |
| ---------------------------- | -------- |
| FW-001 Firmware Architecture | APPROVED |
| FW-002 Servo Bus Driver      | APPROVED |
| FW-003 IMU Driver            | APPROVED |
| FW-004 Wheel Control         | APPROVED |
| FW-005 Gait Engine           | APPROVED |
| FW-006 Safety Manager        | APPROVED |
| FW-007 OTA Framework         | APPROVED |
| FW-008 Bring-Up Software     | APPROVED |

> **ECO-002 变更**：FW-007 标题由 "Telemetry & Logging" 修正为 "OTA Framework"（实际文件名为 FW-007-OTA-Framework.md）。

---

# 10. Validation

Directory

```text
/VAL
```

| Document                         | Status    |
| -------------------------------- | --------- |
| VAL-001 Mechanical Validation    | DRAFT     |
| VAL-002 Electrical Validation    | DRAFT     |
| VAL-003 Power System Validation  | DRAFT     |
| VAL-004 Servo System Validation  | DRAFT     |
| VAL-005 Gait Validation          | DRAFT     |
| VAL-006 Safety System Validation | DRAFT     |
| VAL-007 Endurance Test           | DRAFT     |
| VAL-008 Battery Life Test        | DRAFT     |
| VAL-009 Beta Release Review      | DRAFT     |

> **ECO-002 变更**：状态由 VALIDATED 修正为 DRAFT（实际文件状态为 DRAFT/APPROVED AFTER ALPHA，尚未完成验证）。

---

# 11. Prototype Releases

Directory

```text
/PR
```

| Document                             | Status   |
| ------------------------------------ | -------- |
| PR-001 Alpha Prototype Release       | RELEASED |
| PR-002 Alpha Prototype Functional Validation | APPROVED |
| PR-003 Beta Prototype Iteration      | DRAFT    |

---

# 12. Bill of Materials

Directory

```text
/bom
```

| Document                                       | Status |
| ---------------------------------------------- | ------ |
| BOM-00 Executive Summary                       | APPROVED |
| BOM-01 Master Bill of Materials                | APPROVED |
| BOM-02 Engineering BOM                         | APPROVED |
| BOM-03 Spare Parts & Maintenance List          | APPROVED |

---

# 13. Engineering Change Orders

Directory

```text
/ECO
```

| Document                                       | Status   |
| ---------------------------------------------- | -------- |
| ECO-001 Lightweight Lower Body Architecture    | APPROVED |
| ECO-002 Documentation Consistency Fix          | APPROVED |

---

# 14. Alpha Completion Summary

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

IN PROGRESS (DRAFT)

---

Alpha Status

COMPLETE

---

Beta Status

READY

---

# 15. Next Milestone

Next Document

```text
BP-001 - Beta Prototype Release
```

Purpose

Transition From

Alpha Validation

↓

Beta Engineering Verification

---

Missing Documents (PLANNED)

| Document | Description | Directory |
|----------|-------------|-----------|
| SDS-01 | Software Architecture Specification | /SDS (not yet created) |
| BP-001~008 | Beta program documents | /BETA (not yet created) |

> **ECO-002 变更**：明确标注 SDS-01（EDS-05 引用但尚未创建）和 /BETA 目录（尚未创建）的状态。

---

# 16. File Naming Conventions

All documents follow the convention:

```text
[PREFIX]-[NNN]-[Descriptive-Slug].md
```

Examples:
- `MDS-01-System-Architecture.md`
- `EDS-01-System-Electrical-Architecture.md`
- `CDS-01-CAD-Design-Specification.md`

> **ECO-002 变更**：以下文件已重命名为符合连字符约定：
> - `MDS-03 Assembly Specification.md` -> `MDS-03-Assembly-Specification.md`
> - `MDS-04 Pelvis & Electronics Assembly Specification.md` -> `MDS-04-Pelvis-Electronics-Assembly.md`
> - `BOM-02_Engineering_BOM.md` -> `BOM-02-Engineering-BOM.md`
> - `CDS-07-Full Leg Subsystem Integration.md` -> `CDS-07-Full-Leg-Subsystem-Integration.md`
