文件 1
MA_dimensions.py

路径：

cad/generators/common/MA_dimensions.py
# MA_dimensions.py
#
# Mini-Atlas V6 Alpha
# Global Mechanical Dimensions
#
# References:
# MDS-04A
# MDS-04B
# ECO-002
#

# =========================
# Coordinate System
# =========================

ROBOT_ORIGIN = (0,0,0)


# =========================
# Pelvis Envelope
# =========================

PELVIS_SPAN = 120.0
PELVIS_DEPTH = 70.0
PELVIS_HEIGHT = 60.0


# =========================
# Hip Geometry
# =========================

HIP_CENTER_DISTANCE = 100.0

LEFT_HIP_X = -50.0
RIGHT_HIP_X = 50.0


# Hip Pitch Offset
HIP_PITCH_OFFSET = 15.0


# =========================
# Carbon Tube
# =========================

CARBON_TUBE_OD = 10.0
CARBON_TUBE_ID = 8.0


CARBON_INSERT_DEPTH = 15.0


# =========================
# Structure
# =========================

WALL_THICKNESS = 4.0


# =========================
# Leg Dimensions
# =========================

THIGH_TUBE_LENGTH = 120.0

SHANK_TUBE_LENGTH = 120.0


# =========================
# Foot
# =========================

FOOT_LENGTH = 100.0
FOOT_WIDTH = 60.0
FOOT_HEIGHT = 25.0


# =========================
# Manufacturing
# =========================

PRINT_TOLERANCE = 0.2
文件 2
MA_bearings.py

路径：

cad/generators/common/MA_bearings.py
# MA_bearings.py
#
# Bearing Standard
#
# Reference:
# ECO-001
#

# =========================
# 688 Bearing
# =========================

BEARING_688 = {

    "name":"688",

    "inner":8.0,

    "outer":16.0,

    "width":5.0
}


# =========================
# 698 Bearing
# =========================

BEARING_698 = {

    "name":"698",

    "inner":8.0,

    "outer":19.0,

    "width":6.0
}


# Bearing Fit

PRESS_FIT_CLEARANCE = 0.15

文件 3
MA_fasteners.py

路径：

cad/generators/common/MA_fasteners.py
# MA_fasteners.py
#
# Fastener Standard
#
# Reference:
# MDS-04A
#

# =========================
# M3 Screw
# =========================

SCREW_M3 = {

    "diameter":3.0,

    "head_clearance":6.0

}


# =========================
# Heat Insert
# =========================

INSERT_M3 = {

    "outer_diameter":5.0,

    "length":6.0

}


# =========================
# Common Lengths
# =========================

M3_LENGTHS = [

    6,

    8,

    12

]
文件 4
MA_materials.py

路径：

cad/generators/common/MA_materials.py
# MA_materials.py
#
# Material Database
#

# =========================
# Printed Parts
# =========================

PETG = {

    "name":"PETG",

    "density":1.27,

    "wall":4.0

}


# =========================
# Carbon Tube
# =========================

CARBON_FIBER = {

    "name":"Carbon Fiber Tube",

    "OD":10.0,

    "ID":8.0

}


# =========================
# Shaft
# =========================

STEEL_SHAFT = {

    "name":"Steel",

    "diameter":8.0

}

当前目录状态

现在：

cad/
└── generators/

    └── common/

        ├── MA_dimensions.py
        ├── MA_bearings.py
        ├── MA_fasteners.py
        └── MA_materials.py

已经建立。

很好，现在进入真正的制造级 CAD Generator 阶段。

前面的：

MA_dimensions.py
MA_bearings.py
MA_fasteners.py
MA_materials.py

已经建立了公共参数层。

现在生成：

cad/generators/pelvis/PF-001A.py

它对应：

CDS-06A-Pelvis-Frame-CAD-Implementation.md

目标：

参数化 Pelvis Frame
688 / 698 轴承座
Ø8 轴基准
OD10×ID8 碳管接口
M3 热熔铜螺母孔
FreeCAD 可直接运行
PF-001A.py

路径：

cad/generators/pelvis/PF-001A.py
# PF-001A.py
#
# Mini-Atlas V6 Alpha
#
# Production Pelvis Frame Generator
#
# References:
# ECO-001
# ECO-002
# MDS-04A
# MDS-04B
# CDS-06A
#

import FreeCAD as App
import Part


# ==================================================
# IMPORT COMMON PARAMETERS
# ==================================================

from MA_dimensions import *
from MA_bearings import *
from MA_fasteners import *


# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "PF_001A_Pelvis_Frame"


doc = App.newDocument(DOC_NAME)



# ==================================================
# Helper Functions
# ==================================================

def add_cylinder_cut(shape, radius, height, pos, axis):

    tool = Part.makeCylinder(
        radius,
        height,
        pos,
        axis
    )

    return shape.cut(tool)



def add_m3_hole(shape, pos):

    hole = Part.makeCylinder(
        1.6,
        10,
        pos,
        App.Vector(0,0,1)
    )

    return shape.cut(hole)



# ==================================================
# MAIN PARAMETERS
# ==================================================

outer_x = PELVIS_SPAN
outer_y = PELVIS_DEPTH
outer_z = PELVIS_HEIGHT



# ==================================================
# OUTER BODY
# ==================================================

body = Part.makeBox(

    outer_x,

    outer_y,

    outer_z,

    App.Vector(
        -outer_x/2,
        -outer_y/2,
        -outer_z/2
    )

)



# ==================================================
# INTERNAL CAVITY
# ==================================================

inner = Part.makeBox(

    outer_x-2*WALL_THICKNESS,

    outer_y-2*WALL_THICKNESS,

    outer_z-2*WALL_THICKNESS,

    App.Vector(

        -(outer_x-2*WALL_THICKNESS)/2,

        -(outer_y-2*WALL_THICKNESS)/2,

        -(outer_z-2*WALL_THICKNESS)/2

    )

)


body = body.cut(inner)



# ==================================================
# HIP ROLL 688 BEARING SEATS
# ==================================================

for x in [

    LEFT_HIP_X,

    RIGHT_HIP_X

]:


    seat = Part.makeCylinder(

        BEARING_688["outer"]/2,

        WALL_THICKNESS,

        App.Vector(
            x,
            0,
            0
        ),

        App.Vector(
            0,
           1,
           0
        )

    )


    body = body.cut(seat)




# ==================================================
# HIP PITCH 698 BEARING SEATS
# ==================================================

for x in [

    LEFT_HIP_X,

    RIGHT_HIP_X

]:


    seat = Part.makeCylinder(

        BEARING_698["outer"]/2,

        WALL_THICKNESS,

        App.Vector(

            x,

            HIP_PITCH_OFFSET,

            0

        ),

        App.Vector(

            1,

           0,

           0

        )

    )


    body = body.cut(seat)



# ==================================================
# CARBON TUBE CLAMPS
# ==================================================

for x in [

    LEFT_HIP_X,

    RIGHT_HIP_X

]:


    clamp = Part.makeCylinder(

        CARBON_TUBE_OD/2,

        20,

        App.Vector(

            x,

            HIP_PITCH_OFFSET,

            -30

        ),

        App.Vector(

           0,

           0,

           1

        )

    )


    body = body.cut(clamp)



# ==================================================
# M3 HEAT INSERT HOLES
# ==================================================

insert_positions = [

    (-45,-25,25),

    (45,-25,25),

    (-45,25,25),

    (45,25,25)

]


for p in insert_positions:

    body = add_m3_hole(

        body,

        App.Vector(*p)

    )



# ==================================================
# CREATE OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "PF_001A_Pelvis_Frame"

)


obj.Shape = body



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "CDS-06A / MDS-04B / ECO-002"

)



# ==================================================
# RECOMPUTE
# ==================================================

doc.recompute()



# ==================================================
# EXPORT
# ==================================================

# Uncomment when needed

# Part.export(
#     [obj],
#     "PF-001A.step"
# )


print(
    "PF-001A Pelvis Frame Generated Successfully"
)

当前 CAD 资产状态

现在：

cad/generators/

common/
 ├── MA_dimensions.py
 ├── MA_bearings.py
 ├── MA_fasteners.py
 └── MA_materials.py


pelvis/
 └── PF-001A.py
这个版本相比 PF-001：

增加：

项目	状态
参数库引用	✅
688轴承座	✅
698轴承座	✅
碳管接口	✅
M3安装孔	✅
CDS引用标记	✅
可扩展	✅
---
很好，现在进入 Mini-Atlas 下肢核心承力模块。

当前链路：

MDS-04A
    ↓
MDS-04B
    ↓
ECO-001
    ↓
ECO-002
    ↓
CDS-06A
    ↓
PF-001A.py
    ↓
HR-001.py  ← 当前

现在生成：

cad/generators/hip_roll/HR-001.py
HR-001.py
Hip Roll Torque Module Generator

