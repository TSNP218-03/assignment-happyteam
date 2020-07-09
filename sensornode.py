import socketio
from threading import Timer
import random
import time

min = 36
max = 37

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def msg1(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

def timer(x = False):
    t1 = Timer(2.0, timer)
    if x == True:
        t1.start()
        rnumber = round(random.uniform(min,max),2)
        sio.emit('test-temp',rnumber)
        print(rnumber)
    else:
        t1.cancel()

@sio.event
def ack(message):
    print('message:', message)

sio.connect('http://localhost:55555')
print('my sid is', sio.sid)
timer(True) #call timer

try:
  while True:
    time.sleep(2)
    timer(True)
except KeyboardInterrupt:
  print("handling interrupt...")
  sio.disconnect()

print("done")