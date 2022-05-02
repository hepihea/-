label cum_anal_from_kneel:
    p "Ahh.... fuck..."
    "You drive forward, shoving Clementine into the mattress."
    jump cum_anal_norm

label cum_anal_from_kneel_rough:
    p "Ah cunt!"
    "You growl, driving shoving the girl forward."
    jump cum_anal_rough

label cum_anal_from_prone:
    p "Ah.... "
    "You raise up letting Clementine bring her hips up slightly."
    jump cum_anal_norm

label cum_anal_from_prone_rough:
    p "Ahh... fuck!"
    jump cum_anal_rough


label cum_anal_norm:
    clem "Ngh!"
    stop sound fadeout 0.5
    play sound "sex/cum_anal/sound/cum_anal_intro.mp3" loop fadein 1
    $ button_screens("anal_cumintro", "anal_cumintro_screen")
    "Clementine gasps as you push her head down onto the bed."
    p "Oh fuck... get ready for it..."
    clem "Ah... nnn..."
    "You press her down, slapping into her cheeks as you feel your release build."
    clem "Nnnn.... hnnn..."
    p "Ah... here it comes!"
    clem "Ahhh!"
    "With a grown you drive deep in her ass and empty your balls."
    $ hide_overlay()
    window hide
    stop sound fadeout 0.5
    play sound "sex/cum_anal/sound/cum_anal_actual.mp3" fadein 1
    queue sound "sex/cum_anal/sound/cum_anal_outro.mp3" loop
    scene  anal_cum with flash_sharp
    pause 2.7
    window show
    scene anal_cumoutro with dissolve
    p "Ahhhh..."
    $ button_screens("anal_cumoutro", "anal_cumoutro_screen")
    clem "Mmhh... hnnn..."
    "Clementine whimpers softly as you relax, dick still buried in her ass."
    clem "Ah... ah..."
    p "Oooooooh..."
    "You suck air, relishing the feel of her insides."
    clem "Nnnnn!"
    stop sound fadeout 8
    #image
    $ hide_overlay()
    scene anal_end_01
    with dissolve
    "Slowly you slide your dick out, popping free with a wet suck."
    clem "Ahh.. hah..."
    "Clementine lies on the bed, chest heaving as you stare down at the cum flowing from her ass."
    p "Man... that was good..."
    clem "Hnnnn..."
    scene anal_end_02
    with dissolve
    "The girl doesn’t reply as she lifts her head from the mattress."
    "You step back from the bed, grabbing your clothes."
    clem "Hnn... nnn..."
    "Clementine starts to sniffle, shoulders shaking slightly."
    p "Really? That didn't seem like your first time getting your ass filled."
    clem "Fuck you..."
    "She murmurs in a small voice and rolls onto her side."
    scene anal_end_03
    with dissolve
    p "Whatever, maybe next time you will get it in your pussy?"
    clem "..."
    "Clementine doesn't respond, and with your clothes back on you turn to the door."
    scene anal_end_04
    with dissolve
    "You give one last look at the form on the bed, before swinging the door shut."
    scene door1
    with dissolve
    "With the memories of her tight ass running through your head you walk back down the dim corridor."
    jump the_end

label cum_anal_rough:
    clem "Ahh!"
    stop sound fadeout 0.5
    play sound "sex/cum_anal/sound/cum_anal_intro.mp3" loop fadein 1
    $ button_screens("anal_cumintro", "anal_cumintro_screen")
    "Clementine cries out as you shove her head down onto the bed, wrapping your fingers in her hair."
    p "Nnn! Ready for some cum slut?"
    clem "Ah... fuck you!"
    "She cries out as you pound into her ass feeling your release build."
    clem "Ahh... uhh..."
    p "Here is comes cunt!"
    clem "Nooo!"
    "With her final wail you sink deep into her ass, pumping her full."
    $ hide_overlay()
    window hide
    stop sound fadeout 0.5
    play sound "sex/cum_anal/sound/cum_anal_actual.mp3" fadein 1
    queue sound "sex/cum_anal/sound/cum_anal_outro.mp3" loop
    scene  anal_cum with flash_sharp
    pause 2.7
    window show
    scene anal_cumoutro with dissolve
    p "Ahhhh.....yeeeah..."
    $ button_screens("anal_cumoutro", "anal_cumoutro_screen")
    clem "Hnnn... sniff...."
    p "Fuck...."
    "You slide in and out, draining the last of you cum inside her."
    clem "Nnn... hnnnn..."
    #image
    stop sound fadeout 8
    #image
    $ hide_overlay()
    scene anal_end_01
    with dissolve
    "Clementine groans as you slide your dick out of her ass."
    p "Fuuuck... that’s a nice ass..."
    "You groan as your dick pops free, cum oozing out her rear."
    clem "Hnn... nnnh..."
    p "Shit girl are you crying?"
    "Clementine’s shoulder shake as she sniffs quietly."
    p "Would think you are used to getting your ass filled!"
    "With a laugh you step back, admiring the result of your efforts."
    clem "... fuck you..."
    scene anal_end_02
    with dissolve
    "She props herself up on her elbows, cum still bubbling out of her ass."
    p "Nah slut that was you, just look at that mess!"
    clem "Hnn... hnn..."
    scene anal_end_03
    with dissolve
    "She rolls over onto her side, hugging her stomach."
    p "Look on the bright side, no chance of a whore baby now!"
    clem "..."
    "Clementine ignores you, turning her head away as you pull your shirt on."
    scene anal_end_04
    with dissolve
    "You walk to the door, taking the time to give the girl one last look."
    p "Hah... don’t be too sad girl, maybe next time we can fill that pussy instead?"
    scene door1
    with dissolve
    "With that you pull the door closed, and walk off down the corridor."
    jump the_end
