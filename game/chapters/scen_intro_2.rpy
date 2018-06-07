
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
        
        ka "Who do I look like, a bodybuilder? I'm basically a paperweight with legs!"
        
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
        
        "...No, I'm not. I need to sort out my thoughts."
        
        d "I had just asked if there was any reason you needed to see the slime, and it seemed to set you off daydreaming."
        
        pc "Sorry. Again, distracted... I think I'm going to go for a walk."
        
        show dravenia happy
        
        d "Very well. Would you like me to bring an umbrella? It seems quite overcast."
        
        pc "Actually... I think this is something that needs privacy. Sorry, Dravenia."
        
        show dravenia neutral
        
        d "I ask again - is everything alright?"
        
        pc "Maybe. But I need some alone time to find out."
        
        d "I see... you understand that I am reluctant to part with you."
        
        pc "Yeah..."
        
        show dravenia closed
        
        d "Thankfully, I have been meaning to give you something that will hopefully set both our minds at ease."
        
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
                
                show dravenia happy
                
                d "Ah, an astute question, sir! And one I was just about to address."
                
        d "In the rare event you are essentially 'held at gunpoint' and forced to tell me the press was a false alarm, you need merely speak the words... ah."
        
#       Codeword is 'spilled my drink'
        
        show dravenia neutral
        
        "Dravenia glances around."
        
        d "Perhaps I shall elaborate when I can be absolutely sure we aren't being overheard."
        
        d "For now, though, I do hope you enjoy your walk."
        
        d "I will be in the yard. If you require my aid, be sure to press the button. Failing that, a shout or scream will suffice."
        
        "I strap the device around my wrist. It's pretty light, and not at all uncomfortable."
        
        pc "Thanks, Dravenia."
        
        show dravenia happy
        
        d "Of course."
        
        stop music fadeout 1.0
            
        jump intro_lonewalk
            
    label intro_lonewalk:
        
        scene bg yard with dissolve
        
        play music "assets/sound/bgm/tam-n17.mp3" fadein 3.0
        
        "Fresh air... that's nice."
        
        "At least the sky remains the same no matter where I am, or what sort of insanity's brewing all around me..."
        
        "Alright. Let's cover what I know so far."
        
        "Allise claims to be holding me in some sort of time loop."
        
        "And... she 'proved' this by telling me a story from my past that I've never told anyone."
        
        "And she's right. I've never told anyone that story, not even to my closest friends - and I haven't had many. I've never even written it down anywhere."
        
        "But that doesn't necessarily prove anything. She could have been spying on me on that day. Either that, or she can read minds."
        
        "...None of these options seem likely."
        
        "I was in the basement when I nearly gassed myself. She would have had to be in the room with me. Besides, that was nearly ten years ago."
        
        "I've heard that some rare and powerful chimera can read minds, but it's not an easy task. They always need a lot of time and energy. They can't just do it on a whim, and the odds they'd be able to do it without their victim knowing is pretty low."
        
        "But, still... a chimera powerful enough to read minds on a whim is still more likely than one capable of trapping someone in a time-travel bubble. I mean, at least the former's got {i}some{/i} sort of precedent."
        
        "So let's assume that's the case: Allise isn't really a human, but is actually some sort of chimera unknown to the public capable of incredible feats."
        
        "If that's so, why's she bothering with me? What's so important about me making some sort of permanent bond with someone that she's involving herself like this? And why tell me about all this time travel stuff when she could just threaten me like a normal person?"
        
        "Maybe she's just crazy? I don't know..."
        
        "Well, I suppose I could tell Dravenia about all of this. She's supposed to be an expert on all sorts of Chimera. She might be able to help."
        
        "But... what if Allise is telling the truth? What if I {i}am{/i} trapped in some sort of time loop?"
        
        "She told me if I tried telling anyone the truth, she'd just restart it again, and I'd go through this all over again without any of my memories. That doesn't sound very fun."
        
        "Maybe I should play along for now? I mean, technically, all she's demanding is I make a close friend. It's not like I'm being forced to kill someone."
        
        "It couldn't hurt. This could be a chance to learn more about chimera."
        
        "And I've never really been close to any of my friends..."
        
        "What should I do?"
        
        menu:
            
            "{cps=0}What should I do?{/cps}"
            
            "Trust Allise and resolve to make a friend.":
                
                jump intro_trustallise

            "Doubt Allise and go to Dravenia.":
                
                "Should I explicitly ignore Allise's demands and go tell Dravenia everything?"
                
                "This could get messy - I doubt Dravenia will be happy with Allise."
                
                "And on the off-chance Allise is telling the truth, all of it will be for naught - she'll just start me off from the beginning of the time loop without any of my memories."
                
                "It'd almost be like restarting a game, as crazy as that sounds."
                
                "Though maybe that's not a bad thing. Maybe I'd act slightly differently and see different sides of the people I've met."
                
                menu:
                    
                    "Risk starting from the beginning? After this, there's no going back."
                    
                    "Yes. A restart could help me try different things.":
                        
                        "Here goes nothing..."
                        
                        jump intro_tattlereset
                        
                    "On second thought, I'll play along with Allise.":
                    
                        jump intro_trustallise
        
    label intro_tattlereset:
        
        "TEMP"
        
        a "I see you've decided to disobey my instructions."
        
        a "A dissapointment, perhaps, but not a surprise."
        
        a "Perhaps you will prove more willing in the next cycle."
        
        jump start    
        
    label intro_trustallise:
        
        "I guess I should just go with the flow, for now. I can always try to find a way out later if things start getting bad."
        
        "But still, isn't this a little artificial? It's not like normal friendships start by looking at someone and saying 'I'm going to get close to that person', right?"
        
        "Asking me to just 'decide' isn't really natural at all. It's like Allise doesn't even understand how relationships really work."
        
        "Not that I have much of a choice."
        
        "The people here seem nice enough, and I don't think I've gotten off on the wrong foot with any of them. I just need to choose one."
        
        "The question is... who?"
        
        f "Watch out!"
        
        stop music
        
        play sound "assets/sound/sfx/body_hit.wav"

        show black with vpunch
        
        "I'm suddenly face-down in the grass. My head is ringing, and there's a dull sensation throbbing merrily at the back of my skull. It's still numb - I'm almost scared to acknowledge it, lest it turn to pain."
        
        ka "You- you killed him! You {i}killed{/i} my {i}boyfriend{/i}!"
        
        f "He's not dead, you idiot! [pc]? Are you alright? Can you hear me?"
        
        menu:
            
            f "{cps=0}He's not dead, you idiot! [pc]? Are you alright? Can you hear me?{/cps}"
            
            "'I'm alive...'":
                
                f "Oh, thank god."
                
                ka "Thank god? What're you so relieved for? You called me an idiot for thinking he was dead!"
                
                f "Would you shut up?"
                
                ka "Shut up? I was grieving - is that how you deal with grieving people? By telling them to shut up? I'm going to have to suggest some sensitivity training, or else-"
                
                f "If you don't shut up I'm going to shove my foot so far up your ass that I'll be able to use you as landing gear."
                
                ka "Shutting up."
                
                f "Need a hand?"
                
                "I roll over, wincing as a few jolts of pain prick against my skull."
                
                scene bg yard 
        
                show fenira neutral at fenira_left
        
                show kamao neutral at kamao_right
        
                with fade
                
                "I take Fenira's proffered 'hand' and use it to pull myself off the grass, brushing off my clothes once I'm on steady footing."
                
            "Fake your death.":
                
                "I say nothing, and remain as motionless as possible."
        
                ka "I knew it! You really {i}did{/i} kill him!"
                
                f "Oh, shut up! He's fine!"
                
                "I suddenly feel a pair of downy feathers press into my neck and hold there for several seconds."
                
                f "He's got a pulse."
                
                ka "Really? Can I feel?"
                
                f "If you want."
                
                ka "Great. I'm going to test his pulse straight through his thick, throbbing-"
                
                "I manage to roll over at such speed that even I'm impressed."
                
                scene bg yard 
        
                show fenira shocked at fenira_left
        
                show kamao shocked at kamao_right
                
                pc "I'M OKAY!"
                
                ka "ZOMBIE."
                
                show fenira neutral
                
                f "Ugh."
                
                f "C'mon, you were gonna test his pulse through his {i}dick{/i}? What kinda line is that? Who gets hard after taking a soccer ball to the head?"
                
                show kamao unhappy
                
                ka "Hey, it got him up, didn't it?"
                
                ka "And maybe he's a masochist. You don't know."
                
                "Ignoring the banter, I push myself off the grass and brush off my clothes."
                
        f "Really sorry about that, I didn't see you until it was too late..."
        
        show kamao neutral
        
        ka "I think she just hates your guts."
        
        show fenira angry
        
        f "The only guts I hate are yours."
        
        pc "What are you even doing out here, Kamao? Last I saw you Dravenia was dragging you around by the ear."
        
        show fenira neutral
        
        f "Oh, the new dragon chick? Yeah, she basically dumped this furball on my lap and told me to babysit, so I was being nice and tried letting her play soccer with me. She's pretty bad at it."
        
        show kamao neutral
        
        ka "Don't believe her. I came outside so I wouldn't have to keep breathing in the smell of desperate virgin assaulting me from in there."
        
        f "You could fix that by taking a shower."
        
        show kamao unhappy
        
        ka "I'm not talking about {i}my{/i} smell, I'm talking about everyone else's! You're all crawling over [pc] trying to get as much screentime as possible!"
        
        f "I'm pretty sure that's just you."
        
        ka "Are you kidding? I haven't gotten {i}nearly{/i} enough time with [pc]."
        
        if flag_VisitedKamao:
            
            ka "Even though he did come to visit me yesterday."
            
            ka "All on his own."
            
            ka "Of his own free will."
            
            ka "To visit me."
            
            ka "It's still not enough, y'know?"
            
        show kamao neutral
        
        ka "Speaking of spending time together, you know what we should do, [pc]?"
        
        pc "I'm afraid to ask."
        
        show kamao happy
        
        ka "Well, they have a pool here, so I was thinking - let's go swimming!"
        
        show fenira happy
        
        f "Y'know... that might be fun, actually."
        
        show kamao bored
        
        play music "assets/sound/bgm/tack.mp3" fadein 5.0
        
        ka "Sorry, who were you again?"
        
        ka "I was asking [pc]."
        
        show fenira angry
        
        f "Well, now {i}I'm{/i} asking [pc]. C'mon, man, let's ditch this bitch."
        
        show kamao angry
        
        ka "Whoa, whoa, hold on, you can't just call me a bitch {i}and{/i} steal my boyfriend in one sentence."
        
        show fenira smirk
        
        f "Really? Because I'm pretty sure I just did. C'mon, [pc], let's go for a swim."
        
        show kamao shocked
        
        pc "I don't think I brought any swimming trunks..."
        
        show fenira happy
        
        f "Really? I got some. They'd probably fit you."
        
        show kamao vangry
        
        ka "N-no way! I'm not gonna let you call me a bitch, steal my boyfriend, {i}and{/i} let him wear stuff your butt's touched! No way! Nuh-uh! And what are you even doing with male swimming trunks, you pervert!"

        show fenira neutral
        
        f "The hell's wrong with it? They fit me and they're comfortable. I don't actually use them for swimming, just as shorts."
        
        show kamao embarrassed_open
        
        ka "Careful, [pc]. I bet she's one of those weirdos that gets turned on when they're wearing guys' clothing. Those shorts are gonna be {i}soaked{/i}."
        
        show fenira angry
        
        f "That's it, pipsqueak. I've tried being nice."
        
        show kamao neutral
        
        ka "Ooh, hit close to home, did I?"
        
        n "Alright, I've seen all I need to see."

        stop music fadeout 3.0

        show fenira shocked
        
        show kamao shocked
        
        f "Ah, fuck..."

        show fenira shocked at fenira_farleft
        
        show kamao shocked at kamao_farright

        show nagi bored at nagi_center
        
        with dissolve

        "I turn around - only to find myself standing face-to-face with Nagi. She's not paying me much attention, and passes by as if she hadn't noticed me."

        play music "assets/sound/bgm/068.mp3" fadein 3.0

        n "What the hell is wrong with you two?"
        
        show kamao angry
        
        ka "Your friend's got one too many eggs shoved up her ass."
        
        show fenira angry
        
        f "Move, Nagi, this furball needs to be taught some manners."
        
        "Nagi does move. Her arms, that is. She slaps fenira across the face, and her tail echoes the movement - lashing against Kamao's cheek with whiplike accuracy and leaving both chimera in shock."
        
        show fenira shocked
        
        show kamao shocked
        
        n "I heard that *whump* through my bedroom window, and look out my window to see [pc] face-down on the ground."
        
        n "I get out here, expecting to hear some apologies. And what do I get? A fucking pissing match."
        
        n "The kid's clearly unfamiliar with chimera, and you two immediately start going all out with the most tired, over-the-top stereotypes imaginable."
        
        n "Seriously? Fighting over a human you just met? Hasn't that trope gotten a little tired by now?"
        
        n "The fox I can understand, but you, Fenira? You're better than this."
        
        show fenira smirk_open
        
        f "...You must've practiced that speech for hours, Snaketits."
        
        n "Oh, please, cut the act. You're just trying to distract from the fact you got carried away on an adrenaline rush because the fox pissed you off."
        
        show fenira sad
        
        f "..."
        
        n "Did either of you even consider just asking him who he wanted to hang out with? No."
        
        n "You didn't even ask him if he wanted to go in the first place - you just assumed he would." 
        
        n "After all, he's a weak, passive human and you're a tough chimera, and what choice does he have, right?"
        
        show kamao sad
        
        show fenira angry
        
        f "Okay, hold on, that's not-"
        
        n "Maybe, but that's what it looked like. And is that really the person either of you wanna look like?"
        
        show fenira sad
        
        ka "I was just playing around..."

        n "Could've fooled me. What do you think, [pc]?"
        
        pc "Me? About what?"
        
        show nagi neutral
        
        n "Yes, you. C'mon, assert yourself." 
        
        n "Are you really happy having other people make your choices for you?"
        
        pc "Well... I suppose everyone wants some agency in their life."
        
        n "There you have it. Now be responsible adults and apologize."
        
        f "You're just showing off how mature you are..."
        
        n "And now you're showing off how immature you are."
        
        f "Ugh... sorry, [pc]."
        
        ka "Even if you don't believe me, I'm sorry, too."
        
        n "There, done. How's your head, [pc]?"
        
        "Nagi's reminder of my injury just sends a dull throb through my head."
        
        pc "Ugh... little sore, but I'm alright."
        
        n "Need an ice pack or anything?"
        
        pc "Nah, it's not that bad. I'll be okay. Thanks, though."
        
        n "Hey, no problem. So, {i}were{/i} you interested in going swimming?"
        
        "I nod. It might be a good chance to get to know the others, considering the choice lying ahead. In fact..."
        
        pc "Actually... why don't we all go? You too, Nagi."
        
        n "Great idea. I could go for a swim."
        
        show fenira shocked
        
        "I notice a look of palpable horror in Fenira's eyes, but it passes as quickly as it came."
        
        show fenira neutral
        
        f "...That's cool, I guess."
        
        show kamao shocked
        
        ka "Wait. Does that mean she's going to be wearing-"
        
        f "Don't... don't say it out loud."
        
        "Kamao's now the one wearing the look of horror, but unlike with Fenira, this one sticks."
        
        show fenira happy
        
        f "Alright, well... I'll go get you something to wear, [pc]."
        
        pc "Thanks."
        
        hide fenira with dissolve
        
        pc "While she's doing that, I'll let Dravenia know what's up."
        
        show kamao unhappy
        
        ka "Don't bring her along, too! I've got enough competition to deal with!"
        
        n "I'll go make sure the pool's warm. Wouldn't want to go into hypothermic shock."
        
        pc "You're cold-blooded, Nagi?"
        
        n "Mmh? Yeah, but lamia blood's got a natural antifreeze, so I'll be fine. I was talking about Fenira. Phoenixes don't like the cold - who'dve thought?"
        
        hide nagi with dissolve
        
        show kamao unhappy at kamao_center with move
        
        ka "..."
        
        ka "I'm really sorry about being an inconsiderate ass."
        
        show kamao teasing
        
        "I'll make it up to you with a nip slip."
        
        hide kamao with dissolve
        
        "Well, she's back to her usual self."
        
        menu:
            
            "{cps=0}Well, she's back to her usual self.{/cps}"
            
            "What a relief.":
                
                "Yeah, that was kind of weird."
                
            "What a dissapointment.":
                
                "I was kind of impressed at how serious she was being. Well, at least now I know she's {i}capable{/i} of it. Probably."
        
        "Oh well. Better go let Dravenia know what I'm up to, or she's liable to start worrying."
        
        jump intro_draveniaupdate
        
    label intro_draveniaupdate:
        
        scene bg living with wipeleft
        
        d "Ah, there you are! I was beginning to grow worried!"
        
        "Welp..."
        
        show dravenia neutral at dravenia_center with dissolve
        
        d "Is your head okay? Are you dizzy? How many fingers am I holding up?"
        
        pc "Three. I'm fine, Dravenia."
        
        show dravenia sad
        
        d "Forgive me. I should have rushed to your side, but... Miss Forques told me that if I did so, I would be no better than..."
        
        d "Ah, forget I said anything. I have no excuse."
        
        "Her head hangs."
        
        d "My deepest, sincerest apologies."
        
        menu:
            
            d "{cps=0}My deepest, sincerest apologies.{/cps}"
            
            "'Don't worry about it. It wasn't severe.'":
                
                d "Regardless, it is my job to be prevent you from coming to harm, and I have already failed..."
                
                pc "C'mon, Dravenia. You can't protect me from every trivial injury. I don't expect you to beg forgiveness for every papercut, right?"
                
                show dravenia neutral
                
                d "But if I were to make you wear gloves, then-"
                
                pc "Dravenia."
                
                show dravenia happy
                
                d "A joke, sir."
                
                show dravenia neutral
                
                d "Though perhaps with my behaviour it can be rather difficult to tell... hmm..."
                
                d "N-nevertheless. Please forgive my concern, sir. I am merely, ah..."
                
            "'I'm sort of glad you didn't, honestly. I don't need babysitting.'":
                
                d "I suppose that's true, but..."
                
                pc "Take it easy, Dravenia. I'm an adult. I can handle myself."
                
                pc "If I felt I was in any real danger I would've used this, remember?"
                
                "I hold up the bracelet she'd given me earlier."
                
                show dravenia neutral
    
                d "You are right, of course. Forgive me my concern, I am merely..."
                
        pc "Anxious for your first day at the job, right?"
        
        d "...Yes."
        
        pc "Don't worry about it. Just relax a little, okay? I'm going to go for a swim."
        
        d "With whom, may I ask?"
        
        pc "Nagi, Fenira, and Kamao."
        
        d "...Is that wise?"
        
        pc "Probably not. Is your bracelet waterproof?"
        
        "She nods."
        
        d "Up to a depth of one-hundred meters, yes. Would you like for me to attend you?"
        
        ku "Ah, there you are!"
        
        show dravenia at dravenia_right with move
        
        show kumiru shocked at kumiru_left with dissolve
        
        ku "O-oh."
        
        show kumiru neutral
        
        ku "You must be the dragon Viscella was stammering to me about. Forgive me, she didn't give me your name..."
        
        d "Dravenia Talonstein."
        
        ku "Good to meet you, Miss Talonstein."
        
        d "Dravenia is sufficient."
        
        ku "Dravenia, then."
        
        "Kumiru looks back to me, fidgeting somewhat. Looks like she wasn't expecting to run into two of us."
        
        ku "Um, if you two are in the middle of something..."
        
        pc "Don't worry about it. What's up?"
        
        ku "Well..."
        
        "Her eyes dart from me to my bodyguard."
        
        ku "I was thinking of doing something to get to know the other tenants better. Break the ice, sort of."
        
        d "Ah, fostering communication during the early stages of cohabilitation is a clever idea."
        
        ku "Oh? Ah- thanks. I thought it might help make everyone more comfortable. Especially Viscella."
        
        d "What did you have in mind?"
        
        ku "Well, it's sort of nerdy, but I thought you at least might be interested, [pc]..."
        
        "Is that a compliment, or...?"
        
        ku "Have you ever played a tabletop RPG before?"
        
        show dravenia shocked
        
        pc "Oh, like Ruins & Revenants? I've wanted to for a while now, but I never had the chance..."
        
        show kumiru happy
        
        ku "Really? Perfect! Viscella and I are the same way! But you can't really have a proper RPG with only two people, y'know?"
        
        show kumiru neutral
        
        show dravenia neutral
        
        ku "The problem is, we've only got the books and the internet for help. I'm okay running the session, but I'm not exactly familiar with the rules or anything, so it might be sort of slow at first..."

        d "Is that so? If you are not opposed to my joining, I could run the session."
        
        show kumiru shocked
        
        ku "S-sorry?"
        
        d "I understand if you'd prefer I abstain. I do seem to frighten your friend."
  
        ku "No, no! It's not that, it's just... I'm surprised. You don't look the type."
        
        d "Really? I've been playing them for years - especially R&R, though I haven't been shy about trying other genres and rulesets. I even ran a few games with the other recruits back in boot camp."
        
        show kumiru happy
        
        ku "That's great! We'd love it if you could run a one-shot for us!"
        
        d "I would be glad to. If successful, we could consider running it on a more regular basis. Will your friend be amenable to my company?"
        
        ku "Viscella will get used to you eventually, I'm sure of it. I'm sure she'll warm right up when she finds out you volunteered to run our game."
        
        show dravenia happy
        
        d "I am glad to hear that. [pc], would you be joining us?"
        
        pc "Urgh... I really want to, but I told the others I'd go swimming with them."
        
        show kumiru neutral
        
        ku "Oh, you're going swimming? S-sorry... I got a little carried away before even asking if you were busy..."
        
        show dravenia smug
        
        d "Fret not, sir. Go fulfill your promise - I am sure we will still be in the midst of character creation when you return. It is a lengthly process for new players."
        
        pc "You'll save a seat for me?"
        
        show dravenia happy
        
        d "Of course, sir."
        
        show kumiru happy
        
        ku "Have fun!"
        
        pc "Thanks - go ahead and start without me if I'm not back in good time."
        
        hide dravenia
        
        hide kumiru
        
        with dissolve
        
        "I turn around to leave, and nearly run face-first into Fenira."
        
        show fenira shocked at fenira_center
        
        f "Oof - sorry!" 
        
        show fenira smirk_open
        
        "She looks like she's about to say something clever, but after holding her mouth open for a few moments she clears her throat and turns a little red."
        
        show fenira embarrassed
        
        f "N-nevermind. Here's your shorts."
        
        pc "For me? You think they'll fit?"
        
        show fenira happy
        
        f "Sure! Maybe. Probably?" 
        
        show fenira smirk
        
        f "I mean, you got pretty wide hips for a dude."
        
        f "..."
        
        show fenira flustered
        
        f "Just kidding! I don't think you're, y'know, feminine or anything!"
        
        show fenira bluffing
        
        f "Well, unless you {i}like{/i} being feminine, in which case, damn, you've got nice curves! Ahaha! Haah!"
        
        show fenira neutral
        
        f "..."
        
        show fenira embarrassed
        
        f "...I'm gonna go get changed. Please pretend this never happened."
        
        menu:
            
            f "{cps=0}...I'm gonna go get changed. Please pretend this never happened.{/cps}"
            
            "'What never happened?":
                
                f "Hah, thanks... you're a champ."
                
                f "I swear I'm not usually this much of a dumpster fire."
                
                "She lets out a heavy sigh."
                
                f "See you in a bit..."
                
            "'I've got nice curves, do I?'":
                
                show fenira bluffing
                
                f "Yes! I mean, d-do you want curves? If you don't, I'd say it's less curvy and more, y'know, uh, blocky. Very masculine."
                
                f "..."
                
                show fenira neutral
                
                f "I think I'm gonna sandwhich my head between some pillows and pretend I was never born. I'll catch up to you."
        
        hide fenira with dissolve
        
        "Well, that was entertaining."
        
        scene bg hallway with wipeleft
        
        "Slipping into the bathroom, I undress and try on Fenira's trunks. She's right - they're a pretty good fit. What they lack in flair they make up for in comfort. Nodding to myself in the mirror, I pull on my shirt and socks and head out to the pool."
        
        #temp jump
        
        jump intro_poolparty
        
    label intro_poolparty:
    
        scene bg pool with Dissolve(3.0)
        
        "Stepping into the poolhouse, the humidity is intense. It's warm - the smell of chlorine wafts into my nostrils and reminds me of the pool at my old community center. The memories fade quite quickly, however, when I spot Kamao desperately propped against the changeroom door."
        
        $ ka_Outfit = 1
        
        show kamao neutral at kamao_center with dissolve
        
        ka "O-oh, hey! It's [pc], back already. Where's your swimsuit!"
        
        "She seems to have wedged a chair under the doorknob, and is putting all her weight into keeping the door closed."
        
        pc "I'm wearing it, actually."
        
        ka "Oh, are those the bird's shorts? They look better on you. You gonna swim with your shirt on?"
        
        pc "No, but... what are you doing?"
        
        show kamao happy
        
        ka "Me? Nothing. Nothing at all! Just resting, waiting for my favourite stud to come back and show a little skin!"
        
        "Suddenly, the door Kamao had barricaded opens."
        
        show kamao shocked
        
        ka "Huh?"

        show kamao with MoveTransition(0.3):
            xpos 0.66
            xanchor 0.2
            ypos 1.3
            yanchor 340
            
        play sound "assets/sound/sfx/body_hit.wav"
        
        show kamao pained with vpunch
        
        ka "Oof!"
        
        $ n_Outfit = 1
        
        show nagi bored at nagi_left with dissolve
        
        n "You know it's a pull door, right?"
        
        show kamao sad
        
        ka "I've... I've failed... it's all over..."
        
        show nagi neutral
        
        n "Oh, [pc]. There you are." 
           
        menu:
            
            n "{cps=0}Oh, [pc]. There you are.{/cps}" 
           
            "'I-Isn't that swimsuit a little much?'":
               
               show kamao unhappy
               
               ka "Yeah it's a little much! It's not even the right size for her! How are you supposed to {i}swim{/i} in that thing?!"
               
               show nagi bored
               
               n "You didn't suggest we go to the pool because you wanted to {i}swim{/i}, fox."
               
               n "You suggested we go to the pool so you could show off to the human and ogle him when he's not looking."
               
               n "I'm at least honest with myself. If we're gonna have a contrived swimsuit scene, I'm gonna roll with the punches."
               
               show nagi confident
               
               n "As for you, [pc], you don't have to be embarrassed on my behalf. It's unbecoming."
               
               show kamao neutral
               
               ka "You're just mad because he has good taste."
               
               show nagi bored
               
            "'You look great.'":
               
               show nagi happy
               
               n "Hey, thanks."
               
               show kamao unhappy
               
               ka "[pc], don't let them defeat you! Just imagine what she'll look like as an old lady! They'll be down to her knees!"
               
               show kamao confused
               
               ka "Or, y'know, where her knees {i}would{/i} be."
               
               show nagi bored
               
               n "Shut it."
               
               show kamao neutral
               
        show kamao at kamao_right with move
        
        show nagi neutral
        
        n "Pool's nice and warm. Hopefully we won't have to fish a birdcicle out of the water, but I can't make any promises."
                  
        pc "She's that sensitive to the cold?"
        
        n "You've got no idea. Her dad has to sleep in the basement because the rest of her family keeps the thermostat in the red."
        
        pc "Better than keeping it in the blue, like my family."
                
        n "Your folks keep it in the blue? I suppose that makes sense. I've heard humans sleep better in the cold."
            
        pc "I wouldn't necessarily say we sleep better in the {i}cold{/i}. My parents are just anal when it comes to spending on that sort of stuff."
                
        n "Frugal, huh?"
                
        pc "That's one word for it."
                
        n "..."
               
        show nagi confused
               
        n "Alright, what's the deal? You've had plenty of chances to interject. Hell, he just said 'anal' and you kept your mouth shut."
        
        "Kamao, who had been staring expectantly at me, blinks away her reverie."
        
        show kamao bored
        
        ka "Hm? What?"
        
        show nagi bored
        
        n "I asked what you were doing."
        
        ka "Uh... waiting."
        
        n "Waiting for?"
        
        ka "Nothing."
        
        $ intro_shirtRemove = False
        
        menu:
            
            ka "{cps=0}Nothing.{/cps}"
        
            "'Yes, Kamao, you look good.'":
                
                $ intro_KamaoSwimsuitCanadian = False
                
                $ ka_like += 1
                
                show kamao embarrassed
                
                ka "R-really? You think so?"
                
                show nagi bored
                
                n "Oh, that's what you were waiting for."
                
                ka "Please, just let me have this."
                
                show nagi neutral
                
                n "...Fine."
                
            "'What's up with your swimsuit pattern?'":
                
                $ intro_KamaoSwimsuitCanadian = True
                
                show kamao shocked
                
                ka "W-what do you mean, 'what's up' with it?"

                show kamao confident
                
                ka "Just showing some national pride, obviously!"
        
                pc "You're... Canadian?"
                
                ka "Yup! Strong and free!"

                n "That explains a lot."
                
                show kamao confused
                
                ka "What's that supposed to mean?"
                
            "Continue ignoring her.":
                
                $ intro_KamaoSwimsuitCanadian = False
                
                pc "Where's Fenira, anyways?"
                
                n "I dunno. I thought the two of you would be showing up together."
                
                pc "Nah, she got embarrassed and ran off. She shouldn't be long."
                
                show nagi neutral
                
                n "That's so like her."
                
                show kamao sad
                
                ka "Mnh..."
        
        f "Sorry I'm late!"
        
        show nagi at nagi_farleft
        
        show kamao neutral at kamao_farright
        
        with move
        
        $ f_Outfit = 1
        
        show fenira happy at fenira_center behind kamao with dissolve
            
        f "Who's ready for laps?"
        
        show fenira neutral
        
        f "..."
        
        f "Are you Canadian?"
        
        if intro_KamaoSwimsuitCanadian:
        
            show kamao confused
            
            ka "You too? What, you guys think I just grabbed a random swimsuit out of a bargain bin?"
            
            f "So you are. This explains everything."
        
            show kamao bored
        
            ka "Why do you guys keep saying that..."
            
        else:
            
            show kamao confident
        
            ka "Yup! Born and raised."
        
            f "That explains everything."
        
            show kamao confused
        
            ka "What's that supposed to mean?"
        
        show fenira confused
            
        f "Wait... what's wrong with the rest of you? You're still dry, and [pc]'s still wearing his shirt. What, you guys just gonna gawk at each other?"
        
        menu:
            
            f "{cps=0}Wait... what's wrong with the rest of you? You're still dry, and [pc]'s still wearing his shirt. What, you guys just gonna gawk at each other?{/cps}"
            
