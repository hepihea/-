
label cowgirl_from_missionary:
    $ hide_overlay()
    stop sound fadeout 5
    clem "Ahh wait..."
    #image
    scene cg_miss
    with dissolve
    "In a swift move Clementine slides backwards off your shaft"
    clem "I want to be on top!"
    #image
    scene cg_kneeling
    with dissolve
    "She motions you to lie on the bed, kneeling next to you rubbing her pussy."
    p "Ok..."
    #image
    scene cg_insert
    with dissolve
    "You lie down on the bed and she straddles you, stroking your cock."
    clem "Nnn... Ahhhh.."
    "With ease she slides you into her wet hole and starts to ride."
    jump cowgirl

label cowgirl_from_prone:
    $ hide_overlay()
    stop sound fadeout 5
    clem "Ahh... wait.... stop..."
    #image
    scene cg_after_fours
    with dissolve
    "She gasps roughly and you slowly draw out from inside her."
    clem "I want to be on top..."
    #image
    scene cg_crawl_over
    with dissolve
    "She pushes you onto your back, staring at your cock lustfully."
    #image
    scene cg_insert
    with dissolve
    "You lie down on the bed and she straddles you, stroking your cock."
    clem "Nnn... Ahhhh.."
    "With ease she slides you into her wet hole and starts to ride."
    jump cowgirl

label cowgirl_from_doggy:
    $ hide_overlay()
    stop sound fadeout 5
    clem "Ngghhh... wait..."
    #image
    scene cg_after_fours
    with dissolve
    "She slides forward off your dick, dropping her hip to the bed."
    clem "I want to be on top..."
    "She stares at you through hooded eyes."
    p "Ok..."
    #image
    scene cg_kneeling
    with dissolve
    "She kneels next to you, rubbing her pussy while you reposition on the bed."
    #image
    scene cg_insert
    with dissolve
    "You lie down on the bed and she straddles you, stroking your cock."
    clem "Nnn... Ahhhh.."
    "With ease she slides you into her wet hole and starts to ride."
    jump cowgirl



label cowgirl_from_side:
    $ hide_overlay()
    stop sound fadeout 5
    clem "Ahh... wait..."
    #image
    "She scrambles off your dick, turning to face you."
    clem "I want to be on top..."
    #image
    scene cg_all_fours
    with dissolve
    "She crawls over on all fours as you lie back on the bed"
    #image
    scene cg_insert
    with dissolve
    "You lie down on the bed and she straddles you, stroking your cock."
    clem "Nnn... Ahhhh.."
    "With ease she slides you into her wet hole and starts to ride."
    jump cowgirl

