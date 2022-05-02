#Selector
label pVagSel:
    if abuse >= r_limit:
        jump vprone_rough
    elif abuse > 0:
        jump vprone
    else:
        jump vprone_happy



#normal
label vprone:
    $ posCount += 1
    $ doneProneVag = True
    #if posCount == 5:
        #jump anal_cum
    p "Ohh..."
    "With a groan you slide your hands up Clementine’s body."
    clem "Ngh.."
    "She gasps as she drops to the bed and you follow her down, sinking your rod into her."
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_vag.mp3" loop fadein 1
    $ button_screens("vprone_loop01","vprone_loop01_screen")
    p "Fuck..."
    "You groan as you drive your full length deep inside her, pushing at her womb."
    clem "Uhhhhhhh..."
    "She groans inarticulately as you start to stroke in and out."
    $ nText()
    $ slapLine(1)
    $ noise(3)
    p "Oh shit..."
    window hide
    pause 5
    window show
    "You grip her wrist, staring at her head bob up and down."
    p "You like that dick?"
    $ nText()
    "Clementine groans as you fuck her."
    $ slapLine()
    $ noise(3)
    p "Uh... uh..."
    $ noise(2)
    p "Your pussy is so good..."
    $ nText()
    "She groans in response, fingers flexing."
    window hide
    pause 5
    window show
    $ nText()
    $ noise(2)
    p "Uh... uh..."
    $ slapLine()
    $ noise(2)
    "You stare at her shoulders, watching them roll as you drive her forward."
    p "Shit..."
    $ noise(1)
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_repeat
        "[su]":
            jump vprone_fast
        "[cp]":
            jump from_vag_prone


label vprone_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_vag.mp3" loop fadein 1
    $ button_screens("vprone_loop01","vprone_loop01_screen")
    p "Ahhh..."
    "You slowly sink in and out, relishing the feel of her tight pussy on your cock."
    $ nText()
    p "So good..."
    $ slapLine()
    $ noise(2)
    p "Uh..."
    $ nText()
    $ slapLine()
    $ noise(2)
    window hide
    pause 5
    window show
    "You close your eyes, relishing the feeling as Clementine breathes raggedly."
    $ noise(1)
    $ nText()
    p "Nnn..."
    window hide
    pause 5
    window show
    $ noise(2)
    $ slapLine()
    $ noise(1)
    p "Ahh..."
    $ noise(1)
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_repeat
        "[su]":
            jump vprone_fast
        "[cp]":
            jump from_vag_prone


label vprone_fast:
    $ posCount += 1
    $ doneProneVagFast = True
    p "Shit.."
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("vprone_loop02","vprone_loop02_screen")
    "You grit your teeth and speed up, slapping your hips against Clementine’s ass."
    $ noise(1)
    $ nText()
    "Clementine gasps loudly, trailing off in a whimper as you drive into her."
    p "Ohhh..."
    "The bed shakes as you fuck her, relishing the feeling of her pussy."
    $ noise(2)
    window hide
    pause 5
    window show
    p "Ahh..."
    $ noise(2)
    $ slapLine()
    $ nText()
    "Clementine groans with each stroke as you ride up against the depths of her pussy."
    window hide
    pause 5
    window show
    $ noise(2)
    p "Uh... Fuck..."
    "Her head hangs limp as the girl gasps."
    $ nText()
    $ noise(2)
    p "Uh... Uh.."
    $ noise(2)
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_fast_repeat
        "[sd]":
            jump vprone_repeat
        "[cp]":
            jump from_vag_prone




label vprone_fast_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    "Clementine whimpers as you fuck her, your rod pushing up against her stomach and filling her."
    $ nText()
    p "Fuck! Your pussy is amazing!"
    $ slapLine()
    "She ignores you as the bed creaks and groans."
    $ noise(2)
    $ nText()
    window hide
    pause 5
    window show
    $ noise(2)
    p "Uh... hah..."
    $ nText()
    $ slapLine()
    $ noise(2)
    p "Jesus... Ngh..."
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_fast_repeat
        "[sd]":
            jump vprone_repeat
        "[cp]":
            jump from_vag_prone



