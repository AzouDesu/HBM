
label start:
    
    python:
        flag_DriderSeen = False
        flag_BondhouseExplained = False
        flag_RoomBesideKumiru = True
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
        
    scene black with dissolve
    
    stop music fadeout 1.0
    
    if gamedebug == True:
    
        #scene debugscreen
        
        "GAME IS IN DEBUG MODE."
        
        "TESTING"
        ###
        
        #scene bg pBedroom
        
        ###
        "END TESTING"
        
    "Note: Game is a heavy work-in-progress. Most assets are NOT final."
    
    ""
    
    "..."
    
    "..."
    
    "...Nh?"
    
    "I can... I can see it..."
    
    "Like a great wound in the stars..."
    
    "And... it's already..."
    
    #[QUEUE]TIRE SCREECHING NOISE
    
    $ renpy.pause(3.0)
    
    "Shuttle Driver" "Son of a...!"
    
    "...?"
    
    "I slowly open my eyes..."
    
    #[QUEUE]SHUTTLE BG
    
    scene bg placeholder
    
    #[QUEUE]MUSIC
    
    play music "assets/sound/bgm/Town2.ogg" fadein 1.0
    
    "Where...?"
    
    "Oh, right... I must've fallen asleep in the shuttle bus. Are we here?"
    
    "I glance over to the woman sitting across from me..."
    
    show allise neutral at allise_center with dissolve
    
    "..."
    
    "...And she's still staring at me. I don't think she's even blinked since I've gotten on board. Is there a type of chimera that doesn't need to blink?"
    
    "No point in asking. She hasn't said a word to me. The driver's been pretty much my only company all day."
    
    show allise at allise_right with move
    
    "Shuttle Driver" "We're here. I'd keep away from the slime, kiddo. She nearly ran in front of the damn bus."
    
    "Slime? I've heard about those. They're made of... jelly, aren't they?"
    
    "Shuttle Driver" "Why don't you and your new friend hop off? I'll grab your things, uh..."
    
    "Shuttle Driver" "..."
    
    "Shuttle Driver" "What was your name, again?"
    
    "Ah... right. I don't think I told her."
    
    jump nameSelect
    
label nameSelect:
    
    $ pc = renpy.input("What is my name?")
    
    $ pc = pc.strip()
    
    if pc == "":
        
        "Shuttle Driver" "Sorry? You'll have to speak up, my hearing's a little bad."
        
        jump nameSelect
    
    menu:
        
        
        "Shuttle Driver" "%(pc)s?"
        
        "'Yes, %(pc)s.'":
            
            #At the beginning of the game, set character nicknames to your name.B
            $ pc_ka = pc
            $ pc_ku = pc
            $ pc_d = pc
            $ pc_f = pc
            $ pc_v = pc
            $ pc_n = pc
            $ pc_a = pc
            
            jump intro_ku_v_meeting
                
        "'Sorry, I'm a little out of it. It was actually...'":
            
            jump nameSelect
    
    
