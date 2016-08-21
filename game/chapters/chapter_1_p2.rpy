            
label ch1_scene07:
            
    scene bg street with wipeleft
    
    show kumiru sad with dissolve:
        xpos 0.3
        xanchor 0.5
        ypos 0.6
        yanchor 327
    
    ku "Huff... huff..."
    
    ku "I guess I have no choice. I'll have to drag it."
    
    show kumiru angry
    
    ku "Hnnn!"
    
    $ renpy.sound.play("assets/sound/sfx/wood_drag.wav", fadeout=0.5)
    
    show kumiru angry at kumiru_right with MoveTransition(2.5)

    
    $ renpy.sound.play("assets/sound/sfx/body_hit.wav")
       
    show kumiru angry open with vpunch
       
    ku "Gah, damnit!"
    
    show kumiru sad
    
    ku "A splinter? Come on..."
    
    n "Well, you've moved it a few feet, at least."
    
    show nagi neutral with dissolve:
        nagi_left
        
    show kumiru shocked
        
    ku "Ah, Miss Forques!"
    
    ku "And [pc]!"
    
    show kumiru surprised
    
    ku "..."
    
    show kumiru embarrassed
    
    ku "Well, this is embarrassing."
    
    n "Just call me Nagi."
    
    n "So why'd you offer to carry it if you couldn't handle it?"
    
    show kumiru confident
    
    ku "Because it was the polite thing to do."
    
    ku "..."
    
    show kumiru sad
    
    ku "And it would've been pretty embarrassing if I wasn't able to lift what's basically just a big wooden box."
    
    n "Nah, that thing's stuffed with my winter clothes. Need a hand?"
    
    ku "Um... yes."
    
    "You and Nagi each grab one end of the box and lift. It's... not that heavy."
    
    menu:
        
        "'Whew, this thing weighs a ton! {i}Right, Nagi?{/i}'":
            
            $ n_like += nagAff(1)
            
            show kumiru happy
            
            show nagi surprised
            
            n "Huh?"
            
            show nagi wink
            
            n "Oh, yeah, totally. Feels like my spine's about to give out on me."
            
            show nagi happy
            
            n "And my spine's as strong as you'd expect."
            
            show kumiru confused
            
            ku "You know..."
            
            ku "You vaguely remind me of our new kitsune tenant."
            
            show nagi bored
            
            n "I've got the feeling that's a bad thing."
               
            show kumiru surprised
            
            ku "Vaguely! Vaguely."
            
            show kumiru neutral
            
            n "And I've got the feeling that's a good thing. Alright, [pc]. One-step two-step."
            
        "'Huh. This isn't too bad.'":
            
            show kumiru sad
            
            ku "W-well..."
            
            ku "You know..."
            
            ku "I had to lift it all alone..."
            
            show nagi confident          
            
            n "Don't worry about it."
            
            show nagi teasing
            
            n "[pc]'s just trying to impress you."
            
            show kumiru embarrassed
            
            show nagi confident
            
            n "Right, [pc]?"
            
            menu:
                
                "'You caught me.'":
                    
                    $ ku_love += kumAff(1)
                
                    show nagi wink
                    
                    show kumiru flustered
                    
                    n "See?"
                    
                    ku "E-Erm..."
                    
                    show nagi teasing
                            
                    n "You're blushing."
                    
                    show kumiru embarrassed
                    
                    ku "Of course I am. You're making fun of me."
                
                    show nagi confident
                    
                    n "Just a little. Come on, [pc], let's bring this inside."
                    
                "'Maybe I'm trying to impress {i}you{/i}?'":
                    
                    $ n_love += nagAff(1)
                    
                    show nagi neutral
                    
                    n "Are you, now?"
                    
                    show nagi wink
                    
                    n "Well, it might be working."
                    
                    show nagi confident
                    
                    show kumiru embarrassed
                    
                    ku "Guys..."
                    
                    n "Whoops. C'mon, we can flirt later."
                    
                    ku "Guys!"
                    
                    show nagi happy
                    
                    n "Sorry, sorry."
                
                "'Har har.'":
                    
                    n "See? He didn't deny it."
                    
                    ku "Right..."
                    
                    show nagi teasing
                            
                    n "You're blushing."
                    
                    show kumiru embarrassed
                    
                    ku "Of course I am. You're making fun of me."
                
                    show nagi confident
                    
                    n "Just a little. Come on, [pc], let's bring this inside."

    stop music fadeout 2.0
   
    scene bg nBedroom with wipeleft
      
    "Nagi and I manage to bring the crate up to her room with little effort."
 
    play music "assets/sound/bgm/082.mp3" fadein 2.0
    
    show kumiru neutral at kumiru_right
    
    show nagi happy at nagi_left
    
    with dissolve
    
    n "And... done."
    
    show kumiru happy
    
    ku "Thank you very much."
    
    show nagi confused
    
    n "Why are you thanking me?"
    
    ku "For the help, of course."
    
    n "Right."
    
    n "For {i}my{/i} help bringing {i}my{/i} stuff up to {i}my{/i} room."
    
    show kumiru confused
    
    ku "..."
    
    ku "You're right. Why {i}am{/i} I thanking you?"
    
    show nagi happy
    
    n "Beats me. Not that I mind having someone polite around. Especially after dealing with Fenira for nearly a decade."
    
    menu:
        
        "'You sure like ribbing on her, don't you?'":
            
            show kumiru neutral
            
            show nagi wink
            
            n "You bet. Isn't that what friends are for?"
            
            show nagi happy
            
            n "Besides, I'm fair."
            
            n "Sometimes I let her talk smack without me smacking back."
            
            show nagi teasing
            
            n "Sometimes."
            
        "'A decade?'":
            
            show kumiru neutral
            
            show nagi neutral
            
            n "Yeah, we go waaay back."
            
            n "I've spent a good chunk of my life with birdbrain, in fact."
            
            n "I'm what? Twenty? Twenty one?"
            
            ku "..."
            
            show kumiru confused
            
            ku "Er... why are asking me?"
            
            n "Huh? No reason."
            
            show nagi confused
            
            n "Probably twenty three, actually..."
            
            ku "Sorry?"
            
            show nagi neutral
            
            n "Nothing, nothing."
    
    show nagi neutral
    
    show kumiru neutral
    
    n "Anyways, where were we? Oh, right. Thanks for the help."
    
    "Nagi gives us a little smile."
    
    show kumiru sad
    
    ku "S-sorry for not actually doing much..."
    
    n "Huh? Pfff, it's fine. Effort over results, yadda yadda."
    
    n "Anyways, I woke up this morning at six AM on another continent, so I'm exhausted. If you don't mind, I'm gonna collapse on my bed."
    
    show kumiru neutral
    
    ku "O-oh. Sorry for taking up your time."
    
    n "You should keep count."
    
    show kumiru surprised
    
    ku "Huh?"
    
    show nagi happy
    
    n "How many 'thank-you's and 'sorry's have you said in the past ten minutes?"
    
    ku "Uh..."
    
    show kumiru confused

    ku "Hmmm..."
    
    show nagi neutral
    
    n "I'm... not serious."
    
    show nagi happy
    
    n "Anyways, thanks for the fun. See ya around."
    
    play sound "assets/sound/sfx/door_open.wav"
    
    scene bg hallway with CropMove(1.5, mode="wipeleft")
    
    play sound "assets/sound/sfx/door_close.wav"
    
    show kumiru confused at kumiru_center with dissolve
    
    ku "Once at the door... once up the stairs, when I bumped into you... I think there was one when I opened the door without permission..."
    
    pc "Kumiru?"
    
    show kumiru surprised
    
    ku "Huh? Wha?"
    
    "Kumiru's many eyes blink a few times, and then she gives a nervous cough."
    
    show kumiru sad
    
    ku "Uh... w-well, it seems that pretty much everyone is starting to settle in."
    
    ku "Which is... good..."
    
    show kumiru embarrassed
    
    ku "..."
    
    show kumiru surprised
    
    ku "Oh! Any luck with your memories?"
    
    "You shake your head."
    
    pc "I wish. I'm still half-expecting this to be all some sort of weird dream."
    
    show kumiru neutral
    
    ku "That would probably make this a lot simpler, wouldn't it?"
    
    ku "Well, even if this isn't some sort of dream, I'm sure we'll be able to get your memories back."
    
    menu:
        
        "'Thanks. I'll need all the help I can get.'":
            
            show kumiru happy
            
            ku "Of course. "
            
            show kumiru neutral
            
            ku "I can't even imagine what it's like to forget everything."
            
            pc "I don't think I've forgotten it, exactly."
            
            show kumiru confused
            
            ku "What do you mean?"
            
            pc "It feels like something's missing, but still present. Like it's just out of reach."
            
            ku "Really? That doesn't sound like the memory loss caused by a nightmare."
                
            show kumiru happy
                
            ku "Maybe all you need is a good night's sleep."
            
            pc "Yeah."
            
        "'No rush. Maybe this isn't so bad.'":
            
            show kumiru confused
            
            ku "What do you mean?"

            pc "Well, it's not like I'm under pressure. No reason to stress out over it."
            
            ku "But you can only stay here for a few days before you have to leave..."
            
            pc "That's plenty of time."
            
            show kumiru neutral
            
            ku "You're remarkably relaxed for someone who's lost all their memories."
            
            pc "Well, who knows? Maybe this is a good thing. For all I know, I could have been the world's most depressed man."
            
            show kumiru happy
            
            ku "I guess that's one way to think about it. Though I'm not sure if that makes you an optimist or a pessimist."

    show kumiru neutral

    ku "Well, anyways, I need to finish unpacking."
    
    ku "Viscella and I hadn't even finished exploring when we ran into you."
    
    show kumiru happy
    
    ku "Which explains why two shut-ins like us were the first people to find you."
    
    show kumiru confused
    
    ku "Speaking of Viscella, I haven't seen her in a while. I wonder where she's gone off to...?"
    
    ku "Nevermind what I said about unpacking. I should probably prioritize finding her..."
    
    show kumiru unamused
    
    ku "You know, before she flushes herself down a toilet by accident."
    
    show kumiru neutral
    
    ku "See you around, okay?"

    hide kumiru with dissolve
    
    "The rest of the house seems to be preoccupied with setting up their rooms. I decide to do the same."
    
    play sound "assets/sound/sfx/door_open.wav"
    
    scene bg pBedroom with CropMove(1.5, mode="wipeleft")
    
    play sound "assets/sound/sfx/door_close.wav"
    
    #$ setTime(5)
    
    #$ clock_access = True
    
    "Oh, right."
    
    "I've only got the clothes on my back. I couldn't set up my temporary living quarters even if I wanted to."
    
    "Well, looks like I've got some time on my hands. How should I spend it?"
    
    menu:

        "Help Kumiru look for Viscella.":
            
            "If what Kumiru said is anything to go by, Viscella's been missing."
            
            "To be fair, I saw her less than half an hour ago, so it's not exactly a life-or-death situation."
            
            "Regardless, I decide to join Kumiru's one-drider search party."
            
            jump ch1_scene08_visSearch

        "Help Fenira set up.":
            
            if flags_NagiCourtFenSupport >= 2:
            
                "I recall Fenira offering to shield me from Nagi if I went to help her unpack."
                    
                "I don't exactly need to be shielded, but there's no harm visiting regardless."
        
            elif flag_OfferedFeniraUnpackHelp:
                
                "I recall offering Fenira help unpacking her things. I also vaguely recall her awkwardly accepting."
                    
                "I decide to go pay her a visit."
                
            else:
                
                "I decide to go see what Fenira's up to."
                
                "Maybe I'll be able to make conversation now that she's not being harassed by Nagi."
        
            jump ch1_scene08_fenVisit
            
        "Pay Nagi a visit.":
            
            "Nagi said she was going to collapse on her bed."
               
            "She didn't actually say she was going to sleep on it."
            
            "I decide to take advantage of this loophole."
            
            jump ch1_scene08_nagVisit
        
        "Take Kamao up on her offer.":
            
            "Kamao said she would give me a prize if I went to visit her."
            
            "There's no telling what the prize is, though I have a few good guesses... well, only one way to find out."
    
            jump ch1_scene08_kamVisit  
    
