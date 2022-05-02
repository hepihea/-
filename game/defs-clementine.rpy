#class values
init python:
    import random
    normal = ["Ah", "Ngh", "Ahhh", "Haa", "Ha", "Hah", "Agh", "Ahh", "Mmmmf", "Hngh", "Uh", "Uhh", "Oh", "Ohhh"]
    rough = normal + ["Nnnh", "Ow", "Nnnn", "Hnn", "Hss"]
    happy = normal + ["Mmmm", "Haaa", "Mmm", "Mmmmm", "Haaah", "Ooooo", "Oohh", "Yea"]
    append = ["!", "...", "...", "..", "repeat", "repeat"]
    append2 = ["!", "...", "...", ".."]

    def noise(it):
        c = 0
        while c < it:
            getString(normal)
            c += 1

    def rNoise(it):
        c = 0
        while c < it:
            getString(rough)
            c += 1

    def hNoise(it):
        c = 0
        while c < it:
            getString(happy)
            c += 1

    def getString(list):
        n = getSound(list)
        ap = getSound(append)
        if ap == "repeat":
            clem (n + "...  " + getSound(list).lower() + getSound(append2))
        else:
            clem(n + ap)

    def getSound(list):
        return random.choice(list)

    clem_standard = ["Fuck", "Shit"]
    clem_insults = ["Fuck you", "Go to hell", "Get fucked", "Piece of shit"]
    clem_happyf = clem_standard + ["So good", "Fuck me", "So deep", "More", "Deeper", "Yes", "Yesss", "Keep going", "Yea"]

    def nText():
        buildResponse(clem_standard, normal)

    def hText():
        buildResponse(clem_happyf, happy)

    def rText():
        buildResponse(clem_insults, rough)

    def buildResponse(list1, list2):
        val = random.randint(1,3)
        if val == 0:
            clem (random.choice(list1) + "... " + random.choice(list2) + "..  " + random.choice(list2).lower() + "...")
        elif val == 1:
            clem (random.choice(list1) + "... " + random.choice(list2).lower() + "...")
        elif val == 2:
            clem (random.choice(list2) + "... " + random.choice(list1) + "..  " + random.choice(list2).lower() + "...")
        elif val == 3:
            clem (random.choice(list2) + "... " + random.choice(list1) + "...")

    def slapLine(v = 0):
        val = random.randint(1,3)
        c = 0
        st = "{i}{{ "
        while c< val:
            st += "slap... "
            c += 1
        st += "}{/i}"
        narrator(st)




init:
    image movie = Movie(size=(1280, 720))

define abuse = 0
define position = ""
define posCount = 0

#Position done once defs
#Anal
define doneAnal = False
define doneRoughAnal = False
define doneAnalFast = False
define doneRoughAnalFast = False

#Prone Anal
define doneProneAnal = False
define doneProneAnalFast = False
define doneProneAnalRough = False
define doneProneAnalRoughFast = False
#Prone Vag
define doneProneVag = False
define doneProneVagFast = False
define doneProneVagRough = False
define doneProneVagRoughFast = False
define doneProneVagHappy = False
define doneProneVagHappyFast = False

#Prone Vag
define doneProneVag = False
define doneProneVagFast = False
define doneProneVagRough = False
define doneProneVagRoughFast = False
define doneProneVagHappy = False
define doneProneVagHappyFast = False

#Doggy
define doneDoggy = False
define doneDoggyFast = False
define doneRoughDoggy = False
define doneRoughDoggyFast = False
define doneHappyDoggy = False
define doneHappyDoggyFast = False

#Missionary
define doneMissionary = False
define doneMissionaryFast = False
define doneRoughMissionary = False
define doneRoughMissionaryFast = False
define doneHappyMissionary = False
define doneHappyMissionaryFast = False

#On Side
define doneSide = False
define doneRoughSide = False
define doneHappySide = False


define neverAnal = True

image mag_icon = "mag_glass_icon.png"

#pre sex
image sit_on_bed = "clementine_intro/on_bed_01.jpg"
image sit_on_bed_blink = "clementine_intro/bed_blink.jpg"


