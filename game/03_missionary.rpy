
label vSelector:
    if abuse == 0:
        jump miss_happy
    elif abuse >= r_limit:
        jump miss_norm
    else:
        jump miss_rough


#return from side
label return_side:
    "You roll Clementine onto her back, pushing her knee away."
    jump vSelector


#normal
label miss_start:
    p "Lie back on the bed."
    "Clementine looks at you for a moment before climbing back onto the mattress."
    scene pre_mis with dissolve
    clem "Like this?"
    "You look her up and down, stroking your hardening dick."
    p "Oh yea... let me get in there."
    scene vag_pre
    with dissolve
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_pre_loop.mp3" loop fadein 1
    clem "Ah... "
    "You step forward and slide your dick over her pussy lips."
    p "Oooh..."
    clem "Uh..."
    "The girl moans lightly."
    p "Time for the main course then."
    clem "Hnn.."
    "With a sigh you slide your dick inside Clementine."
    window hide
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_insert.mp3" fadein 1
    queue sound "sex/mission/sound/miss_loop_01.mp3" loop
    scene vag_insert with dissolve
    pause 4
    window show
    jump miss_norm



label miss_norm:
    $ posCount += 1
    if doneMissionary:
        jump miss_norm_repeat
    $ doneMissionary = True
    scene miss_loop_01
    with dissolve
    clem "Ahh!"
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    p "Oh shit..."
    "You easily slide inside her pussy, pumping in and out."
    $ noise(2)
    $ slapLine()
    p "Damn... ah..."
    window hide
    pause 5
    window show
    $ noise(2)
    p "Ah... hah..."
    "The bed creaks as you fuck the girl."
    $ nText()
    $ noise(2)
    window hide
    pause 5
    window show
    p "Ngh... hah.... damn."
    $ noise(2)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_norm_repeat
        "[su]":
            jump miss_norm_fast
        "[cp]":
            jump from_missionary


label miss_norm_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_loop_01.mp3" loop fadein 1
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    p "Shit... so good..."
    $ noise(2)
    "The girl moans as you thrust, one hand holding her leg aside."
    $ slapLine()
    $ noise(2)
    window hide
    pause 5
    window show
    p "Ah... nhh..."
    $ nText()
    $ noise(2)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_norm_repeat
        "[su]":
            jump miss_norm_fast
        "[cp]":
            jump from_missionary




label miss_norm_fast:
    $ posCount += 1
    $ doneMissionaryFast = True
    p "Ah shit..."
    "With a groan you drop forward, hands on the bed and start to drill into Clementine."
    play sound "sex/mission/sound/miss_loop_02.mp3" loop fadein 1
    $ button_screens("miss_loop_02","miss_loop_02_screen")
    $ nText()
    $ noise(2)
    p "Ahh... hah..."
    window hide
    pause 5
    window show
    $ slapLine()
    p "Ah.."
    $ noise(2)
    window hide
    pause 5
    window show
    "Clementine sucks air though her teeth, the sound of slapping flesh filling the air."
    $ nText()
    $ noise(2)
    p "Ngh.... nhhh..."
    $ noise(1)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_norm_fast_repeat
        "[sd]":
            jump miss_norm_repeat
        "[cp]":
            jump from_missionary




label miss_norm_fast_repeat:
    $ posCount += 1
    play sound "sex/mission/sound/miss_loop_02.mp3" loop fadein 1
    $ button_screens("miss_loop_02","miss_loop_02_screen")
    p "Ah... shit..."
    "You look down at her slim body, watching your dick sink inside her over and over."
    $ nText()
    $ noise(2)
    window hide
    pause 5
    window show
    $ slapLine()
    $ noise(2)
    p "Hnn... ngh..."
    $ noise(1)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_norm_fast_repeat
        "[sd]":
            jump miss_norm_repeat
        "[cp]":
            jump from_missionary