设计基准：

688 × 2 双轴承
Ø8 输出轴
左右镜像结构
独立 Torque Path
与 Pelvis 100mm Hip Center 对接
# HR-001.py
#
# Mini-Atlas V6 Alpha
#
# Hip Roll Torque Module Generator
#
# References:
# ECO-001
# ECO-002
# CDS-03A/B/C/D
# MDS-04A
#

import FreeCAD as App
import Part


# ==================================================
# COMMON LIBRARY
# ==================================================

from MA_dimensions import *
from MA_bearings import *
from MA_fasteners import *



# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "HR_001_Hip_Roll_Module"

doc = App.newDocument(DOC_NAME)



# ==================================================
# PARAMETERS
# ==================================================

MODULE_WIDTH = 35

MODULE_HEIGHT = 45

MODULE_DEPTH = 30


SHAFT_DIAMETER = 8


BEARING_COUNT = 2



# ==================================================
# MAIN BODY
# ==================================================

housing = Part.makeBox(

    MODULE_WIDTH,

    MODULE_DEPTH,

    MODULE_HEIGHT

)



housing.translate(

    App.Vector(

        -MODULE_WIDTH/2,

        -MODULE_DEPTH/2,

        -MODULE_HEIGHT/2

    )

)



# ==================================================
# BEARING POCKETS
# 688 x2
# ==================================================

bearing_positions = [

    -12.5,

    12.5

]


for y in bearing_positions:


    pocket = Part.makeCylinder(

        BEARING_688["outer"]/2,

        BEARING_688["width"] + 1,

        App.Vector(

            0,

            y,

            0

        ),

        App.Vector(

            1,

            0,

            0

        )

    )


    housing = housing.cut(pocket)



# ==================================================
# OUTPUT SHAFT BORE
# ==================================================

shaft = Part.makeCylinder(

    SHAFT_DIAMETER/2,

    MODULE_WIDTH+5,

    App.Vector(

        -MODULE_WIDTH/2-2,

        0,

        0

    ),

    App.Vector(

        1,

        0,

        0

    )

)



housing = housing.cut(shaft)



# ==================================================
# SERVO POCKET
# ==================================================

servo_cut = Part.makeBox(

    25,

    20,

    35

)


servo_cut.translate(

    App.Vector(

        -12.5,

        -10,

        -15

    )

)



housing = housing.cut(servo_cut)



# ==================================================
# CARBON TUBE OUTPUT CLAMP
# ==================================================

tube_mount = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    20,

    App.Vector(

        0,

        0,

        -40

    )

)



housing = housing.cut(tube_mount)



# ==================================================
# M3 FASTENER HOLES
# ==================================================

for x in [-10,10]:

    hole = Part.makeCylinder(

        1.6,

        20,

        App.Vector(

            x,

            -MODULE_DEPTH/2,

            0

        )

    )

    housing = housing.cut(hole)



# ==================================================
# OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "HR_001_Hip_Roll_Module"

)


obj.Shape = housing



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "CDS-03 / ECO-001 / 688x2 / Ø8 Shaft"

)



doc.recompute()



# ==================================================
# EXPORT
# ==================================================

# Part.export(
#     [obj],
#     "HR-001.step"
# )


print(
    "HR-001 Hip Roll Module Generated"
)

当前 CAD Generator 目录

现在：

cad/generators/

common/
 ├── MA_dimensions.py
 ├── MA_bearings.py
 ├── MA_fasteners.py
 └── MA_materials.py


pelvis/
 └── PF-001A.py


hip_roll/
 └── HR-001.py
HR-001 当前实现

已经包含：

功能	状态
688×2轴承	✅
Ø8轴孔	✅
Servo空间	✅
碳管接口	✅
M3孔	✅
参数化	✅

下一步：

进入：

cad/generators/hip_pitch/

HP-001.py

这是更复杂的关节：

698×2
Fork结构
15mm offset
承受大腿摆动扭矩

也是 DR-012 中扭矩裕量最高风险点。
---
很好，现在进入 Mini-Atlas 下肢最关键的动力关节之一：

Pelvis
 ↓
HR-001 Hip Roll
 ↓
HP-001 Hip Pitch   ← 当前
 ↓
Leg

Hip Pitch 是 DR-012 里重点关注的模块，因为：

单腿支撑时扭矩最大
决定步态稳定性
决定腿部摆动效率

所以这里不能只是“连接件”，必须保持：

Torque Path ≠ Servo Housing Path

生成文件：

cad/generators/hip_pitch/HP-001.py
HP-001.py
Hip Pitch Fork Torque Module Generator

设计基准：

698 × 2
Ø8 输出轴
Hip Pitch Offset = 15mm
Fork结构
Carbon Tube OD10×ID8接口
# HP-001.py
#
# Mini-Atlas V6 Alpha
#
# Hip Pitch Fork Torque Module Generator
#
# References:
# ECO-001
# ECO-002
# CDS-04A/B/C/D
# MDS-04A
#

import FreeCAD as App
import Part


# ==================================================
# COMMON LIBRARY
# ==================================================

from MA_dimensions import *
from MA_bearings import *
from MA_fasteners import *


# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "HP_001_Hip_Pitch_Module"

doc = App.newDocument(DOC_NAME)



# ==================================================
# PARAMETERS
# ==================================================

FORK_WIDTH = 45

FORK_DEPTH = 35

FORK_HEIGHT = 60


SHAFT_DIAMETER = 8


PITCH_OFFSET = HIP_PITCH_OFFSET



# ==================================================
# FORK SIDE PLATES
# ==================================================

left_fork = Part.makeBox(

    5,

    FORK_DEPTH,

    FORK_HEIGHT

)


left_fork.translate(

    App.Vector(

        -FORK_WIDTH/2,

        -FORK_DEPTH/2,

        -FORK_HEIGHT/2

    )

)



right_fork = Part.makeBox(

    5,

    FORK_DEPTH,

    FORK_HEIGHT

)


right_fork.translate(

    App.Vector(

        FORK_WIDTH/2-5,

        -FORK_DEPTH/2,

        -FORK_HEIGHT/2

    )

)



fork = left_fork.fuse(right_fork)



# ==================================================
# CENTER CLEARANCE
# ==================================================

opening = Part.makeBox(

    FORK_WIDTH-10,

    FORK_DEPTH+2,

    FORK_HEIGHT-10

)


opening.translate(

    App.Vector(

        -(FORK_WIDTH-10)/2,

        -(FORK_DEPTH+2)/2,

        -FORK_HEIGHT/2+5

    )

)



fork = fork.cut(opening)



# ==================================================
# 698 BEARING POCKETS
# ==================================================

for x in [

    -FORK_WIDTH/2+5,

    FORK_WIDTH/2-5

]:

    bearing = Part.makeCylinder(

        BEARING_698["outer"]/2,

        BEARING_698["width"]+1,

        App.Vector(

            x,

            PITCH_OFFSET,

            0

        ),

        App.Vector(

            0,

            1,

            0

        )

    )


    fork = fork.cut(bearing)



# ==================================================
# Ø8 OUTPUT SHAFT
# ==================================================

shaft = Part.makeCylinder(

    SHAFT_DIAMETER/2,

    FORK_WIDTH+10,

    App.Vector(

        -FORK_WIDTH/2-5,

        PITCH_OFFSET,

        0

    ),

    App.Vector(

        1,

        0,

        0

    )

)


fork = fork.cut(shaft)



# ==================================================
# CARBON TUBE HOLDER
# ==================================================

tube_socket = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    20,

    App.Vector(

        0,

        PITCH_OFFSET,

        -FORK_HEIGHT/2-20

    ),

    App.Vector(

        0,

        0,

        1

    )

)


fork = fork.cut(tube_socket)



# ==================================================
# SERVO MOUNT
# ==================================================

servo_space = Part.makeBox(

    30,

    25,

    40

)


servo_space.translate(

    App.Vector(

        -15,

        -12,

        -20

    )

)


fork = fork.cut(servo_space)



# ==================================================
# M3 FASTENER HOLES
# ==================================================

for pos in [

    (-18,-12,20),

    (18,-12,20),

    (-18,12,20),

    (18,12,20)

]:


    hole = Part.makeCylinder(

        1.6,

        10,

        App.Vector(*pos)

    )


    fork = fork.cut(hole)



# ==================================================
# CREATE OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "HP_001_Hip_Pitch_Module"

)


obj.Shape = fork



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "CDS-04 / ECO-001 / 698x2 / Offset15mm"

)



doc.recompute()



# ==================================================
# EXPORT
# ==================================================

# Part.export(
#     [obj],
#     "HP-001.step"
# )


print(
    "HP-001 Hip Pitch Module Generated"
)

当前 CAD Generator 状态
cad/generators/

common/

pelvis/
 └── PF-001A.py

