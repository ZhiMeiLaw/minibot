// 🤖 Mini-Atlas V1 - Calf & Ankle Mount (小腿与脚踝底座)
$fn = 60;

// === 1. 核心参数 ===
calf_length = 90;    // 小腿长度 (膝盖轴心到脚踝结合面)
u_inner_w   = 46.5;  // 配合 STS3215 舵机的 U 型内宽
wall_t      = 4.5;   // 侧壁厚度
joint_r     = 13;    // 膝盖关节外圆半径
u_outer_w   = u_inner_w + 2 * wall_t;

// 脚踝接口参数 (必须足够粗壮)
ankle_w = 30; // 接口宽度
ankle_d = 26; // 接口深度
m3_clear= 3.2; // M3 通孔
m3_insert= 4.2; // M3 热熔螺母孔

// ==========================================
// 🦵 零件 1：小腿主体 (Calf)
// 打印建议：必须侧躺打印 (与大腿一样)，获得最大抗折断强度
// ==========================================
module calf_part() {
    difference() {
        // --- 1. 外形毛坯 ---
        union() {
            // 顶部膝关节球
            translate([0, 0, 0]) rotate([0, 90, 0]) cylinder(r=joint_r, h=u_outer_w, center=true);
            // 梯形收敛过渡到脚踝方形接口
            hull() {
                translate([0, 0, -joint_r]) cube([u_outer_w, joint_r*2, 1], center=true);
                translate([0, 0, -calf_length]) cube([ankle_w, ankle_d, 2], center=true);
            }
        }
        
        // --- 2. 掏空 U 型槽 (容纳膝盖舵机) ---
        translate([0, 0, -joint_r]) 
            cube([u_inner_w, 40, 40], center=true);
            
        // --- 3. 膝关节孔位 (交叉负载布局，动力端在左侧) ---
        // 左侧：金属舵盘安装孔 (动力端)
        translate([-u_outer_w/2 - 1, 0, 0]) rotate([0, 90, 0]) {
            cylinder(d=6.2, h=wall_t+2); // 中心避让
            for(i=[45:90:360]) rotate([0, 0, i]) translate([7, 0, 0]) cylinder(d=2.2, h=wall_t+2);
        }
        // 右侧：法兰轴承安装孔 (支撑端)
        translate([u_outer_w/2 - wall_t - 1, 0, 0]) rotate([0, 90, 0]) 
            cylinder(d=13.2, h=wall_t+2);
            
        // --- 4. 底部脚踝对接孔 (4个 M3 通孔) ---
        translate([0, 0, -calf_length]) {
            translate([8, 8, -5]) cylinder(d=m3_clear, h=20);
            translate([-8, 8, -5]) cylinder(d=m3_clear, h=20);
            translate([8, -8, -5]) cylinder(d=m3_clear, h=20);
            translate([-8, -8, -5]) cylinder(d=m3_clear, h=20);
        }
        
        // --- 5. 肌肉感机甲减重槽 ---
        translate([0, 0, -calf_length/2 - 5]) rotate([90, 0, 0])
            hull() {
                translate([0, 20, 0]) cylinder(d=10, h=40, center=true);
                translate([0, -20, 0]) cylinder(d=8, h=40, center=true);
            }
    }
}

// ==========================================
// 🛞 零件 2：脚踝电机座 (Ankle Mount)
// 打印建议：底部朝下竖直打印，推荐 40% 填充以上
// ==========================================
module ankle_mount() {
    difference() {
        // 主体方块
        translate([0, 0, -10]) cube([ankle_w, ankle_d, 20], center=true);
        
        // 1. 顶部对接孔 (预留给小腿拧下来的 4 个 M3 热熔螺母)
        translate([8, 8, -1]) cylinder(d=m3_insert, h=12);
        translate([-8, 8, -1]) cylinder(d=m3_insert, h=12);
        translate([8, -8, -1]) cylinder(d=m3_insert, h=12);
        translate([-8, -8, -1]) cylinder(d=m3_insert, h=12);
        
        // 2. 侧面 L 型电机支架安装孔 
        // (标准 25mm 支架通常孔距为 17mm 和 10mm，使用 M3 螺丝固定)
        translate([0, -ankle_d/2 - 1, -10]) rotate([-90, 0, 0]) {
            translate([8.5, 5, 0]) cylinder(d=m3_clear, h=15);
            translate([-8.5, 5, 0]) cylinder(d=m3_clear, h=15);
            translate([8.5, -5, 0]) cylinder(d=m3_clear, h=15);
            translate([-8.5, -5, 0]) cylinder(d=m3_clear, h=15);
        }
    }
}

// 渲染视图排版 (拉开距离展示)
calf_part();
translate([0, 40, -calf_length]) ankle_mount();