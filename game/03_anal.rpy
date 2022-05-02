#Selector
label analSel:
    if abuse >= r_limit:
        jump rough_anal_norm
    else:
        jump anal_norm

#Entry from non start
#Doggy from anal
label anal_vag_return:
    $ position = "anal"
    # if never anal, add abuse
    if neverAnal:
        $ neverAnal = False
        $ abuse = abuse + 1
    #$ button_screens("anal_loop_01","anal_loop01_screen")
    scene pre_anal_01c
    with dissolve
    "With a swift motion you slide your dick out of her pussy and with a grunt slide it into Clementines ass."
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_01.mp3" loop fadein 1
    $ button_screens("anal_loop_01","anal_loop01_screen")
    clem "Ahhh!"
    "She cries out as your dick fills her."
    p "Fuck this ass is amazing!"
    $ rText()
    "Clementing grunts in pain as you start to fuck her."
    $ noise(1)
    $ slapLine()
    p "Uh.."
    "You grab her arm as she sinks into the mattress"
    p "Ngh..."
    $ noise(1)
    jump anal_repeat


#Normal
label anal_start:
    $ position = "anal"
    $ neverAnal = False
    $ abuse = abuse + 1
    p "Get on the bed, I am going to fuck that ass."
    "Clementines breath catches slightly but she reluctantly kneels on the mattress."
    #kneeling looking back
    scene pre_anal_01
    with dissolve
    clem "Ngh.."
    "You breathe deeply as you move behind her."
    #kneeling hand on ass
    scene pre_anal_01b
    with dissolve
    "She looks away, head sinking into the bed as she raises her rear."
    clem "Ahhh... hnnn..."
    "You drink in the sight as you lightly stroke yourself."
    p "Nice..."
    scene pre_anal_01c
    with dissolve
    "You whistle softly as you slide your dick between her cheeks"
    p "Ahhh.."
    "A gasp slips from your mouth as you push inside her."
    #play vid
    window hide
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_insert.mp3"  fadein 1
    queue sound "sex/anal/sound/anal_loop_01.mp3" loop
    scene anal_insert with dissolve
    pause 2
    window show
    jump anal_norm


label anal_norm:
    if doneAnal == True:
        $ button_screens("anal_loop_01","anal_loop01_screen")
        jump anal_repeat
    $ posCount += 1
    $ neverAnal = False
    scene anal_loop_01
    with dissolve
    clem "Nghhhh..."
    $ button_screens("anal_loop_01","anal_loop01_screen")
    $ doneAnal = True
    "She hisses as you slide your dick in her tight ass, back clenching."
    p "Fuck."
    "You groan as you thrust into her, tuning out the the hiccups of pain from the girl."
    p "Damn.. worth the wait..."
    $ rText()
    "You slide your hands up to her hips as you go in and out."
    window hide
    pause 5
    window show
    $ noise(3)
    "You reach up and grab her left arm as her head sinks onto the mattress."
    p "Oh.."
    "You speed up, slapping into her cheeks."
    $ noise(2)
    "Her voice catches raggedly as you fuck her ass, in obvious discomfort."
    p "Fuck..."
    $ slapLine()
    "You ignore her pain as you pump in and out"
    window hide
    pause 5
    window show
    $ nText()
    p "Fuck girl..."
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel
    menu:
        "[kg]":
            jump anal_repeat
        "[su]":
            jump anal_faster
        "[cp]":
            jump from_anal



label anal_repeat:
    $ posCount += 1
    $ doneAnal = True
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_01.mp3" loop fadein 1
    $ noise(2)
    p "Ah..."
    p "Your ass is amazing."
    $ rText()
    "She her breath catches as you thrust in and out."
    $ noise(2)
    window hide
    pause 5
    window show
    p "Fuck..."
    $ noise(1)
    #if posCount == 5:
        #jump anal_cum
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel
    menu:
        "[kg]":
            jump anal_repeat
        "[su]":
            jump anal_faster
        "[cp]":
            jump from_anal


