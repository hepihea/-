
#Start branches
label return_doggy_vag:
    $ position = "doggy"
    $ doneDoggy = True
    "You grip Clementines hips and pull her onto all fours, as you sink your dick into her pussy."
    if abuse >= r_limit:
        jump rough_doggy
    if abuse > 0:
        jump doggy_norm
    else:
        jump happy_doggy

label return_doggy_anal:
    $ position = "doggy"
    $ doneDoggy = True
    "With a swift move you slide your dick from Clementine’s ass, position it over her pussy and pull her back onto your shaft."
    if abuse >= r_limit:
        jump rough_doggy
    if abuse > 0:
        jump doggy_norm
    else:
        jump doggy_happy_start


#Starts
label doggy_start:
    $ position = "doggy"
    $ doneDoggy = True
    "You look her up and down slowly."
    p "Get on the bed."
    "Clementine looks at you sideways and sits down on the edge of the mattress."
    p "No. On all fours..."
    clem "Hnn.."
    "Her eyes tighten slightly but she turns over onto her knees."
    show pre_dog01
    with dissolve
    clem "Happy?"
    "She looks back at you over her shoulder while you stare at her ass."
    p "Getting there."
    "You approach and she turns away, placing both hands on the bed."
    show pre_dog02
    with dissolve
    clem "Hah.."
    "You stare at her for a moment."
    p "Nice."
    clem "Mmmh..."
    "Climbing onto the mattress you slide a hand over her brown cheeks as you grip your rod."
    show pre_dog03
    with dissolve
    "You place the head of your dick against her soft lips, a tingle shooting up your spine."
    p "Ooooh..."
    "Clementine emits a low groan as you slide your dick into her pussy."
    window hide
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_insert.mp3" fadein 1
    queue sound "sex/doggy/sound/dog_loop_01.mp3" loop
    show movie
    play movie "sex/doggy/dog_insert.webm" noloop
    pause 2.8
    window show
    jump doggy_norm

label doggy_rough_start:
    $ position = "doggy"
    $ doneRoughDoggy = True
    p "All fours on the bed cunt, time to fuck that pussy."
    show pre_dog02
    with dissolve
    "You give her a shove on her shoulder and she turns and climbs onto the bed, head hanging."
    clem "Hngh..."
    "You climb behind her and grip her ass, kneading it roughly."
    clem "Ngh!"
    p "Try to enjoy it whore."
    show pre_dog03
    with dissolve
    "You chuckle as you line up your dick with her lips."
    p "Ooooooh"
    "With a groan you slide your dick inside her and start pumping."
    window hide
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_insert.mp3" fadein 1
    queue sound "sex/doggy/sound/dog_loop_01.mp3" loop
    show movie
    play movie "sex/doggy/dog_insert.webm" noloop
    pause 2.8
    window show
    jump rough_doggy

label doggy_happy_start:
    $ position = "doggy"
    "Clementine looks at you coyly, a slight smile on her lips."
    clem "Well?"
    p "I am going to fuck that pussy..."
    clem "Hah!"
    "With a laugh she rolls over onto the bed, looking over her shoulder at you."
    show pre_dog01
    with dissolve
    "She swings her hips, looking at you through lidded eyes."
    p "Damn..."
    "You climb onto the bed behind her, admiring the shape of her ass and pussy."
    show pre_dog03
    with dissolve
    "Reaching out you slide your hand over her ass."
    clem "Ahhh..."
    "You run your dick up and down her lips and she coo's slightly."
    p "Ready?"
    clem "Mmmhmmm..."
    "With a gasp you slide your cock inside her."
    window hide
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_insert.mp3" fadein 1
    queue sound "sex/doggy/sound/dog_loop_01.mp3" loop
    show movie
    play movie "sex/doggy/dog_insert.webm" noloop
    pause 2.8
    window show
    jump happy_doggy



#normal
label doggy_norm:
    if doneDoggy:
        $ button_screens("dog_loop01","dog_loop01_screen")
        jump doggy_repeat
    scene dog_loop01
    p "Oh.."
    $ button_screens("dog_loop01","dog_loop01_screen")
    $ posCount += 1
    #if posCount == 5:
        #jump doggy_cum
    $ nText()
    $ slapLine()
    "You relish teh sensation of her tight pussy gripping your shaft."
    p "Damn... so good..."
    $ nText()
    $ noise(1)
    "Her head sinks into towards the mattress as her breath comes ragged."
    window hide
    pause 5
    window show
    p "Fuck... uh..."
    $ slapLine()
    $ noise(2)
    p "Uh... so worth the wait..."
    "Clementine whimpers slightly, feeling it despite the situation."
    window hide
    pause 5
    window show
    $ nText()
    "You keep a grip on her hips, watching her ass shake with each stroke."
    $ noise(1)
    p "Ahh..."
    $ hide_overlay()
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    menu:
        "[kg]":
            jump doggy_repeat
        "[su]":
            jump doggy_fast
        "[cp]":
            jump from_doggy