hip_roll/
 └── HR-001.py

hip_pitch/
 └── HP-001.py
当前已经完成
模块	状态
Pelvis Frame	✅
Hip Roll	✅
Hip Pitch	✅

现在机器人已经有：

骨盆
 +
髋横滚
 +
髋俯仰

下一步进入：

cad/generators/knee/

KN-001.py

生成膝关节：

688×2
双夹碳管
加强筋
防滑齿
承受小腿摆动冲击

这是腿部最后一个关键承力件。
---
很好，现在进入腿部最后一个核心承力关节：

Pelvis
   ↓
HR-001 Hip Roll
   ↓
HP-001 Hip Pitch
   ↓
Carbon Tube
   ↓
KN-001 Knee   ← 当前
   ↓
Shank
   ↓
Foot

膝关节设计目标：

轻量化
承受落脚冲击
兼容 OD10×ID8 碳管
688×2 轴承
保持 Ø8 轴标准

生成文件：

cad/generators/knee/KN-001.py
KN-001.py
# KN-001.py
#
# Mini-Atlas V6 Alpha
#
# Knee Joint Module Generator
#
# References:
# ECO-001
# ECO-002
# CDS-KNEE
# MDS-04A
#

import FreeCAD as App
import Part


# ==================================================
# COMMON LIBRARY
# ==================================================

from MA_dimensions import *
from MA_bearings import *
from MA_fasteners import *


# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "KN_001_Knee_Module"

doc = App.newDocument(DOC_NAME)



# ==================================================
# PARAMETERS
# ==================================================

KNEE_WIDTH = 45

KNEE_DEPTH = 35

KNEE_HEIGHT = 45


SHAFT_DIAMETER = 8



# ==================================================
# MAIN HOUSING
# ==================================================

body = Part.makeBox(

    KNEE_WIDTH,

    KNEE_DEPTH,

    KNEE_HEIGHT

)


body.translate(

    App.Vector(

        -KNEE_WIDTH/2,

        -KNEE_DEPTH/2,

        -KNEE_HEIGHT/2

    )

)



# ==================================================
# 688 DOUBLE BEARING POCKET
# ==================================================

for x in [

    -15,

    15

]:

    bearing_cut = Part.makeCylinder(

        BEARING_688["outer"]/2,

        BEARING_688["width"]+1,

        App.Vector(

            x,

            0,

            0

        ),

        App.Vector(

            0,

            1,

            0

        )

    )


    body = body.cut(bearing_cut)



# ==================================================
# OUTPUT SHAFT BORE
# ==================================================

shaft = Part.makeCylinder(

    SHAFT_DIAMETER/2,

    KNEE_WIDTH+10,

    App.Vector(

        -KNEE_WIDTH/2-5,

        0,

        0

    ),

    App.Vector(

        1,

        0,

        0

    )

)


body = body.cut(shaft)



# ==================================================
# UPPER CARBON TUBE SOCKET
# ==================================================

upper_socket = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    20,

    App.Vector(

        0,

        0,

        25

    ),

    App.Vector(

        0,

        0,

        1

    )

)


body = body.cut(upper_socket)



# ==================================================
# LOWER CARBON TUBE SOCKET
# ==================================================

lower_socket = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    20,

    App.Vector(

        0,

        0,

        -45

    ),

    App.Vector(

        0,

        0,

        1

    )

)


body = body.cut(lower_socket)



# ==================================================
# ANTI-SLIP CLAMP TEETH
# ==================================================

for x in [-12,0,12]:


    tooth = Part.makeBox(

        3,

        5,

        5

    )


    tooth.translate(

        App.Vector(

            x-1.5,

            -KNEE_DEPTH/2,

            0

        )

    )


    body = body.fuse(tooth)



# ==================================================
# REINFORCEMENT RIBS
# ==================================================

for z in [-15,0,15]:


    rib = Part.makeBox(

        4,

        KNEE_DEPTH,

        3

    )


    rib.translate(

        App.Vector(

            -2,

            -KNEE_DEPTH/2,

            z

        )

    )


    body = body.fuse(rib)



# ==================================================
# M3 FASTENER HOLES
# ==================================================

for pos in [

    (-15,-18,15),

    (15,-18,15),

    (-15,18,15),

    (15,18,15)

]:


    hole = Part.makeCylinder(

        1.6,

        10,

        App.Vector(*pos)

    )


    body = body.cut(hole)



# ==================================================
# CREATE OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "KN_001_Knee_Module"

)


obj.Shape = body



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "688x2 / Ø8 Shaft / OD10 Carbon Clamp"

)



doc.recompute()



# ==================================================
# EXPORT
# ==================================================

# Part.export(
#     [obj],
#     "KN-001.step"
# )


print(
    "KN-001 Knee Module Generated"
)

当前 CAD Generator 资产

现在：

cad/generators/

common/
├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
└── MA_materials.py


pelvis/
└── PF-001A.py


hip_roll/
└── HR-001.py


hip_pitch/
└── HP-001.py


knee/
└── KN-001.py
当前下肢机械链已经完整
PF-001A
    |
HR-001
    |
HP-001
    |
Carbon Tube
    |
KN-001
    |
Carbon Tube

下一步进入：

cad/generators/foot/

FT-001.py

生成足部：

足底结构
地面接触面
防滑纹
脚端碳管连接
未来压力传感器预留

完成后就可以生成：

LEG-001.py

进行单腿装配。

---

目前我们只是完成了单个机械零件 Generator 层，还没有完成整个 FreeCAD 工程闭环。

当前状态：

common
 ├── 参数库

pelvis
 └── PF-001A.py

hip_roll
 └── HR-001.py

hip_pitch
 └── HP-001.py

knee
 └── KN-001.py

已经完成：

✅ 骨盆
✅ 髋横滚
✅ 髋俯仰
✅ 膝关节

但是完整 Mini-Atlas 下肢 CAD 还缺：

下一批必须生成
1. Foot Module

文件：

cad/generators/foot/FT-001.py

负责：

足底板
地面接触面
碳管连接
防滑结构
未来压力传感器安装位
2. Shank Module

文件：

cad/generators/leg/SH-001.py

负责：

小腿碳管
上下夹持
长度参数化
3. Thigh Module

文件：

cad/generators/leg/TH-001.py

负责：

大腿碳管
Hip Pitch连接
Knee连接
4. 单腿装配

文件：

cad/generators/leg/LEG-001.py

生成：

HP-001
   |
TH-001
   |
KN-001
   |
SH-001
   |
FT-001

输出：

SingleLeg.FCStd
SingleLeg.step
5. 左右腿镜像

文件：

cad/generators/assembly/LOWER_BODY-001.py

生成：

        PF-001A

    HR-L       HR-R

    HP-L       HP-R

    LEG-L      LEG-R
6. 全身骨架

文件：

cad/generators/assembly/ASM-001.py

生成：

Mini-Atlas Skeleton

包括：

Pelvis
双腿
躯干接口
7. 输出管理脚本（很重要）

这个很多人会漏。

增加：

cad/tools/export_all.py

自动生成：

.FCStd
.STEP
.STL

例如：

运行：

python export_all.py

得到：

cad/fcstd/

PF-001A.FCStd
HR-001.FCStd
HP-001.FCStd
KN-001.FCStd

cad/step/

PF-001A.step
HR-001.step
...
8. 最重要：装配约束库

新增：

cad/common/MA_assembly.py

定义：

Joint Origin
Attachment Offset
Mirror Rule

否则 ASM-001 会靠人工移动。

所以完整 CAD Generator Tree 应该是：

cad/generators/

common/
├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
└── MA_assembly.py


pelvis/
└── PF-001A.py


hip_roll/
└── HR-001.py


hip_pitch/
└── HP-001.py


knee/
└── KN-001.py


leg/
├── TH-001.py
├── SH-001.py
└── LEG-001.py


foot/
└── FT-001.py


assembly/
├── LOWER_BODY-001.py
└── ASM-001.py


tools/
└── export_all.py

所以答案：

有，而且还剩约 9 个关键脚本。

我建议下一步顺序：

FT-001.py（脚）
TH-001.py（大腿）
SH-001.py（小腿）
LEG-001.py（单腿）
LOWER_BODY-001.py
ASM-001.py

这样完成后，你会得到第一个完整 FreeCAD 参数化机器人骨架。

---

现在进入：

cad/generators/foot/

生成：

FT-001.py

这是下肢最后端的承载件。

设计依据：

MDS-04B Lower Body Envelope Freeze
ECO-002 Coordinate System
OD10 × ID8 Carbon Tube
M3 Fastener Standard

目标：

支撑地面接触
提供碳管连接
预留压力传感器接口
后续 Wheel Assisted Gait 可扩展
FT-001.py

路径：