label intro_ku_v_meeting:
    
    pc "Yes, [pc]."
    
    "Shuttle Driver" "Well, [pc], we're here. Hop on out, I'll get your things from the back."
    
    pc "Oh, you don't have to do that..."
    
    "Shuttle Driver" "I do, actually. It's in the job description. Besides, it's not like you or your friend packed heavy..."
    
    "She's got a point. I thought I was packing light, but my 'friend' didn't have a single bag."
    
    "She could have at least brought a change of clothes. Unless... maybe she's a chimera that doesn't need to change?"
    
    "That'd be weird. No weirder than a person made of slime, of course. But everything about her seems completely human."
    
    "Except the strange chill I get whenever I try meeting that dead stare."
    
    "Maybe I can strike up a conversation about her apparent affinity for the colour purple..."
    
    "Shuttle Driver" "...[pc]? Hello?"
    
    pc "Ah! Sorry!"
    
    "Shuttle Driver" "It's fine. But you're gonna have a hard time here if you're getting lost in someone's eyes that easily."
    
    "The shuttle driver gives me a wink as she pushes her door open. The hinges complain. She's an... ogre, I think? Reddish skin, prominent tusks and horns, and generally built like an iron girder. It must be hard for her, driving around in such a cramped space all day. It at least explained the dumbell rack shoved under the passenger seat."
    
    "Blinking away my train of thought, I realize I'm alone in the vehicle with the staring girl. Her unnerving gaze follows me all the way out my door, and I close it maybe a little harder than I should."
    
    hide allise with dissolve
    
    "It's not so much the setting I notice first as the scene currently taking place on it."
    
    scene bg yard
    
    show kumiru angry at kumiru_right
    
    show viscella sad at viscella_left

    with Dissolve(0.5)
    
    v "I s-said I'm sorry..."
    
    ku "It's not me you have to apologize to! You probably gave the driver a heart attack!"
    
    "Shuttle Driver" "Don't worry about it, miss. I've had worse."
    
    "Ah... these must be some of my new roomates. There's the slime the driver was talking about. And the... drider, I think?"
    
    "I'm glad I've never been bad with spiders."
    
    ku_un "Still, what were you thinking running across the road like that? You could've gucked up her radiator - it would've taken days to clean you out!"
    
    v_un "Nnnnh..."
    
    v_un "..."
    
    show viscella shocked
    
    v_un "...Ah? K-Kumi!"
    
    "The slime girl grabs at the drider's sleeve and gives it a few quick tugs, eyes wide as she stares at me."
    
    show kumiru surprised
    
    v_un "Look! It's him!"
        
    "The drider finally notices me. She looks a bit taken aback, but quickly regains her composure."
    
    show kumiru neutral
    
    ku_un "Ah, you must be one of our new roommates!"
    
    ku_un "I'm sorry for the abrupt stop. Viscella here thought she'd dart across the road for..."
    
    show kumiru confused
    
    ku_un "Some reason?"
    
    show viscella confident
    
    v "I-It was to check the number on the side of the bus! I w-wanted to see if it was... {i}his{/i} shuttle or not!"
    
    show kumiru unamused
    
    ku_un "You know that the number's on both sides, right?"
    
    v "..."
    
    show viscella neutral
    
    v "...Oh."
    
    show kumiru neutral
    
    ku_un "Forgive her. She can be a little... slow."
    
    show viscella angry
    
    v "Kumiru!"
    
    "The slime pouts, crossing her arms."
    
    show kumiru unamused
    
    ku "Well, I mean... am I wrong?"
    
    v "N-no, but you can't just {i}introduce{/i} me like that! Especially to... to {i}him!{/i}"
    
    ku "Uh-huh."
    
    pc "Did... did I do something? Every time you refer to me you do it in this hushed whisper that isn't all that hushed..."
            
    show kumiru neutral
    
    ku "Oh, it's because you're a human."
            
    ku "She's not very good with humans."
    
    show viscella flustered
    
    v "K-Kumiru! Seriously!"
    
    show kumiru embarrassed
    
    ku "What! I never said {i}I{/i} was any good with humans either, did I?"
            
    ku "It's not our fault. We haven't exactly had much exposure."
        
    v "Nnh..."
    
    pc "Well... if it makes you feel any better, I haven't had much exposure to chimera, either."
    
    show kumiru neutral
    
    show viscella neutral
    
    ku "Really? You haven't?"
    
    pc "No... my family was very..."
    
    pc "..."
    
    "My parents were the kind of people who'd turn the TV off if a chimera so much as acted like a reasonable role model."
    
    "If I didn't have a steady stream of outside information smuggled to me by a few friends, I'd probably have turned out a lot like them."
    
    "Telling that to a pair of chimera I just met might make things awkward, but..."
    
    menu:
        
        "{cps=0}Telling that to a pair of chimera I just met might make things awkward, but...{/cps}"
        
        "'My parents were specist.'":
            
            pc "My parents were specist."
            
            pc "They punished me pretty badly if I tried associating with any chimera, or even learning about them..."
            
            v "Eh? Why? I m-mean, um, I like to think a lot of chimera are pretty n-nice! Sometimes! Er, usually..."
            
            ku "Come on, Viscella, don't make things awkward."
            
            pc "Sorry, I think I beat her to it."
            
            show kumiru happy
            
            ku "Oh, you only made things a {i}little{/i} awkward. That's nothing."
            
            ku "Viscella and I are experts in making things {i}very{/i} awkward."
            
            v "...She's right."
            
            ku "Mmhm. As you might have gathered, by the way, this is Viscella, and I'm Kumiru. Good to meet you."
    
        "'I was pretty sheltered growing up.'":
            
            pc "I was pretty sheltered growing up."
            
            pc "I... never had much contact with chimera."
            
            v "You didn't? Why not?"
            
            pc "We didn't have a lot of them in my hometown, so I never had the chance..."
            
            ku "Well, by the end of the year I'm sure you'll have had {i}plenty{/i} of contact with chimera."
            
            show viscella embarrassed
            
            ku "..."
            
            v "..."
            
            show kumiru unamused
            
            ku "Don't, Viscella."
            
            v "I'm not saying anything..."
            
            ku "You were going to. Ah, back on topic."
            
            show kumiru happy
            
            ku "This is Viscella, and I'm Kumiru. Nice to meet you."
            
    pc "Nice to meet you, too. I'm [pc]."
    
    show viscella neutral
            
    "It's hard not to stare. I'd very rarely seen anything like these people before. I have this unusual urge to poke my finger in the slime. I wonder what the consistency's like? Is it sticky, or runny?"
    
    "Then my attention is drawn to the drider. All her eyes blink at the same time - even the small, jet-black ones adoring her forehead. Why don't they need glasses? Does she have little contacts for her little eyes?"
    
    show kumiru neutral
    
    ku "Ah... [pc]?"
    
    pc "Oh? Oh! Sorry, it's been a long day..."
    
    "The ogre nudges me as she passes by."
    
    "Shuttle Driver" "Eyes on the prize, kiddo."
    
    "She's carrying all my stuff slung over her shoulders like it's child's play. She must be flexing, because with how easy she's walking there's no way my stuff is actually putting any strain on her arm muscles. That's..."
    
    menu:
        
        "{cps=0}She's carrying all my stuff slung over her shoulders like it's child's play. She must be flexing, because with how easy she's walking there's no way my stuff is actually putting any strain on her arm muscles. That's...{/cps}"
        
        "...kinda scary.":
            
            "She could probably snap me like a twig."
            
            "It's a good thing she seems friendly."
            
        "...kinda hot.":
            
            "She could probably snap me like a twig."
            
            "I don't think I'd complain."
            
    ku "Ah! Well, while she's taking your stuff up to your room - would you like a tour? Viscella and I have already done some exploring."
    
    show viscella excited
    
    v "It's sooo cool! It's got everything! Wait till you see the-"
    
    ku "No spoilers, Viscella."
    
    show viscella neutral
    
    v "Aww..."
    
    "A tour? That could be fun. Plus, it gives me a chance to get to know the people I'm going to be spending a year with."
    
    pc "Sure. I don't have much else going on."
    
    show kumiru happy
    
    show viscella happy
    
    ku "Great! Come on, I'm excited to see your reaction."
    
    hide kumiru with dissolve
    
    "Kumiru's body seems to float as her eight legs carry her down the small garden path towards the front door. It's not a mansion, by any means - but it looks extremely comfortable." 
    
    "Made of red-brown brick, the estate seems about four stories tall, and the roof seems to be bordered by a minimalistic railing - perhaps evidence of a rooftop terrace? There's no lack of windows, at least, and the driveway is long and winding enough that it's difficult to even make out the street we came in on behind the tree cover."
    
    show viscella embarrassed
    
    "I stop taking in the surroundings when I realize Viscella's been more preoccupied with staring at me. I discreetly return the glance, at which she nearly jumps, face turning a deeper shade of blue as she spins around and attempts to catch up to her friend."
    
    hide viscella with dissolve
    
    "I go to follow, before hesitating. I surreptitiously glance over my shoulder."
    
    stop music
    
    play sound "assets/sound/sfx/vinylscratch.wav"
    
    show allise neutral at allise_center with dissolve
    
    play music "assets/sound/bgm/noodle.mp3"
    
    "She's only a few inches away."
    
    "Naturally, I nearly jump out of my skin."
    
    pc "Gah! What the- you scared the hell out of me!"
    
    "The woman just stares as I regain my composure. I don't know what she's trying to accomplish, but..."
    
    menu:
        
        "{cps=0}The woman just stares as I regain my composure. I don't know what she's trying to accomplish, but...{/cps}"
        
        "It's giving me a bad first impression...":
            
            "The least she could do is acknowledge my existence. Well, without just... glaring at me."
            
        "It's got me curious...":
            
            "I'd like her to at least give me a hint. This guessing game is driving me nuts. Is this normal for her, or did I do something to offend her?"
    
    "As if responding to my thoughts, she cocks her head - and, to my complete and utter shock, actually {i}blinks{/i} for once. It's rather slow, as if it was deliberate, but I'll take what I can get."
    
    a_un "I am sorry."
    
    "It's... strange. It's almost posed as a question, but without the sarcasm that would usually imply. As if saying she's sorry is a genuine question."
    
    pc "Ah... don't worry about it."
    
    a_un "...Okay."
    
    "We stare at each other for a good ten seconds before I realize she's not going to elaborate."
    
    menu:
        
        "{cps=0}We stare at each other for a good ten seconds before I realize she's not going to elaborate.{/cps}"
        
        "Retreat":
            
            pc "Well, um... nice to talk to you!"
            
            "She watches me with the same unreadable, blank expression that she'd been giving me for the past two hours. Backing away slowly, I turn around and fastwalk towards the door."
            
            "As I make it there, I glance over my shoulder one more time - and am relieved to see that the woman has apparently become distracted, hunched over on the pavement as she scrutinizes something between her shoes. Relaxing somewhat, I push open the door and step inside."
            
        "Try to chat":
            
            pc "You're... not very talkative, are you?"
            
            "She's back to staring at me again. I'm about to give up and head inside, before..."
            
            a_un "No."
            
            pc "I... see. Did I do anything to offend you...?"
            
            a_un "No."
            
            "I see. Well, that's a bit of a relief, at least."
            
            pc "If you don't mind me asking, um... is there something on my face? I think you've been staring at me for two hours straight..."
            
            a_un "No."
            
            "Ah... is she saying 'no' to the two hours thing, or 'no' to the inquiry about something on my face?"
            
            pc "So, you... haven't been staring at me?"
            
            a_un "No."
            
            "I open my mouth to respond, but realize she could have either been saying 'No, I have not been staring at you', or 'No, I have actually been staring at you'. I don't know who this person is, but she's a bit of a challenge to talk to."
    
            "Or maybe she's just saying 'no' on purpose. Is she actually just screwing with me, I wonder?"
            
            pc "Do... well, what's your name? I'm [pc]."
            
            a_un "I know."
            
            "Ah, right. I told the shuttle driver - she must have overheard. But at least I'm getting something other than a 'no'. I'm about to continue my interrogation until I hear the front door open. Glancing over, I see Kumiru poking her head through the door."
            
            ku "[pc]? Oh! Sorry, I didn't know you were occupied!"
            
            pc "Ah? Oh! Hold on, I'm coming!"
            
            "I glance back to the woman I'm talking to, but... she's hunched over, examining what seems to be a solitary beetle, panicking on the pavement."
            
            "It's flopped over, legs spasming wildly as it tries to roll back onto its belly."
            
            a_un "You should not keep them waiting."
            
            "There's something in her voice - I can tell it's a bit more than a suggestion. Yet it doesn't seem forceful. I watch as she reaches down, nudging the beetle back onto its belly - it scurries away, no worse for wear."
            
            pc "Can't I at least get your name?"
            
            a_un "Later."
            
            "Well... it's the best I'm gonna get, I think. I leave her be, taking the cobbled path that leads up to the entryway stairs. Glancing over my shoulder, I am unsurprised to find her staring at me. At least she's doing it at a distance, now. Sighing, I push open the door, and step inside."
            
    play music "assets/sound/bgm/Town2.ogg" fadein 1.0
    
    "...And nearly run into my driver's chest in the process."
            
    scene bg living
    
    "Shuttle Driver" "Got your stuff moved up to the third floor, since that seemed to be where all the bedrooms were. Grab a nice one, yeah?"
    
    pc "I will. Thanks for all your help."
    
    "Shuttle Driver" "Hey, no problem. You take it easy, kiddo - and good luck."
    
    "She gives me a wink, nodding politely at the other two chimera present before ducking under the doorframe and politely closing the door behind her."
        
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left
    
    with dissolve
    
    ku "She was nice. Out of curiosity, though... who were you talking to out on the driveway?"
    
    pc "I'm not sure."
    
    show kumiru confused
    
    ku "You're not?"
    
    pc "Nope. She arrived with me, but she's barely spoken. I was starting to suspect she was mute..."
    
    show kumiru neutral
    
    ku "I see... well, if she's still around later, I suppose we'd better introduce ourselves. Right, Viscella?"
    
    v "Nnnngh..."
    
    ku "Come on, you knew there were going to be a lot of introductions the first few days. You'll have to bear with it."
    
    "Viscella gives a little huff, but otherwise doesn't raise much of a fuss."
    
    ku "Anyways... welcome to Medley Manor! I think? That's what it was called on the website, at least..."
    
    "Kumiru gestures in welcome. They foyer's spacious and comfortable - and connected directly to the nearby living room through a minimalist arch. Kumiru follows my gaze."
    
    ku "Ah, that's the living room! You, um... live in it."
    
    show kumiru embarrassed
    
    ku "...Obviously."
    
    "Kumiru looks somewhat flustered before those eight legs of hers begin carrying her straight down the foyer and past the arch to the living room, passing into an entrance I can't quite make out. I kick my shoes off and follow. I can hear the soft pitter-patter of Viscella's wet footsteps as she follows a healthy distance behind me."
    
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
        
        v "{cps=0}Because it's huge! It's huge, isn't it?{/cps}"
        
        "'It's huge.'":
            
            pc "It's huge."
            
            show viscella vhappy
            
            v "See?"
            
            ku "Am I the only one not awestruck by the size of the fridge?"
            
            show viscella happy
            
            v "Doesn't it make you realize how small you are? In the grand scheme of things, I mean."
            
            ku "It's a fridge."
            
            v "A {i}huge{/i} fridge."
            
        "'It's pretty average.'":
            
            pc "It's pretty average."
            
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
    
    v "Come on, Kumi, every house has kitchens and living rooms..."
    
    show kumiru neutral
    
    show viscella happy
    
    v "Let's show him the cool stuff!"
    
    ku "Alright, alright, we're getting there."
    
    ku "No point taking you to the basement, since it's mostly empty space..."
    
    ku "You might want to get your shoes on - it's a short walk outside to get to the pool."
    
    show viscella scared
    
    v "...*gulp*."
    
    scene bg pool with dissolve
    
    show kumiru neutral at kumiru_center with dissolve
        
    ku "Well, here we are! The indoor pool. I'm not very good at swimming, to be completely honest."
    
    ku "Neither is Viscella, which is why she's cowering by the entrance."
    
    v "I- I'm not c-cowering!"
    
    show kumiru happy
    
    ku "Don't mind her - slimes don't do well with water. Or faucets, for that matter. Viscella gets nervous even {i}looking{/i} at a kitchen sink."
    
    v "K-Kumiru!"
    
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
    
    ku "..."
    
    show viscella embarrassed
    
    v "...Oh. Whoops."
    
    show kumiru neutral
    
    ku "Anyways, as my good friend was just saying, there's a home theatre up here."
    
    scene bg theatre with wipeleft
    
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left 
    
    with dissolve
    
    ku "Here it is. Pretty neat, huh?"
    
    v "'Pretty neat'? You wouldn't stop talking about it earlier."
    
    ku "I've calmed down. And you were even worse than I was."
    
    show viscella happy
    
    v "Well, of course!" 
    
    show viscella excited
    
    v "Gigantic screen! Surround sound! Noise-proof walls! Lockable door!"
    
    v "All you need for a non-stop night of totally immersive, high-resolution H-gaming!"
    
    show kumiru unamused
    
    v "..."
    
    show viscella shocked
    
    v "...Uh."
    
    show viscella scared
    
    v "As in, y'know, h... h... hurtful games. That are really... sad?"
    
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
    
    ku "This is the study. It has a small library's worth of books, and a computer with working internet."
    
    show kumiru unamused
    
    ku "Not good internet, mind you. Noo, can't have your tenants getting decent download speeds or a consistent connection. They get what they paid for with their exorbitant bondhouse entry fee - an average download speed of 500 kilobytes per second on DSL cables made of rolled-up tinfoil."
    
    v "K-Kumiru..."
    
    ku "No, no, it's fine. I'm fine with spending the rest of the year playing singleplayer games because the internet will do its utmost to constantly drop out at the most crucial moment of a match, raid, whatever. And say bye-bye to server hosting."
    
    show viscella unamused
    
    v "Kumiru?"
    
    ku "And if {i}that{/i} wasn't bad enough, the hundred-gigabyte monthly bandwidth cap is the icing on the fu-"
    
    show viscella flustered
    
    v "KUMIRU!"
    
    show kumiru surprised
    
    ku "Y-yes?"
    
    show viscella angry
    
    v "You're ranting!"
    
    show kumiru embarrassed
    
    ku "Oh... ah. S-sorry. *Ahem*. Next room!"
    
    scene bg gym with wipeleft
    
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left 
        
    with dissolve
    
    ku "This is the exercise room."
    
    ku "Most of the equipment is designed for bipeds, unfortunately, so I can't use them myself."
    
    v "What about the weights? You could lift those..."
    
    ku "Yep, all designed for bipeds. Sad, but there's no helping it. Looks like I'll have no choice but to continue living a sedentary lifestyle."
    
    show viscella angry
    
    v "But what about the-"
    
    ku "Anyways, next room!"
    
    scene bg hallway with wipeleft
    
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left 
    
    with dissolve
    
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
    
    show kumiru neutral at kumiru_right
    
    show viscella excited at viscella_left 
    
    with dissolve
      
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
    
    show kumiru neutral at kumiru_right
    
    show viscella neutral at viscella_left 
    
    with dissolve
        
    ku "Well that's it for the 'fun' rooms."
    
    v "Bedrooms can be fun."
    
    ku "You know what I mean."
    
    ku "I'd like to show you the rooftop, but it's locked and none of us have the key. I'm guessing safety concerns..."
    
    ku "Regardless, all the rooms here on the third floor are bedrooms. Well, except the bathroom, of course."
    
    ku "You can go ahead and choose one, if you'd like. Viscella and I have already chosen these two."
    
    "Kumiru gestures to the middle and far rooms on the left side of the hallway. I notice my things piled on the floor at the end of it, right beside the small spiral staircase that most likely leads to the roof."
    
    "There are six rooms total: three on the right, and three on the left. I could choose the nearby room beside Kumiru, or I could opt for the quiet-looking room in the far corner, across from Viscella."
    
    menu:
        "Which room will I take?"
        
        "Close room beside Kumiru.":
            
            $ flag_RoomBesideKumiru = True
            
            pc "I guess I'll take the one beside you, Kumiru."
            
            show viscella happy
            
            v "Yay! We've got the left side of the hall all to ourselves!"
            
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
            
            pc "I'll take the one across from you, Viscella. I've always been a sucker for corner rooms."
            
            show viscella happy
            
            v "I know! Aren't corner rooms the best?"
            
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
    
    jump intro_ka_meeting

