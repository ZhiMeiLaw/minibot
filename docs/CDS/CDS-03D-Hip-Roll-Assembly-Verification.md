# Mini-Atlas V6 Alpha

# CDS-03D Hip Roll Assembly Verification

Version: 1.0 Freeze A

Status: APPROVED

Assembly Number:

V6-ASM-0001

Assembly Name:

Hip Roll Assembly

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

- CDS-03 Hip Roll Joint CAD Design
- CDS-03A HipRoll_Base CAD Design
- CDS-03B HipRoll_Output CAD Design
- CDS-03C Torque-Transfer-Module CAD Design
- CDS-02A Standard Component Library Revision A
- MDS-02 Detailed Joint Design
- MDS-03 Assembly Specification

---

# 1. Purpose

本文件用于验证：

```text
HipRoll_Base
+
HipRoll_Output
+
Torque Transfer Module
+
STS3046
+
688 Bearings
+
Ø8 Shaft
```

组成的 Hip Roll 总成是否满足：

- 结构强度
- 装配性
- 可维护性
- 运动范围
- 制造可行性
- 成本目标
- 重量目标

通过本文件后：

```text
Hip Roll Joint
```

正式冻结（Design Freeze）。

---

# 2. Assembly Overview

总成结构：

```text

                 Pelvis

                    │

                    ▼

          ┌─────────────────┐
          │ HipRoll_Base    │
          └───────┬─────────┘
                  │
          ┌───────┴────────┐
          │ 688 Bearing #1 │
          └───────┬────────┘
                  │
               Ø8 Shaft
                  │
          ┌───────┴────────┐
          │ 688 Bearing #2 │
          └───────┬────────┘
                  │
          ┌───────┴────────┐
          │ HipRoll_Output │
          └───────┬────────┘
                  │
          Torque Module
                  │
             STS3046
                  │
          Carbon Tube
                  │
              Upper Leg

```

---

# 3. Functional Verification

## Requirement 01

Hip Roll Rotation

目标：

```text
±25°
```

验证：

```text
PASS
```

说明：

机械限位设计：

```text
±30°
```

留有：

```text
5°
```

安全余量。

---

## Requirement 02

Servo Torque Transfer

目标：

```text
无打滑
```

验证：

```text
PASS
```

方案：

```text
Aluminum Horn
+
Double Clamp Hub
```

满足要求。

---

## Requirement 03

Weight Support

目标：

```text
支撑整条腿
```

验证：

```text
PASS
```

原因：

载荷经过：

```text
Shaft
+
Bearings
```

不经过舵机输出轴。

---

# 4. Load Path Verification

正确路径：

```text

Robot Weight

      │

      ▼

 Carbon Tube

      │

      ▼

HipRoll_Output

      │

      ▼

   Ø8 Shaft

      │

      ▼

 688 Bearings

      │

      ▼

HipRoll_Base

      │

      ▼

    Pelvis

```

---

验证：

```text
PASS
```

---

禁止路径：

```text

Robot Weight

      │

      ▼

Servo Horn

      │

      ▼

STS3046

```

---

验证：

```text
PASS

不存在该路径
```

---

# 5. Torque Path Verification

正确路径：

```text

STS3046

   │

   ▼

Aluminum Horn

   │

   ▼

 Horn Hub

   │

   ▼

HipRoll_Output

   │

   ▼

Carbon Tube

```

---

验证：

```text
PASS
```

---

# 6. Bearing Verification

标准件：

```text
688-2RS
```

规格：

```text
8×16×5
```

数量：

```text
2
```

---

轴承间距：

```text
20 mm
```

---

检查项：

```text
抗弯能力
```

结果：

```text
PASS
```

---

检查项：

```text
安装空间
```

结果：

```text
PASS
```

---

检查项：

```text
采购便利性
```

结果：

```text
PASS
```

---

# 7. Shaft Verification

规格：

```text
Ø8 GCr15
```

---

长度：

```text
30 mm
```

---

检查：

```text
与688匹配
```

结果：

```text
PASS
```

---

检查：

```text
加工难度
```

结果：

```text
PASS
```

---

# 8. Carbon Tube Interface Verification

标准：

