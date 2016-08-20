
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
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_angry.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru angry open = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_angry_open.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru confident = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_confident.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru confused = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_confused.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru embarrassed = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_embarrassed.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )
image kumiru flustered = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_flustered.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru happy = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_happy.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru horny = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_horny.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru lovestruck = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_lovestruck.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru neutral = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_neutral.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru sad = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_sad.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru scream = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_scream.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru shocked = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_shocked.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru surprised = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_surprised.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru unamused = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_unamused.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru vangry = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_vangry.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

image kumiru vhorny = LiveComposite(
        (1500, 1518), # Width x Height
        (0, 0), "assets/kumiru/ku_body.png", # base
        (690, 120), "assets/kumiru/ku_face_vhorny.png", # head
        (682, 108), "assets/kumiru/ku_glasses.png", # glasses
        )

transform kumiru_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.6
    yanchor 327
    zoom 1.0
    xzoom 1.0

transform kumiru_center_flipped:
    xpos 0.5
    xanchor 0.5
    ypos 0.6
    yanchor 327
    zoom 1.0
    xzoom -1.0

transform kumiru_right:
    xpos 0.7
    xanchor 0.5
    ypos 0.6
    yanchor 327
    zoom 1.0
    xzoom 1.0
    
transform kumiru_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.6
    yanchor 327
    zoom 1.0
    xzoom -1.0
    
transform kumiru_full:
    xanchor 0.5
    ypos 0.45
    yanchor 327
    xcenter 0.5
    zoom 0.5
    xzoom 1.0

# Viscella

image viscella angry = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_angry.png" # head
        )

image viscella confident = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_confident.png" # head
        )

image viscella confused = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_confused.png" # head
        )

image viscella embarrassed = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_embarrassed.png" # head
        )

image viscella excited = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_excited.png" # head
        )

image viscella flustered = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_flustered.png" # head
        )

image viscella happy = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_happy.png" # head
        )

image viscella horny = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_horny.png" # head
        )

image viscella lovestruck = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_lovestruck.png" # head
        )

image viscella neutral = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_neutral.png" # head
        )

image viscella sad = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_sad.png" # head
        )

image viscella scared = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_scared.png" # head
        )

image viscella scream = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_scream.png" # head
        )

image viscella shocked = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_shocked.png" # head
        )

image viscella unamused = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_unamused.png" # head
        )

image viscella vangry = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_vangry.png" # head
        )

image viscella vhappy = LiveComposite(
        (270, 1320), # Width x Height
        (0, 0), "assets/viscella/vs_body.png", # base
        (42, 114), "assets/viscella/vs_face_vhappy.png" # head
        )

image viscella puddle_neutral = "assets/viscella/vs_puddle_neutral.png"
image viscella puddle_scared = "assets/viscella/vs_puddle_scared.png"
image viscella puddle_happy = "assets/viscella/vs_puddle_happy.png"
image viscella puddle_sad = "assets/viscella/vs_puddle_sad.png"


transform viscella_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.6
    yanchor 260
    zoom 1.0
    xzoom 1.0

transform viscella_center_flipped:
    xpos 0.5
    xanchor 0.5
    ypos 0.6
    yanchor 260
    zoom 1.0
    xzoom -1.0

transform viscella_right:
    xpos 0.7
    xanchor 0.5
    ypos 0.6
    yanchor 260
    zoom 1.0
    xzoom 1.0
    
transform viscella_farright:
    xpos 0.8
    xanchor 0.5
    ypos 0.6
    yanchor 260
    zoom 1.0
    xzoom 1.0
    
transform viscella_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.6
    yanchor 260
    zoom 1.0
    xzoom -1.0
    
transform viscella_full:
    xanchor 0.5
    ypos 0.45
    yanchor 260
    xcenter 0.5
    zoom 0.5
    xzoom -1.0




transform viscella_puddle_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.9
    yanchor 260
    zoom 1.0
    xzoom 1.0
    
transform viscella_puddle_right:
    xpos 0.7
    xanchor 0.5
    ypos 1.0
    yanchor 260
    zoom 1.0
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
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_neutral.png" # head     
        )


image kamao angry = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_angry.png", # head 
        (250, -253), "assets/kamao/gen_vein.png" # vein 
        )

image kamao bored = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_bored.png" # head 
        )

image kamao bluffing = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_bluffing.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao confident = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_confident.png" # head 
        )

image kamao confused = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_confused.png" # head 
        )


image kamao embarrassed = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_embarrassed,unhappy.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao embarrassed_open = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_embarrassed_open.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao flustered = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_flustered.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao happy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_happy.png" # head 
        )

image kamao horny = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_horny.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )
image kamao lovestruck = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_lovestruck,sad.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

image kamao pained = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_pained.png" # head 
        )


image kamao sad = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_lovestruck,sad.png" # head 
        )

image kamao shocked = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_shocked,shockblush.png" # head 
        )
image kamao shocked_open = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_shocked_open.png" # head 
        )
image kamao shockblush = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_shocked,shockblush.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )
image kamao sleepy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_sleepy.png" # head 
        )

image kamao starry = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (82, -253), "assets/kamao/faces/ka_starry.png" # head 
        )