label intro_ka_meeting:
    
    scene bg pBedroom with Dissolve(3.0)
    
    play sound "assets/sound/sfx/door_close.wav"
    
    play music "assets/sound/bgm/tam-n17.mp3" fadein 3.0
    
    
    "It's pretty much barren."
    
    "There's a digital alarm clock on the nighstand that reads three o'clock. There's also a dresser and a desk, complete with a chair."
     
    "I check the furniture, and then the closet. All empty."
    
    "Well, guess it's time to start moving in. I head out into the hall and start dragging my stuff into my room, opening a few boxes as I do so."
     
    "I'm starting to wish I packed a bit more. I'm going to have to last a whole year on a week's worth of clothing, and I've got no decorations whatsoever."
                                                                                                                                                             
    "At least I have some electronics. I hope that number change request has gone through, or else my phone's probably still being inundated with messages from my parents asking me where I've gotten off to. I hope they weren't determined enough to install some sort of tracker..."
    
    "Oh well. I unzip my laptop bag, checking through once more to ensure I have everything. Turns out I might have forgotten a mouse. Oh well, I can always buy a new-"
    
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
        "It seems I've been tackled by..."
        
        "'A catgirl?'":
            
            pc "Uh... a catgirl?"
            
            ka_un "Nope. Fluffier."
            
            ka_un "Touch my tail and see for yourself."
            
            show kamao winkblush
            
            ka_un "Actually, touch anywhere you want."
            
            show kamao neutral
            
        "'A foxgirl!'":
            
            pc "You're a... kitsune, right?"
            
            show kamao winkblush
            
            ka_un "Handsome {i}and{/i} 20/20 vision! I'm impressed!"
            
            show kamao neutral
            
            ka_un "The correct term is kitsune, but..."
                   
            show kamao teasing       
            
            ka_un "You can call me whatever you want, big boy."
            
        "'A nuisance.'":
            
            pc "A nuisance."
            
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
    
    ku "What are you talking about? He was never lost. And why on earth are you sitting on him?"
    
    show kamao neutral
    
    ka_un "Am I not allowed to sit on my future boyfriend?"
    
    show kumiru unamused
    
    show viscella shocked
    
    v "W-What?!"
    
    ka_un "You heard me, jailbait. We just finished consummating our love for one another." 
    
    menu:
        
        ka_un "{cps=0}You heard me, jailbait. We just finished consummating our love for one another.{/cps}" 
        
        "'We definitely did not do that.'":
            
            pc "Yeah, no."
            
            show viscella happy
            
            v "Oh, that's a relief..."
            
            ku "Viscella, it took us less than a minute to get here. The only thing she consummated is a restraining order."
            
            ka_un "Our love transcends all boundaries, including those defined in a legal contract."
            
            show viscella unamused
            
            "The girl rolls off my back. I stand up, brushing off my pants."
            
            
        "'Someone get this furball off of me.'":
            
            pc "Someone please get this furball off of me."
            
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
            
            pc "Now... now I can never get married..."
            
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
    
    ku "A pleasure. Please tell me you're not one of the tenants we should be expecting."
    
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
    
    "A kitsune? Apart from the ears and tails, she doesn't seem all that unusual. Certainly less unusual than the other two. Why is it that she's only got some minor attributes of a fox, whereas Kumiru's entire biology is radically different?"
    
    "Unless it's all surface-level. Maybe she's got three spleens."

    ka "Now, before we were so rudely interrupted by four- ten eyes here, you were telling me your name."
    
    show kumiru unamused
    
    ku "*Sigh*."
    
    menu:
        
        ku "{cps=0}*Sigh*.{/cps}"
        
        "'It's [pc].'":
            
            pc "[pc]."
            
            show kamao horny
            
            ka "Nice. You'll hear me screaming it out soon enough."
            
            show kumiru embarrassed
            
            show viscella embarrassed
            
            ku "..."
            
            v "..."
            
            show kumiru unamused
            
            ku "Can you even feel shame?"
            
            show kamao winkblush
            
            ka "Yeah. It's a huge turn-on."
            
        "'Guess.'":
            
            pc "Guess."
            
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
            
            pc "No."
            
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
            
            show kamao neutral
            
            ka "Duh."
            
    show kamao neutral
            
    ka "Man, I'm so relieved. I was worried this bondhouse was gonna be a total taco fest."
    
    show kamao wink
    
    ka "We're gonna have a lot of fun, handsome!"
    
    ku "Actually, you're not."
    
    show kamao bored
    
    ka "Oh, don't be like that. You're just jealous he's head over heels for me."
    
    ku "Uh-huh. Since your odds of actually winning someone's favour with that behaviour are virtually nil, we'd all appreciate if you kept the sexual harrassment to a minimum."
    
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
        
        ka "Why? You're jailbait."
        
        ka "I never said it was a bad thing, now did I?"
        
        show viscella embarrassed
        
        v "..."

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
    
    ku "Can we have this conversation somewhere else? Not in the middle of [pc]'s room? You'll need to come back downstairs anyways, you dumped your luggage all over the foyer the moment Viscella mentioned a male pronoun."
    
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
    
    jump intro_f_meeting
    
