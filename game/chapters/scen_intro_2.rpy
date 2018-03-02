
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

        f "I was just trying to pass to our striker, but nope! Took her job, and she couldn't have been happier!"

        n "A shame you still lost 7-1."

        show fenira happy

        f "Hey, we may have lost, but at least I saved our pride."

        n "Only to have it torn away from you the following week."

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

        #    "..."

        #    "..."

        #    voice_a "Hey..."

        #    voice_a "Can you hear me?"

        #    voice_a "Easy, easy. Don't move around too much."

        #    voice_a "Are you alright? What's your name?"

        #    voice_b "My... name?"

        #    voice_a "Yeah. What's your name?"

        #    voice_b "..."

        #    voice_b "I have no name."

        #    voice_a "You don't? Well, what do your parents call you?"

        #    voice_b "...Parents?"

        #    voice_a "Yeah. Your mom and dad."

        #    voice_b "Mom and... dad?"

        #    voice_a "Don't tell me you don't have parents."

        #    voice_b "..."

        #    voice_a "This might be harder than I thought."

        #    voice_a "Don't worry about it, though. You should get back to rest. I don't know what you've been through, but it can't have been nice."

        #    voice_a "But before that, I guess you need a name, huh? Any ideas?"

        #    voice_b "..."

        #    voice_a "No? Nothing?"

        #    voice_b "...Why?"

        #    voice_a "Huh?"

        #    voice_b "Why do I need a name?"

        #    voice_a "What do you mean?"

        #    $ renpy.pause(1.0)

        #    voice_a "Everyone deserves a name."


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

        #    $ renpy.pause(2.0, hard = True)

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
        
        d "Confused? Understandable. For many, the prospect of a Hellguard guardian is but a distant dream. But I can assure you, this is no prank."
        
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
        
        d "As previously stated, I am a Hellguard."
        
        d "Our origins go back hundreds of years, when the first..."
        
        d "..."
        
        show dravenia smug
        
        d "Ah. Forgive me. Would you like the long or the short of it?"
        
        "She seems quite eager to talk my ear off..."
        
        menu:
            
            "'I've got time.'":
                
                $ d_like += 1
                
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
                
        
        ###################################### Temporary end of story #######################################
        
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
                
                $ d_love += 1
                
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
            xpos 0.1

        show dravenia:
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
        
        show kamao vhappy at kamao_left

        show kamao:
            xpos -3.0
        
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
        
        ka "What do I look like, Hulk Hogan? I'm basically a paperweight with legs!"
        
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
        
        jump ch2_scene02

    "*TEMPEND*"

    $ renpy.pause(20.0, hard = True)


            