label ch1_scene08_visSearch:  
    
    $ v_like += visAff(2)
    
    $ ku_like += kumAff(2)
    
    stop music fadeout 2.0
    
    scene bg living with Dissolve(1.0)
    
    ku "Viscella? Viscella!"
    
    show kumiru confused at kumiru_center with dissolve
    
    play music "assets/sound/bgm/tam-n06.mp3" fadein 2.0
    
    ku "Where on earth has she gone off to?"
    
    pc "Need a hand?"
    
    show kumiru surprised
    
    ku "Oh, [pc]! What are you doing down here?"
    
    pc "I thought I'd help you look for your friend."
    
    show kumiru neutral
    
    ku "Are you sure? Knowing Viscella, it may take a while..."
    
    pc "I've got nothing better to do."
    
    show kumiru happy
    
    ku "Well, if you say so."
    
    show kumiru neutral
    
    ku "I doubt she's outside, and she's not in her room. I figured she'd come find me as soon as she was done carrying Miss Fo- I mean, Nagi's wine inside."
    
    pc "Uh, about that..."
    
    show kumiru unamused
    
    ku "She broke the bottles, didn't she?"
    
    pc "How'd you know?"
    
    show kumiru neutral
    
    ku "Well, we passed an upside-down box that looked like it had been abandoned in a hurry."
    
    pc "Yeah."
    
    ku "I just wish she would stop running from her problems. She acts so immature sometimes. It's easy to forget she's nineteen, you know?"
    
    ku "If she doesn't learn to take care of herself, she's not going to be able to survive out on her own. I can't hold her hand forever."
    
    ku "..."
    
    show kumiru sad
    
    ku "Sorry. I shouldn't go on like this behind her back."
    
    ku "Anyways, I'll go check the basement. Could you look for her on the second floor?"
    
    pc "Sure."
    
    show kumiru happy 
    
    ku "Thanks. Good luck."
    
    scene bg hallway with dissolve
    
    "Well, time to get started."
    
    pc "Viscella?"
    
    "No response."

    scene bg theatre with wipeleft
    
    "The room's deathly quiet."
    
    pc "Viscella?"
    
    "Nothing."
    
    scene bg rec with wipeleft
    
    "The room's empty, though it looks like someone's raided the alcohol cabinet by the bar."
    
    pc "Viscella? Hello?"
    
    "Unsurprisingly, nothing."
    
    scene bg study with wipeleft
    
    pc "Are you in here, Viscella?"
    
    "The silence is my answer."
    
    scene bg gym with wipeleft
    
    pc "Viscella?"
    
    pc "What am I thinking? Of course she wouldn't be in here."
    
    v "W-why not?!"
    
    "You pause. The voice came from the closet."
    
    pc "Viscella? What are you doing in there?"
    
    v "Nothing!"
    
    "You approach the closet door and pull it open."
    
    show viscella scared at viscella_center with dissolve
    
    v "Um."
    
    v "You see nothing."
    
    pc "Right. What are you doing?"
    
    v "Hiding. From {i}her{/i}."
    
    pc "Who, Nagi?"
    
    v "Yeah. She's gonna do something bad to me."
    
    pc "Fenira was just screwing with you. Nagi doesn't care."
    
    show viscella confused
    
    v "She... doesn't?"
    
    if flags_NagiCourtFenSupport < 2:
        
        pc "No. Didn't Fenira tell you? She told us she was going to apologize."
        
        v "Oh..."
        
        show viscella neutral
        
        v "That explains why she poked her head in here looking all aggravated..."
    
    else:
    
        pc "No. In fact, she was upset with Fenira for misleading you."
        
        v "So... I've been hiding for half an hour for no reason?"
        
        pc "None whatsoever."
        
        show viscella neutral
        
        v "Whew. That's a relief."
    
    menu:
        
        "'Come on. I think Kumiru's worried about you.'":
            
            show viscella angry
            
            v "Really? Jeeze, I'm not a kid. I can look after myself."
            
            pc "She said you might accidentally flush yourself down a toilet."
            
            show viscella flustered
            
            v "That happened one time!"
            
            pc "Really? How?"
            
            show viscella embarrassed
            
            v "I... don't wanna talk about it."
            
            pc "Well, suit yourself."
    
        "'Come on. I think Kumiru's annoyed with you.'":
        
            v "Yeah, probably."
            
            v "She's annoyed with me a lot."
            
            pc "Why?"
            
            show viscella angry
            
            v "I don't know! And she gives me that dumb look of hers all the time!"
            
            pc "What dumb look?"
            
            show viscella neutral
            
            v "You know."
            
            v "The one that she makes when you say something stupid."
    
            pc "Uh... right."
            
    pc "Either way, you shouldn't be hiding in closets."
    
    v "Why not?"
    
    menu:
        
        "'It's immature.'":
            
            show viscella scared
            
            v "It is?"
            
            pc "Well, you're an adult, right?"
            
            show viscella angry
            
            v "Y-yes!"
            
            pc "When was the last time you saw an adult hiding in a closet?"
            
            show viscella happy
            
            v "Blade X Oblivion season two episode seven."
            
            v "Aura hides in a closet from her mother's geist."
            
            pc "But I'm assuming she's not hiding because she broke the geist's stuff, right?"
            
            show viscella excited
            
            v "Actually-"
            
            pc "It was a rhetorical question."
            
            show viscella neutral
            
            pc "Are you ready to go back downstairs?"
        
        "'There are way better hiding places than closets.'":
            
            $ v_love += visAff(1)
            
            show viscella shocked
            
            v "Huh?"
            
            pc "Yeah. Closet's beginner level."
            
            show viscella happy
            
            pc "Unless you're buried in a pile of laundry. That one's pretty effective."
            
            pc "Sorry, you got me sidetracked."
            
            show viscella confident
            
            v "No, sensei. I won't forget your guidance."
            
            pc "Good, my student. Now let's rejoin civilized society."
            
    show viscella neutral
            
    v "Um, before we go..."
    
    show viscella embarrassed
    
    v "Could you not tell Kumiru what I was doing?"
    
    pc "Huh?"
    
    v "She always treats me like a kid. She probably thinks I was up here hiding from my problems rather than facing them..."
    
    pc "Isn't that exactly what you were doing?"
            
    v "Well, yes... but can you not tell her that? Please? I want her to think there's some hope for me..."
 
    pc "So... you want me to lie to her?"
    
    v "It's not lying! It's just... not telling. It's not the same, right?"
    
    v "Please?"
    
    pc "We'll see."
    
    v "A-alright..."
    
    scene bg living with Dissolve(1.5)
    
    "Viscella and I return to the living room. Kumiru seems to have been waiting for us."
    
    show kumiru neutral at kumiru_center with dissolve
    
    ku "No luck in the base- oh, you found her."
    
    show kumiru neutral at kumiru_right with move
    
    show viscella neutral at viscella_left with dissolve
    
    v "You don't sound very relieved."
    
    ku "Well, you were bound to turn up eventually."
    
    ku "Where were you hiding?"
    
    show viscella scared
    
    v "Um... hiding?"
    
    ku "Yes, hiding."
    
    v "Who said anything about hiding?"
    
    ku "Well, we assumed that's what you were doing. You broke Nagi's wine bottles, didn't you?"
    
    v "I... um..."
    
    v "I..."
    
    show viscella flustered
    
    v "I wasn't hiding!"
    
    show viscella scared
    
    show kumiru surprised
    
    ku "You... weren't?"
    
    v "N-no!"
    
    ku "Then what were you doing?"
    
    show viscella scared
    
    "Viscella glances desperately at me."
    
    v "I... I..."
    
    menu:
        
        "'Sorry, Viscella. I mean, she's spot on...'":
            
            $ ku_love += kumAff(2)
            
            $ ku_like += kumAff(1)
            
            $ flag_HelpedViscellaLie = False
            
            show kumiru unamused
            
            show viscella flustered
            
            v "Y-you told her! You weren't supposed to tell her!"
            
            ku "I see. So not only did you hide, you tried to get [pc] to lie for you, too."
            
            show viscella scared
            
            v "I... um..."
            
            show viscella sad
            
            v "I..."
            
            ku "It would have been fine if you were hiding, Viscella. But lying to me? Come on."
            
            v "I'm sorry..."
            
            ku "It's okay. Just be honest with me, alright?"
            
            v "Okay..."
            
            show kumiru happy
            
            ku "Thank you."
            
            ku "Now go apologize to Nagi."
            
            show viscella flustered
            
            v "But I-"
            
            show kumiru unamused
            
            ku "Right now."
            
            show viscella sad
            
            v "..."
            
            v "Okay..."
            
        "'She was trying out the karaoke machine.' (Lie)":
            
            $ v_love += visAff(2)
            
            $ v_like += visAff(1)
            
            $ flag_HelpedViscellaLie = True
            
            show viscella confident
            
            v "Y-yeah! I was super excited to play so I figured I'd find out how the machine works!"
            
            show kumiru confused
            
            ku "Your first instinct after breaking Nagi's property is to run off and play karaoke?"
            
            v "I forgot."
            
            ku "Forgot what?"
            
            v "That I was on the run."
            
            show kumiru unamused
            
            ku "Well, that I {i}can{/i} believe."
            
            show viscella happy
            
            show kumiru happy
            
            ku "Thanks for the help, [pc]. I guess I was worried over nothing."
            
            v "Yeah, [pc]. Thanks."
            
            show viscella embarrassed
            
            v "A lot."
            
            show kumiru unamused
            
            ku "Hold on."
            
            ku "Shouldn't you be apologizing to a certain lamia?"
            
            show viscella shocked
            
            v "Uh."
            
            ku "Go on."
            
            show viscella neutral
            
            v "Aw..."
            
            
        "Say nothing.":
            
            $ flag_HelpedViscellaLie = False
    
            $ ku_like += kumAff(1)
            
            $ v_like += visAff(1)
    
            v "I... I was... um..."
            
            v "Sleeping?"
            
            v "In the..."
            
            v "..."
            
            v "Exercise room."
            
            show kumiru unamused
            
            show viscella neutral
            
            ku "..."
            
            v "..."
            
            ku "Right."
            
            ku "You were hiding in a closet somewhere, weren't you?"
            
            show viscella flustered
            
            v "H-how'd you know?!"
            
            ku "Experience."
    
            ku "Now I think you owe Nagi an apology."
    
            show viscella flustered
            
            v "But I-"
            
            show kumiru unamused
            
            ku "Right now."
            
            show viscella sad
            
            v "..."
            
            v "Okay..."
    
    
    hide viscella with dissolve
    
    show kumiru neutral at kumiru_center with move
    
    ku "Well, that's all dealt with."
    
    if flag_HelpedViscellaLie == False:
        
        ku "Thanks, [pc]. It's nice having someone around I can count on."
        
        ku "Viscella just needs to spend some time in the real world. Her head's always up in the clouds."
        
        ku "Don't get me wrong - I love that about her. But she can't just run away when the going gets rough."
        
        ku "I used to do that, and it never got me anywhere."   
        
    else:
    
        ku "Thanks again, [pc]. It's nice to be pleasantly surprised once in a while."
        
        ku "I guess that it's not fair of my to always assume the worst of Viscella."
        
        show kumiru sad
        
        ku "Well, certainly not the {i}worst{/i}."
        
        ku "But you know what I mean."
        
    show kumiru happy
    
    ku "Sorry, I'm ranting. Anyways, I really appreciate the help. I'll let you get going."
    
    ku "Wouldn't want to get in the way of that good night's rest."
    
    jump ch1_scene09
            
 
