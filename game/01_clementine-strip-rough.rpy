# Rouigh strip


label strip_her:
    $ hide_zoom_screens()
    "You loom over the slight form on the bed, blood boiling."
    p "You aren't here to talk back slut!"
    "Her eyes well with moisture."
    clem "Please..."
    scene rough_strip_hand_out
    with dissolve
    "She thrust out her hand as you move close."
    p "Bitch!"
    scene rough_strip_hand_away
    with dissolve
    "You slap her hand out of the way."
    clem "Ahh!"
    scene hair_grab
    with dissolve
    "You reach and grab a fist full of her hair, yanking her to you."
    clem "Nooo!"
    "The girl shrieks, gripping at your hand as she is lifted off the bed."
    clem "Aaahhh!"
    p "Like I said, I payed for whatever I want whore..."
    menu:
        "Prove your point...":
            jump slap_two
        "Strip her...":
            jump force_strip


label slap_two:
    $ abuse += 2
    play audio "audio/slap_.wav"
    scene rough_slap
    with flash_sharp
    "You draw back your other hand and bring it sharply across Clementine’s cheek."
    scene after_slap
    with dissolve
    clem "Ah... Fuck!"
    "Her chest starts to heave as she fights back tears."
    clem "huh... {i}{{ sniff... }{/i}"
    show camera_on
    "You reach over and turn on the camera, not wanting to miss any of the show."
    hide camera_on
    p "Now that that is out of the way..."
    jump force_strip




label force_strip:
    if abuse == 5:
        p "Let’s see what you are hiding under those rags."
    else:
        p "Now... let's see what you are hiding under those rags."
    scene rough_shirtoff_01
    with dissolve
    "You reach down and grab the base of her shirt."
    "Clementine offers little resistance as you pull the cloth up over her head."
    clem "Hmm..."
    $ isZoomed = "norm"
    $ hide_zoom_screens()
    scene top_off_rough
    show screen roughTopOffScreen()
    "As you throw the shirt into the corner she looks away, crossing her arms over her belly."
    clem "{i}{{ huh... }{/i}"
    "Ignoring her sniffling you slip off your own shoes and stand over the young girl."
    p "Time for the rest..."
    clem "Wha...?"
    "She starts to respond but you put a hand on her shoulder and shove her back onto the bed."
    $ hide_zoom_screens()
    scene bed_push_01
    with dissolve
    clem "Uhh..."
    "Clementine rolls over as you move next to her."
    p "Lets get you out of these..."
    scene bed_push_02
    with dissolve
    "She looks over her shoulder as you kneel on the bed by her legs."
    p "Let’s start with these."
    scene rough_shoe_off_01
    with dissolve
    "You reach and grasp her shin tightly, yanking her leg to you."
    clem "Ahh.."
    "She tries to pull away but you are too strong and hold her firmly."
    "Reaching out you grab her boot and give it a sharp tug."
    clem "Ow!"
    "Clementine cries out as you yank at her boot, slowly working it off over her foot, scraping skin away."
    clem "Argh... {i}{{ hngh... }{/i}"
    scene rough_shoe_off_02
    with dissolve
    "The boot finally pops free of her foot and reach out and grab the other leg."
    clem "Hah!"
    "Again you twist at her foot, ignoring the boot buckles."
    p "Dammit!"
    "You curse as with a final pull the boot comes free."
    p "Why the hell would you wear those anyway!"
    clem "Mph..."
    "She whimpers as you move behind her."
    scene rough_pants_off_01
    with dissolve
    "Reaching out you grab the hem of her jeans and yank."
    clem "No! Stop!"
    "Clementine shrieks and tries to scamper away, but with a firm grip on her waist her legs just slide on the mattress."
    clem "Get the fuck off me!"
    p "Hah!"
    scene rough_pants_off_02
    with dissolve
    "You laugh derisively as with a hard pull you drag her pants off her hips."
    clem "Hngh..."
    "With a final pull you peel her pants off her legs and throw them into the corner."
    $ isZoomed = "norm"
    $ hide_zoom_screens()
    scene naked_rough
    show screen roughNakedScreen()
    p "Oooh..."
    "You exhale sharply at the sight of Clementine lying before you."
    clem "Ngh..."
    "Her shallow breathing comes in gasps as you stare at her perfect ass."
    p "Yeah this is going to be fun..."
    hide screen roughNakedScreen
    $ hide_overlay()
    menu:
        "I am going to fuck your face...":
            jump ff_from_rough
        "Suck my dick whore...":
            jump bj_rough_intro
