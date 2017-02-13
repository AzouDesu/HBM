# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


############################
# Clock

    # Current Time
    # 0 = 12AM
    # 1 = 3AM
    # 2 = 6AM
    # 3 = 9AM
    # 4 = 12PM
    # 5 = 3PM
    # 6 = 6PM
    # 7 = 9PM

    screen clock:
        
        if clock_access:
            
            if current_time == 0:
                
                add "assets/menus/clock/12am.png" xalign 0.0 yalign 0.0
                
            elif current_time == 1:
                
                add "assets/menus/clock/3am.png" xalign 0.0 yalign 0.0
                
            elif current_time == 2:
               
                add "assets/menus/clock/6am.png" xalign 0.0 yalign 0.0
                
            elif current_time == 3:
                
                add "assets/menus/clock/9am.png" xalign 0.0 yalign 0.0
                
            elif current_time == 4:
                
                add "assets/menus/clock/12pm.png" xalign 0.0 yalign 0.0
                
            elif current_time == 5:
                
                add "assets/menus/clock/3pm.png" xalign 0.0 yalign 0.0
                
            elif current_time == 6:
                
                add "assets/menus/clock/6pm.png" xalign 0.0 yalign 0.0
                
            elif current_time == 7:
                
                add "assets/menus/clock/9pm.png" xalign 0.0 yalign 0.0
                
            else:
                
                add "assets/menus/clock/12am.png" xalign 0.0 yalign 0.0

############################
# Affection Button

screen button:
    if app_access:
        vbox xalign 1.0 yalign 0.0:
            imagebutton:
                idle "assets/menus/button_rl.png"
                hover "assets/menus/button_rlh.png"
                activate_sound "assets/sound/sfx/blip.wav"
                #action ui.callsinnewcontext("aff_screen_label")
                action Show("aff_screen", dissolve)             
    
###########################
# Affection Screen

screen aff_screen:
    
    modal True
     
    add "assets/menus/phonebg.png" xalign 0.5 yalign 0.5
    
    #Play("sound", "assets/sounds/sfx/blip.wav")
    
    #Diff between chars: 51y
    #Diff between char bars: 42y
    
    #Aligns:
    
    #Diff between chars: 0.065
    #Diff between char bars: 0.054
    
    #add "assets/menus/phonebg.png" xalign 0.5 yalign 0.5
    
    if gamedebug:
        bar xalign 0.51 yalign 0.118 value FieldValue(store, "ku_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.172 value FieldValue(store, "ku_love", affection_max) range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.237 value FieldValue(store, "v_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.291 value FieldValue(store, "v_love", affection_max) range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.356 value FieldValue(store, "n_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.410 value FieldValue(store, "n_love", affection_max) range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.475 value FieldValue(store, "ka_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.529 value FieldValue(store, "ka_love", affection_max) range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.594 value FieldValue(store, "f_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.648 value FieldValue(store, "f_love", affection_max) range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.713 value FieldValue(store, "d_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.767 value FieldValue(store, "d_love", affection_max) range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.832 value FieldValue(store, "a_like", affection_max) range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.885 value FieldValue(store, "a_love", affection_max) range affection_max style "love_bar"

    else:
        bar xalign 0.51 yalign 0.118 value ku_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.172 value ku_love range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.237 value v_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.291 value v_love range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.356 value n_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.410 value n_love range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.475 value ka_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.529 value ka_love range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.594 value f_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.648 value f_love range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.713 value d_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.767 value d_love range affection_max style "love_bar"
        
        bar xalign 0.51 yalign 0.832 value a_like range affection_max style "like_bar"
        bar xalign 0.51 yalign 0.885 value a_love range affection_max style "love_bar"
    
    add "assets/menus/relationshipscreen.png" xalign 0.5 yalign 0.5
    add "assets/menus/relationshipscreenpips.png" xalign 0.5 yalign 0.5
    
    # 0.131
    
    #94y distance
    
    if ku_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.108
        
    if v_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.239
    
    if n_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.37
    
    if ka_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.501
    
    if f_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.632 
    
    if d_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.763
    
    if a_dating:
        add "assets/menus/heartwallpaper.png" xalign 0.50 yalign 0.894

    add "assets/menus/icons.png" xalign 0.34 yalign 0.5
    
    vbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "assets/menus/button_rl.png"
            hover "assets/menus/button_rlh.png"
            activate_sound "assets/sound/sfx/blip.wav"
            action Hide("aff_screen", dissolve)

#    vbox xalign 0.765 yalign 0.5:
#        imagebutton:
#            idle "assets/menus/button_next.png"
#            hover "assets/menus/button_nexth.png"
#            activate_sound "assets/sound/sfx/blip.wav"
#            action [Hide("aff_screen"), Show("stat_screen")]
            
screen stat_screen:
    
    modal True
    
    #Play("sound", "assets/sounds/sfx/blip.wav")
    
    #Diff between chars: 66y
    #Diff between char bars: 27y
    
    add "assets/menus/phonebg.png" xalign 0.5 yalign 0.5
    
    bar pos (345,142) value stat_spon_caut range stat_max style "sc_bar"
    
    bar pos (345,361) value stat_coop_comp range stat_max style "cc_bar"
    
    bar pos (345,577) value stat_relx_dilg range stat_max style "rd_bar"
    
    add "assets/menus/statscreen.png" xalign 0.5 yalign 0.5
    
    vbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "assets/menus/button_rl.png"
            hover "assets/menus/button_rlh.png"
            activate_sound "assets/sound/sfx/blip.wav"
            action Hide("stat_screen", dissolve)

    vbox xalign 0.765 yalign 0.5:
        imagebutton:
            idle "assets/menus/button_next.png"
            hover "assets/menus/button_nexth.png"
            activate_sound "assets/sound/sfx/blip.wav"
            action [Hide("stat_screen"), Show("aff_screen")]

label aff_screen_label:
    call screen aff_screen
    return
    
label stat_screen_label:
    call screen stat_screen
    return