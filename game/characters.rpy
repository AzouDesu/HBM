
# Declare characters used by this game.

define v = Character('Viscella', color="#3dc4e2")
define v_un = Character('???', color="#3dc4e2")
define ku = Character('Kumiru', color="#b60b0b")
define ku_un = Character('???', color="#b60b0b")
define n = Character('Nagi', color="#40c535")
define n_un = Character('???', color="#40c535")
define ka = Character('Kamao', color="#4070f9")
define ka_un = Character('???', color="#4070f9")
define f = Character('Fenira', color="#dd3c22")
define f_un = Character('???', color="#dd3c22")
define d = Character('Dravenia', color="#ffe749")
define d_un = Character('???', color="#ffe749")
define a = Character('Allise', color="#9236c6")
define a_un = Character('???', color="#9236c6")
define unknown = Character('???')
define pc = Character('???')

define voice_a = Character('Friendly Voice') 
define voice_b = Character('Familiar Voice') 

# Nicknames

define pc_ka = "???"
define pc_ku = "???"
define pc_d = "???"
define pc_f = "???"
define pc_v = "???"
define pc_n = "???"
define pc_a = "???"

# Allise

image allise silhouette = "assets/allise/al_body_s2.png"

image allise neutral = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_neutral.png" # head
        )

image allise angry = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_angry.png" # head
        )

image allise embarrassed = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_embarrassed.png" # head
        )

image allise happy = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_happy.png" # head
        )

image allise horny = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_horny.png" # head
        )

image allise lovestruck = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_lovestruck.png" # head
        )

image allise sad = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_sad.png" # head
        )

image allise e_neutral = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body_e.png", # base
        (256, 124), "assets/allise/al_face_e_neutral.png" # head
        )

image allise e_angry = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body_e.png", # base
        (256, 124), "assets/allise/al_face_e_angry.png" # head
        )

image allise e_sad = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body_e.png", # base
        (256, 124), "assets/allise/al_face_e_sad.png" # head
        )

image allise vsad = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_sad.png", # head
        (262, 146), "assets/allise/al_tears.png" #tears
        )

image allise closed = LiveComposite(
        (629, 1504), # Width x Height
        (0, 0), "assets/allise/al_body.png", # base
        (256, 124), "assets/allise/al_face_closed.png" # head
        )



transform allise_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.55
    yanchor 275
    zoom 1.0
    xzoom 1.0

transform allise_center_flipped:
    xpos 0.5
    xanchor 0.5
    ypos 0.55
    yanchor 275
    zoom 1.0
    xzoom -1.0

transform allise_right:
    xpos 0.7
    xanchor 0.5
    ypos 0.55
    yanchor 275
    zoom 1.0
    xzoom 1.0
    
transform allise_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.55
    yanchor 275
    zoom 1.0
    xzoom -1.0
    
transform allise_full:
    xanchor 0.5
    ypos 0.55
    yanchor 275
    xcenter 0.52
    zoom 0.4
    xzoom 1.0



# Kumiru

image kumiru angry = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_angry.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses
        (1220, 200), "assets/gen_vein.png" # vein 
        
        )

image kumiru angry_open = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_angry_open.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses
        (1220, 200), "assets/gen_vein.png" # vein 
        )

image kumiru confident = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_confident.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru confused = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_confused.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru embarrassed = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_embarrassed.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses   
        (1075, 310), "assets/kumiru/ku_blush.png" # blush 
        )
image kumiru flustered = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_flustered.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses   
        (1075, 310), "assets/kumiru/ku_blush.png" # blush 
        )

image kumiru happy = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_happy.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses   
        )

image kumiru horny = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_horny.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses   
        (1075, 310), "assets/kumiru/ku_blush.png" # blush 
        )

image kumiru lovestruck = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_lovestruck.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses   
        (1075, 310), "assets/kumiru/ku_blush.png" # blush 
        )


image kumiru neutral = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_neutral.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses   
        )


image kumiru sad = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_sad.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru scream = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_scream.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru shocked = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_shocked.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru surprised = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_surprised.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru unamused = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_unamused.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png" # glasses
        )

image kumiru vangry = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 245), "assets/kumiru/faces/ku_vangry.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses
        (1220, 200), "assets/gen_vein.png" # vein 
        )

image kumiru vhorny = LiveComposite(
        (2687, 3036), # Width x Height
        (0, 0), ConditionSwitch(
            "ku_Outfit == 'default'", "assets/kumiru/ku_outfit_default.png"
            ), # base
        (1080, 248), "assets/kumiru/faces/ku_vhorny.png", # head     
        (1052, 245), "assets/kumiru/ku_glasses.png", # glasses   
        (1075, 310), "assets/kumiru/ku_blush.png" # blush 
        )
    
