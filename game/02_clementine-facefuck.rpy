
#she is lieing on bed
label ff_from_rough:
    #dragging back
    "Reaching out you grab hold of Clementine’s foot and drag her towards you."
    #spinning her around
    scene from_rough01
    with dissolve
    p "Time to choke on a cock slut."
    clem "No!"
    #pinning her down
    scene from_std03
    with dissolve
    "She shrieks as you grab her neck, dragging her around and pinning her."
    clem "Fuck off!"
    p "Might want to save your breath slut."
    jump ff_insult

#she is s
label ff_from_neut:
    "Clementines eyes flash wide as you reach out and grip her shoulders."
    scene from_std01
    with dissolve
    "You push her back onto the bed and she looks up at you."
    jump ff_norm

#directly after neutral strip =- stanbding push back on bed
label ff_from_neut_standing:
    "Clementine’s eyes flash wide as you reach out and grip her shoulders."
    scene from_std01
    with dissolve
    "You push her down onto the bed and she looks up at you."
    jump ff_norm

#Sitting on bed, push down
label ff_from_happy:
    "Clementine’s eyes flash with worry as you reach out and grip her shoulders."
    scene from_std01
    with dissolve
    "You push her down onto the bed firmly."
    jump ff_norm


label ff_norm:
    stop music fadeout 10
    $ abuse = abuse + 2
    scene from_std02
    with dissolve
    "With a hand on her shoulder you spin the girl around until her head is off the edge of the mattress."
    scene from_std03
    with dissolve
    "She stares up at you in consternation."
    clem "No..."
    "Clementine murmurs a denial as you step forward."
    p "Oh Yes..."
    scene ff_pantsoff01
    with dissolve
    "You move forward reaching to your waist band."
    p "Best to just relax cause I am going to feed you this snake."
    voice "facefuck/sound/ff_resist_01.mp3"
    clem "hnnn...."
    "You drop your pants to the floor, step out of them and stand over the girl."
    scene ff_pantsoff02
    with dissolve
    "She fixates on your hardening dick."
    p "Like what you see?"
    # Awaiting sound
    "You grip the base of your dick and waggle it in her face."
    p "Haha..."
    voice "facefuck/sound/ff_resist_02.mp3"
    clem "Mmmmh."
    "Clementine whimpers slightly, raising a hand to push you away."
    p "Hey now enough of that!"
    scene pre_slap
    with dissolve
    "You stand over her and slide your dick against her cheek."
    voice "facefuck/sound/ff_resist_03.mp3"
    clem "Hhhhnnn"
    "She presses her lips and turns away."
    scene ff_face_slap
    p "Now you are just being rude..."
    "You slap her in the cheek with your dick."
    voice "facefuck/sound/ff_resist_04.mp3"
    clem "Nnnng.."
    "With a chuckle you keep tapping her cheek with your dick."
    p "Ooo... soft..."
    p "Is your throat as soft?"
    voice "facefuck/sound/ff_resist_02.mp3"
    clem "Hnn..."
    "You chuckle again at her discomfort."
    scene rub_start
    with dissolve
    "You stop slapping Clementine and slide your dick up against her nose, resting the head on her lips."
    p "Surely you are used to dick by now what the hell is this?"
    voice "facefuck/sound/ff_resist_05.mp3"
    clem "Hn.. mmm..."
    scene ff_face_rub
    with dissolve
    "You start to rub your dick up and down, pressing into her cheek and lips."
    p "Mmmm..."
    "She reaches up and pushes against your thigh in a half-hearted attempt to push you away."
    play sound "facefuck/sound/ff_facerub.mp3" loop
    clem "Mhh..."
    "Clementine screws her eyes shut as you grip her head, running your thumb over her chin."
    clem "Nnngh..."
    p "Ahhhh..."
    "You breathe heavily from the friction on your rod, tightening your grip on her head."
    p "Ahh, enough of this."
    "With your thumb you pry her jaw open."
    stop sound fadeout 0.5
    voice "facefuck/sound/ff_pry.mp3"
    scene ff_presuck01
    with dissolve
    voice "facefuck/sound/ff_pre_insert.mp3"
    clem "Hnnn..."
    "She opens her eyes, eyebrows raised as you position your dick in front of her lips."
    scene ff_presuck02
    with dissolve
    p "Ahhh..."
    voice "facefuck/sound/ff_insert.mp3"
    clem "Mmmmmg"
    "Clementine whimpers again as you force your cock between her lips."
    p "Shiiit..."
    "You pause for a moment, relishing the softness of her mouth before you start to push into her."
    $ button_screens("ff_start","ff_start_screen")
    #loop
    play sound "facefuck/sound/ff_norm_start.mp3"
    queue sound "facefuck/sound/ff_medium_loop.mp3" loop
    clem "Hnngh..."
    "She gags slightly as you push into her mouth, feeling your dick push up against her throat."
    p "Ooooh...."
    clem "{i}{{ hurk...  nnnngh... }{/i}"
    "Pushing in and out you fuck her mouth."
    clem "Hnn.. {i}{{ glurk... }{/i}"
    p "Ahh... damn...."
    "Clementine’s soft mouth envelops your rod and you can feel her tongue pushing at your cock every time it knocks against her throat."
    clem "Hnng.. {i}{{ hurk... }{/i}"
    p "Fuck! Enough foreplay!"
    "You reach down and pin her left arm to the bed as you drive your dick into her throat."
    $ button_screens("ff_second","ff_second_screen")
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_medium_loop.mp3" loop
    clem "Huurrk!"
    "The girl’s chest heaves as you push past her tonsils, retching as you force your way down her throat."
    p "Ooooh..."
    clem "Hnnngh.. clurp!"
    "Wet unintelligible sounds come from Clementine as you bury your length in her throat before pulling out and driving in again."
    "You can feel her pushing at your thigh with every thrust but she lacks the strength to stop you."
    clem "{i}{{ glurk.... hurk... }{/i}"
    p "Ahhh.."
    "You grip her neck, feeling it expand with each thrust."
    p "Fuck I can feel my dick in your throat!"
    "Clementine’s only answer is more wet noises as your dick fills her mouth."
    clem "Hnnng... hnnn..."
    p "Shiiit... time for something new!"
    $ hide_overlay()
    menu:
        "Grab her neck and go to town...":
            jump ff_neckgrab
        "Give it to her deep...":
            jump ff_godeep

