# Mini-Atlas V6 Alpha

# FW-002 Servo Bus Driver

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-002

Subsystem:

Firmware – Servo Bus Driver

Target Platform:

ESP32 DevKitC

Related Documents:

* FW-001 Firmware Architecture
* EDS-05 Communication & Control Architecture
* PR-001 Alpha Prototype Release
* MP-001 Manufacturing Package Release

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 上 STS3046 舵机总线的固件驱动架构与实现要求。

目标：

* 支持所有舵机控制（Hip Roll / Hip Pitch / Knee）
* 支持同步写操作
* 支持单舵机读写
* 保证实时性和可靠性
* 与 Motion Layer / Safety Manager 完全集成

---

# 2. Hardware Overview

* Platform: ESP32 DevKitC
* Total Servos: 6 (3 per leg)
* Bus Type: UART (Half-Duplex)
* Bus Pull-Up: 4.7kΩ
* Wiring: Daisy Chain
* Termination: 120Ω optional

---

# 3. Driver Architecture

## Layers

* HAL UART Layer
* Servo Protocol Layer
* Bus Management Layer
* Motion Layer Interface

---

## HAL UART Layer

* Non-blocking TX/RX
* DMA supported
* 1 kHz system tick

---

## Servo Protocol Layer

* STS3046 Protocol: Position Control
* Commands: Ping / Read / Write / Sync Write
* ID Management: 1~254
* Error Detection: CRC + Timeout

---

## Bus Management Layer

* Maintain active servo list
* Retry failed transmissions
* Detect missing servos
* Queue management for Sync Write

---

# 4. Task Architecture

| Task                  | Priority | Period |
| --------------------- | -------: | -----: |
| Servo Update          |        9 |  10 ms |
| Servo Readback        |        8 |  10 ms |
| Timeout / Error Check |        7 |  20 ms |
| Bus Management        |        6 |  10 ms |

---

# 5. Communication Timing

* UART Baud: 1 Mbps (Max STS3046 supported)
* Sync Write Time: ≤5 ms per 3 servos
* Single Write Time: ≤3 ms
* Readback Time: ≤3 ms per servo
* Max Total Cycle: 10 ms (Motion Loop 100 Hz)

---

# 6. Servo ID Management

* Predefined IDs:

| Joint           | ID |
| --------------- | -- |
| Left Hip Roll   | 1  |
| Left Hip Pitch  | 2  |
| Left Knee       | 3  |
| Right Hip Roll  | 4  |
| Right Hip Pitch | 5  |
| Right Knee      | 6  |

* ID Scan Procedure:

1. Ping each expected ID
2. Detect missing / duplicate
3. Report to Safety Manager

---

# 7. Error Handling

* Timeout: 50 ms
* Retry: 2 attempts
* Servo Not Responding → Safety Fault
* Invalid CRC → Retry

---

# 8. Motion Layer Interface

* Functions:

```cpp
// Update all servos position (Sync Write)
servo_bus.set_positions(joint_targets[]);

// Read single servo position
servo_bus.read_position(servo_id);

// Ping servo
servo_bus.ping(servo_id);
```

* Input: Joint Targets from Motion Layer
* Output: Readback for Feedback / Safety

---

# 9. Safety Integration

* Emergency Stop disables torque immediately
* Servo Bus errors → propagate FAULT to Safety Manager
* Watchdog monitors bus timeout
* Bus recovery: Reset UART, re-scan IDs

---

# 10. Testing & Verification

1. Power On
2. Connect all 6 servos in Daisy Chain
3. Flash Servo Bus Driver firmware
4. Run Servo Scan → confirm all IDs
5. Send Sync Write → verify movement
6. Readback all positions → verify accuracy
7. Introduce intentional fault → verify FAULT propagation
8. Repeat for multiple cycles (≥1000 cycles)

Pass Criteria:

* All servos reachable
* All movement commands executed accurately
* All safety mechanisms functional

---

# 11. Freeze Summary

* Bus Type: UART
* Servos: STS3046 ×6
* Servo IDs: Fixed 1~6
* Update Rate: 100 Hz
* Sync Write: Enabled
* Error Handling: Timeout + Retry + Safety Fault
* Safety Integration: Enabled
* Status: APPROVED
* READY FOR: FW-003 IMU Driver Integration
