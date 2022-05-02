
#From doggy
label from_an:
    p "Ahh"
    #image
    stop sound fadeout 2
    $ hide_overlay()
    scene from_vag
    with dissolve
    "You push forward, forcing Clementine onto the bed as you slide a hand under her leg."
    "She rolls onto her side as you lift her leg."
    "Quickly youy slide your cock out of her ass and drive it into her pussy."
    clem "Ngh!"
    jump sideSelector

#From doggy
label from_kneel:
    p "Ahh"
    #image
    stop sound fadeout 2
    $ hide_overlay()
    scene from_vag
    with dissolve
    "You push forward, forcing Clementine onto the bed as you slide a hand under her leg."
    "She rolls onto her side as you lift her leg."
    jump sideSelector

#From missionary
label from_back:
    p "Ahh"
    #image
    stop sound fadeout 2
    $ hide_overlay()
    scene from_anal
    with dissolve
    "You reach under her leg, rolling the girl up onto her side."
    "With a gasp she props herself up as you roll her onto her side and start to stroke in and out."
    jump sideSelector


label sideSelector:
    if abuse >= r_limit:
        jump rough_side
    elif abuse > 0:
        jump side_
    else:
        jump happy_side



#normal
label side_:
    if doneSide:
        $ button_screens("side_loop","side_loop_screen")
        jump side_repeat
    $ position = "onside"
    $ posCount += 1
    $ doneSide = True
    clem "Ah.."
    $ button_screens("side_loop","side_loop_screen")
    stop sound fadeout 0.5
    play sound "sex/onside/sound/onside_loop.mp3" loop fadein 1
    p "Ahh..."
    "Clementine gasp as you drive deep inside her."
    window hide
    pause 5
    window show
    $ noise(1)
    p "Shit..."
    "She rocks back and forth on the bed, eyes lidded."
    $ noise(2)
    p "Oohh..."
    $ noise(1)
    "The girl's head hangs loose, rocking with her body motion."
    window hide
    pause 5
    window show
    $ noise (1)
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_side
    $ hide_overlay()
    menu:
        "[kg]":
            jump side_repeat
        "[cp]":
            jump from_side


label side_repeat:
    $ position = "onside"
    $ posCount += 1
    p "Mmmm... ah"
    $ noise(1)
    p "Oh..."
    $ slapLine()
    $ nText()
    p "Uh..."
    $ noise(2)
    window hide
    pause 5
    window show
    $ noise(1)
    p "Uh.."
    $ noise(2)
    p "Mmm.. Damn..."
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_side
    $ hide_overlay()
    menu:
        "[kg]":
            jump side_repeat
        "[cp]":
            jump from_side





#rough
label rough_side:
    if doneRoughSide:
        $ button_screens("side_loop","side_loop_screen")
        jump rough_side_repeat
    $ position = "onside"
    $ posCount += 1
    $ doneRoughSide = True
    clem "Ah!"
    $ button_screens("side_loop","side_loop_screen")
    stop sound fadeout 0.5
    play sound "sex/onside/sound/onside_loop.mp3" loop fadein 1
    "You grip her ankle tightly and slam into her pussy."
    p "Ahh you are the best whore..."
    "She ignores you, teeth clenched."
    $ rNoise(1)
    window hide
    pause 5
    window show
    "She winces and looks down at the mattress"
    clem "Fuck you..."
    p "Hah... fuck yeah..."
    $ rNoise(1)
    "She looks at you from the corner of her eyes, frowning."
    $ rNoise(2)
    p "Such a nice cunt..."
    window hide
    pause 5
    window show
    p "Ahh..."
    $ rNoise(1)
    "You hold her leg tight, roughly fucking the girl."
    #cum flag
    if posCount == 6:
        jump cum_missionary_rough_side
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_side_repeat
        "[cp]":
            jump from_side

label rough_side_repeat:
    $ position = "onside"
    $ posCount += 1
    p "Ah fuck..."
    $ rNoise(2)
    "Her voice is ragged as you thrust, sucking air through your teeth."
    $ slapLine()
    window hide
    pause 5
    window show
    $ rNoise(1)
    p "Ngh! Whore!"
    $ rText()
    $ rNoise(1)
    #cum flag
    if posCount == 6:
        jump cum_missionary_rough_side
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_side_repeat
        "[cp]":
            jump from_side





#happy
label happy_side:
    if doneHappySide:
        $ button_screens("side_loop","side_loop_screen")
        jump happy_side_repeat
    $ position = "onside"
    $ posCount += 1
    $ doneHappySide = True
    clem "Ah...!"
    $ button_screens("side_loop","side_loop_screen")
    stop sound fadeout 0.5
    play sound "sex/onside/sound/onside_loop.mp3" loop fadein 1
    "Clementine gasps as you sink deep in her pussy."
    $ hText()
    p "Oh... so good..."
    "You gasp as she chuckles softly, eyes hooded."
    $ hNoise(1)
    $ slapLine()
    $ hText()
    p "Mmm..."
    window hide
    pause 5
    window show
    $ hText()
    $ hNoise(1)
    p "Nn.."
    $ slapLine()
    $ hNoise(2)
    "You pump in and out as the girl moans raggedly, her pussy gripping you tight."
    p "Ahh... ah... your pussy is the best!"
    $ hText()
    "She whimpers."
    $ hNoise(1)
    p "Oh god..."
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_side
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_side
    $ hide_overlay()
    menu:
        "[kg]":
            jump happy_side_repeat
        "[cp]":
            jump from_side


label happy_side_repeat:
    $ position = "onside"
    $ posCount += 1
    $ hText()
    p "Oh... yeah..."
    $ slapLine()
    $ hNoise(1)
    p "Uh..."
    $ slapLine()
    $ hText()
    $ hNoise(1)
    window hide
    pause 5
    window show
    p "Ahh..."
    $ hText()
    p "Pussy is so good..."
    $ hNoise(2)
    $ slapLine()
    p "Uh..."
    $ hText()
    p "Damn..."
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_side
    #cum flag
    if posCount == 6:
        jump cum_missionary_norm_side
    $ hide_overlay()
    menu:
        "[kg]":
            jump happy_side_repeat
        "[cp]":
            jump from_side