transform kumiru_center:
    xpos 0.5
    xanchor 0.45
    ypos 0.60
    yanchor 327
    zoom 0.5
    xzoom 1.0

transform kumiru_center_flipped:
    xpos 0.5
    xanchor 0.55
    ypos 0.6
    yanchor 327
    zoom 0.5
    xzoom -1.0

transform kumiru_right:
    xpos 0.67
    xanchor 0.45
    ypos 0.6
    yanchor 327
    zoom 0.5
    xzoom 1.0
    
transform kumiru_left:
    xpos 0.33
    xanchor 0.55
    ypos 0.6
    yanchor 327
    zoom 0.5
    xzoom -1.0
    
transform kumiru_legs:
    xpos 0.5
    xanchor 0.45
    ycenter 0.65
    zoom 0.5
    xzoom 1.0


# Viscella

image viscella angry = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_angry.png" # head
        )

image viscella confident = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_confident.png" # head
        )

image viscella confused = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_confused.png" # head
        )

image viscella embarrassed = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_embarrassed.png", # head
        (100, 290), "assets/viscella/v_blush.png" # head     
        )

image viscella excited = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_excited.png" # head 
        )

image viscella flustered = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_flustered.png", # head
        (100, 290), "assets/viscella/v_blush.png" # head     
        )
        
image viscella happy = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_happy.png" # head  
        )
        
image viscella horny = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_horny.png", # head
        (100, 290), "assets/viscella/v_blush.png" # head     
        )

image viscella lovestruck = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_lovestruck.png", # head
        (100, 290), "assets/viscella/v_blush.png" # head     
        )

image viscella neutral = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_neutral.png" # head     
        )

image viscella sad = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_sad.png" # head 
        )

image viscella scared = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_scared.png" # head
        )

image viscella scream = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_scream.png" # head
        )

image viscella shocked = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_shocked.png" # head  
        )

image viscella unamused = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_unamused.png" # head
        )

image viscella vangry = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_vangry.png" # head
        )

image viscella vhappy = LiveComposite(
        (542, 2643), # Width x Height
        (0, 0), ConditionSwitch(
            "v_Outfit == 'default'", "assets/viscella/v_outfit_default.png"
            ), # base
        (97, 232), "assets/viscella/faces/v_vhappy.png" # head 
        )


image viscella puddle_neutral = LiveComposite(
        (1626, 623), # Width x Height
        (97, 232), "assets/viscella/v_puddle.png", # head 
        (1130, 320), "assets/viscella/v_puddle_neutral.png" # head 
        )

image viscella puddle_happy = LiveComposite(
        (1626, 623), # Width x Height
        (97, 232), "assets/viscella/v_puddle.png", # head 
        (1130, 320), "assets/viscella/v_puddle_happy.png" # head 
        )

image viscella puddle_sad = LiveComposite(
        (1626, 623), # Width x Height
        (97, 232), "assets/viscella/v_puddle.png", # head 
        (1130, 320), "assets/viscella/v_puddle_sad.png" # head 
        )

image viscella puddle_scared = LiveComposite(
        (1626, 623), # Width x Height
        (97, 232), "assets/viscella/v_puddle.png", # head 
        (1130, 320), "assets/viscella/v_puddle_scared.png" # head 
        )

transform viscella_center:
    xpos 0.5
    xanchor 0.4
    ypos 0.6
    yanchor 260
    zoom 0.5
    xzoom 1.0

transform viscella_center_flipped:
    xpos 0.5
    xanchor 0.6
    ypos 0.6
    yanchor 260
    zoom 0.5
    xzoom -1.0

transform viscella_right:
    xpos 0.67
    xanchor 0.4
    ypos 0.6
    yanchor 260
    zoom 0.5
    xzoom 1.0
    
transform viscella_farright:
    xpos 0.83
    xanchor 0.4
    ypos 0.6
    yanchor 260
    zoom 0.5
    xzoom 1.0
    
transform viscella_left:
    xpos 0.33
    xanchor 0.6
    ypos 0.6
    yanchor 260
    zoom 0.5
    xzoom -1.0

transform viscella_farleft:
    xpos 0.17
    xanchor 0.6
    ypos 0.6
    yanchor 260
    zoom 0.5
    xzoom -1.0


transform viscella_puddle_center:
    xpos 0.45
    xanchor 0.5
    ypos 0.7
    yanchor 260
    zoom 0.5
    xzoom 1.0
    
transform viscella_puddle_right:
    xpos 0.6
    xanchor 0.5
    ypos 0.7
    yanchor 260
    zoom 0.5
    xzoom 1.0



# Nagi

image nagi neutral = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_neutral.png" # head
        )

image nagi angry = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_angry.png" # head
        )

image nagi bored = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_bored.png" # head
        )