#Rough
label vprone_rough:
    $ posCount += 1
    $ doneProneVagRough = True
    "You drive forward, scooping up Clementine’s arms and driving her into the mattress."
    clem "Ooof!"
    "She gasps as the weight of your body presses down on her and you take a firm grip on her wrists."
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_vag.mp3" loop fadein 1
    $ button_screens("vprone_loop01","vprone_loop01_screen")
    p "Ahh... fucking hell..."
    "You raise your body and slide out of her, before driving your length back in."
    $ nText()
    p "Yeah you like that whore?"
    $ rText()
    "She lets out a strained groan as your dick presses up against her cervix."
    clem "Hngh!"
    $ slapLine()
    $ rNoise(2)
    p "Ahh... you feel that dick nice and deep slut?"
    $ rText()
    p "Hah!"
    window hide
    pause 5
    window show
    p "Ah your pussy is so tight."
    $ rNoise(2)
    "Clementine ignores you, gripping at the mattress and wincing each time you dick presses into her."
    $ nText()
    $ rNoise(2)
    p "Oooo... "
    $ rNoise(2)
    "You grip tightly at her wrists, turning the skin white."
    window hide
    pause 5
    window show
    p "Ahh... good little slut!"
    $ rText()
    $ rNoise(3)
    p "Ah... nnn!"
    $ rNoise(2)
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_rough_repeat
        "[su]":
            jump vprone_rough_faster
        "[cp]":
            jump from_vag_prone


label vprone_rough_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_vag.mp3" loop fadein 1
    p "Yeah take it deep cunt."
    $ rText()
    "She gasps, her head shaking slightly as she tries to ignore your deep thrusts."
    $ rNoise(2)
    $ slapLIne()
    p "Ah... shit..."
    $ rNoise(2)
    window hide
    pause 5
    window show
    $ nText()
    "Clementine whimpers, hand flexing in your grip."
    $ noise(2)
    p "Ngh!"
    $  rNoise(2)
    p "fuck you like that deep dick right whore?"
    $ rText()
    $ slapLine()
    $ rNoise(2)
    p "Ohhh. uh..."
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_rough_repeat
        "[su]":
            jump vprone_rough_faster
        "[cp]":
            jump from_vag_prone


label vprone_rough_faster:
    $ posCount += 1
    $ doneProneAnalRoughFast = True
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("vprone_loop02","vprone_loop02_screen")
    p "Fuck... take it slut..."
    $ nText()
    $ slapLine()
    "Clementine's breath is ragged and coarse as yoiu slam into her over and over."
    $ rNoise(2)
    p "Ahh! Fucking whore!"
    window hide
    pause 5
    window show
    "You twist at her wrists, pinning her tight to the bed."
    $ nText()
    p "Ngh... ah..."
    $ rNoise(2)
    p"Ahh..."
    $ rNoise(1)
    "Sharp slaps echo around the room as you bounce off her ass, pressing at her womb with each thrust."
    $ rNoise(1)
    window hide
    pause 5
    window show
    p "Take that dick slut... ah..."
    $ nText()
    $ rNoise(2)
    $ slapLine()
    p "Ahh... uh..."
    $ rNoise(1)
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_rough_faster_repeat
        "[sd]":
            jump vprone_rough_repeat
        "[cp]":
            jump from_vag_prone



label vprone_rough_faster_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    "You wallow in the sensation of her body as you bounce off her ass."
    p "Ahh... shit..."
    $ rNoise(2)
    p "Feel that dick slut."
    "You growl in her ear through clenched teeth."
    $ rText()
    window hide
    pause 5
    window show
    $ rNoise(2)
    $ nText()
    p "Ahhh... uh..."
    $ noise(1)
    p "Aah!"
    $ rNoise(2)
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone_rough
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_rough_faster_repeat
        "[sd]":
            jump vprone_rough_repeat
        "[cp]":
            jump from_vag_prone