label intro_f_meeting:
    
    #$ clock_access = True
    
    "Well, that was something."
    
    "I check the alarm clock. It's a quarter after three."
    
    "At least now maybe I'll be able to catch a-"
    
    $ renpy.music.set_volume(0.0)
    
    play sound "assets/sound/sfx/doorbell.wav"
    
    $ renpy.pause(3.0, hard = True)
    
    $ renpy.music.set_volume(1.0)
    
    "-break."
    
    "Well, seems like it's going to be a busy day."
    
    "I decide to go investigate. No use brooding in my room all day."
    
    #$ clock_access = False
    
    scene bg living with Dissolve(2.0)
    
    "I descend the two flights of stairs to the ground floor."
    
    "Halfway there, I hear the sounds of a struggle. I quicken my pace, and before long arrive at what is unmistakably the source."
    
    show fenira angry at fenira_right with dissolve
    
    f_un "N-Nagi! Get your ass back here and get this fleabag off of me!"
    
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
    
    f_un "Are you serious? Are you {i}blind{/i}? Look at me!"
    
    show kamao neutral
    
    ka "You don't walk like a chick."
    
    f_un "And you don't walk like you've got your head stuck up your ass. Guess appearances can be deceiving, huh?"
    
    show kamao shocked

    ka "Well! I never!"
    
    show kamao neutral
    
    ka "[pc], are you gonna let her mad burn your girlfriend like that?"
    
    menu:
        
        ka "{cps=0}[pc], are you gonna let her mad burn your girlfriend like that?{/cps}"
        
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
    
    f_un "Hope I didn't make too much of a bad impression..."
    
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

    "I find my eyes drawn to her enormous talons. It's probably a good idea not to piss her off too much."

    show fenira at fenira_center with dissolve

    f_un "..."
    
    show fenira inquisitive
    
    f_un "Hey, uh, what's your name?"
    
    pc "I'm [pc]. You?"
    
    show fenira happy
    
    f "Fenira."
    
    "She extends a wing towards me. She's only got three fingers - where a human would have their ring and little finger, she instead has a long wing joint that supports many of the feathers of her wing."
    
    show fenira vhappy
    
    "Instinctually, I grasp her version of a hand and give it a firm shake. Thankfully, this seems to be what she expected me to do - she gives me a bright smile and shakes back. She's got a strong grip."
    
    f "Nice to meet ya."
    
    pc "You, too. Where is everyone?"
            
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
        
        f "{cps=0}Actually, you know what? I'll come with you. If I don't, she'll probably end up talking you into helping her, too.{/cps}"
        
        "'Do you want help with your things first?'":
            
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
            
    jump intro_n_meeting
            
