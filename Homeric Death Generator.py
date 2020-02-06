#A homeric death generator
#Made by an IRL friend :)

#Example:
#now solaris, enraged by the battle and loss of her horses, turned on katia, daughter of craig, who used to spend her days herding cats which
#Ailuros-allmother had gave to her in the days of her youth, and the great bronze katana punctured her belly and skewered the liver, and the dark shade
#of death came over her eyes.



import random

#Arrays of the possible outcomes
killer=["solaris", "mr pearce", "the school nurse", "theresa may", "professor oak", "kirby", "garbage cat"]
context=["enraged by battle", "driven blind by Ate", "with the furies mad around them", "hoping for a great victory"]
killed=["katia", "ignaceous", "karen", "putin", "neckbeard", "a militant vegan mother"]
biography=["child of Keanu Reeves", "who spent their days working the land near the sweet river of the muses", "a wonderful singer", "who once bought tickets for the original broadway cast of hamilton"]
grislydetail=["the sharp bronze spear punctured their throat, where the windpipe was", "the shining bronze point sliced off their head", "the great bronze sheild crashed down upon their head and split the helmet in two, and the contents spilled out onto the dusty plains of Ilion"]
ded=["and the darkness came over their eyes.", "and their soul went down to Hades, weeping for the youth and life it must leave.", "and their knees were loosened.", "and the blood within their veins grew cold."]

#generating a random number for each array 
killer_num=random.randint(0,len(killer)-1)
context_num=random.randint(0,len(context)-1)
killed_num=random.randint(0,len(killed)-1)
biography_num=random.randint(0,len(biography)-1)
grislydetail_num=random.randint(0,len(grislydetail)-1)
ded_num=random.randint(0,len(ded)-1)

#Printing the story
print(killer[killer_num]+",",context[context_num]+", turned to face",killed[killed_num]+",",biography[biography_num]+", and",grislydetail[grislydetail_num]+",",ded[ded_num])
