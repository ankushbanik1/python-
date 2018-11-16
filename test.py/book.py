from threading import *
class mythread (Thread):
    def run(self):
        for i in range (10):
            print("child")

t=mythread()
t.start()
for i in range (10) :
    print("main ") 