image nagi confident = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_confident.png" # head
        )

image nagi confused = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_confused.png" # head
        )

image nagi embarrassed = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_embarrassed.png" # head
        )

image nagi flustered = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_flustered.png" # head
        )


image nagi happy = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_happy.png" # head
        )

image nagi horny = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_horny.png" # head
        )

image nagi lovestruck = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_lovestruck.png" # head
        )

image nagi sad = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_sad.png" # head
        )

image nagi surprised = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_surprised.png" # head
        )

image nagi teasing = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_teasing.png" # head
        )

image nagi wink = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_wink.png" # head
        )

image nagi closed = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_closed.png" # head
        )

image nagi tired = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_bored.png", # head
        (504, 160), "assets/nagi/na_face_eyebags.png" #eye bags
        )

image nagi tired_closed = LiveComposite(
        (1202, 1556), # Width x Height
        (0, 0), "assets/nagi/na_body.png", # base
        (500, 126), "assets/nagi/na_face_closed.png", # head
        (504, 160), "assets/nagi/na_face_eyebags.png" #eye bags
        )



transform nagi_center:
    xpos 0.5
    xanchor 525
    ypos 0.55
    yanchor 327
    zoom 1.0
    xzoom 1.0

transform nagi_center_flipped:
    xpos 0.55
    xanchor 677
    ypos 0.55
    yanchor 327
    zoom 1.0
    xzoom -1.0

transform nagi_right:
    xpos 0.7
    xanchor 525
    ypos 0.55
    yanchor 327
    zoom 1.0
    xzoom 1.0
    
transform nagi_left:
    xpos 0.35
    xanchor 677
    ypos 0.55
    yanchor 327
    zoom 1.0
    xzoom -1.0
    
transform nagi_full:
    xanchor 677
    ypos 0.5
    yanchor 327
    xcenter 0.5
    zoom 0.4
    xzoom -1.0

# Kamao

#Valid outfits:
#       'default'

image kamao neutral = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_neutral.png" # head     
        )


image kamao angry = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_angry.png", # head 
        (250, -253), "assets/gen_vein.png" # vein 
        )

image kamao bored = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_bored.png" # head 
        )

image kamao bluffing = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_bluffing.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao confident = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_confident.png" # head 
        )

image kamao confused = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_confused.png" # head 
        )


image kamao embarrassed = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_embarrassed,unhappy.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao embarrassed_open = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base  
        (93, -253), "assets/kamao/faces/ka_embarrassed_open.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao flustered = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_flustered.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao happy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_happy.png" # head 
        )

image kamao horny = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_horny.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )
image kamao lovestruck = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_lovestruck,sad.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao pained = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_pained.png" # head 
        )


image kamao sad = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_lovestruck,sad.png" # head 
        )

image kamao shocked = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_shocked,shockblush.png" # head 
        )
image kamao shocked_open = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base   
        (93, -253), "assets/kamao/faces/ka_shocked_open.png" # head 
        )
image kamao shockblush = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_shocked,shockblush.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )
image kamao sleepy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base 
        (93, -253), "assets/kamao/faces/ka_sleepy.png" # head 
        )

image kamao starry = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (82, -253), "assets/kamao/faces/ka_starry.png" # head 
        )

image kamao starry_s = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_silhouette.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (82, -253), "assets/kamao/faces/ka_starry_s.png" # head 
        )

image kamao teasing = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_teasing.png" # head 
        )

image kamao unhappy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_embarrassed,unhappy.png" # head 
        )

image kamao vangry = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_vangry.png", # head 
        (250, -253), "assets/gen_vein.png" # vein 
        )

image kamao vhappy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_vhappy.png" # head 
        )

image kamao wink = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base 
        (93, -253), "assets/kamao/faces/ka_wink,winkblush.png" # head 
        )

image kamao winkblush = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png",
            "ka_Outfit == 'default_f'", "assets/kamao/ka_outfit_default_f.png"
            ), # base
        (93, -253), "assets/kamao/faces/ka_wink,winkblush.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )


transform kamao_center:
    xpos 0.5
    xanchor 0.2
    ypos 0.93
    yanchor 340
    zoom 0.5
    xzoom 1.0
    
transform kamao_center_flipped:
    xpos 0.5
    xanchor 0.8
    ypos 0.93
    yanchor 340
    zoom 0.5
    xzoom -1.0

transform kamao_right:
    xpos 0.67
    xanchor 0.2
    ypos 0.93
    yanchor 340
    zoom 0.5
    xzoom 1.0
    
transform kamao_left:
    xpos 0.33
    xanchor 0.8
    ypos 0.93
    yanchor 340
    zoom 0.5
    xzoom -1.0

    
# Fenira

image fenira neutral = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ),
        (355, 354), "assets/fenira/faces/f_neutral.png"
        )

