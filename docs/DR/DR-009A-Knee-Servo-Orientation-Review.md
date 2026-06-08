# Mini-Atlas V6 Alpha

# DR-009A Knee Servo Orientation Review

Version: 1.0

Status: REVIEW

Subsystem:

Knee Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

- DR-009 Knee Architecture Review
- CDS-04 Hip Pitch Joint
- MDS-02 Detailed Joint Design

---

# 1. Review Objective

冻结 Knee Servo 安装方向。

决定：

STS3046 在 Knee 中的空间布局。

---

# 2. Design Constraints

当前冻结：

Upper Leg

120 mm

---

Lower Leg

120 mm

---

Servo

STS3046

---

Bearing

698-2RS ×2

---

Joint Shaft

Ø8 mm

---

# 3. Candidate Architecture

方案A：

Parallel Layout

舵机与腿平行

---

方案B：

Perpendicular Layout

舵机与腿垂直

---

# 4. Option A

Parallel Layout

示意：

Side View

Hip Pitch

    │

    │

┌─────────┐
│STS3046  │
└─────────┘

    │

 Knee Axis

    │

 Lower Leg

---

特点：

Servo 长边方向

与腿方向一致

---

优点：

腿部宽度小

重心集中

外观接近 Atlas

走线简单

维护方便

---

缺点：

结构设计稍复杂

---

# 5. Option B

Perpendicular Layout

示意：

Front View

      STS3046

 ┌─────────────┐
 │             │
 └─────────────┘

        │

     Knee Axis

        │

     Lower Leg

---

特点：

Servo 横向放置

---

优点：

设计简单

---

缺点：

腿部变宽

碰撞风险增加

重心变差

---

# 6. Width Analysis

STS3046 尺寸：

约：

40 mm

---

方案A：

腿宽

≈50 mm

---

方案B：

腿宽

≈80 mm

---

结果：

方案A 优势明显

---

# 7. Collision Analysis

最大动作：

Knee Flexion

120°

---

方案A：

基本无干涉

---

方案B：

容易碰撞：

Hip Pitch

Wheel Module

Ground

---

结果：

方案A 更优

---

# 8. Center Of Mass Analysis

方案A：

重心靠近腿中心线

---

方案B：

重心偏离中心线

---

结果：

方案A 更优

---

# 9. Maintenance Analysis

方案A：

拆4颗螺丝

即可更换

---

方案B：

拆装更复杂

---

结果：

方案A 更优

---

# 10. Atlas Reference

现代人形机器人：

Atlas

Unitree H1

Figure 02

Tesla Optimus

---

全部采用：

近似 Parallel Layout

---

结论：

符合行业最佳实践

---

# 11. Freeze Decision

Selected Architecture:

Parallel Layout

---

Servo Orientation:

Long Side

Parallel To Leg

---

Bearing:

698 ×2

---

Joint Shaft:

Ø8 mm

---

Status:

APPROVED