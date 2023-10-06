from threading import *
from time import sleep


class Hello(Thread):

    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Bye(Thread):
    def run(self):
        for i in range(5):
            print("Bye")
            sleep(1)


t1 = Hello()

t2 = Bye()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("task complete")
