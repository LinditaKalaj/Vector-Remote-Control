class MoveVector:
    def __init__(self, robot):
        self.vector = robot
        self.pressed = {}
        self.move_speed = 100
        self.head_speed = 1.0
        self.pressed["w"] = False
        self.pressed["s"] = False
        self.pressed["a"] = False
        self.pressed["d"] = False

    def main_move(self):
        if self.pressed["w"] and self.pressed["a"]:
            self.vector.motors.set_wheel_motors(self.move_speed//2, self.move_speed)
        elif self.pressed["w"] and self.pressed["d"]:
            self.vector.motors.set_wheel_motors(self.move_speed, self.move_speed//2)
        elif self.pressed["s"] and self.pressed["a"]:
            self.vector.motors.set_wheel_motors(-(self.move_speed//2), -self.move_speed)
        elif self.pressed["s"] and self.pressed["d"]:
            self.vector.motors.set_wheel_motors(-self.move_speed, -(self.move_speed//2))
        elif self.pressed["w"]:
            self.vector.motors.set_wheel_motors(self.move_speed, self.move_speed)
        elif self.pressed["a"]:
            self.vector.motors.set_wheel_motors(-self.move_speed, self.move_speed)
        elif self.pressed["d"]:
            self.vector.motors.set_wheel_motors(self.move_speed, -self.move_speed)
        elif self.pressed["s"]:
            self.vector.motors.set_wheel_motors(-self.move_speed, -self.move_speed)

    def key_pressed(self, event):
        self.pressed[event.keysym] = True

    def key_released(self, event):
        self.pressed[event.char] = False
        if not(self.pressed["w"] or self.pressed["s"] or self.pressed["a"] or self.pressed["d"]):
            self.vector.motors.set_wheel_motors(0, 0)

    def move_head(self, direction):
        self.vector.motors.set_head_motor(direction * self.head_speed)

    def stop_head(self, x):
        self.vector.motors.set_head_motor(0)

    def move_lift(self, x):
        self.vector.motors.set_lift_motor(5)

    def stop_lift(self):
        self.vector.motors.set_lift_motor(0)
