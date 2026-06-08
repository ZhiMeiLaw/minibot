# Mini-Atlas V6 Alpha

# DR-004 Hip Architecture Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-004

Subsystem:

Hip Joint Architecture

Parent Documents:

* DR-001 System Architecture Review
* DR-002 Actuator Selection Review
* DR-003 Joint Architecture Review
* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design

Related Documents:

* CDS-03A Hip Roll Base CAD
* CDS-03B Hip Roll Output CAD
* CDS-03C Hip Roll Torque Module CAD
* CDS-04A Hip Pitch Base CAD
* CDS-04B Hip Pitch Output CAD

---

# 1. Purpose

评审 Mini-Atlas V6 Alpha 髋关节设计架构，确定：

* Hip Roll / Hip Pitch 排序
* 输出轴接口
* Torque Transfer Module布局
* 碳管夹紧接口
* 机械限位
* 装配与维护空间

---

# 2. Candidate Architectures

| Option | Sequence             | Notes            |          |
| ------ | -------------------- | ---------------- | -------- |
| A      | Hip Pitch → Hip Roll | 不利于重心控制，CAD设计复杂  | REJECTED |
| B      | Hip Roll → Hip Pitch | 更仿生人体，重心优化，CAD简单 | APPROVED |

---

# 3. Joint Details

## Hip Roll

* Axis: lateral rotation
* Output: 8mm shaft
* Bearing: 6803 ×2
* Torque: STS3046
* Carbon Tube Clamp: fixed at output

## Hip Pitch

* Axis: sagittal rotation
* Output: 8mm shaft
* Bearing: 6803 ×2
* Torque: STS3046
* Carbon Tube Clamp: fixed at output

---

# 4. Torque Module

* Dual Clamp design
* Transfers torque from STS3046 to output shaft
* Isolates servo from bending load
* Assembly verified in CDS-03C / CDS-04C

---

# 5. Mechanical Limits

* Hip Roll: ±30°
* Hip Pitch: -20° / +45°
* Mechanical stop integrated
* Clearance for wires & carbon tube: 3mm minimum

---

# 6. Interface to Pelvis

* Mounting holes: 4 × M3
* Alignment pins: 2 × Ø3mm
* Ensure torque path straight from servo → shaft → tube → leg

---

# 7. Risk Analysis

| Risk                          | Mitigation                           |
| ----------------------------- | ------------------------------------ |
| Misalignment Hip Roll → Pitch | CAD Tolerance ±0.1mm                 |
| Carbon Tube Slippage          | Torque Clamp verified 2Nm            |
| Servo Overload                | Safety Manager + Torque Margin 12.5% |
| Interference                  | Wire harness routing review          |

---

# 8. Validation Plan

* CAD Simulation: Check envelope & interference
* Mechanical Mockup: Verify assembly / disassembly
* Torque Simulation: Check peak load with STS3046
* Printing Test: Orientation & support validation

---

# 9. Freeze Summary

* Hip Roll → Hip Pitch sequence APPROVED
* Output shafts Ø8mm frozen
* Torque Module design frozen
* Mechanical stops frozen
* Pelvis mounting frozen
* Status: APPROVED for CDS-04 CAD and Alpha Prototype
