from machine import Pin,Timer
import utime
#IO PIN SET
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(5, Pin.OUT)
IN4 = Pin(4, Pin.OUT)
SW1 = Pin(14, Pin.IN, Pin.PULL_UP)
SW2 = Pin(15, Pin.IN, Pin.PULL_UP)
pins = [IN1, IN2, IN3, IN4]
sequence = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]

def clock_move(timer):
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[3-i])
            utime.sleep_ms(8)
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(0)
               
Timer().init(freq = 8.53325, mode = Timer.PERIODIC, callback = clock_move) 

while True:
    if SW1.value() == 1 and SW2.value() == 0:
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[3-i])
            utime.sleep_ms(2)
    elif SW1.value() == 0 and SW2.value() == 1:
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
            utime.sleep_ms(2)
    else:
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(0)        
            
            