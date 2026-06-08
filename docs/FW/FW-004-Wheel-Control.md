# Mini-Atlas V6 Alpha

# FW-004 Wheel Control

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-004

Subsystem:

Firmware – Wheel Control

Target Platform:

ESP32 DevKitC

Related Documents:

* FW-001 Firmware Architecture
* FW-003 IMU Driver
* EDS-05 Communication & Control Architecture
* CDS-06 Wheel Module Architecture
* PR-001 Alpha Prototype Release

---

# 1. Purpose

定义 V6 Alpha 轮组控制架构。

负责：

* 电机驱动
* PWM输出
* 速度控制
* 差速控制
* Wheel Mode
* Wheel Assisted Gait

---

# 2. Hardware Configuration

Motor

GB37-520

x2

---

Drive

Left Wheel

Right Wheel

---

Control

Differential Drive

---

Supply

7.4V Rail

---

Status

FROZEN

---

# 3. Control Architecture

Application

↓

Motion Layer

↓

Wheel Controller

↓

Motor Driver

↓

GB37-520

---

控制目标：

Velocity Control

---

Position Control

Not Required

---

# 4. Operating Modes

STOP

↓

MANUAL

↓

WHEEL_MODE

↓

GAIT_ASSIST

↓

FAULT

---

Status

FROZEN

---

# 5. Task Architecture

| Task         | Priority | Period |
| ------------ | -------: | -----: |
| Wheel PID    |        8 |   5 ms |
| Motor Update |        8 |   5 ms |
| Wheel Health |        6 |  20 ms |

---

Control Frequency

200 Hz

---

Status

FROZEN

---

# 6. PWM Configuration

PWM Frequency

20 kHz

---

Resolution

12 Bit

---

Output Range

-100%

↓

+100%

---

Deadband

2%

---

Status

FROZEN

---

# 7. Velocity Control

Input

Target Velocity

(mm/s)

---

Output

PWM Duty

(%)

---

Controller

PID

---

Status

FROZEN

---

# 8. PID Structure

```cpp
struct WheelPid
{
    float kp;
    float ki;
    float kd;

    float integral;
    float previous_error;
};
```

---

Initial Values

Kp = 0.8

Ki = 0.2

Kd = 0.0

---

To Be Tuned

Prototype Phase

---

# 9. Wheel State

```cpp
struct WheelState
{
    float velocity_left;
    float velocity_right;

    float target_left;
    float target_right;

    bool enabled;
};
```

---

# 10. Differential Drive Model

Forward

```text
L = +V
R = +V
```

---

Backward

```text
L = -V
R = -V
```

---

Rotate Left

```text
L = -V
R = +V
```

---

Rotate Right

```text
L = +V
R = -V
```

---

Status

FROZEN

---

# 11. Wheel Assisted Gait

Purpose

辅助步态稳定

---

Functions

Ground Contact Assist

---

Micro Position Correction

---

Low Speed Stabilization

---

Status

Phase 2

---

# 12. Motion Layer Interface

API

```cpp
void wheel_enable();

void wheel_disable();

void wheel_set_velocity(
    float left_mmps,
    float right_mmps);

WheelState wheel_get_state();
```

---

Thread Safe

Required

---

# 13. Safety Integration

Safety Manager

↓

Wheel Disable

↓

PWM = 0

---

Emergency Stop

↓

Immediate Stop

---

Battery Critical

↓

Stop Wheels

---

IMU Failure

↓

Stop Wheels

---

Status

FROZEN

---

# 14. Current Monitoring

Monitor

Motor Current

---

Sample Rate

50 Hz

---

Threshold

2A Continuous

---

Peak

5A

---

Action

Warning

↓

Fault

---

# 15. Thermal Protection

Motor Temp

Optional

---

Driver Temp

Required

---

Threshold

80°C

---

Action

Reduce Output

---

Fault

---

# 16. Bring-Up Procedure

Step 1

Verify PWM

---

Step 2

Verify Direction

---

Step 3

Verify Left Wheel

---

Step 4

Verify Right Wheel

---

Step 5

Verify Differential Drive

---

Step 6

Verify Stop

---

Status

MANDATORY

---

# 17. Verification Checklist

□ PWM Output OK

□ Left Wheel OK

□ Right Wheel OK

□ Direction Correct

□ Velocity Control Working

□ PID Stable

□ Safety Stop Working

□ E-Stop Working

---

Pass Required

---

# 18. Performance Targets

Max Speed

0.8 m/s

---

Cruise Speed

0.3 m/s

---

Control Loop

200 Hz

---

PWM

20 kHz

---

Status

FROZEN

---

# 19. Known Limitations

No Encoder Closed Loop

Alpha Release

---

Open Loop Velocity

Allowed

---

Encoder Upgrade

Future Revision

---

# 20. Freeze Summary

Motor

GB37-520

---

Control

Velocity

---

PID

Enabled

---

Loop Rate

200 Hz

---

PWM

20 kHz

---

Differential Drive

Enabled

---

Safety Integration

Enabled

---

Status

APPROVED

READY FOR

FW-005-Gait-Engine.md
