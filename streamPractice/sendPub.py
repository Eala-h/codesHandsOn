import numpy as np
import json
import zmq


data = np.random.randint(200, size=(100,2))

ctx = zmq.Context()
socket =ctx.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")


while True:
    print(f"Sending message ...")
    #socket.send_string("Hello!")
    socket.send_json(data.tolist())