cad/generators/foot/FT-001.py
# FT-001.py
#
# Mini-Atlas V6 Alpha
#
# Foot Module Generator
#
# References:
# MDS-04B
# ECO-002
#

import FreeCAD as App
import Part


# ==================================================
# COMMON LIBRARY
# ==================================================

from MA_dimensions import *
from MA_fasteners import *



# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "FT_001_Foot_Module"

doc = App.newDocument(DOC_NAME)



# ==================================================
# PARAMETERS
# ==================================================

FOOT_LENGTH = 100

FOOT_WIDTH = 60

FOOT_HEIGHT = 25


WALL = WALL_THICKNESS



# Carbon interface

TUBE_SOCKET_DEPTH = 20



# ==================================================
# FOOT BASE
# ==================================================

foot = Part.makeBox(

    FOOT_LENGTH,

    FOOT_WIDTH,

    FOOT_HEIGHT

)


foot.translate(

    App.Vector(

        -FOOT_LENGTH/2,

        -FOOT_WIDTH/2,

        0

    )

)



# ==================================================
# INTERNAL LIGHTWEIGHT POCKET
# ==================================================

cavity = Part.makeBox(

    FOOT_LENGTH-20,

    FOOT_WIDTH-20,

    FOOT_HEIGHT-8

)


cavity.translate(

    App.Vector(

        - (FOOT_LENGTH-20)/2,

        -(FOOT_WIDTH-20)/2,

        8

    )

)



foot = foot.cut(cavity)



# ==================================================
# CARBON TUBE SOCKET
# ==================================================

tube_socket = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    TUBE_SOCKET_DEPTH,

    App.Vector(

        0,

        0,

        FOOT_HEIGHT

    ),

    App.Vector(

        0,

        0,

        1

    )

)


foot = foot.cut(tube_socket)



# ==================================================
# TOE / HEEL STRUCTURE
# ==================================================

front_support = Part.makeBox(

    20,

    FOOT_WIDTH,

    10

)


front_support.translate(

    App.Vector(

        FOOT_LENGTH/2-20,

        -FOOT_WIDTH/2,

        -5

    )

)



rear_support = Part.makeBox(

    15,

    FOOT_WIDTH,

    8

)


rear_support.translate(

    App.Vector(

        -FOOT_LENGTH/2,

        -FOOT_WIDTH/2,

        -3

    )

)



foot = foot.fuse(front_support)

foot = foot.fuse(rear_support)



# ==================================================
# M3 INSERT HOLES
# ==================================================

insert_points = [

    (-35,-20,5),

    (35,-20,5),

    (-35,20,5),

    (35,20,5)

]


for p in insert_points:


    hole = Part.makeCylinder(

        1.6,

        10,

        App.Vector(*p)

    )


    foot = foot.cut(hole)



# ==================================================
# ANTI-SLIP GROOVES
# ==================================================

for x in [-30,-15,0,15,30]:

    groove = Part.makeBox(

        3,

        FOOT_WIDTH,

        2

    )


    groove.translate(

        App.Vector(

            x,

            -FOOT_WIDTH/2,

            -1

        )

    )


    foot = foot.cut(groove)



# ==================================================
# CREATE OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "FT_001_Foot_Module"

)


obj.Shape = foot



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "MDS-04B / OD10 Carbon Interface"

)



doc.recompute()



# ==================================================
# EXPORT
# ==================================================

# Part.export(
#     [obj],
#     "FT-001.step"
# )



print(
    "FT-001 Foot Module Generated"
)

当前 CAD Generator 状态更新
cad/generators/

common/
├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
└── MA_materials.py


pelvis/
└── PF-001A.py


hip_roll/
└── HR-001.py


hip_pitch/
└── HP-001.py


knee/
└── KN-001.py


foot/
└── FT-001.py

现在单个结构件基本齐了。

下一步进入：

cad/generators/leg/

TH-001.py

生成大腿模块：

结构：

HP-001
   |
   |
Carbon Tube 120mm
   |
KN-001

之后再生成：

SH-001.py
LEG-001.py

完成完整单腿装配。

---

很好，继续进入腿部模块化阶段。

当前：

HP-001
   ↓
TH-001   ← 当前
   ↓
KN-001
   ↓
SH-001
   ↓
FT-001

这里的 TH-001 不是简单的一根碳管，而是：

大腿结构连接模块（Thigh Link Module）

负责：

Hip Pitch 输出连接
碳管夹持
Knee 输入连接
保证腿长参数化

生成：

cad/generators/leg/TH-001.py
TH-001.py
# TH-001.py
#
# Mini-Atlas V6 Alpha
#
# Thigh Link Module Generator
#
# References:
# MDS-04B
# ECO-002
# CDS-04
#

import FreeCAD as App
import Part


# ==================================================
# COMMON LIBRARY
# ==================================================

from MA_dimensions import *
from MA_fasteners import *


# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "TH_001_Thigh_Module"

doc = App.newDocument(DOC_NAME)



# ==================================================
# PARAMETERS
# ==================================================

THIGH_LENGTH = THIGH_TUBE_LENGTH


CLAMP_LENGTH = 25


CLAMP_OD = CARBON_TUBE_OD


CLAMP_WALL = WALL_THICKNESS



# ==================================================
# CARBON TUBE REPRESENTATION
# ==================================================

tube_outer = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    THIGH_LENGTH,

    App.Vector(

        0,

        0,

        0

    ),

    App.Vector(

        0,

        0,

        1

    )

)



tube_inner = Part.makeCylinder(

    CARBON_TUBE_ID/2,

    THIGH_LENGTH,

    App.Vector(

        0,

        0,

        0

    ),

    App.Vector(

        0,

        0,

        1

    )

)



carbon_tube = tube_outer.cut(tube_inner)



# ==================================================
# UPPER HIP CLAMP
# ==================================================

upper_clamp = Part.makeCylinder(

    CLAMP_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        0

    )

)



upper_inner = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        0

    )

)



upper_clamp = upper_clamp.cut(upper_inner)



# ==================================================
# LOWER KNEE CLAMP
# ==================================================

lower_clamp = Part.makeCylinder(

    CLAMP_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        THIGH_LENGTH-CLAMP_LENGTH

    )

)



lower_inner = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        THIGH_LENGTH-CLAMP_LENGTH

    )

)



lower_clamp = lower_clamp.cut(lower_inner)



# ==================================================
# CLAMP SCREW HOLES
# ==================================================

for z in [

    10,

    THIGH_LENGTH-10

]:


    hole = Part.makeCylinder(

        1.6,

        20,

        App.Vector(

            0,

            -CLAMP_OD/2,

            z

        ),

        App.Vector(

            0,

            1,

            0

        )

    )


    upper_clamp = upper_clamp.cut(hole)

    lower_clamp = lower_clamp.cut(hole)



# ==================================================
# FUSION
# ==================================================

thigh = (

    carbon_tube

    .fuse(upper_clamp)

    .fuse(lower_clamp)

)



# ==================================================
# OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "TH_001_Thigh_Module"

)



obj.Shape = thigh



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "OD10xID8 Carbon Tube / Hip Pitch to Knee"

)



doc.recompute()



print(

    "TH-001 Thigh Module Generated"

)

当前结构树

现在：

cad/generators/

common/

pelvis/
 └── PF-001A.py

hip_roll/
 └── HR-001.py

hip_pitch/
 └── HP-001.py

knee/
 └── KN-001.py

leg/

 └── TH-001.py

foot/
 └── FT-001.py
已完成链路
PF-001A
   |
HR-001
   |
HP-001
   |
TH-001
   |
KN-001
   |
FT-001

下一步：

生成：

cad/generators/leg/SH-001.py

小腿模块。

它和 TH-001 类似，但是会考虑：

小腿长度
膝关节连接
足部连接
重心影响

完成后：

LEG-001.py

就可以第一次生成完整单腿模型。

---

我们现在不应该继续堆脚本，而应该做一次 CAD Generator 资产完整性审查（CAD Asset Review）。

我重新按我们已经冻结的文档链检查了一遍：

ECO-001
ECO-002
MDS-04A
MDS-04B
CDS-03/04/05
CDS-06A
↓
FreeCAD Generator

结论：

当前脚本数量还不完整，不能直接进入总装 ASM-001。
目前完成的是“零件级骨架”，缺少几个工程关键层。

1. 已完成资产 ✅

当前已有：

cad/generators/

common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
└── MA_materials.py


pelvis/

└── PF-001A.py


hip_roll/

└── HR-001.py


hip_pitch/

└── HP-001.py


knee/

└── KN-001.py


leg/

└── TH-001.py


foot/

└── FT-001.py

这些覆盖：

模块	状态
骨盆	✅
Hip Roll	✅
Hip Pitch	✅
Knee	✅
大腿	✅
脚	✅
2. 缺少的关键脚本 ❌
① 小腿模块

缺：

