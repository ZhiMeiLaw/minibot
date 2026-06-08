# Mini-Atlas V6 Alpha

# DR-009 Knee Architecture Review

Version: 1.0

Status: REVIEW

Review ID:

DR-009

Subsystem:

Knee Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

- MDS-02 Detailed Joint Design
- CDS-04 Hip Pitch Joint
- DR-007 Hip Pitch Torque Capacity Review
- DR-008 Hip Assembly Structural Review

---

# 1. Review Objective

冻结 Knee Joint 总体架构。

确定：

- Servo Selection
- Bearing Selection
- Joint Shaft
- Motion Range
- Lower Leg Interface
- Wheel Module Interface
- Torque Margin

通过后进入：

CDS-05A Knee_Base CAD Design

---

# 2. Functional Requirement

Knee 必须实现：

1. 支撑整机重量

2. 支撑动态行走载荷

3. 实现屈膝动作

4. 实现蹲下动作

5. 支撑轮组模块

6. 可长期连续运行

---

# 3. Architecture Options

## Option A

Direct Servo Knee

Servo

↓

Output

↓

Lower Leg

---

优点：

简单

便宜

---

缺点：

Servo承担全部载荷

寿命下降

---

结论：

REJECT

---

## Option B

Bearing Supported Knee

Servo

↓

Torque Module

↓

Output

↓

Joint Shaft

↓

Bearings

↓

Base

---

优点：

载荷与扭矩分离

寿命高

可靠

---

结论：

SELECTED

---

# 4. Servo Review

候选：

STS3215

STS3046

STS3250

---

## STS3215

约：

1.9 N·m

---

评估：

风险较高

---

结论：

REJECT

---

## STS3046

约：

3.0 N·m

---

评估：

满足需求

---

结论：

SELECTED

---

## STS3250

约：

5.0 N·m

---

评估：

性能过剩

重量增加

成本增加

---

结论：

NOT REQUIRED

---

# 5. Bearing Review

候选：

688

698

6800

6801

---

## 688

8×16×5

---

评估：

偏小

---

结论：

REJECT

---

## 698

8×19×6

---

评估：

与Hip Pitch统一

库存统一

强度充足

---

结论：

SELECTED

---

# 6. Joint Shaft Review

材料：

GCr15

轴承钢

---

直径：

8 mm

---

长度：

35 mm

---

结构：

双轴承支撑

---

结论：

APPROVED

---

# 7. Motion Range Review

人体膝关节：

约：

0°~135°

---

机器人需求：

无需完全模拟人体

---

建议：

Extension

0°

---

Flexion

120°

---

机械极限：

-5°

125°

---

结论：

APPROVED

---

# 8. Lower Leg Length Review

目标：

与 Upper Leg 对称

---

Upper Leg：

120 mm

---

Lower Leg：

120 mm

---

总腿长：

240 mm

---

结论：

APPROVED

---

# 9. Wheel Module Interface Review

方案：

Wheel Module

安装于 Lower Leg Bottom

---

优势：

结构简单

维护方便

---

结论：

APPROVED

---

# 10. Torque Capacity Review

估算载荷：

0.4~0.6 kg

---

峰值扭矩：

约：

2.2 N·m

---

STS3046：

约：

3.0 N·m

---

利用率：

73%

---

结论：

APPROVED

---

# 11. Mechanical Stop Review

必须配置：

Mechanical Stop

---

工作范围：

0°~120°

---

机械极限：

-5°~125°

---

结论：

APPROVED

---

# 12. Printability Review

平台：

Bambu Lab A1

---

兼容：

Bambu Lab A1 Mini

---

最大零件预计：

60 mm

---

结论：

APPROVED

---

# 13. Weight Budget

目标：

Knee Assembly

<180 g

---

预估：

Servo

62 g

---

Base

40 g

---

Output

30 g

---

Torque Module

22 g

---

Hardware

15 g

---

总计：

169 g

---

结论：

PASS

---

# 14. Risk Assessment

风险1：

Torque不足

---

缓解：

保留STS3250升级路径

---

风险2：

打印件疲劳

---

缓解：

Brass Insert

Rib Reinforcement

---

风险3：

轴承座磨损

---

缓解：

698 Press Fit

---

# 15. Freeze Summary

Servo

STS3046

---

Bearing

698-2RS ×2

---

Joint Shaft

Ø8 GCr15

---

Motion Range

0°~120°

---

Mechanical Limit

-5°~125°

---

Upper Leg

120 mm

---

Lower Leg

120 mm

---

Wheel Module

Bottom Mounted

---

Architecture

Bearing Supported Knee

---

Status

APPROVED

READY FOR

CDS-05A-Knee_Base-CAD-Design.md