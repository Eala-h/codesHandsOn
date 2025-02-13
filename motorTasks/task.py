from epics import PV 
import h5py
import numpy as np 

class Task:
    
    def __init__(self):
         self.val = PV('TEST-DCA-MC:A.VAL')
         self.min = 270
         self.max = 275 
         print(f'min = {self.min} \nmax = {self.max}')
         
    
    def collect(self, data):
        rbv = PV('TEST-DCA-MC:A.RBV')
        step = 1
        for current in range(self.min, self.max+1, step):
            
            self.val.put(current)
            
            while int(rbv.get()) != current:
                pass

            with h5py.File('taskImg2.h5', 'w') as f:
                f.create_dataset(f"Set {current}", data=data)

            print(f"Added to file at {current}")
            

            
        print('Done')





if __name__ == '__main__':

    task = Task()
    #data = np.random.randint(100, size=(10,100))
    #task.collect(data)


    PV('AD:cam1:AcquireTime').put(0.5)
    PV('AD:cam1:AcquirePeriod').put(0.5)
    PV('AD:cam1:ImageMode').put(0)
    PV('AD:cam1:NumImages').put(5)
    acquire = PV('AD:cam1:Acquire')
    arrayData = PV('AD:image1:ArrayData')
    numImgs = 3
    x = PV('AD:cam1:SizeX').get()
    y = PV('AD:cam1:SizeY').get()

    dataArray = []
    for img in range(numImgs):
        acquire.put(1, wait=True)
        data = np.array(arrayData.get())
        data2D = data.reshape(x,y)
        dataArray.append(data2D)

    
    task.collect(dataArray)

    