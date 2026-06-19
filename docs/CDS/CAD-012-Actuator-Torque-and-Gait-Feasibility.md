# Mini-Atlas V6 Alpha

# CAD-012 Actuator Torque and Gait Feasibility

Version: 1.0

Status: PHYSICAL FEASIBILITY GATE

Document Number:

CAD-012

Subsystem:

Actuation & Torque Validation

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 是否在真实物理条件下：

* 能否支撑自身重量
* 能否完成单脚支撑
* 能否完成基础步态
* 扭矩是否在舵机安全范围内

---

# 2. System Under Test

FreeCAD

```text id="s1"
Full Body Robot
    ↓
Hip Roll / Hip Pitch / Knee Actuators
    ↓
Static + Dynamic Load
```

---

# 3. Core Question

```text id="q1"
Can servos actually support walking loads?
```

---

# 4. Load Model

## Body Weight Assumption

```text id="w1"
Total Mass = M_robot
```

分布：

* Torso: 40%
* Pelvis: 20%
* Each leg: 20%

---

## Single Leg Support Load

```text id="l1"
F_leg ≈ 0.5 × M_robot × g
```

---

# 5. Joint Torque Model

## Hip Pitch Torque

```text id="t1"
T = F × L
```

Where:

* F = body weight load
* L = hip lever arm

---

## Hip Roll Torque

```text id="t2"
T = lateral shift × mass × gravity
```

---

## Knee Torque

```text id="t3"
T = vertical support load × shin length
```

---

# 6. Servo Constraint Model

## Example Servo Class

STS3046 servo

Typical limits:

```text id="s2"
Torque_max ≈ 3.0 – 4.0 kg·cm (example class)
```

---

## Critical Condition

```text id="c1"
T_required < T_max × Safety_Factor
```

Safety factor:

```text id="sf1"
0.6 ~ 0.7 recommended
```

---

# 7. Feasibility Check

## Hip Pitch

* Load: HIGH
* Risk: CRITICAL

---

## Knee

* Load: HIGH during stance
* Risk: CRITICAL

---

## Hip Roll

* Load: MEDIUM
* Risk: MANAGEABLE

---

# 8. System-Level Findings

## Observation 1

```text id="o1"
Hip Pitch is the limiting factor
```

---

## Observation 2

```text id="o2"
Knee load spikes during single support phase
```

---

## Observation 3

```text id="o3"
Pelvis mass directly amplifies torque demand
```

---

# 9. Design Implications

## Required Adjustments

* Reduce upper body mass
* Lower center of mass
* Shorten hip lever arm
* Increase servo torque class

---

# 10. Feasibility Classification

| System State       | Result           |
| ------------------ | ---------------- |
| Static Standing    | PASS             |
| Weight Transfer    | PASS             |
| Single Leg Support | CONDITIONAL      |
| Walking            | RISKY / UNSTABLE |

---

# 11. Key Conclusion

```text id="c2"
Current actuator selection is marginal for stable dynamic walking
```

---

# 12. System Decision

机器人当前状态：

* ❌ 不适合高速步态
* ⚠️ 可低速“实验步态”
* ✔ 结构成立

---

# 13. Required Next Action

必须进入优化阶段：

* Actuator upgrade strategy
* Mass reduction plan
* Geometry leverage redesign

---

# 14. Next Step

进入：

```text id="n1"
CAD-013-Optimization-and-Redesign-Loop.md
```

目标：

👉 减重策略
👉 力矩优化
👉 几何重设计
👉 提升 walking feasibility

---

# 15. Status

Feasibility Assessment:

APPROVED (BUT CONSTRAINED)

System State:

```text id="st1"
STRUCTURE OK — ACTUATION MARGIN LOW
```
