from time import sleep

class Trafficlight:

    def running(self, __color):
            print(__color)

tr = Trafficlight()
tr2 = Trafficlight()
tr3 = Trafficlight()

while True:
    tr.running("Red")
    sleep(7)
    tr2.running("Yellow")
    sleep(2)
    tr3.running("Green")
    sleep(2)