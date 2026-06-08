// 🤖 Mini-Atlas V1 - 下肢总成参数化完整装配图 (Full Leg Assembly)
// ====================================================================
$fn = 40; // 渲染圆滑度

// ====== 【核心控制开关：直接在这里修改角度，可以让腿动起来！】 ======
hip_pitch  = -15;  // 髋关节前屈角度 (度) -> 调整看大腿摆动
knee_pitch = 35;   // 膝关节弯曲角度 (度) -> 调整看大腿和小腿嵌套

// ==================== 1. 基础全局参数定义 ====================
pelvis_w = 116; pelvis_h = 74; pelvis_d = 40;
leg_length_thigh = 100; // 大腿长
leg_length_calf  = 90;  // 小腿长

u_inner = 46.5; // 舵机及小腿内侧净宽
wall_t  = 4.5;  // 支架侧壁厚
u_outer = u_inner + 2 * wall_t; // 大腿外宽 (55.5mm)

// ==================== 2. 独立结构件组件库 ====================

// 🧩 部件 A：骨盆核心舱 (灰色)
module pelvis() {
    difference() {
        // 圆角骨盆外壳
        translate([0, pelvis_h/2, pelvis_d/2]) 
            cube([pelvis_w, pelvis_h, pelvis_d], center=true);
        // 底部电池通槽
        translate([0, 17/2 + 5, 16/2]) 
            cube([106, 17, 50], center=true);
        // 左侧髋关节舵机盲槽 (位于 X = -38 处)
        translate([-38, 27 + 32/2, 25/2 - 0.1]) 
            cube([46, 32, 25], center=true);
        // 右侧髋关节舵机盲槽 (位于 X = 38 处)
        translate([38, 27 + 32/2, 25/2 - 0.1]) 
            cube([46, 32, 25], center=true);
    }
}

// 🧩 部件 B：大腿 U 型支撑架 (蓝色)
// 亮点：上下都是开口朝下的 U 型叉，外包络结构
module thigh() {
    difference() {
        // 大腿骨骼毛坯
        hull() {
            rotate([0, 90, 0]) cylinder(r=13, h=u_outer, center=true);
            translate([0, 0, -leg_length_thigh]) rotate([0, 90, 0]) cylinder(r=13, h=u_outer, center=true);
        }
        // 顶部 U 型切口：用来水平夹住骨盆侧壁
        translate([0, 0, 13]) cube([u_inner, 40, 40], center=true);
        // 底部 U 型切口：开口朝下，用来外包包裹住小腿顶部！
        translate([0, 0, -leg_length_thigh - 13]) cube([u_inner, 40, 40], center=true);
        // 中间骨骼拓扑减重槽
        translate([0, 0, -leg_length_thigh/2]) rotate([90, 0, 0])
            hull() {
                translate([0, 20, 0]) cylinder(d=14, h=50, center=true);
                translate([0, -20, 0]) cylinder(d=14, h=50, center=true);
            }
    }
}

// 🧩 部件 C：小腿承重组件 (绿色)
// 亮点：顶部是开口向上的 U 型仓，外壁宽度刚好塞进大腿的下 U 型叉内
module calf() {
    difference() {
        union() {
            // 顶部膝关节旋转头 (外宽为 45.5mm，完美嵌入大腿的 46.5mm 内宽中)
            rotate([0, 90, 0]) cylinder(r=13, h=u_inner - 1, center=true);
            // 向下收拢的骨骼主体
            hull() {
                translate([0, 0, -13]) cube([u_inner - 1, 26, 1], center=true);
                translate([0, 0, -leg_length_calf]) cube([30, 26, 2], center=true);
            }
        }
        // 顶部开口向上的 U 型槽 (用来在内部塞入它自己的膝关节舵机)
        translate([0, 0, 5]) cube([36.5, 32, 20], center=true);
    }
    // 底部固定的脚踝电机转接座 (黑色)
    color("Charcoal") translate([0, 0, -leg_length_calf - 10]) 
        cube([30, 26, 20], center=true);
}


// ==================== 3. 核心物理拓扑装配中心 ====================

// 1️⃣ 放置中心基座：骨盆
color("LightSlateGray") pelvis();

// 2️⃣ 组装左下肢 (面向机器人时的左侧)
translate([-38, 27 + 16, 25/2]) {   // 第一步：将坐标系移动到【左髋关节轴心】
    rotate([hip_pitch, 0, 0]) {     // 第二步：绕着 X 轴水平旋转 (髋关节前屈/后摆)
        
        color("RoyalBlue") thigh();  // 第三步：在此坐标系下渲染大腿
        
        // ──────────────────────────────────────────────────
        translate([0, 0, -leg_length_thigh]) {  // 第四步：顺着大腿骨向下移动到【膝关节轴心】
            rotate([knee_pitch, 0, 0]) {        // 第五步：绕着 X 轴水平旋转 (膝关节屈伸)
                
                color("LimeGreen") calf();     // 第六步：在此坐标系下渲染小腿与脚踝
                
            }
        }
        // ──────────────────────────────────────────────────
    }
}

// 3️⃣ 组装右下肢 (完全对称，镜像共用组件)
translate([38, 27 + 16, 25/2]) {    // 移动到【右髋关节轴心】
    rotate([hip_pitch, 0, 0]) {     // 髋关节同步联动
        color("RoyalBlue") thigh(); 
        
        translate([0, 0, -leg_length_thigh]) {
            rotate([knee_pitch, 0, 0]) { // 膝关节同步联动
                color("LimeGreen") calf();
            }
        }
    }
}