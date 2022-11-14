from framework import DAC

sleep = 1.0

n = 0
up = True
def loop():
    global n
    global up
    DAC.value = n
    
    if up:
        n = n + 10
    else:
        n = n - 10
    
    if n >= 2 ** 14:
        up = False
    if n <= 20:
        up = True