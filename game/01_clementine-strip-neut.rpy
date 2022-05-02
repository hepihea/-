



#neutral route


#standing up off bed intro
label undress_01a:
    p "Stand up!"
    "You bark at the girl, who visibly flinches at your voice."
    show camera_on
    "You reach over and turn on the camera."
    hide camera_on
    scene off_bed
    "Clementine slowly rises from the bed and stands in front of you, eyes downcast."
    p "You know what comes next."
    scene stand_pre_strip
    jump undress





#turned on camera intro
label undress_01b:
    p "You know what comes next."
    "At your statement Clementine turns away slightly, eyes downcast."
    scene stand_pre_strip
    jump undress



label undress:
    p "Start with the top."
    "Clementine looks up, a small spark of defiance flares in her eyes."
    if abuse > 3:
        "But only for a moment before she reluctantly grips the hem of her loose shirt."
    else:
        "You think you also see a hint of... disappointment? But it passes quickly as Clementine grips the hem of her shirt."
    "With little fanfare she pulls her shirt up over her head, exposing her soft dark torso."
    scene top_off_trans
    "Her top and hands drop down as she stares at you, a look of resignation in her eyes."
    $ isZoomed = "norm"
    $ hide_zoom_screens()
    scene top_off
    show screen topOffScreen()
    clem "Happy?"
    "She asks in a dead tone, but you don’t really listen."
    #Only mean naked if she was slapped and told to strip
    if abuse > 3:
        jump naked_mean
    else:
        jump naked_normal

label naked_mean:
    "You drink in her supple body, developing breasts just starting to ripen."
    p "Mmmm"
    $ hide_zoom_screens()
    scene top_off_cover_a
    "A low growl from your throat causes a flash of worry on her face and for a moment her hand rises to cover her breasts."
    clem "Hmm...   {i}sniff{/i}"
    $ isZoomed = "norm"
    scene top_off
    show screen topOffScreen()
    "Before falling back to her side."
    p "Nice..."
    "You drink her in for a moment longer before reaching up and pulling your own shirt off."
    "Stepping in you reach for her, stopping short of touching as Clementine retreats slightly from your hands."
    p "Next part..."
    $ hide_zoom_screens()
    scene shoes_off_a
    with dissolve
    "You stare at her hungrily as she sits on the bed."
    scene shoes_off_b
    with dissolve
    "Clementine reaches down and fumbles with the buckles on her boots."
    p "Idiot..."
    "You snarl as you kick off your own shoes."
    p "Who cares what shoes you wear I won’t see them when you are ass up getting fucked."
    clem "huh.."
    "She catches her breath slightly as one boot comes free."
    p "Quickly..."
    scene shoes_off_c
    "The other boot surrenders much more easily and joins its pair on the floor."
    scene top_off_sad
    "Clementine stands back up, a slight tremble rippling across her chest."
    p "Well?"
    "You bark at her, breathing heavily."
    "Clementines hands move to her waist band and with a push slides her jeans off her hips"
    scene pants_strip
    "She pushes her pants down over her knees and to the floor, sliding her feet out of the legs before standing back up, sniffling slightly"
    $ isZoomed = "norm"
    scene pants_off
    show screen pantsOffScreen()
    clem "{i}{{ sniff... }{/i}"
    jump post_strip


label naked_normal:
    "You stare at her body, noting the developing breasts and curve of her hips."
    "Clementine says nothing for a moment, regarding you with dead eyes."
    clem "Shoes?"
    "She asks dully, arms hanging at her sides."
    p "Hmph"
    $ hide_zoom_screens()
    scene shoes_off_a
    with dissolve
    "You grunt assent and after a moment she sits on the bed."
    scene shoes_off_b
    with dissolve
    "Clementine reaches down, unbuckling her shoes mechanically."
    scene shoes_off_c
    with dissolve
    "She pulls the left off then the right and stands back up."
    $ isZoomed = "norm"
    scene top_off
    show screen topOffScreen()
    clem "...."
    "She says nothing as you both stare at each other."
    "While holding her gaze you kick off your own shoes before gesturing at the girl."
    clem "Hmph"
    "Clementine grunts softly, a slight curl in her top lip as she reaches for the waist of her jeans."
    $ hide_zoom_screens()
    scene pants_strip
    "In one motion she slides her pants to the floor, stepping out of the legs before straightening infront of you."
    $ isZoomed = "norm"
    scene pants_off
    show screen pantsOffScreen()
    clem "...."
    jump post_strip


label post_strip:
    "You can almost feel Clementine’s disapproval as you stare greedily at her body."
    p "Nice.."
    $ hide_overlay()
    menu:
        "Show you her body...":
            jump perv_neutral
        "I am going to fuck your face...":
            jump ff_from_neut_standing
        "Suck my dick":
            jump bj_intro