#Happy
label vprone_happy:
    $ posCount += 1
    $ doneProneVagHappy = True
    p "Ahhh...."
    "With a groan you slide your hands up under Clementine’s arms and she falls to the bed."
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_vag.mp3" loop fadein 1
    $ button_screens("vprone_loop01","vprone_loop01_screen")
    $ nText()
    "She groans as your dick slides deep inside her body, pressing at her womb."
    p "Uhhh.... so good..."
    $ noise(1)
    "Clementine whimpers in agreement."
    p "Ahh..."
    "You stroke in and out, stretching the girl out under you."
    p "You like that dick?"
    $ hText()
    window hide
    pause 5
    window show
    $ hNoise()
    $ nText()
    p "Oh shit..."
    $ hText()
    $ slapLine()
    "Clementine moans raggedly as you fuck her, the bed creaking."
    window hide
    pause 5
    window show
    $ hNoise(3)
    p "Uh... oh..."
    "The girls head hangs loose, rocking in time with the mattress."
    $ hNoise(1)
    $ nText()
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_prone
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_happy_repeat
        "[su]":
            jump vprone_happy_faster
        "[cp]":
            jump from_vag_prone


label vprone_happy_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_vag.mp3" loop fadein 1
    $ hText()
    "You suck air through your teeth."
    p "Ah... do what I can..."
    $ hNoise(2)
    $ slapLine()
    $ hNoise
    p "Ahh... fuck..."
    window hide
    pause 5
    window show
    $ nText()
    p "Ahh.. uh..."
    $ hNoise(2)
    "Clementine's hands flex against the mattress as a strained groan escapes her lips."
    $ hText()
    $ hNoise(2)
    p "Ah... ah..."
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_prone
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_happy_repeat
        "[su]":
            jump vprone_happy_faster
        "[cp]":
            jump from_vag_prone


label vprone_happy_faster:
    $ posCount += 1
    $ doneProneAnalhappyFast = True
    p "Damn... "
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    $ button_screens("vprone_loop02","vprone_loop02_screen")
    "With a groan you speed up driving into Clementine."
    $ hNoise(2)
    p "Ahh... so good..."
    $ hText()
    "Clementine groans in agreement, squeaking as you pump into her."
    window hide
    pause 5
    window show
    $ hNoise(3)
    p "Ahh.. fuck... "
    $ slapLine()
    $ hText()
    $ hNoise(2)
    "The sound of slapping flesh mixes with the girls mewling as your dick digs inside her."
    $ hText()
    p "Ahh.. Ahhh..."
    window hide
    pause 5
    window show
    $ hNoise(2)
    p "Ahh... your pussy is amazing."
    $ hText()
    "Her head hangs loose as you bounce up and down on her."
    $ hNoise(2)
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_prone
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_happy_faster_repeat
        "[sd]":
            jump vprone_happy_repeat
        "[cp]":
            jump from_vag_prone



label vprone_happy_faster_repeat:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/prone/sound/prone_02.mp3" loop fadein 1
    p "Ahh... uh..."
    $ hText()
    $ nText()
    "Clementine gasps ragedly, her breath catching as you fuck her."
    window hide
    pause 5
    window show
    $ hNoise(2)
    p "Ahh.. uh..."
    $ nText()
    p "You like that?"
    $ hText()
    $ hNoise(2)
    p "Ah.. ah..."
    $ hNoise(1)
    p "Goddamn..."
    $ hText()
    $ hNoise(3)
    #cowgirl
    if posCount == 4 and abuse == 0:
        jump cowgirl_from_prone
    # cum flag
    if posCount == 6:
        jump cum_doggy_from_prone
    $ hide_overlay()
    menu:
        "[kg]":
            jump vprone_happy_faster_repeat
        "[sd]":
            jump vprone_happy_repeat
        "[cp]":
            jump from_vag_prone
