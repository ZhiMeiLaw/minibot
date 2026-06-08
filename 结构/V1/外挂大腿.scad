// Mini-Atlas V3.1 - Absolute Symmetrical Layout (Gimbal Architecture)
$fn = 60;

// ==================== 1. CORE PARAMETERS ====================
tol = 0.5; // Mechanical clearance for 3D printing

// Feetech STS3215 Real Physical Dimensions
s_len = 45.2; s_wid = 24.7; s_ht  = 35.0;
s_horn_r = 12.0; s_horn_h = 3.0;
s_offset = 11.5; // Output axis displacement from edge

// Dynamic Test Angles
j_roll  = 10;  
j_pitch = 15;  
j_knee  = -25; 

// ==================== 2. MATERIAL SUB-MODULES ====================

module real_servo() {
    color("#444444") {
        translate([0, 0, -s_ht/2]) cube([s_len, s_wid, s_ht], center=true);
        translate([s_len/2 - s_offset, 0, 1.5]) cube([s_len, s_wid, 3], center=true);
    }
    color("#FFD700") translate([0, 0, 3]) cylinder(r=s_horn_r, h=s_horn_h, center=true);
}

module servo_on_axis() {
    translate([-(s_len/2 - s_offset), 0, -s_horn_h - 1.5]) real_servo();
}

module u_gimbal_yoke() {
    color("#FF9800") difference() {
        translate([0, 0, 12]) cube([s_ht + 14, s_wid + 8, s_len + 10], center=true);
        translate([0, 0, 15]) cube([s_ht + tol, s_wid + tol, s_len + 20], center=true);
        translate([0, 0, -12]) cylinder(r=s_horn_r + tol, h=10, center=true);
        translate([0, 0, 15]) rotate([0, 90, 0]) cylinder(r=10, h=60, center=true);
    }
}

module i_beam_thigh() {
    thigh_len = 90;
    clevis_w  = s_wid + 2*tol + 8; 
    color("#D32F2F") difference() {
        hull() {
            rotate([0, 90, 0]) cylinder(r=16, h=6, center=true);
            translate([0, 0, -thigh_len]) rotate([0, 90, 0]) cylinder(r=14, h=clevis_w, center=true);
        }
        translate([-4, 0, -thigh_len/2 + 5]) rotate([0, 90, 0])
            hull() {
                cylinder(r=8, h=20, center=true);
                translate([-thigh_len + 40, 0, 0]) cylinder(r=6, h=20, center=true);
            }
        translate([12, 0, 0]) cube([20, s_wid+10, 35], center=true);
        translate([0, 0, -thigh_len - 10]) cube([clevis_w - 8, s_len, 40], center=true);
        rotate([0, 90, 0]) cylinder(d=4.2, h=30, center=true); 
    }
}

module lower_calf() {
    calf_len = 80;
    color("#388E3C") difference() {
        union() {
            rotate([0, 90, 0]) cylinder(r=12, h=s_wid + 2*tol, center=true);
            hull() {
                translate([0, 0, -12]) cube([s_wid + 2*tol, 20, 1], center=true);
                translate([0, 0, -calf_len]) cube([22, 18, 2], center=true);
            }
        }
        translate([0, 0, 5]) cube([s_wid, 40, 30], center=true);
    }
    color("#212121") translate([0, 0, -calf_len - 15]) rotate([0, 90, 0]) cylinder(r=22, h=12, center=true);
}

// ==================== 3. MONOLITHIC LEG MODULE ====================
// 封装单侧动力链，基准点处于骨盆左侧的 Roll 轴法兰面
module complete_leg_topology() {
    // 1. Roll 轴固定电机
    rotate([0, -90, 0]) servo_on_axis();
    
    // 2. Roll 轴机械旋转
    rotate([j_roll, 0, 0]) {
        translate([-4, 0, 0]) rotate([0, -90, 0]) u_gimbal_yoke();
        
        // 3. Pitch 轴悬挂电机
        translate([-19, 0, 0]) {
            rotate([90, 0, -90]) servo_on_axis();
            
            // 4. Pitch 轴机械旋转
            rotate([0, 0, j_pitch]) {
                translate([-3, 0, 0]) i_beam_thigh();
                
                // 5. Knee 轴机械旋转
                translate([0, 0, -90]) rotate([0, 0, j_knee]) {
                    lower_calf();
                }
            }
        }
    }
}

// ==================== 4. SYSTEM ASSEMBLY ====================

// Centered Pelvis Chassis
color("#607D8B") difference() {
    cube([50, s_len + 20, s_wid + 15], center=true);
    translate([-25, 0, 0]) rotate([0, -90, 0]) cube([s_wid+tol, s_len+tol, 60], center=true);
    translate([25, 0, 0]) rotate([0, 90, 0]) cube([s_wid+tol, s_len+tol, 60], center=true);
    cube([20, s_len + 22, 15], center=true); // Wire channel
}

// LEFT LEG (Native invocation)
translate([-25 - 4.5, 0, 0]) {
    complete_leg_topology();
}

// RIGHT LEG (Absolute Mathematical Mirror)
// 🚀 核心修正：利用内置 mirror 矩阵直接映射，杜绝手写手性错误
translate([25 + 4.5, 0, 0]) {
    mirror([1, 0, 0]) {
        complete_leg_topology();
    }
}