image kamao starry_s = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_silhouette.png"
            ), # base
        (82, -253), "assets/kamao/faces/ka_starry_s.png" # head 
        )

image kamao teasing = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_teasing.png" # head 
        )

image kamao unhappy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_embarrassed,unhappy.png" # head 
        )

image kamao vangry = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_vangry.png", # head 
        (250, -253), "assets/kamao/gen_vein.png" # vein 
        )

image kamao vhappy = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_vhappy.png" # head 
        )

image kamao wink = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_wink,winkblush.png" # head 
        )

image kamao winkblush = LiveComposite(
        (1042, 3067), # Width x Height
        (-2, -581), ConditionSwitch(
            "ka_Outfit == 'default'", "assets/kamao/ka_outfit_default.png"
            ), # base
        (8, 255), "assets/kamao/ka_foxxy.png", # shirtwords   
        (93, -253), "assets/kamao/faces/ka_wink,winkblush.png", # head 
        (70, -165), "assets/kamao/ka_blush.png" # blush 
        )

#Kamao Foxpatch/Flipped

image kamao neutral_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_neutral.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao angry_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_angry.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao bored_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_bored.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao bluffing_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_bluffing.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao confident_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_confident.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao confused_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_confused.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao embarrassed_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_embarrassed.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao embarrassed_open_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_embarrassed_open.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao flustered_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_flustered.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao happy_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_happy.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao horny_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_horny.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao lovestruck_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_lovestruck.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao pained_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_pain.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )


image kamao sad_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_sad.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao shocked_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_shocked.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao shocked_open_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_shocked_open.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao shockblush_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_shockblush.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao sleepy_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_sleepy.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao starry_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_starry.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao starry_s_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body_s.png", # base
        (370, 156), "assets/kamao/ka_face_starry_s.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao teasing_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_teasing.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao unhappy_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_unhappy.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao vangry_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_vangry.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao vhappy_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_vhappy.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao wink_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_wink.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

image kamao winkblush_f = LiveComposite(
        (848, 1534), # Width x Height
        (0, 0), "assets/kamao/ka_body.png", # base
        (370, 156), "assets/kamao/ka_face_winkblush.png", # head
        (334, 396), "assets/kamao/foxpatch.png"
        )

transform kamao_center:
    xpos 0.65
    xanchor 0.5
    ypos 0.93
    yanchor 340
    zoom 0.5
    xzoom 1.0

transform kamao_center_flipped:
    xpos 0.5
    xanchor 0.5
    ypos 0.55
    yanchor 340
    zoom 1.0
    xzoom -1.0

transform kamao_right:
    xpos 0.7
    xanchor 0.5
    ypos 0.55
    yanchor 340
    zoom 1.0
    xzoom 1.0
    
transform kamao_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.55
    yanchor 340
    zoom 1.0
    xzoom -1.0

transform kamao_full:
    xanchor 0.5
    ypos 0.5
    yanchor 340
    xcenter 0.45
    zoom 0.45
    
transform foxpatch_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.55
    yanchor 340
    zoom 1.0
    xzoom 1.0
    
# Fenira

image fenira neutral = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_neutral.png" # head
        )

image fenira angry = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_angry.png" # head
        )

image fenira bluffing = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_bluffing.png", # head
        (704, 162), "assets/fenira/fe_sweat.png"
        )
image fenira confident = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_confident.png" # head
        )

image fenira confused = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_confused.png" # head
        )

image fenira embarrassed = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_embarrassed.png", # head
        (704, 162), "assets/fenira/fe_sweat.png"
        )
image fenira flustered = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_flustered.png", # head
        (704, 162), "assets/fenira/fe_sweat.png"
        )

image fenira happy = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_happy.png" # head
        )

image fenira horny = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_horny.png", # head
        (704, 162), "assets/fenira/fe_sweat.png"
        )
image fenira inquisitive = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_inquisitive.png" # head
        )

image fenira lovestruck = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_lovestruck.png" # head
        )

image fenira sad = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_sad.png" # head
        )

image fenira shocked = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_shocked.png" # head
        )

image fenira smirk = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_smirk.png" # head
        )

image fenira teasing = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_teasing.png" # head
        )

image fenira vangry = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_vangry.png" # head
        )

image fenira vhappy = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_vhappy.png" # head
        )

image fenira wink = LiveComposite(
        (1564, 1696), # Width x Height
        (0, 0), "assets/fenira/fe_body.png", # base
        (704, 138), "assets/fenira/fe_face_wink.png" # head
        )

transform fenira_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.5
    yanchor 330
    zoom 1.0
    xzoom 1.0

transform fenira_center_flipped:
    xpos 0.5
    xanchor 0.5
    ypos 0.5
    yanchor 330
    zoom 1.0
    xzoom -1.0

transform fenira_right:
    xpos 0.7
    xanchor 0.5
    ypos 0.5
    yanchor 330
    zoom 1.0
    xzoom 1.0
    
transform fenira_left:
    xpos 0.3
    xanchor 0.5
    ypos 0.5
    yanchor 330
    zoom 1.0
    xzoom -1.0

transform fenira_full:
    xanchor 677
    ypos 0.5
    yanchor 327
    xcenter 0.5
    zoom 0.4

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

