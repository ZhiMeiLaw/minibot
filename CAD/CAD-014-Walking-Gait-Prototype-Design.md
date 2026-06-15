# Mini-Atlas V6 Alpha

# CAD-014 Walking Gait Prototype Design

Version: 1.0

Status: MOTION PROTOTYPE LAYER

Document Number:

CAD-014

Subsystem:

Gait Cycle & Motion Primitive Design

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 的最小可行步态（MVP Gait Model），用于：

* 验证是否可以连续行走
* 定义关节运动时序
* 建立 Hip-Knee 协调关系
* 支持后续控制系统开发

---

# 2. Core Concept

```text id="c1"
Walking = Time-Sequence of Controlled Imbalance
```

---

# 3. Gait Cycle Definition

## Full Cycle

```text id="g1"
STANCE → PUSH → SWING → LAND → TRANSFER
```

---

## Step Breakdown

### Phase 1: Stance

* 一只脚支撑
* 另一只脚准备离地
* CoM 位于支撑脚上方

---

### Phase 2: Push

* Hip Pitch 后移
* Knee 轻微伸展
* 重心前移

---

### Phase 3: Swing

FreeCAD

* 摆动腿抬起
* Hip Roll 稳定身体
* Knee 收缩减少碰撞风险

---

### Phase 4: Landing

* 脚接触地面
* Knee 吸收冲击
* Hip Pitch 重新校正

---

### Phase 5: Transfer

* 重心从旧支撑腿转移到新支撑腿
* 进入下一周期

---

# 4. Joint Coordination Model

## Hip Pitch

```text id="h1"
Primary forward propulsion actuator
```

---

## Hip Roll

```text id="h2"
Lateral stability controller
```

---

## Knee

```text id="h3"
Shock absorption + swing clearance control
```

---

# 5. Timing Model (Gait Timeline)

```text id="t1"
T0: stance start
T1: weight shift
T2: swing lift
T3: swing forward
T4: landing
T5: transfer complete
```

---

# 6. Stability Principle

```text id="s1"
At least one foot must always support CoM projection
```

---

# 7. Motion Constraints

## Constraint 1: No Ground Collision

* Swing foot must stay within clearance envelope

---

## Constraint 2: No CG Escape

* CoM must remain inside support polygon

---

## Constraint 3: Smooth Transfer

* No abrupt torque spikes allowed

---

# 8. Minimum Viable Gait

```text id="m1"
Slow alternating step gait
```

Characteristics:

* Low speed
* High stability margin
* Large support overlap

---

# 9. Failure Modes

## Failure 1: Tip Over

→ CoM exits support polygon

---

## Failure 2: Swing Collision

→ knee insufficient clearance

---

## Failure 3: Torque Saturation

→ hip pitch overload

---

# 10. Design Implications for CAD

Gait directly impacts CAD:

* Hip range must support swing arc
* Knee must allow high flexion
* Pelvis must maintain rigidity under oscillation

---

# 11. System Integration

```text id="i1"
CAD Structure
    ↓
Gait Model
    ↓
Control System (future)
```

---

# 12. Key Insight

```text id="k1"
Walking is not geometry problem anymore — it is timing + stability problem
```

---

# 13. Readiness Assessment

| Capability             | Status          |
| ---------------------- | --------------- |
| Static Standing        | PASS            |
| Dynamic Balance        | CONDITIONAL     |
| Step Motion Definition | PASS            |
| Continuous Walking     | NOT IMPLEMENTED |

---

# 14. Next Step

进入：

```text id="n1"
CAD-015-Control-System-Architecture-PreDesign.md
```

目标：

👉 将 gait model 转换为控制系统
👉 引入 PID / balance control
👉 定义 servo control layer
👉 从“动作设计”进入“控制系统设计”

---

# 15. Status

Gait Prototype:

APPROVED (EARLY MODEL)

System State:

```text id="st1"
MOTION MODEL DEFINED — CONTROL SYSTEM REQUIRED
```
