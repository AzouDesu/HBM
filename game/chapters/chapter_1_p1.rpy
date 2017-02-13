
label start:
    
    python:
        flag_DriderSeen = False
        flag_BondhouseExplained = False
        flag_RoomBesideKumiru = True
        flag_FeniraToldAmnesia = False
        flag_ViscellaCalledJailbait = False
        flag_FeniraRacismName = False
        flag_OfferedFeniraUnpackHelp = False
        flag_HelpedViscellaLie = False
        flag_FeniraHideAndSeekLied = False
        flag_AcceptedFeniraChallenge = False
        flag_VisitedNagi = False
        flag_VisitedKamao = False
        flag_VisitedFenira = False
        flags_NagiCourtFenSupport = 0
        
    
    show screen clock
    
    show screen calendar
    
    $ app_access = True
    
    $ calendar_access = True
    
    show screen button
    
    stop music fadeout 1.0
    
    scene bg void 
    
    $ renpy.pause(2.0)
    
    "WARNING: GAME IS WORK IN PROGRESS. MAY (WILL) CONTAIN PLACEHOLDER ART."
    
    play music "assets/sound/bgm/noodle.mp3"
    

    scene bg void with Dissolve(4.0)
    
    if gamedebug == True:
    
        #scene debugscreen
        
        "GAME IS IN DEBUG MODE."
        
        "TESTING"
        ###

        
        ###
        "END TESTING"
        
    $ renpy.pause(3.0)
        

    "It's cold."
    
    "Very cold."
    
    "I can't sense anything. Not a sight, a sound, or a touch."
    
    "How long have I been here?"
    
    "Just a moment? Forever? I'm not sure. Is time even progressing normally?"
    
    "I briefly consider the possibility that I'm dead. If so, that's a pretty big let-down."
    
    "My worries are cut short, however, by a strange new sensation. The sensation of being watched."
    
    "After a moment, I realize I can still see, and can even make out a shape in the darkness..."
    
    show allise silhouette at allise_center with dissolve
    
    ""
    
    "It looks like a person..."
    
    "Right?"
    
    a_un "..."
    
    a_un "....."

    menu: 
        "Say something.":
            
            "I attempt to speak to the silhouette, but I find the words do not come. In fact, now that I think about it, I haven't been breathing much. Actually, scratch that - I haven't been breathing at all."
            
            a_un "Do you remember your name?"
            
        "Stay quiet.":
            
            "I decide to remain silent. I'm not sure if I could speak even if I wanted to."
            
            a_un "..."
            
            "The silence lasts a long time..."
            
            "Or maybe it lasts no time at all. I'm not sure."
            
            "As I begin to consider volunteering a word or two, my thoughts are interrupted."
            
    a_un "Do you remember your name?"
    
    "A voice?"
    
    "It came from inside my head, and it certainly wasn't mine."
    
    "It must belong to the silhouette, and I'm guessing the question was addressed to me."
    
    jump nameSelect
            
        
    
label nameSelect:
    
    $ pc = renpy.input("What is my name?")
    
    $ pc = pc.strip()
    
    if pc == "":
        
        a_un "Did you forget?"
        
        jump nameSelect
    
    menu:
        a_un "%(pc)s?"
        
        "Yes, %(pc)s.":
            
            $ nameselected = True
            
            $ pc_ka = pc
            $ pc_ku = pc
            $ pc_d = pc
            $ pc_f = pc
            $ pc_v = pc
            $ pc_n = pc
            $ pc_a = pc
            
            jump ch1_scene01
                
        "Actually, maybe it was...":
            
            $ nameselected = False
            
            jump nameSelect
    
    
label ch1_scene01:

    a_un "Hmm. You remember."
    
    menu:
        "'Who are you?'":
        
            "There is a moment of silence. The being seems to hesitate."
            
            a_un "That is not important anymore."
            
        "'Where are we?'":
        
            a_un "Travelling."
            
            pc "Travelling? Travelling to where?"
            
            a_un "Back."
            
            pc "Back to where?"
            
        "'Do you know me?'":
            
            a_un "Yes."
            
    a_un "Prepare yourself. This may sting."
    
    a_un "And..."
    
    stop music fadeout 3.0
    
    "I feel something wrench inside of me."
    
    a_un "Goodbye."
    
    hide allise with flashBlack
    
    "And just like that, I'm alone."
    
    "The silence begins to close in on me."
    
    play sound "assets/sound/sfx/heartbeat_slow.wav" fadein 1.0 loop
    
    "Suddenly, I feel a wave of heat coursing through my body."
    
    "It starts as a welcome warmth, that returns feeling and sensation to my cool skin. Oh, yes. Skin. I had that, didn't I?"
    
    "I smile. It feels nice. It's getting warmer and warmer."
    
    $ renpy.pause(2.0)
    
    "I feel weightless, but at least now I can feel my body."
    
    "The warmth tingles."
    
    $ renpy.pause(2.0)
    
    play sound "assets/sound/sfx/heartbeat_med.wav" loop
    
    "I start to sweat."
    
    "The temperature is still rising."
    
    $ renpy.pause(2.0)
    
    "The warmth is growing uncomfortably hot. It accelerates."
    
    $ renpy.pause(2.0)
    
    play sound "assets/sound/sfx/heartbeat_fast.wav" loop
    
    "Painfully hot."
    
    $ renpy.pause(2.0)
    
    "Now agonizingly hot."
    
    $ renpy.pause(2.0)
    
    "In mere moments my skin feels like it's on fire, and I become keenly conscious that my body seems to be... shrinking? Expanding? Or am I being crushed? Maybe all of the above?"
    
    "Suddenly, I feel as if my entire body is being sucked through a pinhole."
    
    "I don't have time to cry out - it only takes a moment."
    
    show black
    
    stop sound fadeout 1.0
    
    $ renpy.pause(1.0)
    
    play sound "assets/sound/sfx/lift.ogg" fadein 1.0
    
    $ renpy.pause(4.0, hard = True)
    
    play sound "assets/sound/sfx/morning.ogg"
    
    $ renpy.pause(2.0, hard = True)
    
    "Birds?"
    
    "I can feel a gentle breeze against my face, and it feels warm - like I'm lying under the sun."
    
    "I try to open my eyes, but find it more difficult than I last remembered it being. I give up and lay still, hoping to recover my energy."
    
    "It's not long before I discover I'm not alone."
    
    play music "assets/sound/bgm/scene_comi1.ogg" fadein 3.0
    
    v_un "Is... is he d-dead?"
    
    ku_un "I don't think so. I certainly hope not."
    
    v_un "Did he fall?"
    
    ku_un "Of course not. Where would he have fallen from?"
    
    v_un "But he wasn't there a second ago... It's like he appeared out of nowhere."
    
    ku_un "It seems so, doesn't it? Oh, do be careful, Viscella! You're dripping all over him!"
    
    v_un  "Wh-whoops! Sorry!"
    
    "Something had, indeed, been dripping on me. I thought it to be water, but after a moment something wet and cool wipes a trail along my forehead."
    
    ku_un "You've just smeared it around..."
    
    v_un "Huh?"
    
    ku_un "Umm, it's nothing. We should bring him inside. Can you take that shoulder?"
    
    v_un  "Sh- shoulder? But what if he wakes up?"
    
    menu:
        "Interrupt.":
            "It's probably a good idea to let them know I'm alright before they dislocate my shoulders."
            
            "I let them know I'm alive by grunting something indecipherable."
            
            v_un "!"
            
            ku_un "Oh, thank goodness! Can you move?"
            
            "I nod, and finally manage to wrench open my weary eyes."
            
        "Stay quiet.":
            "I decide to play along and see what happens. This should be interesting."
           
            ku_un "What do you mean 'if he wakes up?'"
            
            v_un "He might think we're kidnapping him or something..."
            
            ku_un "We'll deal with that if it happens. But right now, we need to get him inside. This might be serious."
            
            v_un "Do... do you think we'll need to call an ambulance?"
            
            ku_un "I'm not sure. Let's get him inside first."
            
            v_un "O... okay!"
            
            "I feel the palms of two very different hands wrap against my forearms. One is warm and soft, while the other is cool and strangely damp."
            
            "At this moment, I decide to open my eyes just enough to see my impromptu paramedics."
    

    
    scene bg yard
    
    show kumiru surprised at kumiru_right
    
    show viscella shocked at viscella_left

    with Dissolve(0.5)
    
    stop music
    
    play sound "assets/sound/sfx/vinylscratch.wav"
    
    $ renpy.pause(2.0)
    
    "That one's made of jell-o."
    
    "The other one looks no-"
    
    hide viscella
    
    show kumiru at kumiru_legs
    
    $ renpy.pause(2.0)
    
    menu:
        "Panic.":
            
            show kumiru neutral at kumiru_right
    
            show viscella neutral at viscella_left
                            
            "I do what any upstanding citizen would do in this situation."
            
            pc "AAAAAAAHHH!"
            
        "PANIC.":
            show kumiru neutral at kumiru_right
    
            show viscella neutral at viscella_left
                
            "I do what any upstanding citizen would do in this situation."
            
            pc "GYAAAAAH!"
            
    show kumiru scream
    
    show viscella scream
    
    ku_un "AAAAAWAWAAAH!"
            
    v_un "EEEEEEYAAAAA!!!"
    
    play sound "assets/sound/sfx/body_hit.wav"
    
    show black with vpunch
    
    hide viscella
    
    hide kumiru
    
    "Something hard hits me on the head, and I once again return to the void."
    
    jump ch1_scene02
    
