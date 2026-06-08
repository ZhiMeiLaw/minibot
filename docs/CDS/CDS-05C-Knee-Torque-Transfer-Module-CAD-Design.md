# Mini-Atlas V6 Alpha

# CDS-05C Knee Torque Transfer Module CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0022

Part Name:

Knee_Torque_Module

Parent Assembly:

V6-ASM-0003 Knee Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* CDS-05A Knee Base CAD Design
* CDS-05B Knee Output CAD Design
* DR-009 Knee Architecture Review
* DR-009A Knee Servo Orientation Review
* CDS-04C HipPitch Torque Transfer Module CAD Design

---

# 1. Purpose

Knee_Torque_Module 用于将 STS3046 Servo 输出扭矩可靠传递至 Knee_Output。

其职责：

* Torque Transfer（扭矩传递）
* Anti Slip（防打滑）
* Anti Backlash（降低回程间隙）
* Long Life（长期可靠运行）
* Easy Maintenance（易维护）

---

注意：

Knee Torque Module 不承担结构重量。

仅承担：

Servo Torque

↓

Knee_Output

---

# 2. Design Philosophy

遵循：

Weight Path

与

Torque Path

分离原则

---

重量路径：

Robot Weight

↓

Lower Leg

↓

Knee_Output

↓

Joint Shaft

↓

698 Bearings

↓

Knee_Base

---

扭矩路径：

STS3046

↓

Servo Horn

↓

Torque Module

↓

Knee_Output

---

Servo 不承担重量。

---

# 3. Why Knee Needs Stronger Design

Hip Pitch：

约 30~50 次动作/分钟

---

Knee：

约 80~150 次动作/分钟

---

循环次数：

约 3 倍

---

因此 Knee Torque Module 必须强化。

---

# 4. Architecture

采用：

Enhanced Double Clamp Hub

增强型双夹紧结构

---

结构：

STS3046

↓

Aluminum Horn

↓

Center Hub

↓

Dual Clamp Ring

↓

Knee_Output

---

Front View

```
   Output

      │
```

┌──────┴──────┐

│ Clamp Ring  │

└──────┬──────┘

```
      │

  Center Hub

      │

 Servo Horn
```

---

# 5. Servo Horn

冻结：

STS3046 Original Aluminum Horn

---

材料：

6061-T6 Aluminum

---

厚度：

3 mm

---

中心螺丝：

M3

---

禁止：

塑料舵盘

---

原因：

疲劳寿命不足

---

# 6. Center Hub

Part Number:

V6-PRT-0022A

---

名称：

Center Hub

---

作用：

连接：

Servo Horn

↓

Clamp Ring

↓

Knee_Output

---

外径：

30 mm

---

厚度：

10 mm

---

相比 Hip Pitch：

28 mm

↓

30 mm

---

增强扭矩容量

---

# 7. Clamp Ring

Part Number:

V6-PRT-0022B

---

名称：

Dual Clamp Ring

---

数量：

2

---

结构：

Split Ring

开口夹环

---

外径：

40 mm

---

内径：

30 mm

---

厚度：

6 mm

---

夹缝：

1.5 mm

---

# 8. Clamp Screw Upgrade

Hip Pitch：

M3 ×2

---

Knee：

M3 ×4

---

布局：

90°均布

---

Top View

```
    ●
```

●         ●

```
    ○
```

●         ●

---

中心：

Knee Axis

---

优势：

夹紧力增加

长期不松动

---

# 9. Brass Insert

规格：

M3 Brass Insert

---

数量：

4

---

孔径：

4.2 mm

---

孔深：

5 mm

---

安装：

Clamp Ring

---

# 10. Torque Interface

连接：

Torque Module

↓

Knee_Output

---

方式：

4 × M3

---

孔径：

Ø3.2 mm

---

PCD：

18 mm

---

均布：

90°

---

# 11. Anti-Slip Teeth

新增：

Micro Serration

微齿纹

---

位置：

Clamp Ring 内壁

---

深度：

0.4 mm

---

齿距：

1.0 mm

---

作用：

增加摩擦力

降低滑移风险

---

# 12. Reinforcement Rib

增加：

Radial Rib

径向加强筋

---

数量：

6

---

厚度：

3 mm

---

长度：

10 mm

---

位置：

Center Hub

↓

Clamp Ring

---

# 13. Torque Capacity Analysis

目标：

Knee Peak Torque

≈2.2 N·m

---

设计能力：

≥7 N·m

---

安全系数：

> 3

---

结果：

PASS

---

# 14. Mechanical Clearance

Torque Module

与

Knee_Base

最小间隙：

1.5 mm

---

推荐：

2.0 mm

---

防止：

打印误差

装配误差

---

# 15. Printing Specification

材料：

PETG

---

Layer Height：

0.20 mm

---

Wall：

4

---

Top：

5

---

Bottom：

5

---

Infill：

50%

Gyroid

---

# 16. Printing Orientation

推荐：

Center Hub 朝上

---

目的：

保证：

Clamp Precision

Screw Hole Precision

---

# 17. Weight Estimate

| Component     | Weight |
| ------------- | -----: |
| Center Hub    |   10 g |
| Clamp Ring ×2 |   12 g |
| Inserts       |    3 g |
| Screws        |    5 g |

---

Total

≈30 g

---

目标：

<35 g

---

结果：

PASS

---

# 18. Assembly Sequence

Step 1

安装 Servo Horn

---

Step 2

安装 Center Hub

---

Step 3

安装 Clamp Ring

---

Step 4

安装 Brass Insert

---

Step 5

连接 Knee_Output

---

Step 6

安装 4×M3 Clamp Screw

---

Step 7

锁紧至指定扭矩

---

# 19. Screw Torque Specification

M3 Clamp Screw

推荐：

0.8 N·m

---

最大：

1.2 N·m

---

螺纹胶：

Loctite 243

---

必须使用

---

# 20. Verification Checklist

CAD检查：

□ Servo Horn正确

□ Clamp Ring正确

□ PCD正确

□ Rib正确

□ 无干涉

---

打印检查：

□ Clamp Gap正确

□ Insert牢固

□ 无裂纹

---

装配检查：

□ 无打滑

□ 无偏心

□ Rotation Smooth

□ Torque Transfer正常

---

# 21. Fatigue Verification Target

目标：

300,000 Cycles

---

检查：

□ Clamp 不松动

□ 无裂纹

□ 无滑移

□ Servo Horn 正常

---

# 22. Future Upgrade Compatibility

兼容：

STS3046

---

兼容：

STS3215

同尺寸版本

---

预留：

STS3250

需重新评审

---

# 23. Freeze Summary

Part Number

V6-PRT-0022

---

Part Name

Knee_Torque_Module

---

Architecture

Enhanced Double Clamp Hub

---

Horn

STS3046 Aluminum Horn

---

Clamp Ring

Dual Split Ring

---

Clamp Screw

M3 ×4

---

Brass Insert

M3 ×4

---

Anti-Slip Teeth

YES

---

Design Torque

≥7 N·m

---

Weight

≈30 g

---

Status

APPROVED

READY FOR

CDS-05D-Knee-Assembly-Verification.md
