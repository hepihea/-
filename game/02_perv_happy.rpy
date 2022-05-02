

label happy_perv_a:
    stop music fadeout 10
    clem "Sooo...."
    clem "What comes next?"
    "Clementine stretches back, dropping onto the bed and bringing her feet up to rest on the metal cross bar."
    $ hide_zoom_screens()
    scene ph_bedsit_01
    with dissolve
    "She sits on the bed, legs pressed together."
    clem "You want to look more or...?"
    scene ph_bedsit_flash
    "With a slight smile she swings her knees open, offering a glimpse of her pussy before closing them."
    menu:
        "Show me more...":
            jump happy_perv_b
        "You are going to suck my dick...":
            jump no_perv_bj

label happy_perv_b:
    stop music fadeout 10
    p "You are too perfect to rush this."
    p "I want to see more..."
    clem "Ahah"
    $ isZommed = "norm"
    $ hide_zoom_screens()
    scene ph_bedsit
    with dissolve
    show screen phBedSitScreen
    "With a laugh Clementine swings her legs open, her brown pussy exposed full to your sight."
    p "Haaa..."
    "You stare at her body, the girl taking pleasure in your obvious desire."
    clem "Think you like it now..."
    p "You're not wrong."
    clem "I can show you more..."
    "With that she lies back on the bed, shifting her feet to lift her hips up into the air."
    scene ph_spread_01
    with dissolve
    $ hide_zoom_screens()
    voice "perv_happy/sound/mast_01.mp3"
    clem "Ahh..."
    "Clementine brings her hands up to her thighs, pulling her legs apart."
    voice "perv_happy/sound/mast_02.mp3"
    clem "Mmmm"
    "She moans lightly as her lower lips separate, peeling away from each other slightly."
    voice "perv_happy/sound/mast_03.mp3"
    clem "Ah..."
    "Her hands rub at her thighs, legs trembling slightly from supporting her weight."
    clem "More?"
    "She moans with a plaintive edge to her voice."
    $ isZommed = "norm"
    scene ph_bedspread
    with dissolve
    show screen phBedSpreadScreen
    "Clementine slides her hands across her mounds and her fingers probe down, pressing at her soft flesh."
    "She presses into the edges of her pussy and peels back the lips, showing you her slightly pink insides."
    voice "perv_happy/sound/mast_04.mp3"
    clem "Mmmm.... ah"
    "She prods and massages her labia as she looks at you, her breathing coming heavier."
    "After a moment her right hand moves to her bud, pressing into it with a circular motion, her head falling back on the bed."
    $ hide_zoom_screens()
    #scene mast_intro
    show mastloop_body
    with dissolve
    show screen ph_face_focus
    play sound "perv_happy/sound/mast_01_loop.mp3" loop
    clem "Ngh..."
    clem "Ahh.."
    "She rubs at her pussy, breathing shallowly."
    clem "Hah...."
    "You watch as she presses at her clit."
    clem "Mmm..."
    "Clementines breath catches for a moment."
    clem "Oooooh"
    clem "Like what you see now...?"
    "You lick your lips before answering hoarsely."
    p "Yeah..."
    clem "Hehe.."
    "She gigles and you can see a sheen appearing on her sex."
    clem "Mmmmmm..."
    stop sound fadeout 0.5
    "She groans and slides her hand down, parting her lips and slipping fingers into her hole."
    $ hide_overlay()
    play sound "perv_happy/sound/mast_transition.mp3"
    window hide
    show movie
    play movie "perv_happy/vid/transition.webm" noloop
    with dissolve_set
    pause 4.93
    show mast_part2
    window show
    play sound "perv_happy/sound/mast_02_loop.mp3" loop
    clem "Hah..."
    clem "Oohh.... ah"
    "Clementine starts to work her fingers in and out of her pussy."
    clem "Mmm... {i}{{ squish... }{/i}"
    "You can hear the soft squelch of liquid as she works her wet hole."
    clem "Ah... ah..."
    clem "Mmmm..."
    "Her breathing comes heavier as she fingers herself."
    p "So hot..."
    "You murmur as you pull your shirt off over your head"
    clem "Shit... ahn..."
    play sound "perv_happy/sound/mast_cum.mp3"
    "Her butt clench and unclench as she buck her hips."
    clem "Nghhh!"
    "Clementines body tightens for a moment and she pulls her fingers from her pussy."
    stop sound fadeout 0.5
    queue sound "perv_happy/sound/after_cum.mp3"
    scene after_mast_01
    with flash_sharp
    clem "Hah.... Hah..."
    "She stays tensed for a moment before relaxing to the bed."
    scene after_mast_02
    with dissolve
    "She gasps as she relaxes back to the bed, looking up at you."
    clem "Hehe..."
    clem "I came a little!"
    "Clementine flashes a smile through hooded eyes."
    clem "But I want to save the real thing..."
    scene after_mast_03
    with dissolve
    "She sits up, chewing on her lower lip."
    clem "So what's next?"
    menu:
        "I am going to fuck your face...":
            jump ff_from_happy
        "Suck my dick...":
            jump happy_to_bj
        "Show me your ass...":
            jump happy_ass


label happy_ass:
    p "Let me see that ass..."
    "Clementine flashes a smile."
    clem "Ok.!"
    $ isZoomed = "norm"
    scene perv_ass_norm
    with dissolve
    show screen pervAssScreen
    "She quickly rolls over onto all fours and pushes her ass back at you."
    clem "Ah..."
    "Clementine looks at you over her shoulder as she sways her hips."
    clem "Mmmm..."
    clem "Hah.."
    $ hide_zoom_screens()
    scene pre_happy_finger
    with dissolve
    "She pants lightly and reaches a hand back between her legs."
    show ass_finger
    with dissolve
    play sound "perv_happy/sound/mast_finger.mp3" loop
    clem "Ahhh.. ah..."
    "Dipping her finger in and out of her pussy she moans."
    clem "Ooooh.."
    clem "Mmmm... feels so good..."
    clem "Hah...."
    show finger_deep
    with dissolve
    "She slides her finger deep into her pussy one last time, probing her own flesh."
    clem "Mmmm..."
    "Before sliding it back out of her wet pussy."
    $ renpy.scene()
    scene pre_happy_finger
    with dissolve
    stop sound fadeout 1.5
    clem "Ahhh.... hehe..."
    scene perv_norm_lie01
    "Clementine rolls back over, onto her back, legs parted."
    clem "Time for the main course?"
    menu:
        "First suck my dick...":
            jump happy_to_bj
        "Time to fuck...":
            #placeholder
            jump prefuck



label mast_body:
    scene mastloop_body
    with fade
    hide screen ph_body_focus
    show screen ph_face_focus
    return

label mast_head:
    scene mastloop_face
    with fade
    hide screen ph_face_focus
    show screen ph_body_focus
    return
