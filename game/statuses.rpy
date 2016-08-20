init python:
  
    import random
  
  # Black = ("#000000")
  # Green = ("#008000")
  # Red =   ("#ff0000")
  # Dark Red = ("#8b0000")
  
  # 
  
    stage1 = affection_max / 4
    stage2 = (affection_max * 2) / 4
    stage3 = (affection_max * 3) / 4
    stage4 = affection_max
  
    def getKumiruThoughts(likePts, lovePts):
      
        kumiThoughts = [ 
            "No, wait, quarter-circle back?",
            "I could try streaming...",
            "Maybe Viscella'd draw it?",
            "Would he top or bottom?",
            "Should I pre-order?",
            "[[CENSORED]",
            "What an intense dream...",
            "Was she trying to troll me?",
            "I was up way too late.",
            "Why'd they have to nerf it...",
            "My wrist is so tired...",
            "I'm craving a soda.",
            "Is that a- NOPE NOPE NOPE.",
            "I hope mother is well."
            ]
      
        return(random.choice(kumiThoughts))
  
    def getViscellaThoughts(likePts, lovePts):
      
        visThoughts = [ 
            "[[CENSORED]",
            "I'm cute... right?",
            "Dubs? Really?",
            "I should get the BDs.",
            "Makoto or Shinjiro? Hmm...",
            "I wanna drink some...",
            "I can't believe I drew that.",
            "My father would be ashamed...",
            "I hope this is waterproof.",
            "Only a few pages left!",
            "I wonder what I taste like?",
            "Maybe Kumi could help?",
            "I wish I could swim.",
            "Motivation... draining..."
            ]
      
        # "Maybe [pc] would model for me?"
      
        #return "T-too close to the sink..."
      
        return(random.choice(visThoughts))
  
    def getNagiThoughts(likePts, lovePts):
      
        nagiThoughts = [ 
            "Ah. Whoops.",
            "Bored, bored, bored.",
            "I'm not being mean, am I?",
            "I should play something.",
            "On a dark desert highway...",
            "My back's killing me.",
            "Good beat on this one.",
            "Am I shedding?",
            "I could eat a horse.",
            "Fenira'd make a cute guy.",
            "Not for honour, but for you...",
            "Windmill, windmill, for the land...",
            "They're not {i}that{/i} big...",
            "Asses are overrated."
            ]
      
        #return ""
      
        return(random.choice(nagiThoughts))
  
    def getKamaoThoughts(likePts, lovePts):
      
        kamThoughts = [ 
            "[[CENSORED]",
            "Catgirls get all the puns...",
            "I could go for a hot dog.",
            "I wonder how dad's doing?",
            "Fairy bitch...",
            "I'm totally gonna go blind.",
            "Bad libido! Bad!",
            "Pff, who needs tits?",
            "Fluffy...",
            "Death is inevitable...",
            "I need a drink.",
            "I'm so lonely...",
            "Technically we're not related..."
            ]
      
        #return "Depressive episode incoming..."
      
        return(random.choice(kamThoughts))
  
    def getFeniraThoughts(likePts, lovePts):
      
        fenThoughts = [ 
            "God I'm bored.",
            "I wonder what Nagi's up to?",
            "Being an adult sucks.",
            "What am I, twelve?",
            "I don't smell, do I?",
            "What's so great about flying?",
            "Nagi'd laugh me to death.",
            "Nah, soccer's way better.",
            "Nerds everywhere...",
            "Ugh, painful memories...",
            "[[CENSORED]",
            "Does she ever shut up?",
            "I'm getting antsy...",
            "Being a dude might be fun.",
            "If I had to pick a chick..."
            ]
      
        return(random.choice(fenThoughts))
  
  
    def getDraveniaThoughts(likePts, lovePts):
        
        rand = renpy.random.randint(1, 10)
        
        draThoughts = [
            "I should be training...",
            "I wish I weren't so tall.",
            "Am I alright as I am?",
            "It wasn't her fault...",
            "These wings are a pain.",
            "I could take her. Definitely.",
            "What an annoying creature.",
            "I'm paid too much for this.",
            "I'm not a brute... am I?",
            "I need a cold shower.",
            "If he could see me now...",
            "What an incredible ending.",
            "Why'd he have to die?",
            "Stop stepping on my tail...",
            "So... cute..."
            ]
            
        return(random.choice(draThoughts))
  
  
    def getAlliseThoughts(likePts, lovePts):
        
        rand = renpy.random.randint(1, 10)
        
        
        
#        allThoughts = [
#            "I'm sorry.",
#            "Can you hear me?",
#            "Forgive me.",
#            "It's rude to listen.",
#            "I love you.",
#            "Do you hate me?",
#            "It's all my fault."
#            ]
            
#        return(random.choice(allThoughts))

        return("!@*$%ERROR^&%$*")
  
  #Legend
  #Blip-Division Percentage
  #Blip 1-Div 8.00
  #Blip 2-Div 4.00
  #Blip 3-Div 2.66
  #Blip 4-Div 2.00
  #Blip 5-Div 1.60
  #Blip 6-Div 1.33
  #Blip 7-Div 1.14
  #Blip 8-Div 1.00
  
  #Love
  #Blip 1-Div 3 (1/3)
  #Blip 2-Div 1.5 (2/3)
  
  
    def getThoughts(likePts, lovePts):
            
        if likePts == 0:
            
            return "Strangers"
            
        elif likePts < (affection_max / 8):
            
            if lovePts < (affection_max / 3):
            
                return "Acquaintances"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts < (affection_max / 4):
            
            if lovePts < (affection_max / 3):
            
                return "Roommates"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts < (affection_max / 2.66):
            
            if lovePts < (affection_max / 3):
            
                return "Buddies"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts < (affection_max / 2.00):
            
            if lovePts < (affection_max / 3):
            
                return "Friends"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts < (affection_max / 1.60):
            
            if lovePts < (affection_max / 3):
            
                return "Good Friends"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts < (affection_max / 1.33):
            
            if lovePts < (affection_max / 3):
            
                return "Close Friends"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts < (affection_max / 1.14):
            
            if lovePts < (affection_max / 3):
            
                return "Best Buddies"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
        
        elif likePts < (affection_max / 1.00):
            
            if lovePts < (affection_max / 3):
            
                return "Best Friends"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        elif likePts == (affection_max / 1.00):
            
            if lovePts < (affection_max / 3):
            
                return "Best Friends Forever"
                
            elif lovePts < (affection_max / 1.5):
                
                return "---"
                
            else:
                
                return "---"
            
        #elif likePts == 0 and lovePts == 0:
        
            #return "[[CENSORED]"
    
        else:
            return "Unknown"
            
            
    def colorThoughts(thought):
        
        if thought == "Stranger":
            
            return ("#000000")
            
        elif thought == "Friend":
            
            return ("#008000")
            
        elif thought == "Crush":
            
            return ("#8b0000")
                
        
        else:
        
            return ("#000000")