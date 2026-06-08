# Mini-Atlas V6 Beta Prototype Iteration

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER ALPHA

Document Number:

PR-003

Release Name:

Mini-Atlas V6 Beta Prototype Iteration

Parent Documents:

* PR-002 Alpha Prototype Functional Validation
* MP-001 Manufacturing Package Release
* FW-001 ~ FW-008

---

# 1. Purpose

记录 Mini-Atlas V6 Beta 样机迭代计划，基于 Alpha 样机验证数据进行优化：

* 步态参数调整
* 舵机 PID 调整
* 机械装配微调
* 电气接口优化
* 软件优化（Gait / Wheel / Safety / Bring-Up）
* 减轻重量或降低摩擦

目标：

* 改善稳定性
* 改善功耗
* 改善步态平滑度
* 为 Beta 样机量产做准备

---

# 2. Alpha 验证问题汇总

| Subsystem      | Issue                      | Priority | Notes                   |
| -------------- | -------------------------- | -------- | ----------------------- |
| Mechanical     | Minor binding at Hip Pitch | Medium   | Adjust tolerances       |
| Servo Bus      | Torque fluctuation         | Medium   | Tune PID                |
| IMU            | Bias drift                 | Low      | Software calibration    |
| Wheel Control  | Low-speed jitter           | Medium   | Tune PID, increase loop |
| Gait Engine    | Slight COM oscillation     | High     | Adjust step timing      |
| Safety Manager | None                       | Low      | Verified                |

---

# 3. Iteration Plan

## Mechanical

* Adjust Hip Pitch clearance ±0.1 mm
* Verify Knee bearing seat
* Recut carbon tubes if necessary
* Ensure Heat-Set Inserts flush

## Servo / Motion

* Tune Hip / Knee PID gains
* Verify Sync Write accuracy
* Re-test torque limits

## Wheel

* Adjust velocity PID
* Confirm 200 Hz control loop
* Verify Wheel Assisted Gait stabilization

## IMU

* Apply software bias calibration
* Confirm 200 Hz sampling
* Validate roll/pitch/yaw accuracy

## Safety

* Re-test E-Stop
* Confirm fault propagation
* Verify overcurrent detection

---

# 4. Beta Prototype Goals

* Stable stand-up and balance
* Smooth forward / backward / turn gait
* Wheel Assisted COM stabilization functional
* Safety interlocks operational
* Firmware logging stable
* Battery consumption measured

---

# 5. Validation Procedure

1. Assemble Beta prototype per MP-001
2. Apply Alpha fixes / tuning
3. Run full Bring-Up sequence (FW-008)
4. Execute Step Forward / Backward / Turn
5. Record currents, voltages, IMU data
6. Adjust PID / trajectory parameters iteratively
7. Document improvements / issues
8. Freeze Beta prototype configuration

---

# 6. Freeze Summary

* Mechanical Adjustments: Applied
* Servo PID: Tuned
* Wheel PID: Tuned
* IMU Calibration: Updated
* Safety Overrides: Verified
* Motion / Gait: Verified
* Status: APPROVED FOR BETA
* Ready For: PR-004 Production Preparation / FW Finalization

---

# 7. Known Risks

* Minor residual COM oscillation
* Long-term IMU drift
* Servo wear over repeated cycles
* Wheel encoder optional (future upgrade)

---

# 8. Deliverables

* Updated CAD (if mechanical changes)
* Updated Firmware Parameters (PID / Trajectory)
* Validation Logs
* Updated BOM (if hardware changes)
* Updated Bring-Up Procedure

---

# 9. Next Steps

* PR-004 Production Preparation
* Finalize Beta hardware and firmware freeze
* Start small-batch manufacturing for field testing