label anal_faster:
    $ neverAnal = False
    if doneAnalFast:
        $ button_screens("anal_loop_02","anal_loop02_screen")
        jump anal_repeat
    $ position = "anal"
    $ posCount += 1
    $ doneAnalFast = True
    p "Ahh shit..."
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_02.mp3" loop fadein 1
    $ button_screens("anal_loop_02","anal_loop02_screen")
    "You let go of the girls arm and grip her hips, driving her into the bed."
    $ button_screens("anal_loop_02","anal_loop02_screen")
    $ noise(2)
    $ slapLine()
    "Clementine cries out as you drive forward, pounding her ass."
    $ nText()
    "The sound of flesh slapping fills the room as you bounce off her rear."
    p "Uh.... so tight."
    $ slapLine()
    $ noise(1)
    p "Uh..."
    "You grip her hips hard, holding her in place as you drive into her."
    window hide
    pause 5
    window show
    p "Oooh..."
    $ noise(1)
    "She cries out as you push her into the bed over and over, gripping at the cloth of the mattress."
    $ slapLine()
    $ noise(1)
    window hide
    pause 5
    window show
    p "Fuck.... ah..."
    $ noise(2)
    "You focus on her ass as you pound, and think about shifting position."
    #if posCount == 5:
        #jump anal_cum
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel
    menu:
        "[kg]":
            jump anal_faster
        "[sd]":
            jump anal_norm
        "[cp]":
            jump from_anal


label anal_fast_repeat:
    $ neverAnal = False
    $ position = "anal"
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_02.mp3" loop fadein 1
    clem "Ahhh!"
    p "Man I can't get enough..."
    "Clementine doesnt reply as you tightly grip her waist, driving your cock into her ass."
    $ noise(1)
    p "Fuck..."
    $ slapLine()
    $ noise(1)
    window hide
    pause 5
    window show
    p "Shit..."
    $ noise(1)
    "You can hear her sucking breath as you pump in and out."
    $ nText()
    $ noise(1)
    $ slapLine()
    "You close your eyes breifly, savouring the sensation."
    #if posCount == 5:
        #jump anal_cum
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel
    menu:
        "[kg]":
            jump anal_fast_repeat
        "[sd]":
            jump anal_norm
        "[cp]":
            jump from_anal


#Rough
label rough_anal_start:
    $ neverAnal = False
    $ position = "rough_anal"
    $ doneRoughAnal = True
    p "Get on the bed slut, I am going to wreck that ass."
    clem "... fuck you!"
    #kneeling, not looking back
    scene pre_anal_02
    with dissolve
    "She whimpers slightly as she kneels down on the bed."
    p "Yeah..."
    "You stroke yourself as you stand behind her, watching the slight tremble in her body."
    p "This is going to be sweet."
    #hand grabbing ass
    scene pre_anal_02b
    with dissolve
    "You grab her cheek, peeling it away as you slide your dick against her hole."
    p "Get ready whore..."
    $ rNoise(1)
    #play vid
    window hide
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_insert.mp3"  fadein 1
    queue sound "sex/anal/sound/anal_loop_01.mp3" loop
    scene anal_insert with dissolve
    pause 2
    window show
    jump rough_anal_norm

label rough_anal_norm:
    $ neverAnal = False
    if doneRoughAnal:
        $ button_screens("anal_loop_01","anal_loop01_screen")
        jump rough_anal_repeat
    $ posCount += 1
    scene anal_loop_01
    "She gasps in pain as you push into her, hissing through her teeth."
    $ button_screens("anal_loop_01","anal_loop01_screen")
    $ rText()
    p "Ah!"
    $ slapLine()
    "You thrust into her, reaching forward to grab her arm and she sinks into the mattress."
    $ rText()
    p "Shut up whore."
    $ rNoise(1)
    $ slapLine()
    $ rNoise(1)
    "You grip her waist firmly as the room fills with slapping sounds."
    window hide
    pause 5
    window show
    $ rNoise(1)
    "She gasps sharply as you fuck her, punctuated with whimpers of pain."
    p "Uhhhh..."
    $ slapLine()
    p "Just shut up and enjoy the ride slut."
    $ rText()
    "You grip her arm tightly, feeling the flesh squish underneath."
    $ rNoise(1)
    p "Uh... uh..."
    $ slapLine()
    $ rNoise(1)
    p "Shit..."
    p "Time for something new..."
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel_rough
    menu:
        "[kg]":
            jump rough_anal_start
        "[su]":
            jump rough_anal_faster
        "[cp]":
            jump from_anal


