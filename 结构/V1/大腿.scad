// 🤖 Mini-Atlas V1 - Thigh U-Bracket (大腿 U 型支撑架)
$fn = 60; // 圆滑度设定

// === 1. 核心骨架参数 ===
leg_length = 100;    // 髋关节到膝关节的轴心距 (决定腿长)
u_inner_w  = 46.5;   // U 型槽内部净宽 (STS3215长度45.5 + 1mm公差)
wall_t     = 4.5;    // U 型叉的手臂壁厚 (必须足够厚以抗形变)
joint_r    = 13;     // 关节端部的外圆半径

u_outer_w = u_inner_w + 2 * wall_t; // 大腿总宽度计算

// === 2. 硬件公差参数 (极其重要) ===
bearing_d = 13.2;    // F683ZZ 法兰轴承外径 (标称13mm，预留0.2mm打印膨胀公差)
horn_center_d = 6.2; // 舵盘中心轴避让孔
horn_screw_d = 2.2;  // M2 螺丝过孔 (用于拧在金属舵盘上)
horn_screw_dist = 14;// 飞特原装金属舵盘螺丝孔距的对角线距离

// === 3. 基础形体模块 ===
module rounded_joint() {
    rotate([0, 90, 0]) cylinder(r=joint_r, h=u_outer_w, center=true);
}

// === 4. 布尔减法：雕刻大腿 ===
difference() {
    
    // 【第一步：生成实心大腿毛坯 (连桥)】
    hull() {
        translate([0, 0, 0]) rounded_joint();               // 顶部髋关节球
        translate([0, 0, -leg_length]) rounded_joint();     // 底部膝关节球
    }
    
    // 【第二步：掏空上下 U 型槽】
    // 顶部槽 (Hip)
    translate([0, 0, joint_r]) 
        cube([u_inner_w, 40, 40], center=true);
    // 底部槽 (Knee)
    translate([0, 0, -leg_length - joint_r]) 
        cube([u_inner_w, 40, 40], center=true);
        
    // 【第三步：打通硬件安装孔】
    // --- 顶部髋关节孔 ---
    // 左侧：法兰轴承安装孔 (支撑端)
    translate([-u_outer_w/2 - 1, 0, 0]) 
        rotate([0, 90, 0]) cylinder(d=bearing_d, h=wall_t+2);
        
    // 右侧：金属舵盘安装孔阵列 (动力端)
    translate([u_outer_w/2 - wall_t - 1, 0, 0]) 
        rotate([0, 90, 0]) {
            cylinder(d=horn_center_d, h=wall_t+2); // 中心避让孔
            // 4个 M2 螺丝环形阵列
            for(i=[45:90:360]) {
                rotate([0, 0, i]) translate([horn_screw_dist/2, 0, 0]) 
                    cylinder(d=horn_screw_d, h=wall_t+2);
            }
        }
        
    // --- 底部膝关节孔 ---
    translate([0, 0, -leg_length]) {
        // 右侧：法兰轴承安装孔 (支撑端)
        translate([u_outer_w/2 - wall_t - 1, 0, 0]) 
            rotate([0, 90, 0]) cylinder(d=bearing_d, h=wall_t+2);
            
        // 左侧：金属舵盘安装孔阵列 (动力端) - 左右交替防止重心偏载
        translate([-u_outer_w/2 - 1, 0, 0]) 
            rotate([0, 90, 0]) {
                cylinder(d=horn_center_d, h=wall_t+2); 
                for(i=[45:90:360]) {
                    rotate([0, 0, i]) translate([horn_screw_dist/2, 0, 0]) 
                        cylinder(d=horn_screw_d, h=wall_t+2);
                }
            }
    }
    
    // 【第四步：中段装甲拓扑减重槽】
    translate([0, 0, -leg_length/2])
        rotate([90, 0, 0])
        hull() {
            translate([0, leg_length/2 - 28, 0]) cylinder(d=14, h=40, center=true);
            translate([0, -leg_length/2 + 28, 0]) cylinder(d=14, h=40, center=true);
        }
}