label ch1_scene02:
    "GAME OVER."
    
    "..."
    
    "Wouldn't that suck?"
    
    "It seems I'm coming to."
    
    play music "assets/sound/bgm/tam-n13.mp3" loop fadein 3.0
    
    scene bg living with Dissolve(4.0)
    
    $ setTime(3)
    
    #$ clock_access = True
    
    "I'm lying on a couch, with something cold pressing uncomfortably into the back of my neck. I tilt my head forward and pull out the foreign object - it's a bag of ice, wrapped in a towel."

    "There is now an numb spot on my neck in addition to the throbbing bump on my scalp. I have felt better."
    
    ku_un "Ah! You're awake!"
    
    show kumiru sad at kumiru_center with dissolve
    
    ku_un "I was about to call an ambulance!"
    
    ku_un "Are you okay? Can you breathe?"
    
    menu:
        "'I think so...'":
            
            $ ku_like += 1
            
            show kumiru neutral
            
            ku_un "What a relief!"
            
            ku_un "I'm so sorry... you startled Viscella, and she... um..."
            
            ku_un "Well, uh..."
            
            ku_un "She doesn't take martial arts or anything, so I'm not sure why her first reflex was to judo chop you..."
            
        "'Sp-spider!'":
            
            show kumiru shocked
            
            ku_un "Wh- what?! Spider?! Where?!"
            
            ku_un "..."
            
            show kumiru embarrassed
            
            ku_un "Oh."
            
    "There's no doubt about it. From the waist down, she's got about six more legs than what I'd expect on a woman. Her face looks normal at first, until I realize the small, almond-shaped black spots are actually small eyes."
            
    "She seems harmless enough."
    
    "Well, as harmless as an eight-legged spider-woman can get, anyways."
    
    show kumiru neutral
    
    ku_un "You know, I might still have to call that ambulance. I'm pretty sure you gave Viscella a heart attack, and she doesn't even have a heart."
    
    menu:
        "'Uh... why are you part spider?'":
            
            show kumiru confused
            
            ku_un "Huh? I'm a drider. You have seen a drider before... right?"
            
            menu:
                "'Not exactly...'":
                    
                    $ flag_DriderSeen = False
                    
                    ku_un "Really? No wonder you yelped..."
                    
                    show kumiru confused
                    
                    ku_un "Still, that's quite... bizarre. You've really never seen a drider before?"
                    
                    ku_un "Hmm... maybe Viscella hit you harder than I thought..."
                    
                "'Oh, yeah, I'm basically a drider expert.' (Lie)":
                    
                    $ flag_DriderSeen = True
                    
                    ku_un "An expert, huh?"
                    
                    ku_un "Well, at least you know what I am. I was worried you might've suffered some minor brain damage..."
        
        "Pretend nothing is wrong.":
            
            $ flag_DriderSeen = True
            
            ku_un "Well, as long as you can talk, I think you're okay."
            
    show kumiru neutral
    
    ku "Oh, um... I'm Kumiru, by the way."
    
    "I introduce myself."
    
    show kumiru happy
    
    ku "Nice to meet you, [pc]."
    
    show kumiru neutral    
        
    ku "Again, I'm... really sorry about all this..."
    
    menu:
        "'Don't be. I'm fine.'":
        
            show kumiru happy
            
            ku "Are you sure?"
            
            pc "Yeah, I barely felt a thing."
            
            "I gently massaging the painful, swollen bump on my head."
            
            pc "Yep. Not a thing."
            
            ku "If you say so."
    
        "'And I'm sorry for bursting your eardrums.'":
            
            $ ku_love += 1
            
            show kumiru happy
    
            ku "I guess now we're even, huh?"
    
    ku "Well, I'm glad you're not too upset. Still, it's a rather rude welcoming to a bondhouse, of all places..."
    
    menu:
        "'Bondhouse?'":
            
            $ flag_BondhouseExplained = True
            
            show kumiru confused
            
            if flag_DriderSeen:
                
                ku "You've never heard of a bondhouse before?"
                
            else:
                
                ku "You've never heard of a bondhouse, either?"
                
                ku "First driders, now bondhouses... you're not pulling my legs, are you?"
                
            "I shake my head."
                
            ku "Well... a bondhouse is a place where people, uh... bond."
            
            show kumiru embarrassed
            
            ku "Er, that sounded more informative in my head."
            
            show kumiru neutral
            
            ku "Basically, it's like summer camp. But, um, over the winter. And there aren't really any activities or anything, you just... live with people."
            
            ku "Does that make sense?"
            
            ku "It's more fun than it sounds. Well, I hope..."
            
            "Kumiru sighs, glancing away momentarily. Before long, her eyes are drawn to the entrance to the living room. A small blue figure is peeking around the archway."
            
            show viscella sad at viscella_farleft with dissolve:
                xalign -0.1
            
            show kumiru confused
            
            ku "Viscella? How long have you been there?"
            
            show viscella scared
            
            v "!"
            
            show viscella sad at viscella_farleft with move:
                xalign -0.7
                
            show kumiru unamused
                
            "The girl darts back around the corner."
            
            "Kumiru gives a quiet sigh."
            
            show kumiru neutral

            ku "Don't be like that, Viscella. He's not angry. Come on out. Please?"
            
        "'It's fine. Is your friend alright?'":
            
            $ bondHouseExplainedFlag = False
    
            show kumiru neutral
    
            ku "Oh, Viscella? I think she's in her room. She ran off after hitting you - probably felt too guilty to look you in the eye. Poor thing."
            
            ku "I told her it wasn't her fault, of course, but she wouldn't listen. For all she knows, she put you into a coma."
            
            ku "She didn't, of course - slimes can't really hit that hard. I'm not even sure why you lost consciousness. I mean, unless you were already in a weak state, which was possible, since we found you passed out..."
            
            ku "Anyways, please don't be too angry with her. She's, um... fragile."
            
            show viscella flustered at viscella_farleft with moveinleft
            
            v "I'm not fragile!"
            
            show viscella embarrassed
            
            "In the entryway, a figure slaps a hand over its mouth and flings itself behind the wall it was peeking from."
            
            show kumiru happy
            
            ku "We know you're there now, Viscella. You can come out."
    
    show kumiru happy at kumiru_right with move
        
    show viscella sad at viscella_left with MoveTransition(2.0)
    
    "The small girl nervously shuffles back into view. She can barely bring herself to look at me."
    
    hide kumiru with dissolve
    
    show viscella at viscella_center_flipped with dissolve
    
    "... Yep, there's no mistake about it. She's made out of goo. The only thing solid about her is some sort of opaque orb floating in the middle of her chest - the rest of her is composed of a viscous liquid, like honey."
    
    show viscella at viscella_left with dissolve
    
    show kumiru happy at kumiru_right behind viscella with dissolve
    
    v "Nnn..."
    
    v "I'm sorry..."
    
    menu:
        "'You guys apologize too much. I'm fine.'":
            
            $ v_like += 1
            
            show viscella neutral
            
            v "But... I knocked you out..."
            
            show kumiru neutral
            
            ku "He was barely conscious when we found him. He probably just passed out the moment you smacked him."
            
            v "But-"
            
            ku "Come on, Viscella, you're too weak to actually hurt anyone."
            
            show viscella happy
            
            v "Really?"
            
            v "..."
            
            show viscella unamused
            
            v "I don't know if that makes me feel better or not..."
            
        "'Whoa. What are you made of?'":
            
            $ v_love += 1
            
            show viscella shocked
            
            v "M-me?"
            
            if flag_DriderSeen == False:
                
                show kumiru confused
                
                ku "You haven't seen many chimera before, have you?"
            
            show viscella happy
            
            v "Um... I'm a pryto- pryta- erm, sel- prytose- prytoself."
            
            show kumiru unamused
            
            ku "Prytosylph."
            
            v "Yeah. I'm a prytosylph, so I'm made of pryto- pryta- um, prytose-"
            
            ku "Prytoplasm."
            
            v "Prytoplasm."
            
            v "..."
            
            ku "In English, she's a slime, and she's made of slime."
            
            show viscella flustered 
            
            v "That just makes it sound gross!"
            
            ku "I'm just saying it like it is."
            
            show viscella embarrassed
            
            v "The way it is sounds gross!"
            
            ku "Yep."
            
    
    show kumiru neutral
    
    ku "Anyways, let's not skip introductions. Viscella, this is [pc]. [pc], Viscella."
    
    show viscella neutral
    
    v "N-nice to meet you."
    
    ku "Right, now that we're all introduced... what happened? What were you doing lying on the driveway? In fact, where did you come from?"
    
    "I think back, but..."
    
    "Nothing's coming to me."
    
    "Not just why I was on the driveway - nothing's coming to me at all. I vaguely recall talking with someone, but the memory is fading fast - like a dream early in the morning. I'm not even certain it was real."
    
    pc "I can't remember."
    
    ku "Well, what's the last thing you remember doing?"
    
    pc "No, I can't remember anything."
    
    show kumiru shocked
    
    show viscella shocked
    
    ku "You can't?"
    
    ku "But you told us your name!"
    
    pc "That's about all I remember."
  
    show kumiru confused
     
    "The rest of my memories, supposing I even had them in the first place, seem to be just beyond reach." 
    
    "I try to think of the day before, but the effort is fruitless. I have a vague feeling my memories are there, but I have no means to access them."
            
    ku "That's..."
        
    ku "Well..."

    ku "..."

    show viscella excited

    v "Awesome!"

    show kumiru shocked

    ku "Eh?"

    v "That's so cool! I bet you're from another dimension or something, right? Right?!"

    show kumiru confused

    ku "C-calm down, Viscella! That's completely absurd! If anything, he was probably attacked by a nightmare!"

    show viscella happy

    v "Hehe, what? Don't be silly, Kumi. Nightmares can't attack people. Even I know that!"

    show viscella excited

    v "He's definitely from an alternate universe! Or maybe he's my son from the future, who travelled back in time to save me from a tragic fate!"

    ku "That doesn't explain why he would have amnesia! And we can't even have sons!"

    show kumiru neutral

    ku "Besides, I wasn't talking about dreams. I was talking about the species."
            
    show viscella shocked
            
    v "Night... mares? Ooooh, those nightmares. Riiight."
    
    show viscella neutral
    
    show kumiru neutral
    
    pc "Nightmares?"
    
    ku "You know, the chimera."
    
    ku "..."
    
    show kumiru confused
        
    ku "Um, right, you don't remember anything..."
    
    if flag_DriderSeen:
        ku "Hold on, didn't you say you'd seen driders before?"
        
        v "Maybe he didn't want to embarrass himself?"
        
        v "I mean, wouldn't it be kinda like saying you'd never seen a human before?"
        
        ku "Well... I suppose..."
    
    show kumiru neutral 
        
    ku "Well, anyways, nightmares share many similarities with ghosts. However, unlike ghosts, they can tamper with memories."
    
    show viscella happy
    
    v "Not mine! I'm nightmare-proof!"
    
    show kumiru unamused
    
    ku "That's because you don't have a brain."
    
    show viscella neutral
    
    v "..."
    
    ku "..."
    
    show kumiru neutral
    
    ku "Anyways, I can only imagine you were kidnapped by a nightmare and had your memories erased."
    
    ku "Which means you might be both an amnesiac and a kidnappee."
    
    show kumiru sad
    
    ku "This is... a lot to take in."
    
    show viscella scared
    
    v "That sounds a lot scarier than what I was thinking... what do you think happened to you, [pc]?"
    
    menu:
        "What do you think happened to you?"
            
        "'This 'nightmare' thing sounds most plausible.'":
            
            $ ku_like += 2
            
            show kumiru happy
            
            ku "That seems most likely."
            
            v "And most boring..."
            
        "'Maybe I really am from a different dimension...'":
            
            $ v_like += 2
     
            show viscella excited
            
            v "Yesss! So cool! I bet you've even got awesome attack powers and buried emotional scars that never heal!"
            
            show kumiru embarrassed
            
            ku "Try not to encourage her too much. It's hard enough keeping her in the real world as-is..."
            
            show viscella happy
            
        "'I don't know...'":
            
            $ v_like += 1
            
            $ ku_like += 1
            
    show kumiru neutral
            
    ku "Well, assuming you were attacked by a nightmare, it's still possible for us to get your memories back."
    
    show viscella shocked
    
    v "It is?"
    
    ku "Yes. Nightmares don't destroy memories permanently. They store them in phylacteries."
        
    show viscella confused
        
    v "Phyl... acteries?"
                                    
    show kumiru confused
    
    ku "Yes, phylacteries. They're like amulets. Phylacteries."
    
    v "...?"
            
    show kumiru unamused
   
    ku "..."
    
    ku "Anyways."
    
    show kumiru neutral
    
    ku "If we can find the culprit, we can get your memories back."
    
    ku "All we need to do is bring you to the police."
    
    show viscella scream
    
    v "P-p-police?! We can't do that!"
    
    show kumiru confused
    
    ku "Er... why not?"
    
    show viscella flustered
    
    v "What- what if they inspect my room! I-I don't wanna go to jail!"
    
    show kumiru unamused
    
    ku "Why would they inspect your room?"
    
    show viscella scared
    
    v "Because I'm a suspect! They'll probably think I kidnapped [pc] or something!"

    show kumiru confused

    ku "That's ridiculous. You couldn't kidnap someone if you wanted to."
    
    v "The police don't know that!"
    
    show viscella flustered
    
    v "They'll probably waterboard me!"
    
    show kumiru neutral
    
    ku "I... don't think so."
    
    show viscella scared
    
    v "Please, don't call the police! I'm too young to be in an episode of {i}COPS{/i}! Besides, it's not like the police can help!"
    
    show kumiru confused
    
    ku "What? Why not?"
    
    v "Police only solve the plot hook in the mystery genre! Any other genre and they usually just make the situation worse!"
    
    show viscella flustered
    
    v "And then a robot comes and shoots up the station while the protagonist is trapped, thus establishing the overwhelming power of the antagonists!"
    
    show kumiru unamused
    
    ku "..."
    
    show viscella scared
    
    ku "You're something else, you know that?"
    
    show kumiru neutral
    
    ku "What do you think, [pc]?"
    
    menu:
        
        "'There's no rush.'":
        
            show viscella shocked
        
            v "Th-thank you!"
            
            show viscella excited
            
            v "I promise I'll use the life you gave me to the fullest!"
                             
            show viscella happy
            
            show kumiru confused
                             
            ku "Are you sure about this? I mean, you {i}did{/i} lose your memories..."

            pc "Well... I've got a feeling they're either gonna be easy to recover or exceptionally difficult. Either way, taking a day or two off couldn't hurt."
            
            show kumiru neutral
            
            ku "Really? I see..."
            
            
        "'I suppose it can wait until tomorrow...'":
    
            show kumiru confused
    
            ku "Are you sure? Don't let Viscella pressure you..."
            
            v "Y-yeah, I'm sure jail's not {i}that{/i} scary..."
            
            show kumiru unamused
            
            ku "Would you stop?"
            
            show viscella sad 
            
            v "Sorry."
            
            pc "It's fine. I'm still a little disoriented, to be honest - it's probably a good idea to rest for today."
            
            show kumiru neutral
            
            ku "Well... if you say so."
    
    
    show viscella neutral
    
    ku "Maybe all you need's a good night's sleep?"

    pc "I can hope..."
    
    ku "Don't worry. Either way, we'll get them back eventually - but for now, you're probably right. Maybe it would be best to take it easy."
    
    show kumiru happy
    
    ku "I can show you around if you like. We can also give you a room to sleep in - there are still four that haven't been claimed yet. I'm sure the tenants won't mind if you use one of the rooms meant for them."
    
    show viscella scared
    
    v "Is- is that a good idea?"
    
    show kumiru confused
    
    ku "Why would it be a problem?"
        
    v "Well, if you give, um..."
    
    ku "[pc]?"
    
    v "Y-yeah. If you give [pc] someone else's room, they might beat him up..."

    show kumiru unamused

    ku "Don't be ridiculous, Viscella. Not everyone is as bad as Veneri, you know. Plus, we're only expecting three more. That means the fourth room is a spare."
    
    show kumiru neutral
    
    menu:
        
        "'You're expecting more?'":
            
            ku "Of course. Viscella and I hardly need to spend any more time bonding than we already have."
            
            ku "We're expacting a lamia, a harpy, and a kitsune."
            
            ku "That's all, unfortunately."
            
            pc "Unfortunately?"
            
            show viscella embarrassed
            
            ku "Well, um..."
            
            ku "The only reason people sign up for bondhouses is because of the off-chance they'll be paired with, ah..."
            
            show kumiru embarrassed
            
            ku "...Nevermind."
            
        "'Veneri?'":
            
            ku "She was a... hard person to get along with."
            
            show viscella angry
            
            v "She was the worst."
            
            show kumiru sad
            
            ku "We're... getting sidetracked. We were talking about what to do with [pc], remember?"
    
            show viscella neutral
    
            v "Yeah..."
            
            show kumiru happy
            
            ku "Thank you, Viscella."
    
    ku "Ahem. As I was saying..."
    
    show kumiru happy
    
    ku "We have a spare room, so feel free to spend the night there and collect your thoughts."
    
    show viscella neutral
    
    v "And memories..."
    
    ku "And those."
    
    ku "So, how about that tour?"
    
    jump ch1_scene03


