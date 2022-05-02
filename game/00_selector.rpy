



label prefuck:
    stop music fadeout 10
    #"Abuse = [abuse], s_limit = [s_limit], r_limit = [r_limit]"
    $ hide_overlay()
    if abuse > 2:
         menu:
            "Fuck her pussy...":
                 jump miss_rough_start
            "Fuck her doggy...":
                 jump doggy_rough_start
            "Fuck her ass...":
                 jump rough_anal_start

    elif abuse == 0:
         menu:
            "Fuck her pussy...":
                 jump miss_happy_start
            "Fuck her doggy...":
                 jump doggy_happy_start
            "Fuck her ass...":
                 jump anal_start
    else:
        menu:
            "Fuck her pussy...":
                jump miss_start
            "Fuck her doggy...":
                jump doggy_start
            "Fuck her ass...":
                jump anal_start


#Selectors handle the selction between rough normal and happy versions of postions

#menu selectors
label from_anal:
    #"poscount = [posCount]"
    menu:
        "Prone bone...":
            jump pAnalSel
        "Doggy...":
            jump return_doggy_anal
        "On side...":
            jump from_an
        "Choke her..." if posCount >= 4 and abuse >= r_limit:
            jump chokeFromFours


label from_anal_prone:
    #"poscount = [posCount]"
    menu:
        "Anal...":
            jump analSel
        "Doggy...":
            jump return_doggy_anal
        "Choke her..." if posCount >= 4 and abuse >= r_limit:
            jump chokeFromProne

label from_vag_prone:
    #"poscount = [posCount]"
    menu:
        "Doggy...":
            jump return_doggy_vag
        "On side...":
            jump from_kneel
        "Choke her..." if posCount >= 4 and abuse >= r_limit:
            jump chokeFromProne

label from_doggy:
    #"poscount = [posCount]"
    menu:
        "Anal...":
            jump anal_vag_return
        "On side...":
            jump from_kneel
        "Pussy prone...":
            jump pVagSel
        "Choke her..." if posCount >= 4 and abuse >= r_limit:
            jump chokeFromFours


label from_missionary:
    menu:
        "On side...":
            jump from_back
        #"Pussy prone...":
        #    jump prone_
        "Choke her..." if posCount == 4 and abuse >= r_limit:
           jump chokeFromMiss



label from_side:
    #"poscount = [posCount]"
    $ doneSide = False
    $ doneRoughSide = False
    $ doneHappySide = False
    menu:
        "Doggy...":
            jump return_doggy_vag
        "Missionary...":
            jump return_side
        "Choke her..." if posCount == 4 and abuse > 2:
           jump chokeFromSide












#
