
    
    
    label ch2_scene01:
        
        python:
            flag_ScaredViscella = True
            flag_RememberedAllise = False
        
        play sound "assets/sound/sfx/morning.ogg"
        
        $ renpy.pause(3.0)
        
        scene bg pBedroom with Dissolve(5.0)
        
        "..."
        
        "I don't recognize the ceiling. It takes me a full minute to realize I'm not dreaming."
        
        "Eventually, the events of the previous day come flooding back to me."
        
        "Unfortunately... that's about all that comes back. I let out a long sigh. Looks like it's gonna take more than a full night's rest before I solve this identity crisis."
        
        d_un "Is something the matter?"
        
        pc "No, it's... it's..."
        
        pc "..."
        
        menu:
            
            "React like a normal human being.":
                
                "I almost jump out of my bed as my head swivels around to the source of the voice."
                
            "Pretend I heard nothing and go back to sleep.":
                
                "I'm hearing things. Clearly hearing things. I pull the covers back up, roll onto my side, and close my eyes."
        
                "Try as I might, however, I can not shake the feeling of being watched. I bolt upright in bed."
                
        show dravenia neutral at dravenia_center with dissolve
        
        d_un "..."
        
        show dravenia confused
        
        d_un "Are you sure nothing is wrong?"
        
        play music "assets/sound/bgm/093.mp3" fadein 5.0
        
        pc "What the- who are you, and what are you doing in my room?!"
        
        d_un "Oh. Have you not been briefed?"
        
        pc "Briefed? What?"

        "I rub my eyes, but the tall woman in front of me makes no signs of disappearing."
        
        show dravenia at dravenia_full with dissolve
        
        "She's... tall. Taller than me, at least. She has long, leathery wings and scales covering a decent portion of her body. That's mostly guesswork, though - the suit makes it hard to tell."
        
        show dravenia smug at dravenia_center with dissolve
        
        d_un "I see. I suspected you were informed, but clearly that is not the case."
        
        d_un "No doubt you are unsettled by the presence of someone such as I watching over you in your sleep, am I correct?"
        
        pc "Uh... yes."
        
        d_un "Of course. For all you know, I could be a dangerous criminal sent here to snuff out your illustrious life."
        
        pc "..."
        
        d_un "But from today onwards, that concern will be a thing of the past."
        
        show dravenia happy
        
        d "After all, what Hellguard would allow harm to come to their patron?"
        
        pc "..."
        
        d "..."
        
        pc "...What?"
        
        show dravenia smug
        
        d "Confused? Understandable. For many, the prospect of a Hellguard guardian is but a distant dream. But I can assure you, this is no prank."
        
        menu:
            
            
            "'I... have no idea what you're talking about.'":
       
                d "Then I suppose I shall put it simply."
                
                d "An anonymous benefactor has seen fit to gift you with a Hellguard contract."
                
                d "I shall do my best to live up to your expectations."
                
                pc "What expectations? I don't even know what a Hellguard is."
                
                d "A Hellguard, of course, is... is..."
                
        
            "'Ah. I understand. Of course.'":
                
                d "Putting the pieces together already? I can respect your early-morning processing abilities, sir."
                
                pc "And by that I mean I have {i}absolutely no idea what is going on.{/i}"
                
                pc "First off, what the hell's a Hellguard?"
                
                d "A Hellguard, of course, is... is..."
                

                    
        d "..."
        
        pc "..."
        
        show dravenia shocked
        
        play sound "assets/sound/sfx/vinylscratch.wav"
        
        stop music
        
        d "Ex... excuse me?"
        
        d "Did you say you... you don't know what a Hellguard is?"
        
        pc "Uh, no."
        
        pc "Is that bad?"
        
        d "W-well, no, but... um... you know. 'Per Portas Inferi?'"
        
        d "'Through the gates of Hell?'"
        
        d "You... you aren't familiar with it?"
        
        menu:
            
            "'I can't say I am...'":
                
                d "I... see..."
                
                "She clears her throat."
                
                show dravenia neutral
                
                d "Sir, would you please verify that you are, indeed, unfamiliar with the Hellguard?"
        
                pc "Uh... how do you want me to do that?"
                
                d "..."
                
                d "So it's not a joke?"
                
                d "You are truly, honestly, one hundred percent confused."
                
                d "Sir, with all due respect, have you been living under a rock?"
                
                pc "Something like that..."
                
                show dravenia smug
                
                d "Ah. Forgive me."
                
                pc "Forgive you?"
                
                d "Of course. It makes perfect sense that a Hellguard would be hired to protect an innocent gentleman with little practical knowledge of the outside world."
                
                pc "H-hey, now..."
            
                show dravenia happy
                
                d "Please, sir. It is nothing to be embarrassed about. But I suppose I should explain my purpose to you, no?"
        
            "'O-oh, yeah, totally. I was just, uh, testing you.' (Lie)":
                
                show dravenia smug
                
                d "Ah, but of course."
                
                d "Can I be surprised that a newly minted patron would test the composure of his guardian? Of course not." 
        
                pc "R-right. Hah. Ahah."
                
                d "After all, if someone was so ignorant to be unaware of the existence of the Hellguard, I would likely be forced to ask something along the lines of 'have you been living under a rock?' But, thankfully, that is not the case."
                
                pc "Yeah..."
                
                show dravenia happy
                
                d "Who would fail to recognize the most illustrious escort service in the world?!"
                
                pc "W-wait, you're an {i}escort{/i}? Like, an {i}escort{/i} escort?!"
                
                d "..."
                
                show dravenia smug
                
                d "Forgive me, sir. I merely sought to reply to your test with a test of my own, and it seems you have fallen into my trap."

                d "You see, the Hellguard are not an escort service."
                
                d "Although we do, on occasion, escort."
                
                show dravenia embarrassed
                
                d "A-as in an {i}armoured{/i} escort. Convoys and the like. Please don't misunderstand."
                
                pc "Er... right. Sorry."
                
                show dravenia smug
                
                d "Do not be concerned, sir. I, too, understand the embarrassment of being ignorant of common knowledge."
                
                d "For example, I thought the moon truly was made of cheese until the age of ten."
                
                d "..."
                
                d "That was a joke, sir, and entirely fabricated. I did not believe the moon was made of cheese."
                
                pc "Uh-huh."
                
                d "Rather, I was of the opinion it was actually the egg of a large beast."
                
                d "Regardless, please allow me to explain my purpose."
        
        play music "assets/sound/bgm/093.mp3" fadein 3.0
        
        show dravenia happy
        
        d "As previously stated, I am a Hellguard."
        
        d "Our origins go back hundreds of years, when the first..."
        
        d "..."
        
        show dravenia smug
        
        d "Ah. Forgive me. Would you like the long or the short of it?"
        
        "She seems quite eager to talk my ear off..."
        
        menu:
            
            "'I've got time.'":
                
                $ d_like += draAff(1)
                
                show dravenia happy
                
                d "Thank you, sir. I shall do my utmost not to bore."
                
                show dravenia neutral
                
                d "As you know, the ancient relationship between human and chimera has been tumultuous, and oft violent."
                
                d "Almost three centuries ago, humanity neared extinction due to chimera decadence."
                
                show dravenia closed
                
                d "Humans were treated as cattle. Whether to satisfy their wives or to produce and raise offspring, men were enslaved en masse."
                
                d "The women weren't as lucky. They were seen only as competition, lesser in every way to their chimera counterparts. The atrocities were endless, and before long, human men outnumbered their women three to one."
                
                show dravenia neutral
                
                d "Our chimeran foremothers lacked foresight. They failed to understand the consequences of their actions. Our species requires humans to survive, after all - both male and female. Your extinction is our extinction."
                
                d "But not all of them were blind."
                
                show dravenia happy
                
                d "In the opening years of the seventeenth century, a collection of chimera noblewomen met in secret in a small inn in Paris."
                
                d "And thus began one of the largest revolts in our people's collective history."
                
                d "You see, human rebellions were beginning to fizzle out. Their numbers were dwindling, and open warfare became impossible; before the advent of firearms, a single powerful chimera was more than a match for a dozen human warriors."
                
                d "But when the monarchies of the old world were set upon by not only a conglomeration of the surviving humans but like-minded chimera, as well, things become complicated."
                
                show dravenia neutral
                
                d "Chimera society was split in half. On one hand, there were those that clung to the old ways - taking mates by force and keeping humans shackled to their whims."
                
                d "On the other hand, some chimera saw change as necessary. Some saw that the old ways were unsustainable and would inveitably signal a slow death for the species."
                
                d "Others were ruled by their heart. Every chimera family was dotted with humans - whether fathers, husbands, or in-laws."
                
                d "Those who had bonded with their human sisters-in-law had particular reason to oppose the status quo, when human women could be put to death for the smallest trivialities."

                d "Regardless, human and chimera fought side-by-side. Prominent human figureheads would rise in rank and reputation... only to be cut down or captured and subjected to far worse."
                
                d "Can we blame them? No matter how powerful the human, there is little they can do to protect them from the breath of a dragon or the magic of a lich."
                
                show dravenia happy
                
                d "Unless, they realized, if they were to fight fire with fire. Do you see where I am going with this?"
                
                pc "I think so..."
                
                d "Well, before long, those prominent figureheads had entire squadrons of elite chimera bodyguards."
                
                d "These chimera were trained specifically to deal with any manner of foe, whether combative or subversive."
                
                d "For every succubus sent to tempt a man or woman to betray their cause, a dreamcatcher was ready to revert the damage."
                
                d "For every mantis sent to drive a dagger through a target's heart, an orc was ready to jump in front of the blade."
                
                d "For every sorceress primed to incinerate a hideout, a mage was taught to raise a protective shield."
                
                d "Would you like to guess what these trained individuals were called?"
                
                menu:
                    
                    "'Hellguard?'":
                        
                        show dravenia smug
                        
                        d "An excellent deduction, and almost completely accurate." 
                        
                    "'Ass-kickers?'":
                        
                        show dravenia smug
                        
                        d "Not quite, but I admit your suggestion carries a certain charm."
                        
                show dravenia happy
                        
                d "At the time, they were called the Order of the Sworn, you see."
                        
                d "After the revolt had concluded, they recreated themselves under the banner of the Hellguard."
                    
                d "Elite bodyguards, created to even the playing field between humans and chimera and give the former a fighting chance."
                    
                d "That is our duty."
                        
                
            "'I'll just go with the short version for now.'":
                
                d "..."
                
                d "Very well. I shall accept your challenge to deliver my purpose in a clear and concise matter."
                
                d "Essentially, back in... "
                   
                d "..."
                       
                d "Once upon a..."
                                  
                d "..."
                                  
                d "At the dawn of..."
                
                d "..."
                
                show dravenia sad
                
                d "Ah. The task you have asked of me is no easy one."
                
                show dravenia confident
                
                d "But I shall not surrender! My pride as a Hellguard depends on it!"
                
                show dravenia neutral
                
                d "Let's see..."
                
                d "There is a huge gap of ability between humans and chimera."
                
                d "Put an unarmed human and an unarmed chimera into a pit and force them to battle... the chimera will win, nine times out of ten."
                
                d "That's where the Hellguard come in."
                
                d "Put an unarmed human in a pit with a chimera, and give that human a Hellguard? Well..."
                
                show dravenia happy
                
                d "To say you've reversed the odds would be what I like to call a 'colossal understatement.'"
                
        pc "So... you're a bodyguard?"
                
        d "The term 'bodyguard' does not do the Hellguard name justice. We are trained from adolescence to protect our patron with our lives. We undergo extensive training in all manner of firearms and martial arts."
        
        d "We have a working knowledge of nearly every chimera species's strengths and weaknesses, can resist psionic attacks and other mind-altering affects, and possess the survival knowledge to thrive in all but the most inhospitable of environments."
        
        d "Most importantly, we are always on-duty. Hellguard do not have 'off-time.' We work to ensure your safety twenty-four hours a day, seven days a week, three-hundred and sixty five days a year."
        
        d "Those of us who serve a lifetime contract will protect you until the day you die."
        
        pc "...Huh."
        
        show dravenia smug
        
        d "Impressive, no? You were not gifted with a lifetime contract, unfortunately. But the day you die will {i}not{/i} fall under the upcoming year. I swear it on my father's grave."
        
        menu:
            
            "'That's... comforting.'":
                
                d "Hellguard are valued for providing peace of mind. I am glad to already be fulfilling that portion of my duties."
            
                d "Not that my other duties or skills are any less important."
            
            "'We'll see about that.'":
                
                show dravenia confident
                
                d "Do you doubt my abilities, sir?"
                
                
        
        show dravenia confident
        
        d "It is no boast to state I could keep a cow alive in the den of a ravenous dragon."
                
        d "..."
                
        show dravenia neutral
                
        d "Well, you get the idea."
        
        pc "Speaking of which, are you...?"
        
        d "A dragon? Yes. Put your mind at ease, sir - my hoarding instincts have been trained out of me. I carry with me nothing but the clothes on my back."
         
        menu:
            
            "'Hoarding instincts?'":
                
                
                d "Yes. Dragons hoard. It's a habit of sorts."
                
                pc "Really? What did you hoard?"
                
                d "Er..."
                
                show dravenia embarrassed
                
                d "Fantasy books."
                
                d "N-not that there's anything wrong with that."
                
                "She sounds a little uncertain."
                        
            "'You're a {i}dragon{/i}?! That's so cool! Can you breathe fire?'":
                
                $ d_love += draAff(1)
                
                show dravenia lovestruck
                
                d "A-ah? Er, um..."
                
                pc "What?"
                
                d "F-Forgive me. I was not expecting the sudden outburst of enthusiasm."
                
                d "Breathing fire is... yes, it is something I am capable of."
                
                show dravenia neutral
                
                d "Though it is unlikely you shall get to see it often."
                
                d "I conducted a thorough analysis of the building before I entered, and discovered to my dissapointment that it is... well, flammable."
                
        d "Anyways, did you have any questions?"
        
        menu:
            
            "'Yes, actually...'":
                
                show dravenia happy
                
                d "Fire away, sir."
                
                pc "Alright... well, first off, why me?"
                
                show dravenia smug
                
                d "Worry not, your contract was only rated a D."
                
                pc "What does that mean?"
                
                show dravenia happy
                
                d "Your life is in no immediate danger."
                
                show dravenia confused
                
                d "I was merely instructed to, and I quote, 'Keep him from getting mobbed by a group of desperate virgins.'"
                
                show dravenia neutral
                
                d "I was also alerted to one individual in particular who is likely to attempt to infiltrate your room after sundown."
                
                "That would probably be Kamao..."
                
                pc "Are you okay with that?"
                
                show dravenia confused
                
                d "What do you mean?"
                
                pc "Well, it doesn't sound particularly thrilling..."
                
                show dravenia happy
                
                d "Nonsense. It would be my honour to protect your dignity. Who knows, perhaps they will even get desperate enough to make an attempt on your life?"
                
                show dravenia confident
                
                d "Then I could show you what I'm capable of."
                
                pc "I... see."
                
                pc "I don't know if I can pay you."
                
                show dravenia smug
                
                d "My services are a gift, remember? It's already handled."
                
                pc "A gift from who?"
                
                show dravenia neutral
                
                d "I am unsure if they wish to remain anonymous or not."
                
                d "For now, I must regretfully keep my lips sealed on the identity of your mysterious benefactor."
                
                pc "And... you're sure it's me?"
                
                d "What do you mean?"
                
                pc "Well, are you sure it's me you're supposed to protect?"
                
                d "Of course. You are [pc], correct?"
                
                "You nod."
                
                show dravenia happy
                
                d "I am... relieved. Making a mistake this far into the procedure would have been rather embarrassing."
                
                d "But it seems no such mistake has been made. I look forward to working with you, sir."
                
                
            "'No, that's about all I need to know.'":
                
                show dravenia happy
                
                d "Understood, sir. I look forward to working with you."
                
        menu:
            
            "'I guess I look forward to working with you, too.'":
                
                d "Good to hear, sir."
                
            "'You can stop calling me 'sir', you know.'":
                
                d "Yes, sir."
                
            "'Uh, thanks. Could you let me get dressed, now?'":
                
                show dravenia embarrassed
                
                d "O-oh, of course. Forgive me."
                
        stop music
        
        show dravenia neutral
        
        play sound "assets/sound/sfx/knock.ogg"
        
        d "..."
        
        d "Are you expecting anyone?"
        
        pc "I wasn't even expecting you..."
        
        d "Hm..."
        
        show dravenia with MoveTransition(0.5):
            xalign -3.0
            xzoom 1.0
        
        show dravenia with dissolve:
            xalign -3.0
            xzoom -1.0
        
        "Dravenia quickly and silently crosses the room, pressing her back up against the wall directly beside the door. She gives you a stoic nod."
        
        menu:
            
            "'Uh. Come in?'":
                
                "The door flies open."
                
            "'You may not want to come in...'":
                
                "The door flies open anyways."
                
        play sound "assets/sound/sfx/door_open.wav"
          
        play music "assets/sound/bgm/097.mp3"
          
        ka "Hayo!!"
        
        $ kaFlip()
        
        show kamao vhappy at kamao_left
    
        show kamao:
            xalign -3.0
        
        show kamao with MoveTransition(0.2):
            xalign 0.0
            
        show kamao shocked
        
        ka "Wha-"
        
        show kamao:
            yalign -0.5
        show dravenia closed:
            yalign -0.3
        with MoveTransition(0.3)
        
        play sound "assets/sound/sfx/body_hit.wav"
        
        show kamao pained
        with vpunch
        
        ka "Ack!"
        
        ka "What the hell?!"
                
        show dravenia neutral
                
        d "You must be the one I was warned about."
        
        ka "I dunno what you're talking about! Lemme go!"
        
        ka "Owowowow! Not the arm, not the arm!"
        
        ka "The hell is this, WWE?"
        
        show dravenia confused
        
        d "Is this... the best you can do?"
        
        ka "What do I look like, Hulk Hogan? I'm basically a paperweight with legs!"
        
        show dravenia neutral at dravenia_left with MoveTransition(0.5)
        
        d "I see. That is... dissapointing..."
          
        ka "I can see the light. Father? Mother? Is that you? Since when were you dead?!"
        
        d "..."
        
        show kamao with MoveTransition(0.5):
            yalign -0.4
            xalign 1.0
        
        ka "Ow."
        
        show kamao with MoveTransition(0.5):
            yalign -0.3
            xalign 2.0
            
        ka "Very ow."
        
        show kamao with MoveTransition(0.5):
            yalign -0.2
        
        ka "AhahaOW."
        
        show kamao with MoveTransition(0.5):
            yalign -0.1
        
        ka "I AM DYING."
        
        show kamao neutral at kamao_right with dissolve
        
        ka "Okay, better."
        
        d "You recover quickly."
        
        show kamao vhappy
        
        ka "Why thank y-"
        
        show kamao shocked
        
        ka "Dragon."
        
        ka "Holy shit."
        
        ka "Dragon."
        
        ka "Why is there a dragon in my house and why is she putting me in headlocks."
        
        d "It's not your house. And that was an armlock."
        
        ka "{i}It talks.{/i}"
        
        d "Uh-huh. May I ask you what you're doing?"
        
        show kamao vhappy
        
        ka "Tending to my boyfriend's morning wood, of course!"
        
        d "..."
        
        ka "..."
        
        d "Definitely dangerous."
        
        show dravenia at dravenia_center with dissolve
        
        ka "What was tha-"
        
        show kamao pained
        
        ka "OWOWOWOW!"
        
        show dravenia:
            xalign -10.0
            
        show kamao:
            xalign -4.0
            
        with MoveTransition(1.0)
            
        ka "NOT THE EAR NOT THE-"
        
        show kamao with MoveTransition(0.2):
            xalign -5.0
            
        play sound "assets/sound/sfx/door_close.wav"
        
        stop music fadeout 1.0

        "The door closes."
                
        play music "assets/sound/bgm/062.mp3" fadein 1.0
        
        "I hear some vocal complaints out in the hallway, but before long they fade away."
        
        "Glancing at my alarm clock, it appears to be nine. Well, at least now I can get out of bed."
        
        show black with dissolve
        
        "I get changed, and head downstairs."
        
        jump ch2_scene02
        
    label ch2_scene02:
        
        # Maybe have viscella up instead?
        
        scene bg kitchen with wipeleft
        
        "It's quiet all the way to the bottom floor, but I spot the first familiar face in the kitchen."
        
        show viscella neutral at viscella_center with dissolve
        
        "It's Viscella. She hasn't noticed me, yet - she's looking out the window, sipping straight from a carton of orange juice."
        
        "I could say hello. Or..."
        
        menu:
            
            "Say hello.":
                
                $ flag_ScaredViscella = False
                
                pc "Morning, Viscella."
                
                show viscella flustered
                
                v "Gwawawa!"
                
                "Viscella jumps nearly a foot into the air, the carton slipping from her fingers and spilling onto the floor."
                
                show viscella neutral
                
                "The two of us stand in silence as we watch the mess spread."
                
                v "Ah..."
                        
                pc "Er... sorry."
                                 
                show viscella embarrassed
                                 
                v "I-It's okay! I'm the one who should be sorry!"
                
                pc "Should I get a mop, or...?"
                
                v "Huh?"
                
                show viscella confused
                
                v "Why would we need a mop?"
                
                pc "Er... you know... the juice..."
                
                "Viscella steps in the spill. Slowly but surely, the liquid begins to recede into her foot, tinting it with a faint orange hue."
                
                pc "Oh. Right."
                
                show viscella happy
                
                v "It's a good thing I'm as good at cleaning up messes as I am at making them."
                
                v "..."
                
                show viscella neutral
                
                v "Actually, I'm a lot better at making them."
                
                menu:
                    
                    "'I'm sure it's not that bad.'":
                        
                        $ v_like += visAff(1)
                        
                        v "..."
                        
                        v "One time I spilled an entire jerry can of gasoline on my mom's bed and then set it on fire."
                        
                        v "{i}By accident.{/i}"
                        
                        pc "..."
                        
                        v "I know what you're thinking. But I'm serious. I was five. I didn't even know gasoline was flammable."
                        
                    "'Yikes.'":
                        
                        v "Yeah..."
                        
                        v "I started doing this thing where I'd put a quarter in a jar every time I did something wrong, and take a quarter out when I did something right."
                        
                        pc "Did you fill it?"
                        
                        v "Never."
                        
                        pc "Oh, that's-"
                        
                        v "I kept breaking it before I could."
                        
                        pc "..."
                        
                        pc "Huh."
                        
                        v "Yeah."
                        
                v "There's a reason Kumiru doesn't let me near her computer..."
                
                v "And she gets really scary when I do."
                    
                pc "'Kumiru? Scary?'"
                        
                v "Yeah. {i}Really scary.{/i}"
                        
                v "Like, one time she was rebuilding it, and..."
                        
                v "Ahem."
                        
                show viscella vhappy
                        
                v "'Please, Viscella, {i}do{/i} continue dripping {i}all over{/i} the six hundred dollar CPU.'"
                        
                v "'Then maybe we'll find out what happens when you add three litres of hot sauce to a slime's reconstructive bath.'" 
                        
                v "..."
                        
                show viscella scared
                        
                v "Pain. Pain is what happens."
                
                v "S-sorry. You got me a little sidetracked thinking about terrifying things."
                
                show viscella happy
                
                v "I know! Let's talk about not-terrifying things! Things like... like..."
                
                d "Ah, there you are. You had me worried."
                
                show viscella vhappy
                
                v "Like dragons!"
                
                show viscella confused
                
                v "Wait, that doesn't make sense. Dragons aren't just terrifying, they're {i}horrifying{/i}. I wonder what made me say tha..."
            
                v "Tha... aah..."
                
            "Scare her.":
                
                $ flag_ScaredViscella = True
                
                "An opportunity like this isn't something I can pass up. I carefully tiptoe forward."
                
                "The slime remains completely oblivious to my approach."
                
                "Eventually, I am less than a foot away from my target. She's still gazing absently out the window, taking the occasional drink of juice."
                
                "I lean forward, until I'm right beside her ear."
                
                pc "Morning."
                
                show viscella shocked
                
                "She barely moves. Looks like she saw me coming."
                
                pc "Well, I tried."
                
                v "..."
                
                pc "Viscella?"
                
                "She continues to stare out the window. I notice that she's no longer drinking, and after a few moments I realize she seems to have frozen solid."
                
                pc "Um... Viscella?"
                
                v "..."
                
                show viscella with MoveTransition(0.1):
                    ypos 0.8
                
                show viscella puddle_scared at viscella_puddle_center with Dissolve(0.3)
                
                "Just like that, she seems to lose all consistency, and collapses into a puddle with a wet {i}fwap{/i}."
                
                "I manage to jump backwards just in time to avoid getting gooed."
                
                pc "V-Viscella?"
                
                "She gives a little whimper. The carton she was holding now floats around inside her, spilling a cloud of orange mist into the otherwise turquoise goop."
                
                pc "Are you okay?"
                
                show viscella puddle_neutral
                
                v "I am at your mercy."
                
                v "Do what needs to be done."
                
                pc "..."
                
                pc "What?"
                
                v "You're an assassin, aren't you?"
                
                v "An assassin sent to kill me."
                
                v "Maybe a ninja. That's how you got behind me, right? Using the forbidden technique of... {i}Shining Terror Quiet Step{/i}."
                
                v "But little did you know..."
                
                v "I, too, have a secret technique."
                
                show viscella puddle_happy
                
                v "I call it... {i}Amorphous... Amorphous...{/i}"
            
                show viscella puddle_neutral
            
                v "..."
                
                show viscella puddle_happy
                
                v "{i}Amorphous Blob.{/i}"
                
                menu:
                    
                    "'Should I get a doctor?'":
                        
                        show viscella puddle_neutral
                        
                        v "N-no. This happens on occasion."
                        
                        v "On rare occasion."
                        
                        v "Yes, very rarely, of course."
                        
                        v "It's not a regular thing."
                        
                        v "..."
                        
                        v "Yes."
                        
                    "'Tch. I underestimated you.'":
                    
                        $ v_love += visAff(1)
                    
                        v "Hehe! Never underestimate your opponent!"
                        
                        v "..."
                        
                        show viscella puddle_neutral
                        
                        v "You know, normally I would be embarrassed half to death by now, but I'm not."
                        
                        v "That's weird."
                        
                        v "I still kinda feel like hiding in a bucket somewhere, though..."
                        
                "As you watch, the pile of goop rises off the ground and soon begins, once again, to take on a human appearance."
                
                show viscella embarrassed at viscella_center with dissolve
        
                v "A-anyways, where were we?"
                
                d "Ah, there you are. You had me worried."
                
        show viscella shocked at viscella_right with move
                
        show dravenia neutral behind viscella at dravenia_left with dissolve
                
        v "..."
                
        show viscella vhappy
                
        v "Oh, there's a dragon."
                
        v "In the house."
                
        d "..."
                
        pc "..."
                
        v "..."
                
        show viscella with MoveTransition(0.1):
                    ypos 0.8
                
        show viscella puddle_scared at viscella_puddle_right with Dissolve(0.3)
        
        if  flag_ScaredViscella:
            
            d "..."
            
            pc "There she goes again."
            
            d "Ah, forgive me. I did not mean to startle you."
              
        else:
            
            pc "What the?!"
            
            d "It seems I have startled her. Deconstituting is a slime's natural reaction to a shock."
            
            pc "That seems... unusual..."
            
            d "Indeed. I believe the idea is to convince potential attackers they are merely an inate puddle of water... though the effectiveness of this tactic is debatable."
            
            d "Regardless, I apologize. I did not mean to startle you."
            
        v "Didn't... mean?"
            
        v "You're... you're not going to play catch with my core?"
          
        d "Of course not."
        
        v "I knew it! You're going to play baseball with it!"
        
        v "Someone help!"
        
        d "Would you calm down? I mean no harm."
        
        v "..."
        
        show viscella scared at viscella_right with dissolve
        
        d "..."
        
        v "Please be gentle..."
        
        "Dravenia glances to me for support."
        
        menu:
            
            "'Viscella, she's not gonna hurt you.'":
                
                v "That's what they all say!"
                
                d "He speaks the truth. My job is preventing pain, not dealing it."
                
            "'In her defense, you {i}do{/i} look deadly.'":
                
                show dravenia smug
                
                d "Of course."
                
                v "..."
                
                show dravenia neutral
                
                d "Er, not that you are in any danger of finding out."
                
        d "Unless under that incompetent and adorable exterior you harbour a malicious heart."
                
        d "Er, core."
                
        show viscella flustered
                
        v "I-I'm not incompetent!"

        if flag_ScaredViscella == False:
            
            "That's not what she was telling me a minute ago..."
            
        show viscella shocked
            
        d "Forgive me. Just adorable, then."
        
        show viscella flustered
        
        v "Why is she being nice to me?!"
        
        show dravenia confused
        
        d "Um...?"
        
        pc "I'm not a hundred percent sure, but I think she had some past trauma involving a dragon."
        
        show viscella scared
        
        v "Past trauma? It wasn't just trauma, it was..."
        
        show viscella confused
        
        v "..."
        
        v "On second thought, trauma is pretty accurate."
        
        show viscella flustered
        
        show dravenia neutral
        
        v "But still, she's a dragon! Aren't you terrified out of your mind right now?!"
        
        menu:
            
            "'Uh... no?'":
                
                show viscella scared
                
                v "You fool! She'll eat your heart if you let your guard down!"
                
                d "I will?"
                
                show viscella flustered
                
                v "You will!"
            
            
            "'Yeah, completely petrified.'":
                
                show viscella confident
                
                v "Hah!"
                
                v "Your games end here, dragon! We know what you're capable of!"
                
                pc "I... wasn't serious."
                
                show viscella shocked
                
                v "Wh-what?!"
                
                show viscella flustered
                
                v "I've been played!"
                
        pc "Listen, Viscella... I think you may be overreacting."
        
        show viscella shocked
        
        v "Me? Overreacting?"
        
        show viscella angry
        
        v "She's a dragon!"
        
        v "Listen, losing your memories is no excuse to forget how dangerous dragons are!"
        
        v "They're like tanks! With built-in flamethrowers!"
        
        show viscella vangry
        
        v "And they're super mean!"
        
        v "And they toss their trash in you!"
        
        show viscella sad
        
        v "And gang up on you and call you worthless and a waste of space!"
        
        v "And... and..."
        
        show dravenia closed
        
        d "..."
        
        v "..."
        
        show dravenia neutral
        
        d "Would you repeat that?"
        
        v "I don't even want to think about it..."
        
        d "Not that part. I am speaking of the brief mention of 'lost memories.'"
        
        v "What? I never said [pc] lost his memories."
        
        show viscella shocked
        
        v "..."
        
        show viscella sad
        
        v "I... I really am a waste of space..."
        
        menu:
            
            "'No, you're not.'":
                
                $ v_like += visAff(1)
                
                v "But... I just said something stupid..."
                
                pc "It's not like it's a big secret or anything."
                
                d "You lost your memories?"
                
            "Pat her head.":
                
                $ v_like += visAff(1)
                
                $ v_love += visAff(2)
                
                "I take a few steps forward, and pat Viscella on the head with a wet {i}splat{/i}."
                
                pc "You're not a waste of space."
                
                show viscella embarrassed
                
                "She almost jumps at the contact."

                v "Wh-wh-what are you doing?!"
                
                pc "Huh? Is something wrong?"
                
                "I stop patting her, shaking the slime from my hand."
                
                show viscella lovestruck
                
                v "Um... n-no."
                
                d "I am terribly sorry to interrupt, but I must clarify - have you lost your memories, sir?"
                
        pc "Kinda..."
              
        show dravenia confused
              
        d "...'Kinda'?"
        
        pc "Yes, I've lost my memories."
        
        d "And you did not see fit to inform me of this before?"
        
        pc "It's not an easy topic to bring up..."
        
        d "On the contrary. That would have much better explained why you were oblivious to the existence of the Hellguard. When did you lose them?"
        
        pc "Yesterday."
        
        show dravenia shocked
        
        d "Yesterday? And you went to the police, yes?"
        
        pc "Uh..."
        
        show viscella shocked
        
        v "Eep."
        
        show dravenia angry
        
        d "You learned of his missing memories and brought him to the police, correct?"
        
        show viscella scared
        
        v "Well, you see... um..."
        
        v "..."
        
        show viscella flustered
        
        v "I'm sorry! Imsorryimsorryimsorry! Please don't suck me up in a vacuum cleaner and then throw it in the ocean!"
        
        d "..."
        
        show dravenia confused
        
        d "Well... I suppose I shall avoid doing whatever it is you just described, for now."
        
        show viscella scared
        
        show dravenia neutral
        
        d "Though I fail to see why you neglected to take steps to alleviate [pc]'s undoubtedly disoriented state."
        
        pc "We were waiting to see if they would come back on their own."
        
        stop music fadeout 2.0
        
        d "I see. And yet they have not. We should take you to the precinct post-haste. It is likely your friends and family are looking for you."
        
        a_un "Unlikely."
        
        d "Unlikely? Why would..."
        
        "The three of us glance to the nearby archway."
        
        jump ch2_scene03
        
    label ch2_scene03:
        
        scene bg living with dissolve
        
        "Standing beneath... is a young woman."

        show allise neutral at allise_center with dissolve
        
        a_un "He has no friends or family."

        d "..."
        
        d "Excuse me?"
        
        a_un "He has no friends or family."
        
        d "We heard you the first time. Would you mind clarifying? And then explaining who you might be, and why you are here?"
        
        a_un "..."
        
        a_un "I am [pc]'s caretaker."
        
        d "Caretaker?"
        
        a_un "Caretaker."
        
        "..."
        
        "What an unusual atmosphere."
        
        "As I think that, the girl approaches until she's only a few inches away."
        
        d "That's far enough, thank you."
        
        scene bg kitchen
        
        show viscella scared at viscella_farright
        
        show dravenia angry at dravenia_farleft
        
        show allise neutral at allise_center
        
        with dissolve
        
        d "And what do you think you are doing?"
        
        a_un "I'm checking."
        
        d "Checking what?"
        
        a_un "If [pc] is okay. Are you okay, [pc]?"
        
        menu:
            
            "'I'm... I'm fine.'":
                
                $ a_like += allAff(1)
                
                "The strange girl pauses for a moment, gazing intently at me."
                
                "I'm not sure if it's just me, but she doesn't seem to be blinking. At all."
                
                a_un "I see. That is unfortunate."
                
                d "Unfortunate? Excuse me?"
                
            "'Not anymore...'":
            
                "The strange girl gives a solemn nod."
                
                show allise closed
                
                a_un "As it should be."
                
                d "..."
                
        d "Ma'am, it would be best if you took a step back and explained yourself properly."
        
        show allise neutral
        
        a_un "..."
        
        "The girl does as she is asked, but keeps her eyes on me."
        
        a_un "[pc] lost his memories in an accident. I was assigned to take care of him. He ran off. But now I found him."
        
        pc "Then... why don't I remember you?"
        
        a_un "The incident left you unable to form long-term memories. We cured it two days ago. You can form them again."
        
        "I watch her uneasily, noticing that she still has yet to blink. Eventually she does, but... only when I start to really notice it. As if she's trying to set my mind at ease..."
        
        v "Um... hold on..."
        
        v "Isn't stuff like that really hard to cure?"
        
        a_un "We cured it two days ago."
        
        v "But-"
        
        show viscella neutral
        
        show dravenia neutral
        
        with flashBlack
        
        play music "assets/sound/bgm/noodle.mp3"
        
        v "..."
        
        d "..."
        
        "Uh... what?"
        
        "The atmosphere just shifted."
        
        show allise closed
        
        a_un "You are confused. I suppose I should explain."
        
        a_un "Your memories."
        
        a_un "It was me."
    
        "..."
        
        pc "What?"
        
        show allise neutral
        
        a_un "I destroyed your memories."
        
        menu:
            
            "'What?!'":
            
                a_un "I. Destroyed. Your memories."
        
                pc "W-what? You're not making any sense!"
                        
                "I glance desperately from Dravenia to Viscella, hoping they'll back me up."
                
                "They don't."
                
                "In fact, they look frozen."
                
                "They're breathing, but their eyes are vacant."
                
                "It's uncanny. Regardless, they're clearly not going to be any help."
                
                a_un "Your memories. The ones you're missing. I destroyed them. I took them from your head."
                
                "She makes a movement with her hands, as if she's pinching one of her temples, and pulls it outwards like an invisible strand."
                
                a_un "Cut them free..."
                
                "She whips her hand away from her head, holding it out in front of her."
                
                a_un "And obliterated them."
                
                "She releases her grip, letting the nonexistant strips of my past fall to the floor."
                
                "She's crazy. That has to be it. That, or I'm dreaming. None of this makes sense. This situation... it doesn't even feel real."
                
            "'...Oh. Well, thanks for clearing that up, I suppose.'":
             
                a_un "You're welcome."
                
                a_un "I figured I would set your mind at ease."
                
                "I glance from Dravenia to Viscella, making sure at least they've heard the admission of guilt."
                
                "They haven't."
                
                "In fact, they look frozen."
                
                "They're breathing, but their eyes are vacant."
                
                "It's uncanny. Regardless, they're clearly not going to be any help."
                
                pc "...And you're not pulling a prank on me?"
                
                a_un "I do not pull pranks."
                
                a_un "Usually."
                
                a_un "Regardless, I am responsible for your missing memories."

        a_un "You are free to believe whatever you like."
                
        a_un "But know that regardless of what you believe..."
                
        a_un "You can never remember."
        
        a_un "I will not allow you to remember."

        pc "Why?"
        
        "She blinks at me. Guess she's not in the business of dropping hints."
        
        "This is... a lot to take in."

        pc "So, my memories are... gone?"
        
        pc "No... that's not right."
        
        a_un "...?"        

        pc "My name. I know my name."
        
        a_un "..."
        
        a_un "Of course."
        
        a_un "Everyone..."
        
        "She looks at me for a moment. Her stare is no longer distant."
        
        a_un "Everyone deserves a name."
        
        a_un "Or so..."
        
        a_un "..."
        
        show allise closed
        
        a_un "Or so I've been told."
        
        "She takes a deep breath. When she opens her eyes, they are as empty as they had been before."
        
        show allise neutral
        
        a_un "I left you your name, yes."
        
        a_un "But that is all."
        
        menu:
            
            "'Why? Why'd you do this to me?":
                
                a_un "Irrelevant."
                
                jump ch2_scene04_forgotAllise
            
            "'No... it's not. There's something else I remember.'":
                
                show allise closed
                
                a_un "..."
                
                "Yes... that's right."
                
                "I've had this sensation..."
                
                "This unusual sensation..."
                
                "There's something I know..."
                
                pc "And that is..."
                
                menu:
                    
                    "'Who I am.'":
                        
                        show allise neutral
                        
                        a_un "Is that so?"
                        
                        a_un "Who are you."
                        
                        a_un "What have you done."
                        
                        a_un "Who have you hurt."
                        
                        a_un "Who have you saved."
                        
                        a_un "What do you believe."
                        
                        a_un "What do you stand for."
                        
                        a_un "Do you require more dramatic flair, or are you satisfied?"
                        
                        "This girl... what is she saying..."
                        
                        jump ch2_scene04_forgotAllise
                        
                    "'Your name...'":
                        
                        a_un "..."
                        
                        "This has to be it... I know it... I know it..."
                        
                        menu:
                            
                            "'...Violet.'":
                                
                                a_un "..."
                                
                                show allise sad
                                
                                a_un "I am... sorry."
                            
                                jump ch2_scene04_forgotAllise
                            
                            "'...Saya.'":
                                
                                a_un "..."
                                
                                show allise sad
                                
                                a_un "I am... sorry."
                                
                                jump ch2_scene04_forgotAllise
                            
                            "'...Allise.'":
                        
                                jump ch2_scene04_rememberedAllise
                        


                        
    label ch2_scene04_rememberedAllise:
        
        $ flag_RememberedAllise = True

        $ a_like += allAff(1)

        $ a_love += allAff(3)
        
        stop music fadeout 1.0
        
        a_un "..."
        
        "Did... did I get it wrong?"

        a_un "..."
        
        "She's not saying anything..."
        
        a_un "..."
        
        "But... somehow I know..."
        
        a_un "..."
        
        "That the person standing in front of me..."
        
        a_un "..."
        
        "Her name..."
        
        a_un "..."
        
        "It's-"
        
        play sound "assets/sound/sfx/flash.ogg"
        
        show allise neutral with flash
        
        a "I have already taken enough of your time."
        
        a "Your memories are gone. Do not seek them."
        
        a "..."
        
        show allise sad
        
        a "Please..."
        
        a "[pc]."
        
        jump ch2_scene05

        
    label ch2_scene04_forgotAllise:
        
        $ flag_RememberedAllise = False
        
        a_un "I have already taken enough of your time."
        
        "She takes a deep breath."
        
        show allise closed
        
        a_un "Your memories are gone."
        
        a_un "Do not go searching for them."
        
        a_un "Now..."
        
        show allise neutral
        
        a_un "I think we've kept your friends waiting long enough."
        
        jump ch2_scene05
        
    label ch2_scene05:
    
        show viscella scared
        
        show dravenia angry
        
        show allise neutral
        
        with flashBlack
    
        play music "assets/sound/bgm/062.mp3" fadein 1.0
    
        v "-isn't that impossible for people like us? You'd need magic to fix something serious like that, right?"
        
        d "The slime is right. Your story is flimsy at best, Miss...?"
        
        show allise neutral
        
        a "Allise."
            
        d "Miss Allise."
        
        "It's like nothing happened..."
        
        d "So unless you can come up with a more convincing argument, I suggest you leave."
        
        a "..."
        
        a "I am a tenant."
        
        d "What? But you just said-"
        
        a "I am here to fulfill the species quota."
        
        show viscella confused
        
        v "S-species quota?"
        
        show dravenia neutral
        
        d "Ridiculous. Just seconds ago you claimed to be [pc]'s caretaker, and now you claim to be a tenant?"
        
        a "I do not claim to be a tenant."
        
        a "I am a tenant."
        
        a "I am officially registered. If I was not, this facility would not meet the regulated species quota."
        
        show viscella flustered
        
        v "What's the species quota?!"
        
        show dravenia closed
        
        show viscella embarrassed
        
        d "..."
        
        show dravenia neutral
        
        d "The species quota of the WBA asserts that each bondhouse must harbour at least one human woman for every four chimera."

        show viscella confused

        v "Um..."
        
        v "So..."
        
        v "That... that means, that... um..."
        
        d "...*Sigh*." 
        
        d "It means we require a human woman. A role that Miss Allise seems to have conveniently fulfilled."
        
        show dravenia angry
        
        d "Which is extremely unusual, given the contradictory story she gave us just a minute ago."
        
        a "You remain skeptical."
        
        d "Of course I do. But if what you say is true, naught would come from me reporting you. {i}If{/i} what you say is true."
        
        a "I am not lying."
        
        show dravenia stern
        
        d "You lied about being [pc]'s caretaker. Who's to say you're not lying now?"

        a "I was not lying. I was joking."
        
        show dravenia shocked

        show viscella neutral
        
        d "...You were {i}joking{/i} about being a lost and confused young man's only remaining link to his past, providing him a glimmer of hope, only to crush it to dust for the sake of a {i}joke{/i}?"
        
        a "Yes."
        
        a "My sense of humour is very refined."
        
        v "..."
        
        d "..."
        
        a "See."
        
        show dravenia neutral
        
        d "But... but how did you know [pc] 's memories were even missing?"
        
        a "I eavesdropped. You speak loudly."
        
        v "W-wait, I don't understand. Me and Kumi checked the roster - there were only three other names!"
        
        a "I was a late addition."
        
        d "..."
        
        d "This conversation isn't going to go anywhere, is it?"
        
        show allise closed
        
        a "Correct."
        
        show allise neutral
        
        a "I will depart to the basement. [pc], follow."
        
        "Allise waits for me to blink, which she seems to interpret as me accepting her proposal. She nods, then wanders off. She doesn't seem to notice Dravenia's glare - that, or she just doesn't care."
        
        hide allise with dissolve
        
        show viscella at viscella_right
        
        show dravenia behind viscella at dravenia_left
        
        with move
        
        d "..."
        
        show viscella scared
        
        v "Um... miss?"
        
        d "What?"
        
        v "A-Are you going to bite someone's head off?"
        
        show dravenia confused
        
        d "What? Why would I do that?"
        
        v "Don't dragons bite heads off when they're mad?"
        
        show dravenia neutral
        
        d "Only when they are asked unnecessary questions."
        
        v "Oh. Um, did I just ask an unnecessary question?"
        
        d "Yes."
        
        v "Oh. Should I run away?"
        
        show dravenia closed
        
        d "*Sigh*. No, you don't need to run away."
        
        show dravenia neutral
        
        d "More than I can say for [pc], I'm afriad..."
        
        show viscella neutral
        
        pc "Huh?"
        
        d "Nothing, nothing. It is not my place to voice an unsubstantiated mistrust of an individual I have just met."
        
        show dravenia closed
        
        d "If it {i}was{/i} my place, however, I would likely encourage my patron to exercise extreme caution around our new tenant."
        
        menu:
            
            "'Thanks... I'll keep that in mind.'":

                $ d_like += draAff(3)

                show dravenia happy

                d "That is all I ask."
                
                show dravenia neutral
                
                d "Oh... and to scream loudly if anything disconcerning happens."
                
                pc "Uh... right."
                
                d "Now, it would be most improper to keep Miss Allise waiting."
                
                show dravenia happy
                
                d "So feel free to take your time climbing the stairs. You would not wish to wear yourself out so early in the morning."
                
                show viscella shocked
                
                v "Did... did the dragon just say something funny?"
                
                show dravenia neutral
                
                v "Whoa! I didn't know dragons could do that without being total sadists!"
                
                v "Maybe... maybe you're {i}not{/i} totally evil!"
                
                d "..."
                
                show dravenia closed
                
                d "..."
                
                v "...What?"
                
                "...I decide to head after Allise."
                
            "'If it were your place, huh?'":
                
                $ d_like += draAff(2)
                
                d "Of course. A hellguard exists to be vigilant, not paranoid."
                
                d "Though gut instincts are not something to be ignored..."
                
                show dravenia neutral
                
                d "Ah, I'm rambling. Do not let me hold you, sir - Miss Allise wishes to speak with you, like as not."
    
                v "Um... good luck."
                
                d "Yes, break a leg."
                
                d "..."
                
                d "Do not {i}actually{/i} break a leg."
                
                pc "I... I know."
                
                show dravenia closed
                
                d "Just checking."
                
                pc "I decide to head after Allise."
                
            "'Aren't you being a little paranoid?'":
                
                $ d_like += draAff(1)
            
                d "Of course not, sir."
                
                show dravenia neutral
                
                d "I am being {i}very{i} paranoid."
                
                d "But I will not interfere with your life until that paranoia becomes properly justified."
                
                d "Regardless, sir. I believe Miss Allise declared a desire to speak with you."
                
                v "Yeah... I wonder why..."
                
                show dravenia closed
                
                d "Fear not. If her motives are malicious, I shall handle it the Hellguard way."
                
                pc "The Hellguard way?"
                
                show dravenia smug
                
                d "Yes. Known to many as 'blunt force trauma'."
                
                show viscella unamused
        
                "...I'm not sure who to be more worried about. I decide to head after Allise."
                
        show dravenia neutral
                
        d "Ah... sir?"
        
        pc "Huh?"
        
        d "If I do not hear from you within the next twenty minutes, I will be inclined investigate."
        
        d "If you would to return before then, I would most appreciate it - just until I know whether this newcomer is to be trusted."
        
        d "Will you do me this small favour?"
                
        menu:
            
            "'I'll try.'":
                
                show dravenia happy
                
                d "Thank you."
                
            "'We'll have to see.'":
                
                d "Understood."
                
            "'You're really worried about Allise, huh?":
                
                show dravenia closed
                
                d "I know nothing about her, and she is difficult to read."
                
                show dravenia neutral
                
                d "So yes, I am worried. It is my job to be aware of potential threats."
                
                d "Regardless, please keep my request in mind."
                
                pc "Alright."
                
                show dravenia happy
                
                d "Thank you, sir."
                
        
        stop music fadeout 2.0
                
        jump ch2_scene06
        
    label ch2_scene06:
        
        scene bg basement with wipeleft
        
        pc "Hello? Allise?"
        
        show allise closed at allise_center with dissolve
        
        a "..."
        
        "She's just standing in the middle of the room."

        play music "assets/sound/bgm/082.mp3" fadein 3.0
    
        show allise neutral
    
        a "I have something for you."
        
        pc "I... what?"
        
        show allise closed
        
        a "I have something for you."
        
        menu:
            
            "'What is it?'":
                
                a "You must say please."
                        
                pc "Uh... please?"
                        
                "Allise nods. Then she reaches into her sweater pocket, and pulls out what seems to be a featureless black smartphone."
                        
            "'My memories?'":
                
                a "No."
                
                pc "Damn."
                
                show allise neutral
                
                a "Do you want to know what it is?"
                
                menu:
                    
                    "'Well... yeah.'":
                        
                        a "You must say please."
                        
                        pc "Uh... please?"
                        
                        "Allise nods. Then she reaches into her sweater pocket, and pulls out what seems to be a featureless black smartphone."
                        
                    "'No, not really.'":
                        
                        a "I see."
                        
                        a "I will give it to you anyways."

                        "Allise reaches into her sweater pocket, and pulls out what seems to be a featureless black smartphone."    
        
        "Well... more of a tablet, really. It's pretty wide for a smartphone."
        
        show allise neutral
        
        a "Here."
        
        menu:
            
            "'Uh... thanks?'":
                
                "Allise nods, and I take the phone... tablet... thing. It's quite light."
                
            "'So, you'll give me a phone, but not my memories?'":
                
                a "Yes."
                
                "Well. That was straightforward. I approach, and take a look at the phone... tablet... thing she's offering me. Seems normal. I pick it up - it's quite light."
                
        pc "I'm not sure I can pay you back just yet..."
        
        show allise neutral
        
        a "Payment is unnecessary."
        
        pc "But-"
        
        a "Payment is unnecessary."
        
        "Looks like payment is unnecessary."
        
        "I turn it on. Weird. It's getting full bars in the basement, and there doesn't seem to be a battery indicator."
        
        pc "Is it a standard charger?"
        
        a "Yes. A type-four self-contained antimatter reactor."
        
        pc "What?"
        
        show allise closed
        
        a "I said it was solar powered."
        
        pc "But you just-"
        
        a "I said it was solar powered."
        
        pc "...Alright."
        
        pc "Uh, any particular reason you're giving me this?"
        
        show allise neutral
        
        a "No."
        
        pc "..."
        
        a "..."
        
        pc "I see."
        
        pc "Is... is that all?"
        
        a "Yes."
        
        a "Is our discourse concluded?"
        
        menu:
            
            "'Uh... yes?'":
                
                "Allise nods." 
        
            "'Not yet.'":
                
                a "I see."
                
                pc "..."
                
                a "..."
                
                pc "..."
                
                a "..."
                
                menu:
                    
                    "'How about those memories, huh?'":
                        
                        show allise closed
                        
                        a "Is our discourse concluded?"
                        
                        pc "Not yet, I asked about my-"
                        
                        show allise neutral
                        
                        a "Our discourse is concluded."

                    "'Did you... wanna chat?'":
                        
                        $ a_like += allAff(2)
                        
                        a "..."
                        
                        a "We are already conversing."
                        
                        pc "Sure, but we're not really talking about anything."
                        
                        a "Is there a topic you wish to address?"
                        
                        pc "Uh..."
                        
                        menu:
                            
                            "'Nice weather we're having.'":
                                
                                a "Yes."
                                
                                pc "..."
                                
                                a "..."
                                
                                a "Is there another topic you wish to address?"
                                        
                                pc "Well... not that I can think of..."
                                        
                                a "Then our discourse is concluded."    
                                
                            "'Where are you from?'":
                                
                                a "..."
                                
                                a "Is there another topic you wish to address?"
                                
                                menu:
                                    
                                    "'Uh... nice weather we're having.'":
                                        
                                        a "Yes."
                                        
                                        pc "..."
                                        
                                        a "..."
                                        
                                        a "Is there another topic you wish to address?"
                                        
                                        pc "Well... not that I can think of..."
                                        
                                        a "Then our discourse is concluded."
                                        
                                    "'No. I'd really like to know where you're from.'":
                                        
                                        a "Then our discourse is concluded."
                                        
                                        

    "With that, she wanders into one of the nearby rooms without so much as a backwards glance, and the door closes silently behind her."
    
    hide allise with dissolve
    
    "It doesn't look like she's the talkative sort."
    
    "Still, though... that doesn't mean I have to give up just yet."
    
    "On the other hand, I could head back upstairs. Dravenia told me not to be long, after all. It would probably set her at ease."

    #$ affection_max = 10.0

    "Should I keep trying with Allise, or should I go back to Dravenia and the others?"

    menu:
        
        "'Head back upstairs.'":
            
            jump ch2_scene07_draVisit
        
        "'Keep trying with Allise.'":
            
            jump ch2_scene07_allVisit
            
    label ch2_scene07_draVisit:
        
        $ d_like += draAff(4)
        
        "I decide it's probably best to head back upstairs for now and set my new bodyguard at ease."
        
        scene bg kitchen with wipeleft
        
        "...That is, if she was here."
        
        pc "Dravenia? Viscella? Hello?"
        
        "They must have wandered off. At least someone bothered picking up the spilt carton of-"
        
        d "Dead."
        
        "I feel something round jab into my back."
        
        d "Hmm... we shall have to work on that."
        
        show dravenia smug at dravenia_center with dissolve
        
        "I spin around. How I missed the towering woman on my way in is a complete mystery. She gives me a little smile, and pulls the hilt of the spoon away from my back."
    
        menu:
            
            "'Yeah, you got me...'":
                
                d "Merely to prove a point, sir."
                
                d "Through no fault of your own, you are vulnerable to attack."
                
                d "With me here, however, you can immunize yourself from any such fate."
                
                menu:  
                    
                    "'The fate where I get murdered with a spoon?'":
                        
                        show dravenia happy
                        
                        d "I... took some artistic liberties, yes."
                        
                        d "But the thought is the same."
                        
                        show dravenia smug
                        
                        d "I could have incapacitated you in thirty different and increasingly creative ways when your back was turned."
                        
                        show dravenia closed
                        
                        d "N-not that I would, of course."
                        
                        d "But I digress. How went your conversation with Miss Allise?"
                        
                    "'What if I get attacked and you're not around?'":
                        
                        d "Simple."
                        
                        show dravenia happy
                        
                        d "Come get me."
                        
                        pc "Uh..."
                        
                        d "I kid, of course."
                        
                        d "In honesty, that is not something you need to worry about."
                        
                        show dravenia smug
                        
                        d "That would be my job."
                        
                        d "But I digress. How went your conversation with Miss Allise?"

            "'If you wanted to spoon me, you just had to ask.'":
                
                $ d_love += draAff(1)
                
                show dravenia happy
                
                d "Ah, but it would not be much of a sneak attack if I had asked permission, would it?"
                
                d "..."
                
                show dravenia neutral
                
                d "Unless you mean spooning as in-"
                
                pc "Yes." 
                
                d "Oh."
                
                d "..."
                
                show dravenia embarrassed
                
                d "I see. Nevermind, then."
                
                d "Um..."
                
                show dravenia neutral
                
                d "Oh! How fared your encounter with Miss Allise?"
                
            "'You're trying way too hard, I think.'":
                
                show dravenia happy
                
                d "Am I? I thought this challenge was rather rudimentary. After all, I lacked a proper briefing, sniper support, and an emergency suicide pill for this particular mock assassination attempt."
                
                show dravenia smug
                
                d "Furthermore, a spoon would be a sub-optimal weapon for the occasion. A spoon lacks range, and is quite messy when properly used."
                
                pc "I... see."
                
                show dravenia happy
                
                d "I am joking, sir."
                
                show dravenia neutral
                
                d "..."
                
                d "Mostly. The spoon comment was rather accurate."
                
                d "But I digress. How went your conversation with Miss Allise?"            

        menu:
            
            "'Just fine. I think.'":
                
                d "So... she did not make any unwanted advances?"
                
                pc "No?"
                
                d "Neither violent nor sexual?"
                
                pc "Very no."
                
                show dravenia confused
                
                d "Are you positive?"
                
                pc "Yes."
                
                show dravenia neutral
                
                d "I... see."
                
                "She looks a little dissapointed."
                
                pc "Anyways..."
                
            "'I'm not actually sure.'":
                
                d "Hmm?"
                
                pc "She's... not much of a talker."
                
                d "I figured as much."
                
                show dravenia closed
                
                d "Regardless, I trust you will keep me informed in the event she uses her body to communicate what her voice will not."
                
                pc "I... don't think you'll have to worry about that."
                
                d "Just in case, sir."
                
                pc "Uh... anyways..."
                
        pc "Where's Viscella?"
        
        show dravenia neutral
        
        d "She excused herself shortly after you left."
        
        show dravenia closed
        
        d "I have the feeling she is somewhat afraid of me."
        
        menu:
            
            "'What makes you say that?'":
                
                show dravenia neutral
                
                d "I am not stupid, sir."
                
                d "During our conversation she demonstrated her fear in every way but outright stating it."
                
                d "Furthermore, she looked at me with the same eyes a child regards a clown."
        
                show dravenia closed
        
                d "And I am {i}convinced{/i} that no child is actually comfortable around a clown."
        
            "'She's scared of a lot of things...'":
            
                show dravenia neutral
            
                d "That may be true, but I still feel somewhat responsible for her agitation."
                
                d "After all, I am keenly aware of the myriad weaknesses of the slime family of chimera."
                
                d "Though, to her credit, she seems more concerned about my species than my profession."
                
        d "But there are more pressing matters to attend to."
        
        d "Your memories, for example."
        
        pc "I'm... not sure what else needs to be said."
        
        d "How far back can you remember?"
        
        pc "Yesterday."
        
        d "That is all?"
        
        pc "That's it."
        
        d "Most unusual..."
        
        d "If you do not mind me asking, why are you here?"
        
        pc "I woke up here."
        
        d "In this kitchen?"
        
        pc "No, outside. Kumiru and Viscella found me. Apparently I just... appeared."
        
        d "Hmm..."
        
        d "Miss Allise's story is fraud, then. There is no way a licensed medical institution would allow a patient to run wild without so much as a missing persons announcement."
        
        d "And, if she is lying about such a serious matter, I see no reason to trust whatever else she may say."
        
        d "May I speak with her?"
        
        menu:
            
            "'You don't need my permission...'":
                
                d "True. But what harm in there is being polite?"
                
            "'Good luck with that.'":
                
                d "You sounds skeptical."
                
                d "I assure you, I can be quite persuasive."
        
        "With that, Dravenia marches off downstairs. I'm starting to feel like a yo-yo."
        
        jump ch2_scene08
        
    label ch2_scene07_allVisit:
        
        $ a_like += allAff(4)
        
        "I decide not to give up with Allise. After all, she's the only thing I've got that connects me to my past."
    
        jump ch2_scene08

    label ch2_scene08:
        
        "Test"

            ###################################### End of story #######################################
    
    "*TEMPEND*"
    
    $ renpy.pause(20.0, hard = True)