label ff_neckgrab:
    "You let go of her arm and wrap both hands around Clementine’s neck."
    $ button_screens("ff_throatgrab","ff_throatgrab_screen")
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_rough_loop.mp3" loop
    p "Nnnngh!"
    "With a grown you start to pump into her throat with abandon."
    clem "{i}{{ glurk... }{/i} Huuurkk"
    "Clementine starts to thrash as you fuck her face."
    "You can feel your dick pushing her neck against your thumbs with each thrust."
    p "Ahhh.... fuck.... so good..."
    "Any semblance of actual sounds Clementine had been making devolve into wet suffocated slurps as she fights for breath."
    clem "{i}{{ hurk... hnk... }{/i}"
    "You grip tightly at her neck, feeling the muscle pulse and twitch as the combination of hands and dick starve her of air."
    p "Oh... oh...."
    clem "Hunng..."
    "Her body spasms violently, spit and saliva oozing out of her mouth."
    "The rippling of her neck sends you rapidly to the edge and to lean forward."
    jump norm_cum




label ff_godeep:
    "You drop your hands down onto the bed and drive your dick deep into Clementine’s throat."
    $ button_screens("ff_deep","ff_deep_screen")
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_deep_loop.mp3" loop
    p "Ahhh..."
    clem "Hnnnggg..."
    "You keep your shaft buried in her throat for a moment before withdrawing it."
    clem "Hah...  Nnn!"
    "Clementine sucks air for only a moment before yelping as you sink back into her mouth."
    p "Shit..."
    clem "Hurk!"
    "Her body spasms as her throat is pushed wide by your cock."
    clem "{i}{{ hurk... glurk... }{/i}"
    "The girl tries to suck air in through her nose, and you can see the shape of your dick as it pushes its way into her throat."
    clem "{i}{{ glurp... }{/i}"
    "You can feel her throat muscles twitching and spasming at the intrusion, sending delightful ripples along your shaft."
    p "Ooooh.."
    clem "{i}{{ hurk... }{/i}"
    "The caress of her throat becomes too much and you can feel your release building."
    "Sliding forward you start to pump rapidly into her throat."
    jump norm_cum



