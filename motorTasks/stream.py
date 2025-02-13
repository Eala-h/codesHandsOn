from epics import PV 
import h5py
import zmq 
import numpy as np 
import queue
import threading

# thread 1 -> receives arrays and meta data -> then place in queque
# thread 2 -> takes data from queque 

acquire = PV('AD:cam1:Acquire')
x = PV('AD:cam1:SizeX_RBV').get()
y = PV('AD:cam1:SizeY_RBV').get()
sharedQ = queue.Queue()
acquire.put(1)

def recive():
    for i in range(10):
        ctx = zmq.Context()
        socket = ctx.socket(zmq.SUB)
        socket.setsockopt(zmq.SUBSCRIBE, b'')
        socket.connect('tcp://10.1.50.20:12345')

        meta = socket.recv_string()
        #sharedQ.put(meta)
        array = socket.recv()
        sharedQ.put(array)

def reshape():
    for i in range(10):
        array = np.frombuffer(sharedQ.get(), dtype= np.uint8)
        arr = array.reshape(x,y)

        with h5py.File('stream2.h5', 'a') as file:
            file.create_dataset(f'img {i}',data=arr)

    

if __name__ == '__main__':

    
    th1 = threading.Thread(target=recive)
    th2 = threading.Thread(target=reshape)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    acquire.put(0)