label ch1_scene03:
    
    show kumiru happy
    
    ku "This is the living room. There are... couches. Nothing special. There's a bathroom over by the front door, and down the hallway is the staircase." 
    
    ku "Over there's the garage. We're free to use the van as we like, but I don't think you'll be able to drive if you don't have ID. Next is the kitchen - can you walk?"
    
    "I nod, pushing myself off the couch. I leave an indent in the cushions - I was probably out for at least half an hour."
    
    "Kumiru points out other landmarks of significant interest, such as the lamps and placeholder photographs decorating the walls, until moving to the kitchen."
    
    "Her legs are a spectacle to watch - all eight of them working in tandem with such grace that she seems to float silently from place to place. Her movements seem unusually disconnected with her easygoing personality."
    
    scene bg kitchen with wipeleft
    
    show kumiru happy at kumiru_right
    
    show viscella neutral at viscella_left
    
    with dissolve
    
    ku "And this is the kitchen! Um, obviously. Feel free to help yourself, we don't have to pay for food unless we go way over-budget."
    
    show viscella shocked
    
    v "That's a huge fridge."
    
    show kumiru confused
    
    ku "You've said that every time you've walked in here."
    
    v "Because it's huge! It's huge, isn't it?"
    
    menu:
        "'It's huge.'":
            
            show viscella vhappy
            
            $ v_like += 1
            
            v "See?"
            
            ku "Am I the only one not awestruck by the size of the fridge?"
            
            show viscella happy
            
            v "Doesn't it make you realize how small you are? In the grand scheme of things, I mean."
            
            ku "It's a fridge."
            
            v "A {i}huge{/i} fridge."
            
        "'It's normal.'":
            
            $ ku_like += 1
            
            v "It is?"
            
            ku "Everything's huge compared to you, Viscella."
            
            show viscella angry
            
            v "Not true!"
            
            ku "You're what, five feet tall?"
            
            show viscella embarrassed
            
            v "...Eight."
            
            ku "Five foot eight?"
            
            v "Four foot eight..."
        
    show kumiru neutral
        
    ku "...Right. Where were we, again? Oh, right, the tour. The dining room's right over there, but you can eat in here if you want."
    
    ku "Well, not like you need me to tell you where to eat."
    
    show kumiru embarrassed
    
    ku "I mean, I'm not your mother..."
    
    show viscella neutral
    
    v "Come on, Kumi, tours are supposed to be fun."
    
    show viscella happy
    
    v "Let's show him the cool stuff!"
    
    ku "Well... I suppose... okay, then, um, follow me, please."
    
    scene bg hallway with dissolve
    
    show kumiru neutral at kumiru_right
    
    show viscella happy at viscella_left 
        
    with dissolve
        
    ku "This is the second floor."
    
    show kumiru embarrassed
    
    ku "Obviously."
    
    show viscella excited
    
    v "This is where the fun starts! Wait 'till you see the-"
    
    show kumiru shocked
    
    ku "Shh! Don't spoil it!"
    
    show viscella happy
    
    v "What, the home theatre?"
    
    show kumiru unamused
    
    v "...No?"
    
    v "The bar?"
    
    ku "Stop talking."
    
    show kumiru neutral
    
    ku "Anyways, as my good friend was just saying, there's a home theatre and a rec room up here."
    
    scene bg theatre with wipeleft
    
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left 
    
    with dissolve
    
    ku "Here's the home theatre. Pretty neat, huh?"
    
    v "'Pretty neat'? You wouldn't stop talking about it earlier."
    
    ku "I've calmed down. And you were even worse than I was."
    
    show viscella happy
    
    v "Well, of course!" 
    
    show viscella excited
    
    v "Gigantic screen! Surround sound! Noise-proof walls! Lockable door!"
    
    v "All you need for a non-stop night of totally immersive, high-definition he-"
    
    v "..."
    
    show viscella shocked
    
    v "He..."
    
    show viscella scared
    
    v "Hehe, ahaha, *cough cough*"
    
    v "I, um, think I got something in my throat."
    
    show kumiru confused
    
    ku "You don't have a throat."
    
    show viscella embarrassed
    
    v "W-what was I saying?"
    
    show kumiru unamused
    
    ku "Something about 'next room'."
    
    scene bg study with wipeleft
    
    show kumiru neutral at kumiru_right
    
    show viscella embarrassed at viscella_left 
    
    with dissolve
    
    ku "This is the study. It has a small library's worth of books, and a computer with working internet. I wouldn't bother - it's a bit of a dinosaur."
    
    show viscella confused
    
    v "Dinosaur?"
    
    ku "You know, an ancient piece of technology?"
    
    v "Oh, I get it. Is that why you always called Mrs. Leoptis a dinosaur?"
    
    ku "Er... not quite."
    
    scene bg gym with wipeleft
    
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left 
        
    with dissolve
    
    ku "This is the exercise room."
    
    ku "Most of the equipment is designed for bipeds, unfortunately, so I can't use them myself."
    
    v "What about the weights?"
    
    ku "Yep, all designed for bipeds. Can't use a thing."
    
    show viscella angry
    
    v "But what about the-"
    
    show kumiru unamused
    
    ku "Ahem. Next room."
    
    scene bg hallway with wipeleft
    
    show kumiru neutral at kumiru_right with dissolve
    
    show viscella neutral at viscella_left with dissolve
    
    ku "Well, that's about everything on this floor."
    
    show viscella angry
    
    v "Kumiru!"
    
    show kumiru confused
    
    ku "What?"
    
    v "You didn't tell him about the rec room!"
    
    show kumiru neutral
    
    show viscella happy
    
    ku "Oh, right. The recreation room has a bar, a pool table, darts, that sort of thing. And a T.V, of course, because we don't have enough of those."
    
    v "And?"
    
    ku "And what?"
    
    scene bg rec with wipeleft
    
    show kumiru neutral at kumiru_right with dissolve
    
    show viscella excited at viscella_left with dissolve
      
    v "A karaoke machine!"
    
    show kumiru happy

    ku "And a karaoke machine."
    
    v "We should play right now! I've always wanted to do karaoke!"
    
    show kumiru neutral
    
    ku "I'm not sure now's the best time."
    
    show viscella happy
    
    v "Why not?"
    
    ku "Well, we're showing [pc] around. That, and you need to prepare for karaoke."
    
    v "Prepare? How?"
    
    ku "I think spending about an hour at the bar would do it."
    
    scene bg hallway with wipeleft
    
    show kumiru neutral at kumiru_right with dissolve
    
    show viscella neutral at viscella_left with dissolve
        
    ku "Well that's it for the 'fun' rooms."
    
    v "Bedrooms can be fun."
    
    show kumiru embarrassed
    
    ku "Well, uh..."
    
    ku "I mean, you're not {i}wrong{/i}."
    
    ku "..."
    
    ku "M-moving on."
    
    show kumiru neutral
    
    ku "All the rooms here on the third floor are bedrooms. Well, except the bathroom, of course."
    
    ku "Go ahead and choose one. You'll probably only be staying for a few days, so it's no big deal."
    
    "There are six rooms total: three on the right, and three on the left. I could choose the room beside my new friends, or I could opt for the quiet-looking room in the far corner."
    
    menu:
        "Which room will I take?"
        
        "Close room beside Kumiru.":
            
            $ flag_RoomBesideKumiru = True
            
            show viscella happy
            
            v "Yay!"
            
            show viscella neutral
            
            v "Actually, we shouldn't celebrate yet."
            
            v "Now you have to share a wall with Kumi, too."
            
            v "You might want earplugs."
            
            show kumiru embarrassed
            
            ku "Gu- Viscella!"
            
            ku "At least I'm not singing butchered J-Pop lyrics at two in the morning!"
            
            show viscella embarrassed
            
            v "..!"
            
        "Far room across from Viscella.":
            
            $ flag_RoomBesideKumiru = False
            
            show viscella happy
            
            v "Aren't corner rooms the best?"
            
            v "They're like the corner seats in Japanese classes were the totally ordinary protagonist sits."
            
            v "Except she's not {i}really{/i} a totally ordinary protagonist."
            
            show kumiru unamused
            
            show viscella excited
            
            v "Because she meets this cool boy who's a half-demon half-spirit hybrid and his companion who's actually a cyborg-"
            
            ku "That's enough, Viscella. At this rate he's going to choose the room furthest from you."
            
    show kumiru surprised
    
    show viscella shocked
    
    $ renpy.music.set_volume(0.0)
    
    play sound "assets/sound/sfx/doorbell.wav"
    
    $ renpy.pause(3.0, hard = True)
    
    $ renpy.music.set_volume(1.0)
    
    v "Was that the doorbell?"
    
    show kumiru neutral
    
    ku "Obviously. It's probably one of the tenants."
    
    show viscella scared
    
    v "Already?!"
    
    ku "Yes, already."
 
    v "..."
    
    v "Can I hide in my room?"
    
    show kumiru unamused
    
    ku "No."
    
    show kumiru neutral
    
    ku "Anyways, [pc], feel free to check out your room. I'll go make sure Viscella properly introduces herself."
    
    show viscella flustered
    
    v "I'm not that pathetic!"
    
    show kumiru unamused
    
    ku "Yeah, yeah, tell it to our new roommate."
    
    hide kumiru
    
    hide viscella 
    
    with dissolve
    
    "The drider coerces her friend down the staircase, leaving me alone with my thoughts. I decide to take a look at my new room."
    
    stop music fadeout 3.0
    jump ch1_scene04
    
    