image fenira angry = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_angry.png", 
        (500, 325), "assets/gen_vein.png"
        )

image fenira bluffing = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_bluffing.png",  
        (355, 430), "assets/fenira/f_blush.png", 
        )
image fenira confident = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_confident,horny.png"  
        )

image fenira confused = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_confused.png"  
        )

image fenira embarrassed = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_embarrassed.png",  
        (340, 327), "assets/fenira/f_sweat.png", 
        (355, 430), "assets/fenira/f_blush.png" 
        )
image fenira flustered = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_flustered.png", 
        (340, 327), "assets/fenira/f_sweat.png", 
        (355, 430), "assets/fenira/f_blush.png" 
        )

image fenira happy = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_happy.png"
        )

image fenira horny = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_confident,horny.png",
        (340, 327), "assets/fenira/f_sweat.png",
        (355, 430), "assets/fenira/f_blush.png"
        )

image fenira horny_open = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_horny_open.png",
        (340, 327), "assets/fenira/f_sweat.png",
        (355, 430), "assets/fenira/f_blush.png"
        )

image fenira inquisitive = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_inquisitive.png",  
        )

image fenira lovestruck = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_lovestruck,sad.png", 
        (355, 430), "assets/fenira/f_blush.png" 
        )

image fenira sad = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_lovestruck,sad.png" 
        )

image fenira shocked = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_shocked.png"
        )

image fenira smirk = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_smirk.png"
        )

image fenira smirk_open = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_smirk_open.png"
        )

image fenira vangry = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_vangry.png", 
        (500, 325), "assets/gen_vein.png"
        )

image fenira vhappy = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_vhappy.png"
        )

image fenira wink = LiveComposite(
        (2045, 3404), # Width x Height
        (0, 0), ConditionSwitch(
            "f_Outfit == 'default'", "assets/fenira/f_outfit_default.png"
            ), 
        (355, 354), "assets/fenira/faces/f_wink.png"
        )

transform fenira_center:
    xpos 0.5
    xanchor 0.25
    ypos 0.5
    yanchor 330
    zoom 0.5
    xzoom 1.0

transform fenira_center_flipped:
    xpos 0.5
    xanchor 0.75
    ypos 0.5
    yanchor 330
    zoom 0.5
    xzoom -1.0

transform fenira_right:
    xpos 0.68
    xanchor 0.25
    ypos 0.5
    yanchor 330
    zoom 0.5
    xzoom 1.0
    
transform fenira_left:
    xpos 0.32
    xanchor 0.75
    ypos 0.5
    yanchor 330
    zoom 0.5
    xzoom -1.0

# Dravenia

image dravenia neutral = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_neutral.png" # head
        )

image dravenia angry = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_angry.png" # head
        )

image dravenia vangry = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_vangry.png" # head
        )

image dravenia embarrassed = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_embarrassed.png" # head
        )

image dravenia flustered = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_flustered.png" # head
        )

image dravenia happy = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_happy.png" # head
        )

image dravenia horny = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_horny.png" # head
        )

image dravenia lovestruck = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_lovestruck.png" # head
        )

image dravenia sad = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_sad.png" # head
        )

image dravenia stern = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_stern.png" # head
        )

image dravenia surprised = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_surprised.png" # head
        )

image dravenia vflustered = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_vflustered.png" # head
        )

image dravenia vhorny = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_vhorny.png" # head
        )

image dravenia confused = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_confused.png" # head
        )

image dravenia smug = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_smug.png" # head
        )

image dravenia confident = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_confident.png" # head
        )

image dravenia closed = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_closed.png" # head
        )

image dravenia flamethrower = LiveComposite(
        (932, 1682), # Width x Height
        (0, 0), "assets/dravenia/dr_body.png", # base
        (372, 98), "assets/dravenia/dr_face_vflustered.png", # head
        (186, 174), "assets/dravenia/dr_flamethrower.png"
        )

transform dravenia_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.5
    yanchor 381
    zoom 1.0
    xzoom 1.0

transform dravenia_center_flipped:
    xpos 0.5
    xanchor 0.5
    ypos 0.5
    yanchor 381
    zoom 1.0
    xzoom -1.0

transform dravenia_right:
    xpos 0.7
    xanchor 0.5
    ypos 0.5
    yanchor 381
    zoom 1.0
    xzoom 1.0
    
transform dravenia_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.5
    yanchor 381
    zoom 1.0
    xzoom -1.0
    
transform dravenia_farleft:
    xpos 0.2
    xanchor 0.5
    ypos 0.5
    yanchor 381
    zoom 1.0
    xzoom -1.0
    
transform dravenia_full:
    xanchor 0.5
    ypos 0.5
    yanchor 381
    xcenter 0.52
    zoom 0.4
    xzoom 1.0

