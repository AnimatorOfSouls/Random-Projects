supremium = int(input("Supremium: "))
superium = int(input("Superium: "))
intermedium = int(input("Intermedium: "))
prudentium = int(input("Prudentium: "))
inferium = int(input("Inferium: "))

superium += supremium*4
intermedium += superium*4
prudentium += intermedium*4
inferium += prudentium*4

items = inferium
stacks = 0

while items > 64:
    items = items-64
    stacks += 1

print()
print("Total inferium needed:",inferium,"("+str(stacks),"stacks +",str(items)+")")
