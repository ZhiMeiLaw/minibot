# Mini-Atlas V6 Alpha

# CAD-011 Dynamic Walking Pre-Architecture

Version: 1.0

Status: MOTION SYSTEM DESIGN GATE

Document Number:

CAD-011

Subsystem:

Pre-Gait Architecture System

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 在进入控制系统之前的**步态结构基础架构**，包括：

* 步态生成逻辑
* 重心（CoM）运动策略
* 支撑多边形控制
* Hip compensation机制
* 单脚支撑可行性结构

---

# 2. System Transition

```text id="t1"
STRUCTURE (CAD-010)
        ↓
MOTION ARCHITECTURE (CAD-011)
        ↓
CONTROL SYSTEM (FUTURE)
```

---

# 3. Core Walking Principle

```text id="p1"
Walking = Controlled Falling
```

系统目标：

* 允许重心偏移
* 通过换脚维持稳定
* 连续破坏 + 重建平衡

---

# 4. Support Polygon Model

FreeCAD

## Static State

```text id="s1"
Both feet support polygon
```

---

## Dynamic State

```text id="s2"
Single foot support polygon
```

关键：

* 重心必须始终落在当前支撑区域内

---

# 5. Center of Mass (CoM) Strategy

## CoM Rule

```text id="c1"
CoM must remain inside support polygon projection
```

---

## CoM Shift Phases

### Phase 1: Double Support

* CoM centered
* Stability high

---

### Phase 2: Transfer Phase

* CoM moves toward support leg
* Hip Roll compensates

---

### Phase 3: Single Support

* CoM fully over one leg
* Knee absorbs load

---

# 6. Hip Compensation System

## Hip Roll Role

```text id="h1"
Lateral balance control
```

---

## Hip Pitch Role

```text id="h2"
Forward/backward balance control
```

---

## Combined Function

```text id="h3"
Hip = Real-time CoM correction actuator
```

---

# 7. Step Cycle Definition

```text id="sc1"
1. Shift weight to support leg
2. Lift swing leg
3. Move swing leg forward
4. Place swing leg
5. Transfer weight
6. Repeat
```

---

# 8. Swing Leg Dynamics

## Constraints

* Must avoid ground collision
* Must not destabilize pelvis
* Must maintain clearance envelope

---

## Swing Envelope Rule

```text id="sw1"
Leg trajectory must stay within safe 3D cone
```

---

# 9. Stability Control Zones

## Zone A: Stable

* Double support
* Low risk

---

## Zone B: Transitional

* Weight shifting
* Medium risk

---

## Zone C: Critical

* Single support
* High risk of tipping

---

# 10. Mechanical Preconditions for Walking

系统必须满足：

* Hip Roll torque sufficient for lateral correction
* Knee can support full body weight
* Pelvis rigid under torsion
* Foot contact stable

---

# 11. Failure Modes

## Failure 1: Lateral Tip

→ insufficient hip roll torque

---

## Failure 2: Forward Collapse

→ CoM too far ahead

---

## Failure 3: Swing Instability

→ leg swing disturbs balance

---

# 12. Architecture Requirement

必须预留：

* real-time CoM correction capability
* pelvis rigid-body assumption
* hip as primary stabilization actuator

---

# 13. System Readiness Level

| Capability         | Status          |
| ------------------ | --------------- |
| Static Standing    | PASS            |
| Weight Transfer    | PASS            |
| Single Leg Support | CONDITIONAL     |
| Dynamic Walking    | NOT IMPLEMENTED |

---

# 14. Design Conclusion

```text id="c1"
Robot is now structurally capable of walking, but lacks control system implementation
```

---

# 15. Next Step

进入：

```text id="n1"
CAD-012-Actuator-Torque-and-Gait-Feasibility.md
```

目标：

👉 验证 servo torque 是否支撑步态
👉 计算真实负载裕度
👉 判断是否“能真正走”
👉 进入动力学可行性阶段

---

# 16. Status

Walking Architecture:

APPROVED (PRE-CONTROL LAYER)

System State:

```text id="st1"
MOTION ARCHITECTURE DEFINED — CONTROL SYSTEM REQUIRED
```