label norm_cum:
    show ff_precum_loop
    with dissolve
    stop sound fadeout 0.5
    play sound "facefuck/sound/pre_loop.mp3"
    $ hide_overlay()
    p "Shit.... Here it comes!"
    "Clementine doesn’t respond, simply fighting to stay conscious as you push down on her head, pumping your rod into her face."
    clem "Hnnng.... hurk...."
    "She reaches up with the last of her strength and pushes feebly at your stomach, trying to relieve the pressure."
    p "Fuuuuuuck..."
    "With a groan your balls tighten and a flood of cum rushes down your dick."
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_cum.mp3"
    queue sound "facefuck/sound/ff_cum_loop.mp3" loop
    window hide
    show movie
    play movie "facefuck/vid/ff_cum_seq.webm" noloop #4.12
    with flash_sharp
    pause 3.6
    $ button_screens("ff_endloop","ff_endloop_screen")
    #with dissolve
    #with flash_sharp
    "Buried deep in her mouth you fire spurt after spurt into her throat."
    clem "Hhhhhhnnnnghlu...."
    "The girl makes an inarticulate noise as you flood her mouth and throat."
    p "Oh goddamn..."
    "Breathing deeply you stay in her mouth, draining every last drop into her spasming body."
    clem "....."
    "Clementine’s arms start to sag, dropping from your stomach and you realize she is at her limit."
    $ hide_overlay()
    scene ff_exit
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_gasping.mp3" fadeout 2.0
    "With a groan you pull your dick from her mouth, accompanied by a wet slurping sound."
    clem "Hurk... {i}{{ cough... }{/i}"
    "As your dick slides free Clementine’s body heaves, spewing cum and saliva out of her full mouth."
    scene ff_postsuck03
    with dissolve
    "In a daze she rolls onto her side, arms hanging limply to the floor."
    clem "Hah... hah.... hah... "
    "She fights for breath, wet sucking gasps as drawing breath fights with rejecting a mouth full of cum."
    scene ff_postsuck04
    with dissolve
    "You say nothing, breathing deeply, as she rolls over onto her stomach."
    clem "Hhhhnnnnn huh... huh..."
    "Clementine lays on the bed limply, drool and cum still dripping from her mouth as she sobs."
    p "Are you crying?"
    scene ff_postsuck05
    with dissolve
    clem "Hhhhnn... {i}{{ sniff... }{/i} hnnn"
    p "Come on, there is no way that’s the first time you have been face fucked!"
    "She says nothing, body shaking as she slowly recovers her composition."
    clem "Fuck you..."
    "She says in a small voice, between sniffles."
    p "Nah. That’s the next part girl."
    #placeholder
    jump prefuck


