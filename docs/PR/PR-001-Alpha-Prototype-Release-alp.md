# Mini-Atlas V6 Alpha

# PR-001 Alpha Prototype Release

Version: 1.0

Status: RELEASED

Document Number:

PR-001

Subsystem:

Full Robot

Release Type:

Alpha Prototype

Parent Documents:

* CDS-03~CDS-09 (Mechanical & Digital Mockups)
* DR-001~DR-010 (Design Reviews)
* SR-001 (System Weight Budget)
* FW-001~FW-003 (Firmware Architecture)

---

# 1. Purpose

正式发布 Mini-Atlas V6 Alpha 原型版本。

目标：

* 冻结全机机械设计
* 冻结单腿与双腿关节架构
* 冻结重量与重心预算
* 冻结电气接口与布线
* 提供 Alpha Prototype Build-1 基线用于制造与调试

---

# 2. Scope

Alpha Prototype 包含：

* 双腿完整 3-DOF 关节链路
* 骨盆总成
* Torso 框架
* Head 框架
* 电池和主控接口
* Wheel Module

---

# 3. Deliverables

* Digital Mockup: MiniAtlas_V6_Alpha_RevA.f3d / .step
* BOM List: MiniAtlas_V6_Alpha_BOM.xlsx
* Weight Report: MiniAtlas_V6_Alpha_Weight.pdf
* CG Report: MiniAtlas_V6_Alpha_CG.pdf
* Assembly Instructions: MiniAtlas_V6_Alpha_Assembly.pdf
* Firmware Baseline: FW-001~FW-003

---

# 4. Release Status

| Subsystem         | Status           |
| ----------------- | ---------------- |
| Hip Roll          | FROZEN           |
| Hip Pitch         | FROZEN           |
| Knee              | FROZEN           |
| Single Leg        | FROZEN           |
| Dual Leg & Pelvis | FROZEN           |
| Full Body         | FROZEN           |
| Electronics       | FROZEN           |
| Firmware          | READY FOR DEPLOY |

---

# 5. Usage

* 可用于制造第一台 Alpha 原型
* 可用于调试关节运动学与动力学
* 可用于验证全机重量分布与重心
* 可用于初步固件集成

---

# 6. Change Management

任何设计变更必须：

1. 提交 ECN (Engineering Change Notice)
2. 更新数字样机与 BOM
3. 重新通过 DR-010 系统级评审
4. 经 PR 批准后，才能制造下一版原型

---

# 7. Exit Criteria

* All CDS documents frozen
* All DR documents approved
* Weight, CG, Kinematics validated
* Electronics and firmware baseline verified

Status: RELEASED

---

# 8. Notes

* Alpha Prototype Build-1 仅用于原型验证
* 不可作为量产基线
* 所有 3D 打印件按照 CDS 冻结参数制造
* 所有舵机、轴承、硬件按 BOM 提供