image bed_blink:
    choice (4.0):
        "sit_on_bed"
    choice:
        "sit_on_bed_blink"
        pause 0.2
        "sit_on_bed"

    pause 1.0
    repeat

#images

#script
image clem_stand = "clementine_intro/clem_stand_01.jpg"
image clem_stand_02 = "clementine_intro/clem_stand_02.jpg"
image clem_stand_03 = "clementine_intro/clem_stand_03.jpg"
image clem_stand_sad = "clementine_intro/clem_stand_04.jpg"
image clem_stand_happy = "clementine_intro/clem_stand_05.jpg"

image clem_slap = "clementine_intro/slap.jpg"
image clem_slap_bed = "clementine_intro/slap_on_bed.jpg"

image camera_on = "clementine_intro/camera_on.jpg"


#clementine-strip-mild
image off_bed:
    "clementine_normal/off_bed.jpg" with dissolve
    pause 1
    "clementine_normal/stand_pre_strip.jpg" with dissolve

image stand_pre_strip = "clementine_normal/stand_pre_strip.jpg"



image top_off_trans:
    "clementine_normal/top_strip_a.jpg" with dissolve
    pause 1
    "clementine_normal/top_strip_b.jpg" with dissolve
    pause 1
    "clementine_normal/top_off_norm.jpg" with dissolve



image top_off = "images/clementine_normal/top_off_[isZoomed].jpg"
image top_off_sad = "images/clementine_normal/top_off_sad.jpg"

define isZoomed = "norm"
screen topOffScreen():
    imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")

image top_off_cover_a = "clementine_normal/top_off_coverup.jpg"


image shoes_off_a = "clementine_normal/shoes_off_a.jpg"
image shoes_off_b = "clementine_normal/shoes_off_b.jpg"
image shoes_off_c = "clementine_normal/shoes_off_c.jpg"

image pants_strip:
    "clementine_normal/pants_off_a.jpg" with dissolve
    pause 1
    "clementine_normal/pants_off_b.jpg" with dissolve
    pause 1
    "clementine_normal/pants_off_norm.jpg" with dissolve

image pants_off = "clementine_normal/pants_off_[isZoomed].jpg"
screen pantsOffScreen():
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")


#Clementine strip happy

define hsdir = "clementine_happy_strip/"

image stand_happy01 = "[hsdir]pre_stand_01.jpg"
image stand_happy02 = "[hsdir]pre_stand_02.jpg"
image stand_happy03 = "[hsdir]pre_stand_03.jpg"
image stand_happy04 = "[hsdir]pre_stand_04.jpg"

image top_off_happy_trans:
    "[hsdir]top_off_a.jpg" with dissolve
    pause 1
    "[hsdir]top_off_b.jpg" with dissolve
    pause 1
    "[hsdir]topless.jpg" with dissolve

image top_off_happy = "[hsdir]topless_[isZoomed].jpg"
screen topOffHappyScreen():
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")

image cupbreasts_a = "[hsdir]tit_cover_a.jpg"
image cupbreasts_b = "[hsdir]tit_cover_b.jpg"

image naked_happy = "[hsdir]naked_[isZoomed].jpg"
screen nakedHappyScreen():
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")


# Clementine strip rough
define rsdir =  "clementine_rough_strip/"
image rough_strip_hand_out = "[rsdir]bed_01.jpg"
image rough_strip_hand_away = "[rsdir]slap_hand_01.jpg"
image hair_grab = "[rsdir]hair_grab_01.jpg"
image rough_slap = "[rsdir]hair_grab_02.jpg"
image after_slap = "[rsdir]slap_01.jpg"
image rough_shirtoff_01:
    "[rsdir]top_off_01.jpg" with dissolve
    pause 0.5
    "[rsdir]top_off_02.jpg" with dissolve
    pause 0.5
    "[rsdir]top_off_03.jpg" with dissolve
    pause 0.5
    "[rsdir]top_off_norm.jpg" with dissolve

image top_off_rough = "[rsdir]top_off_[isZoomed].jpg"
screen roughTopOffScreen():
        #textbutton _("Zoom") action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")

