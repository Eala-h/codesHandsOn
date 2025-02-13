from epics import PV 
import h5py
import numpy as np 

def addToH5(arrayData, i):
    with h5py.File('adSimImg3D(2).h5', 'a') as file:
        file.create_dataset(f'img {i}', data=arrayData)


PV('AD:cam1:AcquireTime').put(0.5)
PV('AD:cam1:AcquirePeriod').put(0.5)
PV('AD:cam1:ImageMode').put(0)
numImgs = PV('AD:cam1:NumImages').put(5)
acquire = PV('AD:cam1:Acquire')
arrayData = PV('AD:image1:ArrayData')

x = PV('AD:cam1:SizeX').get()
y = PV('AD:cam1:SizeY').get()
''' 
dataArray = []

for img in range(numImgs):
    acquire.put(1, wait=True)
    data = np.array(arrayData.get())
    data2D = data.reshape(x,y)
    dataArray.append(data2D)

addToH5(dataArray, img)
    
'''

#Multiple
#acquire.put(0, wait=True)



        