label ch1_scene04:
    
    scene bg pBedroom with Dissolve(3.0)
    
    play sound "assets/sound/sfx/door_close.wav"
    
    play music "assets/sound/bgm/tam-n17.mp3" fadein 3.0
    
    
    "It's pretty much barren."
    
    "There's a digital alarm clock on the nighstand that reads twelve o'clock. There's also a dresser and a desk, complete with a chair."
     
    "I check the furniture, and then the closet. All empty."
    
    "Looks like I've got nothing but the clothes on my back."
    
    "I drop down onto the bed, trying to remember the day before. Just the attempt gives me a headache - the shroud around my memories might as well be a brick wall."
    
    "At least I have some sort of memory. Enough for me to know that women have two legs, two eyes, and are not made of jell-o."
    
    "But the girls I just met acted like it was all so normal..."
    
    "[pc]."
    
    "It's my name, and it's the only thing I've got."
    
    "Will it be permanent?"
    
    "According to the drider, memory loss caused by a nightmare is reversible - if what caused this even was a nightmare."
    
    "Maybe I really lost all my memories with that blow to the head."
    
    "For just a moment, I can almost grasp a memory - something that happened just before I woke with the breeze on my face, but..."
    
    "..."
    
    "It's gone. Behind the haze, like all the rest."
    
    "Looks like all I can do is-"
    
    stop music fadeout 0.5
    
    play sound "assets/sound/sfx/footstep_rush_close.wav"
    
    $renpy.pause(4.0)
    
    ka_un "Room serviiice!"
    
    play sound "assets/sound/sfx/door_open.wav"

    show kamao starry_s at kamao_center with dissolve
    
    $renpy.pause (1.0)
    
    play sound "assets/sound/sfx/door_close.wav"

    play music "assets/sound/bgm/slapstick.mp3"

    $renpy.pause (1.0)

    menu:
        "Fight":
            
            "My brain switches to autopilot. I fling myself off the bed, lock on to the intruder, and charge."
            
            "Unfortunately, it seems they had the same idea."
            
        "Run":
        
            "My brain switches to autopilot. I fling myself off the bed, lock on to the window, and prepare to jump through."
            
            "There is a flurry of movement behind me, and I find myself rushing to meet the floor."                                                                                                                                
            
    play sound "assets/sound/sfx/body_hit.wav"

    show black with vpunch
    
    scene bg pBedroom with Dissolve(4.0)
                                            
    "Someone is pinning me to the floor, though they don't feel too heavy."
    
    "I crane my neck around to try and get a good look at them."
    
    show kamao teasing at kamao_center with dissolve
    
    ka_un "Helloooo handsome!"
    
    menu:
        "'A catgirl?'":
            
            $ ka_like += 1
            
            ka_un "Nope. Fluffier."
            
            ka_un "Touch my tail and see for yourself."
            
            show kamao winkblush
            
            ka_un "Actually, touch anywhere you want."
            
            show kamao neutral
            
        "'A foxgirl!'":
            
            $ka_like += 1
            
            show kamao winkblush
            
            ka_un "Handsome {i}and{/i} 20/20 vision! I'm impressed!"
            
            show kamao neutral
            
            ka_un "The correct term is kitsune, but..."
                   
            show kamao teasing       
            
            ka_un "You can call me whatever you want, big boy."
            
        "'A nuisance.'":
            
            show kamao shocked
            
            ka_un "Zing!"
            
            show kamao neutral
            
            ka_un "Don't worry, I'm adorable once you get to know me."
                   
            show kamao winkblush
                   
            ka_un "And you {i}will{/i} get to know me."
           
    stop music fadeout 2.0
    
    show kamao shocked       
    
    play sound "assets/sound/sfx/footstep_rush_close.wav"
    
    $renpy.pause(2.0)
    
    play music "assets/sound/bgm/tam-n13.mp3"
    
    
    show kamao bored
    
    ka_un "Here comes the cavalry."
    
    play sound "assets/sound/sfx/door_open.wav"
    
    show kamao bored at kamao_right with move
    
    show kumiru angry at kumiru_left behind kamao with dissolve
    
    show viscella excited:
        xpos -0.5
        xanchor 0.5
        ypos 0.6
        yanchor 260
        zoom 0.5
        xzoom -1.0
    
    
    
    ku "Ma'am! What on earth are you-"
    
    show viscella excited with MoveTransition(0.2):
        xpos 0.12
        xanchor 0.5
        ypos 0.6
        yanchor 260
        zoom 0.5
    
        
    play sound "assets/sound/sfx/body_hit.wav"
    
    show viscella flustered
    
    show kumiru shocked with MoveTransition(0.1):
        xpos 0.35
        xanchor 0.5
        ypos 0.6
        yanchor 327
        zoom 1.0
        xzoom -1.0
        zoom 0.5
    
    show kamao shocked
    
    v "Oof!"
    
    show viscella neutral
    
    show kumiru unamused at kumiru_left with MoveTransition(0.2)
        
    ku "..."
        
    ku "*Ahem.*"
    
    show kumiru confused
    
    ku "Ma'am, what are you doing?"
    
    show kamao unhappy
    
    ka_un "Nice try, four eyes."
    
    show kamao confused
    
    ka_un "I mean."
    
    ka_un "One, two, three..."
    
    $ renpy.pause(1.0)
    
    show kumiru unamused
    
    ku "..."
    
    ka_un "Six, seven, eight..."
    
    $ renpy.pause(1.0)
    
    show viscella confused
    
    v "..."
    
    show kamao unhappy
    
    ka_un "Nice try, ten eyes. I found him first."
    
    show kumiru confused
    
    ku "Found him? What?"
    
    ka_un "Finders keepers!"
    
    ku "What are you talking about? We're the ones that found him. And why on earth are you sitting on him?"
    
    show kamao neutral
    
    ka_un "Am I not allowed to sit on my future boyfriend?"
    
    show kumiru unamused
    
    show viscella shocked
    
    v "W-What?!"
    
    ka_un "You heard me, jailbait. We just finished consummating our love for one another." 
    
    menu:
        "'We definitely did not do that.'":
            
            $ v_like += 1
            
            show viscella happy
            
            v "Oh, that's a relief..."
            
            ku "Viscella, it took us less than a minute to get here. The only thing she consummated is a restraining order."
            
            ka_un "Our love transcends all boundaries, including those defined in a legal contract."
            
            show viscella unamused
            
            "The girl rolls off my back. I stand up, brushing off my pants."
            
            
        "'Someone get this furball off of me.'":
            
            $ ku_like += 1
            
            show viscella neutral
            
            ku "Say no more."
            
            show kumiru unamused at kumiru_center_flipped with MoveTransition(0.5)
                
            show kamao angry
            
            ka_un "Back off, sister! I've already marked him with my-"
            
            "Kumiru easily lifts the intruder off of me."
            
            show kamao shocked with vpunch
            
            show kumiru unamused at kumiru_left with MoveTransition(0.5)
                
            ka_un "Defeated... by a nerd..."
            
            ka_un "How far the great Kamao has fallen..."
            
        "'It's true. I'm sorry...'":
            
            $ ka_love += 1
            
            $ ka_like += 1
            
            show kamao teasing
            
            ka_un "I blew his mind {i}and{/i} his-"
            
            show viscella flustered
            
            show kumiru embarrassed
            
            ku "Come on, guys, we're not that gullible."
            
            v "Awawawa..."
            
            show kumiru unamused
            
            ku "Well, I'm not, at least."
            
            "The girl rolls off my back and helps me to my feet."
            
            show viscella embarrassed
    
    show kamao neutral
    
    ka "I'm Kamao, by the way."
    
    show kumiru neutral
    
    ku "A pleasure. I sincerely hope you're not the kitsune we're expecting."
    
    show viscella scared
    
    v "Careful, Kumi! She's still a kitsune! They have scary luck powers!"
    
    ku "Please. She has a single tail. She's about as powerful as you."
    
    show kamao vangry
    
    ka "Two tails."
    
    show kumiru confused
    
    ku "What?"
    
    ka "Look. Look with your special eyes. One. Two. Two tails."
    
    ku "But one's short."
    
    show kamao angry
    
    ka "I'm an amputee, okay? I've still got two tails."
    
    show viscella confused
    
    v "How did you lose half of a tail?"
    
    show kamao bored
    
    ka "It's a long story that involves a rubber duck and a vacuum cleaner. That's all I'm gonna say."
    
    "A kitsune? Apart from the ears and tails, she doesn't seem all that unusual. Certainly less unusual than the other two."
    
    "Not that I remember enough to know what is and is not unusual in this place..."

    ka "Now, before you were so rudely interrupted by four- ten eyes here, you were telling me your name."
    
    show kumiru confused
    
    ku "I interrupted you, not him."
    
    ka "Yeah, I just told him my name. Isn't it a cultural custom to return a name with a name?"
    
    show viscella confused
    
    ku "Well... yes?"
    
    ka "So, naturally, he was about to tell me his before you started blabbing."
    
    ku "...What?"
    
    show kamao unhappy
    
    ka "Whaddya mean, 'what'? See, look! You're doing it now. Let the poor man speak."
    
    show kumiru unamused
    
    ku "..."
    
    menu:
        "'It's [pc].'":
            
            $ ka_like += 2
            
            show kamao horny
            
            ka "Oh, [pc]. [pc]! Yeah, right there! Just like that! Oh, [pc], I'm- I'm-"
            
            show kumiru embarrassed
            
            show viscella embarrassed
            
            ku "..."
            
            v "..."
            
            show kamao teasing
            
            ka "Just practicing."
            
            show kumiru unamused
            
            ku "Can you even feel shame?"
            
            show kamao winkblush
            
            ka "Yeah. It's a huge turn-on."
            
        "'Guess.'":
            
            $ ka_like += 2
            
            show kamao confused
            
            ka "Beautiful?"
            
            ka "Gorgeous?"
            
            ka "Sexy?"
            
            show kumiru unamused
            
            ka "Uh... Good-Lookin'?"
            
            ka "Help me out, here."
            
            ku "His name is [pc]."
            
            show viscella neutral
            
            show kamao neutral
            
            v "You're not supposed to give her the answer, Kumi."
            
            $ flag_ViscellaCalledJailbait = True
            
            ka "Yeah, what jailbait said."
            
            show viscella flustered
            
            v "Stop calling me that!"
            
            ka "Maybe."
            
            show viscella embarrassed
            
        "'No.'":
            
            ka "'No' it is."
            
            show kamao wink
            
            ka "Nice to meet you, No."
            
            show kumiru unamused
            
            ku "You're impossible."
            
            show kamao neutral
            
            ka "I try."
            
            show kumiru neutral
            
            ka "But really, what's your name?"
            
            ka "If you don't tell me, I'll call you 'Sexy' for the rest of your life."
            
            ka "I'm not joking."
            
            ka "Does this look like a face that would joke?"
            
            show viscella confused
            
            v "Ummm... yes?"
            
            show kumiru unamused
            
            show kamao neutral
            
            ku "His name is [pc]."
            
            show kamao teasing
            
            ka "[pc]? I like it."
            
            ku "You'd say that regardless of what his name was."
            
            show kamao winkblush
            
            ka "You know it!"
            
    show kamao neutral
            
    ka "Man, I didn't know there was gonna be a guy here."
    
    ka "I mean, I checked the website. It looked like it was gonna be a total taco fest."
    
    show kamao wink
    
    ka "We're gonna have a lot of fun, handsome!"
    
    ku "Actually, you're not."
    
    show kamao bored
    
    ka "Oh, don't be like that. You're just jealous he's head over heels for me."
    
    show kumiru angry
    
    ku "That's a tragedy, then, since he's not staying."
    
    show kamao shocked
    
    ka "What?!"
    
    show kumiru confident
    
    ku "He's lost his memories. He's only staying here until he gets them back. Latest."
    
    show kamao bored
    
    ka "Nice try, ten-eyes, but you're not in nerdtropolis anymore. I know that trick like the back of my hand."
    
    show kumiru confused
    
    ku "In whose trickbook is 'pretend he has amnesia' written down?" 
    
    show kamao neutral
    
    ka "{i}My{/i} trickbook."
    
    ku "...Right. Well, regardless, the fact of the matter is that [pc] is not signed up as a tenant. He's not allowed to stay even if he wanted to."
    
    show kamao unhappy
    
    ka "He will be once I'm through with management!"
    
    show kumiru unamused
    
    ku "Of course. I assume you have the two and a half thousand dollars on hand to pay for him?"
    
    ka "..."
    
    ka "Don't worry, [pc]. Long distance relationships can work. As long as you send nudes."
    
    show kumiru neutral
    
    show viscella scared
    
    v "W-wait. Kumiru?"
    
    ku "Hm?"
    
    v "If [pc]'s not allowed to stay here, is there a chance we could get in trouble?"
    
    ku "He's just a guest. The rules state that we can host him, as long as he doesn't stay longer than three days."
    
    show viscella neutral
    
    ku "So as long as we get his memories back by then, there's no problem."
    
    show kamao confused
    
    ka "Wait, you guys are serious about this amnesia thing?"
    
    ku "Unlike you, we treat lost individuals with missing memories seriously."
    
    show viscella excited
    
    v "Because they're so cool! Maybe he was an ex-detective who nearly caught up with his sister's killer, only for the killer to ambush him! When he woke up, he had no memory of his past life!" 
    
    show viscella happy
    
    show kumiru unamused
    
    show kamao neutral
    
    ka "Yeah. Real serious."
    
    ku "Regardless, that's the situation. Since your odds of actually winning [pc]'s favour are virtually nil, we'd all appreciate if you kept the sexual harrassment to a minimum."
    
    show kamao angry
    
    ka "'Virtually nil'? I don't know what that means. Anyone here speak nerd?"
    
    show kamao unhappy
    
    v "She meant 'basically zero'."
    
    show kumiru unamused
    
    show kamao neutral
    
    ka "Thanks, jailbait."
    
    show viscella flustered
    
    if flag_ViscellaCalledJailbait:
        
        show kumiru surprised
        
        v "I'm not jailbait! Stop calling me jailbait!"
        
        ka "Trust me, kiddo."
        
        ka "You're jailbait."
        
        ka "Unless you'd prefer 'pedobait'?"
        
        show kumiru embarrassed
        
        show viscella embarrassed
        
        v "...!"
        
        show viscella angry
        
        v "Hmph..."
        
        show kamao wink
        
        ka "That's what I thought."
        
    else:
        
        show viscella flustered
        
        v "S-Stop calling me that!"
        
        show viscella embarrassed
        
    show kamao neutral
        
    ka "Anyways, you said my odds were 'basically' zero. But not 'absolutely' zero."
    
    show kumiru confused
    
    ku "Statistically, it is also theoretically possible that I will start quantum tunnelling through the floor."
    
    ka "I don't know what that means, either, but I heard the word 'possible'."
    
    show kumiru unamused
    
    ku "Can we have this conversation somewhere else? Not in the middle of [pc]'s room?"
    
    show kamao confused
    
    ka "I thought you said he was a guest?"
    
    show kumiru confused
    
    ku "What, were you going to make him sleep on the floor?"
    
    show kamao unhappy
    
    ka "Of course not!"
    
    show kamao wink
    
    ka "He can sleep in my bed."
    
    show kumiru unamused
    
    ku "As long as you're not in it."    
    
    ka "No deal!"
    
    show kamao bored
    
    ku "Either way, you need to come with me. You dumped your luggage all over the foyer the moment Viscella mentioned a male pronoun."
    
    ka "Fine."
    
    show kamao teasing
    
    ka "But don't think I'm done with you, [pc]."
    
    ka "I'm gonna take the room right beside you."
    
    if flag_RoomBesideKumiru:
        
        show kumiru confident
        
        ku "Nice try. That's my room."
        
        show kamao teasing
        
        ka "Then I'll take the one across from you."
        
        show kumiru unamused
        
    show kamao winkblush
    
    ka "Stop by later. I'll give you a prize~"
    
    show viscella embarrassed
    
    show kumiru unamused
    
    ku "Don't count on it."
    
    hide viscella with dissolve
    
    hide kumiru with dissolve
    
    show kamao neutral at kamao_center with MoveTransition(1.0)
        
    ka "I'm serious, you know."
    
    show kamao wink
    
    ka "Think about it."
    
    show kamao neutral
    
    ka "..."
    
    show kamao unhappy
    
    ka "I'm begging you."
    
    hide kamao with dissolve
    
    $ kaUnFlip()
    
    jump ch1_scene05
    
