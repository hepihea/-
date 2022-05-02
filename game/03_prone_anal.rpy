
label pAnalSel:
    if abuse >= r_limit:
        jump rough_panal
    else:
        jump panal



label panal:
    $ posCount += 1
    $ doneProneAnal = True
    "With a groan you shove hard into Clementine's ass, driving her forward."
    clem "Ahh!"
    p "Ngh!"
    "She falls to the mattress and you start to stroke in and out of her ass."
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_anal.mp3" loop fadein 1
    $ button_screens("aprone_loop01","aprone_loop01_screen")
    $ noise(2)
    $ slapLine()
    p "Oh shit..."
    "You drive your cock deep in her cheeks, slapping against her felsh."
    $ nText()
    $ noise(1)
    window hide
    pause 5
    window show
    p "So good..."
    $ noise(1)
    $ nText()
    window hide
    pause 5
    window show
    p "Ah... ah..."
    p "Shit..."
    $ noise(1)
    $ nText()
    "You grip the girls wrist tightly as you bounce off her rear."
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump panal_repeat
        "[su]":
            jump panal_fast
        "[cp]":
            jump from_anal_prone


label panal_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_anal.mp3" loop fadein 1
    $ button_screens("aprone_loop01","aprone_loop01_screen")
    $ nText()
    p "Ah... hah"
    "You drive your dick in as deep as you can, pressing into her hips."
    $ nText()
    "Then draw it out before driving back in."
    p "Ngg... hah..."
    window hide
    pause 5
    window show
    $ noise(1)
    $ slapLine()
    p "Fuck! Getting in there girl..."
    $ nText()
    p "Ahh.. hnn..."
    $ noise(1)
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump panal_repeat
        "[su]":
            jump panal_fast
        "[cp]":
            jump from_anal_prone


label panal_fast:
    $ posCount += 1
    stop sound fadeout 0.5
    p "Oooooh..."
    "With a groan you speed up, driving into Clementines ass."
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("aprone_loop02","aprone_loop02_screen")
    $ nText()
    $ noise(1)
    "Loud slaps echo around the room as the bed creaks and shakes."
    p "Goddamn!"
    $ noise(1)
    $ slapLine()
    window hide
    pause 5
    window show
    p "Ah shit... so good..."
    $ noise(1)
    $ nText()
    p "Nnh... hnnn..."
    window hide
    pause 5
    window show
    $ noise(1)
    p "Ah..."
    $ noise(1)
    "You can hear Clementine sucking air through her teeth as you drill her."
    $ nText()
    $ noise(1)
    p "Ah... nnnn..."
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump panal_fast_repeat
        "[sd]":
            jump panal_repeat
        "[cp]":
            jump from_anal_prone


label panal_fast_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("aprone_loop02","aprone_loop02_screen")
    # cum flag
    $ noise(1)
    $ slapLine()
    p "Ahh... damn..."
    $ nText()
    $ noise(1)
    window hide
    pause 5
    window show
    p "Ngh... ngh..."
    $ noise(2)
    $ nText()
    if posCount == 6:
        jump cum_anal_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump panal_fast_repeat
        "[sd]":
            jump panal_repeat
        "[cp]":
            jump from_anal_prone


#Rough
label rough_panal:
    $ doneProneAnalRough = True
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_anal.mp3" loop fadein 1
    $ button_screens("aprone_loop01","aprone_loop01_screen")
    p "Arrr!"
    "You shove Clemetine forward, drving your dick as deep as you can."
    clem "Ahhh!"
    "You press her down on the mattress, gripping her wrists while you dig into her ass."
    p "Ahh you feel that deep dick cunt?"
    $ rText()
    "Hah..ha..."
    "You laugh at her defiance, redoubling your efforts."
    $ rNoise(1)
    $ slapLine()
    window hide
    pause 5
    window show
    p "Fuck cunt... what an ass.."
    $ rText()
    "The bed creaks ominously as you bounce off her ass."
    $ rNoise(2)
    p "Ahh... hah... could stay in here all day..."
    $ rText()
    window hide
    pause 5
    window show
    p "Hnn... nng... yea slut..."
    $ rNoise(1)
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_panal_repeat
        "[su]":
            jump rough_panal_fast
        "[cp]":
            jump from_anal_prone

label rough_panal_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_anal.mp3" loop fadein 1
    $ button_screens("aprone_loop01","aprone_loop01_screen")
    "You grip her wrists firmly, stretching her out as you pump her ass."
    $ rNoise(2)
    p "Ahh... so good..."
    $ rText()
    window hide
    pause 5
    window show
    $ slapLine()
    $ rNoise(1)
    p "Nggg... hnnn..."
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_panal_repeat
        "[su]":
            jump rough_panal_fast
        "[cp]":
            jump from_anal_prone

label rough_panal_fast:
    $ doneProneAnalRoughFast = True
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("aprone_loop02","aprone_loop02_screen")
    p "Shit!"
    "You speed up, slamming into Clementine's hips."
    $ slapLine()
    $ rNoise(1)
    p "Fuck... you... slut..."
    $ rText()
    window hide
    pause 5
    window show
    "She gasps and shakes as you pound into her ass, the sounds of flesh on flash echoing."
    $ rNoise(1)
    window hide
    pause 5
    window show
    p "Fee that dick cunt?"
    $ rText()
    $ rNoise(1)
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_panal_fast_repeat
        "[sd]":
            jump rough_panal_repeat
        "[cp]":
            jump from_anal_prone

label rough_panal_fast_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("aprone_loop02","aprone_loop02_screen")
    "The bed bounces off the wall as you bounce off the girl."
    $ rNoise(2)
    $ nText()
    p "Ahh... fuck..."
    window hide
    pause 5
    window show
    $ rNoise(2)
    p "Ahh... ngh..."
    $ nText()
    # cum flag
    if posCount == 6:
        jump cum_anal_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_panal_fast_repeat
        "[sd]":
            jump rough_panal_repeat
        "[cp]":
            jump from_anal_prone