label ch1_scene08_fenVisit:
    
    $ f_like += fenAff(4)
        
    
    $ flag_VisitedFenira = True
    
    scene bg hallway with dissolve
    
    if flag_RoomBesideKumiru:
        
        "The door across from me, which I remember to be Kamao's, is ajar. I stealthily slip past in order to avoid detection, and approach the room two doors over."
        
        "Fenira must have taken the room wedged in the corner, across from Viscella."
    
    else:
        
        "The door to my left, which I remember to be Kamao's, is ajar. I stealthily slip past in order to avoid detection, and approach the opposite end of the hallway."
        
        "If Kamao and Nagi took the two rooms beside you, Fenira must have taken the room beside Kumiru."
    
    "As I approach, I can start to hear music on the other side of the door."
    
    play sound "assets/sound/sfx/knock.ogg"
    
    stop music fadeout 2.0
    
    "I give it a knock."
    
    f "It's open. Unless you've got a tail. Then it's locked."
    
    "I push open the door."
    
    scene bg fBedroom with dissolve
    
    play music "assets/sound/bgm/093.mp3" fadein 2.0
    
    if flags_NagiCourtFenSupport >= 2:
    
        f "Oh, hey [pc]!"
           
        show fenira vhappy at fenira_center with dissolve
        
        f "What's up?"
        
        show fenira neutral
        
        f "Which one do you need me to punch?"
        
        pc "Neither, actually. Just thought I'd stop by."
        
        show fenira vhappy
        
        f "Hey, great!"
        
        
    elif flag_OfferedFeniraUnpackHelp:
        
        f "Oh, [pc]! You showed!"
        
        show fenira vhappy at fenira_center with dissolve
        
        pc "You sound surprised."
        
        show fenira happy
        
        f "I'd figured Nagi ruined your plans. Glad to see that's not the case."
        
        pc "Nah, she passed out on her bed."
        
        f "Figures. She's not an early riser."
        
        f "Anyways, you arrived just in time."
        
    else:
        
        f "[pc]?" 
        
        show fenira happy at fenira_center with dissolve
        
        f "Don't mind the mess. What's up?"
        
        pc "Just thought I'd stop by and visit."
        
        show fenira shocked
        
        f "Visit me? Seriously?"
        
        pc "Is that bad?"
        
        show fenira vhappy
        
        f "No way!"
        
        show fenira happy
        
        "I'm not gonna be a lot of fun right now, though. I'm still unpacking."
        
    show fenira vhappy
        
    f "You get to watch me pull out all my trophies." 
    
    show fenira wink
    
    f "Try not to be too impressed."
    
    menu:
        
        "'Athletic trophies?'":
            
            show fenira neutral
            
            f "Nah, academic."
            
            f "..."
            
            show fenira happy
            
            f "Just screwing with you."
            
            show fenira wink
            
            f "What, don't think I have the brains to go with my brawn?"
        
            show fenira neutral
            
            f "Cuz, uh, you'd be right."
            
        "'Academic trophies?'":
            
            show fenira neutral
            
            f "I wish."
            
            f "Maybe then I wouldn't be working at a gas station."
            
            f "Besides, they don't give trophies for academics, do they? Just certificates."
            
            f "Dunno why. Maybe smart kids complain less when the reward for all their effort is a flimsy sheet of paper?"
            
            f "Either way, I consider it a win."
            
            show fenira happy
            
            f "When the kitsune tries sneaking into my room while I'm sleeping, I can at least bludgeon her with the trophies. Wouldn't be able to do that with a certificate. Fenira 1, Society 0."
            
    pc "Uh, about those trophies..."
    
    show fenira happy
    
    f "Oh, right. Yeah, most of 'em are from middle school. Soccer and track, that kinda thing."
    
    show fenira neutral
    
    f "Except this one."
    
    "Fenira holds up a decently-sized golden trophy. Sculpted on it is an individual so tightly bound in a snowsuit that their joints are locked at ninety-degree angles from their body, and their features are indistinguishable."
    
    "I get a closer look at the engraving."
    
    "BEST DRESSED 2007"
    
    show fenira happy 
    
    f "I used to snowboard, but..."
    
    f "I hate the cold."
    
    show fenira neutral
    
    f "Anything below forty pisses me off, and it was something like minus six degrees that day. Not including wind chill. What was I supposed to wear, short shorts?"
    
    f "Nagi laughed at me for weeks. Then she made this."
    
    menu:
        
        "'Wait, {i}Nagi{/i} made this?":
            
            show fenira happy
            
            f "You kidding? She paid someone else to do it."
            
            f "I've never seen anyone put so much money into an inside joke."
            
            show fenira neutral
            
            f "Though I guess getting a custom-made trophy is probably pennies for her."
            
        "'Wait, you {i}snowboarded{/i} in that?":
    
            show fenira happy
    
            f "Not really. I just kinda... rolled."
            
            pc "Down a ski hill?"
            
            show fenira vhappy
            
            f "Down a ski hill."
            
            show fenira happy
            
            f "Had too much padding to worry about getting hurt."
            
            show fenira neutral
            
            f "Until I hit the minotaurus, that is."

    "Fenira places the trophy on her bed, with all the rest."
    
    f "Well, that's pretty much everything. Yeah, I'm not a very exciting packer, I know."
    
    f "Oh, that reminds me - have you seen that slime around?"
    
    pc "Viscella? I haven't. Kumiru's looking for her."
    
    f "What, she missing or something?"
    
    pc "Well, Kumiru hasn't seen her."
    
    f "Shit. You think I made her run off or something?"
    
    menu:
        
        "'Probably.'":
            
            show fenira sad
            
            f "Damnit."
            
            f "You wanna help me find her and convince her that Nagi's not actually going to drag her into her torture dungeon?"
            
        "'Probably not.'":
        
            show fenira happy
        
            f "I hope so. Still, I should probably go find her and correct our little misunderstanding. Wanna help?"
    
    if flags_NagiCourtFenSupport >= 2:
    
        pc "I thought you decided that was Nagi's job?"
        
        f "Yeah, but I guess I've had a change of heart. I get kinda stupid when I'm angry."
        
        show fenira happy 
        
        f "Don't get me wrong, though. I still appreciate you backing me up."
    
        f "Anyways, what do you say? Wanna go on a slime hunt?"
    
    pc "Sure. I don't have much else to do."
        
    show fenira vhappy
        
    f "Great!"
    
    f "Last one to find her gets to apologize!"

    menu:
        
        "'Hey, wait, I never agreed to-'":
            
            $ flag_AcceptedFeniraChallenge = False
            
            hide fenira with dissolve
            
        "'You better start rehearsing, then!'":
            
            $ flag_AcceptedFeniraChallenge = True
            
            $ f_love += fenAff(1)
            
            show fenira confident
            
            f "Oh, I'll be rehearsing, alright. Rehearsing my victory dance!"
            
            hide fenira with dissolve
            
    "Fenira bolts it out the door. Looks like it's a race."
                
    "I decide to start my search on the second floor."
    
    scene bg hallway with wipeleft
    
    "Fenira's checking the basement. I can only hope that Viscella's up here, and not down there."
                
    "Well, time to get started."
    
    pc "Viscella?"
    
    "No response."

    scene bg theatre with wipeleft
    
    "The room's deathly quiet."
    
    pc "Viscella?"
    
    "Nothing."
    
    scene bg rec with wipeleft
    
    "The room's empty, though it looks like someone's raided the alcohol cabinet by the bar."
    
    pc "Viscella? Hello?"
    
    "Unsurprisingly, nothing."
    
    scene bg hallway with wipeleft
    
    "Sounds like someone's sprinting up the stairs. Must be Fenira."
    
    "I need to hurry. But which room should I check?"
    
    menu:
        
        "Study.":
            
            "I doubt Viscella would be hiding in the home gym. I decide to search the study."
    
            scene bg study with wipeleft
            
            pc "Are you in here, Viscella?"
            
            "There's no response."
            
            show fenira happy at fenira_center with dissolve
            
            f "Any luck?"
            
            pc "Nothing."
            
            f "Hah! I got you now! What rooms have you checked?"
    
            menu:
    
                "'Theatre and rec room.'":
                    
                    $ flag_FeniraHideAndSeekLied = False
                    
                    show fenira vhappy
                    
                    f "Then she's gotta be in the gym!"
                    
                    hide fenira with dissolve
                    
                    "I check through the study."
                    
                    $ renpy.pause(2.0)
                    
                    "No sign of Viscella."
                    
                    f "Hah! Found her!"
                    
                    "...well, looks like I lost. I make my way to the gym."
                    
                    jump ch1_scene08_fenVisit_fenWins
                    
                "'Only the gym.' (Lie)":
                    
                    $ flag_FeniraHideAndSeekLied = True
                    
                    show fenira vhappy
                    
                    f "Then she's gotta be in the theatre or rec room!"
                    
                    hide fenira with dissolve
                    
                    "Looks like she fell for it."
                    
                    "I check through the study."
                    
                    $ renpy.pause(2.0)
                    
                    "No sign of Viscella."
                    
                    "Time to go check the gym."
                    
                    jump ch1_scene08_fenVisit_pcWins
            
        "Gym.":
            
            "Fenira's hot on my heels. I throw myself into the gym."
            
            jump ch1_scene08_fenVisit_pcWins
    
   
