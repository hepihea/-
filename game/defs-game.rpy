

init python:

    r_limit = 5
    s_limit = 7
    current_screen = ""

    def hide_zoom_screens():
        renpy.hide_screen("topOffScreen")
        renpy.hide_screen("pantsOffScreen")
        renpy.hide_screen("topOffHappyScreen")
        renpy.hide_screen("nakedHappyScreen")
        renpy.hide_screen("roughTopOffScreen")
        renpy.hide_screen("roughNakedScreen")
        renpy.hide_screen("phBedSitScreen")
        renpy.hide_screen("phBedSpreadScreen")
        renpy.hide_screen("ph_face_focus")
        renpy.hide_screen("ph_body_focus")
        renpy.hide_screen("pervAssScreen")
        renpy.hide_screen("pervLegsUpScreen")
        renpy.hide_screen("pervLegUpScreen")
        renpy.hide_screen("")
        renpy.hide_screen("")

    def hide_overlay():
        global current_screen
        renpy.hide_screen(current_screen)
        current_screen = ""
        hide_zoom_screens()


    def button_screens( scenename, show_screen ):
        global current_screen
        if scenename == None:
            raise Exception ("Scene cannot be None!")
        renpy.transition(dissolve)
        renpy.scene()
        renpy.show(scenename, layer = "master")
        renpy.hide_screen(current_screen)
        current_screen = show_screen
        renpy.show_screen(show_screen)
        return None


    def wait(t):
        renpy.pause(t)


    renpy.music.set_music(5, True)





#Character definitions

define clem_name = "???"
define clem = Character("[clem_name]", color="#e679e3", what_outlines=[(1, "000")])

define povname = ">>>"
define p = Character("[povname]", color="#5660E8" , what_outlines=[(1, "000")])
define narrator = Character(None, what_outlines=[(1, "000")])

define man = Character("Man", color="#a9a9a9", what_outlines=[(1, "000")])

#transitions
define flash_sharp = Fade(.1, 0.1, .5, color="#fff")
define flash = Fade(.3, 0.1, .5, color="#fff")
define dissolve_set = Dissolve(0.2)


#Scene and general image defs
image black_screen = "black.png"

#intro
image door1 = "intro/door1.jpg"
image door2 = "intro/door2.jpg"
image door3 = "intro/door3.jpg"


image contb = "gui/cont_button.png"

image const = "construction.jpg"


#misc
define cp = "Change position..."
define kg = "Keep going..."
define sd = "Slow down..."
define su = "Go faster..."
