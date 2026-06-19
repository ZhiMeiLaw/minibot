# Mini-Atlas V6 Alpha

# MP-001 Manufacturing Package Release

Version: 1.0 Freeze A

Status: RELEASED

Document Number:

MP-001

Release Name:

Mini-Atlas V6 Alpha Manufacturing Package

Release Type:

Engineering Prototype Manufacturing Release

Parent Documents:

* PR-001 Alpha Prototype Release
* CDS-09 Full Body Integration
* BOM-01 Master Bill Of Materials
* BOM-02 Engineering BOM
* SR-001 System Weight Budget

---

# 1. Purpose

本文件定义：

Mini-Atlas V6 Alpha

首台工程样机的完整制造包（Manufacturing Package）。

目标：

* 打印全部零件
* 采购全部标准件
* 完成机械装配
* 完成电气集成
* 完成首次上电
* 完成首次站立验证

---

# 2. Manufacturing Configuration Freeze

## Mechanical Architecture

Hip Roll ×2

Hip Pitch ×2

Knee ×2

Wheel Module ×2

---

## Electronics

ESP32 DevKitC

ICM42688

PDB

7.4V Buck

5V Buck

---

## Power

3S2P Samsung 30Q

XT30 Main Connector

15A Fuse

---

## Locomotion

Wheel Assisted Walker

3 DOF Per Leg

---

Status

FROZEN

---

# 3. Manufacturing Deliverables

必须生成：

## CAD

Native CAD

STEP

STL

---

## Electrical

Schematic

Wiring Diagram

Cable Table

---

## Documentation

Assembly Guide

Bring-Up Guide

Test Procedure

---

Status

REQUIRED

---

# 4. STL Release List

## Pelvis

V6-PRT-0001

Pelvis Main Frame

---

Battery Bay

---

Electronics Deck

---

Service Hatch

---

## Hip Roll

HipRoll_Base

HipRoll_Output

HipRoll_TorqueModule

---

## Hip Pitch

HipPitch_Base

HipPitch_Output

HipPitch_TorqueModule

---

## Knee

Knee_Base

Knee_Output

Knee_TorqueModule

---

## Wheel Module

Wheel_Adapter

Wheel_Hub

Motor_Mount

---

## Torso

Torso_Frame_Node

Torso_Cover

---

## Head

Head_Frame

Camera_Mount

---

Status

RELEASED

---

# 5. Printing Specification

Printer

Bambu Lab A1

---

Compatible

Bambu Lab A1 Mini

---

Material

PETG

---

Nozzle

0.4 mm

---

Layer Height

0.20 mm

---

Wall Count

4

---

Top Layers

5

---

Bottom Layers

5

---

Infill

40%

Gyroid

---

Support

Minimal

---

Status

RELEASED

---

# 6. Brass Insert Installation Table

| Insert Type       | Qty |
| ----------------- | --: |
| M2 Brass Insert   |  20 |
| M2.5 Brass Insert |  10 |
| M3 Brass Insert   |  60 |

---

Installation Temperature

220~240°C

---

Verification

Flush Surface

No Tilt

No Crack

---

Status

RELEASED

---

# 7. Bearing Installation Table

| Bearing | Qty |
| ------- | --: |
| 688-2RS |   4 |
| 698-2RS |   8 |

---

Installation Method

Press Fit

---

禁止：

Hammer Installation

---

Status

RELEASED

---

# 8. Carbon Tube Cutting Table

## Leg

Upper Leg

120 mm ×4

OD 10mm × ID 8mm Carbon Tube

---

Lower Leg

120 mm ×4

OD 10mm × ID 8mm Carbon Tube

---

## Torso

Vertical Tube

150 mm ×2

---

Horizontal Tube

180 mm ×2

---

Tolerance

±0.5 mm

---

Status

RELEASED

---

# 9. Fastener Kit

## M2

M2×6

M2×8

---

## M2.5

M2.5×8

M2.5×10

---

## M3

M3×8

M3×10

M3×12

M3×16

---

## Other

M3 Lock Nut

M3 Washer

E-Clip

Cable Tie

---

Status

RELEASED

---

# 10. Required Tools

Hex Driver Set

---

Soldering Station

---

Heat Insert Tool

---

Bearing Press

---

Digital Caliper

---

Multimeter

---

Bench Power Supply

---

Status

REQUIRED

---

# 11. Manufacturing Sequence

Stage 1

Procurement

---

Stage 2

Print Parts

---

Stage 3

Install Brass Inserts

---

Stage 4

Install Bearings

---

Stage 5

Cut Carbon Tubes

---

Stage 6

Build Hip Roll

---

Stage 7

Build Hip Pitch

---

Stage 8

Build Knee

---

Stage 9

Build Wheel Module

---

Stage 10

Build Legs

---

Stage 11

Build Pelvis

---

Stage 12

Install Electronics

---

Stage 13

Cable Routing

---

Stage 14

Install Battery

---

Stage 15

Bring-Up

---

# 12. Quality Gates

## QG-01

Printed Parts Inspection

---

Dimension

±0.2 mm

---

PASS Required

---

## QG-02

Bearing Fit Inspection

---

No Excessive Force

---

PASS Required

---

## QG-03

Joint Motion Inspection

---

Smooth Rotation

---

No Binding

---

PASS Required

---

## QG-04

Electrical Inspection

---

No Short Circuit

---

Correct Polarity

---

PASS Required

---

## QG-05

Power-On Inspection

---

11.1V Rail

PASS

---

7.4V Rail

PASS

---

5V Rail

PASS

---

PASS Required

---

# 13. First Power-On Procedure

Robot Suspended

No Ground Contact

---

Connect Battery

---

Measure Current

---

Verify Voltage Rails

---

Verify Temperature

---

Verify No Smoke

---

Status

MANDATORY

---

# 14. Bring-Up Checklist

□ ESP32 Boot

□ UART Operational

□ IMU Operational

□ Servo Scan Success

□ Servo ID Verified

□ Wheel Driver Verified

□ Battery Voltage Verified

□ Current Consumption Normal

□ Emergency Stop Verified

---

Status

MANDATORY

---

# 15. First Motion Procedure

Hip Roll Test

---

Hip Pitch Test

---

Knee Test

---

Wheel Rotation Test

---

Low-Speed Motion Only

---

Status

MANDATORY

---

# 16. First Standing Procedure

Support Frame Recommended

---

Move To Stand Pose

---

Hold 10 Seconds

---

Monitor:

Current

Temperature

Servo Load

---

Pass Criteria

No Fall

No Alarm

No Overcurrent

---

# 17. Manufacturing Acceptance Criteria

Mechanical Assembly

PASS

---

Electrical Assembly

PASS

---

Power System

PASS

---

Communication

PASS

---

Standing Test

PASS

---

Wheel Mode

PASS

---

Weight

<4.0 kg

---

Status

ALPHA ACCEPTED

---

# 18. Known Risks

Hip Pitch Load Margin

MEDIUM

---

Cable Routing

LOW

---

Battery Retention

LOW

---

Servo Clamp Loosening

LOW

---

# 19. Manufacturing Freeze Summary

CAD

FROZEN

---

Electronics

FROZEN

---

Power System

FROZEN

---

Mechanical Architecture

FROZEN

---

BOM

FROZEN

---

Status

RELEASED

---

# 20. Next Document

READY FOR

FW-001-Firmware-Architecture.md

Status

MANUFACTURING RELEASE COMPLETE
