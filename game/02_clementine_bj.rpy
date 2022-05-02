
#from perv_happy full sequence
label happy_to_bj:
    p "Time to suck my dick."
    $ abuse = abuse +1
    "Clementine’s smile wavers and you notice a slight tightening around her eyes."
    clem "... Ok"
    scene kneel_01
    with dissolve
    "Without another word she slides down onto her knees in front of you"
    "She reaches out and unbuttons your pants, pulling them down."
    "Her smile now gone completely Clementine stares at your dick."
    scene kneel_02
    with dissolve
    p "Well?"
    jump bj


label no_perv_bj:
    p "Time to suck my dick."
    $ abuse = abuse +1
    "Clementine’s expression doesn't change but you notice a slight tightening of her eyes."
    clem "Ok..."
    "You notice the playful tone has gone out of her voice as she regards you."
    p "Get on your knees..."
    scene kneel_01
    with dissolve
    "You pull your shirt off as she slides off the bed and kneels down, looking up."
    p "Your mouth looks so good..."
    "Hands fumble momentarily at your waist as you unbutton your jeans, and push them to the floor."
    scene kneel_02
    with dissolve
    clem "Hmm..."
    "She regards your semi erect dick impassively."
    p "Well? Get to it..."
    jump bj

#From all neutral points
label bj_intro:
    if abuse > 3:
        jump  bj_rough_intro
    p "Alright on your knees..."
    "Clementine scowls at you slightly while you undo the button on your jeans."
    clem "Huh..."
    scene kneel_01
    with dissolve
    "As you push down your pants she drops to her knees, regarding your hardening dick dispassionately."
    p "Well? Get to it..."
    scene kneel_02
    with dissolve
    "She stares at your cock indifferently."
    p "What’s the problem? Never seen one this big before."
    clem "Hngh..."
    "She snorts, rocking slightly."
    clem "Yeah that’s it..."
    p "Well? Get to it..."
    jump bj


#from force strip
label bj_rough_intro:
    p "Time to suck a dick slut"
    "Clementine glares at you as you unbutton your jeans."
    p "What are you waiting for an invitation? On your knees before I choke you with it."
    "You drop your jeans to the floor."
    p "Well? Get to it..."
    clem "..."
    scene kneel_02
    with dissolve
    "She stares at you for a moment, consternation etched on her face before kneeling down."
    jump insult_bj


