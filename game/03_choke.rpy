#From fours
label chokeFromFours:
    p "Ahh.. fuck!"
    "With a growl you shove Clementine forward."
    clem "Ah!"
    "She shrieks as you slide out of her."
    "You grab her foot, roughly dragging her back to you."
    clem "Ahh! Get off!"
    p "Shut up cunt!"
    scene turn_choke
    with dissolve
    "You snarl at her as you wrap a hand around her neck."
    p "Ahh yea..."
    "With your other hand you slide yourself back inside the girl."
    clem "Hnnk..."
    jump choke


#From prone
label chokeFromProne:
    p "Ngh!"
    "With a growl you slide back off the girl, leaving her flat on the bed."
    p "Not over yet slut.."
    scene turn_choke
    with dissolve
    "You reach out and grab her shoulder, rolling her over and clamping your hand around her throat."
    clem "Ngh!"
    p "Ah fuck!"
    "You slam your dick back in and Clementine grunts in pain."
    clem "Hurk..."
    jump choke


#From side
label chokeFromSide:
    p "Ahh!"
    "You drop her leg down and reach out, wrapping your hand around her throat."
    clem "Hnk!"
    "Clementine’s eyes flash wide as your fingers dig into her skin."
    p "Nggg fucking cunt!"
    clem "Hngh..."
    jump choke


#From missionary
label chokeFromMiss:
    p "Ngh fuck you whore!"
    "You reach out, wrapping your hand around Clementine’s neck."
    clem "Hngh!"
    "Her eyes widen as you dig into her flesh."
    p "Ahh... slut..."
    clem "Hngh..."


label choke:
    $ posCount += 1
    stop sound fadeout 0.5
    play sound "sex/choke/sound/choke_loop_01.mp3" loop fadein 1
    $ button_screens("choke_loop01","choke_loop01_screen")
    "Clementine claws at the air briefly."
    p "Fucking cunt..."
    "You tighten your grip and the girl grimaces."
    clem "Hngh..."
    $ rNoise(2)
    "Her lips peel back and her eyelids flutter as you press into her neck."
    p "Ah... ah... not yet cunt..."
    "You loosen your grip slightly and she shudders a gasping breath."
    clem "Nggh... hah..."
    p "Nhh. ah..."
    p "Like this slut? Like that dick?"
    clem "Ha... hnk... fuck you!"
    "Clementine croaks hoarsely."
    p "Hah.. ngh.."
    $ slapLine()
    "You grit your teeth and double down, driving deep inside her with each rough thrust."
    $ nText()
    window hide
    pause 5
    window show
    p "Ahh... fuck..."
    clem "Hng... urk!"
    "You slide your thumb up and down her neck, feeling the muscle twitching underneath."
    p "You like that cunt, maybe we take this through to the end?"
    clem "Hnnk..!"
    "Her eyes flash open as you tighten your grip."
    window hide
    pause 5
    window show
    p "Ah... hah..."
    clem "Hnn..."
    $ rNoise(1)
    "Clementine’s eyes tighten as she fights for breath."
    clem "Hnnnk... sto... stop..."
    "She croaks as you squeeze her neck."
    if posCount == 6:
        jump cum_missionary_norm_choke
    #keep bonin
    p "Huh? You want me to stop?"
    "You bring your other hand to her neck, squeezing the soft flesh."
    stop sound fadeout 0.5
    play sound "sex/choke/sound/choke_loop_02.mp3" loop fadein 1
    $ button_screens("choke_loop02","choke_loop02_screen")
    clem "Hnghe!!"
    "Her lips peel back and her face scrunches up as you choke the air out of her."
    p "You don’t tell me what to do cunt..."
    clem "Hnngh... hnnn..."
    "Clementine reaches up and grabs at your arms."
    clem "Hnnn!"
    "She tries weakly to pull your hands away."
    p "Ahh.... ngh... take it whore!"
    "Her resistance only spurs you on."
    clem "Hnn! Unh!"
    "Feeling her soft flesh give under your fingers just drives you on."
    "She changes to gripping one arm but still lacks the strength to peel your hands away."
    p "Ahh... fucking tight little slut.."
    clem "Nnn... Hnnngh!"
    window hide
    pause 5
    window show
    $ rNoise(1)
    $ slapLine()
    p "Ah... fuck.."
    clem "Nnnngh!  Hnn!"
    "Her eyes start to roll back in her head, gasping and spluttering as she fights for air."
    window hide
    pause 5
    window show
    p "Ah.... fuck..."
    clem "Ngg st... st..."
    "Clementine fights to stay conscious, jerking slightly as you continue to slam into her pussy."
    p "Hah... hah... hah...."
    "You suck air through your teeth, fixated on her twitching face."
    clem "Nhhhh... hhhhh..."
    "Gripping her neck tightly you feel the flesh give under your fingers."
    clem "Hhhh..."
    #cum jump
    if abuse >= s_limit:
        jump cum_choke
    jump cum_missionary_rough_choke
