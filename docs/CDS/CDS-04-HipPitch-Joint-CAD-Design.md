# Mini-Atlas V6 Alpha

# CDS-04 Hip Pitch Joint CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Assembly Number:

V6-ASM-0002

Assembly Name:

Hip Pitch Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

CDS-03D Hip Roll Assembly Verification

CDS-02A Standard Component Library Revision A

MDS-02 Detailed Joint Design

MDS-03 Assembly Specification

---

# 1. Purpose

本文件定义：

Hip Pitch Joint

（髋关节俯仰自由度）

的总体机械架构。

Hip Pitch 是整个机器人最重要的承重关节。

负责：

- 抬腿
- 前摆
- 后摆
- 重心转移
- 下蹲
- 起步
- 停止

其性能直接决定：

- 步态能力
- 越障能力
- 整机重心
- 稳定性

---

# 2. Design Objectives

Hip Pitch 必须满足：

- 承受整条腿重量
- 支持动态步态
- 支持未来轮腿混合模式
- 易维护
- 易打印
- 易升级

---

设计寿命：

100小时以上

Alpha Prototype

---

# 3. Coordinate System

沿用机器人全局坐标系：

X+

Forward

Y+

Left

Z+

Up

---

Hip Pitch Rotation Axis：

Y Axis

---

运动形式：

Pitch Around Y

---

# 4. Relationship To Hip Roll

Hip Pitch 位于：

Hip Roll 下方

---

轴心偏移：

15 mm

---

示意：

Front View

      Hip Roll

          O

          │

       15 mm

          │

          O

      Hip Pitch

---

目的：

- 保持骨盆宽度合理
- 提高结构紧凑性
- 避免舵机干涉

---

# 5. Motion Range

Forward

+60°

---

Backward

-30°

---

Total

90°

---

满足：

Walking

Turning

Squatting

Obstacle Crossing

---

# 6. Mechanical Stop

工作范围：

+60°

-30°

---

机械极限：

+65°

-35°

---

保留：

5°

安全余量

---

# 7. Load Path

正确载荷路径：

Wheel Module
↓
Lower Leg
↓
Knee
↓
Upper Leg
↓
Hip Pitch Output
↓
Ø8 Shaft
↓
698 Bearings
↓
Hip Pitch Base
↓
Hip Roll Output
↓
Pelvis

---

禁止：

Wheel Module
↓
Servo
↓
Horn

---

Servo 永远不承担结构载荷。

---

# 8. Bearing Selection

冻结：

698-2RS

---

规格：

8 × 19 × 6 mm

---

数量：

2

---

原因：

相比688：

- 刚性更高
- 宽度更大
- 更适合主承重关节

---

# 9. Shaft Specification

Joint Shaft：

Ø8 mm

---

Material：

GCr15

---

Tolerance：

h6

---

长度：

待 CDS-04A 确定

---

# 10. Servo Selection

冻结：

STS3046 ×1

---

安装方式：

Bearing Supported

Architecture

---

Servo 仅负责：

Torque

---

不负责：

Weight Support

---

# 11. Torque Transfer Architecture

结构：

STS3046
↓
Aluminum Horn
↓
Double Clamp Hub
↓
Hip Pitch Output

---

沿用：

CDS-03C

Torque Transfer Module

---

# 12. Leg Interface

Hip Pitch Output

↓

Leg Adapter

↓

Carbon Tube

---

不允许：

Carbon Tube

直接连接舵机结构

---

# 13. Carbon Tube Standard

保持统一：

OD 10mm × ID 8mm

Carbon Tube

---

优势：

统一库存

统一夹具

统一维护

---

# 14. Estimated Joint Loads

静态：

≈1.0 kg

---

动态：

≈3.0 kg

---

冲击峰值：

≈5.0 kg

---

设计安全系数：

2.0

---

# 15. Weight Target

Hip Pitch Joint：

<180 g

---

目标：

尽量接近：

150 g

---

# 16. Cost Target

目标：

<120 RMB

---

理想：

≈100 RMB

---

# 17. Future Compatibility

兼容：

STS3046

STS3215

---

预留：

STS3250

STS3255

---

无需修改：

Pelvis

Hip Roll

---

# 18. Subdocuments

本文件冻结后：

进入：

CDS-04A-HipPitch_Base-CAD-Design.md

---

随后：

CDS-04B-HipPitch_Output-CAD-Design.md

---

随后：

CDS-04C-HipPitch-Torque-Module-CAD-Design.md

---

最后：

CDS-04D-HipPitch-Assembly-Verification.md

---

# 19. Freeze Summary

Joint:

Hip Pitch

---

Axis:

Y Axis

---

Range:

+60°

-30°

---

Mechanical Stop:

+65°

-35°

---

Bearing:

698-2RS ×2

---

Shaft:

Ø8 GCr15

---

Servo:

STS3046 ×1

---

Carbon Tube:

OD 10mm × ID 8mm

---

Status:

APPROVED

READY FOR

CDS-04A-HipPitch_Base-CAD-Design