image bed_push_01 = "[rsdir]bed_push_01.jpg"
image bed_push_01 = "[rsdir]bed_push_02.jpg"
image rough_shoe_off_01 = "[rsdir]boots_off_01.jpg"
image rough_shoe_off_02 = "[rsdir]boots_off_02.jpg"
image rough_pants_off_01 = "[rsdir]pants_off_01.jpg"
image rough_pants_off_02 = "[rsdir]pants_off_02.jpg"

image naked_rough = "[rsdir]naked_[isZoomed].jpg"
screen roughNakedScreen():
        #textbutton _("Zoom") action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")




#Perv naked happy
define phdir = "perv_happy/"

image ph_bedsit_01 = "[phdir]sit_01.jpg"
image ph_bedsit_flash:
    "[phdir]sit_flash.jpg" with dissolve
    pause 1.0
    "[phdir]sit_01.jpg" with dissolve

image ph_bedsit = "[phdir]sit_[isZoomed].jpg"
screen phBedSitScreen():
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")

image ph_spread_01 = "[phdir]spread_01.jpg"

image ph_bedspread = "[phdir]spread_[isZoomed].jpg"
screen phBedSpreadScreen():
        imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")

image ph_mast_intro = "[phdir]mast_intro.jpg"

define val = "norm"

image mastloop_body = Movie(play="perv_happy/vid/mast_body.webm", mask="perv_happy/vid/white_.webm")
image mastloop_face = Movie(play="perv_happy/vid/mast_face.webm", mask="perv_happy/vid/white_.webm")

screen ph_face_focus:
    imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action Call("mast_head")

screen ph_body_focus:
    imagebutton idle "mag_glass_icon.png" hover "mag_glass_icon_hover.png" left_padding 10 top_padding 10 action Call("mast_body")

image trans = Movie(play="perv_happy/vid/transition.webm", mask="perv_happy/vid/transition_alpha.webm", loop=False)
image mast_part2 = Movie(play="perv_happy/vid/mast_pt2.webm", mask="perv_happy/vid/mast_pt2_alpha.webm")

image after_mast_01 = "[phdir]after_mast_01.jpg"
image after_mast_02 = "[phdir]after_mast_02.jpg"
image after_mast_03 = "[phdir]sit_up_post.jpg"

image pre_happy_finger = "[phdir]finger/finger01.jpg"
image finger_deep = "[phdir]finger/finger04.jpg"
image ass_finger = Movie(play="perv_happy/vid/finger.webm")

define count = 1
define inc = True
image happy_finger:
    "[phdir]finger/finger01.jpg"
    pause 0.5
    "[phdir]finger/finger02.jpg"
    pause 0.5
    "[phdir]finger/finger03.jpg"
    pause 0.5
    "[phdir]finger/finger04.jpg"
    pause 0.5
    "[phdir]finger/finger03.jpg"
    pause 0.5
    "[phdir]finger/finger02.jpg"
    pause 0.5
    repeat



#clementine-cons
define pndir = "perv_normal/"

image perv_norm_sit01 = "[pndir]sit_01.jpg"
image perv_norm_lie01 = "[pndir]lie_01.jpg"

image perv_ass_norm = "[pndir]ass_[isZoomed].jpg"
screen pervAssScreen():
        imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")
image legsup_norm = "[pndir]legsup_[isZoomed].jpg"
screen pervLegsUpScreen():
        imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")
image legup_norm = "[pndir]liftleg_[isZoomed].jpg"
screen pervLegUpScreen():
        imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action ToggleVariable("isZoomed", true_value="zoom", false_value="norm")




#clementine-blowjob
#imgaes
define bjdir = "blowjob/"

image kneel_01 = "[bjdir]blow_kneel_01.jpg"
image kneel_02 = "[bjdir]blow_kneel_02.jpg"
image kneel_03 = "[bjdir]blow_kneel_03.jpg"

image hj_start = "[bjdir]to_hj_trans.jpg"
image bj_transition = "[bjdir]hj_to_bj_trans.jpg"

image bj_end = "[bjdir]bj_end.jpg"


image mouth_cum_01 = "[bjdir]mouth_cum_01.jpg"
image mouth_cum_02 = "[bjdir]mouth_cum_02.jpg"
image mouth_cum_03 = "[bjdir]mouth_cum_03.jpg"
image mouth_cum_04 = "[bjdir]mouth_cum_04.jpg"

