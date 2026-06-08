# Mini-Atlas V6 Alpha

# CDS-04C HipPitch Torque Transfer Module CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0012

Part Name:

HipPitch_Torque_Module

Parent Assembly:

V6-ASM-0002 Hip Pitch Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

- CDS-04 Hip Pitch Joint CAD Design
- CDS-04A HipPitch_Base CAD Design
- CDS-04B HipPitch_Output CAD Design
- CDS-03C HipRoll Torque Transfer Module CAD Design
- DR-007 Hip Pitch Torque Capacity Review

---

# 1. Purpose

HipPitch_Torque_Module 用于将 STS3046 Servo 输出扭矩可靠传递到 HipPitch_Output。

其职责：

- 传递 Servo Torque（舵机扭矩）
- 消除 Horn 打滑风险
- 消除 Horn 偏心问题
- 防止长期疲劳松动
- 提供可维护结构

---

Torque Module 不承担结构重量。

仅承担：

Torque Transfer

---

# 2. Design Philosophy

核心原则：

```text
Weight Path
≠
Torque Path
```

---

重量路径：

Wheel Module

↓

Lower Leg

↓

Knee

↓

Upper Leg

↓

HipPitch_Output

↓

Joint Shaft

↓

698 Bearings

↓

HipPitch_Base

---

扭矩路径：

STS3046

↓

Aluminum Horn

↓

Torque Module

↓

HipPitch_Output

---

Servo 永远不承担结构重量。

---

# 3. Architecture

采用：

Double Clamp Hub

双夹紧式扭矩模块

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

HipPitch_Output

---

示意：

Front View

          Output

             │

      ┌──────┴──────┐

      │   Clamp     │

      └──────┬──────┘

             │

       Center Hub

             │

         Servo Horn

---

# 4. Why Double Clamp

禁止：

Single Screw Horn

---

原因：

长期运行后容易：

- 打滑
- 偏心
- 裂纹
- 松动

---

双夹紧优点：

- 均匀受力
- 更高摩擦力
- 更高可靠性
- 易维护

---

# 5. Servo Horn

冻结：

STS3046 Aluminum Horn

---

材料：

6061-T6 Aluminum

---

厚度：

3 mm

---

安装方式：

Servo Standard Spline

---

中心螺丝：

M3

---

# 6. Center Hub

Part Number：

V6-PRT-0012A

---

名称：

Center Hub

---

作用：

连接：

Servo Horn

↓

Clamp Ring

---

外径：

28 mm

---

厚度：

8 mm

---

中心孔：

STS3046 Spline Interface

---

材料：

PETG

Alpha Prototype

---

未来：

CNC Aluminum Optional

---

# 7. Clamp Ring

Part Number：

V6-PRT-0012B

---

名称：

Dual Clamp Ring

---

作用：

锁紧：

HipPitch_Output

---

数量：

2

---

结构：

Split Ring

开口夹环

---

外径：

36 mm

---

内径：

28 mm

---

厚度：

5 mm

---

夹缝：

1.5 mm

---

# 8. Clamp Screw

规格：

M3 × 16

---

数量：

2

---

安装方式：

对称布局

---

示意：

Top View

      M3

       ●

   ┌───────┐

   │ Clamp │

   └───────┘

       ●

      M3

---

# 9. Brass Insert

规格：

M3 Brass Insert

---

数量：

2

---

安装位置：

Clamp Ring

---

孔径：

4.2 mm

---

孔深：

5 mm

---

# 10. Torque Interface

Torque Module

↓

HipPitch_Output

---

接口：

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

示意：

      ●

  ●       ●

      ○

  ●       ●

---

中心：

Hip Pitch Axis

---

# 11. Estimated Torque Capacity

依据：

STS3046

≈3 N·m

---

设计目标：

≥6 N·m

---

安全系数：

2×

---

结果：

PASS

---

# 12. Mechanical Clearance

Torque Module

与

HipPitch_Base

之间最小间隙：

1.5 mm

---

推荐：

2.0 mm

---

避免：

- 打印误差干涉
- 装配误差干涉

---

# 13. Structural Reinforcement

增加：

Radial Rib

径向加强筋

---

数量：

4

---

厚度：

2.5 mm

---

长度：

8 mm

---

位置：

Center Hub

↓

Clamp Ring

---

作用：

提高抗扭刚度

---

# 14. Weight Estimate

| Component | Weight |
|------------|--------:|
| Center Hub | 8 g |
| Clamp Ring ×2 | 10 g |
| Brass Insert | 2 g |
| M3 Screw | 2 g |

---

总重：

≈22 g

---

目标：

<25 g

---

结果：

PASS

---

# 15. Assembly Sequence

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

连接 HipPitch_Output

---

Step 6

安装 M3 Clamp Screw

---

Step 7

锁紧至规定扭矩

---

# 16. Screw Torque Specification

M3 Clamp Screw

---

推荐：

0.8 N·m

---

最大：

1.2 N·m

---

避免：

PETG 变形

---

# 17. Verification Checklist

CAD检查：

□ Servo Horn Interface正确

□ Clamp Ring正确

□ PCD正确

□ 无干涉

□ 输出轴同心

---

打印检查：

□ Clamp Gap正确

□ Brass Insert正常

□ 无裂纹

---

装配检查：

□ 无打滑

□ 无偏心

□ Rotation Smooth

□ Torque Transfer正常

---

# 18. Failure Mode Review

失效模式1：

Clamp Screw 松动

解决：

Loctite 243

---

失效模式2：

PETG 蠕变

解决：

增大接触面积

---

失效模式3：

Horn 滑牙

解决：

使用原厂 Aluminum Horn

---

# 19. Future Upgrade Compatibility

兼容：

STS3046

---

兼容：

STS3215

（同尺寸版本）

---

预留：

STS3250

需重新评审

---

# 20. Freeze Summary

Part Number

V6-PRT-0012

---

Part Name

HipPitch_Torque_Module

---

Architecture

Double Clamp Hub

---

Horn

STS3046 Aluminum Horn

---

Clamp

Dual Clamp Ring

---

Clamp Screw

M3 × 16 ×2

---

Brass Insert

M3 ×2

---

Design Torque

≥6 N·m

---

Weight

≈22 g

---

Status

APPROVED

READY FOR

CDS-04D-HipPitch-Assembly-Verification.md