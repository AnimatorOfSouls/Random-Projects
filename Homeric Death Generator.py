#A homeric death generator
#Made by an IRL friend :)

#Example:
#now solaris, enraged by the battle and loss of her horses, turned on katia, daughter of craig, who used to spend her days herding cats which
#Ailuros-allmother had gave to her in the days of her youth, and the great bronze katana punctured her belly and skewered the liver, and the dark shade
#of death came over her eyes.



import random

#Arrays of the possible outcomes
killer=["solaris", "mr pearce", "the school nurse", "theresa may", "professor oak", "kirby", "garbage cat", "jacob sartorius", "student loan debt", "Robert McVitie", "john peters, you know, the farmer", "garnet", "one precocious nine year old", "trixie mattel"]
context=["enraged by battle", "driven blind by Ate", "with the furies mad around them", "hoping for a great victory"]
killed=["katia", "ignaceous", "karen", "putin", "neckbeard", "a militant vegan mother", "the labour leader candidate", "jasmine li", "this bitch"]
biography=["child of Keanu Reeves", "who spent their days working the land near the sweet river of the muses", "who once spent time studying for archaeology but had left to pursue a life of glory", "who had lost the fifth season of drag race", "a wonderful singer", "who once bought tickets for the original broadway cast of hamilton"]
grislydetail=["the sharp bronze spear punctured their throat, where the windpipe was", "the shining bronze point sliced off their head", "the great bronze sheild crashed down upon their head and split the helmet in two, and the contents spilled out onto the dusty plains of Ilion"]
ded=["and the darkness came over their eyes.", "and their soul went down to Hades, weeping for the youth and life it must leave.", "and their knees were loosened.", "and the blood within their veins grew cold."]


#Printing the story
print(killer[random.randint(0,len(killer)-1)]+",",context[random.randint(0,len(context)-1)]+", turned to face",killed[random.randint(0,len(killed)-1)]+",",biography[random.randint(0,len(biography)-1)]+", and",grislydetail[random.randint(0,len(grislydetail)-1)]+",",ded[random.randint(0,len(ded)-1)])

while True:
    ans = str(input("ANOTHER! (y/n) "))
    if ans == "y":
        print("")
        print(killer[random.randint(0,len(killer)-1)]+",",context[random.randint(0,len(context)-1)]+", turned to face",killed[random.randint(0,len(killed)-1)]+",",biography[random.randint(0,len(biography)-1)]+", and",grislydetail[random.randint(0,len(grislydetail)-1)]+",",ded[random.randint(0,len(ded)-1)])
    else:
        break