image face_cum_01 = "[bjdir]face_cum_01.jpg"
image face_cum_02 = "[bjdir]face_cum_02.jpg"
image face_cum_03 = "[bjdir]face_cum_03.jpg"
image face_cum_04 = "[bjdir]face_cum_04.jpg"

#video
image hj_pov = Movie(play="blowjob/vid/hj_pov.webm", mask="blowjob/vid/hj_alpha.webm")
image hj_alt = Movie(play="blowjob/vid/hj_alt.webm", mask="blowjob/vid/hj_alpha.webm")
screen hj_pov_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "hj_alt", "hj_alt_screen")
screen hj_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "hj_pov", "hj_pov_screen")


image bj_pov = Movie(play="blowjob/vid/bj_pov.webm", mask="blowjob/vid/bj_alpha.webm")
image bj_at = Movie(play="blowjob/vid/bj_alt.webm", mask="blowjob/vid/bj_alpha.webm")

screen bj_pov_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "bj_at", "bj_at_screen")
screen bj_at_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "bj_pov", "bj_pov_screen")

image bj2_pov = Movie(play="blowjob/vid/bj_2_pov.webm", mask="blowjob/vid/bj_2_alpha.webm")
image bj2_alt = Movie(play="blowjob/vid/bj_2_alt.webm", mask="blowjob/vid/bj_2_alpha.webm")
screen bj2_pov_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "bj2_alt", "bj2_alt_screen")
screen bj2_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "bj2_pov", "bj2_pov_screen")

image bj_R_pov = Movie(play="blowjob/vid/bj_R_pov.webm", mask="blowjob/vid/bj_2_alpha.webm")
image bj_R_alt = Movie(play="blowjob/vid/bj_R_alt.webm", mask="blowjob/vid/bj_2_alpha.webm")
screen bj_R_pov_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "bj_R_alt", "bj_R_alt_screen")
screen bj_R_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "bj_R_pov", "bj_R_pov_screen" )

image moutcum_Rough  = Movie(play="blowjob/vid/bj_R_cum.webm", mask="blowjob/vid/bj_R_cum_alpha.webm")
image mouthcum2 = Movie(play="blowjob/vid/mouthcum2.webm", mask="blowjob/vid/mouthcum2_alpha.webm")



#Facefuck
define ffdir = "facefuck/"

#from rough
image from_rough01:
    "[ffdir]ff_to_rough_01.jpg" with dissolve
    pause 0.5
    "[ffdir]ff_to_rough_02.jpg" with dissolve
    pause 0.5
    "[ffdir]start_turn_02.jpg" with dissolve


#from standard
image from_std01 = "[ffdir]start_turn_01.jpg"
image from_std02 = "[ffdir]start_turn_02.jpg"
image from_std03 = "[ffdir]start_turn_03.jpg"

#pants_off
image ff_pantsoff01 = "[ffdir]pants_off_01.jpg"
image ff_pantsoff02 = "[ffdir]pants_off_02.jpg"

#preFF
image pre_slap = "[ffdir]face_slap_02.jpg"
image ff_face_slap:
    choice(2):
        "[ffdir]face_slap_02.jpg" with dissolve
    choice:
        "[ffdir]face_slap_01.jpg" with dissolve
        pause 0.3
        "[ffdir]face_slap_02.jpg" with dissolve
    pause 1.0
    repeat

image rub_start = "[ffdir]face_rub_01.jpg"
image rub_rough_start = "[ffdir]face_rub_02.jpg"
image ff_face_rub:
    "[ffdir]face_rub_02.jpg" with dissolve
    pause 1
    "[ffdir]face_rub_03.jpg" with dissolve
    pause 1
    repeat

image ff_presuck01 = "[ffdir]pre_suck_01.jpg"
image ff_presuck02 = "[ffdir]pre_suck_02.jpg"
image ff_postsuck01 = "[ffdir]post_ff_01.jpg"
image ff_postsuck02 = "[ffdir]post_ff_02.jpg"
image ff_postsuck03 = "[ffdir]post_ff_03.jpg"
image ff_postsuck04 = "[ffdir]post_ff_04.jpg"
image ff_postsuck05 = "[ffdir]post_ff_05.jpg"

