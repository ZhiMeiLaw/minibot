
// ============================================================
// Mini-Atlas V5 - Hybrid Wheel-Leg Humanoid
// ============================================================

$fn = 64;

// ============================================================
// PARAMETERS
// ============================================================

// Servo
s_len       = 45.2;
s_wid       = 24.7;
s_ht        = 35.0;
s_horn_r    = 12;
s_horn_h    = 3;
s_offset    = 11.5;

// Structure
wall         = 3;
tol          = 0.45;
shaft_d      = 8;

// Robot Geometry
pelvis_w     = 100;
pelvis_d     = 70;
pelvis_h     = 50;

hip_spacing  = 86;

thigh_len    = 100;
calf_len     = 95;

wheel_d      = 100;
wheel_w      = 36;

fork_w       = 50;
fork_h       = 70;

// Pose
j_roll       = 8;
j_pitch      = 12;
j_knee       = -18;

// ============================================================
// SERVO
// ============================================================

module real_servo() {

    color("#424242") {

        translate([0,0,-s_ht/2])
            cube([s_len,s_wid,s_ht], center=true);

        translate([s_len/2 - s_offset,0,1.5])
            cube([s_len,s_wid,3], center=true);
    }

    color("#FFD54F")
        translate([0,0,3])
            cylinder(r=s_horn_r,h=s_horn_h,center=true);
}

module servo_on_axis() {

    translate([-(s_len/2 - s_offset),0,-s_horn_h - 1.5])
        real_servo();
}

// ============================================================
// STRUCTURAL SHAFT
// ============================================================

module shaft(len=40) {

    color("silver")
        rotate([0,90,0])
            cylinder(d=shaft_d,h=len,center=true);
}

// ============================================================
// HIP ROLL FRAME
// ============================================================

module hip_roll_frame() {

    color("#FB8C00")
    difference() {

        union() {

            cube([30,54,54], center=true);

            translate([18,0,0])
                cube([12,54,54], center=true);
        }

        cube([36,26,60], center=true);

        rotate([0,90,0])
            cylinder(d=shaft_d + tol,h=80,center=true);
    }

    shaft(60);
}

// ============================================================
// BOX THIGH
// ============================================================

module box_thigh() {

    color("#C62828")
    difference() {

        hull() {

            cube([34,40,24], center=true);

            translate([0,0,-thigh_len])
                cube([28,34,22], center=true);
        }

        hull() {

            cube([24,30,18], center=true);

            translate([0,0,-thigh_len])
                cube([18,24,16], center=true);
        }
    }
}

// ============================================================
// KNEE JOINT
// ============================================================

module knee_joint() {

    color("#5E35B1") {

        translate([0,18,0])
            cube([50,4,40], center=true);

        translate([0,-18,0])
            cube([50,4,40], center=true);

        cube([12,40,20], center=true);
    }

    shaft(44);
}

// ============================================================
// CALF
// ============================================================

module calf_box() {

    color("#2E7D32")
    difference() {

        hull() {

            cube([24,32,20], center=true);

            translate([0,0,-calf_len])
                cube([20,28,20], center=true);
        }

        hull() {

            cube([16,24,14], center=true);

            translate([0,0,-calf_len])
                cube([12,20,14], center=true);
        }
    }
}

// ============================================================
// WHEEL MODULE (NEW V5 CORE)
// ============================================================

module wheel() {

    color("#212121")
    rotate([90,0,0])
    difference() {

        cylinder(d=wheel_d,h=wheel_w,center=true);

        cylinder(d=wheel_d - 18,h=wheel_w + 2,center=true);
    }
}

module wheel_fork() {

    color("#455A64")
    union() {

        // Left fork arm
        translate([0,18,-fork_h/2])
            cube([8,4,fork_h], center=true);

        // Right fork arm
        translate([0,-18,-fork_h/2])
            cube([8,4,fork_h], center=true);

        // Upper mount
        cube([24,40,8], center=true);

        // Axle shaft
        translate([0,0,-fork_h])
            rotate([0,90,0])
                cylinder(d=8,h=50,center=true);
    }
}

module wheel_motor() {

    color("#616161")
    translate([-18,0,-fork_h + 10])
        rotate([0,90,0])
            cylinder(d=37,h=40,center=true);
}

module wheel_foot_module() {

    // Passive ankle adapter
    color("#78909C")
    difference() {

        cube([30,34,10], center=true);

        cylinder(d=8.5,h=20,center=true);
    }

    // Fork
    translate([0,0,-8])
        wheel_fork();

    // Motor
    translate([0,0,-8])
        wheel_motor();

    // Wheel
    translate([0,0,-fork_h - 8])
        wheel();
}

// ============================================================
// COMPLETE LEG
// ============================================================

module complete_leg_v5() {

    // Hip Roll Servo
    rotate([0,-90,0])
        servo_on_axis();

    rotate([j_roll,0,0]) {

        translate([-6,0,0])
            rotate([0,-90,0])
                hip_roll_frame();

        // Hip Pitch Servo
        translate([-24,0,0]) {

            rotate([90,0,-90])
                servo_on_axis();

            rotate([0,0,j_pitch]) {

                translate([-4,0,0])
                    box_thigh();

                // Knee
                translate([0,0,-thigh_len]) {

                    rotate([0,0,j_knee]) {

                        knee_joint();

                        rotate([90,0,-90])
                            servo_on_axis();

                        // Calf
                        translate([0,0,-16])
                            calf_box();

                        // Wheel Foot Module
                        translate([0,0,-calf_len - 10])
                            wheel_foot_module();
                    }
                }
            }
        }
    }
}

// ============================================================
// PELVIS
// ============================================================

module pelvis() {

    color("#607D8B")
    difference() {

        cube([pelvis_w,pelvis_d,pelvis_h], center=true);

        cube([
            pelvis_w - 14,
            pelvis_d - 14,
            pelvis_h - 8
        ], center=true);

        cube([32,pelvis_d + 2,18], center=true);
    }

    // Top mounting plate
    color("#90A4AE")
    translate([0,0,pelvis_h/2 + 3])
        cube([70,50,6], center=true);
}

// ============================================================
// ASSEMBLY
// ============================================================

pelvis();

// Left Leg
translate([-hip_spacing/2,0,0])
    complete_leg_v5();

// Right Leg
translate([hip_spacing/2,0,0])
    mirror([1,0,0])
        complete_leg_v5();

// ============================================================
// END