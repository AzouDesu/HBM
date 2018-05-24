
    label intro_kam_nagi_fight:

        stop music fadeout 2.0

        scene bg pBedroom_n with Dissolve(2.0)

        "I'm back in my room."

        "It's only six, but I feel exhausted. Probably because of the running away thing."

        "I sprawl out on my bed, the day's events whirling through my mind."

        "I barely even notice myself falling asleep..."

        show black with Dissolve(5.0)

        play music "assets/sound/bgm/tam-n17.mp3" fadein 3.0

        $ renpy.pause (2.0)

        "...and it curved straight into the net!" 

        scene bg nBedroom_n

        show nagi neutral at nagi_right

        show fenira vhappy at fenira_left

        with Dissolve(3.0)

        f "I was just trying to pass, but mid-kick I decided, y'know what, fuck it, let's show the fresh meat how it's done."

        n "A shame you still lost 3-1."

        show fenira happy

        f "Hey, we may have lost, but at least I saved our pride."

        n "Only to have it torn away from you the following week. You guys got your asses handed to you. It was hard to watch."

        show fenira neutral

        f "It was a tough year, okay? Plus we had a bunch of newbies, and I was focusing on schoolwork."

        n "For once in your life."

        show fenira smirk_open

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

        show fenira:
            xzoom 1.0
            xanchor 0.25

        show fenira with move:
            xpos 0.05
            

        play sound "assets/sound/sfx/body_hit.wav"

        stop music

        show nagi confused with vpunch

        show fenira shocked with MoveTransition(0.1):
            xpos 0.1
            
        f "Ack, who the-"

        f "..."

        show fenira smirk

        f "Pfft. Have fun, Nagi."

        show fenira with MoveTransition(1.5):
            xpos -0.6
            
        $ renpy.pause(1.0)

        show kamao neutral at kamao_left

        show kamao:
            xalign -3.0
            
        show kamao with MoveTransition(0.2):
            xalign -0.5
            
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

        show kamao confused

        ka "Hmm..."

        show kamao neutral

        ka "I won't annoy you anymore."

        show nagi bored

        n "I find that hard to believe."

        ka "Okay, then how about this?"

        ka "You give me exclusive [pc] privileges, and I don't wake you up every morning by bellyflopping onto your bed."

        n "I thought we've already established that I'm higher on the food chain."

        show kamao confident

        ka "Sure. But I did some internet searching, and found to my amazement that eating people is illegal."

        n "Is reporting you to the supervisor for sexual harassment {i}also{/i} illegal?"
            
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
            
            n "Which I'm not."
            
            n "But if I {i}was{/i}, you've already lost."
            
            ka "Huh?"
            
            n "Playing dumb? Remind me who [pc] decided to visit in his free time? It was one of us, I recall. And by that I mean it was me."
            
            show kamao confident
            
            ka "He probably just wanted advice on how to approach someone as drop-dead gorgeous as me!"

            n "That's a stretch. Oh, well, let's indulge these fantasies of yours for a moment. Let's say he {i}did{/i} come to me for advice. That means he trusts me."
            
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
            
            ka "Huh? You're a chimera. He's a human."
            
            ka "What more proof do I need?"
            
            n "Maybe I'm a lesbian."
            
            show kamao shocked
            
            ka "A- are you?"
            
            show nagi closed
            
            n "Hm..."
            
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
            
            n "..."
            
            ka "Whoops, we're getting sidetracked. So, you gonna let me have him or not?"
            
            
        show nagi neutral
            
        n "Absolutely."

        show kamao shocked_open

        ka "R-Really?"

        n "No."
            
        show kamao angry
            
        ka "Tch!"
            
        show nagi neutral
            
        n "For his sake, of course. I mean, I only just met the guy. Unlike you, I don't start slobbering over a dude just because he makes eye contact with me someplace other than a courtroom."
            
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

        ka "But, just so you know, I'm not gonna give up that easy. [pc]'s got my name all over him. Not even a legion of Hellsguard could keep me from what's rightfully mine!"

        n "Really? How about just one?"

        show kamao confused

        ka "What?"

        show nagi neutral

        n "Just one Hellsguard."

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

        jump intro_d_meeting

    label intro_d_meeting:

            
        python:
            flag_ScaredViscella = True
            flag_RememberedAllise = False
        
        $advDay()
        
        play sound "assets/sound/sfx/morning.ogg"
        
        $ renpy.pause(3.0)
        
        scene bg pBedroom with Dissolve(5.0)
        
        "..."
        
        "I don't recognize the ceiling. It takes me a full minute to realize I'm not dreaming."
        
        "Eventually, the events of the previous day come flooding back to me."
        
        "Right... ran away, took a friend's place at a bondhouse. What a weird situation..."
        
        d_un "Is something the matter?"
        
        pc "No, it's... it's..."
        
        pc "..."
        
        menu:
            
            pc "{cps=0}...{/cps}"
            
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
        
        d_un "After all, what Hellsguard would allow harm to come to their patron?"
        
        show dravenia smug
        
        d "Dravenia Talonstein, at your service."
        
        pc "..."
        
        d "..."
        
        pc "...What?"
        
        d "Confused? Understandable. For many, the prospect of a Hellsguard guardian is but a distant dream. But I can assure you, this is no prank."
        
        "Hold on, Hellsguard? No way. They're pretty famous, but..."
        
        pc "Hellsguard? Aren't... aren't those that old order of bodyguards that constantly run into problems because they keep trying to sleep with the people they're protecting?"
        
        d "More than simply bodyguards, of course, a Hellsguard is... is..."
                
        d "..."
        
        pc "..."
        
        show dravenia shocked
        
        play sound "assets/sound/sfx/vinylscratch.wav"
        
        stop music
        
        d "No, no, not at all! The Hellsguard are a noble order of warriors dedicated to justice and the protection of the weak!"
        
        pc "Are you sure? Because these scandals have been all over the news for these last few years."
        
        "I came from a reserve and even I knew that..."
        
        pc "Plus, isn't it a little politically incorrect to call humans weak?"
        
        show dravenia embarrassed
        
        d "H-Hellsguard protect more than just humans these days! And those 'scandals' you speak of are misunderstood! It is not dishonourable for a Hellsguard to enter into a relationship with her patron - quite the opposite, in fact!"
        
        d "Those rare few who have dared coerce their patrons into unwanted sexual relationships have had their rank and titles revoked without fail!"
        
        pc "Uh-huh."
        
        d "I swear on my father's grave it is true!"
        
        pc "Alright, alright, but... still, why are you here?"
        
        show dravenia neutral
        
        d "Ah, of course. Ahem."
        
        play music "assets/sound/bgm/093.mp3" fadein 3.0
        
        show dravenia happy
        
        d "As previously stated, I am a Hellsguard."
        
        d "Our origins go back hundreds of years, when the first..."
        
        d "..."
        
        show dravenia smug
        
        d "Ah. Forgive me. Would you like the long or the short of it?"
        
        "I don't know much about the Hellsguard, and she seems quite eager to talk my ear off..."
        
        menu:
            
            "{cps=0}I don't know much about the Hellsguard, and she seems quite eager to talk my ear off...{/cps}"
            
            "'I've got time.'":
                
                $ d_like += 1
                
                show dravenia happy
                
                d "Thank you, sir. I shall do my utmost not to bore."
                
                show dravenia neutral
                
                d "As you know, the ancient relationship between human and chimera was tumultuous, and oft violent."
                
                d "Almost three centuries ago, humanity neared extinction due to chimera decadence."
                
                show dravenia closed
                
                d "Humans were treated as cattle, with little freedom to do ought but satisfy their chimera owners or to produce and raise offspring."
                
                show dravenia neutral
                
                d "Our chimeran forebears lacked foresight. They failed to understand the consequences of their actions. Our species requires humans to survive and reproduce, after all. Your extinction is our extinction."
                
                d "But not all of them were blind."
                
                show dravenia happy
                
                d "In the closing years of the eighteenth century, a collection of chimera noblewomen met in secret in a small inn in Paris. They decided that something must be done."
                
                d "And thus began one of the largest revolts in our people's collective history."
                
                d "You see, human rebellions were beginning to fizzle out. Their numbers were dwindling, and open warfare became impossible; before the advent of firearms, a single powerful chimera was more than a match for a handful of human combatants."
                
                d "But when the monarchies of the old world were set upon by an organized force of the surviving humans {i}and{/i} like-minded chimera, as well, things become complicated."
                
                show dravenia neutral
                
                d "Chimera society was split in half. On one hand, there were those that clung to the old ways - taking mates by force and keeping humans shackled to their whims."
                
                d "On the other hand, some chimera saw change as necessary. Some saw that the old ways were unsustainable and would inveitably signal a slow death for the species."
                
                d "Others were ruled by their heart. Every chimera family was dotted with humans - husbands, wives, in-laws."

                d "Regardless of their reasons, human and chimera fought side-by-side. Prominent human figureheads would rise in rank and reputation - leaders who thrashed the stereotype of the meek, subservient human and threw the traditional worldview into question... only to be cut down or captured and subjected to far worse."
                
                d "Can we blame them? No matter how powerful the human, there is little they can do to protect them from a dragon's breath or a succubi's touch."
                
                show dravenia happy
                
                d "Unless, they realized, they were to fight fire with fire. Do you see where I am going with this?"
                
                pc "I think so..."
                
                d "Well, before long, those prominent figureheads had entire squadrons of elite chimera bodyguards."
                
                d "These chimera were trained specifically to deal with any manner of foe, whether combative or subversive."
                
                d "For every seducer sent to tempt a man or woman to betray their cause, a purifier was ready to revert the damage."
                
                d "For every assassin sent to drive a dagger through a target's heart, a warrior was ready to jump in front of the blade."
                
                d "For every warlock primed to incinerate a hideout, a sorceress was ready to intercept the fireball."
                
                d "Would you like to guess what these trained individuals were called?"
                
                menu:
                    
                    d "{cps=0}Would you like to guess what these trained individuals were called?{/cps}"
                    
                    "'Hellsguard?'":
                        
                        show dravenia smug
                        
                        d "An excellent deduction, and almost completely accurate." 
                        
                    "'Ass-kickers?'":
                        
                        show dravenia smug
                        
                        d "Not quite, but I admit your suggestion carries a certain charm."
                        
                show dravenia happy
                        
                d "At the time, they were called the Order of the Sworn, you see."
                        
                d "After the revolution had concluded with their victory, they recreated themselves under the banner of the Hellsguard."
                    
                d "Elite bodyguards, created to even the playing field between humans and chimera and give the former a fighting chance."
                    
                d "That is our duty. - though in the modern era, anyone with the proper financial connections can find themselves under Hellsguard protection, whether human or chimera."
                        
                
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
                
                d "But I shall not surrender! My pride as a Hellsguard depends on it!"
                
                show dravenia neutral
                
                d "Let's see..."
                
                d "There is a huge gap of ability between humans and chimera."
                
                d "Put an unarmed human and an unarmed chimera into a pit and force them to battle... the chimera will win, nine times out of ten."
                
                d "That's where the Hellsguard come in."
                
                d "Put an unarmed human in a pit with a chimera, and give that human a Hellsguard? Well..."
                
                show dravenia happy
                
                d "To say you've reversed the odds would be what I like to call a 'colossal understatement.'"
                
                d "We protect more than just humans these days - anyone with the proper financial connections can find themselves under Hellsguard protection."
                
        pc "So... you're a bodyguard?"
        
        show dravenia neutral
                
        d "The term 'bodyguard' does not do the Hellsguard name justice. We are trained from adolescence to protect our patron with our lives. We undergo extensive training in all manner of firearms and martial arts."
        
        d "We have a working knowledge of nearly every chimera species's strengths and weaknesses, can resist psionic attacks and other mind-altering affects, and possess the survival knowledge to thrive in all but the most inhospitable of environments."
        
        d "Most importantly, we are always on-duty. Hellsguard do not have 'off-time.' We work to ensure your safety twenty-four hours a day, seven days a week, three-hundred and sixty five days a year."
        
        d "Those of us who serve a lifetime contract will protect you until the day you die."
        
        pc "...Huh."
        
        show dravenia smug
        
        d "Impressive, no? You were not gifted with a lifetime contract, unfortunately. But I can promise the day you die will {i}not{/i} fall under the upcoming year."
        
        menu:
            
            d "{cps=0}Impressive, no? You were not gifted with a lifetime contract, unfortunately. But I can promise the day you die will {i}not{/i} fall under the upcoming year.{/cps}"
        
            "'That's... comforting.'":
                
                d "Hellsguard are valued for providing peace of mind. I am glad to already be fulfilling that portion of my duties."
            
                d "Not that my other duties or skills are any less notable."
            
            "'We'll see about that.'":
                
                show dravenia confident
                
                d "Do you doubt my abilities, sir?"
        
        show dravenia confident
        
        d "It is no brag to say I could carry the Holy Grail unscathed through a dragon's den."
                
        d "..."
                
        show dravenia neutral
                
        d "Well, mayhap that was {i}somewhat{/i} of a brag."
        
        pc "Speaking of which, are you...?"
        
        d "A dragon? Yes. Put your mind at ease, sir - my hoarding instincts have been trained out of me. I carry with me nothing but the clothes on my back."
         
        menu:
            
            d "{cps=0}A dragon? Yes. Put your mind at ease, sir - my hoarding instincts have been trained out of me. I carry with me nothing but the clothes on my back.{/cps}"
         
            "'Hoarding instincts?'":
                
                d "Yes. Dragons hoard. It's a habit of sorts."
                
                pc "Really? What did you hoard?"
                
                d "Er..."
                
                show dravenia embarrassed
                
                d "Fantasy books."
                
                d "N-not that there's anything wrong with that."
                
                "She sounds a little uncertain."
                        
            "'You're a {i}dragon{/i}?! That's so cool! Can you breathe fire?'":
                
                $ d_love += 1
                
                show dravenia lovestruck
                
                d "A-ah? Er, um..."
                
                pc "Oh, sorry. Did I say something weird?"
                
                d "No! No. F-Forgive me. I was not expecting the sudden outburst of enthusiasm."
                
                d "Breathing fire is... yes, it is something I am capable of."
                
                show dravenia neutral
                
                d "Though it is unlikely you shall get to see it often."
                
                d "I conducted a thorough analysis of the building before I entered, and discovered to my dissapointment that it is indeed... flammable."
                
                "She gives a somewhat disappointed sigh."
                
        d "Did you have any other questions?"

        $ tempvar = ""
        
        menu:
            
            d "{cps=0}Did you have any other questions?{/cps}"
            
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
                
                d "For now, I must regretfully keep my lips sealed on the identity of your mysterious, slithering benefactor."
                
                "..."
                
                pc "And... you're sure it's me?"
                
                d "What do you mean?"
                
                pc "Well, are you sure it's me you're supposed to protect?"
                
                d "Of course. You are [pc], correct?"
                
                "You nod."
                
                show dravenia happy
                
                d "I am... relieved. Making a mistake this far into the procedure would have been rather embarrassing."
                
                $ tempvar = "But it seems no such mistake has been made. I look forward to working with you, sir."
                
                d "[tempvar]"
                
            "'No, that's about all I need to know.'":
                
                show dravenia happy
                
                $ tempvar = "Understood, sir. I look forward to working with you."
                
                d "[tempvar]"
                
        menu:
            
            d "{cps=0}[tempvar]{/cps}"
            
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
            xpos 0.1

        show dravenia:
            xzoom -1.0

        "Dravenia quickly and silently crosses the room, pressing her back up against the wall directly beside the door. She gives you a stoic nod."
        
        "Is she genuinely concerned, or is she just trying to show off? As for the knock..."
        
        menu:
            
            "{cps=0}Is she genuinely concerned, or is she just trying to show off? As for the knock... {/cps}"
                
            "'Uh. Come in?'":
                
                "The door flies open."
                
            "'You may not want to come in...'":
                
                "The door flies open anyways."
                
        play sound "assets/sound/sfx/door_open.wav"
          
        play music "assets/sound/bgm/097.mp3"
          
        ka "Hayo!!"
        
        show kamao vhappy at kamao_left

        show kamao:
            xpos -1.0
        
        show kamao with MoveTransition(0.2):
            xpos 0.2
            
        show kamao shocked
        
        ka "Wha-"
        
        show kamao:
            ypos 1.3
            
        show dravenia closed:
            ypos 0.8
            
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
        
        ka "What do I look like, Hulk Helga? I'm basically a paperweight with legs!"
        
        show dravenia neutral at dravenia_left with MoveTransition(0.5)
        
        d "I see. That is... dissapointing..."
          
        ka "I can see the light. Father? Mother? Is that you? Since when were you dead?!"
        
        d "..."
        
        show kamao with MoveTransition(0.5):
            ypos 1.2
            xpos 0.35
        
        ka "Ow."
        
        show kamao with MoveTransition(0.5):
            ypos 1.1
            xpos 0.5
            
        ka "Very ow."
        
        show kamao with MoveTransition(0.5):
            ypos 0.95
            xpos 0.68
        
        ka "AhahaOW."
        
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
            xpos -1.0
            
        show kamao:
            xpos -0.85
            
        with MoveTransition(2.0)
            
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
        
        jump intro_breakfast
        
    label intro_breakfast:
        
        # Maybe have viscella up instead?
        
        scene bg kitchen with wipeleft
        
        "It's quiet all the way to the bottom floor, but I spot the first familiar face in the kitchen."
        
        show viscella neutral at viscella_center with dissolve
        
        "It's Viscella. She hasn't noticed me, yet - she's looking out the window, sipping straight from a carton of orange juice."
        
        "I could say hello. Or..."
        
        menu:
            
            "{cps=0}I could say hello. Or...{/cps}"
            
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
                    
                    v "{cps=0}Actually, I'm a lot better at making them.{/cps}"
                    
                    "'I'm sure it's not that bad.'":
                        
                        $ v_like += 1
                        
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
                
                show viscella with MoveTransition(0.3):
                    ypos 1.4
                
                play sound "assets/sound/sfx/splat.wav"
                
                "..."
                
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
                    
                    v "{cps=0}{i}Amorphous Blob.{/i}{/cps}"
                    
                    "'Should I get a doctor?'":
                        
                        show viscella puddle_neutral
                        
                        v "N-no. This happens sometimes."
                        
                        v "...Only sometimes."
                        
                        v "Yes, very rarely, of course."
                        
                        v "It's not a regular thing."
                        
                        v "..."
                        
                        v "Yes."
                        
                    "'Tch. I underestimated you.'":
                    
                        $ v_love += 1
                    
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
                
        show viscella with MoveTransition(0.3):
                    ypos 1.4
                
        play sound "assets/sound/sfx/splat.wav"
                
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
        
        v "I knew it! You're going to go bowling with it!"
        
        v "Someone help!"
        
        d "Would you calm down? I mean no harm."
        
        v "..."
        
        show viscella scared at viscella_right with dissolve
        
        d "..."
        
        v "Please be gentle..."
        
        "Dravenia glances to me for support."
        
        menu:
            
            "{cps=0}Dravenia glances to me for support.{/cps}"
            
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
        
        "Dravenia's looking to me for support again."
        
        pc "I'm... not sure. Maybe she had some past trauma or something."
        
        show viscella scared
        
        v "Past trauma? It wasn't just trauma, it was..."
        
        show viscella confused
        
        v "..."
        
        v "On second thought, trauma is pretty accurate."
        
        show viscella flustered
        
        show dravenia neutral
        
        v "But still, she's a dragon! Aren't you terrified out of your mind right now?!"
        
        menu:
            
            v "{cps=0}But still, she's a dragon! Aren't you terrified out of your mind right now?!{/cps}"
            
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
        
        v "They're one of the most dangerous chimera out there! And they have the arrogance to back it up!"
        
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
        
        menu:
            
            v "{cps=0}...{/cps}"
            
            "'You're not a waste of space.'":
                
                $ v_like += 1
                
                show dravenia neutral
                
                v "I'm... not?"
                
                pc "Why are you acting so surprised?"
                
                v "The only one who tells me I'm not a waste of space is Kumi... and some online friends..."
                
                pc "Give yourself more credit, Viscella."
                
                v "I try to, but..."
                
                v "...Thanks."
                
            "Pat her head.":
                
                $ v_like += 1
                
                $ v_love += 2
                
                show dravenia neutral
                
                "I take a few steps forward, and pat Viscella on the head with a wet {i}splat{/i}."
                
                show viscella embarrassed
                
                "She almost jumps at the contact."

                show viscella flustered

                v "Wh-wh-what are you doing?!"
                
                pc "Huh? Is something wrong?"
                
                "I stop patting her, shaking the slime from my hand."
                
                show viscella lovestruck
                
                v "Um... n-no."
                
        d "I am terribly sorry to interrupt, but..."
                
        d "We're being watched."
        
        stop music fadeout 1.0
        
        "Dravenia points, and the three of us glance to the nearby archway."
        
        jump intro_a_meeting

    label intro_a_meeting:
        
        scene bg living with dissolve
        
        play music "assets/sound/bgm/noodle.mp3" fadein 2.0
        
        "Standing beneath... is a young woman."

        show allise neutral at allise_center with dissolve
        
        a_un "..."

        d "Hello?"
        
        a_un "Hello."
        
        d "You must be the human woman on the roster."
           
        a_un "Yes."
        
        d "I... see."
        
        scene bg kitchen
        
        show viscella scared at viscella_farright
        
        show dravenia neutral at dravenia_farleft
        
        show allise neutral at allise_center
        
        with dissolve
        
        "The girl approaches until she's only a few inches away. She's staring straight at me. She won't even look at Dravenia when she's talking to her."
        
        d "Good to meet you. I am Dravenia. This is [pc]."
        
        a_un "..."
        
        show dravenia confused
        
        d "Uhm. And this is Viscella. What is your name?"
        
        "The woman, for her part, continues to stare at me, before she passes me by."
        
        a_un "Come. I have something to discuss. Alone."
        
        pc "Me?"
        
        a_un "Yes."
        
        "She doesn't turn back, heading down a nearby flight of stairs towards the basement. I glance back at the other two. Dravenia, still left hanging, clears her throat, looking somewhat flustered."
        
        hide allise
        
        show dravenia neutral at dravenia_left
        
        show viscella at viscella_right
        
        with dissolve
        
        v "And I thought {i}I{/i} was socially awkward..."
        
        d "Mmh... I don't like this. Why would she explicitly want to speak to you alone?"
        
        v "Maybe it's a human thing?"
        
        d "Unlikely. Regardless, please don't let your guard down around her, sir. I will position myself at the top of the stairs - if she tries anything, please scream at the top of your lungs."
        
        pc "I don't think that will be necessary..."
        
        d "Perhaps. I am aware humans are generally less aggressive in their advances than chimera. Regardless, something strikes me as... unusual, about her."
        
        v "She didn't even acknowledge my existence..."
        
        menu:
            
            v "{cps=0}She didn't even acknowledge my existence...{/cps}"
            
            "'She's probably just socially awkward, like Viscella said.'":
                
                v "Yeah... um, maybe she just wanted to to pull you aside so she could explain how shy she is and ask you to introduce her to us?"
                
                show viscella happy
                
                v "That sounds like something I'd do!"
                
                d "I'm not sure... either way, only one way to find out. Apologies - I would follow, but she specifically asked for privacy. I do not wish to be overbearing."
                
                pc "Don't worry about it. I'll be fine."
                
                d "I will be just out of earshot, sir."
                
            "'There is something sort of bizarre about her...'":
                
                d "Exactly. There is no harm taking precautions. I could lend you a push dagger?"
                
                pc "Nonono, I'm fine. Really."
                
                show viscella scared
                
                v "You... you have daggers?"
                
                d "I cannot answer that question."
                
                v "But you just said you'd lend him one!"
                
                d "Nonsense. Be safe, sir."
                
        pc "Again with the sir..."
        
        "I march off downstairs. Dravenia follows, but stops at the top of the stairs, leaning casually against the railing as I descend into the basement."
        

        stop music fadeout 2.0
                
        jump ch2_scene06
        
    label ch2_scene06:
        
        scene bg basement with wipeleft
        
        "Come to think of it, I haven't been down here yet. Not that it seems I was missing much - there's not a single piece of furniture. Just a few doors - one of which is slightly open. Squinting, I can see an eye peering out of the darkness."
        
        "Once I make eye contact, the door creaks open."
        
        show allise neutral at allise_center with dissolve
        
        play music "assets/sound/bgm/082.mp3" fadein 3.0
        
        a_un "Come."
        
        pc "Uhm..."
        
        "The woman beckons. I glance up the stairs once, before approaching. She retreats into the darkness of the room, and as I cross the threshold of the doorframe I fumble for a light switch. I find it - and, switching it on, find myself standing in a completely empty room aside from myself and our mysterious tenant."
        
        scene bg aBedroom 
        
        show allise neutral at allise_center
        
        with dissolve
        
        a_un "Welcome."
        
        pc "Welcome? It's just an empty room..."
        
        a_un "It is my bedroom."
        
        pc "Oh, is it? You should really get some decorations in here. Like a bed, for example."
        
        a_un "No."
        
        pc "...Okay."
        
        "There's a long, incredibly awkward silence as I try desperately to find something to look at without returning the stare she's leveling at me."
        
        pc "D-Did you need something? I mean, I still haven't caught your name..."
        
        a "Allise."
        
        pc "Your name is Allise?"
        
        a "Yes."
        
        pc "I see... so, Allise, what did you bring me down here for?"
        
        "Allise seems to consider this for a moment - and by consider it, I mean she continues to stare impassively at me for what feels like half a minute. She's still not blinking."
        
        "The moment I take a mental note of it, though... she blinks. Just once."
        
        a "To explain."
        
        pc "Explain what?"
        
        a "The situation."
        
        pc "Well, what's the situation?"
        
        a "You need to choose."
        
        pc "Choose?"
        
        a "Yes. Choose."
        
        pc "Choose what?"
        
        a "A favourite."
        
        pc "Sorry, but... could you please explain what's going on using more than 3 words in each sentence?"
        
        a "Yes. You need to choose a favourite individual among the members of this building over the course of the next year."
        
        pc "...Why?"
        
        a "Reasons."
        
        pc "Reasons? That's not a very good reason."
        
        a "It does not matter. If you do {i}not{/i} choose a favourite, I will restart the cycle until you do."
        
        "I frown. What's this lady talking about?"
        
        pc "Cycle?"
        
        a "Yes. Starting from yesterday."
        
        pc "I don't follow."
        
        a "You must develop a close bond with one member of this household by the end of the term."
        
        a "If you fail to do this, I will reset the cy-"
        
        pc "Hold up, hold up. What is a cycle?"
        
        "Allise's stair remains consistent, but for some reason I get the feeling she's looking at me as if I said something stupid."
        
        a "A period of time. The upcoming year."
        
        pc "Right. And you're going to restart it. What, you're going to turn back the clock? Rewind time?"
        
        a "Yes."
        
        pc "Because otherwise, I still don't get what you're trying to- what?"
        
        a "If you fail to develop a bond by the end of the term, I will restart from the beginning of the time-loop."
        
        pc "Is this a joke?"
        
        a "I do not joke."
        
        menu:
            
            a "{cps=0}I do not joke.{/cps}"
            
            "Don't believe her.":
                
                "I think she might be off her rocker."
                
            "Don't believe her.":
        
                "I think she might be off her rocker."
        
        pc "Sorry, Allise, but... that's probably the craziest thing I've ever heard."
        
        a "You do not believe me."
        
        pc "Of course I don't. C'mon, you're gonna go back in time? That's absolutely crazy."
        
        a "Why?"
        
        pc "The most powerful chimera in the world can't go back in time, and you're telling me you can? A human?"
        
        a "..."
        
        a "I was expecting you would require evidence. When you were eleven years of age, home alone, you were playing with chemicals in your basement."
        
        a "A friend had told you that a mixture of common household substances would synthesize a slime."
        
        a "You were lonely, so you decided to give it a try. But the concoction did not create a slime - it created toxic gas. Your parents returned shortly afterwards and found you passed out."
        
        a "You narrowly avoided a hospital visit. When your parents demanded to know what you were doing mixing chemicals."
        
        a "Panicked, you told them instead that you were attempting to make drugs. You believed the punishment would be less severe than if you had confessed you were attempting to create a chimera."
        
        "For once, I return this woman's stare just as intently. Swallowing, I open my mouth to sp-"
        
        a "Now you will ask: 'How did you know that? I never mentioned it to anyone!'"
        
        "For a moment, I'm confused into thinking it was me that spoke. No - it was her, mimicking my voice perfectly, and predicting exactly what I was going to ask."
        
        a "Perhaps you have never mentioned that story to anyone. But you will, when you are intoxicated at the halloween party next month."
        
        a "Of course, now that I have revealed this information to you, perhaps you will refrain from telling that story. Perhaps you will refrain from attending at all."
        
        a "Such is the consequence of interfering in causality." 
        
        pc "I... don't quite understand, what-"
        
        a "Simple, then."
        
        a "I have created a semi-stable time loop. At the end of the year, we will return to its beginning. Only I will retain my memories of the previous cycle - you and the others will forget."
        
        pc "Wait, hold on, just - just stop for a second, would you? This is a lot to take in, and even if I {i}did{/i} believe you-"
        
        a "Belief is irrelevant. This is fact." 

        a "If you prove incapable of following my instructions in this cycle as was the case in the previous, I will immediately restart the cycle."
        
        pc "What are you? Is there even a chimera-"
        
        a "Cease."
        
        a "Are you or are you not prepared to follow my instructions."
        
        pc "What- what instructions?"
        
        a "To form a bond with a tenant."
        
        pc "Wait, so just... you go through all this, this... weird, crazy talk just to tell me I need to make a friend?"

        a "The first cycle, I did not reveal my presence. You spent your days in relative happiness. You made connections with the other tenants."
        
        a "But the bonds were impermanent. Weak. Unfit. You spread yourself thin by attempting to befriend them all."
        
        a "I require a deep, powerful connection. A year is not long enough for one of your skills to develop that with everyone."
        
        a "But perhaps you will have more success with a single individual."
        
        a "Choose one tenant. Just one. Work your way into their psyche, and let them work their way into yours. Become reliant on one another, inseperable."
        
        a "If you can do this, I will release you from the cycle."
        
        a "If you cannot, I will evaluate this strategy and refine it for the next cycle - as I have done with all the others."
        
        a "If you refuse outright, I will restart the cycle prematurely. What you undoubtedly believes is a rebellious assertion of free will is really just a waste of time for both of us. I {i}will{/i} have you follow my instructions eventually - it is only a matter of how many cycles it takes to do so." 
        
        a "If you attempt to speak to the others about your situation or my role in it, I will restart the cycle prematurely. Their meddling is an annoyance, and rarely improves their opinion of your mental health."
        
        a "I expect your answer by midnight tonight. I will ask only once. Decide on a course of action by then."
        
        menu:
            
            a "{cps=0}I expect your answer by midnight tonight. I will ask only once. Decide on a course of action by then.{/cps}"
            
            "Demand more time.":
                
                pc "Just slow down, damnit! You're dumping way too much responsibility on me! If what you're telling me is true, how do you expect me to make such a serious decision in one night?!"
                
                a "You will adapt. It is a particular talent of your species to endure under immense stress."
                
                pc "Stress? What are you talking about! This isn't stress, this is insanity!"
                
                pc "And what do you mean, you'll convince me eventually? You're just looping the same thing over and over again, aren't you?"
                
            "Grudgingly accept.":
                
                pc "...I don't have much choice, do I? If you're telling the truth, and I turn you down, you'll just... start everything over again. Over and over, until I agree."
                
                a "Yes."
                
                pc "Won't I just say all of this over again?"
                
        a "No. I will gradually change my approach. Furthermore, there are discrepencies in each cycle that cannot be accounted for. This happens naturally for all subjects of casaulity - but its effect is hightened dramatically for you."
        
        pc "What do you mean, for me?"
        
        a "...Irrelevant. Remember: your choice is to be made by midnight."
        
        scene bg basement with Fade(0.1, 0.0, 0.1)
        
        pc "Wait, hold on, there's still so much-"
        
        "Wait. What?"
        
        "I only blinked, but... I'm in the basement? Huh?"
        
        "Did I black out? Microsleep? Did she push me out the door?"
        
        "I glance back towards the door. It's closed. I give it a knock."
        
        pc "Allise?"
        
        "There's no answer."
        
        menu:
            
            "{cps=0}There's no answer.{/cps}"
            
            "Try the doorknob.":
                
                "I try the doorknob."
                
                "It's locked. Of course."
                
            "Shrug it off.":
                
                "Well, it's clear she has some sort of bizarre power. I guess kicking me out of her room faster than I can blink isn't entirely out of the question."
                
        "No use staying down here, then. Casting one last cautious glance at the door, I trudge my way back upstairs. My head's spinning in all sorts of directions. It's a miracle I don't tumble down the steps."
        
        "Do I believe her or not? It's a lot to take in, but... maybe I'm doing myself a disservice by treating this rationally. I left my rational life when I left my parents."
        
        "Still, choosing a single person to form an inseperable bond with? What kind of contrived, strung-together plot..."
        
        "... No use losing my mind over it, I guess."
        
        scene bg kitchen with wipeleft
        
        pc "Dravenia? Viscella? Hello?"
        
        "They must have wandered off. At least someone bothered picking up the spilt carton of-"
        
        d "Dead."
        
        "I feel something round jab into my back."
        
        d "Hmm... we shall have to work on that."
        
        show dravenia smug at dravenia_center with dissolve
        
        "I spin around. How I missed the towering woman on my way in is a complete mystery. She gives me a little smile, and pulls the hilt of the spoon away from my back."
    
        $ tempString = ""

        menu:
            
            "{cps=0}I spin around. How I missed the towering woman on my way in is a complete mystery. She gives me a little smile, and pulls the hilt of the spoon away from my back.{/cps}"
    
            "'Yeah, you got me...'":
                
                d "Merely to prove a point, sir."
                
                d "Through no fault of your own, you are vulnerable to attack."
                
                d "With me here, however, you can immunize yourself from any such fate."
                
                menu:  
                    
                    d "{cps=0}With me here, however, you can immunize yourself from any such fate.{/cps}"
                    
                    "'The fate where I get murdered with a spoon?'":
                        
                        show dravenia happy
                        
                        d "I... took some artistic liberties, yes."
                        
                        d "But the thought is the same."
                        
                        show dravenia smug
                        
                        d "I could have incapacitated you in thirty different and increasingly creative ways when your back was turned."
                        
                        show dravenia closed
                        
                        d "N-not that I would, of course."
                        
                        $ tempString = "But I digress. How went your conversation with Miss Allise?"
                        
                        d "[tempString]"
                        
                    "'What if I get attacked and you're not around?'":
                        
                        d "Simple."
                        
                        show dravenia happy
                        
                        d "Come get me."
        
                        pc "Uh..."
                        
                        $ tempString = "But I digress. How went your conversation with Miss Allise?"
                        
                        d "[tempString]"

            "'If you wanted to spoon me, you just had to ask.'":
                
                $ d_love += 1
                
                show dravenia happy
                
                d "Ah, but it would not be much of a sneak attack if I had asked permission, would it?"
                
                d "..."
                
                show dravenia neutral
                
                d "Unless you mean spooning as in-"
                
                pc "Yeah." 
                
                d "Oh."
                
                d "..."
                
                show dravenia embarrassed
                
                d "I see. Nevermind, then."
                
                d "Um..."
                
                show dravenia neutral
                
                $ tempString = "Oh! How fared your encounter with Miss Allise?"
                
                d "[tempString]"
                
            "'You're trying... way too hard, Dravenia.'":
                
                show dravenia happy
                
                d "Am I? I thought this challenge was rather rudimentary. After all, I lacked a proper briefing, sniper support, and an emergency suicide pill for this particular mock assassination attempt."
                
                show dravenia smug
                
                d "Furthermore, a spoon would be a sub-optimal weapon for the occasion. A spoon lacks range, and is quite messy when properly used."
                
                pc "I... see."
                
                show dravenia happy
                
                d "I am joking, sir."
                
                show dravenia neutral
                
                d "..."
                
                d "Mostly. The spoon comment was rather accurate - they are quite messy when properly used."
                
                $ tempString = "But I digress. How went your conversation with Miss Allise?"
                
                d "[tempString]"

        menu:
            
            d "{cps=0}[tempString]{/cps}"
            
            "'It went alright. I mean, all things considered...'":
                
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
                
            "'I'm not actually sure.'":
                
                d "Hmm?"
                
                pc "It's sort of hard to explain."
                
                d "I figured as much. She seems the type where explaining is difficult."
                
                "Lady, you have no idea."
                
                show dravenia closed
                
                d "Regardless, I trust you will keep me informed in the event she uses her body to communicate what her voice will not."
                
                pc "I... don't think you'll have to worry about that."
                
                d "Just in case, sir."
                
        pc "Hey, where's Viscella? Wasn't she here with you?"
        
        show dravenia neutral
        
        d "She excused herself shortly after you left."
        
        show dravenia closed
        
        d "I have the feeling she is somewhat afraid of me."
        
        menu:
            
            d "{cps=0}I have the feeling she is somewhat afraid of me.{/cps}"
            
            "'What makes you say that?'":
                
                show dravenia neutral
                
                d "I am not stupid, sir."
                
                d "During our conversation she demonstrated her fear in every way other than outright stating it."
                
                d "...On second thought, I am quite convinced she {i}did{/i} outright state it."
                
                d "Furthermore, she looked at me with the same eyes with which a child regards a clown."
        
                show dravenia closed
        
                d "And I am {i}convinced{/i} that no child is actually comfortable around a clown."
                
                pc "Were you?"
                
                d "...No."
        
            "'She's scared of a lot of things...'":
            
                show dravenia neutral
            
                d "That may be true, but I still feel somewhat responsible for her agitation."
                
                d "After all, I am keenly aware of the myriad weaknesses of the slime family of chimera."
                
                show dravenia closed
                
                d "Indeed, it is only a minor exaggeration to claim there are dozens of techniques I could use to pacify, incapacitate, and eliminate her..."
                
                "That seems more like pride than concern..."
                
                show dravenia neutral
                
                d "Though, to her credit, she seems more concerned about my species than my profession."
                
        "Dravenia clears her throat."
        
        d "Regardless, though - was there any reason you wanted to see the slime?"
        
        "I'd like to tell someone, but... it's sort of risky. Maybe I should wait to know them better, to make sure they won't alert Allise. Or think I'm completely insane..."
        
        "Gah, who am I kidding? This {i}is{/i} insane. I've heard some varieties of chimera possess some powerful magic, but stuff like this is just... just..."
        
        show dravenia confused
        
        d "...Sir?"
        
        pc "A-ah! Sorry, I'm a little..."
        
        d "Distracted. Is everything alright?"
        
        pc "Yeah, it's fine. I'm fine."
        
        "...No, I'm not. I need to talk to someone. Make sure I'm thinking clearly. But I can't have them thinking I'm crazy, either."
        
        "C'mon, think... who do I know who's imaginative and gullible and equal measure?"
        
        menu:
            
            "{cps=0}C'mon, think... who do I know who's imaginative and gullible and equal measure?{/cps}"
            
            "'Viscella. Obviously.'":
                
                "Yeah, if anyone's gonna entertain this lunacy, it'll probably be her."
                
            "'Kamao. Definitely.'":
                
                "Now that I think about it, she sure does fit those criteria..."
                
                "But I don't think my current mental state can handle Kamao right now. Viscella's a safer bet."
        
        d "I had just asked if there was any reason you needed to see the slime, and it seemed to set you off daydreaming."
        
        show dravenia shocked
        
        "Her eyes widen."
        
        d "Don't tell me you..."
        
        pc "Yes! I need to talk to Viscella. It's urgent. Well - not urgent, but, uh, it's important."
        
        d "Important? I'm sure together we can find her in a matter of-"
        
        pc "No! I mean no. Well, sorry. I just... this is something that needs privacy."
        
        show dravenia embarrassed
        
        d "I... I see... are, um, you two familiar, or was it at first sight?"
        
        pc "Huh?"
        
        d "Nothing! Nothing, I- this way. I'm pretty sure she went this way."
        
        "Dravenia starts towards the staircase, but freezes on the spot. Beads of sweat trickle down her face."
        
        show dravenia smug
         
        d "Oh... so my first test, is it... v-very well..."
        
        pc "Are... you okay?"
        
        d "Yes. Yes, sir. I will stay right here. Without following you. Your privacy is important, even if it puts you at risk."
        
        d "..."
        
        d "On second thought, saying it out loud..."
        
        show dravenia embarrassed
        
        d "Would it be okay if I at least stood outside the door?"
        
        menu:
            
            d "{cps=0}Would it be okay if I at least stood outside the door?{/cps}"
            
            "'Only if you swear not to eavesdrop.'":
                
                $ flag_intro_DraveniaAccompanies = False
                
                show dravenia stern
                
                d "Yes, sir! I swear it, sir!"
                
                d "I will attune my hearing to only the highest-pitch cries for aid!"
                
                pc "I don't think you'll hear any of those. Unless Viscella catches you standing ominously outside her door, that is."
                
                show dravenia embarrassed 
                
                d "Perhaps I shall stand slightly to the side of the door, instead..."
                
                pc "Probably a good idea. You just want me to scream if something goes wrong?"
                
                "Though I doubt it will..."
                
                show dravenia neutral
                
                d "Ah, it would likely be ineffective. The slime could smother you in an instant, rendering you incapable of calling for aid."
                
            "'Viscella's not a threat.'":
                
                $ flag_intro_DraveniaAccompanies = False
                
                show dravenia neutral
                
                d "Do not underestimate her simply because she is a slime. Contrary to their appearance, they can be deadly."
                
                pc "Do you really have to assume the worst in everyone?"
                
                show dravenia smug
                
                d "It is not assuming the worst, sir. It is assessing the threat."
                
                pc  "'And do you honestly think Viscella's a threat? From what I've been able to gather, she's a nervous, socially anxious doormat."
                
                show dravenia neutral
                        
                d "Well..."
                
                menu:  
                    
                    d "{cps=0}Well...{/cps}"
                    
                    "'Please, Dravenia, I'll be fine. I'll scream loud enough to wake the house if I get in trouble.'":
                        
                        show dravenia stern
                        
                        d "But if a slime smothers you the only sound you'll be able to make is-"
                        
                        show dravenia neutral
                        
                        d "..."
                        
                        d "Forgive me. I see that I am being rather overbearing.'"
                        
                    "'Are you trying to protect me, or are you just trying to show off?'":
                        
                        show dravenia shocked
                        
                        d "Wha-"
                    
                        show dravenia vangry
                    
                        d "I'm...!"
                        
                        d "..."
                        
                        show dravenia sad
                        
                        d "...Sincerest apologies, sir. That was an unprofessional outburst. More importantly, you are right - perhaps I am getting somewhat carried away."
            
                        d "Nevertheless, I swear my concern is genuine. You think me paranoid, but caution is trained into us above all else."

        show dravenia closed

        d "With that said, could I give you something to set my mind at ease?"
        
        pc "Oh? What?"
        
        "Dravenia reaches into her suit, revealing a thin, black band - an armband or watch, by the looks of it. Very stylish - the face is flat, and seems to be inset. A button?"
        
        show dravenia neutral
        
        d "Pressing this button will immediately alert me if you are in danger, and open a two-way line of communication between us."
        
        d "You will then be able to either explain the dangerous situation to the best of your ability, or cancel the alert in the case of a false alarm."
        
        menu:
            
            d "{cps=0}You will then be able to either explain the dangerous situation to the best of your ability, or cancel the alert in the case of a false alarm.{/cps}"
            
            "'Is this necessary...?'":
                
                d "Necessary? No. But the alternative is me hovering in close proximity to you for the majority of the day. Including during private activities."
                
            "'What if someone forces me to tell you it's a false alarm?'":
                
                d "Ah, an astute question, sir! And one I was just about to address."
                
        d "In the rare event you are essentially 'held at gunpoint' and forced to tell me the press was a false alarm, you need merely speak the words... ah."
        
