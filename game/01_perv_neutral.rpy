
define pn_legsup = False
define pn_legup = False
define pn_ass = False



label perv_neutral:
    p "Sit down..."
    "The girl glowers at you a moment before sitting down on the edge of the bed."
    $ hide_zoom_screens()
    scene perv_norm_sit01
    with dissolve
    clem "..."
    p "Open your legs."
    "You pull your shirt off as she stares at you, before slowly swinging her legs open, eyebrows arching slightly."
    clem "Better?"
    p "Hmph.."
    "You stare at her for a moment, looking over her supple body."
    clem "... hnn..."
    p "Lie back..."
    scene perv_norm_lie01
    with dissolve
    "Clementine holds your gaze as she leans back on the bed."
    clem "{i}{{ sniff... }{/i}"
    "She sniffs slightly as her gaze drops, breaking eye contact."
    p "Nice.."
    clem "..."
    jump pn_view_select

label pn_view_select:
    $ hide_overlay()
    if not pn_legsup or not pn_legup or not pn_ass:
        menu:
            "Hold up your legs..." if not pn_legsup:
                jump perv_n_legsup
            "Spread your pussy..." if not pn_legup:
                jump perv_n_leg_lift
            "Show me your ass..." if not pn_ass:
                jump perv_n_ass
    else:
        jump pn_continue


label perv_n_legsup:
    $ pn_legsup = True
    p "Lift your legs."
    "To stress your point you reach down and grab one of her feet, pushing it upwards."
    clem "Uhhh..."
    $ isZoomed = "norm"
    $ hide_overlay()
    scene legsup_norm
    with dissolve
    show screen pervLegsUpScreen
    "Clementine rocks backward, bringing her knees to her chest and gripping her thighs."
    clem "Huh..."
    "She looks down to the side as you study her dark lips."
    p "Very nice..."
    jump pn_view_select

label perv_n_leg_lift:
    $ pn_legup = True
    p "Show me your pussy..."
    clem "Hnn..."
    "Clementine rolls onto her side, legs dangling off the bed."
    $ isZoomed = "norm"
    $ hide_overlay()
    scene legup_norm
    with dissolve
    show screen pervLegUpScreen
    "She looks away as she lifts her leg."
    "Her pussy splits as she reaches around and grips her thigh, breathing heavily."
    clem "Hmm... hah..."
    "You lean in close, noticing the twitch of her sex as she breathes."
    p "So, still nice and tight down there?"
    "You see her brow knit as she frowns."
    clem "{size=-10}Fuck you...{/size}"
    "You smile slightly at her discomfort."
    p "Sorry did you say something?"
    "Clementine looks back at you and scowls."
    clem "No..."
    p "Thought not."
    p "Doesn't matter I will find out soon enough."
    clem "... "
    "She says nothing in response."
    jump pn_view_select




label perv_n_ass:
    $ pn_ass = True
    p "Turn over..."
    "Clementine wordlessly turns onto all fours, lifting her ass up."
    $ isZoomed = "norm"
    $ hide_overlay()
    scene perv_ass_norm
    with dissolve
    show screen pervAssScreen
    clem "Hah..."
    "She kneels awkwardly as you study her smooth ass."
    p "So you been fucked in the ass yet?"
    clem "..."
    "She doesn't respond but you can feel her disapproval."
    p "Hah well doesn't matter."
    p "Maybe if you play your cards right you'll get a fat dick in there too."
    "Clementine glances over her shoulder at you, scowling."
    p "Don't get mad at me, I made sure that was on the list of things I can do..."
    jump pn_view_select



label pn_continue:
    $ hide_zoom_screens()
    scene perv_norm_sit01
    with dissolve
    "Clementine slides back the the edge of the bed."
    p "Alright then enough looking, let’s get to the tasting."
    menu:
        "You are going to blow me...":
            jump bj_intro
        "I am going to fuck your face...":
            jump ff_from_neut
        "Time to fuck...":
            #placeholder
            jump prefuck