label rough_anal_repeat:
    $ position = "anal"
    $ posCount += 1
    clem "Ahh!"
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_01.mp3" loop fadein 1
    "Clementine grunts as you pump her ass, fingers clawing at air."
    p "Fuck slut!"
    $ rNoise(1)
    $ slapLine()
    p "So good..."
    $ rText()
    "You exhale sharply as you fuck her."
    p "Such a good piece of ass!"
    $ rText()
    window hide
    pause 5
    window show
    $ rNoise(1)
    p "Uh.. uh..."
    $ slapLine()
    $ rNoise(1)
    "You grip tightly at her arm, fingers digging into her arm."
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel_rough
    if posCount == 6:
        jump cum_anal_from_kneel
    menu:
        "[kg]":
            jump rough_anal_repeat
        "[su]":
            jump rough_anal_faster
        "[cp]":
            jump from_anal


label rough_anal_faster:
    $ neverAnal = False
    if doneRoughAnalFast:
        jump rough_anal_fast_repeat
    $ position = "anal"
    $ posCount += 1
    $ doneRoughAnalFast = True
    p "Time to pound that ass cunt!"
    "You let go of the girls arm and grab her hips, driving her into the bed."
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_02.mp3" loop fadein 1
    $ button_screens("anal_loop_02","anal_loop02_screen")
    clem "Ahhh!"
    p "Take it whore!"
    "She screams out as you start to slam into her ass."
    $ rNoise(1)
    $ slapLine()
    p "Fucking slut!"
    $ rText()
    "You tighten your grip on her hips, feeling her flesh tear under your fingers."
    $ rNoise(1)
    $ rText()
    "Clementine screams out as you fuck her."
    $ nText()
    p "Shut up and take it!"
    $ slapLine()
    window hide
    pause 5
    window show
    $ rNoise(1)
    "She claws at the air while you bounce off her ass."
    $ nText()
    $ rNoise(1)
    p "Ah fuck... I could fuck your ass all day!"
    $ rText()
    "Clementine whimpers as the sound of slapping flesh fills the room."
    window hide
    pause 5
    window show
    $ rNoise(1)
    p "Ngg!"
    $ rNoise(1)
    p "Shit... whore..."
    #if posCount == 5:
        #jump rough_anal_cum
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel_rough
    menu:
        "[kg]":
            jump rough_anal_fast_repeat
        "[sd]":
            jump rough_anal_norm
        "[cp]":
            jump from_anal



label rough_anal_fast_repeat:
    $ position = "anal"
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/anal/sound/anal_loop_02.mp3" loop fadein 1
    p "Fuck cunt your ass is great. Take it!"
    $ rText()
    $ rNoise(1)
    "You can feel her breaking as you pump her ass."
    p "Ahh fuck cunt. So good!"
    $ nText()
    $ rNoise(1)
    p "Can't wait to fill it!"
    $ rText()
    window hide
    pause 5
    window show
    $ rNoise(1)
    p "Yeah slut..."
    $ nText()
    "You lean in, breath hot on the back of her neck."
    p "You think we are done yet cunt?"
    $ rNoise(1)
    #if posCount == 5:
        #jump rough_anal_cum
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_anal_from_kneel_rough
    menu:
        "[kg]":
            jump rough_anal_fast_repeat
        "[sd]":
            jump rough_anal_norm
        "[cp]":
            jump from_anal
