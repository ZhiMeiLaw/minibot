# Mini-Atlas V6 Alpha

# FW-007 OTA Framework

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-007

Subsystem:

Firmware – OTA (Over-The-Air) Update Framework

Target Platform:

ESP32 DevKitC

Related Documents:

* FW-001 Firmware Architecture
* FW-006 Safety Manager
* PR-001 Alpha Prototype Release
* MP-001 Manufacturing Package Release

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 的 OTA 升级架构。

目标：

* 支持 WiFi OTA 升级固件
* 支持 A/B 分区安全回滚
* 与 Safety Manager 集成
* 防止升级过程意外损坏主控制器
* 支持 Alpha 样机固件版本管理

---

# 2. Architecture Overview

ESP32 Partition Layout:

* OTA_A (Active)
* OTA_B (Backup)
* OTA_Config (Metadata)
* OTA_Data (Optional)

---

Update Process:

1. Download firmware over WiFi
2. Verify CRC / SHA256
3. Write to inactive partition (A or B)
4. Update OTA_Config
5. Reboot into new firmware
6. Verify boot success → mark partition active
7. Failure → rollback to previous partition

---

# 3. Task Architecture

| Task                   | Priority |       Period |
| ---------------------- | -------: | -----------: |
| OTA Download           |        6 | Event Driven |
| CRC / SHA Verification |        7 | Event Driven |
| Partition Switch       |       10 | Event Driven |
| Post-Update Check      |        9 | Event Driven |

---

# 4. Firmware Integrity

* Verification: CRC32 + SHA256
* Backup: Previous firmware kept in alternate partition
* Rollback: Automatic on boot failure
* Logging: Update status logged in OTA_Config

---

# 5. Communication

* WiFi Client
* HTTPS download preferred
* Retry: 3 attempts on failure
* Timeout: 30 s per chunk
* OTA Status Reporting: UART / Optional WiFi

---

# 6. Safety Integration

* Safety Manager must verify system before applying firmware
* E-Stop or motion lock active during OTA
* Any sensor fault → OTA paused / aborted

---

# 7. Bring-Up Procedure

1. Connect Alpha to WiFi
2. Flash initial firmware if required
3. Initiate OTA update from PC / Cloud server
4. Verify checksum
5. Reboot and verify firmware boot success
6. Confirm Motion Layer operational
7. Log OTA completion

Pass Criteria:

* Firmware version incremented
* System boots normally
* Motion Layer functional
* Safety Manager active

---

# 8. Freeze Summary

* OTA Enabled: Yes
* Partition Layout: A/B
* Update Verification: CRC + SHA256
* Rollback: Automatic
* Safety Integration: Yes
* Status: APPROVED
* READY FOR: FW-008 Bring-Up Software