label intro_n_meeting:
            
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
        
        f "{cps=0}Pffft.{/cps}"
        
        "'That was mean.'":
            
            $ flag_FeniraRacismName = False
            
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
            
            f "Hah! You too?"
            
            f "Worse thing Nagi'll do is make us clean it up."
            
            show fenira neutral
            
            f "Don't get me wrong, she {i}can{/i} be scary, but... normally she doesn't quite have the energy."
            
            show fenira shocked
            
            stop music
            
            n_un "Don't have the energy, do I?"
    
    play music "assets/sound/bgm/scene_comi2.ogg"
    
    f "Oh crap."
    
    n_un "Oh crap indeed."
    
    n_un "How about we play a little game, Fen-fen?"
    
    show fenira angry
    
    f "Nuh-uh. No way. You can take your dumb games and shove 'em up your-"
    
    show nagi confident at nagi_left behind fenira with dissolve
    
    n_un "Shove them up my what?"
    
    show fenira shocked at fenira_center
    
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
    
    n "...Yeah, I know. I overheard the whole thing."
    
    f "So what's the damned problem?"
    
    n "You'll find out in a moment."
    
    n "I, Nagi Forques, hereby charge you, Fenira Featherwood, with..."
    
    show fenira confused
    
    n "With..."
    
    show nagi bored
    
    stop music fadeout 1.0
    
    n "...Eh, nevermind. Too much effort."
    
    show fenira neutral
    
    f "Just like that?"
    
    play music "assets/sound/bgm/Town2.ogg"  
    
    n "Yeah. I'm tired. Least you could do is go tell the slime I'm not gonna eat her or anything."
    
    f "Uh... you're not upset about the bottles?"
    
    n "Huh? They're empty wine bottles. I don't even drink wine - why would I care?"
    
    show fenira confused
    
    f "I mean, you {i}packed{/i} them, didn't you?"
    
    show nagi neutral
    
    n "Mmh? So? I packed a lot."
    
    "The snake woman gestures over her shoulder to a veritable mountain of boxes left on a large, velvet blanket further down the driveway, with a moving truck tottering off out of sight. I can vaguely make out a figure struggling with something - Kumiru, by the looks of it."
    
    show fenira angry
    
    f "I don't... you were telling me just last week that your wine bottle collection was your pride and joy!"
    
    n "Yeah, I was just screwing with you. Why would I collect wine bottles?"
    
    show fenira neutral
    
    f "God, Nagi, this is... you're a real piece of work, you know?"
    
    n "Yup. Who's this?"
    
    hide fenira
    
    show nagi neutral at nagi_full 
    
    with dissolve
    
    "Her tail... it's huge, probably around four meters long, but from what I've read that's actually rather short for a lamia. Even the owner of this one must have some sort of trouble navigating buildings and vehicles built for humans. I guess that starts explaining the special accomodations for chimera bodyshapes I've noticed in my few days within mainstream society..."
    
    n "I think he's checking me out."
    
    f "[pc]?"
    
    
    f "[pc]!"
    
    show nagi neutral at nagi_left
    
    show fenira confused at fenira_right
    
    with dissolve
    
    pc "Hwa? Huh?"
    
    show nagi happy
    
    n "Hi."
    
    pc "Oh, sorry! I was-"
    
    show fenira neutral
    
    show nagi wink
    
    n "Distracted? I'm not complaining. I shed recently, so my scales are nice and shiny - glad someone finally notices."
    
    f "Look the same as they always do..."
    
    show nagi neutral
    
    n "And this is what I mean by 'glad someone finally notices'."
    
    n "Alright Fen-Fen. Go apologize to that slime for me."
    
    f "But-"
    
    n "Wow. You know how sensitive I am about the 'not having a butt' thing."
    
    show fenira annoyed
    
    f "Ugh..."
    
    n "Go. Shoo."
    
    f "Fine! Fine, I'll go. Why the hell do I even bother..."
    
    n "Oh, am I being inconsiderate?"
    
    show nagi confident
    
    n "Ooh, I see. I'm {i}interrupting{/i}, aren't I?"
    
    show fenira flustered
    
    f "N-no, I-"
    
    f "I didn't- I wasn't-"
    
    show fenira embarrassed
    
    f "Grrr..."
    
    f "Y'know what, screw you."
    
    hide fenira with dissolve
    
    show nagi neutral at nagi_center_flipped with move
    
    n "I'm good, aren't I?"
    
    f "Shuddup, snaketits!"
    
    n "Sure thing, birdbrain."
    
    "Fenira stomps off, shoving the corners of her wings - her 'hands' - deep into her pockets. Her wingtips drag along the cobblestone as she sulks her way into the house, slamming the door behind her with a talon."
    
    n "Well, that was fun. [pc], was it?"
    
    pc "Yeah, that's me..."
    
    n "Nice to meet you. I'm Nagi, as you probably gathered."
    
    "We're interrupted by a hissed curse coming over from the pile of packed boxes. Kumiru seems to be having some trouble with one of them."
    
    n "We should probably go help, huh?"
    
    pc "Yeah. Don't want her to hurt herself."
            
    show nagi happy
            
    n "Little too late for that, I think."
            
    scene bg street with wipeleft
    
    show kumiru sad at kumiru_center with dissolve:
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
       
    show kumiru angry_open with vpunch
       
    ku "Gah, damnit!"
    
    show kumiru sad
    
    n "Well, you've moved it a few feet, at least."
    
    show nagi neutral with dissolve:
        nagi_left
        
    show kumiru shocked
        
    ku "Ah, Miss Forques!"
    
    show nagi bored
    
    n "Just 'Nagi', please."
    
    ku "And [pc]!"
    
    show kumiru surprised
    
    ku "..."
    
    show kumiru embarrassed
    
    ku "Well, this is embarrassing."
    
    show nagi neutral
    
    n "Why'd you offer to carry it if you couldn't handle it?"
    
    show kumiru confident
    
    ku "Because it was polite."
    
    ku "..."
    
    show kumiru sad
    
    ku "And it would've been pretty embarrassing. A drider should have no problem lifting something like this..."
    
    n "Nah, that thing's stuffed with my winter clothes. Need a hand?"
    
    ku "Um... yes."
    
    "You and Nagi each grab one end of the box and lift. It's... not that heavy."
    
    menu:
        
        "{cps=0}You and Nagi each grab one end of the box and lift. It's... not that heavy.{/cps}"
        
        "'Whew, this thing weighs a ton! {i}Right, Nagi?{/i}'":
            
            $ n_like += 1
            
            show kumiru happy
            
            show nagi surprised
            
            n "Huh?"
            
            show nagi wink
            
            n "Oh, yeah, totally. Feels like my spine's about to give out on me."
            
            show nagi happy
            
            n "And my spine's as strong as you'd expect. Alright, [pc]. One-step two-step."
            
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
                
                n "{cps=0}Right, [pc]?{/cps}"
                
                "'You caught me.'":
                    
                    $ ku_love += 1
                
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
                    
                    $ n_love += 1
                    
                    show nagi neutral
                    
                    n "Are you, now?"
                    
                    show nagi wink
                    
                    n "Well, it might be working."
                    
                    show nagi confident
                    
                    show kumiru embarrassed
                    
                    ku "Guys..."
                    
                    n "Whoops. C'mon, we can flirt later."
                    
                    ku "Miss Forques!"
                    
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
        
        n "{cps=0}Beats me. Not that I mind having someone polite around. Especially after dealing with Fenira for nearly a decade.{/cps}"

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
    
    n "How many times have you said 'sorry' and 'thank-you' in the last ten minutes?"
    
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
    
    "Kumiru blinks, and then gives a nervous cough."
    
    show kumiru sad
    
    ku "Uh... w-well, it seems that pretty much everyone is starting to settle in."
    
    ku "Which is... good..."

    ku "..."
    
    show kumiru neutral
    
    ku "Er, are {i}you{/i} settling in? Since, y'know, I guess you're not used to chimera and stuff..."
    
    "You shake your head."
    
    pc "I'm doing just fine. It can get a little nervewracking, though... I'm worried about accidentally offending someone." 
    
    ku "Oh, really? What do you mean?"
    
    pc "Well, you know..."
    
    pc "Like... how can the eyes on your forehead see if they've got no irises?"
    
    show kumiru happy
    
    ku "Oh, they don't see in the same way as my human eyes. They're primarily for detecting movement and motion."
    
    pc "Really?"
    
    ku "Yup. So don't worry about asking innocent questions like that, I doubt anyone would mind answering them."

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
    
    "I take a few minutes to drag in my things. I've only got two boxes and a suitcase stuffed with clothes and other necessities, which I get to work unpacking."
    
    "I hope it's enough. I've gotta survive six months off this stuff, and while there's nothing stopping me from buying more, I don't exactly have a steady income."
    
    "All in all, it takes me about a half-hour to load my dresser with clothes and install a few necessities - like a reading lamp and alarm clock. The rest mostly consists of books, a few movies, my laptop, razor - that sort of thing."
    
    "By the time I finish, I triumphantly overlook my territory. It looks... somewhat more habitable. I'm tempted to spend some time here reflecting on what I've seen - or, more likely, spend it goofing off - but I'm still curious about the people I've met today."
    
    "Besides, I've got some time on my hands. How should I spend it?"
    
    menu:
        
        "{cps=0}Besides, I've got some time on my hands. How should I spend it?{/cps}"

        "Help Kumiru look for Viscella.":
            
            "If what Kumiru said is anything to go by, Viscella's been missing."
            
            "To be fair, I saw her less than half an hour ago, so it's not exactly a life-or-death situation."
            
            "Regardless, I decide to join Kumiru's one-drider search party."
            
            jump intro_visSearch

        "Help Fenira set up.":

            if flag_OfferedFeniraUnpackHelp:
                
                "I recall offering to help Fenira unpack her things. Might as well follow up on it."
                
            else:
                
                "I decide to go see what Fenira's up to. Maybe we'll be able to talk a little now that she's not getting teased by Nagi."
                
            jump intro_fenVisit
            
        "Pay Nagi a visit.":
            
            "Nagi said she was going to collapse on her bed."
               
            "She didn't actually say she was going to sleep on it."
            
            "I decide to take advantage of this loophole."
            
            jump intro_nagVisit
        
        "Take Kamao up on her offer.":
            
            "Kamao said she would give me a prize if I went to visit her."
            
            "There's no telling what the prize is, though I have a few good guesses... well, only one way to find out."
    
            jump intro_kamVisit  
            