label doggy_repeat:
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_01.mp3" loop fadein 1
    $ posCount += 1
    $ position = "doggy"
    p "Shit..."
    "You pump away at her pussy, slapping into her ass."
    window hide
    pause 5
    window show
    $ slapLine()
    $ noise(2)
    p "Ngh..."
    $ nText()
    $ noise(1)
    p "Ha..."
    $ noise(1)
    p "God... dammit..."
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump doggy_repeat
        "[su]":
            jump doggy_fast
        "[cp]":
            jump from_doggy

label doggy_fast:
    if doneDoggyFast:
        $ button_screens("dog_loop02","dog_loop02_screen")
        jump doggy_fast_repeat
    $ posCount += 1
    $ position = "doggy"
    $ doneDoggyFast = True
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_02.mp3" loop fadein 1
    $ button_screens("dog_loop02","dog_loop02_screen")
    "You grasp her waist tighter and start to hammer into her pussy."
    $ noise(1)
    "Clementine gasps as you slam into her, stretching her hands out to grip at the mattress"
    $ nText()
    $ slapLine()
    $ noise(1)
    p "Oh..."
    $ noise(2)
    p "Nnn..."
    window hide
    pause 5
    window show
    $ noise(2)
    $ slapLine()
    "The sharp slaps of your pelvis hitting her ass echoes around the room as Clementine whimpers slightly."
    $ noise(1)
    "The feeling of her pussy drives you on as the bed creaks and shakes."
    p "Ahhh!"
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump doggy_fast_repeat
        "[sd]":
            jump doggy_norm
        "[cp]":
            jump from_doggy

label doggy_fast_repeat:
    $ posCount += 1
    $ position = "doggy"
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_02.mp3" loop fadein 1
    $ slapLine()
    p "Goddamn..."
    $ nText()
    $ noise(1)
    p "Ahh..."
    $ noise(2)
    "Clementine’s ass shakes as you pound her."
    window hide
    pause 5
    window show
    $ slapLine()
    $ noise(1)
    $ nText()
    p "So good..."
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump doggy_fast_repeat
        "[sd]":
            jump doggy_norm
        "[cp]":
            jump from_doggy




#rough
label rough_doggy:
    scene dog_loop01
    p "Ahh!"
    $ button_screens("dog_loop01","dog_loop01_screen")
    if doneRoughDoggy:
        jump rough_doggy_repeat
    $ posCount += 1
    "You groan loudly as you grip her waste, driving into the girl."
    p "Damn that pussy is good!"
    $ rText()
    "You laugh as you fuck her."
    $ rNoise(1)
    p "Ngh..."
    $ rNoise(1)
    p "Enjoying it yet whore?"
    $ rText()
    window hide
    pause 5
    window show
    "You drive into her, gripping her hips tight enough to turn the flesh white."
    clem "Ow!"
    "Clementine cries out in pain but you ignore her."
    p "Uh... uh..."
    $ slapLine()
    $ rNoise(1)
    p "Could do this all day, still tight for a whore."
    $ rText()
    p "Haha!"
    window hide
    pause 5
    window show
    $ rNoise(1)
    p "Oh... fucking slut..."
    $ rNoise(2)
    p "Don't want to end too soon though do we cunt?"
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_doggy_repeat
        "[su]":
            jump rough_doggy_fast
        "[cp]":
            jump from_doggy

label rough_doggy_repeat:
    $ posCount += 1
    $ position = "doggy"
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_01.mp3" loop fadein 1
    $ slapLine()
    "Slapping sounds echo through the room each time you slam into her ass."
    p "Uh..."
    p "Take it cunt!"
    $ rText()
    $ rNoise(1)
    p "Ngh!"
    "Clementine sucks breath through her teeth."
    window hide
    pause 5
    window show
    $ rNoise(1)
    p "Let me know if you’re going to cum whore."
    $ rText()
    $ rNoise(1)
    p "Uhh!"
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_doggy_repeat
        "[su]":
            jump rough_doggy_fast
        "[cp]":
            jump from_doggy


label rough_doggy_fast:
    $ button_screens("dog_loop02","dog_loop02_screen")
    if doneRoughDoggyFast:
        jump rough_doggy_fast_repeat
    $ posCount += 1
    $ position = "doggy"
    $ doneRoughDoggyFast = True
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_02.mp3" loop fadein 1
    "You sink your hips and yank Clementine back onto your dick, speeding up inside her."
    clem "Ahhh!"
    "She cries out, gripping at the mattress."
    p "Take it you whore!"
    $ rText()
    "You laugh at the girl as you pound her cunt."
    window hide
    pause 5
    window show
    p "Ahh fuck!"
    $ rNoise(1)
    p "Uh... uh..."
    $ slapLine()
    "Clementine gasps in pain with each thrust as you yank her back onto your dick over and over."
    window hide
    pause 5
    window show
    $ rNoise(2)
    p "Ngh..."
    p "Hah...!"
    $ rNoise(1)
    p "Damn slut! Fucking you is the best."
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_doggy_repeat
        "[sd]":
            jump rough_doggy_start
        "[cp]":
            jump from_doggy


