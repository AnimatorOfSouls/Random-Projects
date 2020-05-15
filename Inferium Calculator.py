def seed_costs():
    print("Tier:\t\t\tInferium:")
    print("1 (Inferium)\t\t8 (0st + 8)")
    print("2 (Prudentium)\t\t36 (0st + 36)")
    print("3 (Intermedium)\t\t148 (2st + 20)")
    print("4 (Superium)\t\t680 (9st + 20)")
    print("5 (Supremium)\t\t2728 (37st + 20)")
    print("6 (Insanium)\t\t10920 (149st + 20)")


def total_inferium_calc():
    insanium = int(input("Insanium: "))
    supremium = int(input("Supremium: "))
    superium = int(input("Superium: "))
    intermedium = int(input("Intermedium: "))
    prudentium = int(input("Prudentium: "))
    inferium = int(input("Inferium: "))

    supremium += insanium*4
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



### MAIN ###
print("Welcome back to the inferium calcultor, for use with the Mystical Agriculture Minecraft Mod.")
print("What would you like to do?")
selection = int(input("1. Display inferium cost of different tiers of seed.\n2. Input number of different essences used.\n\n"))

if selection == 1:
    seed_costs()
else:
    total_inferium_calc()
