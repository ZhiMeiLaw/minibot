# Mini-Atlas V6 Alpha

# DR-010 Leg Subsystem Review

Version: 1.0 Freeze A

Status: REVIEW

Review Number:

DR-010

Subsystem:

Leg Subsystem

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* CDS-03 Hip Roll Joint
* CDS-04 Hip Pitch Joint
* CDS-05 Knee Joint
* MDS-01 System Architecture
* MDS-02 Detailed Joint Design
* EDS-02 Power Budget & Current Analysis

---

# 1. Review Objective

验证完整腿部子系统是否满足：

* 结构要求
* 运动要求
* 扭矩要求
* 重心要求
* 制造要求
* 轮组集成要求

通过后：

允许进入：

CDS-06 Ankle Joint Design

---

# 2. Leg Architecture Overview

当前结构：

Pelvis

↓

Hip Roll

↓

Hip Pitch

↓

Upper Leg

↓

Knee

↓

Lower Leg

↓

Wheel Module (Future)

---

自由度：

Hip Roll

1 DOF

---

Hip Pitch

1 DOF

---

Knee

1 DOF

---

Total

3 DOF

Per Leg

---

# 3. Geometry Review

Upper Leg：

120 mm

---

Knee Center：

≈15 mm

---

Lower Leg：

120 mm

---

预估总腿长：

255 mm

---

结果：

PASS

---

# 4. Robot Height Verification

目标：

550 mm

---

腿部：

255 mm

---

Pelvis：

70 mm

---

Torso：

150 mm

---

Neck + Head：

75 mm

---

Foot/Wheel：

30 mm

---

总高度：

≈580 mm

---

误差：

+30 mm

---

评估：

可接受

---

结果：

PASS

---

# 5. Motion Envelope Review

Hip Pitch：

+60°

↓

-30°

---

Knee：

0°

↓

120°

---

验证动作：

站立

PASS

---

抬腿

PASS

---

坐下

PASS

---

半蹲

PASS

---

结果：

PASS

---

# 6. Walking Capability Review

估算步幅：

约：

120 mm

---

步频：

1~2 Hz

---

速度：

0.12~0.24 m/s

---

评估：

满足 V6 Alpha

---

结果：

PASS

---

# 7. Wheel Assisted Mode Review

设计：

Wheel Module

安装于 Lower Leg 底部

---

预留空间：

≥50 mm

---

安装方式：

4×M3

---

评估：

满足后续设计

---

结果：

PASS

---

# 8. Torque Budget Review

Hip Roll：

STS3046

利用率：

≈60%

---

Hip Pitch：

STS3046

利用率：

≈67%

---

Knee：

STS3046

利用率：

≈73%

---

最大：

Knee

---

评估：

仍有安全余量

---

结果：

PASS

---

# 9. Weight Budget Review

单腿：

Hip Roll：

约150 g

---

Hip Pitch：

约154 g

---

Knee：

约179 g

---

Carbon Tubes：

约40 g

---

Hardware：

约30 g

---

单腿总计：

≈553 g

---

双腿：

≈1.11 kg

---

目标：

<1.3 kg

---

结果：

PASS

---

# 10. Center Of Mass Review

当前布局：

Battery

位于 Pelvis

---

ESP32

位于 Pelvis

---

Servo

集中于髋部与膝部

---

评估：

重心位于骨盆附近

---

结果：

PASS

---

# 11. Structural Load Path Review

载荷路径：

Robot Weight

↓

Pelvis

↓

Hip Roll

↓

Hip Pitch

↓

Knee

↓

Wheel / Ground

---

特点：

所有关节均采用：

Bearing Supported Architecture

---

评估：

合理

---

结果：

PASS

---

# 12. Manufacturing Review

打印平台：

Bambu Lab A1

---

兼容：

Bambu Lab A1 Mini

---

最大打印件：

<100 mm

---

评估：

完全满足

---

结果：

PASS

---

# 13. Serviceability Review

Servo更换：

<5 min

---

Carbon Tube更换：

<5 min

---

Bearing更换：

<10 min

---

评估：

满足维护要求

---

结果：

PASS

---

# 14. Reliability Review

关键风险：

Knee Clamp Loosening

---

措施：

Loctite 243

M3×4 Clamp

---

关键风险：

PETG Fatigue

---

措施：

Triangular Rib

Brass Insert

---

关键风险：

Carbon Tube Slip

---

措施：

Dual Clamp

Micro Serration

---

评估：

风险可控

---

结果：

PASS

---

# 15. Future Expansion Review

兼容：

Ankle Joint

PASS

---

兼容：

Wheel Module

PASS

---

兼容：

Vision System

PASS

---

兼容：

Arm System

PASS

---

兼容：

STS3250 Upgrade

PASS

---

# 16. Leg Subsystem Freeze

Upper Leg

120 mm

---

Lower Leg

120 mm

---

Hip Roll

STS3046

---

Hip Pitch

STS3046

---

Knee

STS3046

---

Carbon Tube

OD 10mm × ID 8mm

---

Joint Shaft

Ø8 GCr15

---

Bearing

698-2RS

---

Architecture

Bearing Supported

---

Status

APPROVED

READY FOR

CDS-06 Ankle Joint Design
