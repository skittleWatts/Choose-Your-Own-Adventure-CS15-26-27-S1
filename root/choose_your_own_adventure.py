userChoice = None

story = """
Everyone has seen the news. 

Scientists have discovered how to create time machines. 

They have decided that this privilege should not be based on not wealth or popularity, but randomness. 
Four months later, after everyone who wished to join submitted their applications, you get an email 
from the International Coalition of Time Travel (ICTT). 

You have been selected. 

They ask you, "What time do you want to travel to?"

You can choose either:

OPTION A:
    Travel so far into the past that there is no recorded history from that time. Before the dinosaurs. 
OPTION B: 
    Travel one million years into the future. 

Make your selection. 
"""

print(story)

userChoice = input().lower()

if userChoice == "a":
    story = """
    You enter the machine, and a loud voice announces, "TRAVELLING IN 3... 2... 1."
    
    You are overwhelmed by pure light, and you feel a jolt as your feet touch firm ground. 
    
    As soon your eyes adjust, awe knocks you to your knees. You had been sent with weapons and food, 
    ready to survive in a prehistoric jungle, yet nothing could compare to the bustling metropolis 
    sprawling in front of you. Flying cars dart across the open blue expanse, and skyscrapers reach 
    so high it seems impossible. 
    
    Immediately, a drone rushes over to you, blaring, "IDENTIFY YOURSELF HUMAN. YOUR DNA IS NOT WITHIN
    KNOWN DATABASES!"
    
    Your mind races, and you can either:
    
    OPTION A:
        Tell the truth that you are a time traveller from billions of years in the future. 
    OPTION B:
        Lie and say you do not know why you're not within databases, and convince the clanker you're a citizen. 
    
    Make your selection. 
    """
    print(story)

    userChoice = input().lower()

    if userChoice == "a":
        story = """
        The robot blares again, and you flinch, expecting guns, lasers, or for you to be captured. Instead, 
        it says, "TRUTH DETECTED. TRANSPORTING TO SUPREME LEADER PETER XXI. MAXIMUM IMPORTANCE LEVEL." 
        It flashes a laser at you, and suddenly you are standing before a throne, with what looks like the pope 
        sitting on it. 
        "How did you get here?" he (who you assume is Supreme Leader Peter XXI) asks. "Your DNA was analyzed
        by our scientists, and it looks like you've gone through approximately one billion years of evolution." 
        "They're right," you reply. "I'm from one billion years in the future."
        "How?" Peter demands. "We've removed diseases and poverty, explored throughout our entire galaxy, yet 
        the one thing that is impossible is time travel. Your society must be unbeliveably advanced!" 
        "Well, although we have time travel, we still have diseases and haven't even escaped our solar system." 
        you reply. 
        "Interesting... We're going to get our scientists to study y-" Peter starts, before a serious-looking 
        woman bursts through the door. 
        "Taravangia has threatened nuclear war! They're demanding that our nation of Kholinar cedes to their 
        demands or nuclear war will break out! What do we do?" she exclaims. 
        "This is urgent, and we don't have time to escort you out," Peter says to you. "I'm treating this as a 
        sign from God, that you are to help me. What do we do? Do we:
        
        OPTION A: 
            Tell Peter to cede to the demands, preventing nuclear war, with untold future ramifications that 
            could affect your very existence.
        OPTION B:
            Tell Peter to start the war, with untold future ramifications that could affect your very existence. 
            
        Make your selection.
        """
        print(story)

        userChoice = input().lower()

        if userChoice == "a":
            story = """
            With Supreme Leader Peter XXI ceding to Taravangia's demands, nuclear war is successfully prevented. 
            
            Unfortunately, when you and Peter are taking dinner together, alarms go off, and a medical officer 
            rushes into the room, shouting "There is a fading temporal signature in this room, we don't know 
            what to do!" 
            
            Now that she mentions it, you do feel a bit queasy, and when you look down at your arm, it seems 
            almost transluecent or intangible. You realize the consequences of this made sure that you were never 
            born, and now you do not exist. You make peace with your decision of sacrificing your timeline for 
            theirs, and you smile as it all fades to black. 
            
            THE END.
            """
            print(story)
        else:
            story = """
            Once nuclear war starts, the scientists realize the ramifications. They predict that within the next 
            two decades, there will be no trace of their society left. 
            
            Peter escorts you back to the place of your arrival to this time, thanking you for your help. 
            "No matter what the scientists say, I'm glad you came to give your advice. Even if this destroys 
            my society, it's a worthy sacrifice for yours." 
            
            You two have a tear-filled goodbye, and you find yourself back in the time machine.
            "How was it?" one of the scientists ask.
            
            "Don't even get me started," you reply. 
            
            THE END.
            """
            print(story)
    else:
        story = """
        The drone flares with an angry red light, screaming, "LIE DETECTED! LIE DETECTED! TRANSPORTING TO 
        PRISON FOR FELONY A14-3: UNTRACKED IDENTITY."
        
        A laser flashes at you, and you flinch, expecting total eradication, but instead you suddenly find 
        yourself behind bars in a stereotypical concrete prison, albeit with higher tech utilities such as a 
        bathroom and what seems to be a hologram TV, only broadcasting content meant to prepare for reentry 
        into society. 
        
        You panic, realizing you have to get back to your time to report your findings. You narrow down your 
        escape options to two choices:
        
        OPTION A:
            Try to convince the warden of the truth in order for him to understand the importance of you 
            escaping.
        OPTION B: 
            Bide your time, slowly digging a hole in the concrete with your spoon until you can escape and make 
            a run back to your arrival area.
            
        Make your selection.
        """
        print(story)

        userChoice = input().lower()

        if userChoice == "a":
            story = """
            ;)
            """