#            "'Last one in gets to lock up!'":
                
#                show fenira happy
                
#                "After calling out my challenge, I immediately tug off my shirt. Fenira, seeing me burst into movement, begins to laugh - she's already mid-air by the time I've managed to get rid of my shirt."
                
#                hide fenira with dissolve
                
#                play sound "assets/sound/sfx/water_splash3.wav"
                
#                "Fenira performs a nice cannonball. Kamao's too busy staring at my chest to act, and Nagi seems to be enjoying watching the activity as a take a running start and leap, tucking in my legs and holding my breath as I crash into the water."
                
            "'Last one in has to take off a piece of clothing!'":
                
                stop music fadeout 2.0
                
                hide fenira

                hide kamao
                
                show nagi smug
                
                with flash
                
                "Before I even finish my sentence there's a flash of motion. Like lightning, two of the chimera fling themselves towards the pool. I only manage to process what has happened before they're hitting the water."
                
                play sound "assets/sound/sfx/water_splash1.wav"
                
                "Kamao first."
                
                play sound "assets/sound/sfx/water_splash2.wav"
                
                "Followed by Fenira."
                
                "Well, I guess I was asking for that one."
                
                ka "Damnit, you idiot! You're supposed to wait for him to take his shirt off and {i}then{/i} make a break for it - he would've had to take off his trunks!"
                
                f "You were the first one in, moron! I just followed on reflex!"
                
                ka "Uuugh, the chance of a {i}lifetime{/i}, wasted. At least we'll get to see some... wait! Snaketits!"
                
                play music "assets/sound/bgm/scene_comi2.ogg" fadein 1.0
                
                show nagi at nagi_center_flipped with move
                
                f "Woah! Did she catch on? Wait, what am I saying? Of {i}course{/i} she caught on!"
                
                show nagi confident
                
                pc "...Clever."
                
                n "I try."
                
                n "So."
                
                pc "So."
                
                n "This isn't very fair, is it?"
                
                n "We've both got a top and a bottom. It's socially acceptable for you to take your top off. Me? Not so much."
                
                n "Don't use double standards as a crutch."
                
                n "C'mon. Take it off."

                menu:
                    

                    n "{cps=0}C'mon. Take it off.{/cps}"
                    
                    "Raise the stakes and take off your shirt.":
                        
                        $ intro_shirtRemove = True
                        
                        "She's right, and I'm no coward."
                        
                        "I take off my shirt, and hear a pair of gasps from the pool."
                        
                        n "That's more like it. Nice chest, by the way. On three?"
                        
                        "I nod."
                        
                        n "Fenira, please."
                        
                        f "Huh? Oh! *Ahem*."
                        
                        f "One!"
                        
                        "If I lose this..."
                        
                        f "Two!"
                        
                        "Kamao's gonna see my junk."
                        
                        f "And..."
                        
                        stop music fadeout 2.0
                        
                        "I can't let that happen."
                        
                        f "Three!"
                        
                        "I fly like the wind."

                    "Run for it like a coward.":
                        
                        $ intro_shirtRemove = False
                        
                        "Show Kamao my junk? No. Not today."
                        
                        show nagi smug
                        
                        "I make a mad dash for the end of the pool - but Nagi's faster."
                        
                        stop music fadeout 2.0
                        
                        hide nagi with flash
                        
                        "She unravels like a spring, diving past me and dissapearing under the water with a loud splash, her tail coiling down past the surface. I'm barely able to stop my momentum from carrying me in."
                        
                        "I stand in defeated shame as Nagi resurfaces with a smug grin on her face, a chorus of playful boos being hurled at me by Kamao and Fenira."
                        
                        play music "assets/sound/bgm/068.mp3" fadein 3.0
                        
                        n "You lose."
 
                        pc "Yeah, yeah."
                        
                        "Sighing, I pull off my shirt. The booing quickly turns into encouragement, emphasized by Kamao's wolf whistle as I toss it to the side and jump in."
                        
           
            "'Nothing wrong with a bit of gawking.":
                
                show fenira happy
                
                f "Pft."
                
                n "Maybe {i}you've{/i} been enjoying gawking. How about you take your shirt off and give the rest of us something to look at?"
                
                show kamao unhappy
                
                ka "I agree with Snaketits."
            
                pc "Of course you do."
                
                "Sighing, I grab my collar and pull my shirt up over my head. Normally I wouldn't bat an eye at doing such a thing in public, but with these three staring it's a little awkward."
                
                show kamao horny
                
                show fenira embarrassed
                
                ka "Daaaaamn."
                
                "Nagi gives Kamao a whack upside the head."
                
                show kamao pained
                
                ka "Oof!"
                
                n "Stop making him uncomfortable."
                
                show kamao unhappy
            
                ka "I was giving him a compliment!"
                
                n "Not with that face you weren't. Speaking of shameless facial expressions, maybe you should take a dive, Fenira."
                
                show fenira shocked
                
                f "He- wha- hey! Don't put me in the same category as {i}her{/i}!"
            
                n "I just suggested you take a swim. Any 'categorizing' was strictly on your end."
            
                show fenira angry
            
                "Fenira huffs, before she turns around and takes a running jump into the deep end of the pool."
                
                hide fenira with dissolve
                
                play sound "assets/sound/sfx/water_splash2.wav"
                
                "Smirking, I follow suit."
                
        play sound "assets/sound/sfx/water_splash1.wav"
            
        hide fenira
        
        hide kamao
        
        hide nagi
        
        with flash
            
        $renpy.pause(0.9)    
        
        play sound "assets/sound/sfx/underwater.wav" loop
                
        if intro_shirtRemove:
            
            play music "assets/sound/bgm/068.mp3" fadein 3.0
            
            "It's done..."
            
            "I'll spend a moment down here before facing whatever fate the cards have dealt."
        
        "It's warm!"
            
        "I take a moment to enjoy the familiar sensation of swimming. I used to love it - I wish I'd kept it up."
            
        "Shaking my head, I break through the surface."
            
        stop sound
            
        play sound "assets/sound/sfx/water_splash3.wav"
        
        if intro_shirtRemove:
            
            n "And our winner surfaces."
            
            "I take a look around. Nagi's sitting on the edge of the pool, trailing her tail in the water and giving me a grin."
            
            show nagi happy at nagi_center
            
            show fenira sad at fenira_farleft
            
            show kamao angry at kamao_farright
            
            with dissolve
            
            "Fenira and Kamao look completely dismayed."
            
            f "Ugh, I knew this would happen..."
            
            n "He won fair and square."
            
            ka "You didn't even {i}try{/i}! You frolicked up to the edge of the pool like you were taking in the scenery!"
          
        else:
          
            show nagi neutral at nagi_center
            
            show fenira happy at fenira_farleft
            
            show kamao neutral at kamao_farright
            
            with dissolve
            
        jump intro_routeselect
    
