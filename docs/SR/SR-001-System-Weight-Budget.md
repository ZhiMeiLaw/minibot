# Mini-Atlas V6 Alpha

# SR-001 System Weight Budget

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

SR-001

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* BOM-01 Master Bill Of Materials
* DR-010 Leg Subsystem Review
* DR-012 Leg Kinematics & Torque Validation
* EDS-02 Power Budget & Current Analysis

---

# 1. Purpose

建立整机重量预算。

用于：

* 验证 STS3046 是否足够
* 验证续航能力
* 验证步态能力
* 控制设计范围
* 作为所有后续设计约束

---

# 2. Weight Philosophy

V6 Alpha 目标：

优先实现：

* 可制造
* 可行走
* 可维护

而不是：

* 极限性能
* 高速运动

---

因此：

重量控制优先级：

HIGH

---

# 3. System Weight Targets

## Stretch Goal

≤ 3.5 kg

---

## Target

≤ 4.0 kg

---

## Maximum Acceptable

≤ 4.5 kg

---

## Design Limit

5.0 kg

---

超过 5 kg：

必须重新评审

Hip Pitch 架构

---

# 4. Weight Budget Allocation

| Subsystem     |  Target |
| ------------- | ------: |
| Left Leg      | 0.80 kg |
| Right Leg     | 0.80 kg |
| Pelvis        | 0.40 kg |
| Battery       | 0.40 kg |
| Electronics   | 0.20 kg |
| Torso Frame   | 0.50 kg |
| Arms (Future) | 0.40 kg |
| Head          | 0.20 kg |
| Covers        | 0.20 kg |

---

Target Total

≈3.90 kg

---

结果：

PASS

---

# 5. Leg Weight Budget

单腿：

目标：

≤800 g

---

当前：

≈798 g

---

Margin：

≈2 g

---

结果：

WARNING

---

说明：

后续 CAD 必须严格控制重量

---

# 6. Pelvis Weight Budget

组成：

Pelvis Frame

Battery Bay

PDB

Buck Modules

Mount Plates

---

目标：

≤400 g

---

推荐：

350 g

---

结果：

PASS

---

# 7. Battery Weight Budget

方案：

3S2P 18650

Samsung 30Q

---

单节：

≈48 g

---

总计：

6 Cells

---

电芯：

288 g

---

支架

线材

XT30

---

总计：

≈350~400 g

---

结果：

PASS

---

# 8. Electronics Budget

组成：

ESP32

IMU

PDB

Buck

Power Switch

Connectors

---

目标：

≤200 g

---

推荐：

150 g

---

结果：

PASS

---

# 9. Torso Budget

组成：

Carbon Tube

Printed Frame

Mounts

Fasteners

---

目标：

≤500 g

---

推荐：

450 g

---

结果：

PASS

---

# 10. Head Budget

组成：

Camera

ESP32-CAM

Frame

Shell

---

目标：

≤200 g

---

推荐：

150 g

---

结果：

PASS

---

# 11. Cover Budget

外壳：

PETG

---

目标：

≤200 g

---

推荐：

150 g

---

结果：

PASS

---

# 12. Servo Weight Analysis

STS3046

≈62 g

---

数量：

6

---

总计：

372 g

---

占整机：

≈9.5 %

---

结果：

合理

---

# 13. Battery Percentage Analysis

Battery

≈380 g

---

占整机：

≈9.7 %

---

结果：

合理

---

# 14. Leg Percentage Analysis

双腿：

≈1.60 kg

---

占整机：

≈41 %

---

结果：

合理

---

# 15. Center Of Mass Target

目标：

重心位于：

Pelvis 中心

↓

向下 20~50 mm

---

原因：

提高稳定性

降低 Hip Torque

---

结果：

PASS

---

# 16. Hip Pitch Impact Analysis

## Weight = 3.5 kg

Hip Pitch 利用率

≈70 %

---

状态：

GOOD

---

## Weight = 4.0 kg

Hip Pitch 利用率

≈80 %

---

状态：

ACCEPTABLE

---

## Weight = 4.5 kg

Hip Pitch 利用率

≈90 %

---

状态：

WARNING

---

## Weight = 5.0 kg

Hip Pitch 利用率

≈97 %

---

状态：

CRITICAL

---

# 17. Design Rules

Rule 1

新增零件必须记录重量

---

Rule 2

每个 CAD Part 必须估重

---

Rule 3

每次 Freeze 必须更新 Weight Table

---

Rule 4

禁止无重量预算设计

---

# 18. Manufacturing Impact

若超重：

优先优化：

* Covers
* Torso
* Pelvis

---

禁止优化：

* Bearing
* Shaft
* Fasteners

---

原因：

这些影响可靠性

---

# 19. Future Upgrade Impact

升级：

STS3250

---

预计增加：

约 20~30 g / Servo

---

总增加：

≈120~180 g

---

仍可接受

---

# 20. Freeze Summary

Stretch Goal

≤3.5 kg

---

Target

≤4.0 kg

---

Maximum

≤4.5 kg

---

Design Limit

5.0 kg

---

Leg Budget

0.80 kg / Leg

---

Battery Budget

0.40 kg

---

Pelvis Budget

0.40 kg

---

Torso Budget

0.50 kg

---

Electronics Budget

0.20 kg

---

Status

APPROVED

READY FOR

CDS-08 Dual Leg & Pelvis Integration
