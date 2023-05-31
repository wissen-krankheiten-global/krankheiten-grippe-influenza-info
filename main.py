import random as r
from pyscript import *

def randomise():
    Element("test").write(r.randint(1,10))