label ch1_scene08_fenVisit_fenWins:
    
    scene bg gym with dissolve
    
    show fenira neutral at fenira_center_flipped with dissolve
    
    f "You gonna come out or what?"
    
    v "Y-you want to take me to your master so she can beat me up!"
    
    show fenira angry
    
    f "Master? The only thing Nagi's a master of is bating. Come on out."
    
    v "No!"
    
    f "I'm not gonna hurt you. Just come out."
    
    v "You're not going to hurt me, but she will!"
    
    f "For crying out- it was a joke, okay?"
    
    show fenira neutral
    
    f "Oh, [pc]. She's hiding in the closet."
        
    show fenira smirk
    
    f "You should use your slime bait to coax her out."
    
    pc "Slime bait?"
    
    f "Yeah, slime bait."
    
    f "You know."
    
    show fenira teasing
    
    f "Ji-"
    
    show viscella flustered with Dissolve(0.2):
        xpos 0.8
        xanchor 0.5
        ypos 0.6
        yanchor 260
    
    show fenira shocked
    
    v "Nonononono!"
    
    v "Stop!"
    
    show fenira teasing
    
    f "Stop what? Telling [pc] how much you love-"
    
    v "Please please please stop!"
    
    v "That's a dirty stereotype!"

    show fenira happy
    
    f "It's dirty, all right."
    
    show fenira at fenira_left
    
    show viscella embarrassed at viscella_right
    
    with move
    
    f "Now are you willing to listen?"
    
    show viscella flustered
    
    v "You're blackmailing me! Of course I'm willing to listen!"
    
    show fenira confused
    
    f "Blackmailing? I was just gonna tell him some common knowledge."
    
    v "It's a stereotype! {i}A stereotype{/i}!"
    
    show fenira neutral
    
    f "Yeah, whatever. You'll have to find a way to prove me wrong."
    
    f "Anyways, that's not what I'm here to talk about. It's Nagi."
    
    show viscella scared
    
    v "H-her? Oops, look at the time! Gotta go!"
    
    show viscella at viscella_center with MoveTransition(0.2)
    
    play sound "assets/sound/sfx/body_hit.wav"
    
    show fenira confident 
    
    show viscella flustered
    
    with vpunch
    
    f "You're not going anywhere."
    
    show viscella scared
    
    f "Not until [pc] clarifies our little misunderstanding."
    
    show viscella sad at viscella_right with move
    
    menu:
        
        "'I never agreed to that.'":
            
            if flag_AcceptedFeniraChallenge:
                
                f "You didn't? You sure about that?"
                
                show fenira teasing
                
                f "Whatever happened to 'you better start rehearsing?'"
                
                show fenira wink
                
                f "Sorry, bud, but in my eyes a boast is as good as a handshake."
                
            else:
                
                f "Too late, now."
                
                show fenira wink
                
                f "Next time try opting out before I'm the clear winner."
                
            show fenira happy
                
            pc "Alright, alright, you win."
            
        "'Fine.'":
            
            show fenira vhappy
            
    f "That's the spirit."
            
    show fenira happy
    
    pc "So, basically..."
    
    pc "Fenira lied. Nagi's not angry at you." 
    
    show viscella neutral
    
    pc "In fact, if there's anyone she's angry at, it's Fenira."
    
    show fenira sad
    
    f "You didn't have to be so blunt about it."
    
    show fenira neutral
    
    jump ch1_scene08_fenVisit_end
    
label ch1_scene08_fenVisit_pcWins:
    
    scene bg gym with dissolve
    
    "The gym looks empty. Not a good sign."
    
    pc "Viscella?"
    
    "No response."
    
    pc "Damn. If Fenira finds her first..."
    
    v "I-if she finds me first what?"
    
    menu:
        
        "'It won't be pretty.'":
            
            show viscella flustered at viscella_center with dissolve
            
            v "You gotta help me, [pc]!"
            
            v "They're gonna do bad things to me!"
            
            v "Like coating my core with cement and dropping it into the ocean!"
            
            v "Or coating my core with cement and dropping it onto someone's foot!"
            
            v "Or-"
            
            pc "Calm down. They're not going to do anything like that."
            
            show viscella neutral
            
            v "They're... not?"
            
            menu:
                
                "'No. They're going to do something far worse.'":
                    
                    show viscella scared
                    
                    v "Not that! Anything but that!"
                    
                    pc "No. Even {i}worse{/i} than that."
                    
                    show viscella flustered
                    
                    v "Noooooooo!"
                    
                    "This is fun."
                    
                "'No. They just want to clear up a misunderstanding.'":
                    
                    show viscella scared
                    
                    v "That sounds just like something a hitman would say to lure his target out of a closet!"
                    
                    show viscella excited
                    
                    v "But unfortunately for you, I'll never fall for your-"
                    
                    v "..."
                    
                    show viscella scared
                    
                    v "Oh."
                    
            
        "'I'll have to do her job.'":
            
            v "Her... job?"
            
            v "You can't mean... {i}dealing with{/i} me?!"
            
            v "I won't let you! And I'll never spill the beans!"
            
            pc "Beans? What beans?"
            
            v "You know, how Kumi secretely plays mobile games!"
            
            pc "What are you talking about? Fenira just wants to help clear up a misunderstanding."
            
            v "That sounds {i}super{/i} fishy!"
            
            menu:
                
                "'If you don't come out, I'm going to start spoiling your favourite shows.'":
                    
                    show viscella flustered at viscella_center with dissolve
                    
                    v "Noooooo! Anything but that!"
                    
                    v "..."
                    
                    show viscella confused
                    
                    v "Do you even know what my favorite shows are?"
                    
                    pc "Nope."
                    
                    show viscella flustered
                    
                    v "I've been had!"
                    
                "'Trust me, Viscella. I'm from the resistance.'":
                
                    show viscella excited at viscella_center with dissolve
                    
                    v "Ohmigosh really?"
                    
                    pc "No."
                    
                    show viscella scared
                    
                    v "Oh."
                    
                    v "..."
                    
                    v "Is this the part where you coat my core in cement and-"
    
    show viscella shocked
    
    show fenira happy at fenira_left with dissolve
    
    show viscella at viscella_right with move
    
    f "Damnit. Looks like you beat me this time."
    
    show fenira wink
    
    f "Don't get used to it."

    show viscella scared
    
    v "Not like this..."
    
    show fenira confused
    
    f "What's with her?"
    
    pc "She thinks we're here to take her to Nagi."
    
    f "Really?"
    
    show viscella flustered
    
    v "You'll never take me alive!"
        
    show viscella at viscella_center with MoveTransition(0.2)
    
    play sound "assets/sound/sfx/body_hit.wav"
    
    show fenira confident with vpunch
    
    f "Oh, really?"
    
    show viscella sad at viscella_right with move
    
    show fenira happy
    
    f "Well, I've got good news for you. Nagi? She doesn't care that you broke her bottles."
    
    show viscella neutral
    
    f "If we're honest, I don't even think she likes them that much anyways."
    
    f "Probably just wants to look classy."

label ch1_scene08_fenVisit_end:
    
    v "She's... not angry at me?"
    
    pc "No."
    
    v "So... she's not going to smash my core in an industrial compactor?"
        
    show fenira confused
        
    f "Very no."
    
    show viscella happy
    
    v "Really?"
    
    f "Yes, really. What, you think she's some kind of bond villain?"
    
    show viscella neutral
    
    v "Well..."
    
    show fenira happy
    
    f "No, no, I understand. I was just surprised I wasn't the only one."
    
    f "Well, that's all we wanted to say. Feel free to leave and do whatever it is you do."
    
    f "You know, besides hiding in closets."
    
    v "Um... thanks."
    
    v "I think."
    
    hide viscella with dissolve
    
    show fenira at fenira_center_flipped with move

    f "Well, that's a load off my mind."
    
    show fenira confused
    
    f "Still can't believe she actually fell for it that hard."
    
    f "Well, least I know not to tease her in the future."
    
    show fenira wink
    
    f "...Or to tease her a lot."
    
    show fenira happy
    
    f "Anyways, thanks for the help. That was a lot of fun."
    
    f "You, uh, want me to walk you back to your room or something?"
    
    f "..."
    
    show fenira bluffing
    
    f "You know."
    
    f "In case the fleabag tries to chloroform you."
    
    menu:
        
        "Sure, if you want.":
            
            $ f_love += fenAff(2)
            
            show fenira lovestruck
            
            f "Really? C-cool."
            
            f "Uh, after you, then?"
            
            
        "My room's just a floor up, you know.":
            
            show fenira embarrassed
            
            f "Uh... I guess you're right."
            
            f "You probably don't need me escorting you up a staircase."
            
            show fenira bluffing
            
            f "But, you know, {i}my{/i} room's up there too, so you don't mind if I just, kinda... walk behind you, right?"
            
            f "Since my room's up there."
            
            f "Too."
            
    scene bg hallway with dissolve
    
    "Fenira and I return to our floor."
    
    show fenira happy at fenira_center with dissolve
    
    f "Thanks again. I was bored as hell."
    
    show fenira wink
    
    f "If you ever wanna hang out again, feel free to stop by!"
    
    show fenira neutral
    
    f "..."
    
    show fenira bluffing
    
    f "Bye!"
    
    hide fenira with dissolve
    
    "Fenira hurries back into her own room. I decide to do the same."
    
    jump ch1_scene09
            
            
