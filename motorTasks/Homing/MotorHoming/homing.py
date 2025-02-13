from epics import PV 
import json
import time

class motorHoming:

    def __init__(self, fileName):
        with open(fileName, 'r') as file:
            data = json.load(file)
        motor = data["pvName"]
        self.HL = data["HL"]
        self.OG = data["OG"]
        
        set = motor + '.SET'
        self.set = PV(set)
        #self.val = PV(motor + '.VAL')
        val = motor + '.VAL'
        self.val = PV(val)
        #self.softLimit = PV(motor + '.HLM')
        softLimit = motor + '.HLM'
        self.softLimit = PV(softLimit)
        self.HLS = motor + '.HLS'
    
    def homing(self):
        self.set.put(0)
        self.softLimit.put(999)
        self.val.put(999)
        time.sleep(1)
        while not PV(self.HLS).get():
            pass

        self.set.put(1) # Write in set mode
        self.val.put(self.HL + 1)
        self.softLimit.put(self.HL)
        
        self.set.put(0)
        self.val.put(self.OG)




if __name__ == '__main__':

    import argparse as ap

    parser = ap.ArgumentParser()
    parser.add_argument('fileName',type=str)
    arg = parser.parse_args()

    test = motorHoming(arg.fileName)
    test.homing()        

