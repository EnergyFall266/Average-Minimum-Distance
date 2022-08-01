


import random
vertices = 5000
edges = 900
with open("am.in","a") as f:
    f.truncate(0)
    f.write(f'{vertices} {edges}\n')
i=0
while i<edges:
    num = random.randint(0,vertices)
    num2 = random.randint(0,vertices)

    weight = random.randint(1,vertices)
    with open("am.in","a") as f:
        f.write(f'{num} {num2} {weight}\n')
    i+=1
