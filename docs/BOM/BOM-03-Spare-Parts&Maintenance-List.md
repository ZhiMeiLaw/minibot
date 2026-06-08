# Mini-Atlas V6 Alpha

# BOM-03 Spare Parts & Maintenance List

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结：

- Spare Parts（备件）
- Consumables（耗材）
- Wear Parts（易损件）
- Maintenance Schedule（维护周期）
- Replacement Procedure（更换建议）
- Service Stock（建议库存）

目标：

```text
保证样机长期运行

降低停机时间

降低维护成本

提高现场维修能力
```

---

# 2. Spare Parts Classification

全机备件分为：

## Class A

关键备件

```text
缺失即停机
```

例如：

```text
Servo
Battery
Motor Driver
```

---

## Class B

重要备件

```text
可短时间运行

但应尽快更换
```

例如：

```text
Bearing
Wheel
XT30
```

---

## Class C

普通耗材

```text
现场常备即可
```

例如：

```text
Screw
Tie Wrap
Heat Shrink
```

---

# 3. Servo Maintenance Plan

---

# STS3046

## Quantity Installed

```text
6
```

---

## Recommended Spare

```text
2
```

---

## Failure Modes

### Gear Wear

齿轮磨损

症状：

```text
关节间隙增大

抖动

异响
```

---

### Output Shaft Looseness

输出轴松动

症状：

```text
姿态不稳定
```

---

### Driver Board Failure

驱动板故障

症状：

```text
失联

无法响应
```

---

## Inspection Interval

```text
50小时
```

---

## Replacement Interval

```text
300~500小时
```

---

# STS3215

## Quantity Installed

```text
2
```

---

## Recommended Spare

```text
1
```

---

## Inspection

```text
每50小时
```

---

## Replacement

```text
300小时以上视状态
```

---

# 4. Bearing Maintenance Plan

---

# 6803-2RS

Installed

```text
12
```

---

Recommended Spare

```text
4
```

---

Inspection

```text
100小时
```

---

Check

```text
转动阻力

异响

间隙
```

---

Replacement

```text
500小时
```

---

# 6802-2RS

Installed

```text
8
```

---

Recommended Spare

```text
4
```

---

Replacement

```text
500小时
```

---

# 5. Wheel Motor Maintenance

---

# GB37-520 Encoder

Installed

```text
2
```

---

Recommended Spare

```text
1
```

---

Inspection

```text
100小时
```

---

Check

```text
减速箱噪声

编码器信号

轴承状态
```

---

Expected Life

```text
500~1000小时
```

---

Replacement Trigger

```text
RPM异常

电流异常

减速箱异响
```

---

# 6. Wheel Maintenance

---

Installed

```text
2
```

---

Recommended Spare

```text
2
```

---

Check

```text
磨损

开裂

脱胶
```

---

Replacement

```text
视磨损程度
```

---

Expected Life

```text
200~500小时
```

---

# 7. Battery Maintenance

---

# Samsung 30Q

Installed

```text
6 Cells
```

---

Configuration

```text
3S2P
```

---

Inspection

```text
每20次充电
```

---

Check

```text
内阻

容量

鼓包
```

---

Replacement

```text
300循环
```

---

Expected Life

```text
2~3年
```

---

Storage Voltage

```text
3.7~3.8V/Cell
```

---

Storage Temperature

```text
10~25℃
```

---

# 8. Power Electronics

---

# DRV8871

Installed

```text
2
```

---

Recommended Spare

```text
2
```

---

Failure Modes

```text
过流损坏

短路损坏
```

---

Replacement

```text
按故障更换
```

---

# Buck Converter

Installed

```text
2
```

---

Recommended Spare

```text
1
```

---

Inspection

```text
输出电压

温升
```

---

# 9. Fuse Maintenance

---

Installed

```text
25A ATO
```

---

Recommended Spare

```text
10
```

---

Replacement Trigger

```text
熔断
```

---

Inspection

```text
每次维修
```

---

# 10. Connector Maintenance

---

# XT30

Installed

```text
4 Sets
```

---

Recommended Spare

```text
4 Sets
```

---

Check

```text
接触电阻

发热

松动
```

---

Replacement

```text
500次插拔
```

---

# JST-XH

Recommended Spare

```text
20 Sets
```

---

# 11. Wiring Maintenance

---

Inspection

```text
50小时
```

---

Check

```text
磨损

压伤

绝缘层破损
```

---

重点检查

```text
Hip Roll

Hip Pitch

Knee
```

---

因为这些位置存在：

```text
反复弯折
```

---

# 12. Fastener Maintenance

---

# M3 Screw

Inspection

```text
50小时
```

---

Check

```text
松动
```

---

Action

```text
重新上螺纹胶
```

---

推荐：

```text
Loctite 243
```

---

# Brass Insert

Check

```text
是否脱出
```

---

Action

```text
热熔重新安装
```

---

# 13. Maintenance Schedule

## Before Every Run

检查：

```text
电池电压

舵机通信

急停按钮

轮子固定
```

预计：

```text
2分钟
```

---

## Every 10 Hours

检查：

```text
螺丝松动

线束状态

轮胎磨损
```

预计：

```text
10分钟
```

---

## Every 50 Hours

检查：

```text
舵机间隙

轴承状态

连接器状态
```

预计：

```text
30分钟
```

---

## Every 100 Hours

检查：

```text
电机减速箱

编码器

电池容量
```

预计：

```text
1小时
```

---

## Every 500 Hours

大保养：

```text
更换全部轴承

检查全部舵机

更换磨损轮胎
```

预计：

```text
半天
```

---

# 14. Spare Parts Inventory

## Alpha Prototype

建议库存：

### Servo

```text
STS3046 ×2

STS3215 ×1
```

---

### Motor

```text
GB37-520 ×1
```

---

### Bearing

```text
6803 ×4

6802 ×4
```

---

### Electronics

```text
DRV8871 ×2

Buck ×1

ESP32 ×1

IMU ×1
```

---

### Power

```text
XT30 ×4

ATO 25A Fuse ×10
```

---

### Mechanical

```text
M3 Screw Kit ×1

M3 Brass Insert ×50

E-Clip ×20
```

---

# 15. Estimated Spare Parts Budget

| Item | Cost |
|--------|--------:|
| STS3046 ×2 | 300 RMB |
| STS3215 ×1 | 70 RMB |
| GB37-520 ×1 | 40 RMB |
| Bearings | 40 RMB |
| DRV8871 | 30 RMB |
| Buck | 40 RMB |
| XT30 | 20 RMB |
| Fuse | 10 RMB |
| Fastener Kit | 30 RMB |

---

Total

```text
≈ 580 RMB
```

---

# 16. Field Repair Capability

具备以下能力：

```text
现场更换舵机

现场更换轮电机

现场更换轴承

现场更换保险丝

现场更换电池
```

---

无需返厂。

---

# 17. Reliability Target

V6 Alpha目标：

```text
MTBF > 100小时
```

(MTBF = Mean Time Between Failures，平均无故障时间)

---

V6 Beta目标：

```text
MTBF > 500小时
```

---

# 18. Freeze Summary

## Critical Spare Parts

```text
STS3046

STS3215

GB37-520

6803

6802

DRV8871

XT30

Fuse
```

---

## Annual Maintenance Budget

预计：

```text
200~500 RMB
```

---

## Spare Parts Inventory Cost

预计：

```text
≈580 RMB
```

---

Status

```text
APPROVED

READY FOR PROTOTYPE BUILD

READY FOR FIELD TEST
```