label ch1_scene05:
    
    #$ clock_access = True
    
    "Well, that was something."
    
    "I check the alarm clock. It's a quarter after noon."
    
    "At least now maybe I'll be able to catch a-"
    
    $ renpy.music.set_volume(0.0)
    
    play sound "assets/sound/sfx/doorbell.wav"
    
    $ renpy.pause(3.0, hard = True)
    
    $ renpy.music.set_volume(1.0)
    
    "-break."
    
    "Well, seems like it's going to be a busy day."
    
    "I decide to go investigate. No use sitting in my room all day trying to brute force my way into my own memories."
    
    #$ clock_access = False
    
    scene bg living with Dissolve(2.0)
    
    "I descend the two flights of stairs to the ground floor."
    
    "Halfway there, I hear the sounds of a struggle. I quicken my pace, and before long arrive at what is unmistakably the source."
    
    show fenira angry at fenira_right with dissolve
    
    f_un "N-Nagi! Get your ass back here and get this fleabag off of me!"
    
    $ kaFlip()
    
    show kamao teasing at kamao_center_flipped with dissolve
    
    ka "Fleabag? I'll have you know I haven't had fleas since I was four!"
    
    f_un "Paws off the goods!"
    
    ka "I'll let you go if you give me a..."
    
    show kamao shocked
    
    stop music
    
    play sound "assets/sound/sfx/vinylscratch.wav"
    
    ka "..."
    
    ka "...kiss?"
    
    show kamao shocked at kamao_left with MoveTransition(0.1)
    
    ka "..."
    
    ka "Why do you have boobs?"
    
    play music "assets/sound/bgm/scene_comi2.ogg"
    
    
    show fenira confused
    
    f_un "Why do you think?"
    
    ka "Are you actually... a chick?"
    
    show fenira angry
    
    f_un "..."
    
    f_un "Are you serious?"
    
    show kamao neutral
    
    ka "Dead serious. You don't walk like a chick."
    
    f_un "And you don't walk like you've got your head stuck up your ass. Guess appearances can be deceiving, huh?"
    
    show kamao shocked

    ka "Well! I never!"
    
    show kamao neutral
    
    ka "[pc], are you gonna let her mad burn your girlfriend like that?"
    
    menu:
        "'You're not my girlfriend.'":

            ka "Don't mind him, he's in denial."
            
            show fenira confused
            
            f_un "I'd be in denial too if my girlfriend was dumber than a sack of bricks."
            
            ka "Foxes are smarter than birds."
            
            show fenira angry
            
            f_un "Sure, but I'm willing to bet my fist is harder than your face."
            
            show kamao horny
            
            ka "Not the only part of you that's hard right now, I bet..."
            
            f_un "Can you get lost before I remember how to properly break someone's arm?"
            
            show kamao shocked
            
            ka "Hoo boy, sounds like someone's got some aggression they need to work out."
            
            show kamao unhappy
            
            ka "Watch it, [pc] she'll probably break your nose the moment you glance at her boobs."
            
            show fenira vangry
            
            f_un "Get. Lost."
            
            ka "I'm going, I'm going. Yeesh."
            
        "'You had fleas when you were four?'":
            
            show kamao shocked
            
            ka "N-no!"
            
            show kamao embarrassed_open
            
            ka "Only a little bit!"
            
            show fenira smirk_open
            
            f_un "Fleas, huh? Who'd you get 'em from? Dog? Cat? Parents?"
            
            show kamao sad
            
            ka "My parents are dead."
            
            show fenira shocked
            
            f_un "O-oh. Uh... shit. Sorry."
            
            show kamao wink
            
            ka "Just kidding."
            
            show fenira angry
            
            f_un "That's it, fleabag."
            
            show fenira angry at fenira_center with move
            
            show kamao shocked
            
            ka "Oop! I think I hear my flea-free laundry calling! Laters!"
            
        "'You had it coming.'":
            
            $ ka_like += 1
            
            show kamao happy
            
            ka "Hah! You didn't actually deny I was your girlfriend!"
            
            show fenira confused
            
            f_un "Are you serious?"
            
            ka "I'm always serious."
            
            f_un "Why do I find that hard to believe?"
            
            show kamao neutral
            
            ka "Because you're basically a dude."
            
            show fenira vangry
            
            f_un "What the fuck are you talking about? Not only are you blind, that has nothing to do with anything!"
            
            ka "It has everything to do with everything."
            
            show fenira angry
            
            f_un "If you open your mouth one more goddamned time I'm gonna fill it with my-"
            
            show kamao winkblush
            
            ka "Whoa there, lover boy! I know you want a piece of this, but let's not rush too {i}deep{/i} into this relationship just yet, mkay?"
            
            f_un "That's it, fleabag, I'm gonna-"
            
            show kamao neutral
            
            ka "Take a chill pill and relax, right?"
            
            show fenira vangry at fenira_center with move
                
            show kamao shocked
            
            ka "On second thought, I have to finish unpacking. Toodles!"
            
    stop music fadeout 2.0
            
    hide kamao with dissolve
    
    show fenira angry with move:
        fenira_center
        
    "Kamao darts off, back up the stairs I just descended."
    
    play music "assets/sound/bgm/Town2.ogg" fadein 3.0
    
    
    f_un "Ugh."
    
    f_un "Please tell me I'm not going to be living with her."
    
    pc "Sorry."
    
    f_un "Great. Just great."
    
    show fenira sad
    
    f_un "*Sigh*."
    
    f_un "Probably should've chilled out a little, I guess..."
    
    menu:
        "'She has that effect on people.'":
            
            $ f_like += 1
            
            f_un "I figured. But I still shouldn't be picking fights with people I just met."
            
            f_un "Especially future roommates."
            
        "'Maybe a little.'":
            
            $ stat_sincerity += 1
            
            f_un "Yeah. I guess I'm just a little anxious. Still feel like an asshole, though."
            
    show fenira confused
            
    f_un "Still, who the hell greets someone by tackling them?"
            
    pc "She tackled you, too?"
            
    show fenira happy
            
    f_un "She sure did. Glad I'm not the only one."
    
    show fenira angry
    
    f_un "Too bad my so-called 'best friend' fucked off and left me to fend for myself."
    
    pc "Best friend?"
    
    f_un "Nagi. Part snake, part tits. Can't miss her."
    
    show fenira neutral
    
    f_un "I think she dragged the other two tenants off to help her with her stuff. A drider and a slime, I think."

    show fenira at fenira_legs with dissolve

    "This one seems to be some sort of bird hybrid. Those talons would probably be able to make short work of me. It's probably a good idea not to piss her off too much."

    show fenira at fenira_center with dissolve

    f_un "..."
    
    show fenira inquisitive
    
    f_un "Hey, uh, what's your name?"
    
    pc "I'm [pc]. You?"
    
    show fenira happy
    
    f "Fenira."
    
    f "I'm surprised. Didn't expect to see any guys here."
    
    "She extends a wing towards me. She's only got three fingers - the rest of her hand is attached to a large wing joint."
    
    show fenira vhappy
    
    "Instinctually, I grasp her version of a hand and give it a firm shake. Thankfully, this seems to be what she expected me to do - she gives me a bright smile and shakes back. She's got a strong grip."
    
    pc "Well, I'm not a tenant. I'm just a guest."
    
    show fenira confused
    
    f "A guest? You're not rooming with us?"
    
    pc "No, just stopping by until I remember."
    
    f "Remember? Remember what?"
    
    menu:
        "'Uh... everything.'":
            
            $ flag_FeniraToldAmnesia = True
            
            f "Everything? Like, everything everything?"
            
            pc "Everything everything."
            
            f "That sounds kinda serious."
            
            pc "It is. Where is everyone?"
            
        "'Oh, you know. Stuff.'":
            
            $ flag_FeniraToldAmnesia = False
            
            f "Stuff? What kind of stuff?"
            
            pc "I'll tell you when I remember. Where is everyone?"
            
    show fenira neutral
    
    f "As I said, Nagi dragged them outside while I was being assaulted."
    
    f "She's probably getting them to haul her junk up to her room."
    
    pc "Does she have a lot?"
    
    f "Well, she's under the limit. But just barely." 
    
    show fenira happy
    
    f "Me, on the other hand - I only brought a couple suitcases."
    
    show fenira neutral
    
    f "Anyways, you might wanna get out there and make sure she does her own dirty work. Don't be afraid to smack her around a bit if she's being a pain."
    
    f "..."
    
    show fenira inquisitive
    
    f "Actually, you know what? I'll come with you. If I don't, she'll probably end up talking you into helping her, too."
    
    menu:
        
        "'Do you want help with your things first?'":
            
            $ f_love += 1
            
            $ flag_OfferedFeniraUnpackHelp = True
            
            show fenira shocked
            
            f "Huh?"
            
            show fenira wink
            
            f "Oh, no, dude, that's cool. Unlike Nagi, I'm not gonna make you lug my shit up two flights of stairs."
            
            f "..."
            
            show fenira embarrassed
            
            f "But, I mean, if you wanna help me set up later, don't let me stop you."
            
            f "Or something."
            
            f "..."
            
            f "I should just quit while I'm ahead."
            
            pc "Huh?"
            
            show fenira bluffing
            
            f "Nothing! Nothing."
            
            f "C-Come on, let's go introduce you to Nagi!"
            
            $ renpy.sound.play("assets/sound/sfx/glass_break.mp3")
            
            show fenira shocked with vpunch
            
            $ renpy.pause(2.0)
            
            f "Uh."
            
            f "That didn't sound good."
            
        "'Let's go before their arms snap off.'":
            
            show fenira happy
            
            f "If that's our deadline, I'm guessing we got about thirty seconds."
            
            pc "Aw, they're probably not {i}that{/i} weak."
            
            $ renpy.sound.play("assets/sound/sfx/glass_break.mp3")
            
            show fenira shocked with vpunch
            
            $ renpy.pause(2.0)
            
            pc "I stand corrected."
            
    jump ch1_scene06
            