#rough
label miss_rough_start:
    p "Sit on the bed whore."
    "Clementine glowers at you as she sits down on the mattress."
    scene pre_mis with dissolve
    p "Time to fuck that pussy!"
    clem "Ngg..."
    "Clementine sucks in her breath as you step forward."
    p "Ahh... nice..."
    clem "Hn.."
    scene vag_pre
    with dissolve
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_pre_loop.mp3" loop fadein 1
    "You slide your dick up and down her slit, relighing her discomfort."
    p "Yeah like that, cunt?"
    clem "Fuck you."
    p "Mmm... nah think thats you..."
    clem "Hnn..."
    p "Well lets get started slut!"
    clem "Ahh!"
    "With a swift move you slide back and drive your dick into her pussy."
    window hide
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_insert.mp3" fadein 1
    queue sound "sex/mission/sound/miss_loop_01.mp3" loop
    scene vag_insert with dissolve
    pause 4
    window show
    jump miss_rough



label miss_rough:
    $ posCount += 1
    $ doneMissionary = True
    if doneRoughMissionary:
        jump miss_rough_repeat
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    scene miss_loop_01
    with dissolve
    p "Shit..."
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    $ rNoise(1)
    "Youy grip her knee, spreading her leg as you pump in and out."
    p "Thats a nice pussy whore!"
    $ rText()
    $ rNoise(1)
    window hide
    pause 5
    window show
    p "Ah... shit..."
    $ rNoise(2)
    "Clementine gasps roughly as you fuck her."
    p "You like being full of dick cunt?"
    $ rText()
    $ slapLine()
    $ rNoise(2)
    window hide
    pause 5
    window show
    p "Ngg... ah..."
    $ rNoise(2)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_rough_repeat
        "[su]":
            jump miss_rough_fast
        "[cp]":
            jump from_missionary


label miss_rough_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_loop_01.mp3" loop fadein 1
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    p "Goddamn..."
    "You push her leg out, focusing on your dick fucking her."
    $ rNoise(2)
    p "Ahh... could do this all day..."
    $ rText()
    window hide
    pause 5
    window show
    $ slapLine()
    $ rNoise(2)
    p "Ngh... hnn..."
    $ noise(2)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_rough_missionary
    menu:
        "[kg]":
            jump miss_rough_repeat
        "[su]":
            jump miss_rough_fast
        "[cp]":
            jump from_missionary




label miss_rough_fast:
    $ posCount += 1
    $ doneMissionaryFast = True
    p "Shit... nnn..."
    play sound "sex/mission/sound/miss_loop_02.mp3" loop fadein 1
    $ button_screens("miss_loop_02","miss_loop_02_screen")
    "You drop forward and start to drive in to the girl rapidly."
    $ rNoise(1)
    p "Hah... ha..."
    $ rNoise(2)
    window hide
    pause 5
    window show
    p "Ah... fell that dick whore?"
    $ rText()
    $ slapLine()
    $ rNoise(1)
    "She raises a hand weakly to press at your stomach but you brush it away."
    p "None of that slut..."
    $ rNoise(1)
    window hide
    pause 5
    window show
    $ rNoise(2)
    p "Fuck...."
    $ slapLine()
    $ rNoise(1)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_rough_missionary
    menu:
        "[kg]":
            jump miss_rough_fast_repeat
        "[sd]":
            jump miss_rough_repeat
        "[cp]":
            jump from_missionary




label miss_rough_fast_repeat:
    $ posCount += 1
    play sound "sex/mission/sound/miss_loop_02.mp3" loop fadein 1
    $ button_screens("miss_loop_02","miss_loop_02_screen")
    p "Ah fuck whore..."
    $ rNoise(2)
    $ slapLine()
    "You watch your dick pump into her, relishing the softness."
    $ nText()
    $ rNoise(2)
    window hide
    pause 5
    window show
    p "Ah... nnng..."
    $ rNoise(2)
    p "Whore..."
    $ rNoise(1)
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_missionary_rough_missionary
    menu:
        "[kg]":
            jump miss_rough_fast_repeat
        "[sd]":
            jump miss_rough_repeat
        "[cp]":
            jump from_missionary