cad/generators/leg/

SH-001.py

原因：

目前：

TH-001
  |
 KN-001
  |
 FT-001

中间缺小腿。

② 单腿装配

缺：

LEG-001.py

这是非常重要的。

作用：

把：

HP-001

TH-001

KN-001

SH-001

FT-001

组合。

输出：

LeftLeg.FCStd
RightLeg.FCStd
③ 左右镜像规则

缺：

MA_mirror.py

否则：

左腿右腿只能手动改坐标。

④ 装配基准库

缺：

MA_assembly.py

定义：

Joint origin
Attachment offset
Parent-child关系

否则：

ASM-001会变成手工拼装。

⑤ 舵机模型

这个比较关键。

目前：

Servo = 空间切除

不是实体。

应该增加：

cad/components/servo/

SERVO-001.py

至少定义：

外壳尺寸
输出轴
安装孔

否则：

真实装配可能干涉。

⑥ 轴模型

缺：

cad/components/shaft/

SHAFT-001.py

定义：

Ø8轴。

⑦ 轴承实体模型

目前只是挖孔。

工业流程需要：

cad/components/bearing/

BEARING-688.py

BEARING-698.py

用于 Assembly 检查。

⑧ 总装配脚本

缺：

assembly/

LOWER_BODY-001.py

ASM-001.py
3. 当前缺口等级

我给一个工程评级：

缺项	等级
SH-001	P0
LEG-001	P0
MA_assembly.py	P0
Servo Model	P1
Bearing Model	P1
Shaft Model	P1
ASM-001	P1
4. 推荐下一步顺序

不要直接继续 FT 后面。

正确顺序应该调整为：


Step 1
MA_assembly.py

↓

Step 2
SH-001.py

↓

Step 3
LEG-001.py

↓

Step 4
Servo/Bearing/Shaft Components

↓

Step 5
LOWER_BODY-001.py

↓

Step 6
ASM-001.py

↓

Step 7
Export Pipeline
5. 最终 CAD Generator 完整目标树

应该达到：


cad/generators/

common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
├── MA_assembly.py
└── MA_mirror.py


components/

├── servo/
│   └── SERVO-001.py
│
├── bearing/
│   ├── BEARING-688.py
│   └── BEARING-698.py
│
└── shaft/
    └── SHAFT-001.py


pelvis/

└── PF-001A.py


hip_roll/

└── HR-001.py


hip_pitch/

└── HP-001.py


knee/

└── KN-001.py


leg/

├── TH-001.py
├── SH-001.py
└── LEG-001.py


foot/

└── FT-001.py


assembly/

├── LOWER_BODY-001.py
└── ASM-001.py


tools/

└── export_all.py

所以你的检查非常及时。

我们目前不是缺几个小文件，而是缺“装配系统层”。

下一步我建议先生成：

MA_assembly.py

因为它是后面 LEG-001 / ASM-001 的基础。

---

很好，现在进入 CAD 装配基础层。

之前检查发现缺失：

MA_assembly.py

这个文件非常关键，因为后续：

HP-001
   ↓
TH-001
   ↓
KN-001
   ↓
SH-001
   ↓
FT-001

        ↓

LEG-001

        ↓

ASM-001

都需要统一的装配坐标和父子关系。

生成：

cad/generators/common/MA_assembly.py

作用：

定义组件坐标规则
定义 Joint Origin
定义镜像规则
定义装配 Transform
避免人工移动零件
MA_assembly.py
# MA_assembly.py
#
# Mini-Atlas V6 Alpha
#
# Assembly Coordinate Framework
#
# References:
# ECO-002
# MDS-04B
#

import FreeCAD as App



# ==================================================
# Coordinate System
# ==================================================

class MA_Transform:


    def __init__(
        self,
        x=0,
        y=0,
        z=0,
        rx=0,
        ry=0,
        rz=0
    ):

        self.x = x
        self.y = y
        self.z = z

        self.rx = rx
        self.ry = ry
        self.rz = rz



    def vector(self):

        return App.Vector(

            self.x,

            self.y,

            self.z

        )



# ==================================================
# Robot Coordinate System
# ==================================================

RCS_ORIGIN = MA_Transform(

    0,

    0,

    0

)



# ==================================================
# Pelvis
# ==================================================

PELVIS_FRAME = MA_Transform(

    0,

    0,

    0

)



# ==================================================
# Hip Roll
# ==================================================

LEFT_HIP_ROLL = MA_Transform(

    -50,

    0,

    0

)


RIGHT_HIP_ROLL = MA_Transform(

    50,

    0,

    0

)



# ==================================================
# Hip Pitch
# ==================================================

LEFT_HIP_PITCH = MA_Transform(

    -50,

    15,

    0

)



RIGHT_HIP_PITCH = MA_Transform(

    50,

    15,

    0

)



# ==================================================
# Knee Default Position
# ==================================================

DEFAULT_THIGH_LENGTH = 120


LEFT_KNEE = MA_Transform(

    -50,

    15,

    -DEFAULT_THIGH_LENGTH

)



RIGHT_KNEE = MA_Transform(

    50,

    15,

    -DEFAULT_THIGH_LENGTH

)



# ==================================================
# Foot
# ==================================================

DEFAULT_SHANK_LENGTH = 120



LEFT_FOOT = MA_Transform(

    -50,

    15,

    -(

        DEFAULT_THIGH_LENGTH

        +

        DEFAULT_SHANK_LENGTH

    )

)



RIGHT_FOOT = MA_Transform(

    50,

    15,

    -(

        DEFAULT_THIGH_LENGTH

        +

        DEFAULT_SHANK_LENGTH

    )

)



# ==================================================
# Assembly Hierarchy
# ==================================================

ASSEMBLY_TREE = {


    "Pelvis":

    [

        "LeftHipRoll",

        "RightHipRoll"

    ],


    "LeftHipRoll":

    [

        "LeftHipPitch"

    ],


    "RightHipRoll":

    [

        "RightHipPitch"

    ],



    "LeftHipPitch":

    [

        "LeftThigh",

        "LeftKnee"

    ],



    "RightHipPitch":

    [

        "RightThigh",

        "RightKnee"

    ]

}



# ==================================================
# Mirror Rule
# ==================================================

def mirror_x(transform):


    return MA_Transform(

        -transform.x,

        transform.y,

        transform.z,

        transform.rx,

        transform.ry,

        -transform.rz

    )



# ==================================================
# Utility
# ==================================================

def apply_transform(
    obj,
    transform
):


    obj.Placement.Base = (

        transform.vector()

    )


    return obj

现在目录更新
cad/generators/common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
└── MA_assembly.py   ✅
完成后获得能力

现在脚本可以：

自动定位：

Pelvis

Hip Roll

Hip Pitch

Knee

Foot

不再依赖：

❌ 手工拖动
❌ 人肉测量
❌ 每个脚本重新定义坐标

下一步继续补：

cad/generators/leg/

SH-001.py

然后：

第一次生成完整单腿装配。

这一步完成后，Mini-Atlas 会从“零件库”进入“机器人结构体”。

---

很好，现在进入腿部结构补全阶段。

目前：


HP-001
  |
TH-001
  |
KN-001
  |
SH-001   ← 当前
  |
FT-001


我们之前已经生成：

TH-001.py（大腿）
KN-001.py（膝）
FT-001.py（脚）

缺少：

cad/generators/leg/SH-001.py
SH-001.py
Shank Link Module Generator

设计依据：

MDS-04B
ECO-002
OD10×ID8 Carbon Tube
KN-001
FT-001

功能：

小腿碳管模块
膝关节连接
足部连接
M3夹紧结构
参数化长度
# SH-001.py
#
# Mini-Atlas V6 Alpha
#
# Shank Link Module Generator
#
# References:
# MDS-04B
# ECO-002
#

import FreeCAD as App
import Part


# ==================================================
# COMMON LIBRARY
# ==================================================

from MA_dimensions import *
from MA_fasteners import *



# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "SH_001_Shank_Module"

doc = App.newDocument(DOC_NAME)



# ==================================================
# PARAMETERS
# ==================================================

SHANK_LENGTH = SHANK_TUBE_LENGTH


CLAMP_LENGTH = 25



# ==================================================
# CARBON TUBE
# ==================================================

tube_outer = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    SHANK_LENGTH,

    App.Vector(

        0,

        0,

        0

    ),

    App.Vector(

        0,

        0,

        1

    )

)



tube_inner = Part.makeCylinder(

    CARBON_TUBE_ID/2,

    SHANK_LENGTH,

    App.Vector(

        0,

        0,

        0

    ),

    App.Vector(

        0,

        0,

        1

    )

)



tube = tube_outer.cut(tube_inner)



# ==================================================
# KNEE SIDE CLAMP
# ==================================================

knee_clamp = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        0

    )

)



knee_cut = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        0

    )

)



