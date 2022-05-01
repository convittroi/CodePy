import random
import time
while True:
    a= random.sample(range(1,10),3)
    print(a)
    time.sleep(1)
    if sum(a) <10:
        break