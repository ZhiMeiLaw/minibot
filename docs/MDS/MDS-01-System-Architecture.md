# Mini-Atlas V6 Alpha

# MDS-01 System Architecture Specification

## 系统架构设计规范

---

| Item        | Value                             |
| ----------- | --------------------------------- |
| Project     | Mini-Atlas V6 Alpha               |
| Document    | MDS-01                            |
| Title       | System Architecture Specification |
| Version     | v0.1                              |
| Status      | Design Freeze Candidate           |
| Last Update | 2026-06                           |
| Author      | Mini-Atlas Project                |

---

# 1. Introduction（项目简介）

## 1.1 Purpose（文档目的）

本文档定义 Mini-Atlas V6 Alpha 的总体系统架构（System Architecture）。

后续所有设计均必须遵循本文件：

* Mechanical Design（机械设计）
* Electrical Design（电气设计）
* PCB Design（电路设计）
* Firmware Design（固件开发）
* Motion Control（运动控制）
* Manufacturing（生产制造）

---

## 1.2 Design Philosophy（设计理念）

Mini-Atlas V6 不是传统双足机器人（Biped Robot）。

采用：

```text
Wheel-Assisted Humanoid
轮足融合人形机器人
```

架构。

核心思想：

```text
Humanoid Posture
+
Wheel Mobility
+
Low Cost
+
DIY Friendly
```

即：

* 保持人形机器人姿态
* 保留抬腿能力
* 保留重心转移能力
* 通过轮子降低平衡难度
* 降低对高扭矩舵机的依赖

---

## 1.3 Design Objectives（设计目标）

### Objective 1：Stable Standing（稳定站立）

机器人能够独立站立。

---

### Objective 2：Weight Shift（重心转移）

机器人能够进行：

```text
Center Of Mass Shift
(COM Shift)
重心转移
```

实现单腿支撑。

---

### Objective 3：Leg Lifting（抬腿）

机器人能够：

```text
Left Leg Lift
Right Leg Lift
```

用于跨越障碍。

---

### Objective 4：Wheel Assisted Walking（轮足步态）

机器人通过：

* 腿部动作
* 轮子驱动

完成连续移动。

---

### Objective 5：Obstacle Crossing（越障）

机器人能够跨越：

* 电线
* 门槛
* 地毯边缘
* 小型障碍物

目标高度：

```text
20~40 mm
```

---

# 2. Non Goals（非目标）

V6 Alpha 暂不追求：

## Running（奔跑）

不支持动态跑步。

---

## Jumping（跳跃）

不支持双脚离地。

---

## Stair Climbing（爬楼梯）

暂不支持。

---

## Atlas Level Balance（高动态平衡）

暂不实现波士顿动力 Atlas 级动态控制。

---

# 3. Robot Classification（机器人分类）

## Type（类型）

```text
Wheel-Assisted Humanoid
轮足融合机器人
```

---

## Height（高度）

```text
550 mm
```

---

## Weight（重量）

目标：

```text
< 4 kg
```

推荐：

```text
3.0 kg ~ 3.8 kg
```

---

# 4. System Architecture（总体架构）

## Top Level Architecture

```text
                Robot

                   │

    ┌──────────────┼──────────────┐

 Mechanical      Electrical      Software

   机械            电气            软件
```

---

# 5. Mechanical Architecture（机械架构）

## Main Components（主要组成）

```text
Pelvis
骨盆

Left Leg
左腿

Right Leg
右腿

Wheel Module
轮组
```

---

## Mechanical Topology（机械拓扑）

```text
              Pelvis
              （骨盆）

                 │

           Hip Roll
         （髋关节侧摆）

                 │

           Hip Pitch
         （髋关节前后摆）

                 │

              Thigh
              （大腿）

                 │

              Knee
             （膝盖）

                 │

              Calf
             （小腿）

                 │

           Wheel
          （轮组）
```

> 注：踝关节已移除（DR-011），小腿直接连接刚性轮足安装座。

---

# 6. Degrees Of Freedom（自由度）

## Per Leg（单腿自由度）

| Joint       | 中文名称   |
| ----------- | ------ |
| Hip Roll    | 髋关节侧摆  |
| Hip Pitch   | 髋关节前后摆 |
| Knee Pitch  | 膝关节    |

---

总计：

```text
3 Servo DOF × 2 Legs
=
6 Servo DOF
```

> **ECO-001 变更**：踝关节已移除（DR-011 Rigid Wheel Mount）。原 Ankle Pitch DOF 取消。

---

## Full Robot（整机自由度）

> **ECO-002 变更**：删除错误的 "4 DOF × 2 Legs = 8 Servo DOF" 行（单腿为 3 DOF 非 4 DOF）。

轮组：

```text
2 Wheel Motors
```

---

总计：

```text
6 Servo DOF
+
2 Wheel DOF
=
8 DOF
```

---