label cowgirl:
    stop sound fadeout 1
    play sound "sex/cowgirl/sound/cowgirl_01.mp3" loop fadein 1
    $ button_screens("cg_loop01", "cg_loop01_screen")
    clem "Ahh...Shit..."
    p "Uhhh..."
    "You groan as her wetness wraps around you."
    clem "Mmm... ah...."
    "Clementine places her hands on your chest and rocks back and forth."
    clem "Hmm... mmmm..."
    clem "Ahh..."
    p "Uh..."
    "She runs her hands up and down your chest, breathing heavily."
    window hide
    pause 5
    window show
    clem "Haa... hah..."
    "You run your hands up her soft thighs rocking your hips in time with her movement."
    p "Ahh... uh...."
    clem "Hmm... nice?"
    "She coo's at you, nails dragging lightly across your skin."
    p "Yeah... oh yeah..."
    clem "Hehe.."
    "She giggles softly and chews her lower lip."
    window hide
    pause 5
    window show
    "Clementine looks down starting to roll her upper body."
    clem "Hmmmm!"
    $ button_screens("cg_loop02", "cg_loop02_screen")
    stop sound fadeout 0.5
    play sound "sex/cowgirl/sound/cowgirl_02.mp3" loop fadein 1
    "With a grunt she rolls back and start to bounce up and down on your cock."
    clem "Ahh... hah..."
    $ hText()
    "She gasps hoarsely as her hands drift out to her sides."
    p "Ah... shit!"
    "You groan loudly as she slide up your length before driving back into your hips with a soft squelch."
    clem "Ahh.... Oh..."
    clem "Hnn.. hnnn..."
    p "Ahh.. ah..."
    window hide
    pause 5
    window show
    "Her breath comes in ragged gasps as she approaches stares ahead, eyes unfocused."
    $ hText()
    p "Ah damn.. so good..."
    clem "Uh huh..."
    "She responds but doesnt seem to be paying much attention, her breasts heaving as she bounces on you."
    clem "Oh god... I think..."
    "She doesnt finish, hissing air through her teeth."
    window hide
    pause 5
    window show
    clem "Hah... hah... hah..."
    clem "Oh... fuuuuck..."
    "Clementines brown knits as she clenches her teeth."
    clem "I think... ah I ..."
    p "You going to cum for me?"
    "She mewls in response."
    clem "Yeah... yea..."
    "She gasp raggedly."
    p "Alright then!"
    stop sound fadeout 1
    play sound "sex/cowgirl/sound/cowgirl_cum_intro.mp3" loop
    $ button_screens("cg_cumintro", "cg_cumintro_screen")
    "You grip her thighs and push up into her."
    clem "Haaaang..."
    "She cries out as you start to pump into her."
    clem "Oh god..."
    p "Hnnn fuck..."
    "You grit your teeth as her thigh pussy grips you."
    clem "Oh god!"
    "Clementine starts to rub at her clit, making plaintive noises."
    p "Going to cum for me girl?"
    clem "Mmmm..."
    clem "Yeah... yes..."
    "You feel your own release building, the sight and feel of the girl pushing you over the edge."
    p "Uhh here it comes..."
    clem "Ahh yeah... fill me up!"
    "You groan as she cries out, pumping hot cum inside her."
    $ hide_overlay()
    stop sound fadeout 1
    play sound "sex/cowgirl/sound/cowgirl_cum_actual.mp3" fadein 1
    queue sound "sex/cowgirl/sound/cowgirl_cum_outro.mp3" loop
    scene cg_cum with flash_sharp
    pause 4.3
    window show
    scene cg_cumoutro
    with dissolve
    clem "Haaaah..."
    $ button_screens("cg_cumoutro", "cg_cumoutro_screen")
    p "Ahhh... hah...."
    "Clementine breathes heavily on top of you while your cock tries to keep pulsing inside her."
    clem "Hah.... ah... mmmm..."
    clem "ha..."
    "She stares at your chest, eyes unfocused, catching her breath."
    p "Ah.. shit..."
    "You can feel your shaft starting to soften inside her soaked tunnel."
    clem "Hmm... hmmmm..."
    #image
    $ hide_overlay()
    stop sound fadeout 8
    scene cg_end_01
    with dissolve
    "Finally she looks up at you, raising her hips to slide you dick out."
    clem "Hmmmm..."
    "She kneels over you, swaying side to side."
    p "Ahh damn..."
    clem "Hehe..."
    "Clementine giggles as your cum drips from her pussy."
    p "Ah.."
    "You lie on the bed getting your breath back, before finally sliding back off the matterss."
    scene cg_end_02
    with dissolve
    clem "Mmmm that was good!"
    "She kneels infront of you, one hand playing with the gooey mess between her legs."
    p "Girl you are seriously good at that."
    clem "Heh thanks!"
    "As you pull on your clothes she slides to the edge of the bed."
    scene cg_end_03
    with dissolve
    p "Will have to come and see you again some time..."
    "Clementine flashes you a bright smile."
    clem "Look forwrad to it! Especially if its more of that..."
    "With a last look at the girl you walk over to the door, calling out."
    p "Bye!"
    scene cg_end_04
    with dissolve
    "As the door swings shut you think you see Clementines face collapse, staring blankly ahead with dead eyes."
    scene door1
    with dissolve
    "But before you can be sure the door is shut."
    "You stare at the wooden door for a moment, before walking away down the cooly lit corridor."
    jump the_end
































#
