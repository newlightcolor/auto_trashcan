from machine import Pin,PWM
import utime

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
led = Pin(25, Pin.OUT)

pwm = PWM(Pin(0))
pwm.freq(50)

sensor_adc = machine.ADC(0)

def read_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("dinstance: ",distance,"cm")
    return distance

def servo_value(degree):
    return int((degree * 9.5 / 180 + 2.5) * 65535 / 100)

while True:
    led.toggle()
    if read_distance() <= 10:
        pwm.duty_u16(servo_value(90))
        print("trashcan opened!!!")
        utime.sleep(3)
        pwm.duty_u16(servo_value(0))
    utime.sleep(0.1)
