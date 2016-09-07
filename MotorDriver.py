# Please refer to the licensing terms stated in the README.md section of
# https://github.com/hummingworksllc/motordriver

import RPi.GPIO as GPIO, Tkinter

L1 = 36
L2 = 35
R1 = 33
R2 = 32

def init():
    global p, q, a, b
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(L1, GPIO.OUT)
    p = GPIO.PWM(L1, 20)
    p.start(0)

    GPIO.setup(L2, GPIO.OUT)
    q = GPIO.PWM(L2, 20)
    q.start(0)

    GPIO.setup(R1, GPIO.OUT)
    a = GPIO.PWM(R1, 20)
    a.start(0)

    GPIO.setup(R2, GPIO.OUT)
    b = GPIO.PWM(R2, 20)
    b.start(0)

def cleanup():
    stop()
    GPIO.cleanup()

def stop():
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)

def forward(speed):
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)

def reverse(speed):
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(speed)
    q.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)

def spinLeft(speed):
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    q.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)

def spinRight(speed):
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(speed)
    p.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)

root = Tkinter.Tk()

init()

spd = Tkinter.IntVar()
spd.set(0)

dr = Tkinter.IntVar()
dr.set(1)

def change_spd(s):
    if(dr.get() == 0):
        forward(spd.get())
        lbl.config(text = 'Speed = %.2f' % spd.get())
    elif(dr.get() == 1):
        stop()
        lbl.config(text = 'Stop')
    elif(dr.get() == 2):
        reverse(spd.get())
        lbl.config(text = 'Speed = %.2f' % spd.get())

def change_dr(d):
    if(dr.get() == 0):
        stop()
        spd.set(0)
        lbl.config(text = 'Forward')
    elif(dr.get() == 1):
        stop()
        spd.set(0)
        lbl.config(text = 'Stop')
    elif(dr.get() == 2):
        stop()
        spd.set(0)
        lbl.config(text = 'Reverse')

lbl = Tkinter.Label(root, text = 'Speed = %.2f' % spd.get())
lbl.pack()

drSlider = Tkinter.Scale(root, label = 'Direction', orient = 'h', from_ = 0, to = 2, showvalue = False, variable = dr, command = change_dr)
drSlider.pack()

spdSlider = Tkinter.Scale(root, label = 'Speed', orient = 'h', from_ = 0, to = 100, showvalue = False, variable = spd, command = change_spd)
spdSlider.pack()

root.mainloop()