label bj:
    $ abuse += 1 # no matter what make her suck yo dick no good end
    stop music fadeout 10
    scene kneel_03
    with dissolve
    "Clementine continues to stare at your hardening dick."
    p "You know it doesn’t suck itself..."
    clem "Huh..."
    "She takes a deep breath and reluctantly reaches out wrapping her small hands around your shaft."
    scene hj_start
    with dissolve
    p "Oooh"
    "The girl looks up at you, squeezing at your cock."
    "Her hands are soft and warm around your now hard dick"
    p "Ah.."
    "She draws her hand up slowly, enveloping your head."
    clem "Mmm.."
    "Slowly at first then picking up speed she starts to jerk you off."
    $ button_screens("hj_pov","hj_pov_screen")
    #call screen_manager pass "hj_pov", "hj_pov_screen"
    #show hj_pov
    #show screen hj_pov_screen
    play sound "blowjob/sound/bj_hj_loop.mp3" loop
    clem "Hah..."
    p "Ohhh..."
    p "Your hands are great..."
    "She looks up while she jerks you and cocks an eyebrow slightly."
    clem "Thanks?"
    "You ignore the sarcasm, focusing on the feel of her hand."
    p "Ahh..."
    clem "Hah..."
    "Clementine holds your gaze as her hand moves up and down."
    p "Ah..."
    "Staring at her you feel a familiar urge and realise you need to get to main course."
    p "Ahh .... now suck it..."
    clem "Ohhhh..."
    "She coo's softly, still jerking you off."
    p "Fuck..."
    p "I said suck it!"
    "Clementine frowns for a moment, her hand massaging your cock head."
    "Then in one motion leans forward, and slides her lips over your dick."
    clem "Ahhh..."
    stop sound fadeout 0.5
    play sound "blowjob/sound/bj_norm_loop.mp3" loop
    $ button_screens("bj_pov","bj_pov_screen")
    p "Woooo..."
    "You groan deeply as her warm mouth envelops you."
    p "Shiiiit...."
    clem "Mmmph  {i}{{ schlup... } {/i}"
    "Her head bobs up and down on your shaft."
    "You can feel her tongue as it flicks across your head."
    p "Jesus..."
    p "At least you can suck a cock."
    clem "Mmmm"
    clem "Mph"
    clem "{i}{{ slurp....    schlup {/i}.... } hah..."
    "You can hear her sucking air through her nose as her lips form a vacuum."
    clem "Mmmph..... mmmmm "
    p "Fuck..."
    "You look down at her head bobbing on your dick."
    p "Yea.... suck my cock..."
    clem "Mmm... {i} mmph {/i}"
    "You can feel the soft flesh of her cheek brushing your dick as she tilts her head while her tongue continues to flick around your tip."
    p "Ohh.... ugggh"
    $ button_screens("bj2_pov","bj2_pov_screen")
    stop sound fadeout 0.5
    play sound "blowjob/sound/bj_norm2_loop.mp3" loop
    "Without waring she speeds up, her head dropping even further along your shaft."
    clem "Hmmph..."
    p "Ahhhh...."
    "Her hand starts to work along your dick, fingers stroking at the base of your cock."
    clem "Mmmf.... mmmf"
    p "Oh fuck... "
    clem "{i}{{ slurp...{/i}  {i}slurp... }{/i}"
    p "Hah.... hah..."
    "You gasp for air as the girl sucks you, her clearly practiced technique bringing you rapidly to the edge."
    clem "Mmm .... a... hnn...."
    "Clementine moans and her chest heaves as she fights for air, her mouth full of dick."
    clem "Mmmph... {i}{{ schlup... }{/i}"
    "You can feel your head touching the back of her throat."
    p "Hoooo..."
    "Staring down at her sucking you can feel the end approaching."
    $ hide_overlay()
    menu:
        "Warn her...":
            jump face_cum
        "Cum in her throat...":
            jump mouth_cum





label face_cum:
    p "Oh fuck..."
    p "That feels so good.... I can't last much longer."
    clem "Mmmmm..."
    "She groans in response and her tongue redoubles its efforts."
    p "Oh fuck here it comes..."
    p "Uuuuugh!"
    "You feel your balls tighten as a wave of cum rushes towards release."
    clem "Mmm!"
    "Clementine quickly pulls her head off your dick and closes her eyes, looking away."
    $ hide_overlay()
    stop sound fadeout 0.5
    play sound "blowjob/sound/bj_facial.mp3"
    queue sound "blowjob/sound/bj_facial_01.mp3"
    # Awaiting sound
    #queue sound
    window hide
    show movie
    play movie "blowjob/vid/bj_face_cum.webm" noloop
    pause 2.15
    scene face_cum_01
    with flash
    window show
    clem "Mmmph!"
    p "Ahhhh"
    "The girl stays frozen, your cum dripping down her cheek and chest."
    clem "Nnngh..."
    p "Damn you can suck a dick girl."
    clem "Nnn..."
    scene face_cum_02
    with dissolve
    "Eyes tight she reaches up and claws at her cheek, scraping the cum off her skin."
    voice "blowjob/sound/bj_facial_03.mp3"
    clem "Hnnn... hnn..."
    "She wipes at her face until she has most of your cum in her hand."
    scene face_cum_03
    with dissolve
    voice "blowjob/sound/bj_facial_02.mp3"
    clem "Ha..."
    "Clementine looks up at you, almost hyperventilating."
    p "Shit girl I think you might have a problem..."
    p "Surely you are used to a little cum on your face by now."
    clem "N.... yeah .... sure..."
    "Her breathing slowly returns to normal as she unclenches her fist."
    scene face_cum_04
    with dissolve
    clem "Thanks for warning me at least..."
    p "Yeah sure whatever... I guess..."
    "She holds your gaze for a moment, her hand lightly on your leg, before standing back up."
    jump bj_end_label