label intro_visSearch:  
    
    $ v_like += 2
    
    $ ku_like += 2
    
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
    
    pc "Yeah..."
    
    ku "I just wish she would stop running from her problems. She acts so immature sometimes. It's easy to forget she's nineteen, you know?"
    
    pc "Nineteen?"
    
    ku "I know, right? If she doesn't learn to take care of herself, she's not going to be able to survive out on her own. I can't hold her hand forever."
    
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
    
    "The room's empty, though it looks like someone's already raided the alcohol cabinet by the bar - it looks lighter than I remember it being."
    
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
    
    pc "No. In fact, she was upset with Fenira for misleading you."
    
    v "So... I've been hiding for half an hour for no reason?"
    
    pc "None whatsoever."
    
    show viscella neutral
    
    v "Whew. That's a relief."
    
    menu:
        
        v "{cps=0}Whew. That's a relief.{/cps}"
        
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
            
            v "The one that she makes when I say something stupid."
    
            pc "Uh... right."
            
    pc "Either way, you shouldn't be hiding in closets."
    
    v "Why not?"
    
    menu:
        
        v "{cps=0}Why not?{/cps}"
        
        "'It's immature.'":
            
            show viscella scared
            
            v "It is?"
            
            pc "Well, you're an adult, right?"
            
            show viscella angry
            
            v "Y-yes!"
            
            pc "When was the last time you saw an adult hiding in a closet?"
            
            show viscella happy
            
            v "Blade X Oblivion season two episode seven."
            
            v "Kizuna hides in a closet from her mother's geist."
            
            pc "But I'm assuming she's not hiding because she broke the geist's stuff, right?"
            
            show viscella excited
            
            v "Actually-"
            
            pc "It was a rhetorical question."
            
            show viscella neutral
            
            pc "Are you ready to go back downstairs?"
        
        "'There are way better hiding places than closets.'":
            
            $ v_love += 1
            
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
    
    "Viscella and I return to the living room. Kumiru seems to have been hard at work trying to align a photo frame..."
    
    show kumiru angry at kumiru_center with dissolve
    
    ku "Who the hell did they hire to organize this place? Come on, I could do better in my sleep..."
     
    "She glances over her shoulder."
     
    show kumiru surprised
     
    ku "O-oh, [pc]! You found her!"
    
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
        
        v "{cps=0}I... I...{/cps}"
        
        "'Sorry, Viscella. I mean, she's spot on...'":
            
            $ ku_love += 2
            
            $ ku_like += 2
            
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
            
            $ v_love += 2
            
            $ v_like += 2
            
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
    
            $ ku_like += 1
            
            $ v_like += 1
    
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
        
        ku "I guess it's not fair of me to always assume the worst of Viscella."
        
        "Er... about that..."
        
        ku "Well, certainly not the {i}worst{/i}."
        
        ku "But you know what I mean."
        
        ku "I mean this in the best possible way, but if Viscella {i}can{/i} screw something up, chances are she {i}will{/i}." 
        
    show kumiru happy
    
    ku "Sorry, I'm ranting. Anyways, I really appreciate the help. I'll let you get going."
    
    ku "Wouldn't want to get in the way of that good night's rest."
    
    jump intro_kam_nagi_fight
    