label ch1_scene08_nagVisit:
    
    $ n_like += nagAff(4)
    
    $ flag_VisitedNagi = True
    
    scene bg hallway with dissolve
    
    if flag_RoomBesideKumiru:
        
        "The door across from me, which I remember to be Kamao's, is ajar. I stealthily slip past in order to avoid detection, and approach the room directly beside it."
        
    
    else:
        
        "The door to my left, which I remember to be Kamao's, is ajar. I stealthily slip past in order to avoid detection, and approach the opposite end of the hallway."
    
    "I can hear music from inside. Sounds like a guitar."
    
    "I give the door a knock."
    
    play sound "assets/sound/sfx/knock.ogg"
    
    stop music fadeout 2.0
    
    n "Hmm? It's open."
    
    "I push open the door."
    
    scene bg nBedroom
    
    play music "assets/sound/bgm/068.mp3" fadein 2.0
    
    show nagi neutral at nagi_center
    
    with dissolve
    
    "Nagi is seated on the side of her bed, strumming idly on a guitar. She gives me a smile."
    
    show nagi happy
    
    n "Oh, [pc]. Long time no see."
    
    menu:
        
        "'You play the guitar?'":
            
            n "Sure do."
            
            n "I was in a band and everything. Fenira did vocals, believe it or not. She could do some crazy things with her voice."
            
            show nagi neutral
            
            n "She could also do some crazy things to a stage."
            
            n "Probably why the school shut us down."
            
            n "Sorry, you probably didn't stop by for a history lesson. What's up?"
            
        "'What happened to sleeping'?":
            
            show nagi neutral
            
            n "Sorry."
            
            n "I mean, I wasn't lying. I {i}am{/i} completely wiped, but the moment my head hit the pillow I realized I wasn't gonna get any sleep. Must be all the excitement from moving to a new place."

            show nagi wink

            n "And even if it was a lame excuse to get rid of you, which it wasn't... clearly it didn't work."
            
            show nagi neutral
            
            n "Anyways, what's up?"

    pc "Nothing, which is the problem. I don't have anything to unpack, so..."
    
    show nagi confused
    
    n "Really? You just showed up with the clothes on your back?"
    
    pc "That's one way to put it, yeah."
    
    show nagi neutral
    
    n "I don't know how you do it. I bring a ton of stuff."
    
    pc "Really? I don't see a lot of boxes."
    
    show nagi happy
    
    n "Trust me, you will."
    
    stop music
    
    play sound "assets/sound/sfx/door_open.wav"
     
    $ kaFlip()
     
    show kamao wink:
        xpos 0.1
        xanchor 0.5
        ypos 0.55
        yanchor 340
        zoom 1.0
        xzoom -1.0
        
    with dissolve
    
    play music "assets/sound/bgm/scene_comi1.ogg"
    
    show nagi bored
    
    ka "Knock knock!"
    
    n "Normally, you knock and {i}then{/i} enter."
    
    show kamao confused
    
    ka "Really?"
    
    ka "Then how are you supposed to walk in on someone doing something dirty?"
    
    n "I think that's the point. Can I help you?"
    
    show kamao neutral
    
    ka "Yeah, I'm looking for-"
    
    show kamao shocked
    
    ka "..."
    
    show kamao vhappy at kamao_left with MoveTransition(0.2)
    
    ka "[pc]!"

    show nagi at nagi_right with MoveTransition(0.8)
    
    n "Let's try again."
    
    n "Can we help you?"
    
    ka "I've been looking for you since thirty-two seconds ago!"
    
    show kamao neutral
    
    ka "Anyways, let's go."
    
    n "We were having a discussion."
    
    ka "About what?"
    
    show nagi confident
    
    n "Our good chemistry, of course."
    
    ka "..."
    
    show kamao shocked
    
    ka "Eh?"
    
    show kamao unhappy
    
    ka "I mean, pfft. Nice try, snake lady, but I used that trick like two hours ago."
    
    ka "Right, [pc]?"
    
    menu:
        
        "'Sorry, Nagi, she beat you to it.'":
            
            show kamao vhappy
            
            show nagi neutral
            
            ka "Heeheehee!"
            
            show nagi confused
            
            n "Did you just {i}say{/i} 'heeheehee'?"
            
            show kamao confident
            
            ka "Who knows? Fufufu."
            
            show nagi bored
            
            n "Oh my god."
            
            n "You're like a walking, talking aneurysm."
            
            show kamao unhappy
            
            ka "At least this walking, talking aneurysm has a boyfriend!"
            
            n "The poor man."
            
            ka "[pc]'s not poor. He's just financially disadvantaged."
            
            show nagi bored
            
        "'So, Nagi, eight o'clock tomorrow night?'":
            
            show nagi wink
            
            n "Perfect. I can't wait."
            
            show kamao confused
            
            ka "Can't wait for what?"
    
            show nagi bored
            
            n "Our date. Are you even listening?"
            
            show kamao embarrassed_open
            
            ka "Wha? B-But that was just bullshit you came up with to get rid of me!"
            
            show kamao confused behind nagi
            
            n "Right." 

            show nagi confident

            n "Anyways, [pc], what do you think about crashing at my place afterwards? It's not far, and it'll afford us a bit more privacy."
            
            show kamao embarrassed behind nagi
            
            ka "Hmph! If you guys wanna bone so badly, prove it! Start snogging right now! I dare you! I double dare you!"
            
            n "And here I thought you'd never ask."
            
            $ n_love += nagAff(1)
            
            show nagi neutral with dissolve:
                xpos 0.2
                xanchor 525
                zoom 1.5
                
            show kamao flustered
            
            ka "Whoa whoa whoa, whaddya think you're doing?!"
            
            show nagi wink
            
            n "I thought you wanted snogging?"
            
            show kamao bluffing
            
            ka "I lied! I am a liar and a scoundrel! Now move {i}away{/i} from my boyfriend!"
            
            show kamao unhappy
            
            show nagi confused at nagi_right with dissolve
            
            n "Your... boyfriend?"
    
            ka "You know it. Which means I get exclusive snogging privileges. So, y'know, back off."
    
            n "..."
    
    menu:
        
        "'She's a bit delusional.'":
            
            n "A bit?"
            
            pc "A lot."
            
            ka "A {i}not{/i}."
            
            show kamao wink
            
            ka "Besides, if I'm crazy, I don't wanna be sane."
            
        "'She's been doing this since the moment we met.'":
            
            show kamao neutral
            
            ka "And what a moment it was."
            
            show kamao sleepy
            
            ka "Aah, I remember it like it was two hours ago..."
            
    n "Right."
            
    show nagi neutral
            
    n "Hey, if you need any help filing a restraining order, I know a girl."
            
    show kamao unhappy
            
    ka "What's up with you people and your restraining orders? You can't contain me. I'm a force of nature."
    
    show kamao shocked with vpunch
    
    ka "Hrk!"
    
    show nagi confident
    
    n "Can't contain you, huh?"
    
    "You glance down at Kamao's feet. Nagi's tail is squeezing around her calves and ankles."
    
    show kamao shockblush
    
    ka "I've seen enough hentai to know where this is going."
    
    n "And I'm sure you've watched enough {i}weird{/i} hentai to know what happens when a lamia catches a nice, juicy kitsune?"
    
    ka "Uh... chokeplay?"
    
    n "After that."
    
    ka "..."
    
    show kamao shocked
    
    ka "Alright."
    
    ka "I've made some mistakes."
    
    ka "Nobody's perfect."

    ka "Please don't eat me."
    
    show kamao with MoveTransition(0.2):
        xpos 0.3
        xanchor 0.5
        ypos 0.85
        yanchor 340
        zoom 1.0
        xzoom -1.0
        
    play sound "assets/sound/sfx/body_hit.wav"
    
    show kamao pained with vpunch
        
    ka "Gah!"
    
    show kamao unhappy at kamao_left with MoveTransition(0.8)
    
    ka "Jeeze. At least I haven't physically assaulted anyone."
    
    pc "Didn't you tackle me?"
    
    ka "Hey, that was a hug."
    
    show nagi confused
    
    ka "A high-velocity, full-contact rugby hug."
    
    show nagi bored
    
    n "Ugh. Can you just leave? Please? I'll give you a dollar."
    
    show kamao confident
    
    ka "Hah! I can't be bought!"
    
    n "Two dollars."
    
    show kamao happy
    
    ka "Deal."
    
    hide kamao with dissolve
    
    $ kaUnFlip()
    
    stop music fadeout 2.0
    
    show nagi neutral at nagi_center with move

    n "Well, then."
    
    n "She's..."
    
    play music "assets/sound/bgm/068.mp3" fadein 2.0
    
    
    menu:
        
        "'Something.'":
            
            n "Yeah. A whole lot of something."
            
            show nagi bored
            
            n "Maybe a little too much something for her own good."
            
            show nagi neutral
            
            n "It's a small miracle she managed to pass the screening process."
            
            pc "Screening process?"
            
            n "Yeah, you know. The one where they check the candidates to make sure none of them are a 'risk'."
            
            pc "A risk? To what?"
            
            n "You, usually."
            
        "'A major pain in the ass.'":
            
            n "Yeah, I definitely don't envy you right now."
            
            n "At least she knows how to take a joke. Maybe she'll be fun."
            
            show nagi happy
            
            n "Not as fun as Fenira, of course."
            
            pc "You sure like teasing her, don't you?"
            
            n "It's not a hobby. It's a lifestyle."
        
        "'Absolutely adorable.'":
            
            show nagi happy
            
            n "Hah!"
            
            n "..."
            
            show nagi confused
            
            n "Wait. Are you serious?"
            
            menu:
                
                "'Dead serious.'":
                    
                    n "I mean, whatever floats your boat."
                    
                    n "I wouldn't tell her that, though. If you think she won't leave you alone now..."
                    
                "'Pfft.'":
                    
                    show nagi happy
                    
                    n "You had me worried for a second."
            
    
    show nagi neutral
    
    n "Anyways, what were we talking about?"
    
    n "Oh, right. Boxes."
    
    show nagi bored
    
    n "Wow. See what happens when I haven't unpacked any of my conversation starters? It's not pretty."

    n "At least the kitsune gave us something to talk about."
    
    n "Where are you from, anyways?"
    
    pc "Uh..."
    
    menu:
        
        "'I can't remember.'":
            
            show nagi

        "'You know. Around.'":
    
            n "Around, huh? You born here in Skellow?"
            
            menu:
                
                "'Yeah.'":
                    
                    n "Really? That's funny." 
                    
                    show nagi wink
                    
                    n "Especially since Skellow's a name I just made up."
                    
                    n "But hey, if you don't wanna tell me where you're from, I won't force you."
                    
                    pc "It's not that, it's just... I can't remember."
                    
                "'Uh, no...'":
                    
                    n "Then where were you born?"
                    
                    pc "I, uh... I can't remember."
       
    show nagi confused
       
    n "You... can't remember?"
            
    "You shake your head."
    
    n "How do you not know where you're from?"
    
    pc "I've forgotten a lot more than just where I'm from..."
    
    n "You're telling me you have amnesia?"
    
    pc "Well... yeah."
    
    n "Oh."
    
    show nagi neutral
    
    n "That's fine, then."
    
    pc "Huh?"
    
    n "Well, no helping amnesia, right?"
    
    pc "You don't think I'm crazy?"
    
    n "Why would I think you're crazy? There are at least four different kinds of chimera that can screw with your memories. And they're all pretty easy to piss off."
    
    show nagi bored
    
    n "Trust me. I know."
    
    show nagi neutral
    
    n "So, how far back can you remember?"
    
    pc "Uh... three hours?"
    
    show nagi surprised
    
    n "Wow, really?"
    
    pc "Really. I'm still wrapping my head around monster people."
    
    n "Monster people?"
    
    pc "Uh, chimera."
    
    show nagi confused
    
    n "Wait, you've forgotten about chimera?"
    
    pc "I think I had this same conversation with Kumiru and Viscella."
    
    show nagi neutral
    
    n "Sorry. It's just surprising. What kind of people are you used to?"
    
    pc "You know... people people. Two legs, two arms, no tail, made of flesh, that kind of thing."
    
    show nagi confused
    
    n "So you know about humans, but not chimera?"
    
    pc "I guess, yeah."
    
    show nagi neutral
    
    n "Sounds fun."
    
    pc "Really?"
    
    show nagi wink
    
    n "Totally. You're like the protagonist from an action movie. You can't tell me that's not cool."

    pc "There hasn't been much action so far..."
        
    show nagi neutral
        
    n "Well, I'm sure you'll run into some eventually."
    
    "Nagi yawns, stretching her arms over her head."
    
    n "I'm kinda jealous, honest."
    
    pc "Really? Why?"
    
    n "Well, you know. Sometimes I think maybe a clean slate would be nice."
    
    pc "You'd forget all your friends and family..."
    
    n "Fair enough, I suppose. But still. Right now, you're freer than most of us will ever be. Might as well squeeze a little joy out of it, right?"
    
    n "But hey, enough of that. Now I really {i}am{/i} exhausted. I'm gonna get some sleep. Wanna join me?"
    
    menu:
        
        "'Who wouldn't?'":
            
            $ n_love += nagAff(1)
            
            show nagi bored
            
            n "More than I'd care to count, I'm afraid."
            
            pc "Yeah, right."
            
            n "I'm as stunned as you are."
            
            show nagi wink
            
            n "I mean, just {i}look{/i} at these puppies."
            
            show nagi confident
            
            n "No touching, though."
            
            show nagi teasing
            
            n "You want that, you'll need to keep me company more often."
            
            show nagi confident
            
            
        "'Wh- ah, well, I, um-'":
            
            $ n_love += nagAff(1)
            
            show nagi sad
            
            n "Is that a no? Aw." 
            
            show nagi wink
            
            n "Maybe next time, hm?"
            
            show nagi confident
            
        "'I, uh, think I hear my laundry calling!'":
            
            n "Really? Better hurry before the kitsune nabs your underwear."
            
            n "But don't be a stranger, alright? I don't do much but pester Fenira and watch movies, so I've got a lot of free time."
            
            n "Which means I'll talk to you soon, right? Right."
            
            show nagi happy
    
    n "Anyways, I'll stop stalling. Sleep tight, [pc]. Later."
    
    "I say goodbye to Nagi, and head back to my own room."
    
    jump ch1_scene09
        