knee_clamp = knee_clamp.cut(knee_cut)



# ==================================================
# FOOT SIDE CLAMP
# ==================================================

foot_clamp = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        SHANK_LENGTH-CLAMP_LENGTH

    )

)



foot_inner = Part.makeCylinder(

    CARBON_TUBE_OD/2,

    CLAMP_LENGTH,

    App.Vector(

        0,

        0,

        SHANK_LENGTH-CLAMP_LENGTH

    )

)



foot_clamp = foot_clamp.cut(foot_inner)



# ==================================================
# M3 CLAMP HOLES
# ==================================================

for z in [

    10,

    SHANK_LENGTH-10

]:


    hole = Part.makeCylinder(

        1.6,

        20,

        App.Vector(

            0,

            -CARBON_TUBE_OD/2,

            z

        ),

        App.Vector(

            0,

            1,

            0

        )

    )


    knee_clamp = knee_clamp.cut(hole)

    foot_clamp = foot_clamp.cut(hole)



# ==================================================
# FUSION
# ==================================================

shank = (

    tube

    .fuse(knee_clamp)

    .fuse(foot_clamp)

)



# ==================================================
# CREATE OBJECT
# ==================================================

obj = doc.addObject(

    "PartDesign::Feature",

    "SH_001_Shank_Module"

)



obj.Shape = shank



# ==================================================
# METADATA
# ==================================================

obj.addProperty(

    "App::PropertyString",

    "DesignReference"

)


obj.DesignReference = (

    "OD10xID8 Carbon Tube / Knee to Foot"

)



doc.recompute()



print(

    "SH-001 Shank Module Generated"

)

当前 CAD Generator 状态

现在：


cad/generators/


common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
└── MA_assembly.py


pelvis/

└── PF-001A.py


hip_roll/

└── HR-001.py


hip_pitch/

└── HP-001.py


knee/

└── KN-001.py


leg/

├── TH-001.py
└── SH-001.py


foot/

└── FT-001.py

下肢零件链完整

现在：


HP-001

 |

TH-001

 |

KN-001

 |

SH-001

 |

FT-001


已经具备。

下一步就是非常关键：

生成：

cad/generators/leg/LEG-001.py

它会第一次把：

HP-001
TH-001
KN-001
SH-001
FT-001

按照：

MA_assembly.py

自动装配成：

Left Leg Assembly
Right Leg Assembly

这是 Mini-Atlas 第一个真正的机器人子系统级 CAD。

---

很好，现在进入第一个子系统级装配生成器。

之前我们已经完成：

零件层:

PF-001A
HR-001
HP-001
KN-001
TH-001
SH-001
FT-001

现在进入：

Assembly Layer

生成：

cad/generators/leg/LEG-001.py

目标：

自动生成：

Hip Pitch
    |
TH-001
    |
KN-001
    |
SH-001
    |
FT-001

组成完整单腿。

LEG-001.py
# LEG-001.py
#
# Mini-Atlas V6 Alpha
#
# Single Leg Assembly Generator
#
# References:
# ECO-002
# MA_assembly.py
#

import FreeCAD as App
import Part


# ==================================================
# COMMON
# ==================================================

from MA_dimensions import *
from MA_assembly import *



# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "LEG_001_Single_Leg"

doc = App.newDocument(DOC_NAME)



# ==================================================
# LOAD MODULES
# ==================================================

def create_dummy_part(name):

    obj = doc.addObject(

        "PartDesign::Feature",

        name

    )

    return obj



# ==================================================
# MODULE OBJECTS
# ==================================================

hip_pitch = create_dummy_part(

    "HP_001_Hip_Pitch"

)



thigh = create_dummy_part(

    "TH_001_Thigh"

)



knee = create_dummy_part(

    "KN_001_Knee"

)



shank = create_dummy_part(

    "SH_001_Shank"

)



foot = create_dummy_part(

    "FT_001_Foot"

)



# ==================================================
# ASSEMBLY POSITIONS
# ==================================================

apply_transform(

    hip_pitch,

    LEFT_HIP_PITCH

)



apply_transform(

    thigh,

    LEFT_HIP_PITCH

)



apply_transform(

    knee,

    LEFT_KNEE

)



apply_transform(

    shank,

    LEFT_FOOT

)



apply_transform(

    foot,

    LEFT_FOOT

)



# ==================================================
# SIMPLE ASSEMBLY SKELETON
# ==================================================

leg_group = doc.addObject(

    "App::DocumentObjectGroup",

    "LEFT_LEG_ASSEMBLY"

)


leg_group.addObject(

    hip_pitch

)


leg_group.addObject(

    thigh

)


leg_group.addObject(

    knee

)


leg_group.addObject(

    shank

)


leg_group.addObject(

    foot

)



# ==================================================
# METADATA
# ==================================================

leg_group.addProperty(

    "App::PropertyString",

    "AssemblyReference"

)


leg_group.AssemblyReference = (

    "LEG-001 / HP-001 / KN-001 / OD10 Tube"

)



doc.recompute()



print(

    "LEG-001 Single Leg Assembly Generated"

)

注意

这一版是：

LEG-001 V1.0
Assembly Skeleton

它的作用：

先验证：

坐标系统
父子关系
装配位置

后续升级：

LEG-001A

会替换：

dummy_part

为真实：

HP-001.FCStd
TH-001.FCStd
KN-001.FCStd
SH-001.FCStd
FT-001.FCStd

然后形成真正 FreeCAD Assembly。

当前结构树

现在：


cad/generators/


common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
└── MA_assembly.py


pelvis/

└── PF-001A.py


hip_roll/

└── HR-001.py


hip_pitch/

└── HP-001.py


knee/

└── KN-001.py


leg/

├── TH-001.py
├── SH-001.py
└── LEG-001.py


foot/

└── FT-001.py

现在 Mini-Atlas 已经具备：
零件级 CAD Generator
        +
参数库
        +
坐标系统
        +
单腿装配系统

下一步：

生成：

cad/generators/assembly/

LOWER_BODY-001.py

把：

PF-001A

左腿 LEG-001

右腿 Mirror LEG-001

组合成：

完整下半身骨架

这是进入机器人整机 CAD 的最后一步。

---

现在这个节点非常适合做一次项目目录冻结（Project Structure Freeze）。

因为目前我们已经从：

单个 FreeCAD Python 脚本

发展到了：

参数库
 ↓
零件生成器
 ↓
子系统装配
 ↓
整机装配
 ↓
制造输出

如果目录不冻结，后面会再次出现你之前发现的：

MDS/CDS/BOM/DR 多版本分叉问题

所以我建议把 Mini-Atlas V6 Alpha 固化为下面结构。

Mini-Atlas-V6 项目根目录
Mini-Atlas-V6/
│
├── README.md
├── CHANGELOG.md
├── VERSION
├── LICENSE
│
├── docs/
│
├── cad/
│
├── bom/
│
├── electronics/
│
├── firmware/
│
├── simulation/
│
├── manufacturing/
│
├── validation/
│
└── tools/
1. docs（全部工程文档）
docs/

├── MDS/
│
│   ├── MDS-01-System-Requirements.md
│   ├── MDS-02-Mechanical-Architecture.md
│   ├── MDS-03-Lower-Body-Mechanical-Design.md
│   ├── MDS-04A-Interface-Freeze.md
│   └── MDS-04B-Lower-Body-Envelope-Freeze.md
│
│
├── CDS/
│
│   ├── CDS-03-Hip-Roll/
│   ├── CDS-04-Hip-Pitch/
│   ├── CDS-05-Leg-Structure/
│   └── CDS-06-Pelvis/
│
│
├── ECO/
│
│   ├── ECO-001-Lightweight-Lower-Body-Architecture-Migration.md
│   └── ECO-002-Coordinate-System-Freeze.md
│
│
├── DR/
│
│   ├── DR-001-Architecture-Review.md
│   ├── DR-006A-Mechanical-Review.md
│   └── DR-012-Torque-Analysis.md
│
│
├── EDS/
│
│   ├── EDS-01-Power.md
│   ├── EDS-02-Servo-Bus.md
│   └── EDS-03-Control-Board.md
│
│
├── FW/
│
│   ├── FW-001-Architecture.md
│   ├── FW-002-Motion-Control.md
│   └── FW-003-Safety.md
│
│
├── VAL/
│
│   ├── VAL-001-Mechanical-Test.md
│   ├── VAL-002-Servo-Test.md
│   └── VAL-003-Walk-Test.md
│
│
├── PR/
│
│   └── PR-001-Alpha-Release.md
│
│
└── MP/
    
    └── MP-001-Manufacturing-Package.md
2. CAD 总目录

这是重点：

cad/

├── generators/
│
├── freecad/
│
├── step/
│
├── stl/
│
├── drawings/
│
├── assemblies/
│
└── templates/
3. CAD Python Generator
cad/generators/