image ff_exit:
    "[ffdir]post_ff_01.jpg" with dissolve
    pause 0.2
    "[ffdir]post_ff_02.jpg" with dissolve

#video
image ff_start = Movie(play="facefuck/vid/ff_start_pov.webm", mask="facefuck/vid/ff_start_alpha.webm")
image ff_start_alt = Movie(play="facefuck/vid/ff_start_alt.webm", mask="facefuck/vid/ff_start_alpha.webm")
screen ff_start_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_start_alt", "ff_start_alt_screen")
screen ff_start_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_start", "ff_start_screen")

image ff_second = Movie(play="facefuck/vid/ff_second_pov.webm", mask="facefuck/vid/ff_second_alpha.webm")
image ff_second_alt = Movie(play="facefuck/vid/ff_second_alt.webm", mask="facefuck/vid/ff_second_alpha.webm")
screen ff_second_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_second_alt", "ff_second_alt_screen")
screen ff_second_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_second", "ff_second_screen")

image ff_deep = Movie(play="facefuck/vid/ff_deep_pov.webm", mask="facefuck/vid/ff_deep_alpha.webm")
image ff_deep_alt = Movie(play="facefuck/vid/ff_deep_alt.webm", mask="facefuck/vid/ff_deep_alpha.webm")
screen ff_deep_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_deep_alt", "ff_deep_alt_screen")
screen ff_deep_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_deep", "ff_deep_screen")


image ff_throatgrab = Movie(play="facefuck/vid/ff_throatgrab_pov.webm", mask="facefuck/vid/ff_throatgrab_alpha.webm")
image ff_throatgrab_alt = Movie(play="facefuck/vid/ff_throatgrab_alt.webm", mask="facefuck/vid/ff_throatgrab_alpha.webm")
screen ff_throatgrab_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_throatgrab_alt", "ff_throatgrab_alt_screen")
screen ff_throatgrab_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_throatgrab", "ff_throatgrab_screen")


image ff_precum_loop = Movie(play="facefuck/vid/ff_precum_loop.webm", mask="facefuck/vid/ff_precum_loop_alpha.webm")

image ff_endloop = Movie(play="facefuck/vid/ff_cum_end_loop.webm", mask="facefuck/vid/ff_cum_end_loop_alpha.webm")
image ff_endloop_alt = Movie(play="facefuck/vid/ff_cum_end_loop_alt.webm", mask="facefuck/vid/ff_cum_end_loop_alpha.webm")
screen ff_endloop_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_endloop_alt", "ff_endloop_alt_screen")
screen ff_endloop_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "ff_endloop", "ff_endloop_screen")



#sex
#Missionary
define misdir = "sex/mission/"
#images
image pre_mis = "[misdir]pre_still.jpg"
# Insert video
image vag_pre = Movie(play="sex/mission/miss_pre.webm")
image vag_insert = Movie(play="sex/mission/miss_insert.webm")
#Loop 01
image miss_loop_01 = Movie(play="sex/mission/miss_loop01.webm", mask="sex/mission/miss_loop01_mask.webm")
image miss_loop_01_alt = Movie(play="sex/mission/miss_loop01_alt.webm", mask="sex/mission/miss_loop01_mask.webm")
screen miss_loop_01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_loop_01_alt", "miss_loop_01_alt_screen")
screen miss_loop_01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_loop_01", "miss_loop_01_screen")
#Loop 02
image miss_loop_02 = Movie(play="sex/mission/miss_loop02.webm")
image miss_loop_02_alt = Movie(play="sex/mission/miss_loop02_alt.webm")
screen miss_loop_02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_loop_02_alt", "miss_loop_02_alt_screen")
screen miss_loop_02_alt_screen:
        imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_loop_02", "miss_loop_02_screen")