> **ECO-002 变更**：修正为 6 Servo DOF + 2 Wheel DOF = 8 Total DOF（原 "8 Servo DOF" 为错误值）。

---

# 7. Actuator Architecture（执行器架构）

## Servo Allocation（舵机配置）

### Hip Roll

```text
STS3046
```

---

### Hip Pitch

```text
STS3046
```

---

### Knee

```text
STS3046
```

---

> **ECO-001 变更**：踝关节已移除（DR-011）。原 STS3215 × 2 方案取消。

## Servo Quantity（舵机数量）

| Model   | Quantity |
| ------- | -------: |
| STS3046 |        6 |

> **ECO-001 变更**：踝关节取消，仅保留 6 × STS3046。原 STS3215 × 2 方案取消。

---

# 8. Wheel System（轮组系统）

## Wheel Motor（轮毂电机）

冻结：

```text
GB37-520
```

---

## Voltage（额定电压）

```text
12V
```

---

## Gearbox（减速箱）

```text
Metal Gearbox
全金属减速箱
```

---

## Wheel Diameter（轮径）

冻结：

```text
80 mm
```

---

## Wheel Radius（轮半径）

```text
40 mm
```

---

# 9. Geometry Freeze（关键尺寸冻结）

## Pelvis Width（骨盆宽度）

```text
120 mm
```

---

## Pelvis Depth（骨盆前后）

```text
80 mm
```

---

## Pelvis Height（骨盆高度）

```text
60 mm
```

---

## Thigh Length（大腿长度）

```text
120 mm
```

---

## Calf Length（小腿长度）

```text
120 mm
```

---

## Wheel Diameter（轮径）

```text
80 mm
```

---

## Overall Height（整机高度）

```text
≈ 550 mm
```

---

# 10. Weight Budget（重量预算）

| Module       | Target Weight |
| ------------ | ------------: |
| Servos       |         700 g |
| Wheel System |         800 g |
| Battery      |         200 g |
| Electronics  |          50 g |
| Structure    |        1200 g |

---

Total：

```text
3.0kg ~ 4.0kg
```

---

# 11. Electrical Architecture（电气架构）

## Main Controller（主控）

冻结：

```text
ESP32 DevKitC-32E
```

---

负责：

* Servo Control（舵机控制）
* Wheel Control（轮组控制）
* IMU Processing（惯导处理）
* Inverse Kinematics（逆运动学）
* Gait Generation（步态生成）

---

## IMU（惯导）

推荐：

```text
ICM42688
```

备选：

```text
MPU6050
```

---

# 12. Power Architecture（供电架构）

## Main Battery（主电池）

```text
3S Li-ion
```

---

Nominal Voltage：

```text
11.1V
```

---

## Power Distribution（电源分配）

```text
Battery

├── Wheel Rail
│      11.1V
│
├── Servo Rail
│      7.4V
│
└── Logic Rail
       5V
```

---

## Wheel Power Rail（轮组供电）

```text
11.1V Direct
```

---

## Servo Power Rail（舵机供电）

通过 Buck Converter（降压模块）：

```text
11.1V → 7.4V
```

---

## Logic Power Rail（逻辑供电）

通过 Buck Converter：

```text
11.1V → 5V
```

---

# 13. Wiring Strategy（布线策略）

## Servo Bus（舵机总线）

采用：

```text
Daisy Chain
菊花链
```

连接方式。

---

## Internal Wiring（内部布线）

所有线束优先走：

```text
Carbon Tube
碳纤维管
```

内部。

---

优点：

* 美观
* 防缠绕
* 防磨损

---

# 14. Development Roadmap（开发路线）

## Phase 0

Servo Evaluation

舵机验证

---

## Phase 1

Single Joint Bench

单关节测试平台

---

## Phase 2

Single Leg Prototype

单腿原型

---

## Phase 3

Dual Leg Rig

双腿测试架

---

## Phase 4

Free Standing Robot

独立站立机器人

---

## Phase 5

Wheel Assisted Gait

轮足步态

---

## Phase 6

Obstacle Crossing

越障能力验证

---

# 15. Design Freeze Summary（设计冻结参数）

## Mechanical

```text
Height = 550 mm

Pelvis Width = 120 mm

Pelvis Depth = 80 mm

Pelvis Height = 60 mm

Thigh Length = 120 mm

Calf Length = 120 mm

Wheel Diameter = 80 mm
```

---

## Actuators

```text
Hip Roll  = STS3046

Hip Pitch = STS3046

Knee      = STS3046
```

> ECO-001 变更：踝关节取消，无 STS3215。
> 3 DOF/Leg × 2 Legs = 6 Servo DOF + 2 Wheel DOF = 8 Total DOF

---

## Electronics

```text
ESP32 DevKitC-32E

ICM42688

3S Li-ion
```

---

## Weight Target

```text
Target Weight < 4 kg
```

---

# End Of Document
