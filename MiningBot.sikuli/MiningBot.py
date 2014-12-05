#Outer determines the number of inventories to fill and drop (Also prevent infinite loop)
pickUpRune = True #flag for if you want to pick up rune, faster if false
outer = 4
while outer > 0 :
    notFull = True
    stop = 0
    while (notFull and stop < 40):      
        foundRune = False
        if(exists("iron-ore-1.png")) :        
            if foundRune :
                sleep(3.5) #Time to run back from getting the rune
                foundRune = False
            click(Pattern("iron-ore-1.png").similar(0.75))
            sleep(1.75) #Time it takes to get the ore
        if(exists(Pattern("iron-ore-2.png").similar(0.75))) :
            click(Pattern("iron-ore-2.png").similar(0.75))
            sleep(1.75) #Time it takes to get the ore

        if(stop % 6 == 0 and pickUpRune):
            if(exists(Pattern("fire-rune.png").similar(0.60))) : #Check ever other cycle, increase productivity
                click(Pattern("fire-rune.png").similar(0.60))
                foundRune = True
                sleep(1.5) #Time it takes to run and get the rune
        else :
            sleep(1)
        if(stop > 11): #Check if full only after 11 cycles, increase productivity
           
            if(False): #TODO Check for gems
                if(exists("sapphire.png")):
                    sleep(.05)#TODO drop
                if(exists("emerald.png")):
                    sleep(.05)#TODO drop
               
            if(exists(Pattern("full-inventory.png").similar(0.75))):
                notFull = False
        stop = stop + 1
    #Loop to drop all ores 
    stop = 0    
    while (stop < 26): 
        try:
            rightClick(Pattern("action-ore.png").similar(0.65))   
            sleep(.1)    
            click(Pattern("action-ore-menu.png").similar(0.39).targetOffset(-25,-7))
            sleep(.1)
        except:
            sleep(.25)
        stop = stop + 1;
    outer = outer - 1
