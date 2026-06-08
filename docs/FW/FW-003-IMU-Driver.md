# Mini-Atlas V6 Alpha

# FW-003 IMU Driver

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-003

Subsystem:

Firmware – IMU Driver

Target Platform:

ESP32 DevKitC

Primary Sensor:

ICM42688-P

Related Documents:

* FW-001 Firmware Architecture
* FW-002 Servo Bus Driver
* EDS-05 Communication & Control Architecture
* PR-001 Alpha Prototype Release

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 的 IMU 驱动架构。

负责：

* IMU初始化
* 数据采集
* 数据滤波
* 姿态解算
* 故障检测
* Motion Layer接口

为：

* 平衡控制
* 站立检测
* 跌倒检测
* 步态控制

提供基础传感器数据。

---

# 2. Hardware Configuration

IMU

ICM42688-P

---

Interface

I2C

---

Address

0x68

---

Mount Location

Pelvis Upper Deck

---

Mount Orientation

Robot Coordinate System

---

Status

FROZEN

---

# 3. Coordinate System

采用机器人坐标系：

```text
           +Z
            ↑
            |
            |
+Y <--------+--------> -Y

            |
            |
            ↓

           -Z

Forward = +X
Left    = +Y
Up      = +Z
```

---

Roll

绕 X 轴

---

Pitch

绕 Y 轴

---

Yaw

绕 Z 轴

---

Status

FROZEN

---

# 4. Driver Architecture

Application Layer

↓

Motion Layer

↓

Attitude Estimator

↓

IMU Driver

↓

I2C HAL

↓

ICM42688

---

职责划分：

IMU Driver

↓

原始数据采集

---

Attitude Estimator

↓

姿态解算

---

Motion Layer

↓

控制逻辑

---

# 5. Initialization Sequence

Power On

↓

I2C Init

↓

WHO_AM_I Read

↓

Verify Device

↓

Configure Registers

↓

Start Sampling

↓

Ready

---

失败：

↓

FAULT

---

# 6. Sensor Configuration

Gyroscope

200 Hz

---

Accelerometer

200 Hz

---

Gyro Range

±500 dps

---

Accel Range

±4g

---

Digital Low Pass Filter

Enabled

---

Status

FROZEN

---

# 7. Sampling Architecture

IMU Task

200 Hz

5 ms

---

Data Buffer

Ring Buffer

---

Buffer Size

64 Samples

---

Timestamp

Microsecond Resolution

---

Status

FROZEN

---

# 8. Raw Data Structure

```cpp
struct ImuRawData
{
    int16_t accel_x;
    int16_t accel_y;
    int16_t accel_z;

    int16_t gyro_x;
    int16_t gyro_y;
    int16_t gyro_z;

    uint64_t timestamp_us;
};
```

---

# 9. Attitude Estimation

V6 Alpha

采用：

Complementary Filter

---

原因：

简单

稳定

计算量低

---

Future

EKF

Optional

---

Status

FROZEN

---

# 10. Attitude Data Structure

```cpp
struct Attitude
{
    float roll_deg;
    float pitch_deg;
    float yaw_deg;

    float roll_rate_dps;
    float pitch_rate_dps;
    float yaw_rate_dps;
};
```

---

# 11. Filter Parameters

Update Rate

200 Hz

---

Alpha

0.98

---

Gyro Weight

98%

---

Accel Weight

2%

---

Status

FROZEN

---

# 12. Calibration Procedure

Startup Calibration

Required

---

Duration

3 Seconds

---

Robot State

Motionless

---

Outputs

Gyro Bias

Accel Bias

---

Store

RAM Only

---

# 13. Motion Layer Interface

API

```cpp
Attitude imu_get_attitude();

ImuRawData imu_get_raw();

bool imu_is_ready();
```

---

Update Rate

200 Hz

---

Thread Safe

Required

---

# 14. Fall Detection

Pitch

> 45°

---

Roll

> 45°

---

持续

500 ms

---

Action

Enter FALLEN State

---

Status

FROZEN

---

# 15. Sensor Health Monitoring

Check

WHO_AM_I

---

Data Timeout

50 ms

---

Stuck Data

Detect

---

I2C Error Counter

Monitor

---

Status

FROZEN

---

# 16. Safety Integration

IMU Failure

↓

Safety Manager

↓

FAULT

---

Wheel Stop

↓

Immediate

---

Servo Motion

↓

Disabled

---

Status

FROZEN

---

# 17. Logging

Startup Calibration

INFO

---

IMU Failure

ERROR

---

Bias Values

DEBUG

---

Output

UART

---

Future

WiFi Streaming

---

# 18. Bring-Up Procedure

Step 1

Verify I2C

---

Step 2

Read WHO_AM_I

---

Step 3

Verify Raw Data

---

Step 4

Verify Calibration

---

Step 5

Verify Roll/Pitch

---

Step 6

Verify Fall Detection

---

Status

MANDATORY

---

# 19. Verification Checklist

□ ICM42688 Detected

□ Calibration Successful

□ Raw Data Valid

□ Roll Accurate

□ Pitch Accurate

□ Yaw Stable

□ Fall Detection Working

□ Safety Integration Working

---

Pass Required

---

# 20. Freeze Summary

IMU

ICM42688-P

---

Interface

I2C

---

Rate

200 Hz

---

Filter

Complementary

---

Calibration

Startup

---

Fall Detection

Enabled

---

Safety Integration

Enabled

---

Status

APPROVED

READY FOR

FW-004-Wheel-Control.md
