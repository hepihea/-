
label cum_doggy_from_doggy:
    p "Oh shit..."
    jump cum_doggy_norm

label cum_doggy_from_prone:
    p "Oh shit..."
    "You sit back, pulling Clementine up onto all fours."
    jump cum_doggy_norm


label cum_doggy_from_doggy_rough:
    p "Ah fuck... time to fill you up cunt..."
    jump cum_doggy_rough

label cum_doggy_from_prone_rough:
    p "Ah fuck... time to fill you up cunt..."
    "You sit back, dragging Clementine up onto all fours."
    jump cum_doggy_rough




label cum_doggy_norm:
    clem "Ahhh!"
    stop sound fadeout 0.5
    play sound "sex/cum_doggy/sound/dog_cum_intro.mp3" loop fadein 1
    $ button_screens("doggy_cumintro", "doggy_cumintro_screen")
    "She gasps as you grip her shoulder, slapping into her."
    p "Ahh.... gonna cum..."
    clem "Nnnn... hah..."
    "She gasps hoarsely as you feel your end approach."
    clem "Hah... ah..."
    p "Get ready... here it comes..."
    clem "Uhhhh!"
    "With a groan you drive deep inside her, shooting cum deep in her womb."
    $ hide_overlay()
    window hide
    stop sound fadeout 0.5
    play sound "sex/cum_doggy/sound/dog_cum_actual.mp3" fadein 1
    queue sound "sex/cum_doggy/sound/dog_cum_outro.mp3" loop
    scene  doggy_cum with flash_sharp
    pause 4.4
    window show
    scene doggy_cumoutro with dissolve
    clem "Ahhhh...."
    "With a groan you slide out of the girl, white cum dripping from her pussy."
    $ button_screens("doggy_cumoutro", "doggy_cumoutro_screen")
    p "Ahhh... shit..."
    clem "Hah... hah..."
    p "Your pussy is amazing..."
    p "Hah!"
    $ hide_overlay()
    # image
    stop sound fadeout 8
    scene doggy_end_01
    with dissolve
    "You slide back off the bed as Clementine kneels on the mattress, head hanging."
    clem "Hmm..."
    p "Damn that’s a sight..."
    clem "Ah..."
    "Clementine kneels on the bed, breathing heavily."
    "You step back, picking your clothes off the floor as she turns to look at you."
    scene doggy_end_02
    with dissolve
    clem "Ahh... ah..."
    "She doesn’t speak and you can see the white streaks running down her thigh."
    p "You are one hell of a good fuck girl... money well spent."
    clem "Hmmf"
    "She snorts, raising an eyebrow as she lays back on the bed."
    scene doggy_end_03
    with dissolve
    p "Will have to come back again some time for round two!"
    clem "..."
    scene doggy_end_03
    with dissolve
    "The girl ignores you as you walk to the door."
    scene door1
    with dissolve
    "You give her one last look before you swing the door closed and head down the corridor"
    jump the_end




label cum_doggy_rough:
    clem "Hngh!"
    stop sound fadeout 0.5
    play sound "sex/cum_doggy/sound/dog_cum_intro.mp3" loop fadein 1
    $ button_screens("doggy_cumintro", "doggy_cumintro_screen")
    "You reach up and grip her shoulder tightly."
    p "Get ready slut..."
    clem "Ngh... hnn..."
    p "Ah... here is comes!"
    clem "Mmmm... no..."
    p "With a shout you shove your dick deep inside her, firing cum into her womb."
    $ hide_overlay()
    window hide
    stop sound fadeout 0.5
    play sound "sex/cum_doggy/sound/dog_cum_actual.mp3" fadein 1
    queue sound "sex/cum_doggy/sound/dog_cum_outro.mp3" loop
    scene  doggy_cum with flash_sharp
    pause 4.4
    window show
    scene doggy_cumoutro with dissolve
    p "Ahhhh...."
    "With a groan you slide out of the girl, watching as your cum drips from her pussy."
    $ button_screens("doggy_cumoutro", "doggy_cumoutro_screen")
    clem "Ahhh... hah...."
    "Clementine hangs her head, sniffing."
    p "Hah... if nothing else you got a tight pussy on you slut."
    p "Don't move now... I want to savour this..."
    $ hide_overlay()
    #image
    stop sound fadeout 8
    scene doggy_end_01
    with dissolve
    "You slide back off the bed."
    p "That is nice...."
    clem "Hah..."
    p "You like being filled up cunt?"
    scene doggy_end_02
    with dissolve
    "She turns to glare at you, cum running down her thigh."
    clem "Fuck you."
    p "Hah!"
    "With a laugh you pull on your clothes."
    p "Now don’t you go calling me if you're late next month!"
    clem "..."
    scene doggy_end_03
    with dissolve
    "Clementine ignores your barb, turning away as you walk to the door."
    p "No sweet goodbye?"
    clem "I hope you get hit by a truck!"
    p "Haha."
    scene doggy_end_03
    with dissolve
    "With a final look at the girl on the bed you grab the door handle."
    p "See you next time girl."
    scene door1
    with dissolve
    "With that you pull the door closed and set off down the hallway."
    jump the_end
