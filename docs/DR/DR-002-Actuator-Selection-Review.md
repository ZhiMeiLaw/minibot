# Mini-Atlas V6 Alpha

# DR-002 Actuator Selection Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-002

Subsystem:

Actuator / Joint Drive

Parent Documents:

* DR-001 System Architecture Review
* EDS-01 Electrical Design Specification
* MDS-02 Joint Requirements
* SR-001 System Weight Budget

Related Documents:

* CDS-03 Hip Roll CAD Design
* CDS-04 Hip Pitch CAD Design
* CDS-05 Knee CAD Design

---

# 1. Purpose

本评审用于选择 Mini-Atlas V6 Alpha 的执行器（舵机/驱动器）。

目标：

* 满足每个关节扭矩与速度要求
* 符合重量预算
* 符合成本要求
* 支持总线控制（UART）
* 易于采购与替换

---

# 2. Candidate Actuators

| Actuator        | Max Torque | Voltage |  Speed | Weight | Cost | Bus Type | Notes                     |
| --------------- | ---------: | ------: | -----: | -----: | ---: | -------- | ------------------------- |
| STS3046         |     4.5 Nm |   7.4 V | 46 RPM |   80 g |  $25 | UART     | Low cost, domestic supply |
| STS3215         |     6.0 Nm |   7.4 V | 60 RPM |  120 g |  $45 | UART     | Higher torque, heavier    |
| STS3250         |     8.0 Nm |   7.4 V | 50 RPM |  130 g |  $55 | UART     | Overkill for Alpha        |
| Dynamixel XL430 |     4.3 Nm |     12V | 60 RPM |   90 g | $100 | TTL/UART | Expensive, high latency   |

---

# 3. Joint Requirements

| Joint     | Required Torque | Required Speed | Safety Margin |
| --------- | --------------: | -------------: | ------------: |
| Hip Roll  |          3.0 Nm |         45 RPM |           50% |
| Hip Pitch |          4.0 Nm |         45 RPM |           50% |
| Knee      |          4.0 Nm |         45 RPM |           50% |

---

# 4. Actuator Evaluation

## 4.1 STS3046

* Torque: 4.5 Nm → meets all joints
* Weight: 80 g → acceptable
* Cost: $25 → low
* Bus: UART → compatible
* Safety Margin: 12.5~50% depending on joint

## 4.2 STS3215

* Torque: higher than needed
* Weight: heavier
* Cost: higher
* Conclusion: Overkill for Alpha

## 4.3 STS3250

* Torque excessive
* Weight & Cost high
* Conclusion: Not cost-effective

## 4.4 Dynamixel XL430

* Torque sufficient
* Cost high
* Voltage 12V → needs separate Buck
* Conclusion: Not selected for Alpha

---

# 5. Decision Matrix

| Joint     | Selected Actuator | Reason                             |
| --------- | ----------------- | ---------------------------------- |
| Hip Roll  | STS3046           | Meets torque, low weight, low cost |
| Hip Pitch | STS3046           | Meets torque, low weight, low cost |
| Knee      | STS3046           | Meets torque, low weight, low cost |

---

# 6. Safety Margin Analysis

Formula

```text id="v78ym2"
Safety Margin = (Actuator Torque - Required Torque) / Required Torque × 100%
```

* Hip Roll: (4.5 - 3.0)/3.0 × 100% = 50%
* Hip Pitch: (4.5 - 4.0)/4.0 × 100% = 12.5%
* Knee: (4.5 - 4.0)/4.0 × 100% = 12.5%

Comment: Hip Roll margin largest → conservative
Hip Pitch & Knee marginal → acceptable for Alpha, can increase in Beta

---

# 7. Power Considerations

* Max Current per servo ~1.2A @ peak load
* Battery 3S2P Samsung 30Q sufficient
* PDB & Buck rails verified in EDS-04
* UART bus supports 6 servos with sync write

---

# 8. Supply & Procurement

* Domestic supplier for STS3046
* Lead time: 1–2 weeks
* Spare units recommended: 2 per joint type

---

# 9. Freeze Summary

* All joints: STS3046 selected
* Weight budget satisfied
* Cost budget satisfied
* Electrical compatibility validated
* Status: APPROVED for Alpha CAD & BOM

---

Next Document:

DR-003-Joint-Architecture-Review.md
