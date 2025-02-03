import zmq
import h5py
import numpy as np

def addToH5(recvData):
    fileName = "streamFile1.h5"
    with h5py.File(fileName, "w") as f:
        f.create_dataset(fileName, data= recvData)


ctx =zmq.Context()
socket =ctx.socket(zmq.SUB)
print("Connecting to pub...")
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

print("Waiting for message ...")

#msg = socket.recv_string()
msg = socket.recv_json()
print("Message Recieved..")
shutdown = 1

data = np.array(msg)
addToH5(data)    