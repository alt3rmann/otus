from car import Car
from engine import Engine

c = Car(1200, 50, 0.2)
c.start()
c.move(100)
c.set_engine(Engine(2.0, 4))
print(c.engine)
