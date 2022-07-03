from Icosahedron import Icosahedron

counter=0

def main(n):
    ic=Icosahedron(1)

    for i in range(n):
        ic.move()

    if ic.is_at_start():
        global counter
        counter+=1

for i in range(100_000):
    main(100)

print(counter/100_000)