label intro_fenVisit:
    
    $ f_like += 4
        
    
    $ flag_VisitedFenira = True
    
    scene bg hallway with dissolve
    
    if flag_RoomBesideKumiru:
        
        "The door across from me, which I remember to be Kamao's, is ajar. I stealthily slip past in order to avoid detection, and approach the room two doors over."
        
        "Fenira must have taken the room wedged in the corner, across from Viscella."
    
    else:
        
        "The door to my left, which I remember to be Kamao's, is ajar. I stealthily slip past in order to avoid detection, and approach the opposite end of the hallway."
        
        "If Kamao and Nagi took the two rooms beside me, Fenira must have taken the room beside Kumiru."
    
    "As I approach, I can start to hear music on the other side of the door."
    
    play sound "assets/sound/sfx/knock.ogg"
    
    stop music fadeout 2.0
    
    "I give it a knock."
    
    f "It's open. Unless you've got a tail. Then it's locked."
    
    "I push open the door."
    
    scene bg fBedroom with dissolve
    
    play music "assets/sound/bgm/093.mp3" fadein 2.0
        
        
    if flag_OfferedFeniraUnpackHelp:
        
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
        
        f "{cps=0}Try not to be too impressed.{/cps}"
        
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
            
            f "Can't bludgeon the Kitsune with a certificate."
            
    pc "What'd you get them for?"
    
    show fenira happy
    
    f "The trophies? Most of 'em are from middle school. Soccer and track, that kinda thing."
    
    show fenira neutral
    
    f "Except this one."
    
    "Fenira holds up a decently-sized golden trophy. Sculpted on it is an individual so tightly bound in a snowsuit that their joints are locked at ninety-degree angles from their body, and their features are indistinguishable."
    
    "I get a closer look at the engraving."
    
    "BEST DRESSED 2007"
    
    show fenira happy 
    
    f "I used to snowboard, but..."
    
    show fenira neutral
    
    f "I really, really... {i}really{/i} hate the cold."
    
    f "I'm a phoenix, y'know? We like warm."
    
    pc "And yet you snowboarded?"
    
    f "Yeah. It was fun. The pay-off was the temperature..."
    
    f "Anyways, it was something like minus six degrees farenheit that day. And that wasn't including wind chill. What was I supposed to wear, short shorts?"
    
    f "So, uh, I bundled up."
    
    show fenira happy
    
    f "I bundled up {i}good{/i}."
    
    f "Nagi laughed at me for weeks. Then she made this."
    
    menu:
        
        f "{cps=0}Nagi laughed at me for weeks. Then she made this.{/cps}"
        
        "'Wait, {i}Nagi{/i} made this?":
            
            show fenira happy
            
            f "You kidding? Sorry, she didn't make it - she had it made. Paid someone else to do it."
            
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
            
            f "Here's a lesson for you: no amount of padding's gonna keep a minotaurus from kicking your ass."

    f "Anyways, Nagi laughed it up, but she's cold-blooded. She had to head back inside to warm up every half hour, which meant that I did, too. At least it was nice in there."

    "Fenira places the trophy on her bed, with all the rest."
    
    f "Well, that's pretty much everything. Yeah, I'm not a very exciting packer, I know."
    
    f "Oh, that reminds me - have you seen that slime around?"
    
    pc "Viscella? I haven't. Kumiru's looking for her."
    
    f "What, she missing or something?"
    
    pc "Well, Kumiru hasn't seen her."
    
    f "Shit. You think I made her run off or something?"
    
    menu:
        
        f "{cps=0}Shit. You think I made her run off or something?{/cps}"
        
        "'Probably.'":
            
            show fenira sad
            
            f "Damnit."
            
            f "You wanna help me find her and convince her that Nagi's not actually going to drag her into her BDSM torture dungeon?"
            
        "'Probably not.'":
        
            show fenira happy
        
            f "I hope so. Still, I should probably go find her and correct our little misunderstanding. Wanna help?"
    
    pc "Sure. I don't have much else to do."
        
    show fenira vhappy
        
    f "Great!"
    
    f "Last one to find her gets to apologize!"

    menu:
        
        f "{cps=0}Last one to find her gets to apologize!{/cps}"
        
        "'Hey, wait, I never agreed to-'":
            
            $ flag_AcceptedFeniraChallenge = False
            
            hide fenira with dissolve
            
        "'You better start rehearsing.'":
            
            $ flag_AcceptedFeniraChallenge = True
            
            $ f_love += 1
            
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
        
        "Which room should I check?"
        
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
                
                f "{cps=0}Hah! I got you now! What rooms have you checked?{/cps}"
    
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
                    
                    jump intro_fenVisit_fenWins
                    
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
                    
                    jump intro_fenVisit_pcWins
            
        "Gym.":
            
            "Fenira's hot on my heels. I throw myself into the gym."
            
            jump intro_fenVisit_pcWins
    
   
label intro_fenVisit_fenWins:
    
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
    
    show fenira smirk_open
    
    f "Ji-"
    
    show viscella flustered at viscella_farright with dissolve
    
    show fenira shocked
    
    v "Nonononono!"
    
    v "Stop!"
    
    show fenira smirk_open
    
    f "Stop what? Telling [pc] how much you love-"
    
    v "Pleaseplease{i}please{i} stop!"
    
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
        
        f "{cps=0}Not until [pc] clarifies our little misunderstanding.{/cps}"
        
        "'I never agreed to that.'":
            
            if flag_AcceptedFeniraChallenge:
                
                f "You didn't? You sure about that?"
                
                show fenira smirk_open
                
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
    
    jump intro_fenVisit_end
    
label intro_fenVisit_pcWins:
    
    scene bg gym with dissolve
    
    "The gym looks empty. Not a good sign."
    
    pc "Viscella?"
    
    "No response."
    
    pc "Damn. If Fenira finds her first..."
    
    v "I-if she finds me first what?"
    
    menu:
        
        v "{cps=0}I-if she finds me first what?{/cps}"
        
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
                
                v "{cps=0}They're... not?{/cps}"
                
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
            
            v "You know, how Kumi secretly plays mobile games!"
            
            pc "What are you talking about? Fenira just wants to help clear up a misunderstanding."
            
            v "That sounds {i}super{/i} fishy!"
            
            menu:
                
                v "{cps=0}That sounds {i}super{/i} fishy!{/cps}"
                
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
    
    show fenira neutral at fenira_left with dissolve
    
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
    
    f "She doesn't even care about them."
    
    show fenira neutral
    
    f "She's weird like that."

label intro_fenVisit_end:
    
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
        
        f "{cps=0}In case the fleabag tries to chloroform you.{/cps}"
        
        "Sure, if you want.":
            
            $ f_love += 2
            
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
    
    jump intro_kam_nagi_fight
    
      