#happy
label miss_happy_start:
    p "Jump on the bed..."
    clem "Ok!"
    "She flashes you a smile as she sits back on the mattress."
    scene pre_mis with dissolve
    clem "Ahh..."
    "Clementine wriggles her hips as you step between her legs."
    p "Ahhh..."
    "You drop your dick onto her lips and slide it up and down."
    scene vag_pre
    with dissolve
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_pre_loop.mp3" loop fadein 1
    clem "Nnnn...."
    p "Yeah... you like that?"
    clem "Nnn... yeah..."
    p "Well lets get to the main course then..."
    clem "Ahh!"
    "She gasps as you push her leg to the side and slide into her wet pussy."
    window hide
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_insert.mp3" fadein 1
    queue sound "sex/mission/sound/miss_loop_01.mp3" loop
    scene vag_insert with dissolve
    pause 4
    window show
    jump miss_happy



label miss_happy:
    $ posCount += 1
    $ doneMissionary = True
    if doneHappyMissionary:
        jump miss_happy_repeat
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    p "Fuuuuck..."
    $ nText()
    "Clementine groans as your dick moves in and out of her."
    p "Ahh... you like that?"
    clem "Ngh... yea..."
    $ hNoise(2)
    window hide
    pause 5
    window show
    p "So good..."
    $ hNoise(2)
    p "Ah... hnnn..."
    window hide
    pause 5
    window show
    $ nText()
    p "Ahh.. hah..."
    $ hide_overlay()
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_missionary
    #cum flag
    if posCount == 6:
        jump cum_missionary_happy_missionary
    menu:
        "[kg]":
            jump miss_happy_repeat
        "[su]":
            jump miss_happy_fast
        "[cp]":
            jump from_missionary


label miss_happy_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/mission/sound/miss_loop_01.mp3" loop fadein 1
    $ button_screens("miss_loop_01","miss_loop_01_screen")
    $ hNoise(1)
    p "Ahh... damn..."
    "You push her leg wide, relishing the view."
    $ nText()
    $ hNoise(2)
    window hide
    pause 5
    window show
    p "hah... hah..."
    $ hNoise(1)
    $ hide_overlay()
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_missionary
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_happy_repeat
        "[su]":
            jump miss_happy_fast
        "[cp]":
            jump from_missionary




label miss_happy_fast:
    $ posCount += 1
    $ doneMissionaryFast = True
    "You lean forward, hands on the bed and drive into her."
    play sound "sex/mission/sound/miss_loop_02.mp3" loop fadein 1
    $ button_screens("miss_loop_02","miss_loop_02_screen")
    $ nText()
    p "Ahh..."
    $ hNoise(2)
    window hide
    pause 5
    window show
    $ slapLine()
    "The crack of flesh on flesh echoes with the creaking bed."
    $ hNoise(1)
    p "Ahh... yeah..."
    $ hText()
    window hide
    pause 5
    window show
    $ hText()
    p "Ahh... take it..."
    clem "Hnn... yeah..."
    $ hNoise(1)
    $ hide_overlay()
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_missionary
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_missionary
    menu:
        "[kg]":
            jump miss_happy_fast_repeat
        "[sd]":
            jump miss_happy_repeat
        "[cp]":
            jump from_missionary




label miss_happy_fast_repeat:
    $ posCount += 1
    play sound "sex/mission/sound/miss_loop_02.mp3" loop fadein 1
    $ button_screens("miss_loop_02","miss_loop_02_screen")
    p "Hhn.. fuck.."
    $ hNoise(1)
    $ nText()
    "Clementine gasps as the bad bangs agains the wall."
    $ slapLine()
    $ hNoise(2)
    window hide
    pause 5
    window show
    p "Ahh... shit..."
    $ hNoise(2)
    $ hide_overlay()
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_missionary
    #cum flag
    if posCount == 6:
        jump cum_missionary_happy_missionary
    menu:
        "[kg]":
            jump miss_happy_fast_repeat
        "[sd]":
            jump miss_happy_repeat
        "[cp]":
            jump from_missionary
