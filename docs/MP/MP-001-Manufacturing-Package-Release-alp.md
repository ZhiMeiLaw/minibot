# Mini-Atlas V6 Alpha

# MP-001 Manufacturing Package Release

Version: 1.0

Status: RELEASED

Document Number:

MP-001

Subsystem:

Full Robot

Release Type:

Manufacturing Package

Parent Documents:

* PR-001 Alpha Prototype Release
* CDS-03~CDS-09 Mechanical CAD & Digital Mockups
* DR-001~DR-010 Design Reviews
* SR-001 System Weight Budget

---

# 1. Purpose

提供 Mini-Atlas V6 Alpha 原型的完整制造包，保证：

* 可打印零件可直接制造
* 装配顺序清晰
* BOM 明确
* 重量与重心符合设计
* 电子线束、固件基线可同步安装

---

# 2. Scope

制造包包含：

* 全部 3D 打印件 (.stl / .f3d / .step)
* BOM 表格 (.xlsx)
* 装配说明文档 (.pdf)
* 重量报告 (.pdf)
* CG 报告 (.pdf)
* 线束布局图 (.pdf)
* 固件基线 (FW-001 ~ FW-003)

适用于：

* Alpha Prototype Build-1 制造
* 工程验证和初步调试
* 数字样机对照制造

---

# 3. Subsystem Files

| Subsystem    | Files                      |
| ------------ | -------------------------- |
| Hip Roll     | Base, Output, TorqueModule |
| Hip Pitch    | Base, Output, TorqueModule |
| Knee         | Base, Output, TorqueModule |
| Pelvis       | Full assembly              |
| Torso        | Structural frames          |
| Lower Leg    | Carbon Tube, Clamps        |
| Wheel Module | Assembly                   |
| Electronics  | Wiring Harness, Connectors |
| Firmware     | FW-001 ~ FW-003            |

---

# 4. BOM

* Excel 表格包含所有零件编号、数量、材料、供应商
* 与 PR-001 版本一致
* 明确标注 3D 打印件、硬件、舵机、轴承

---

# 5. Assembly Instructions

* 提供 PDF 装配手册
* 包含步骤、插图、爆炸视图、剖视图
* 强调零件安装顺序
* 特别标注维护可拆卸件

---

# 6. Weight & CG Reports

* 计算每个子系统重量
* 计算全机重心
* 确保 Alpha Prototype Build-1 满足稳定性要求

---

# 7. Line Harness & Electronics

* 提供线束主干布局
* 提供电源分配与信号接口图
* 标注固定点、走线通道
* 保证运动范围不干涉线束

---

# 8. Printability & Manufacturing Notes

* 打印材料：PETG
* 打印机：Bambu A1 Mini
* 支撑策略说明
* 层厚、填充率、壁厚规范
* 关键轴承座、安装孔方向标注

---

# 9. Firmware Baseline

* 包含 FW-001 ~ FW-003
* 用于 Alpha Prototype Build-1
* 支持所有舵机驱动、传感器接口
* 与机械、电子完全匹配

---

# 10. Freeze & Release

* 所有 CDS 文件冻结
* 所有 DR 审核通过
* Weight / CG / Kinematics 验证通过
* Status: RELEASED

---

# 11. Deliverables

Required Files:

* 3D CAD: f3d / step / stl
* BOM: XLSX
* Assembly Instructions: PDF
* Weight Report: PDF
* CG Report: PDF
* Wiring & Electronics Layout: PDF
* Firmware Baseline: FW-001~FW-003

---

# 12. Usage

* 制造 Alpha Prototype Build-1
* 作为调试和验证基线
* 后续迭代必须基于此版本进行 ECN 批准

---

# 13. Exit Criteria

* 所有零件打印可行
* 装配顺序清晰
* 全机重量及重心符合设计
* 线束及固件同步完成
* Alpha Prototype Build-1 可制造

Status: MANUFACTURING PACKAGE RELEASED
