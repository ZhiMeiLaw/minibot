# Mini-Atlas V6 Alpha

# CDS-09 Full Body Integration

Version: 1.0 Freeze A

Status: APPROVED

Assembly Number:

V6-ASM-0030

Assembly Name:

Full Body Integration

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* CDS-08 Dual Leg & Pelvis Integration
* SR-001 System Weight Budget
* MDS-01 System Architecture
* MDS-04 Pelvis & Electronics Assembly Specification
* EDS-05 Communication & Control Architecture

---

# 1. Purpose

完成整机集成设计。

验证：

* 机械结构
* 重量分布
* 重心位置
* 电子布局
* 视觉布局
* 可维护性

通过后：

允许进入 Alpha Prototype CAD 阶段。

---

# 2. System Architecture

Head

↓

Neck

↓

Torso

↓

Pelvis

↓

Legs

↓

Wheel Modules

---

自由度：

Hip Roll ×2

Hip Pitch ×2

Knee ×2

Wheel Drive ×2

---

Total

8 Actuators

---

# 3. Overall Dimensions

Height

≈560 mm

---

Shoulder Width

≈180 mm

---

Pelvis Width

180 mm

---

Leg Length

280 mm

---

Wheel Diameter

80 mm

---

Status

FROZEN

---

# 4. Torso Architecture

结构：

Carbon Tube Frame

*

PETG Printed Nodes

---

尺寸：

Width

180 mm

---

Depth

90 mm

---

Height

150 mm

---

目标重量：

≤500 g

---

结果：

PASS

---

# 5. Head Architecture

配置：

ESP32-CAM

---

Camera

Forward Facing

---

安装高度：

≈520 mm

---

FOV：

水平视角优先

---

重量目标：

≤150 g

---

结果：

PASS

---

# 6. Neck Structure

方案：

Fixed Neck

---

无 Pitch

无 Roll

---

原因：

降低重量

降低复杂度

---

预留升级接口：

YES

---

结果：

PASS

---

# 7. Battery Placement

配置：

3S2P Samsung 30Q

---

位置：

Pelvis Center

---

安装：

Slide-In Battery Tray

---

重量：

≈380 g

---

结果：

PASS

---

# 8. Electronics Layout

Pelvis Upper Deck

安装：

ESP32

PDB

Buck

IMU

---

布局原则：

靠近重心

靠近电池

---

结果：

PASS

---

# 9. Center Of Mass Review

目标：

Pelvis Center

↓

30~50 mm

---

实际估算：

Pelvis Center

↓

40 mm

---

结果：

PASS

---

# 10. Weight Budget Review

| Subsystem   |  Weight |
| ----------- | ------: |
| Legs        | 1.60 kg |
| Pelvis      | 0.35 kg |
| Battery     | 0.38 kg |
| Electronics | 0.15 kg |
| Torso       | 0.45 kg |
| Head        | 0.15 kg |
| Covers      | 0.20 kg |

---

Total

≈3.28 kg

---

Target

≤4.0 kg

---

Margin

≈720 g

---

结果：

PASS

---

# 11. Hip Pitch Margin Review

依据：

DR-012

---

当前整机：

≈3.3 kg

---

预计利用率：

≈68%

---

结果：

GOOD

---

# 12. Wire Harness Architecture

Servo Bus

Daisy Chain

---

Wheel Motor

Dedicated Cable

---

Battery

XT30 Main Rail

---

IMU

I2C

---

Camera

ESP32-CAM Local

---

结果：

PASS

---

# 13. Maintenance Review

Battery

<2 min

---

Servo

<5 min

---

Wheel

<5 min

---

ESP32

<5 min

---

结果：

PASS

---

# 14. Transport Review

整机高度：

≈560 mm

---

重量：

≈3.3 kg

---

单手搬运：

YES

---

桌面调试：

YES

---

结果：

PASS

---

# 15. Manufacturing Review

平台：

Bambu Lab A1

---

兼容：

A1 Mini

（部分件分体打印）

---

预计打印材料：

PETG

约1.5 kg

---

结果：

PASS

---

# 16. Reliability Review

关键风险：

Hip Pitch

---

状态：

已解决

---

关键风险：

Battery Mount

---

措施：

Dual Lock

---

关键风险：

Wheel Cable

---

措施：

Internal Routing

---

结果：

PASS

---

# 17. Prototype Configuration Freeze

Leg

3 DOF

---

Ankle

None

---

Wheel

80 mm

---

Battery

3S2P

---

Controller

ESP32

---

IMU

ICM42688

---

Vision

ESP32-CAM

---

Status

FROZEN

---

# 18. CAD Assembly Structure

V6-ASM-0030

Full Body

├── Pelvis

├── Left Leg

├── Right Leg

├── Torso

├── Head

└── Electronics

---

状态：

READY

---

# 19. Prototype Readiness Review

Mechanical

PASS

---

Electrical

PASS

---

Weight

PASS

---

Manufacturing

PASS

---

Maintenance

PASS

---

结果：

APPROVED

---

# 20. Freeze Summary

Height

≈560 mm

---

Weight

≈3.3 kg

---

Battery

3S2P

---

Controller

ESP32

---

Vision

ESP32-CAM

---

Leg Architecture

3 DOF

*

Wheel Assisted

---

Status

APPROVED

READY FOR

PR-001 Alpha Prototype Release