label mouth_cum:
    p "Oooo shit..."
    p "Girl.... hah.... your mouth..."
    clem "Mmm.... mmm..."
    "You can feel your balls tighten as her mouth works your dick."
    clem "Mmf... {i}slurp{/i}"
    p "Uuuuuuh"
    "You groan as you feel your balls twitch and you reach out, grabbing Clementine’s hair."
    clem "Nnnggghgh!"
    "You can feel her shriek as you grab her head, the vibrations in her mouth pushing you over the edge."
    p "Oooooooh"
    "With a groan you unload into the back of her throat."
    $ hide_overlay()
    stop sound fadeout 0.5
    play sound "blowjob/sound/bj_cum.mp3"
    queue sound "blowjob/sound/bj_drain_loop.mp3" loop
    window hide
    show movie
    play movie "blowjob/vid/bj_mouth_cum.webm" noloop
    pause 4.11
    scene mouthcum2
    window show
    "You can feel Clementine struggling as you hold her head on your dick."
    clem "Mngh!"
    p "Oooooo...."
    "You drive your dick in again and again, draining every drop into her mouth."
    clem "NNNNGH!"
    p "Yeeeah...."
    "With a groan you finally release her head and she snaps backwards off your dick."
    scene mouth_cum_01
    with dissolve
    stop sound fadeout 0.5
    #Awaiting audio
    play sound "blowjob/sound/bj_bubbling.mp3"
    clem "Eeeeeeee!"
    "She stares at you, shaking violently as cum bubbles out of her mouth and trickles down her chin."
    p "Shiiiiit girl that was great."
    play sound "blowjob/sound/bj_bubbling_01.mp3"
    clem "Hnnnnng!"
    "With a final convulsion she drops to her knees."
    scene mouth_cum_02
    with dissolve
    play sound "blowjob/sound/bj_vomit.mp3"
    clem "Huuuuurgh!"
    "With a heave she empties her stomach on the floor, spit and cum splashing onto the carpet."
    p "Holy shit!"
    clem "Hnnnng!"
    "Clementine retches spitting cum and saliva onto the ground, shaking violently."
    clem "Haaaa.... hnnnn..."
    "Finally her retching subsides and she starts to breathe again."
    scene mouth_cum_03
    with dissolve
    clem "You asshole!"
    "She shrieks at you."
    p "Whoa now slut...."
    clem "You trying to fucking choke me?"
    p "Well thats new, a whore that can’t stand the taste of cum!"
    scene mouth_cum_04
    with dissolve
    "Clementine rises from the floor, propping herself on the bed."
    clem "Taste doesn't have anything to do with it when you stick your dick down my throat!"
    p "Well too fucking bad?"
    p "This might come as a shock but I didn’t pay to hear your opinions about choking on dick."
    p "I paid to shove my cock down your throat until you pass out if I feel like it."
    clem "..."
    "She scowls at you silently, jaw flexing as she clenches her teeth."
    "Finally she seems to calm down."
    clem "Whatever, just get the rest of this over with."
    "With that she stands back up, glaring at you."
    jump bj_end_label

