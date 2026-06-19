// 🤖 Mini-Atlas V1 - Pelvis Core (Armored Edition)
// 渲染精度设置 (越高越平滑，按 F6 渲染时可能稍慢)
$fn = 60; 

// === 1. 核心尺寸参数库 ===
pelvis_w = 116;    // 骨盆总宽度
pelvis_h = 74;     // 骨盆总高度
pelvis_d = 40;     // Z轴深度
wall_r   = 3;      // 整体外壳圆角半径 (防应力集中)

batt_w = 106;      // 电池仓尺寸 (已包含公差)
batt_h = 17;
batt_d = 36;

servo_w = 46;      // STS3215 舵机槽尺寸
servo_h = 32;
servo_d = 25;

// === 2. 紧固件工程公差标准 ===
minsert_d = 4.2;   // M3 铜热熔螺母预留底孔径 (非常关键！)
m3_clear_d = 3.2;  // M3 螺丝顺滑穿透孔径

// === 3. 高级自定义模块：圆角长方体 ===
// 利用 hull() 把四个圆柱体包络成一个带圆角的盒子
module rounded_box(w, h, d, r) {
    translate([r, r, 0])
    hull() {
        translate([0, 0, 0]) cylinder(r=r, h=d);
        translate([w-2*r, 0, 0]) cylinder(r=r, h=d);
        translate([0, h-2*r, 0]) cylinder(r=r, h=d);
        translate([w-2*r, h-2*r, 0]) cylinder(r=r, h=d);
    }
}

// === 4. 主体布尔相减逻辑 ===
difference() {
    
    // 【第一步：生成物理外壳与装甲 (Union 合集)】
    union() {
        // 基础倒角骨盆箱体
        translate([-pelvis_w/2, 0, 0])
            rounded_box(pelvis_w, pelvis_h, pelvis_d, wall_r);
        
        // 🚀 核心更新：背部防悬空装甲 (滑橇防刮条)
        // 突出于表面的半圆柱结构，防止摔倒时肚皮贴地导致轮子悬空
        translate([-pelvis_w/2 + 20, pelvis_h, -3]) 
            rotate([90, 0, 0]) cylinder(r=4, h=pelvis_h);
        translate([pelvis_w/2 - 20, pelvis_h, -3]) 
            rotate([90, 0, 0]) cylinder(r=4, h=pelvis_h);
    }

    // 【第二步：掏空内部机能舱室 (Difference 减法)】
    
    // 1. 电池抽屉
    translate([-batt_w/2, 5, -0.1])
        cube([batt_w, batt_h, batt_d]);
        
    // 2. 左右两侧总线舵机盲槽
    translate([-pelvis_w/2 + 5, 27, -0.1])
        cube([servo_w, servo_h, servo_d]);
    translate([pelvis_w/2 - 5 - servo_w, 27, -0.1])
        cube([servo_w, servo_h, servo_d]);
        
    // 3. 中心神经走线井
    translate([-7, 27, -0.1])
        cube([14, 47.1, 20]);

    // 【第三步：打孔 - M3 紧固件阵列】
    
    // 1. 顶部装配阵列 (4个 M3 热熔螺母孔)
    // 用于向上连接胸腔 (Torso) 或固定转接板，孔径设定为 4.2mm
    translate([-35, pelvis_h+0.1, 8]) rotate([90, 0, 0]) cylinder(d=minsert_d, h=6);
    translate([35, pelvis_h+0.1, 8]) rotate([90, 0, 0]) cylinder(d=minsert_d, h=6);
    translate([-35, pelvis_h+0.1, 32]) rotate([90, 0, 0]) cylinder(d=minsert_d, h=6);
    translate([35, pelvis_h+0.1, 32]) rotate([90, 0, 0]) cylinder(d=minsert_d, h=6);
    
    // 2. 髋关节舵机横向贯穿固定孔 (M3 穿透孔)
    // 用于穿透侧壁死死锁住 STS3215 舵机的安装耳，孔径设定为 3.2mm
    // (这里取舵机安装耳的标准间距做示例)
    // 左侧舵机固定孔
    translate([-pelvis_w/2 - 1, 32, 5]) rotate([0, 90, 0]) cylinder(d=m3_clear_d, h=12);
    translate([-pelvis_w/2 - 1, 54, 5]) rotate([0, 90, 0]) cylinder(d=m3_clear_d, h=12);
    // 右侧舵机固定孔
    translate([pelvis_w/2 - 11, 32, 5]) rotate([0, 90, 0]) cylinder(d=m3_clear_d, h=12);
    translate([pelvis_w/2 - 11, 54, 5]) rotate([0, 90, 0]) cylinder(d=m3_clear_d, h=12);
}