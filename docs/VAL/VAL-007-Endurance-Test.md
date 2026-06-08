# Mini-Atlas V6 Alpha

# VAL-007 Endurance Test

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER TEST

Document Number:

VAL-007

Release Name:

Mini-Atlas V6 Alpha Endurance Test

Parent Documents:

* VAL-001 ~ VAL-006
* FW-001 ~ FW-008
* PR-002 Alpha Prototype Functional Validation

Related Documents:

* VAL-008 Battery Life Test
* PR-003 Beta Prototype Iteration

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 样机长时间运行能力，确保机械、电气及软件系统在连续工作情况下可靠。

目标：

* 验证步态连续运行稳定性
* 验证舵机热稳定性
* 验证电源系统温升与电流负载
* 验证轮子及差速控制可靠性
* 验证 Safety Manager 对长时间运行故障处理能力

---

# 2. Test Configuration

* Surface: Non-slip, flat floor
* Power: Full 3S2P Samsung 30Q
* Firmware: FW-008 Bring-Up Software
* Servo: STS3046 ×6
* Wheels: GB37-520 ×2
* IMU: ICM42688-P
* Logging: UART / WiFi telemetry
* Safety Rope: Optional for initial cycles

---

# 3. Test Scenarios

| Scenario               |     Duration | Mode                      | Objective                      |
| ---------------------- | -----------: | ------------------------- | ------------------------------ |
| Continuous Walking     |      2 hours | Forward                   | Evaluate servo & wheel heating |
| Step Cycle Repetition  | 10,000 steps | Forward / Backward / Turn | Mechanical wear                |
| Stand Pose Hold        |       30 min | Stand                     | Servo torque & COM stability   |
| Wheel Assisted Walking |       1 hour | Forward + Turn            | Wheel PID stability            |
| Random Fault Injection |     Multiple | All                       | Safety Manager response        |

---

# 4. Measurement Parameters

* Joint Currents
* Servo Temperatures
* Wheel Currents & Voltages
* COM deviation
* Gait trajectory error
* Power Rail Voltages
* Battery voltage & current
* Any FAULT state trigger
* Number of motion cycles completed

---

# 5. Acceptance Criteria

* No servo overheating > 70°C
* Joint currents < 80% rated torque
* COM deviation < ±5 mm
* No falls / mechanical damage
* Wheel velocities stable
* Safety Manager correctly handles faults
* Firmware logging without loss
* No resets or brownouts

---

# 6. Procedure

1. Fully charge battery
2. Assemble robot per MP-001
3. Verify all subsystems functional (VAL-001 ~ VAL-006)
4. Enable Bring-Up software (FW-008)
5. Command continuous walking forward for 2 hours
6. Record all parameters every 1 minute
7. Pause at predefined intervals to check temperatures and battery
8. Command backward and turn cycles
9. Inject random faults (IMU, servo disconnect, wheel loss)
10. Verify Safety Manager reaction and recovery
11. Continue until total cycles reach 10,000 steps

---

# 7. Data Logging

* Servo position & current
* Wheel velocity & current
* Battery voltage & current
* COM trajectory
* IMU Roll/Pitch/Yaw
* FAULT events
* Temperature logs

---

# 8. Reporting

Compile into:

```text id="f1zvnp"
VAL-007-Endurance-Test-Log.xlsx
```

Include:

* All parameters vs. time
* Peak & average currents
* Temperature profiles
* Servo & wheel deviations
* Any safety events

---

# 9. Freeze Summary

* Continuous Walking: VALIDATED
* Step Cycle Repetition: VALIDATED
* Stand Pose Hold: VALIDATED
* Wheel Assisted Gait: VALIDATED
* Safety Manager Response: VALIDATED
* Power System & Thermal Stability: VALIDATED
* Status: READY FOR VAL-008 Battery Life Test