#       Codeword is 'spilled my drink'
        
        "Dravenia glances around."
        
        d "Perhaps I shall elaborate when I can be absolutely sure we aren't being overheard."
        
        d "For now, though, it is unlikely such a fringe scenario will come to pass."
        
        if flag_intro_DraveniaAccompanies:
            
            d "Especially with myself in such proximity!"
            
            pc "You know you'll still be outside the room, right? And not eavesdropping?"
            
            pc "Assuming she's even {i}in{/i} her room."
            
            d "Of course. To a Hellguard, a measly door is nothing."
            
            pc "Just don't break anything. Bondhouses charge a lot for property damage..."
            
        else:
            
            d "..."
            
            show dravenia sad
            
            d "I suppose this is goodbye..."
            
            pc "C'mon, Dravenia, don't be so dramatic. I'll be fine."
            
            d "Yes, sir..."
            
        jump intro_viscellachatconspiracy
            
    label intro_viscellachatconspiracy:
        
        "Here we go, scene change."

###################################################################################CURRENT###############################################################################################
        
    label ch2_scene09:
        
        scene bg kitchen with dissolve
        
        "Now, let's see what we've got..."
        
        "..."
        
        "Cereal, cereal, and more cereal. Nothing exciting, either - just boxes upon boxes of bran flakes. It'll have to do."
        
        "I grab a box, and close the cupboard - only to find myself face-to-face with, well..."
        
        show kamao neutral at kamao_center with dissolve
        
        ka "Hey."
        
        pc "Uh... hey."
        
        "I vaguely recall that Dravenia instructed me to scream should anything happen to me, but... I should be okay."
        
        ka "Whatcha doin'?"
        
        "I heft the box."
        
        pc "Eating."
        
        show kamao shocked
        
        ka "Eugh. Are you one of those health nuts?"
        
        pc "This is all they had."
        
        show kamao confused
        
        ka "What? For real? Nothing with marshmellows?"
        
        pc "Nope."
        
        show kamao bored
        
        ka "Wow, guess it's time to move out..."
        
        ka "..."
        
        show kamao vhappy
        
        ka "Anyways! Come swimming with me!"
        
        pc "Uh... swimming?"
        
        show kamao happy
        
        ka "Swimming! I was looking around after the dragon punted me out and discovered that the big shed in the backyard is actually..."
        
        show kamao neutral
        
        ka "Wait for it..."
        
        show kamao vhappy
        
        ka "An indoor pool!"
        
        show kamao wink
        
        ka "So let's go. Last one there has to skinny dip."
        
        show kamao with MoveTransition(0.2):
            xpos 0
            
        play sound "assets/sound/sfx/body_hit.wav"
    
        show kamao pained
        
        show nagi neutral at nagi_farleft with vpunch:
            xpos -0.5
        
        ka "Oof!"
        
        n "Oh. Hello."
           
        show kamao at kamao_center
        
        show nagi bored at nagi_left
        
        with dissolve
        
        ka "Mffmfffm?!"
        
        n "Having fun?"
        
        show kamao embarrassed at kamao_right with move
           
        ka "Gah! Huah! I c-can breathe! I thought I was g-gonna {i}suffocate{/i} in that marshmellow hell!"
        
        show nagi confused
        
        n "Yeah. You hated it. Which is why you shoved your face downwards when you ran into me."
           
        ka "..."
           
        show kamao sleepy
           
        ka "Yeah..."
           
        n "..."
           
        show nagi closed
           
        n "*Sigh*."
        
        show nagi neutral
        
        n "Where were you off to in such a hurry, hm? Vibrator finish charging?"
        
        show kamao unhappy
        
        ka "{i}Excuse me{/i}! I'll have you know I have a {i}backup{/i} vibe for when one runs outta juice!"
        
        show nagi bored
        
        ka "What do I look like to you, some sorta barbarian? Jeeze."
           
        show kamao neutral
           
        ka "Anyways, [pc] and I were gonna go for swim! One of us was gonna be naked. One thing would lead to another, and soon we'd {i}both{/i} be naked."
        
        n "Uh-huh."
        
        show nagi neutral
        
        n "Hey, [pc], you wanna go shopping? You've barely got any worldly possessions, not to mention clothes. It's on me."
        
        show kamao unhappy
        
        ka "He- wha?! I just {i}told{/i} you we were going swimming!"
           
        show kamao horny
        
        ka "C'mon, [pc], do you want snaketits' pity cash or my scantily-clad-slash-naked-body, huh? Huh?!"
           
        menu:
            
            "'I don't recall agreeing to go swimming...'":
                
                $ n_like += 1
                
                show nagi happy
                
                show kamao unhappy
                
                ka "You were getting around to it!"
                
                pc "Sure, but... {i}pity cash{/i}."
                
                n "Cool. I need to use the washroom, then I'll get my car ready."
                
                show nagi wink
                
                n "My {i}sports car{/i}."
                show kamao flustered
                
                ka "Nooooo!"
                
            "'Sorry, Nagi, she beat you to it.'":
                
                $ ka_like += 1
                
                show nagi surprised
                
                show kamao confident
                
                n "You're actually... are you sure?"
                
                show nagi confused
                
                n "Hint hint, I'm giving you an out."
                
                pc "Thanks, Nagi, but if she goes swimming alone she'll probably knock herself out with a pool noodle."
                
                show nagi neutral
                
                show kamao embarrassed
                
                ka "Hey, those things can pack a {i}punch{/i}."
                
                n "Well, alright. I'm still buying you things, though. I'll just drag Fenira to the store instead."
                
                show nagi confident
                
                show kamao neutral
                
                n "Hope you like assless chaps."
                
                pc "Please tell me you're-"
                
                hide nagi with dissolve
                
                pc "...Well. Assless chaps it is."
                
                ka "I'm not complaining."
           
        "Test"

            
    
    "*TEMPEND*"
    
    $ renpy.pause(20.0, hard = True)


    "*TEMPEND*"

    $ renpy.pause(20.0, hard = True)


            
