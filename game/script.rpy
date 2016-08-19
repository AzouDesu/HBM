# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"


#Ages:
#Dravenia - 26, Fenira - 23, Nagi - 23, Kumiru - 20, Viscella - 19, Kamao - 18

init python:
    
    ku_like = 0.0
    ku_love = 0.0
    ku_dating = False
    
    v_like = 0
    v_love = 0.0
    v_dating = False
    
    n_like = 0.0
    n_love = 0.0
    n_dating = False
    
    ka_like = 0.0
    ka_love = 0.0
    ka_dating = False
    
    f_like = 0.0
    f_love = 0.0
    f_dating = False
    
    d_like = 0.0
    d_love = 0.0
    d_dating = False
    
    a_like = 0.0
    a_love = 0.0
    a_dating = False
    
    narrator_like = 0.0
    
    affection_max = 200.0
    
    stat_spon_caut = 50.0
    stat_coop_comp = 50.0
    stat_relx_dilg = 50.0
    stat_sincerity = 0.0
    
    stat_max = 100
    
    
    # Current Time
    # 0 = 12AM
    # 1 = 3AM
    # 2 = 6AM
    # 3 = 9AM
    # 4 = 12PM
    # 5 = 3PM
    # 6 = 6PM
    # 7 = 9PM

    current_time = 0

    # App Access allows us to access the app that shows us our relationships with everyone
    app_access = False
    clock_access = False
    
    flash = Fade(.25, 0, .75, color="#fff")
    
    flashBlack = Fade(.25, 0, .75, color="#000")
    
    #Functions

    def visAff(affPts):
        tempVar = 0.0  
        tempVar = (100 - stat_coop_comp) - 50.0
        if tempVar >= 0.0:
            ptMod = (tempVar / 50.0) + 1.0
            return affPts * ptMod  
        else:
            ptMod = ((tempVar * -1.0) / 50.0) + 1.0
            return affPts * (1.0 / ptMod) 

    def kumAff(affPts):
        tempVar = 0.0  
        tempVar = stat_spon_caut - 50.0
        if tempVar >= 0.0:
            ptMod = (tempVar / 50.0) + 1.0
            return affPts * ptMod  
        else:
            ptMod = ((tempVar * -1.0) / 50.0) + 1.0
            return affPts * (1.0 / ptMod) 


    def kamAff(affPts):
        tempVar = 0.0  
        tempVar = (100 - stat_spon_caut) - 50.0
        if tempVar >= 0.0:
            ptMod = (tempVar / 50.0) + 1.0
            return affPts * ptMod  
        else:
            ptMod = ((tempVar * -1.0) / 50.0) + 1.0
            return affPts * (1.0 / ptMod) 
            
    def fenAff(affPts):
        tempVar = 0.0  
        tempVar = stat_coop_comp - 50.0
        if tempVar >= 0.0:
            ptMod = (tempVar / 50.0) + 1.0
            return affPts * ptMod  
        else:
            ptMod = ((tempVar * -1.0) / 50.0) + 1.0
            return affPts * (1.0 / ptMod) 
            
    def nagAff(affPts):
        tempVar = 0.0  
        tempVar = (100 - stat_relx_dilg) - 50.0
        if tempVar >= 0.0:
            ptMod = (tempVar / 50.0) + 1.0
            return affPts * ptMod  
        else:
            ptMod = ((tempVar * -1.0) / 50.0) + 1.0
            return affPts * (1.0 / ptMod) 
            
    def draAff(affPts):
        tempVar = 0.0  
        tempVar = stat_relx_dilg - 50.0
        if tempVar >= 0.0:
            ptMod = (tempVar / 50.0) + 1.0
            return affPts * ptMod  
        else:
            ptMod = ((tempVar * -1.0) / 50.0) + 1.0
            return affPts * (1.0 / ptMod) 
            
    def allAff(affPts):
        ptMod = (stat_sincerity / 200.0) + 1.0
        return affPts * ptMod
        
        
    def incTime(time_inc = 1):
        
        global current_time
        
        current_time += time_inc
        
        if current_time > 7 or current_time < 0:
            
            current_time = 0
        
    def setTime(time):
        
        global current_time
        
        if time > 7 or time < 0:
            
            current_time = 0
            
        else:
            
            current_time = time

# Backgrounds
image bg bedroom = "assets/bg/placeholder bedroom day.png"
image bg basement = "assets/bg/placeholder basement.png"
image bg yard = "assets/bg/placeholder garden.png"
image bg void = "assets/bg/void.png"
image bg kitchen = "assets/bg/placeholder kitchen.png"
image bg living = "assets/bg/placeholder living.png"
image bg hallway = "assets/bg/placeholder hallway day.png"
image bg theatre = "assets/bg/placeholder theatre.jpg"
image bg study = "assets/bg/placeholder study.jpg"
image bg gym = "assets/bg/placeholder gym.png"
image bg rec = "assets/bg/placeholder rec.png"
image bg street = "assets/bg/placeholder street.png"


image bg pBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/playerroom.png" # head
        )

image bg kuBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/kumiruroom.png" # head
        )

image bg vBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/viscellaroom.png" # head
        )

image bg nBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/nagiroom.png" # head
        )

image bg kaBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/kamaoroom.png" # head
        )

image bg fBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/feniraroom.png" # head
        )

image bg dBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/draveniaroom.png" # head
        )

image bg aBedroom = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom day.png", # base
        (128, 32), "assets/menus/rooms/alliseroom.png" # head
        )

#NIGHT

image bg pBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/playerroom.png" # head
        )

image bg kuBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/kumiruroom.png" # head
        )

image bg vBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/viscellaroom.png" # head
        )

image bg nBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/nagiroom.png" # head
        )

image bg kaBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/kamaoroom.png" # head
        )

image bg fBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/feniraroom.png" # head
        )

image bg dBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/draveniaroom.png" # head
        )

image bg aBedroom_n = LiveComposite(
        (1280, 800), # Width x Height
        (0, 0), "assets/bg/placeholder bedroom night.png", # base
        (128, 32), "assets/menus/rooms/alliseroom.png" # head
        )



define startpc = Character('You', color="#FFFFFF")
define nameselected = False

# ch1_sc01_01_01
# chapter_scene_decision_choice

# The game starts here.

jump start