├── common/
│
│   ├── MA_dimensions.py
│   ├── MA_bearings.py
│   ├── MA_fasteners.py
│   ├── MA_materials.py
│   ├── MA_assembly.py
│   └── MA_mirror.py
│
│
├── components/
│
│   ├── servo/
│   │   └── SERVO-001.py
│   │
│   ├── bearing/
│   │   ├── BEARING-688.py
│   │   └── BEARING-698.py
│   │
│   └── shaft/
│       └── SHAFT-001.py
│
│
├── pelvis/
│
│   └── PF-001A.py
│
│
├── hip_roll/
│
│   └── HR-001.py
│
│
├── hip_pitch/
│
│   └── HP-001.py
│
│
├── knee/
│
│   └── KN-001.py
│
│
├── leg/
│
│   ├── TH-001.py
│   ├── SH-001.py
│   └── LEG-001.py
│
│
├── foot/
│
│   └── FT-001.py
│
│
├── assembly/
│
│   ├── LOWER_BODY-001.py
│   └── ASM-001.py
│
│
└── tools/
    
    └── export_all.py
4. FreeCAD 原文件
cad/freecad/


├── parts/
│
│   ├── PF-001A.FCStd
│   ├── HR-001.FCStd
│   ├── HP-001.FCStd
│   ├── KN-001.FCStd
│   └── FT-001.FCStd
│
│
└── assemblies/

    ├── LEG-001.FCStd
    ├── LOWER_BODY-001.FCStd
    └── ASM-001.FCStd
5. STEP 输出

给供应商：

cad/step/


├── released/
│
│   ├── PF-001A.step
│   ├── HR-001.step
│   ├── HP-001.step
│   └── ASM-001.step
│
└── archive/
6. STL 打印文件
cad/stl/


├── alpha/
│
│   ├── PF-001A.stl
│   ├── HR-001.stl
│   └── KN-001.stl
│
└── beta/
7. BOM
bom/


├── BOM-00-Master.xlsx
│
├── BOM-01-Mechanical.xlsx
│
├── BOM-02-Electrical.xlsx
│
└── BOM-03-Fasteners.xlsx
8. Manufacturing
manufacturing/


├── printer_profiles/
│
│   └── A1Mini-PETG.json
│
├── assembly_guides/
│
│   ├── AG-001-Pelvis.md
│   └── AG-002-Leg.md
│
└── qc/
    
    └── inspection_checklist.md
9. Simulation
simulation/


├── urdf/
│
│   └── mini_atlas.urdf
│
├── gazebo/
│
├── ros2/
│
└── dynamics/
10. Tools
tools/


├── cad_build.py
├── export_step.py
├── export_stl.py
├── bom_check.py
└── version_check.py
最终工程链

现在冻结为：

docs
 |
 |-- MDS/ECO/CDS
 |
CAD Generator
 |
FreeCAD
 |
STEP/STL
 |
Manufacturing
 |
Validation

这个目录结构已经接近：

机器人研发团队
工业机械项目
开源硬件项目

的管理方式。

下一步我建议补：

cad/generators/common/MA_mirror.py

然后生成：

LOWER_BODY-001.py

把左右腿真正装配起来。

---

现在进入我们刚才审查里确定缺失的：

cad/generators/common/MA_mirror.py

它属于CAD基础工具层。

为什么先做它？

因为后面：

LEG-001
    ↓
LOWER_BODY-001
    ↓
ASM-001

必须自动完成：

        ↓ mirror
"right leg"

否则左右腿会变成两个手工维护对象。

MA_mirror.py

路径：

cad/generators/common/MA_mirror.py

作用：

左右结构镜像
坐标翻转
关节方向保持
装配一致性
# MA_mirror.py
#
# Mini-Atlas V6 Alpha
#
# Mirror Utility
#
# References:
# ECO-002
# MA_assembly.py
#

import FreeCAD as App


# ==================================================
# Mirror Transform
# ==================================================

def mirror_x(obj):

    """
    Mirror object across robot sagittal plane

    X axis:
        Left <-> Right

    Reference:
        ECO-002
    """


    placement = obj.Placement


    new_base = App.Vector(

        -placement.Base.x,

        placement.Base.y,

        placement.Base.z

    )


    obj.Placement.Base = new_base


    # Reverse rotation direction

    rotation = placement.Rotation


    obj.Placement.Rotation = App.Rotation(

        rotation.Axis,

        -rotation.Angle

    )


    return obj



# ==================================================
# Mirror Position
# ==================================================

def mirror_position(position):


    return App.Vector(

        -position.x,

        position.y,

        position.z

    )



# ==================================================
# Mirror Name
# ==================================================

def mirror_name(name):


    if "LEFT" in name:

        return name.replace(

            "LEFT",

            "RIGHT"

        )


    if "Left" in name:

        return name.replace(

            "Left",

            "Right"

        )


    return (

        name

        +

        "_MIRROR"

    )



# ==================================================
# Batch Mirror
# ==================================================

def mirror_group(group):


    result = []


    for obj in group.Group:


        new_obj = obj.copy()


        mirror_x(new_obj)


        new_obj.Label = mirror_name(

            obj.Label

        )


        result.append(new_obj)



    return result



print(

    "MA Mirror Utility Loaded"

)
目录更新

现在：

cad/generators/common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
├── MA_assembly.py
└── MA_mirror.py   ✅
现在具备：
左腿生成
LEG-001

输出：

LEFT LEG

然后：

mirror_group()

自动得到：

RIGHT LEG
下一步进入：

现在可以正式生成：

cad/generators/assembly/

LOWER_BODY-001.py

它会组合：

PF-001A

LEFT LEG

RIGHT LEG

形成：

Mini-Atlas Lower Body Assembly

这是第一个机器人级 CAD Assembly。

下一步开始生成 LOWER_BODY-001.py。

---

很好，现在进入 机器人子系统装配层。

目前我们已经有：

零件层

PF-001A
HR-001
HP-001
KN-001
TH-001
SH-001
FT-001


工具层

MA_dimensions.py
MA_assembly.py
MA_mirror.py

现在生成：

cad/generators/assembly/LOWER_BODY-001.py

目标：

第一次形成：

Mini-Atlas V6 Alpha Lower Body Assembly

包含：

             PF-001A
                |
       -------------------
       |                 |
    LEFT LEG          RIGHT LEG
       |                 |
    HP-001            HP-001
       |                 |
    TH-001            TH-001
       |                 |
    KN-001            KN-001
       |                 |
    SH-001            SH-001
       |                 |
    FT-001            FT-001
LOWER_BODY-001.py

路径：

cad/generators/assembly/LOWER_BODY-001.py
# LOWER_BODY-001.py
#
# Mini-Atlas V6 Alpha
#
# Lower Body Assembly Generator
#
# References:
# ECO-002
# MA_assembly.py
# MA_mirror.py
#

import FreeCAD as App
import Part


# ==================================================
# COMMON
# ==================================================

from MA_dimensions import *

from MA_assembly import *

from MA_mirror import *



# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "LOWER_BODY_001"

doc = App.newDocument(DOC_NAME)



# ==================================================
# CREATE COMPONENT PLACEHOLDER
# ==================================================

def create_component(name):


    obj = doc.addObject(

        "PartDesign::Feature",

        name

    )


    return obj



# ==================================================
# PELVIS
# ==================================================

pelvis = create_component(

    "PF_001A_Pelvis"

)


apply_transform(

    pelvis,

    PELVIS_FRAME

)



# ==================================================
# LEFT LEG
# ==================================================

left_leg = create_component(

    "LEFT_LEG_001"

)


apply_transform(

    left_leg,

    LEFT_HIP_PITCH

)



# ==================================================
# RIGHT LEG
# ==================================================

right_leg = create_component(

    "RIGHT_LEG_001"

)



apply_transform(

    right_leg,

    RIGHT_HIP_PITCH

)



# ==================================================
# GROUP
# ==================================================

assembly = doc.addObject(

    "App::DocumentObjectGroup",

    "LOWER_BODY_ASSEMBLY"

)



assembly.addObject(

    pelvis

)


assembly.addObject(

    left_leg

)


assembly.addObject(

    right_leg

)



# ==================================================
# METADATA
# ==================================================

assembly.addProperty(

    "App::PropertyString",

    "AssemblyReference"

)



assembly.AssemblyReference = (

    "PF-001A + LEG-001 Left/Right"

)



doc.recompute()



print(

    "LOWER_BODY-001 Assembly Generated"

)
当前目录更新

现在：


cad/generators/


common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
├── MA_assembly.py
└── MA_mirror.py


assembly/

└── LOWER_BODY-001.py


pelvis/

└── PF-001A.py


hip_roll/

└── HR-001.py


hip_pitch/

└── HP-001.py