label rough_doggy_fast_repeat:
    $ posCount += 1
    $ position = "doggy"
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_02.mp3" loop fadein 1
    p "Ah..."
    "The bed creaks and groans as you fuck Clementine."
    $ rNoise(1)
    p "Ahh!"
    $ slapLine()
    p "Take it whore!"
    $ rText()
    p "Hngh!"
    $ rNoise(1)
    window hide
    pause 5
    window show
    p "Ahh!"
    $ rNoise(2)
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump rough_doggy_fast_repeat
        "[sd]":
            jump rough_doggy
        "[cp]":
            jump from_doggy





#happy
label happy_doggy:
    if doneHappyDoggy:
        $ button_screens("dog_loop01","dog_loop01_screen")
        jump happy_doggy_repeat
    scene dog_loop01
    clem "Ahhh..."
    $ button_screens("dog_loop01","dog_loop01_screen")
    $ posCount += 1
    $ doneHappyDoggy = True
    "Clementine moans as you start to fuck her, gripping tightly to her hips."
    $ hText()
    $ hNoise(1)
    p "Ahh... damn..."
    $ slapLine()
    p "So good..."
    $ hText()
    window hide
    pause 5
    window show
    p "Uh... damn"
    "Clementine's breath is ragged as you bounce off her ass."
    $ hText()
    $ hNoise(1)
    p "Shit..."
    "You slide your hands up and down her hips as you thrust."
    window hide
    pause 5
    window show
    p "You feel so good."
    clem "Uh-huh..."
    "She moans in response."
    $ hNoise(1)
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_doggy
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump happy_doggy_repeat
        "[su]":
            jump happy_doggy_fast
        "[cp]":
            jump from_doggy



label happy_doggy_repeat:
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_01.mp3" loop fadein 1
    $ posCount += 1
    $ position = "doggy"
    p "Ohhh..."
    $ slapLine()
    $ hNoise(1)
    p "Uh..."
    $ hNoise(1)
    $ "Your pussy is amazing..."
    $ hText()
    "Clementine moans in response."
    window hide
    pause 5
    window show
    p "Ahh..."
    $ hNoise(2)
    p "Ohhh..."
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_doggy
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump happy_doggy
        "[su]":
            jump happy_doggy_fast
        "[cp]":
            jump from_doggy



label happy_doggy_fast:
    if doneHappyDoggyFast:
        jump happy_doggy_fast_repeat
        $ button_screens("dog_loop02","dog_loop02_screen")
    $ posCount += 1
    $ position = "doggy"
    $ doneHappyDoggyFast = True
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_02.mp3" loop fadein 1
    clem "Uhhh... yeah..."
    $ button_screens("dog_loop02","dog_loop02_screen")
    "Clementine drives back into you, bouncing herself on your dick."
    p "Oh shit!"
    "You groan as she speeds up, slapping into your hips."
    $ hText()
    $ hNoise(1)
    p "Jesus..."
    "The bed rocks and creaks to the sounds of sharp slaps echoing around the room."
    $ hText()
    window hide
    pause 5
    window show
    p "Uh... ah..."
    $ slapLine()
    $ hText()
    $ hNoise(1)
    p "So good...."
    clem "Mmmm.... yea..."
    "She whines plaintively as she grips at the matress."
    window hide
    pause 5
    window show
    p "Ahh..."
    $ hNoise(1)
    p "Goddamn!"
    $ hText()
    $ hNoise(1)
    p "Argh!"
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_doggy
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump happy_doggy_fast
        "[sd]":
            jump happy_doggy
        "[cp]":
            jump from_doggy



label happy_doggy_fast_repeat:
    $ posCount += 1
    $ position = "doggy"
    stop sound fadeout 0.5
    play sound "sex/doggy/sound/dog_loop_02.mp3" loop fadein 1
    p "Ahh..."
    $ hText()
    $ hNoise(1)
    "Clementine pushes back on you, moaning as her she slides up and down your shaft."
    window hide
    pause 5
    window show
    p "Oh so good."
    "You groan at the sensations."
    $ hText()
    $ slapLine(2)
    $ hNoise(1)
    p "Uh... Ahh..."
    $ rNoise(1)
    p "Fuck..."
    $ hText()
    "You grip at her hips, letting her do the work."
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_doggy
    #cum flag
    if posCount == 6:
        jump cum_doggy_from_doggy
    $ hide_overlay()
    menu:
        "[kg]":
            jump happy_doggy_fast_repeat
        "[sd]":
            jump happy_doggy
        "[cp]":
            jump from_doggy
