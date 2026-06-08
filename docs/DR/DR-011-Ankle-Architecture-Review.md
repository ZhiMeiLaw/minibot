# Mini-Atlas V6 Alpha

# DR-011 Ankle Architecture Review

Version: 1.0 Freeze A

Status: REVIEW

Review Number:

DR-011

Subsystem:

Ankle Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* DR-010 Leg Subsystem Review
* CDS-03 Hip Roll Joint
* CDS-04 Hip Pitch Joint
* CDS-05 Knee Joint
* MDS-01 System Architecture
* EDS-02 Power Budget & Current Analysis

---

# 1. Review Objective

冻结 Ankle 架构。

确定：

* 是否保留 Ankle Pitch
* 是否保留 Ankle Roll
* Wheel Module 安装方式
* 足部结构方案
* Wheel Assisted Gait 架构

通过后进入：

CDS-06 Ankle Joint CAD Design

---

# 2. Current Leg Architecture

当前：

Hip Roll

↓

Hip Pitch

↓

Knee

↓

Lower Leg

↓

Ankle

↓

Wheel / Foot

---

已冻结：

Hip Roll

STS3046

---

Hip Pitch

STS3046

---

Knee

STS3046

---

# 3. Design Requirements

V6 Alpha 必须实现：

* 原地站立
* 前进
* 后退
* 转向
* 轮式辅助移动
* 基础越障

---

V6 Alpha 不要求：

* 跑步
* 跳跃
* 后空翻
* 动态平衡控制

---

结论：

优先可靠性

而非仿生自由度

---

# 4. Candidate Architecture

方案A

Ankle Pitch + Ankle Roll

双自由度踝关节

---

方案B

仅 Ankle Pitch

单自由度踝关节

---

方案C

Rigid Wheel Mount

无踝关节

---

# 5. Option A Review

Ankle Pitch

*

Ankle Roll

---

总自由度：

5 DOF

Per Leg

---

优点：

接近人类

地形适应强

---

缺点：

增加：

1 Servo

*

1 Bearing Pair

*

1 Torque Module

*

大量控制复杂度

---

重量增加：

约：

150 g / Leg

---

成本增加：

约：

150 RMB / Leg

---

结论：

REJECT

---

# 6. Option B Review

Ankle Pitch

Only

---

总自由度：

4 DOF

Per Leg

---

优点：

可调整脚掌角度

可改善步态

---

缺点：

控制收益有限

成本仍较高

---

重量增加：

约：

150 g / Leg

---

结论：

NOT RECOMMENDED

---

# 7. Option C Review

Rigid Wheel Mount

刚性轮组安装

---

结构：

Lower Leg

↓

Wheel Module

---

无 Ankle Servo

---

优点：

最轻

最简单

最可靠

最低成本

---

缺点：

不具备脚踝动作

---

评估：

符合 V6 Alpha 目标

---

结论：

SELECTED

---

# 8. Wheel Assisted Gait Review

采用：

Wheel Assisted Walking

---

模式1：

Walking

步行

---

模式2：

Wheel Mode

轮式移动

---

模式3：

Hybrid

低速步行

*

轮辅助

---

结论：

APPROVED

---

# 9. Wheel Location Review

安装位置：

Lower Leg Bottom

---

方式：

Rigid Mount

---

接口：

4 × M3

---

安装板：

Wheel Adapter Plate

---

结论：

APPROVED

---

# 10. Wheel Size Review

候选：

60 mm

---

80 mm

---

100 mm

---

评估：

60 mm

离地间隙不足

---

100 mm

比例过大

---

80 mm

最佳

---

结论：

SELECTED

---

# 11. Wheel Motor Review

候选：

N20

---

GB37-520

---

评估：

N20扭矩不足

---

GB37-520成熟可靠

---

结论：

SELECTED

---

# 12. Ground Clearance Review

Wheel Diameter：

80 mm

---

Wheel Radius：

40 mm

---

Lower Leg Offset：

20 mm

---

Ground Clearance：

约20 mm

---

评估：

满足室内环境

---

结论：

PASS

---

# 13. Weight Review

Ankle Servo方案：

增加约：

300 g

双腿

---

Rigid Wheel方案：

增加约：

140 g

双腿

---

节省：

约160 g

---

结论：

PASS

---

# 14. Power Review

Ankle Servo方案：

额外峰值电流：

约：

4~6 A

---

Rigid Wheel方案：

0 A

---

结论：

PASS

---

# 15. Reliability Review

Rigid Wheel：

活动件最少

---

故障点最少

---

维护最简单

---

结论：

PASS

---

# 16. Future Upgrade Path

预留：

Ankle Pitch

升级空间

---

方式：

Wheel Adapter

↓

Ankle Module

↓

Lower Leg

---

兼容：

V6 Beta

---

结论：

APPROVED

---

# 17. Final Architecture

Hip Roll

↓

Hip Pitch

↓

Knee

↓

Lower Leg

↓

Wheel Adapter

↓

80 mm Wheel

---

无 Ankle Servo

---

无 Ankle Bearing

---

无 Ankle Torque Module

---

# 18. System Impact

单腿：

3 DOF

---

双腿：

6 DOF

---

全机：

6 DOF

*

Wheel Drive

---

符合：

V6 Alpha MVP

---

# 19. Freeze Summary

Ankle Pitch

REMOVED

---

Ankle Roll

REMOVED

---

Wheel Mount

Rigid

---

Wheel Diameter

80 mm

---

Wheel Motor

GB37-520

---

Wheel Interface

4×M3

---

Architecture

Wheel Assisted Walker

---

Status

APPROVED

READY FOR

CDS-06-Wheel-Module-Architecture.md
