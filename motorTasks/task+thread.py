from epics import PV 
import threading


class Task:
    
    def __init__(self, motor, mn, mx, step):
         self.motor = motor
         self.val = PV(f'TEST-DCA-MC:{self.motor}.VAL')
         self.min = mn
         self.max = mx
         self.step = step
         print(f'min = {self.min} \nmax = {self.max}')
         
    
    def collect(self):
        rbv = PV(f'TEST-DCA-MC:{self.motor}.RBV')
        for current in range(self.min, self.max+1, self.step):
            
            self.val.put(current)
            
            while int(rbv.get()) != current:
                pass

            imgName = 'taskMotor' + self.motor +'.txt'
            with open(imgName, 'a') as f:
                f.write(f"Added to file at {current}\n")

    
        print('Done')

class ThreadsFun:

    def func(self, motor, min, max , step):
        task = Task(motor, min , max, step)
        task.collect()
        
        


if __name__ == '__main__':

    task_A = ThreadsFun()
    task_E = ThreadsFun()

    thread_A = threading.Thread(target=task_A.func, args=('A', 235, 265, 10))
    thread_E = threading.Thread(target=task_E.func, args=('E', -5, 10, 5))

    thread_A.start()
    thread_E.start()

    thread_A.join()
    thread_E.join()
    
    