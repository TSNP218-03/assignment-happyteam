import socketio
from threading import Timer
import random
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

@sio.event
def timer():
    Timer(2.0, timer).start()
    rnumber = round(random.uniform(min,max),2)
    sio.emit('test-temp',rnumber)

@sio.event
def ack(message):
    print('message:', message)



timer() #call timer

sio.connect('http://192.168.0.35:55555')
print('my sid is', sio.sid)

#sio.wait()