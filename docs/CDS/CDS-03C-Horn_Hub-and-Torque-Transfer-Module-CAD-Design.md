# Mini-Atlas V6 Alpha

# CDS-03C Horn_Hub & Torque Transfer Module CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Parent Assembly:

V6-ASM-0001 Hip Roll Assembly

Part Number:

V6-PRT-0003

Part Name:

Horn_Hub_Torque_Module

Related Documents:

CDS-03 Hip Roll Joint CAD Design

CDS-03A HipRoll_Base CAD Design

CDS-03B HipRoll_Output CAD Design

DR-003 Torque Transfer Design Review

---

# 1. Purpose

本文件用于冻结：

- Servo Spline Interface（舵机花键接口）
- Aluminum Horn（铝合金舵盘）
- Horn Hub（联接Hub）
- Double Clamp（双夹紧机构）
- Mechanical Stop（机械限位）
- Torque Transfer Path（扭矩传递路径）
- Servo Quick Replacement（舵机快速更换）

这是：

Mini-Atlas V6 Alpha

Hip Roll关节中最关键的动力传递模块。

---

# 2. Design Philosophy

原则：

Servo Never Carries Structural Load

舵机永远不承受结构载荷

---

正确载荷路径：

Robot Weight
↓
Carbon Tube
↓
HipRoll_Output
↓
Joint Shaft
↓
688 Bearings
↓
HipRoll_Base

---

正确扭矩路径：

STS3046
↓
Aluminum Horn
↓
Horn Hub
↓
HipRoll_Output
↓
Carbon Tube

---

禁止：

Robot Weight
↓
Horn
↓
Servo Output Shaft

---

# 3. Torque Requirements

Servo：

STS3046

---

额定扭矩：

约30kg·cm

≈3N·m

---

设计目标：

Torque Capacity

≥6N·m

---

安全系数：

2.0

---

# 4. Module Architecture

结构：

STS3046
│
├─ Aluminum Horn
│
├─ Horn Hub
│
├─ Double Clamp
│
│
└─ HipRoll_Output

---

剖面图：

          M3
           ▼

    ┌───────────┐
    │ Horn Hub  │
    └─────┬─────┘
          │
      Aluminum
        Horn
          │
      STS3046

---

# 5. Servo Spline Standard

Servo：

STS3046

---

冻结：

使用原厂输出花键

---

禁止：

修改输出轴

磨削花键

胶水固定

---

要求：

100%兼容原厂Horn

---

# 6. Horn Selection

冻结：

Original Aluminum Horn

原厂铝合金舵盘

---

禁止：

Plastic Horn

塑料舵盘

---

原因：

塑料长期存在：

蠕变

变形

定位误差

---

# 7. Horn Dimensions

参考尺寸：

外径：

25 mm

---

厚度：

3 mm

---

中心：

STS3046 Spline

---

固定：

Center Screw

---

# 8. Horn Hub Design

Part Number

V6-PRT-0003

---

材料：

PETG

Alpha Prototype

---

Beta版本：

6061 Aluminum

---

外径：

28 mm

---

厚度：

10 mm

---

中心孔：

Horn Pocket

---

深度：

3.5 mm

---

配合：

Slip Fit

---

间隙：

0.1 mm

---

# 9. Double Clamp Design

采用：

Double Split Clamp

双夹紧结构

---

结构：

Top View

      M3

       ▼

 ┌─────────────┐
 │             │
 │     HUB     │
 │             │
 └─┬───────┬───┘
   │       │
   ▼       ▼

  M3       M3

---

夹缝宽度：

1.5 mm

---

夹紧螺丝：

M3 × 12

---

数量：

2

---

# 10. Hub to Output Connection

连接：

Horn Hub

↓

HipRoll_Output

---

方式：

4 Bolt Pattern

---

螺丝：

M3 × 10

---

数量：

4

---

PCD：

18 mm

---

孔径：

3.2 mm

---

均布：

90°

---

# 11. Torque Transfer Verification

设计扭矩：

6N·m

---

M3×4连接：

可承受：

远大于10N·m

---

满足：

STS3046全部输出能力

---

# 12. Mechanical Stop

必须增加：

Mechanical Stop

机械限位

---

原因：

防止程序异常

防止舵机打齿

---

工作范围：

±25°

---

机械极限：

±30°

---

保留：

5°

安全余量

---

# 13. Mechanical Stop Design

Base侧：

增加 Stop Block

---

Output侧：

增加 Stop Tab

---

示意：

        Stop Tab

            ▼

 ┌──────────────┐
 │              │
 │              │
 │              │
 └─────┬────────┘
       │
       │
 Stop Block

---

接触面厚度：

4 mm

---

接触长度：

8 mm

---

# 14. Quick Replacement Design

要求：

无需拆腿

即可拆舵机

---

流程：

Step 1

拆4颗M2.5

---

Step 2

拆Horn Screw

---

Step 3

取出Servo

---

时间：

<5分钟

---

# 15. Fastener Standard

Hub Clamp：

M3 × 12

---

Output Connection：

M3 × 10

---

Horn Center Screw：

原厂

---

Servo Mount：

M2.5 × 8

---

# 16. Threadlocker Requirement

冻结：

Loctite 243

Blue Threadlocker

---

使用位置：

Hub Clamp

---

Output Connection

---

Horn Screw

---

禁止：

永久胶

红胶

---

# 17. Maintenance Specification

每20小时：

检查：

Hub Clamp

Horn Screw

---

每50小时：

检查：

Horn磨损

Spline间隙

---

# 18. Estimated Weight

Aluminum Horn

5 g

---

Horn Hub

8 g

---

Fasteners

6 g

---

Total

≈19 g

---

目标：

<20 g

---

# 19. CAD Modeling Sequence

Step 1

Import STS3046

---

Step 2

Import Aluminum Horn

---

Step 3

Build Horn Pocket

---

Step 4

Build Double Clamp

---

Step 5

Build Mechanical Stop

---

Step 6

Assembly Verification

---

# 20. Verification Checklist

CAD验证：

□ Horn安装正常

□ Hub安装正常

□ Clamp可锁紧

□ ±25°无干涉

□ ±30°机械限位生效

□ Servo可拆卸

□ Torque Path闭环

---

打印验证：

□ Horn无松动

□ Clamp无开裂

□ Servo正常工作

□ 无打滑

---

# 21. Future Upgrade Compatibility

兼容：

STS3046

STS3215

---

预留：

STS3250

STS3255

---

仅需修改：

Horn Pocket

---

无需修改：

HipRoll_Base

HipRoll_Output

Carbon Interface

---

# 22. Freeze Summary

Torque Architecture

Servo
↓
Aluminum Horn
↓
Double Clamp Hub
↓
HipRoll_Output

---

Horn

Original Aluminum Horn

---

Hub

Double Clamp

---

Mechanical Stop

Required

---

Threadlocker

Loctite 243

---

Weight

≈19 g

---

Status

APPROVED

READY FOR

CDS-03D Hip Roll Assembly Verification

READY FOR

Full Hip Roll CAD Assembly