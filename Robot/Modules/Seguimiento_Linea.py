from picarx import Picarx
from time import sleep

class Seguimiento_Linea:
    def __init__(self):
        self.px = Picarx()
        self.px.set_line_reference([1400, 1400, 1400])
        self.power = 4
        self.offset = 10
        self.current_angle = 0
        self.last_state = "stop"

    def get_status(self, val_list, umbral=500):
        state = [1 if val < umbral else 0 for val in val_list]
        if state == [0, 0, 0]:
            return 'lost'
        elif state == [1, 1, 0]:
            return 'slight_right'
        elif state == [0, 1, 1]:
            return 'slight_left'
        elif state[1] == 1:
            return 'forward'
        elif state[0] == 1:
            return 'left'
        elif state[2] == 1:
            return 'right'
        return 'unknown'

    def smooth_turn(self, target, step=2, delay=0.01):
        while abs(self.current_angle - target) > step:
            if self.current_angle < target:
                self.current_angle += step
            else:
                self.current_angle -= step
            self.px.set_dir_servo_angle(self.current_angle)
            sleep(delay)
        self.px.set_dir_servo_angle(target)
        self.current_angle = target

    def outHandle(self):
        self.px.stop()
        sleep(0.1)
        search_angles = [-30, -15, 0, 15, 30] if self.last_state == "right" else [30, 15, 0, -15, -30]

        for angle in search_angles:
            self.smooth_turn(angle)
            self.px.backward(3)
            sleep(0.1)
            gm_val_list = self.px.get_grayscale_data()
            gm_state = self.get_status(gm_val_list)
            if gm_state != 'lost':
                break

        self.px.stop()
        self.smooth_turn(0)




    def ejecutar(self):
        try:
            while True:
                gm_val_list = self.px.get_grayscale_data()
                gm_state = self.get_status(gm_val_list)

                print(f"Sensores: {gm_val_list} | Estado: {gm_state} | Último: {self.last_state}")

                if gm_state != self.last_state:
                    if gm_state == 'forward':
                        self.smooth_turn(0)
                        self.px.forward(self.power)
                    elif gm_state == 'slight_left':
                        self.smooth_turn(self.offset // 2)
                        self.px.forward(self.power)
                    elif gm_state == 'slight_right':
                        self.smooth_turn(-self.offset // 2)
                        self.px.forward(self.power)
                    elif gm_state == 'left':
                        self.smooth_turn(self.offset)
                        self.px.forward(self.power)
                    elif gm_state == 'right':
                        self.smooth_turn(-self.offset)
                        self.px.forward(self.power)
                    elif gm_state == 'lost':
                        self.outHandle()
                    else:
                        self.px.stop()
                        self.smooth_turn(0)
                    self.last_state = gm_state

                sleep(0.1)

        except KeyboardInterrupt:
            print("Interrupción manual detectada.")
        finally:
            self.px.stop()
            self.px.set_dir_servo_angle(0)
            print("Robot detenido y servo centrado")