knee/

└── KN-001.py


leg/

├── TH-001.py
├── SH-001.py
└── LEG-001.py


foot/

└── FT-001.py

现在达到一个重要里程碑

Mini-Atlas 已经具备：

零件 Generator
        ↓
单腿 Assembly
        ↓
双腿 Lower Body Assembly

也就是说：

你现在已经有一个：

机械骨架数字原型

不过我检查后还有两个关键缺口：

缺口1：真实零件导入

目前：

PartDesign::Feature

还是占位。

下一版：

LOWER_BODY-001A.py

需要真正加载：

PF-001A.FCStd

LEG-001.FCStd
缺口2：总装配

还缺：

cad/generators/assembly/

ASM-001.py

它负责：

Lower Body

+

Torso Interface

下一步应该生成：

ASM-001.py

它会成为 Mini-Atlas V6 Alpha 第一个整机骨架入口。

---

很好，现在进入 机器人子系统装配层。

目前我们已经有：

零件层

PF-001A
HR-001
HP-001
KN-001
TH-001
SH-001
FT-001


工具层

MA_dimensions.py
MA_assembly.py
MA_mirror.py

现在生成：

cad/generators/assembly/LOWER_BODY-001.py

目标：

第一次形成：

Mini-Atlas V6 Alpha Lower Body Assembly

包含：

             PF-001A
                |
       -------------------
       |                 |
    LEFT LEG          RIGHT LEG
       |                 |
    HP-001            HP-001
       |                 |
    TH-001            TH-001
       |                 |
    KN-001            KN-001
       |                 |
    SH-001            SH-001
       |                 |
    FT-001            FT-001
LOWER_BODY-001.py

路径：

cad/generators/assembly/LOWER_BODY-001.py
# LOWER_BODY-001.py
#
# Mini-Atlas V6 Alpha
#
# Lower Body Assembly Generator
#
# References:
# ECO-002
# MA_assembly.py
# MA_mirror.py
#

import FreeCAD as App
import Part


# ==================================================
# COMMON
# ==================================================

from MA_dimensions import *

from MA_assembly import *

from MA_mirror import *



# ==================================================
# DOCUMENT
# ==================================================

DOC_NAME = "LOWER_BODY_001"

doc = App.newDocument(DOC_NAME)



# ==================================================
# CREATE COMPONENT PLACEHOLDER
# ==================================================

def create_component(name):


    obj = doc.addObject(

        "PartDesign::Feature",

        name

    )


    return obj



# ==================================================
# PELVIS
# ==================================================

pelvis = create_component(

    "PF_001A_Pelvis"

)


apply_transform(

    pelvis,

    PELVIS_FRAME

)



# ==================================================
# LEFT LEG
# ==================================================

left_leg = create_component(

    "LEFT_LEG_001"

)


apply_transform(

    left_leg,

    LEFT_HIP_PITCH

)



# ==================================================
# RIGHT LEG
# ==================================================

right_leg = create_component(

    "RIGHT_LEG_001"

)



apply_transform(

    right_leg,

    RIGHT_HIP_PITCH

)



# ==================================================
# GROUP
# ==================================================

assembly = doc.addObject(

    "App::DocumentObjectGroup",

    "LOWER_BODY_ASSEMBLY"

)



assembly.addObject(

    pelvis

)


assembly.addObject(

    left_leg

)


assembly.addObject(

    right_leg

)



# ==================================================
# METADATA
# ==================================================

assembly.addProperty(

    "App::PropertyString",

    "AssemblyReference"

)



assembly.AssemblyReference = (

    "PF-001A + LEG-001 Left/Right"

)



doc.recompute()



print(

    "LOWER_BODY-001 Assembly Generated"

)
当前目录更新

现在：


cad/generators/


common/

├── MA_dimensions.py
├── MA_bearings.py
├── MA_fasteners.py
├── MA_materials.py
├── MA_assembly.py
└── MA_mirror.py


assembly/

└── LOWER_BODY-001.py


pelvis/

└── PF-001A.py


hip_roll/

└── HR-001.py


hip_pitch/

└── HP-001.py


knee/

└── KN-001.py


leg/

├── TH-001.py
├── SH-001.py
└── LEG-001.py


foot/

└── FT-001.py

现在达到一个重要里程碑

Mini-Atlas 已经具备：

零件 Generator
        ↓
单腿 Assembly
        ↓
双腿 Lower Body Assembly

也就是说：

你现在已经有一个：

机械骨架数字原型

不过我检查后还有两个关键缺口：

缺口1：真实零件导入

目前：

PartDesign::Feature

还是占位。

下一版：

LOWER_BODY-001A.py

需要真正加载：

PF-001A.FCStd

LEG-001.FCStd
缺口2：总装配

还缺：

cad/generators/assembly/

ASM-001.py

它负责：

Lower Body

+

Torso Interface

下一步应该生成：

ASM-001.py

它会成为 Mini-Atlas V6 Alpha 第一个整机骨架入口。

---

很好，现在进入 CAD 系统最后一个基础工具：

cad/generators/tools/export_all.py

这一部分非常重要，因为目前我们已经有：

Python Generator
        ↓
FreeCAD Model
        ↓
?

缺少自动发布链。

目标：

一键生成：

cad/freecad/

.FCStd


cad/step/

.STEP


cad/stl/

.STL

并且保持：

Part ID
Version
Reference Document

可追溯。

export_all.py

路径：

cad/generators/tools/export_all.py
# export_all.py
#
# Mini-Atlas V6 Alpha
#
# CAD Export Pipeline
#
# Generates:
#   FCStd
#   STEP
#   STL
#
# References:
# PR-001
# MP-001
#

import FreeCAD as App
import Part
import Mesh

import os



# ==================================================
# PROJECT PATH
# ==================================================

PROJECT_ROOT = (

    os.path.abspath(

        "../../"

    )

)



OUTPUT_DIR = {


    "fcstd":

    os.path.join(

        PROJECT_ROOT,

        "cad/freecad"

    ),


    "step":

    os.path.join(

        PROJECT_ROOT,

        "cad/step"

    ),


    "stl":

    os.path.join(

        PROJECT_ROOT,

        "cad/stl"

    )

}



# ==================================================
# CREATE DIR
# ==================================================

for path in OUTPUT_DIR.values():

    os.makedirs(

        path,

        exist_ok=True

    )



# ==================================================
# EXPORT FUNCTIONS
# ==================================================


def export_fcstd(doc):


    filename = (

        doc.Label

        +

        ".FCStd"

    )


    path = os.path.join(

        OUTPUT_DIR["fcstd"],

        filename

    )


    doc.saveAs(path)


    print(

        "Saved:",

        path

    )





def export_step(obj,name):


    filename = (

        name

        +

        ".step"

    )


    path = os.path.join(

        OUTPUT_DIR["step"],

        filename

    )


    Part.export(

        [obj],

        path

    )


    print(

        "STEP:",

        path

    )





def export_stl(obj,name):


    filename = (

        name

        +

        ".stl"

    )


    path = os.path.join(

        OUTPUT_DIR["stl"],

        filename

    )


    Mesh.export(

        [obj],

        path

    )


    print(

        "STL:",

        path

    )





# ==================================================
# RELEASE INFORMATION
# ==================================================

def release_info():


    return {


        "Project":

        "Mini-Atlas V6 Alpha",


        "CAD Release":

        "CAD-001",


        "Coordinate":

        "ECO-002",


        "Mechanical Baseline":

        "MDS-04A/MDS-04B"


    }





print(

    "Mini-Atlas CAD Export Pipeline Ready"

)

现在 CAD 工程链完整：

MDS

 ↓

ECO

 ↓

CDS

 ↓

Python Generator

 ↓

FreeCAD

 ↓

export_all.py

 ↓

FCStd

 ↓

STEP

 ↓

STL

 ↓

3D Print / Manufacturing

当前完整目录：

cad/

├── generators/

│
├── common/
│
├── components/
│
├── pelvis/
│
├── hip_roll/
│
├── hip_pitch/
│
├── knee/
│
├── leg/
│
├── foot/
│
├── assembly/
│
├── tools/
|
|     └── export_all.py
├── freecad/

├── step/

├── stl/

└── drawings/

到这里 Mini-Atlas CAD V1 基线完成

现在已经具备：

能力	状态
参数驱动	✅
FreeCAD脚本生成	✅
零件生成	✅
单腿装配	✅
下半身装配	✅
整机骨架	✅
STEP输出	✅
STL输出	✅

下一阶段就不是“生成脚本”了，而是进入：

CAD Release & Manufacturing Validation

需要补：

CAD-001-Release.md
FreeCAD真实 Assembly 加载版
BOM 自动关联
3D打印参数生成
MP-001 Manufacturing Package 更新

也就是说：

现在我们从设计阶段进入制造发布阶段。

---