label ch1_scene06:
            
    scene bg yard with wipeleft
    
    show viscella scared at viscella_center with dissolve
    
    v "Um... I... um..."
    
    v "..."
    
    v "I didn't do it."
    
    show viscella scared at viscella_right with move
    
    show fenira confused at fenira_left with dissolve
    
    f "Didn't do what?"
    
    v "Drop the box full of broken glass."
    
    f "You were carrying a box full of broken glass?"
    
    v "Well, it wasn't broken before I dropped it."
    
    show fenira smirk
    
    f "..."
    
    v "..."
    
    v "I didn't do it."
    
    show fenira smirk_open
    
    f "Right. You might wanna bunker down inside. If Nagi finds out you shattered her collection of antique wine bottles, she'll..."
    
    show viscella shocked
    
    v "S-She'll?"
    
    show fenira wink
    
    f "...Well, let's hope it doesn't come to that."
    
    show viscella scared
    
    v "U-um... I- ah-"
    
    show viscella flustered
    
    v "I gotta go!"
    
    hide viscella with dissolve
    
    show fenira smirk with move:
        fenira_center_flipped
    
    f "Pffft."
    
    menu:
        
        "'That was mean.'":
            
            $ stat_sincerity += 1
            
            $ flag_FeniraRacismName = False
            
            $ flags_NagiCourtFenSupport = -1
            
            show fenira neutral
            
            f "Oh, come on. It's just a bit of fun."
            
            f "She'll realize I'm pulling her leg sooner or later."
            
            show fenira confused
            
            f "Uh. Probably."
            
            show fenira shocked
            
            stop music
            
            n_un "And when she doesn't, I'll make sure you deliver a formal apology."
            
        "'She's really gullible...'":
            
            $ flag_FeniraRacismName = True
            
            $ flags_NagiCourtFenSupport = 1
            
            f "Yeah, I didn't think that would actually work."
            
            show fenira smirk_open
            
            f "But, I mean, she's a slime. Whaddya expect, right?"
            
            show fenira happy
            
            pc "Are slimes normally gullible?"
            
            f "Well, they literally don't have brains, so I wouldn't put it past them."
            
            show fenira neutral
            
            f "Yeah, don't mind me. Casual specism is my middle name. 'Fenira Casual Specism Featherwood' they call me."
            
            f "I'll stop now."
            
            show fenira shocked
            
            stop music
            
            n_un "No, please continue." 
            
            n_un "Watching you try to dig yourself out of your own hole is the best part."
            
        "'Why are you laughing? Shouldn't we run too?'":
            
            $ flag_FeniraRacismName = False
            
            $ flags_NagiCourtFenSupport = 0
            
            f "Hah! You too?"
            
            f "Worse thing Nagi'll do is make us clean it up."
            
            show fenira neutral
            
            f "Which, now that I think about it, {i}would{/i} suck pretty bad..."
            
            show fenira shocked
            
            stop music
            
            n_un "Oh, I don't think it would be {i}that{/i} bad."
    
    play music "assets/sound/bgm/scene_comi2.ogg"
    
    f "Oh crap."
    
    n_un "Oh crap indeed."
    
    n_un "How about we play a little game, Fen-fen?"
    
    show fenira angry
    
    f "Nuh-uh. No way. You can take your dumb games and shove 'em up your-"
    
    show nagi confident at nagi_left behind fenira with dissolve
    
    n_un "Shove them up my what?"
    
    show fenira shocked at fenira_right with MoveTransition(0.2)
    
    f "Gah!"
    
    show nagi teasing
    
    n_un "The game's called 'pin the crime on the donkey'."
    
    show nagi confused
    
    n_un "Er, phoenix. Whatever."
    
    show nagi confident
    
    n_un "I came up with it myself."
    
    show fenira angry
    
    f "Look, Nagi, we didn't break your dumb bottles!"
    
    show nagi neutral
    
    n "I'm not talking about the bottles."
    
    show fenira confused
    
    f "What? But you just said-"
    
    n "And I'm not talking to you."
    
    show fenira angry
    
    n "How about you? What do you think?"
    
    n "Guilty or not guilty?"
    
    menu:
        
        "'Guilty.'":
            
            $ n_like += 1
            
            $ flags_NagiCourtFenSupport -= 1
            
            show nagi teasing
            
            n "The jury has spoken."
            
            show fenira angry
    
            show nagi confident
    
            f "Damnit, [pc], don't encourage her!"
            
            f "And what the hell are you going on about, Snaketits?!"
            
            n "Your sentence."
            
            f "What?"
            
            n "How about we of the court review the case?"
            
        "'Not guilty.'":
            
            $ f_like += 1
            
            $ flags_NagiCourtFenSupport += 1
            
            show fenira confident
            
            show nagi bored
            
            f "Thanks, [pc]. At least {i}someone's{/i} got my back around here."
            
            n "Oh? Looks like the witness has been bribed, blackmailed, or both."
            
            show fenira angry
            
            f "Not everyone who refuses to go along with your bullshit has corrupted morals, Snaketits."
            
            show nagi confident
            
            n "Really? Then how would the two of you explain the travesty that just occured before my very eyes?"
            
            show fenira vangry
            
            f "I just told you we didn't break your fucking-"
            
            show nagi bored
            
            n "Are you going to let me speak?"
            
            show fenira angry
            
            f "..."
            
            show nagi confident
            
            n "Good."
            
            
        "'Uh... what?'":
            
            f "Come on, Nagi. [pc] just met you, he's not gonna know how to react to your bullshit."
            
            n "He just needs context."
            
            show fenira confident
            
            f "Like what?" 
            
            show fenira smirk_open
            
            f "'Hi, I'm Nagi!'"
            
            show nagi bored
            
            f "'Look at me! I'm filthy fucking rich! I've got maids for my maids! My tits alone are worth more than Fenira's entire life savings, and I love it!"
            
            f "'Also, I'm a gigantic sadist who gets off on making her best friend uncomfortable!'"
            
            show fenira confident
            
            n "You could've at least put a little more effort into getting my voice right."
        
            show fenira neutral
            
            show nagi neutral
            
            n "Besides, that's not the kind of context [pc] is looking for, is it?"
            
            n "How about we of the court review the case?"
            
    n "An adorable little slime shatters a collection of wine bottles that date back to the nineteenth century."
    
    f "Then why are you-"
    
    show nagi bored
    
    n "Would you please shut up, Fen-fen?"
    
    n "Ahem."
    
    show nagi confident
    
    if flag_FeniraRacismName:
    
        n "After freezing like a deer in headlights, the slime is approached by our suspect, Fenira Casual Specism Featherwood." 
    
        show fenira angry
    
        f "Son of a-"
    
    else:
       
        n "After freezing like a deer in headlights, the slime is approached by our suspect, Fenira Featherwood." 
    
    n "Accompanying her is a new acquaintence and love interest, a young Mr. [pc]."
    
    show fenira embarrassed
    
    f "Fuck off, Nagi!"
    
    n "After a brief altercation, the suspect informs the slime that, and I quote..."

    show nagi neutral

    n "'If Nagi finds out you shattered her collection of antique wine bottles, she'll...'"
    
    show fenira confused
    
    f "..."
    
    show nagi neutral
    
    n "..."
    
    f "She'll?"

    n "Yes, well, you didn't actually {i}say{/i} what I would do."
    
    n "But the intention was clear."
    
    show fenira angry
    
    f "What kinda fucked up justice system are you running off of?"
    
    show nagi confident
    
    n "I like to call it the 'common sense' school of justice."
    
    n "Regardless, here's my current situation."
    
    show nagi angry
    
    n "Because you decided to repay my friendship with lies and slander, I now have a roommate with an overactive imagination who thinks I'm the devil incarnate."
    
    f "She's not far off..."
    
    show nagi neutral
    
    n "Oh, don't be like that."
    
    show fenira confused
    
    f "This isn't a big deal. Fuck, she's probably forgotten all about it. Just tell her I was screwing with her."
    
    n "I don't want to."
    
    show fenira angry
    
    f "Why the hell not?!"
    
    n "I have better things to do."
    
    f "In other words, you're lazy. Big surprise there."
    
    show nagi confident

    n "Perhaps."
    
    n "But, unlike you, that's the extent of my crimes."

    n "It's the slanderer's duty to undo her handiwork. Don't you agree, [pc]?"
    
    menu:
         
        "'Well, that goes without saying...'":
            
            $ n_like += 1
            
            $ flags_NagiCourtFenSupport -= 1
            
            n "See?"
            
            f "That was a dumb question. Anyone would agree with that."
            
            n "Including you, I presume?"
            
        "'Aren't you blowing this a little out of proportion?'":
            
            $ f_like += 1
            
            $ flags_NagiCourtFenSupport += 1
            
            n "Please. I just want to make sure I'm making a good first impression on my new roommates."
            
            n "Is that so wrong?"
                    
            f "Then why the hell didn't you just ask me to apologize instead of making us play your stupid game?"
            
            n "That'd be boring."
            
            f "Are you serious?"
            
            f "I swear to god, Nagi. Sometimes you make me want to tear my feathers out."
            
            show nagi teasing
            
            n "Only sometimes?"
            
        "'I exercize my right to remain silent.'":
            
            n "Oh? Don't make me put you down for obstruction of justice."
    
            f "Are you done with this shit? Can you please just introduce yourself like a normal chimera?"
    
            n "Is that what you want?"
            
            n "Then how about we make a deal?"
            
            n "You go explain our little misunderstanding, and I'll make sure [pc] doesn't think you're best friends with a basket case."
            
    show nagi confident
            
            
    if flags_NagiCourtFenSupport <= -1:
    
        $ n_like += 2
    
        show fenira sad
        
        f "Fuck. You guys are making me look like the bad guy."
        
        f "I'm sorry, okay? It was harmless fun. Can I go now?"
        
        n "To apologize?"
        
        f "What do you think, smartass?"
        
        show nagi happy
        
        n "Just asking. Don't let me stop you."
        
        f "I have no idea how I'm going to survive living with you {i}and{/i} that kitsune."
    
        show nagi confident    
    
        n "It'll be fine. Just keep your eyes on the prize."
    
        show fenira neutral
    
        show nagi teasing
    
        n "Only your eyes, though. Don't want you to end up with a restraining order."
        
    elif flags_NagiCourtFenSupport >= 0 and flags_NagiCourtFenSupport <= 1:
    
        $ n_like += 1
        
        $ f_like += 1
        
        show fenira angry
        
        f "Damnit, Nagi, no more games. I'll apologize, okay?"
        
        show nagi happy
        
        n "Good girl."
        
        f "Don't you 'good girl' me."
        
        show fenira neutral
        
        f "I have no idea how I'm going to survive living with you {i}and{/i} that kitsune."
    
        show nagi confident    
    
        n "It'll be fine. Just keep your eyes on the prize."
    
        show nagi teasing
    
        n "Only your eyes, though. Don't want you to end up with a restraining order."
    
    
    elif flags_NagiCourtFenSupport >= 2:
            
        $ f_like += 2
        
        f "No, you know what? We're done here. I don't need this shit, and [pc] definitely doesn't need this shit."
        
        show nagi bored
        
        n "Is that so?"
        
        f "That {i}is{/i} so. Now if you'll excuse me, I have some unpacking to do."
        
        f "Come on, [pc]."
        
        show nagi surprised
        
        n "Huh?"
        
        n "Oh, no no no, Fen-fen. You can't take [pc] with you."
        
        f "Why the fuck not? He can go where he wants, and right now I bet the last place he wants to be in front of you."
        
        show nagi neutral
        
        n "That's nice, but I'm pretty sure [pc] can speak for himself."
        
        if flag_OfferedFeniraUnpackHelp:
        
            f "Ugh, fine! Listen, [pc], remember when I said you can help me unpack? Well, I was serious. You're free to come over whenever you get tired of Snaketits here."
            
        else:
            
            #$ flag_OfferedFeniraUnpackHelp = True
            
            f "Ugh, fine! Listen, [pc], if you wanna get away from this tool later you can come help me unpack."
            
            
        f "I'll make sure she doesn't try sticking that tongue of hers where it doesn't belong."
            
        show nagi teasing
            
        n "Oooh, inviting him to your bedroom already? Are you sure it's my tongue he should be worried about?"
            
    show fenira embarrassed
    
    stop music fadeout 2.0
    
    f "S-screw you, Snaketits!"
    
    hide fenira with dissolve
    
    show nagi neutral at nagi_center_flipped with move
        
    play music "assets/sound/bgm/093.mp3" fadein 3.0
        
    n "Well, that was fun."
    
    if flags_NagiCourtFenSupport <= -1:
        
        n "Thanks for playing along, by the way."
    
    n "As you probably gathered, I'm Nagi."
    
    n "And, as I gathered, you're [pc], so I think we can safely skip the introductions you've probably been exchanging all day."

    #show nagi intro
    
    show nagi neutral at nagi_full with dissolve
    
    "That's... a lot of snake. Her tail's probably over four meters long. I can only imagine how much she needs to eat."
    
    show nagi neutral at nagi_center_flipped with dissolve
    
    n "If you were looking for your drider friend, she's by the moving van. Probably still trying to lift that box of clothes I handed her."
    
    n "We should probably go help, huh?"
    
    menu:
        
        "'Yeah. Don't want her to hurt herself.'":
            
            $ n_like += 1
            
            show nagi happy
            
            n "Little too late for that, I think."
            
        "''We' as in me and you, or 'we' as in me?'":
            
            show nagi bored
            
            n "What's that dumb bird been telling you? I {i}can{/i} be helpful."
            
            n "You know."
            
            show nagi neutral
            
            n "Sometimes."
            
    jump ch1_scene07
            