```text
OD 10mm × ID 8mm Carbon Tube
```

---

插入深度：

```text
15 mm
```

---

夹持方式：

```text
Split Clamp
```

---

验证：

```text
PASS
```

---

检查：

```text
可拆卸
```

结果：

```text
PASS
```

---

# 9. Mechanical Stop Verification

工作角度：

```text
±25°
```

---

机械极限：

```text
±30°
```

---

结果：

```text
PASS
```

---

说明：

程序失效时：

```text
Stop Block
```

保护舵机。

---

# 10. Assembly Sequence Verification

步骤：

```text
Base
↓
Bearings
↓
Shaft
↓
Output
↓
Hub
↓
Horn
↓
Servo
```

---

验证：

```text
PASS
```

---

无反向装配问题。

---

# 11. Serviceability Verification

目标：

```text
<5分钟
更换舵机
```

---

步骤：

```text
拆4颗M2.5
拆Horn Screw
取出Servo
```

---

结果：

```text
PASS
```

---

# 12. Tolerance Stack-up Review

关键尺寸链：

```text

688 ID

 8.000

     ↓

Ø8 Shaft

 7.98~8.00

     ↓

Output Bore

 8.10

```

---

结果：

```text
PASS
```

---

无过盈风险。

---

# 13. Interference Check

检查：

```text
Base vs Output
```

结果：

```text
PASS
```

---

检查：

```text
Servo vs Base
```

结果：

```text
PASS
```

---

检查：

```text
Hub vs Base
```

结果：

```text
PASS
```

---

检查：

```text
Carbon Tube vs Pelvis
```

结果：

```text
PASS
```

---

# 14. Manufacturing Review

材料：

```text
PETG
```

---

打印方向：

符合 CDS-03A

CDS-03B

要求。

---

结果：

```text
PASS
```

---

# 15. Cost Review

Hip Roll Joint：

| Item | Cost (RMB) |
|--------|--------:|
| STS3046 | 85 |
| 688 ×2 | 2 |
| Shaft | 3 |
| Screws | 2 |
| Inserts | 1 |
| PETG | 3 |
| Carbon Tube | 5 |

---

总计：

```text
≈101 RMB
```

---

结果：

```text
PASS
```

---

# 16. Weight Review

| Item | Weight |
|--------|--------:|
| STS3046 | 62 g |
| Base | 35 g |
| Output | 23 g |
| Bearings | 4 g |
| Shaft | 8 g |
| Fasteners | 8 g |
| Carbon Tube | 6 g |

---

总计：

```text
≈146 g
```

---

目标：

```text
<160 g
```

---

结果：

```text
PASS
```

---

# 17. Risk Assessment

## Risk 01

Horn Loosening

等级：

Medium

---

缓解：

```text
Loctite 243
```

---

## Risk 02

PETG Clamp Crack

等级：

Medium

---

缓解：

```text
增加圆角
```

---

## Risk 03

Bearing Pocket Too Tight

等级：

Low

---

缓解：

```text
16.05 mm Pocket
```

---

# 18. Validation Plan

Phase 1

Bench Test

---

项目：

```text
±25°
连续摆动
```

---

时间：

```text
1小时
```

---

Phase 2

Static Load Test

---

负载：

```text
2 kg
```

---

时间：

```text
30分钟
```

---

Phase 3

Walking Test

---

目标：

```text
1000步
```

---

# 19. Assembly Freeze

Hip Roll Joint：

```text
DESIGN APPROVED
```

---

进入：

```text
CAD Modeling
```

---

进入：

```text
Prototype Manufacturing
```

---

进入：

```text
Bench Validation
```

---

# 20. Final Freeze Summary

Assembly

```text
V6-ASM-0001
```

---

Joint

```text
Hip Roll
```

---

Servo

```text
STS3046
```

---

Bearing

```text
688-2RS ×2
```

---

Shaft

```text
Ø8 GCr15
```

---

Carbon Tube

```text
OD 10mm × ID 8mm
```

---

Weight

```text
≈146 g
```

---

Cost

```text
≈101 RMB
```

---

Status

```text
HIP ROLL DESIGN FREEZE COMPLETE

READY FOR CDS-04
Hip Pitch Joint CAD Design
```