label insult_bj:
    stop music fadeout 10
    p "I said suck slut!"
    "Clementine flinches at your voice before quickly leaning forward and taking your dick in her mouth."
    play sound "blowjob/sound/bj_norm2_loop.mp3" loop
    $ button_screens("bj_pov","bj_pov_screen")
    p "Fuck yeah..."
    clem "Mmf... {i}{{ slurp... }{/i}"
    "She bobs up and down on your cock mechanically."
    clem "Mmmf..."
    clem "Mmm..."
    p "Fuck your mouth is so soft..."
    p "Better not get any teeth in there whore."
    clem "Ngh..."
    p "Ahhh..."
    p "Shit at least you can suck a dick slut...."
    clem "{i}{{ schlurp.... suck... }{/i}"
    "You tilt your head back, enjoying the sensation of her warm mouth."
    clem "Mmm..."
    p "Dont just suck it, let me feel some tongue whore..."
    clem "Nnn..."
    "You feel her tongue start to flick over your head."
    p "Ahh thats more like it..."
    clem "{i}{{ slurp... slurp... }{/i}"
    p "Ahh fuck, you slut!"
    "You reach forward and wrap your fingers into Clementine’s hair, pulling her down onto your dick."
    $ button_screens("bj_R_pov","bj_R_pov_screen")
    clem "Mmmmm!"
    p "Ahh... get it in there cunt!"
    "You yank her head up and down along your cock."
    p "Nnnng... fuck..."
    clem "Mmm... nggh...!"
    p "Suck it whore..."
    clem "{i}{{ hurk... schlup... }{/i}"
    "You grip Clementine’s hair tightly as you pump into her face."
    p "How many dicks you sucked slut?"
    clem "Hnnn..."
    clem "Ngh..."
    "You feel the end approaching as you turn and twist her head."
    p "Get ready for it slut..."
    clem "Mmmmmgh!"
    "She starts to buck on your cock, trying to pull away but you hold firmly too her head."
    p "Oh fuck yeah...."
    "With a groan you empty your balls down her throat."
    $ hide_overlay()
    stop sound fadeout 0.5
    play sound "blowjob/sound/bj_cum.mp3"
    queue sound "blowjob/sound/bj_drain_loop.mp3" loop
    window hide
    show movie
    play movie "blowjob/vid/bj_R_cum.webm" noloop
    pause 2.19
    scene mouthcum2
    window show
    clem "Hnnnnn!"
    p "Fuuuuuck..."
    "You hold tightly to her hair as you finish down her throat, her tongue thrashing as she tries to get you out of her mouth."
    clem "Nnnnnnn!"
    p "Oooooooh..."
    "Clementine pushes at your hips trying to get you out of her, chest heaving."
    p "Nggg... stop that..."
    "You push hard into her face and you can hear her desperately sucking air in through her nose."
    clem "Mmmfm... Mmmm!"
    "You hold a moment longer before releasing your hand from her head."
    scene mouth_cum_01
    with dissolve
    stop sound fadeout 0.5
    play sound "blowjob/sound/bj_bubbling.mp3"
    queue sound "blowjob/sound/bj_bubbling_01.mp3"
    clem "Uuuuuuuun!"
    "She jerks back off your dick and makes an agonized mewl, sucking air as cum bubbles out of her mouth."
    scene mouth_cum_02
    with dissolve
    play sound "blowjob/sound/bj_vomit.mp3"
    clem "Hurngh!"
    "Clementine drops to all fours and heaves the contents of her stomach onto the carpet."
    clem "Hurk!"
    p "Haha..."
    "You laugh as she vomits cum and spit onto the floor."
    p "What the fuck slut, I gave you good meal this is how you thank me?"
    scene mouth_cum_04
    with dissolve
    "She pushes herself up off the ground, glaring at you."
    clem "Fuck you!"
    p "Hey!"
    p "Watch your fucking tone whore."
    p "Now stand the fuck up cause I am far from finished with you."
    "Clementing gets back to her feet, hand clenched at her sides glowering at you."
    jump bj_end_label


label bj_end_label:
    scene bj_end
    "You look Clementine up and down and realise that you will need little rest before another round."
    p "Get on the bed! Time to fuck that pussy!"
    #placeholder
    jump prefuck