#anal
define analdir = "sex/anal/"
#images
image pre_anal_01 = "[analdir]01_preanal.jpg"
image pre_anal_01b = "[analdir]01_b_preanal.jpg"
image pre_anal_01c = "[analdir]01_c_preanal.jpg"
image pre_anal_02 = "[analdir]02_preanal.jpg"
image pre_anal_02b = "[analdir]02_b_preanal.jpg"
#video
image anal_insert = Movie(play="sex/anal/anal_enter.webm", loop="False")
#anal loop 01
image anal_loop_01 = Movie(play="sex/anal/anal_loop01.webm")
image anal_loop_01_alt = Movie(play="sex/anal/anal_loop01_alt.webm")
screen anal_loop01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_loop_01_alt", "anal_loop01_alt_screen")
screen anal_loop01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_loop_01", "anal_loop01_screen")
#anal loop 02
image anal_loop_02 = Movie(play="sex/anal/anal_loop02.webm")
image anal_loop_02_alt = Movie(play="sex/anal/anal_loop02_alt.webm")
screen anal_loop02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_loop_02_alt", "anal_loop02_alt_screen")
screen anal_loop02_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_loop_02", "anal_loop02_screen")



#On Side
define sidedir = "sex/onside/"
image from_anal = "[sidedir]from_anal.jpg"
image from_vag = "[sidedir]from_vag.jpg"
#On side loop
image side_loop = Movie(play="sex/onside/onSide.webm")
image side_loop_alt = Movie(play="sex/onside/onSide_alt.webm")
screen side_loop_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "side_loop_alt", "side_loop_alt_screen")
screen side_loop_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "side_loop", "side_loop_screen")


#Doggy
define dogdir = "sex/doggy/"
image pre_dog01 = "[dogdir]pre_dog01.jpg"
image pre_dog02 = "[dogdir]pre_dog02.jpg"
image pre_dog03 = "[dogdir]pre_dog03.jpg"
#Insert
image god_insert = Movie(play="sex/doggy/dog_insert.webm")
#Loop 01
image dog_loop01 = Movie(play="sex/doggy/dog_loop01.webm")
image dog_loop01_alt = Movie(play="sex/doggy/dog_loop01_alt.webm")
screen dog_loop01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "dog_loop01_alt", "dog_loop01_alt_screen")
screen dog_loop01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "dog_loop01", "dog_loop01_screen")
#Loop 02
image dog_loop02 = Movie(play="sex/doggy/dog_loop02.webm")
image dog_loop02_alt = Movie(play="sex/doggy/dog_loop02_alt.webm")
screen dog_loop02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "dog_loop02_alt", "dog_loop02_alt_screen")
screen dog_loop02_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "dog_loop02", "dog_loop02_screen")


#Prone
define pronedir = "sex/prone/"
define sharedProne = Movie(play="sex/prone/prone02.webm")
define sharedProne_alt = Movie(play="sex/prone/prone02_alt.webm")

#Anal
#Loop 01
image aprone_loop01 = Movie(play="sex/prone/prone_anal01.webm")
image aprone_loop01_alt = Movie(play="sex/prone/prone_anal01_alt.webm")
screen aprone_loop01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "aprone_loop01_alt", "aprone_loop01_alt_screen")
screen aprone_loop01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "aprone_loop01", "aprone_loop01_screen")
#Loop 02
image aprone_loop02 = sharedProne
image aprone_loop02_alt = sharedProne_alt
screen aprone_loop02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "aprone_loop02_alt", "aprone_loop02_alt_screen")
screen aprone_loop02_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "aprone_loop02", "aprone_loop02_screen")

#Vag
#Loop 01
image vprone_loop01 = Movie(play="sex/prone/prone_vag01.webm")
image vprone_loop01_alt = Movie(play="sex/prone/prone_vag01_alt.webm")
screen vprone_loop01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "vprone_loop01_alt", "vprone_loop01_alt_screen")
screen vprone_loop01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "vprone_loop01", "vprone_loop01_screen")
#Loop 02
image vprone_loop02 = sharedProne
image vprone_loop02_alt = sharedProne_alt
screen vprone_loop02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "vprone_loop02_alt", "vprone_loop02_alt_screen")
screen vprone_loop02_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "vprone_loop02", "vprone_loop02_screen")



