# Mini-Atlas V6 Alpha

# CDS-08 Dual Leg & Pelvis Integration

Version: 1.0 Freeze A

Status: APPROVED

Assembly Number:

V6-ASM-0020

Assembly Name:

Dual Leg & Pelvis Subsystem

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* CDS-07 Full Leg Subsystem Integration
* SR-001 System Weight Budget
* DR-012 Leg Kinematics & Torque Validation
* MDS-04 Pelvis & Electronics Assembly Specification
* EDS-02 Power Budget & Current Analysis

---

# 1. Purpose

将左/右腿与 Pelvis 总成集成为完整下半身子系统，冻结：

* 双腿间距 (Hip Spacing)
* Pelvis 总成尺寸与安装孔位
* Battery Bay 布局
* PDB 和 Buck 模块位置
* 主线束走向
* 重心 (COM) 布局
* 下半身维护通道

通过后，下半身总成达到系统级设计冻结，可进入全身组装阶段。

---

# 2. Dual Leg Layout

* Hip Spacing：160 mm（中心到中心）
* 左右腿：对称布局
* 下肢自由度：3 DOF / Leg
* 轮模块：刚性安装于 Lower Leg
* 结构链：

Pelvis

↓

Hip Roll

↓

Hip Pitch

↓

Upper Leg

↓

Knee

↓

Lower Leg

↓

Wheel Module

---

# 3. Pelvis Frame

* 宽度：180 mm
* 高度：70 mm
* 材质：PETG + Carbon Tube Reinforcement
* 下腿接口：2 × Hip Roll Base Plate
* 插拔方式：螺丝固定 + Brass Insert
* 维护开口：左右对称，直通 Battery Bay

---

# 4. Battery Bay

* 电池类型：3S2P 18650 Samsung 30Q
* 容量：约 3800 mAh
* 安装方式：抽拉式卡槽
* 电池接口：XT30
* 位置：Pelvis 下方，靠近中心
* 重心优化：尽量靠近骨盆 COM

---

# 5. Electronics Mounting

* ESP32 DevKitC ×1
* PDB ×1
* 7.4V Buck ×1
* 5V Buck ×1
* 电源开关位置：Pelvis 前端上盖
* 接口布局：整洁，便于维护
* 线束通道：Ø8 mm，贯穿左右腿

---

# 6. COM Layout

* 双腿重量中心：约 100 mm 下方 Pelvis 平面
* Battery COM：约 20 mm 下方 Pelvis 中心
* Electronics COM：Pelvis 上层
* 整体重心：约 Pelvis 中心线下 30~50 mm
* 目标：保证站立稳定，Hip Pitch 扭矩 ≤ 80% 峰值

---

# 7. Wire Harness Routing

* Servo Bus：左右腿各 3 舵机，串联至 Pelvis
* Wheel Motor Cable：穿通 Lower Leg 与 Pelvis
* 电池电源：XT30 至 PDB
* 备用接口：IMU、未来传感器
* 线束固定：Cable Tie Anchor + 支架槽

---

# 8. Assembly Sequence

1. 安装 Pelvis Frame
2. 安装 Battery Bay
3. 安装 PDB / Buck / ESP32
4. 左右腿安装至 Hip Roll Base
5. 固定 Hip Spacing 螺丝
6. 安装 Lower Leg Carbon Tube
7. 安装 Knee & Wheel Module
8. 线束穿通并固定
9. 电池安装
10. 功能验证（站立、姿态、轮模块驱动）

---

# 9. Weight Budget Verification

| Component          | Weight |
| ------------------ | -----: |
| Pelvis Frame       |  350 g |
| Battery            |  380 g |
| Electronics        |  150 g |
| Left Leg           |  798 g |
| Right Leg          |  798 g |
| Covers / Fasteners |  120 g |

Total ≈ 2596 g

---

目标 ≤ 4.0 kg ✅
Margin = 1.4 kg，满足 DR-012 设定

---

# 10. Maintenance Verification

* Servo 更换 <5 min / Leg
* Wheel Module 更换 <5 min / Leg
* Battery 更换 <2 min
* Electronics 快速可维护
* Brass Insert + Cable Tie 易操作

---

# 11. Stability & COM Verification

* 双腿站立：PASS
* 静态步态：PASS
* 轮辅助模式：PASS
* Ground Clearance：≈20 mm
* 重心偏差：≤10 mm

---

# 12. Freeze Summary

* Hip Spacing：160 mm
* Pelvis Width：180 mm
* Battery Bay：固定，XT30接口
* PDB / Buck / ESP32 安装位置冻结
* Wire Harness Routing 冻结
* COM Layout 冻结
* 维护开口冻结
* Weight Budget 符合 SR-001

Status: APPROVED
READY FOR: CDS-09 Full Body Integration
