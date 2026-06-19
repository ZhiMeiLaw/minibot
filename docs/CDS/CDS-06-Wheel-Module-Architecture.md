# Mini-Atlas V6 Alpha

# CDS-06 Wheel Module Architecture

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0030

Part Name:

Wheel Module

Parent Assembly:

V6-ASM-0003 Leg Subsystem

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* DR-011 Ankle Architecture Review
* CDS-05D Knee Assembly Verification
* CDS-02A Standard Component Library Revision A
* MDS-01 System Architecture
* EDS-03 Power Distribution & Protection Design

---

# 1. Purpose

Wheel Module 提供：

* 轮式辅助移动功能
* 基础越障能力
* 支撑下肢重量

设计目标：

* 与 Lower Leg 下端接口匹配
* 安装 GB37-520 电机
* 兼容 80 mm 轮子
* 可快速拆装维护
* 保证可靠性与低成本

---

# 2. Design Philosophy

* 无踝关节（Ankle Removed）
* Rigid Mount（刚性安装）
* 支撑轮轴受力直接传递至 Knee Output
* 保持重量低、结构简单、制造可行
* 保留未来升级空间（Ankle 或更大轮子）

---

# 3. Coordinate System

X+ Forward

Y+ Left

Z+ Up

轮子旋转轴：Z Axis

安装孔中心与 Lower Leg 下端中心对齐

---

# 4. Overall Dimensions

* Wheel Diameter：80 mm
* Wheel Width：20 mm
* Wheel Offset：下缘距 Knee Output 底面 20 mm
* Motor Envelope：GB37-520 约 40×40×55 mm
* Total Weight 目标：≤250 g（含轮+电机+安装板+硬件）

---

# 5. Interface to Lower Leg

* Lower Leg Carbon Tube OD 10mm × ID 8mm
* Mount Plate：Rigid Adapter Plate
* 4 × M3 螺丝固定
* 插拔兼容性：可快速拆卸维护
* 安装高度：保持 20 mm 离地间隙

---

# 6. Motor Selection

* GB37-520
* 额定电压：12 V
* 最大扭矩：0.6 N·m
* 安装方式：底部固定于 Wheel Adapter Plate
* 编码器接口预留：10 mm 插口
* 兼容性：未来可升级到更高扭矩轮电机

---

# 7. Wheel Hub

* 内径：20 mm
* 外径：32 mm
* 材质：PLA / PETG 可打印
* Clamp Screw：M3 ×2
* Anti-Slip Teeth：内壁微齿纹
* 可快速更换轮子

---

# 8. Torque Path

* 电机输出轴 → Wheel Hub → 轮子
* 输出直接作用于下肢末端
* Lower Leg 仅承受重量与动载荷，不承受扭矩
* 无活动轴承，降低摩擦与维护复杂度

---

# 9. Bearing / Support

* 电机内置轴承
* Wheel Hub 与 Adapter Plate 采用 Press Fit + M3 Clamp
* 静态 / 动态载荷估算：

  * Robot Weight：≈5 kg
  * Peak Load：≈10 N
  * Safety Factor：≥2

---

# 10. Mechanical Stop

* 不需要独立机械限位
* 轮子旋转受轮电机限位控制
* 防止轮子干涉 Lower Leg 或地面

---

# 11. Wire Routing

* 电机线缆通道：Ø6 mm
* 位置：Lower Leg 后侧通道
* 接口：XT30 电源接口 + Encoder 信号线
* 线束固定：3×Cable Tie Anchor

---

# 12. Assembly Sequence

1. Lower Leg 安装 Adapter Plate
2. Wheel Hub 安装至 Adapter Plate
3. GB37-520 电机安装至 Wheel Hub
4. M3 Clamp Screw 锁紧
5. 轮子安装至 Hub
6. 电机线缆通过通道
7. XT30 接口连接
8. 功能验证（旋转、离地间隙）

---

# 13. Weight Estimate

| Component                 | Weight |
| ------------------------- | -----: |
| GB37-520 Motor            |  120 g |
| Wheel 80 mm               |   50 g |
| Adapter Plate             |   40 g |
| Screws / Clamp / Hardware |   25 g |

Total ≈ 235 g

---

# 14. Clearance Verification

* Ground Clearance ≈ 20 mm
* Wheel 与 Lower Leg 保持 ≥2 mm 间隙
* 动作全程无干涉

---

# 15. Reliability / Maintenance

* 轮子可快速拆装
* Clamp + Screw + Anti-Slip Teeth 确保长期不松动
* 电机与 Hub 可单独更换
* 线缆可快速维护

---

# 16. Printability / Manufacturing

* Platform：Bambu Lab A1 / Mini
* 材料：PETG
* Infill：40~50%
* Printing Orientation：Wheel Hub Face Up
* Wall：4
* Top / Bottom：5
* 支撑：Minimal, 避免干涉

---

# 17. Future Upgrade Path

* 兼容更大轮子（100 mm）
* 兼容 Wheel Encoder 升级
* 预留 Ankle 模块升级接口
* 可兼容双电机 / 双轮配置

---

# 18. Verification Checklist

| Item               | Result |
| ------------------ | ------ |
| CAD Geometry       | PASS   |
| Wheel Hub Fit      | PASS   |
| Motor Installation | PASS   |
| Clamp / Screw      | PASS   |
| Wire Routing       | PASS   |
| Ground Clearance   | PASS   |
| Printability       | PASS   |
| Weight             | PASS   |
| Maintenance        | PASS   |

---

# 19. Freeze Summary

* Wheel Module Type：Rigid Mount
* Wheel Diameter：80 mm
* Motor：GB37-520
* Adapter Plate：Rigid Lower Leg Interface
* Clamp Screw：M3 ×4
* Anti-Slip Teeth：YES
* Architecture：Wheel Assisted Walker
* Status：APPROVED
* READY FOR：CDS-07-Full Leg Subsystem Integration