label ch1_scene08_kamVisit:
    
    $ ka_like += kamAff(4)
    
    $ flag_VisitedKamao = True
    
    stop music fadeout 3.0
    
    scene bg hallway with dissolve
    
    if flag_RoomBesideKumiru:
        
        "The door across from me, which I remember to be Kamao's, is ajar. I approach, and peek my head in."
        
    
    else:
        
        "The door to my left, which I remember to be Kamao's, is ajar. I approach, and peek my head in."
        
    scene bg kaBedroom with dissolve
        
    ka "Fufufu. Fu-fu-fu. Fu! Fu! Fu!"
        
    "Well, there she is. She's holding up a mirror, and appears to be laughing at herself."
     
    play music "assets/sound/bgm/070.mp3" fadein 3.0
    
    ka "Fu... fu... fu..."
                 
    menu:
        
        "'What are you doing?'":
            
            "She jumps, nearly dropping the mirror in the process."
            
            show kamao shocked_open at kamao_center
            
            ka "Gyah!"
            
            ka "[pc]?!"
            
            ka "What are you doing there!"
            
            show kamao shocked
            
            ka "I- I mean..."
            
            show kamao neutral
            
            ka "Hey. handsome."
            
            ka "Was your mom a goddess?"
            
            show kamao wink
            
            ka "Cuz I think she spilled some stars in your eyes. Fupupu."
            
            show kamao confused
            
            ka "I mean, fufufu."
            
            ka "..."
            
            show kamao bluffing
            
            ka "Do over?"
            
            pc "I don't think a do over will help."

            show kamao embarrassed
            
            ka "Really? Even if I do it..."
            
            show kamao teasing
            
            ka "Naked?"
            
            pc "Especially if you do it naked."
            
            show kamao sad
            
            ka "Aw."
            
        "Just... watch.":
            
            "You watch the kitsune intently. She continues to laugh at herself in the mirror."
            
            ka "Fufufu!"
            
            "Suddenly, she pumps her fist."
            
            show kamao confident at kamao_center
            
            ka "Nice, Kamao. Nice. It's all in the laugh."
            
            show kamao neutral
            
            ka "Alright, let's try that one more time."
    
            ka "Ahem."
            
            ka "Hey. handsome."
            
            ka "Was your mom a goddess?"
            
            show kamao wink
            
            ka "Cuz I think she spilled some stars in your eyes. Fufufu."
            
            show kamao bored
            
            ka "Eh. The laugh's gotta go."
            
            pc "Definitely."
            
            show kamao shocked_open
            
            "She jumps, nearly dropping the mirror in the process."
            
            ka "Gyah!"
            
            ka "[pc]?!"
            
            show kamao shocked
            
            ka "How much did you hear?!"
            
            pc "All of it."
            
            show kamao flustered
            
            ka "No way! Including my soliloquy on the futility of our collective struggle against the shackles of mortality?!"
    
            pc "Er, no."
            
            show kamao lovestruck
            
            ka "Whew."
    
    ka "..."
    
    pc "..."
    
    show kamao embarrassed
    
    ka "So."
    
    ka "Uh."
    
    ka "Heyy. Yy. Yyyyy."
    
    ka "..."
    
    ka "Heyyyyyyyy."
    
    pc "What are you doing?"
    
    show kamao bluffing
    
    ka "I have absolutely no idea!"
    
    ka "C-come in, come in!"
    
    "Kamao ushers me into her bedroom, kicking various articles of clothing under her bed as she does so."
    
    pc "How'd you manage to get your room so messy? Didn't you just move in a couple hours ago?"
    
    show kamao wink
    
    ka "I'm a Fawkes."
    
    pc "Yeah, I know."
    
    show kamao unhappy
    
    ka "No, like, a Fawkes."
    
    pc "What?"
    
    ka "F-A-W-K-E-S. It's my last name."
    
    pc "Oh. What does that have to do with anything?"
    
    show kamao vhappy
    
    ka "Us Fawkeses are renowned for our ability to make a mess out of absolutely anything!"
    
    pc "You sound proud."
    
    show kamao happy
    
    ka "Because I'm proud! It's like... a family tradition!"
    
    ka "One time, at band camp, I literally broke {i}all the flutes{/i}. On accident, of course. Mostly."
    
    pc "All of them?"
    
    show kamao sleepy
    
    ka "Yeah. All of them."
    
    show kamao vhappy
    
    ka "When the flute players were done with me, I had to breathe through a straw!"
    
    show kamao confused
    
    ka "Actually, that would've made my throat a bit like a flute, wouldn't it?"
    
    show kamao unhappy
    
    ka "Damn. That's poetry, right there."
    
    ka "Anyways, enough about me! Tell me about you!"
    
    show kamao embarrassed
    
    ka "Actually, for now, just tell me why you're in my bedroom."
    
    menu:
        
        "Ask about her offer":
            
            ka "My offer... offer..."
            
            ka "..."
            
            show kamao confused
            
            ka "What offer?"
            
            pc "You don't remember?"
            
            #FLASHBACK#
            
            scene bg pBedroom 
            
            show kamao winkblush at kamao_right
            
            show kumiru unamused at kumiru_left
            
            show viscella neutral:
                xpos 0.12
                xanchor 0.5
                ypos 0.6
                yanchor 260
                xzoom -1.0
            
            with flash
            
            
            ka "Stop by later. I'll give you a prize~"
            
            #END FLASHBACK#
            
            scene bg kaBedroom
            
            show kamao confused at kamao_center
            
            with flash
            
            ka "..."
            
            show kamao shocked
            
            ka "..."
            
            show kamao shockblush
            
            ka "Oh. Your {i}prize{/i}. Right."
            
            ka "Alright. It's my first time. Be gentle."
            
            menu:
                
                "'I take it back.'":
                    
                    ka "What? You dangle it in front of me like that and just tear it away?!"
                    
                    show kamao unhappy
                    
                    ka "That's cold. Ice cold."
                    
                    ka "It's also kinda hot."
                    
                "'Let's do this thing.'":
                    
                    ka "Okay."
                    
                    "Kamao nervously pulls her tails onto her lap, though only one is long enough to reach."
                    
                    ka "You can pet it."
                    
                    pc "Pet it...?"
                    
                    show kamao flustered
                    
                    ka "Th-three pets! Max! I'm not ready for any more than that!"
                    
                    show kamao lovestruck
                    
                    menu:
                        
                        "'On second thought, this is kind of weird...'":
                            
                            show kamao shockblush
                            
                            ka "Did I say three pets? I meant six."
                            
                            ka "No? Twelve?"
                            
                            ka "I'm willing to negotiate."
                            
                            pc "Sorry, the offer's off."
                            
                            show kamao pained
                            
                            ka "Noooooooo!"
                            
                            ka "My hesitation was my downfall!"
                            
                            show kamao neutral
                            
                            ka "Eh, oh well. I won't let you off easy next time you blueball me."
                            
                        "Touch fluffy tail.":
                            
                            show kamao shockblush
                            
                            $ ka_love += kamAff(2)
                            
                            "You pet Kamao's tail."
                            
                            "It's soft."
                            
                            "Very soft."
                            
                            "{i}Too soft.{/i}"

                            "You spend approximately three minutes petting her tail."
                            
                            "It's so soft. Oh my god."
                            
                            "You manage to pry your hand away."
                            
                            ka "..."
                            
                            show kamao bluffing
                            
                            ka "I- I see you're t-totally entranced by kitsune f-fluff mag... magic!"
                            
                            ka "D-D-Don't worry, happens t-t-to me all the t-time! Aha!"
            
                            pc "Are you okay?"
                            
                            ka "Are you okay? Am I okay? I'm okay! Okay?"
                            
                            show kamao shockblush
                            
                            ka "..."
                        
                            ka "I'm gonna go take a shower."
                            
                            hide kamao with dissolve
                            
                            play sound "assets/sound/sfx/footstep_rush.wav"
                            
                            "Kamao hurries out of the room without a second glance, nearly tripping on her way out the doorway."

                            "You can hear her bounding down the hallway, followed moments later by a slamming door and the sound of running water."
            
                            "Well, looks like your job here is done."
                            
                            "You decide to head back to your room."
                            
                            jump ch1_scene09
            
        "'Just thought I'd say hello.'":
            
            ka "Really?!"
            
            ka "You're not gonna take advantage of a poor, helpless kitsune?"
            
            ka "Who, may I mention, would be totally powerless to resist even the most pathetic of sexual advances?"
            
            pc "Uh, no."
            
            show kamao unhappy
            
            ka "Damn."
            
            show kamao shocked
            
            ka "I mean, thank the heavens!"
            
    show kamao neutral
            
    ka "So... what're you buying? Premium Kamao hang-out time?"
    
    pc "I guess. How much is it gonna cost me?"
    
    ka "Five K-bux."
    
    ka "Before you ask, you can earn 100 K-bux by whispering dirty stuff into my ear."
    
    menu:
        
        "Whisper something dirty into her ear.":
            
            show kamao shockblush
            
            "You lean in close. Kamao freezes, her breath caught in her throat, as you whisper something into her ear."
            
            pc "Omlette du fromage."
            
            ka "..."                              
            
            show kamao happy
            
            ka "Hah! I get that reference!"
            
            show kamao vhappy
            
            ka "K-bux get!"
                                           
        "'How many do I get for doing dirty stuff to you?'":
            
            $ ka_love += kamAff(1)
            
            show kamao embarrassed
            
            ka "Yes."
            
            ka "The answer to your question is 'yes.'"
            
            ka "And just for suggesting it I'll give you a hundred."
            
        "'I'm leaving.'":
        
            show kamao bluffing
        
            ka "B-but it's your lucky day! K-bux sweepstakes! As our only contestant, you win the grand prize of infinity K-bux!"
                       
            pc "Oh, boy. It's my lucky day."
            
            show kamao winkblush
            
            ka "You betcha!"
                       
    show kamao neutral
                       
    ka "So, now that business is taken care of- how can can Kamao be of service?"
    
    show kamao winkblush
    
    ka "And I do mean {i}service{/i}."
    
    menu:
        
        "'You seem a little... desperate.'":
            
            show kamao confused
            
            ka "A little?"
            
            show kamao unhappy
            
            ka "Listen here, good-looking. I am the {i}personification{/i} of unquenchable thirst."
            
            ka "I've got this friend, right? She's got herself a boytoy, and she'll still complain when she's had a week long dry spell."
            
            show kamao vhappy
            
            ka "Hah-hah, right? She hasn't been laid in days! Funny!" 
            
            show kamao vangry
            
            ka "Lady, I'm in the middle of an eighteen-year long dry spell. You don't understand the {i}meaning{/i} of suffering."
                  
            pc "You're eighteen?"
        
            show kamao neutral
            
            ka "Sure am."
            
            show kamao wink

            ka "Barely legal."
                  
            menu:
                
                "'What's the rush?'":
                    
                    show kamao confused
                    
                    ka "Huh? Whaddya mean?"
                    
                    pc "You're eighteen. You've got plenty of time. No need to rush into that kinda thing, you know?"
                    
                    ka "You kidding? I don't wanna get laid because of societal pressures or anything."
                    
                    show kamao horny
                    
                    ka "I just want a big, fat-"
                    
                    pc "Alright, I get it."
                    
                "'Well. Good luck.":
                    
                    show kamao bored
                    
                    ka "I want sex, not sympathy."
                    
                    show kamao shocked
                    
                    ka "Wait, what if you combined the two? Sympathy sex?"
                    
                    show kamao vhappy
                    
                    ka "Brilliant!"
                    
                    show kamao wink
                    
                    ka "Am I a genius or what?"
                    
                    pc "I'm pretty sure that's a thing already."
                    
                    show kamao bored
                    
                    ka "Oh. Bummer. There go my chances at a Nobel prize."
                  
        "'I'm not sure I follow.'":
            
            show kamao embarrassed
            
            ka "You know."
            
            ka "Service."
            
            show kamao horny
            
            ka "Like, I'll get on my knees and-"
            
            pc "I think I can infer the rest."
            
            ka "Oh man, did you actually picture it?"
            
            pc "Why do you ask?"
            
            ka "Because giving a guy a boner would probably be the greatest thing to ever happen to me."
            
            pc "That's... kinda sad, actually."
            
            show kamao bored
            
            ka "Tell me about it."
            
    show kamao bored
            
    ka "That's basically all there is to my character, by the way."
    
    ka "Dick lust is, like, my defining feature."
    
    ka "That and fox puns."
    
    show kamao neutral

    ka "For example..."

    show kamao confused

    ka "..."
    
    ka "..."
    
    ka "..."
    
    show kamao bored
    
    ka "Okay, maybe just the dick lust."
    
    menu:
        
        "I find that hard to believe.":
            
            $ ka_love += kamAff(2)
            
            show kamao bored
            
            ka "No, it's true."
            
            ka "I tried having a well-rounded personality once."
            
            ka "Still didn't get me laid."
            
            show kamao neutral
            
            ka "But, I mean, I'm glad you have faith in me."
            
            ka "This is probably the longest I've talked to a guy without getting a call from his lawyer."
            
            pc "I don't have a lawyer."
            
            show kamao bored
            
            ka "Oh. That explains it."
            
            show kamao unhappy
            
            ka "Jeeze, why'd you have to go ruin a perfectly good moment?"

            ka "That's {i}my{/i} job."
            
        "Well, at least you're honest.":
            
            ka "Am I, though?"
            
            show kamao shocked
            
            ka "Maybe I'm saying all this to hide a my innermost thoughts and beliefs. Maybe I'm trying to scare you off because I fear companionship. Maybe beneath this supple flesh lies a broken girl, scabbing over her wounds with layer upon layer of dick jokes."
            
            show kamao neutral
            
            ka "Or maybe I'm not. Who knows?"
            
            show kamao wink
            
            ka "I sure don't."
            
    show kamao shocked        
    
    $ renpy.music.set_volume(1, delay=0, channel='sound')
    
    play sound "assets/sound/sfx/vibrate.mp3" loop
    
    $ renpy.pause(1.0)
    
    ka "Oop, there goes my vi- I mean my phone."
    
    ka "Hold on a sec."
    
    stop sound
    
    show kamao confused
    
    ka "Hello?"
    
    ka "..."
    
    show kamao vhappy
    
    ka "Daddy!"
    
    ka "Sorry, I've been so busy that I forgot!"
    
    ka "Mmhm!"
    
    show kamao happy
    
    ka "Oh my god, Dad, it's so cool. They've got their own movie theatre. I'm not kidding."
    
    ka "Well, obviously not {i}that{/i} big, but pretty big."
    
    show kamao bored
    
    ka "Hmmm? Well, I don't wanna talk to her."
    
    ka "I don't care, Dad. I don't wanna talk to her."
    
    ka "What? No, I don't wanna-"
    
    show kamao unhappy
    
    ka "Start what? I'm not starting anything. I'm just telling you what I've been telling you for the last six months, but you haven't been-"
    
    show kamao shocked_open
    
    ka "Oh my god. Did I just hear what I think I heard? Did she just call you Daddy? She did, didn't she?"
    
    show kamao shocked
    
    ka "I'm actually gonna barf. Here come the cheerios."
    
    show kamao unhappy
    
    ka "What? Why you gotta bring up old stuff? She started it!"
    
    show kamao angry
    
    ka "Okay, that was an accident! I thought it was just normal glue! Besides, I paid her hospital bill, didn't I?"
    
    "Kamao seems to have completely forgotten about me."
    
    "I decide to slip away before I get roped into an argument."
            
    jump ch1_scene09
            
