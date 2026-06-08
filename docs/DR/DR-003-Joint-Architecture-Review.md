# Mini-Atlas V6 Alpha

# DR-003 Joint Architecture Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-003

Subsystem:

Joint / Mechanical Architecture

Parent Documents:

* DR-001 System Architecture Review
* DR-002 Actuator Selection Review
* MDS-02 Joint Requirements
* CDS-03~05 CAD Design

Related Documents:

* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design
* CDS-05 Knee Joint CAD Design
* MP-001 Manufacturing Package

---

# 1. Purpose

评审 Mini-Atlas V6 Alpha 各关节机械架构，决定：

* 舵机与轴承组合方式
* 输出轴结构
* 扭矩传递方式
* 可维护性与可打印性
* 机械限位与安装接口

---

# 2. Candidate Architectures

| Option | Description                         | Pros          | Cons       |
| ------ | ----------------------------------- | ------------- | ---------- |
| A      | Servo directly drives link          | 简单            | 舵机承受弯矩，寿命低 |
| B      | Servo + Single Bearing              | 减少弯矩          | 仍有轴向偏心     |
| C      | Servo + Dual Bearing + Output Shaft | 舵机不承受弯矩，结构刚性高 | 复杂，重量略高    |

---

# 3. Evaluation Criteria

* 扭矩传递效率
* 机械刚性
* 寿命与维护
* 可打印性
* 舵机重量承受
* 安装便利性
* 扭矩裕量

---

# 4. Analysis

## Option A

* Servo直接承载
* 扭矩峰值时舵机承受全部弯矩
* 风险: 过载、齿轮损坏
* 结论: 不适合Alpha

## Option B

* 单轴承支撑
* 部分弯矩传递给轴承
* 风险: 长期磨损，偏心载荷
* 结论: 较安全，但不最佳

## Option C

* 双轴承支撑，独立输出轴
* Torque Transfer Module保证舵机仅承受扭矩
* 可维护、可打印
* 结论: 最优方案 → APPROVED

---

# 5. Freeze Parameters

* Dual Bearing Support
* Independent Output Shaft
* Torque Transfer Module
* 机械限位安装接口
* 舵机安装孔位

---

# 6. Mechanical Verification Plan

* CAD验证输出轴与舵机对齐
* 扭矩传递仿真
* 打印件可打印性验证
* 安装/拆卸测试

---

# 7. Risk Analysis

| Risk                       | Mitigation                           |
| -------------------------- | ------------------------------------ |
| Torque Peak > Servo Rating | Torque Module + Safety Manager       |
| Bearing Wear               | Use 6802/6803 Bearings + Lubrication |
| Shaft Misalignment         | CAD Simulation & Tolerances          |
| Print Layer Delamination   | Orientation & Infill Optimization    |

---

# 8. Decision

Selected Architecture: Option C

Rationale:

* 扭矩安全裕量高
* 可维护
* 可打印
* 支持后续Beta升级
* 已通过初步 CAD 验证

---

# 9. Freeze Summary

* All Joints: Dual Bearing + Output Shaft
* Torque Module installed
* Servo mounting interface frozen
* Mechanical limits defined
* Status: APPROVED

Next Document:

DR-004-Hip-Architecture-Review.md