label intro_nagVisit:
    
    $ n_like += 4
    
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
    
    pc "You play the guitar?"
    
    show nagi neutral
    
    n "Nope. I'm just pretending. Makes me very popular with the boys, you know."
    
    "Nagi strums a few delicate chords, slowly picking up the pace until she's formed a nice rhythm."
    
    n "I kid. I was in a band and everything. Fenira did vocals, believe it or not. She could do some crazy things with her voice."
    
    show nagi bored
    
    n "She could also do some crazy things to a stage."
    
    n "Probably why the school shut us down..."
    
    n "Sorry, you probably didn't stop by for a history lesson. What's up?"
    
    menu:
        
        n "{cps=0}Sorry, you probably didn't stop by for a history lesson. What's up?{/cps}"
        
        "'You're pretty good.'":
            
            show nagi neutral
            
            n "Hey, thanks. Keep complimenting me and maybe you'll end up in a song one day."
            
            n "So you'd better keep it up, because I've had creative block for months now."
            
            show nagi happy
            
            n "I'll even bribe you. I think I've still got some chocolate-coated peanuts from the plane trip here." 
            
            show nagi neutral
            
            n "Think they melted, though... anyways, what's up?"
            
        "'What happened to sleeping'?":
            
            show nagi neutral
            
            n "Sorry."
            
            n "I mean, I wasn't lying. I {i}am{/i} completely wiped, but the moment my head hit the pillow I realized I wasn't gonna get any sleep. Must be all the excitement from moving to a new place."

            show nagi wink

            n "And even if it was a lame excuse to get rid of you, which it wasn't... clearly it didn't work."
            
            show nagi neutral
            
            n "Anyways, what's up?"

    pc "Just figured I'd visit some of my new roommates."
    
    n "Oh? Well, if you want me to entertain you, you might have to reciprocate and keep me company while I unpack."
    
    pc "Unpack? Unpack what? I don't see a lot of boxes..."
    
    show nagi happy
    
    n "Trust me, you will."
    
    stop music
    
    play sound "assets/sound/sfx/door_open.wav"
     
    show kamao wink at kamao_farleft with dissolve
    
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
    
    n "Our good chemistry, of course."
    
    ka "..."
    
    show kamao shocked
    
    ka "Eh?"
    
    show kamao unhappy
    
    ka "I mean, pfft. Nice try, snake lady, but I used that trick like an hour ago."
    
    ka "Right, [pc]?"
    
    $ tempvar = ""
    
    menu:
        
        "Do I play along, or..."
        
        "Come clean.":
            
            pc "Sorry, Nagi, she beat you to it."
            
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
            
            n "..."
            
        "Play along with Nagi.":
            
            pc "So, Nagi, eight o'clock tomorrow night?"
            
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
            
            $ n_love += 1
            
            show nagi neutral with dissolve:
                xalign 0.35
                ypos 0.4
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
        
        n "{cps=0}...{/cps}"
        
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
            
            ka "Aah, I remember it like it was an hour ago..."
            
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
        ypos 1.1
        
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
    
    "Nagi pulls her purse off her bed, and rifles around inside for a few moments before withdrawing a few coins, which she drops in Kamao's hand. The kistune gives me a grin, and pops out the door."
    
    hide kamao with dissolve
    
    stop music fadeout 2.0
    
    show nagi neutral at nagi_center with move

    n "Well, then."
    
    n "She's..."
    
    play music "assets/sound/bgm/068.mp3" fadein 2.0
    
    
    menu:
        
        n "{cps=0}She's...{/cps}"
        
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
                
                n "{cps=0}Wait. Are you serious?{/cps}"
                
                "'Dead serious.'":
                    
                    n "I mean, whatever floats your boat."
                    
                    n "I wouldn't tell her that, though. If you think she won't leave you alone now..."
                    
                "'Pfft.'":
                    
                    show nagi happy
                    
                    n "You had me worried for a second."
            
    
    show nagi neutral
    
    n "Anyways, what were we talking about?"
    
    n "Oh, right. Boxes."
    
    n "Talking all about boxes."
    
    n "..."
    
    show nagi bored
    
    n "Wow. See what happens when I haven't unpacked any of my conversation starters? It's not pretty."

    n "At least the kitsune gave us something to talk about."
    
    show nagi neutral
    
    n "Where are you from, anyways?"
    
    pc "Uh..."
    
    "She seems nice enough, but I can't take the risk."
    
    menu:
        
        "{cps=0}She seems nice enough, but I can't take the risk.{/cps}"
        
        "Dodge the question.":
            
            pc "Oh, you know. Around. How about you?"
            
            n "Around, huh? I've heard it was a nice place. A little quaint, though. You fly here from Around?"
    
            pc "Hah."
            
            n "I try. Not often I have people dodge the question when I ask them where they're from, though. Must be some interesting secret you're holding on to, huh?"
            
            pc "Er..."
            
            show nagi happy
            
            n "Don't worry, I won't prod. More fun if I figure it out on my own, right?"
                    
        "Make up a name at random.":
            
            pc "Where I'm from? Oh, I'm from a little place called, ah, Skellow."
            
            n "Skellow? Where's that?"
            
            pc "Um. Northeast of here, I guess. It's a really tiny town, so... easy to miss."
            
            n "Hey, if you say so. I don't know much about the area, so you could probably make up a totally random name and I'd believe you."
            
            pc "Hah... hah. Crazy."
            
            n "I know, right?"
            
    n "Well, I hope you at least know what you've gotten yourself into."
    
    show nagi bored
    
    n "Not that it's your fault. Bondhouses aren't normally supposed to be this lopsided. There's five of us chimera - for both of our sakes there should be another human or two."

    show nagi confident

    n "...But you're probably the sort who enjoys having a group of chimera fighting over you, huh?"
    
    menu:
        
        n "{cps=0}...But you're probably the sort who enjoys having a group of chimera fighting over you, huh?{/cps}"
        
        "'Well...'":
            
            n "Nailed it."
            
            n "Nothing to be ashamed of, it's a pretty common fantasy, y'know?"
            
            pc "You sure like teasing, huh?"
            
        "'N-no...'":
            
            show nagi teasing
            
            n "You blushing? You're totally blushing."
            
            pc "Well, yeah. You're teasing me."
            
    show nagi wink
            
    n "Oh, you haven't seen anything yet."
    
    show nagi neutral

    n "But hey, enough of that. Now I really {i}am{/i} exhausted. I'm gonna get some sleep. Wanna join me?"
    
    menu:
        
        n "{cps=0}But hey, enough of that. Now I really {i}am{/i} exhausted. I'm gonna get some sleep. Wanna join me?{/cps}"
        
        "'Who wouldn't?'":
            
            $ n_love += 1
            
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
            
            $ n_love += 1
            
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
    
    jump intro_kam_nagi_fight
        
label intro_kamVisit:
    
    $ ka_like += 4
    
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
        
        ka "{cps=0}Fu... fu... fu...{/cps}"
        
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
    
    pc "How'd you manage to get your room so messy? Didn't you just move in an hour ago?"
    
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
    
    show kamao vhappy
    
    ka "One time, my dad called in a hazmat team because I wouldn't clean my room!"
    
    pc "Uh..."
    
    ka "It was hilarious!"
    
    show kamao bored
    
    ka "Until I got the whole lecture on mishandling dangerous biohazards..."
    
    pc "..."
    
    show kamao smirk
    
    ka "Pff, I'm just kidding."
    
    ka "..."
    
    show kamao neutral
    
    ka "Uh, mostly."
    
    show kamao happy
    
    ka "Anyways, enough about me! Tell me about you!"
    
    show kamao embarrassed
    
    ka "Actually, for now, just tell me why you're in my bedroom."
    
    menu:
        
        ka "{cps=0}Actually, for now, just tell me why you're in my bedroom.{/cps}"
        
        "Ask about her offer.":
            
            ka "My offer... offer..."
            
            ka "..."
            
            show kamao confused
            
            ka "What offer?"
            
            pc "You don't remember?"
            
            #FLASHBACK#
            
            scene bg pBedroom 
            
            show kamao winkblush at kamao_right
            
            show kumiru unamused at kumiru_left
            
            show viscella neutral at viscella_farleft
            
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
                
                ka "{cps=0}Alright. It's my first time. Be gentle.{/cps}"
                
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
                        
                        ka "{cps=0}Th-three pets! Max! I'm not ready for any more than that!{/cps}"
                        
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
                            
                            $ ka_love += 2
                            
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
                            
                            jump intro_kam_nagi_fight
            
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
        
        ka "{cps=0}Before you ask, you can earn 100 K-bux by whispering dirty stuff into my ear.{/cps}"
        
        "Whisper 'dirty stuff' into her ear.":
            
            show kamao shockblush
            
            "You lean in close. Kamao freezes, her breath caught in her throat, as you whisper something into her ear."
            
            pc "Dirty stuff."
            
            ka "..."                              
            
            show kamao bored
            
            ka "Smartass."
            
            show kamao smirk
            
            ka "Oh well. K-bux get."
                                           
        "'How many do I get for doing dirty stuff to you?'":
            
            $ ka_love += 1
            
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
        
        ka "{cps=0}And I do mean {i}service{/i}.{/cps}"
        
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
                
                ka "{cps=0}Barely legal.{/cps}"
                
                "'What's the rush?'":
                    
                    show kamao confused
                    
                    ka "Huh? Whaddya mean?"
                    
                    pc "You're eighteen. You've got plenty of time. No need to rush into that kinda thing, you know?"
                    
                    ka "You kidding? I don't wanna get laid because of societal pressures or anything."
                    
                    show kamao horny
                    
                    ka "I just want a big, fat-"
                    
                    pc "Alright, I get it."
                    
                    ka "Oooh, I {i}bet{/i} you got it."
                    
                    pc "..."
                    
                "'Well. Good luck.":
                    
                    show kamao bored
                    
                    ka "Thanks, but I want sex, not sympathy."
                    
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
        
        ka "{cps=0}Okay, maybe just the dick lust.{/cps}"
        
        "'I find that hard to believe.'":
            
            $ ka_love += 2
            
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
            
        "'Well, at least you're honest.'":
            
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
    
    ka "Oh my god, it's so cool. They've got their own movie theatre. I'm not kidding."
    
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
            
    jump intro_kam_nagi_fight
    
    "*TEMPEND*"
    
    $ renpy.pause(20.0, hard = True)

    
            