#Choke
image turn_choke = "sex/choke/turn_choke.jpg"
#Loop 01
image choke_loop01 = Movie(play="sex/choke/choke_loop01.webm")
image choke_loop01_alt = Movie(play="sex/choke/choke_loop01_alt.webm")
screen choke_loop01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "choke_loop01_alt", "choke_loop01_alt_screen")
screen choke_loop01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "choke_loop01", "choke_loop01_screen")
#Loop 02
image choke_loop02 = Movie(play="sex/choke/choke_loop02.webm")
image choke_loop02_alt = Movie(play="sex/choke/choke_loop02_alt.webm")
screen choke_loop02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "choke_loop02_alt", "choke_loop02_alt_screen")
screen choke_loop02_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "choke_loop02", "choke_loop02_screen")


#Cowgirl
image cg_after_fours = "sex/cowgirl/after_fours.jpg"
image cg_all_fours = "sex/cowgirl/all_fours.jpg"
image cg_insert = "sex/cowgirl/cowgirl_in.jpg"
image cg_crawl_over = "sex/cowgirl/crawl_over.jpg"
image cg_kneeling = "sex/cowgirl/doggy_02.jpg"
image cg_miss = "sex/cowgirl/cowgirl_miss.jpg"
#Loop 01
image cg_loop01 = Movie(play="sex/cowgirl/cow_loop01.webm")
image cg_loop01_alt = Movie(play="sex/cowgirl/cow_loop01_alt.webm")
screen cg_loop01_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_loop01_alt", "cg_loop01_alt_screen")
screen cg_loop01_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_loop01", "cg_loop01_screen")
#Loop 02
image cg_loop02 = Movie(play="sex/cowgirl/cow_loop02.webm")
image cg_loop02_alt = Movie(play="sex/cowgirl/cow_loop02_alt.webm")
screen cg_loop02_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_loop02_alt", "cg_loop02_alt_screen")
screen cg_loop02_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_loop02", "cg_loop02_screen")
#Cum intro
image cg_cumintro = Movie(play="sex/cum_cowgirl/cow_cum_intro.webm")
image cg_cumintro_alt = Movie(play="sex/cum_cowgirl/cow_cum_intro_alt.webm")
screen cg_cumintro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_cumintro_alt", "cg_cumintro_alt_screen")
screen cg_cumintro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_cumintro", "cg_cumintro_screen")
#Actual
image cg_cum = Movie(play="sex/cum_cowgirl/cow_cum_actual.webm", loop="False")
#Cum outro
image cg_cumoutro = Movie(play="sex/cum_cowgirl/cow_cum_outro.webm")
image cg_cumoutro_alt = Movie(play="sex/cum_cowgirl/cow_cum_outro_alt.webm")
screen cg_cumoutro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_cumoutro_alt", "cg_cumoutro_alt_screen")
screen cg_cumoutro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "cg_cumoutro", "cg_cumoutro_screen")
#end
image cg_end_01 = "sex/cum_cowgirl/cg_end_01.jpg"
image cg_end_02 = "sex/cum_cowgirl/cg_end_02.jpg"
image cg_end_03 = "sex/cum_cowgirl/cg_end_03.jpg"
image cg_end_04 = "sex/cum_cowgirl/cg_end_04.jpg"




#Snuff
#Cum intro
image snuff_cumintro = Movie(play="sex/cum_choke/cum_choke_intro.webm")
image snuff_cumintro_alt = Movie(play="sex/cum_choke/cum_choke_intro_alt.webm")
screen snuff_cumintro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "snuff_cumintro_alt", "snuff_cumintro_alt_screen")
screen snuff_cumintro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "snuff_cumintro", "snuff_cumintro_screen")
#Actual
image snuff_cum = Movie(play="sex/cum_choke/cum_choke_actual.webm", loop="False")
#Cum outro
image snuff_cumoutro = Movie(play="sex/cum_choke/cum_choke_outro.webm")
image snuff_cumoutro_alt = Movie(play="sex/cum_choke/cum_choke_outro_alt.webm")
screen snuff_cumoutro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "snuff_cumoutro_alt", "snuff_cumoutro_alt_screen")
screen snuff_cumoutro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "snuff_cumoutro", "snuff_cumoutro_screen")
#end
image snuff_end_01 = "sex/cum_choke/choke_end_01.jpg"
image snuff_end_02 = "sex/cum_choke/choke_end_02.jpg"
image snuff_end_03 = "sex/cum_choke/choke_end_03.jpg"
image snuff_end_04 = "sex/cum_choke/choke_end_04.jpg"



