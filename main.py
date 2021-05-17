from dynamikontrol import Module, Timer
import time

module = Module()
module.motor.angle(-85)

def feed():
    module.motor.angle(0)
    time.sleep(0.5)
    module.motor.angle(-85)

timer = Timer()
timer.callback_after(func=feed, interval=10)