label ch1_scene09:
    
    stop music fadeout 2.0
    
    scene bg pBedroom_n with Dissolve(2.0)

    "I'm back in my room."
    
    "It's only six, but I feel exhausted. Probably because of the whole amnesia business."
    
    "I sprawl out on my bed, the day's events whirling through my mind."
    
    "I barely even notice myself falling asleep..."
    
    show black with Dissolve(5.0)
    
    play music "assets/sound/bgm/tam-n17.mp3" fadein 3.0
    
    $ renpy.pause (2.0)
    
    "...and it curved straight into the net!" 
    
    scene bg nBedroom_n
    
    show nagi happy at nagi_right
    
    show fenira vhappy at fenira_left
    
    with Dissolve(3.0)
    
    f "I was just trying to pass to our striker, but nope! Took her job, and she couldn't have been happier!"
    
    n "A shame you still lost 7-1."
    
    show fenira happy
    
    f "Hey, we may have lost, but at least I saved our pride."
    
    n "Only to have it torn away from you the following week."
    
    show fenira neutral
    
    f "It was a tough year, okay? Plus we had a bunch of newbies, and I was focusing on schoolwork."
    
    n "For once in your life."
    
    show fenira teasing
    
    f "Yeah, and while I was doing that, you were focusing on me. Which was a better use of time, I wonder?"
    
    show fenira smirk   
    
    show nagi flustered
    
    n "Low blow."

    show fenira happy

    f "Hey, give and take. Anyways, I should get to bed. It's nine already."
    
    #$ flag_VisitedFenira = True
    
    if flag_VisitedFenira == True:
        
        show nagi neutral
        
        n "Hey, hey. You're not going anywhere until you tell me what you and [pc] were up to earlier."
        
        show fenira confused
        
        f "How'd you find out about that?"
        
        n "The slime came up to me earlier and apologized. She looked a little terrified."
        
        show fenira neutral
        
        f "Oh. Yeah, we just threw together a little search party, that's all."
        
        n "How'd it go?"
        
        f "Oh, it was fine. We found her hiding in a-"
        
        n "I'm not talking about the search."
        
        show fenira sad

        f "..."
        
        show fenira embarrassed
        
        f "Look, I can handle myself, okay?"
        
        n "I'm just asking."
        
        f "And I'm just telling. I just met the guy. I'm not that desperate."
        
        n "News to me."
        
        show fenira angry
        
        f "Oh, fuck off, Nagi. If I want help I'll ask for it, okay?"
        
        show nagi confused
        
        n "Right. Because that worked {i}so well{/i} last time."

        show fenira vangry

        f "Sorry? Could you repeat that?"
        
        show nagi bored
        
        n "Alright, alright. I'll just cheer for you from the sidelines."
        
        show fenira angry
        
        f "I'm telling you, I just met him!"
        
        show nagi confident
        
        n "He's cute, huh?"
        
        f "I'm leaving."
        
    show nagi neutral
        
    n "If you say so. Night-night, Fen-Fen."
    
    f "Yeah, yeah."
    
    show fenira with MoveTransition(0.5):
        xalign 1.5
        xzoom 1.0
    
    play sound "assets/sound/sfx/body_hit.wav"
    
    stop music
    
    show nagi confused with vpunch

    show fenira shocked with MoveTransition(0.1):
        xalign 1.4
        
    f "Ack, who the-"
    
    f "..."
    
    show fenira smirk
    
    f "Pfft. Have fun, Nagi."
    
    show fenira with MoveTransition(1.5):
        xalign 3.0
        
    $ renpy.pause(1.0)
    
    $ kaFlip()
    
    show kamao neutral at kamao_left
    
    show kamao:
        xalign -3.0
        
    show kamao with MoveTransition(0.2):
        xalign -2.0
        
    play music "assets/sound/bgm/scene_comi1.ogg"
        
    ka "Hey."
    
    show nagi bored
    
    n "Oh, no."
    
    show kamao wink
    
    ka "Oh, yes."
    
    show kamao neutral at kamao_left with MoveTransition(0.3)
    
    ka "You know why I'm here."
    
    n "To annoy me. Again."
    
    show kamao vhappy
    
    ka "Yes!"
    
    show kamao unhappy
    
    ka "And no."
    
    ka "I'm here to talk to you about... {i}him{/i}."
    
    n "I'm afraid I don't know any 'Him.' You can go now."
    
    ka "You know."
    
    ka "{i}[pc]{/i}."
    
    n "Whatever you're going to ask, the answer is no."

    show kamao confident
    
    ka "Concerned? You are right to fear me, tits-for-brains."
    
    n "I've heard kitsune tastes like fried tofu. Any truth to that?"
    
    show kamao shocked
    
    ka "Alright, let's start over."

    n "Let's."
    
    show kamao neutral
    
    ka "So, basically, I demand exclusive [pc] rights."
    
    n "..."
    
    ka "..."
    
    show nagi confused
    
    n "And?"
    
    show kamao confused
    
    ka "And what?"
    
    show nagi neutral
    
    n "And in exchange for these exclusive rights? What's in it for me?"
    
    show kamao shocked
    
    ka "Whoah, you're actually considering it?"
    
    n "No. But I figured I'd hear your reasoning before I shoot you down."

    show kamao unhappy
    
    ka "Uncool!"
    
    if flag_VisitedKamao == True:
    
        ka "He came to visit me, you know! We're basically dating!"
    
        show nagi confused
    
        n "Kidnapping doesn't count."
        
        show kamao confident
        
        ka "Hah! I didn't have to! He came to see me all on his own!"

        n "Right."
        
        show kamao confused
        
        ka "You... don't believe me?"
        
        show nagi bored
        
        n "Of course not."
        
        show kamao unhappy
        
        ka "Well, I'm not gonna waste my breath trying to convince you of this {i}100\% real thing that actually happened{/i}."

        ka "Even though it's true."
        
    n "Whatever. You still haven't answered my question."
    
    ka "What question?"
    
    n "What's in it for me?"
    
    n "You know, besides the loss of all my pride and dignity."
    
    show kamao confused
    
    ka "Hmm..."
    
    show kamao neutral
    
    ka "I won't annoy you anymore."
    
    show nagi bored
    
    n "I find that hard to believe."
    
    ka "Okay, then how about this?"
    
    ka "You give me exclusive [pc] privileges, and I don't wake you up every morning by bellyflopping onto your bed."
    
    n "You think threats are gonna work? We've already established that I'm higher on the food chain."
    
    show kamao confident
    
    ka "Not so fast! I did some internet searching, and found to my amazement that eating people is illegal."
    
    n "Is reporting you to the supervisor also illegal?"
        
    show kamao shocked
        
    ka "Uh... yes?"
    
    n "Wrong. Do not pass go. Do not collect $200."
        
    show kamao angry
        
    ka "Okay, fine. I don't need any stupid exclusivity anyways. I'll beat you the good old fashioned way."
    
    show nagi confused
    
    n "Since when have I been competing with {i}you{/i}?"
    
    show kamao unhappy
    
    ka "Don't try to play wise. You're the only person standing in my way."
    
    show nagi bored
    
    n "What?"
    
    show kamao neutral
    
    ka "The spider's a nerd, the slime's a bigger nerd, and the bird's not a problem."
    
    n "Why not?"
    
    ka "Cuz I don't think [pc]'s gay."
    
    show nagi neutral
    
    n "I wish she was here to have heard that. I really do."
    
    show kamao unhappy
    
    ka "Anyways, through this process of elimination I realized you were the only person here with the potential to tear [pc] away from my tender, loving grasp."
    
    show nagi bored
    
    n "So you decided to barge into my room and deliver this pathetic excuse of an ultimatum?"

    ka "Yes."
    
    n "..."
 
    if flag_VisitedNagi == True:
        
        n "Okay. Let's say for a moment that I {i}am{/i} competing with you."
        
        n "If that's the case, you've already lost."
        
        ka "Huh?"
        
        n "Playing dumb? Remind me who [pc] decided to visit in his free time? It was one of us, I recall. And by that I mean it was me."
        
        show kamao confident
        
        ka "He probably just wanted advice on how to approach someone as drop-dead gorgeous as me!"

        n "If that was the case, it meant he trusted me more than anyone in this house. Probably more than anyone he knows, considering the whole 'amnesia' thing."
        
        show kamao confused

        show nagi neutral

        n "And trust makes people pliant. Maybe I could suggest he practice asking me on a date? Calm his nerves before asking you, of course."
        
        show kamao shockblush
        
        n "Then maybe he's nervous about kissing you, so I give him some practice with that, too?"
        
        show kamao embarrassed
        
        show nagi teasing
        
        n "And then when the stakes get higher, I give him some hands-on learning. I can go into detail, if you want."

        show nagi confident     

        ka "..."
        
        show kamao confused
        
        ka "So you'll let me have him?"

    else:
        
        show nagi bored
        
        n "And what makes you think I'm interested in [pc]?"
        
        ka "Huh? You're a chimera. He's a guy."
        
        ka "What more proof do I need?"
        
        n "Maybe I'm a lesbian."
        
        show kamao shocked
        
        ka "A- are you?"
        
        show nagi neutral
        
        n "No."
        
        show kamao unhappy
        
        ka "My point exactly!"
        
        n "You sound pretty desperate, you know. That's generally a turn-off."
        
        ka "I'm not desperate! I'm just... I'm just..."
        
        ka "..."
        
        show kamao confused
        
        ka "What's another word for 'desperate?'"
        
        show nagi bored
        
        n "Do I look like a thesaurus?"
        
        ka "Yeah, actually. You're green, and my last thesaurus was green. No way that's a coincidence."
        
        show nagi confused
        
        n "Uh... huh."
        
        ka "Anyways, you gonna let me have him or not?"
        
        
    show nagi neutral
        
    n "Absolutely..."
    
    show kamao shocked_open
    
    ka "R-Really?"
    
    show nagi confident
    
    n "...not."
        
    show kamao angry
        
    ka "Tch!"
        
    show nagi neutral
        
    n "For his sake, of course. I mean, I only just met the guy."
        
    ka "Tch!"
    
    n "Would you stop?"
    
    ka "Tch! Stop what?"
    
    show nagi bored
    
    n "...Whatever it is you're doing."
    
    show kamao unhappy
    
    ka "I'm doing a lot of things."
    
    n "Yeah. Stop doing all of them. Including breathing, please."
    
    show kamao shocked
    
    ka "Oooh, ice queen."
    
    n "Uh-huh. You can leave, now."
    
    show kamao unhappy
    
    ka "Fine!" 

    ka "But, just so you know, I'm not gonna give up that easy. [pc]'s got my name all over him. Not even a legion of Hellguard could keep me from what's rightfully mine!"

    n "Really? How about just one?"
    
    show kamao confused
    
    ka "What?"
    
    show nagi neutral
    
    n "Just one Hellguard."
    
    show kamao unhappy
    
    ka "Well, duh. If I can handle a legion, I'd definitely be able to take on one. Probably with my tails tied behind my back."
    
    n "I see. Excuse me, I have to make a call."
    
    ka "Brushing me off already? Is my aura that terrifying? Fine. Audieu, Snaketits!"
    
    show nagi bored
    
    stop music fadeout 3.0
    
    hide kamao with dissolve
    
    show nagi bored at nagi_center with move
    
    n "..."
    
    n "That nickname's going to follow me to the grave, isn't it?"
    
    n "Oh well."
    
    show nagi happy
    
    n "Now, where'd I leave that phone of mine..."
    
    show black with Dissolve(3.0) 
    
    "..."

    "..."
    
    voice_a "Hey..."
    
    voice_a "Can you hear me?"
    
    voice_a "Easy, easy. Don't move around too much."
    
    voice_a "Are you alright? What's your name?"
    
    voice_b "My... name?"

    voice_a "Yeah. What's your name?"

    voice_b "..."
    
    voice_b "I have no name."
    
    voice_a "You don't? Well, what do your parents call you?"
    
    voice_b "...Parents?"
    
    voice_a "Yeah. Your mom and dad."
    
    voice_b "Mom and... dad?"
    
    voice_a "Don't tell me you don't have parents."
    
    voice_b "..."
    
    voice_a "This might be harder than I thought."
    
    voice_a "Don't worry about it, though. You should get back to rest. I don't know what you've been through, but it can't have been nice."
    
    voice_a "But before that, I guess you need a name, huh? Any ideas?"
    
    voice_b "..."
    
    voice_a "No? Nothing?"
    
    voice_b "...Why?"
    
    voice_a "Huh?"
    
    voice_b "Why do I need a name?"
    
    voice_a "What do you mean?"

    $ renpy.pause(1.0)

    voice_a "Everyone deserves a name."

    
#    unknown "I'm... sorry..."
    
#    "..."
    
#    unknown "This is all my fault."

#    unknown "I'm not going to hurt you ever again."
    
#    unknown "..."
    
#    unknown "That's what I want to say."
    
#    unknown "But..."
    
#    unknown "I don't want to to go."
    
#    unknown "I... I don't want to leave you..."
    
#    unknown "And I don't want you... to leave me."
    
#    unknown "I know I'm a monster... I know that more than anything..."
    
#    unknown "But please..."
    
#    unknown "Don't leave me..."
    
#    unknown "Don't... go..."
    
#    "..."
    
    $ renpy.pause(2.0, hard = True)
    
    jump ch2_scene01