label ff_insult:
    stop music fadeout 10
    $ abuse = abuse + 3
    scene ff_pantsoff01
    with dissolve
    "You step forward and unbutton your pants."
    p "This is going to be great."
    scene ff_pantsoff02
    with dissolve
    "You drop your pants and grab your cock."
    voice "facefuck/sound/ff_resist_01.mp3"
    clem "Hnnn..."
    scene rub_rough_start
    with dissolve
    "Clementine whimpers as you step forward and grab her head."
    p "Time for a meal slut..."
    play sound "facefuck/sound/ff_facerub.mp3" loop
    clem "Hnnnngh!"
    "She tries to hold her jaw shut but you easily pry it open."
    scene ff_presuck01
    with dissolve
    p "Open wide!"
    scene ff_presuck02
    with dissolve
    play sound "facefuck/sound/ff_norm_start.mp3"
    clem "Mmmmfgh!"
    "The girl struggles as you shove your dick deep into her mouth and start pumping."
    $ button_screens("ff_start","ff_start_screen")
    play sound "facefuck/sound/ff_medium_loop.mp3" loop
    clem "{i}{{ hurk...  glurk... }{/i}"
    p "Ahh yeah you got a good mouth whore..."
    "Clementine gags and splutters as you force your dick in and out of her mouth."
    "You can feel the head of your dick pushing against her throat."
    p "You think this is as deep as we can go?"
    clem "Mmmmmmgh!"
    p "Haha..."
    $ button_screens("ff_second","ff_second_screen")
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_medium_loop.mp3" loop
    "With a laugh you pin down her left hand and sink the length of your dick into her throat."
    p "Oooohh..."
    clem "Hurk..."
    "Clementine jerks, gagging as you shove your cock down her throat."
    p "Fuck yeah slut... your mouth is the best..."
    "You continue to pound her mouth, ignoring the gagging and shaking girl."
    clem "{i}{{ hurgh...  glurk... }{/i}"
    "With each thrust spit and saliva spurt from her mouth, displaced by your ravaging dick."
    p "Ng! Now we are talking!"
    p "Take it slut..."
    "You keep pounding at her face, gripping her neck to feel the tip of your dick as it pushes into her throat."
    clem "Nnnnggh {i}{{ huur.... }{/i}"
    "The girl seems reduced to animalistic noises as you violate her."
    p "Lets step it up a gear slut."
    $ button_screens("ff_throatgrab","ff_throatgrab_screen")
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_rough_loop.mp3" loop
    "You grab her neck and squeeze, increasing your speed as you slam your dick in and out of her."
    p "Shit..."
    clem "{i} schlurp...  sclup...{/i}"
    "Under you Clementine starts to go limp, your hands cutting off the last source of oxygen."
    "She grips loosely at your hips and arm as she slobbers on your dick."
    p "Oh.. fuck ..."
    "You feel the end approaching, drinking in the sight in front of you."
    stop sound fadeout 0.5
    play sound "facefuck/sound/pre_loop.mp3" loop
    show ff_precum_loop
    with dissolve
    $ hide_overlay()
    "Leaning forward you place your hands on the bed and start to slam furiously into Clementine’s face."
    p "Oh fuck..."
    p "Get ready for a present slut.."
    clem "Hnng... hnnn..."
    "With a last show of strength she reaches up, pushing feeble at your stomach, desperate to breathe."
    p "Oh fuck..."
    p "Take it you whore... "
    clem "Hnnnne!"
    "Clementine emits a high pitched whine as with a groan you unload in her throat."
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_cum.mp3"
    queue sound "facefuck/sound/ff_cum_loop.mp3" loop
    window hide
    show movie
    play movie "facefuck/vid/ff_cum_seq.webm" noloop #4.12
    with flash_sharp
    pause 3.6
    $ button_screens("ff_endloop","ff_endloop_screen")
    p "Oh fuck..."
    clem "Nnhnnngn...{i}{{ snort... }{/i}"
    "You keep your dick buried down her throat as you shoot streams of cum into her neck."
    clem "{i}{{ splort... }{/i}"
    "With a heave Clementine splutters a wave of cum out of her mouth, convulsing as she fails to breathe."
    p "Ahhhhgh..."
    "With a last grunt and shake you finally pull your cock from her body."
    clem "Hurk..."
    stop sound fadeout 0.5
    play sound "facefuck/sound/ff_gasping.mp3" fadeout 2.0
    scene ff_exit
    "With a heave Clementine gasps for breath, vomiting cum and saliva down her face as she shudders."
    clem "Hnnnnnngh!"
    scene ff_postsuck03
    with dissolve
    "She draws a shuddering breath and rolls over onto her side."
    p "Fuck that was good slut, could do that all again yeah?"
    clem "Nnnnn..."
    scene ff_postsuck04
    with dissolve
    "She whimpers, drooling spit onto the floor in a daze."
    p "But I still plan to fuck the shit out of that pussy and ass of yours, so don’t want to waste it all right?"
    "Clementine doesn't respond as she rolls limply onto her stomach."
    scene ff_postsuck04
    with dissolve
    clem "Huh... huh..."
    #placeholder
    jump prefuck