#Anal
#Cum intro
image anal_cumintro = Movie(play="sex/cum_anal/cum_anal_intro.webm")
image anal_cumintro_alt = Movie(play="sex/cum_anal/cum_anal_intro_alt.webm")
screen anal_cumintro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_cumintro_alt", "anal_cumintro_alt_screen")
screen anal_cumintro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_cumintro", "anal_cumintro_screen")
#Actual
image anal_cum = Movie(play="sex/cum_anal/cum_anal_actual.webm", loop="False")
#Cum outro
image anal_cumoutro = Movie(play="sex/cum_anal/cum_anal_outro.webm")
image anal_cumoutro_alt = Movie(play="sex/cum_anal/cum_anal_outro_alt.webm")
screen anal_cumoutro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_cumoutro_alt", "anal_cumoutro_alt_screen")
screen anal_cumoutro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "anal_cumoutro", "anal_cumoutro_screen")
#end
image anal_end_01 = "sex/cum_anal/anal_end_01.jpg"
image anal_end_02 = "sex/cum_anal/anal_end_02.jpg"
image anal_end_03 = "sex/cum_anal/anal_end_03.jpg"
image anal_end_04 = "sex/cum_anal/anal_end_04.jpg"


#Doggy
#Cum intro
image doggy_cumintro = Movie(play="sex/cum_doggy/dog_cum_intro.webm")
image doggy_cumintro_alt = Movie(play="sex/cum_doggy/dog_cum_intro_alt.webm")
screen doggy_cumintro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "doggy_cumintro_alt", "doggy_cumintro_alt_screen")
screen doggy_cumintro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "doggy_cumintro", "doggy_cumintro_screen")
#Actual
image doggy_cum = Movie(play="sex/cum_doggy/dog_cum_actual.webm", loop="False")
#Cum outro
image doggy_cumoutro = Movie(play="sex/cum_doggy/dog_cum_outro.webm")
image doggy_cumoutro_alt = Movie(play="sex/cum_doggy/dog_cum_outro_alt.webm")
screen doggy_cumoutro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "doggy_cumoutro_alt", "doggy_cumoutro_alt_screen")
screen doggy_cumoutro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "doggy_cumoutro", "doggy_cumoutro_screen")
#end
image doggy_end_01 = "sex/cum_doggy/dog_end_01.jpg"
image doggy_end_02 = "sex/cum_doggy/dog_end_02.jpg"
image doggy_end_03 = "sex/cum_doggy/dog_end_03.jpg"
image doggy_end_04 = "sex/cum_doggy/dog_end_04.jpg"



#Miss
#Cum intro
image miss_cumintro = Movie(play="sex/cum_mission/cum_miss_intro.webm")
image miss_cumintro_alt = Movie(play="sex/cum_mission/cum_miss_intro_alt.webm")
screen miss_cumintro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_cumintro_alt", "miss_cumintro_alt_screen")
screen miss_cumintro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_cumintro", "miss_cumintro_screen")
#Actual
image miss_cum = Movie(play="sex/cum_mission/cum_miss_actual.webm", loop="False")
#Cum outro
image miss_cumoutro = Movie(play="sex/cum_mission/cum_miss_outro.webm")
image miss_cumoutro_alt = Movie(play="sex/cum_mission/cum_miss_outro_alt.webm")
screen miss_cumoutro_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_cumoutro_alt", "miss_cumoutro_alt_screen")
screen miss_cumoutro_alt_screen:
    imagebutton idle "alt_button.png" hover "alt_button_hover.png" left_padding 10 top_padding 10 action Function(button_screens, "miss_cumoutro", "miss_cumoutro_screen")
#end
image miss_end_01 = "sex/cum_mission/miss_end_01.jpg"
image miss_end_02 = "sex/cum_mission/miss_end_02.jpg"
image miss_end_03 = "sex/cum_mission/miss_end_03.jpg"
image miss_end_04 = "sex/cum_mission/miss_end_04.jpg"