###################################################################################CURRENT###############################################################################################
       
    
    label intro_routeselect:

        

        "Viscella: [v_like] Kumiru: [ku_like] Kamao: [ka_like] Nagi: [n_like] Fenira: [f_like] Dravenia: [d_like] Allise: [a_like]"

        #Viscella Pref
        
        if v_like > ka_like and v_like > ku_like and v_like > d_like and v_like > n_like and v_like > f_like and v_like > a_like:
            
            "Viscella and I seem to get along."
            
        #Kumiru Pref
        
        elif ku_like > v_like and ku_like > ka_like and ku_like > d_like and ku_like > n_like and ku_like > f_like and ku_like > a_like:
            
            "Kumiru and I seem to get along."
        
        #Kamao Pref
        
        elif ka_like > v_like and ka_like > ku_like and ka_like > d_like and ka_like > n_like and ka_like > f_like and ka_like > a_like:
            
            "As much as I hate to admit it... Kamao and I seem to get along."
            
        #Fenira Pref
        
        elif f_like > v_like and f_like > ka_like and f_like > d_like and f_like > n_like and f_like > ku_like and f_like > a_like:
            
            "Fenira and I seem to get along."
            
        #Nagi Pref
        
        elif n_like > v_like and n_like > ka_like and n_like > d_like and n_like > f_like and n_like > ku_like and n_like > a_like:
            
            "Nagi and I seem to get along."
            
        #Dravenia Pref
        
        elif d_like > v_like and d_like > ka_like and d_like > n_like and d_like > f_like and d_like > ku_like and d_like > a_like:
            
            "Dravenia and I seem to get along."
            
        #Allise Pref
        
        elif a_like > v_like and a_like > ku_like and a_like > d_like and a_like > f_like and a_like > n_like and a_like > ka_like:
            
            "Strangely enough... Allise and I seem to get along, in a weird way"
            
        else:
        
            "I seem to get along pretty well with a few tenants..."
        
        
 
           
        "Test"

            
    
    "*TEMPEND*"
    
    $ renpy.pause(20.0, hard = True)


    "*TEMPEND*"

    $ renpy.pause(20.0, hard = True)


            
