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
            
            "You might want to sit down for this," you reply.
            
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
            When the warden understands how badly you want to escape, he dials up the security on you. 
            
            Years pass, and with the increased security, you can't escape.
            
            You die of old age. 
            
            THE END.
            """
            print(story)
        else:
            story = """
            Slowly but surely, you dig through the wall with your spoon, and after 20 long, grueling years, you 
            break free. 
            
            You make a mad dash for your teleportation area, and once you reach it, you find yourself back in 
            the time machine, with your body miraculously the same age as when you left. 
            
            For the scientists, only 3 seconds had passed, but for you, an entire lifetime.
            
            "How was it?" one of the scientists ask.
            
            "Don't even get me started," you reply. 
            
            THE END.
            """
            print(story)
else:
    story = """
    You enter the machine, and a loud voice announces, "TRAVELLING IN 3... 2... 1."
    
    You are overwhelmed by pure light, and you feel a jolt as your feet touch firm ground. 
    
    Confusion fills your mind, as what you see makes no sense. You seem to be on top of a mountain or large 
    hill, and all around you is either barren ground or light foliage and fields. 
    
    Behind you in the distance, you hear what seems to be music and celebration, but just down the hill you see 
    a person dressed in simple clothes and a cowboy hat, sitting by a campfire. 
    
    Do you: 
    
    OPTION A:
        Make your way towards the celebration.
    OPTION B:
        Go down the hill towards the lone cowboy. 
        
    Make your choice.
    """
    print(story)

    userChoice = input().lower()

    if userChoice == "a":
        story = """ 
        The music gets louder as you get closer, and you begin to hear unashamed hoots and hollers. 
        
        When you arrive, you are struck by how barbaric the celebrations are. All the people seem to be wearing 
        animal skins, and they jump up and down around a large bonfire. 
        
        One member notices you and greets you. "How are you doing stranger?"
        "I'm well, how are you?" you reply.
        "Enjoying this celebration! Would you care to join in?" 
        "Sure, but first, what's going on? Where are the cities, the technology?" 
        "Do not worry about troubles such as that, stranger. Here, have a drink!" he says as he grabs a wooden  
        mug from a nearby table. You taste it, and it tastes like apple juice, just off somehow. 
        
        You continue to drink as you try to find the leader to get some answers, but as you are approaching what 
        appears to be an elder or leader, you get lightheaded, and suddenly, you find yourself in the inky 
        blackness of sleep. 
        
        When you wake up, you are dressed in garb similar to the others, mere animal skin, and you are in a 
        wooden cage. Your supplies that you took have been taken, and you are horrified at your situation. You 
        brainstorm two solutions, and can either: 
        
        OPTION A: 
            Convince the tribe members that you can trade them information and stories of the past for freedom. 
        OPTION B:
            Bide your time and wait for an opportunity to escape.
        """
        print(story)

        userChoice = input().lower()

        if userChoice == "a":
            story = """
            The guard laughs at you. 
            
            You spend the rest of your short life as a slave to their clan, and one day, when who you recognize 
            as the lone traveller comes to rescue all the slaves, you are caught in the crossfire and tragically 
            die. 
            
            THE END.
            """
            print(story)
        else:
            story = """
            When the guard isn't looking, you grab the keys off his belt. In the dead of night, you open the cage 
            and make a run for it. 
            
            The noise of your footsteps wakes a few tribe member up, and suddenly they are all awake, chasing you 
            and the other slaves who were in your cell. You just barely make it to the arrival area, and feel a 
            moment of pity for the slaves who don't have an escape method. 
            
            You find yourself back in the time machine, with your body miraculously the same age as when you left. 
            
            For the scientists, only 3 seconds had passed, but you had gone through the adventure of a lifetime.
            
            "How was it?" one of the scientists ask.
            
            "You might want to sit down for this," you reply.
            
            THE END.
            """
            print(story)
    else:
        story = """
        As you approach, the cowboy doesn't seem to react. When you come to stand awkwardly next to him, a low, 
        gravelly voice drawls, "Grab a seat, stranger." 
        
        You timidly have a seat opposite to him, trying to gauge how dangerous he is. You begin to speak, but he 
        cuts you off.
        
        "We rarely see your kind 'round these parts. You bumbling city folk. Ever since the wars targeted the major 
        cities, there seems to be none of ya'll left." 
        
        You begin to tell him who you are and what time you're from, but again, he cuts you off. "I ain't got no 
        time for your bullcrap. I have a proposition for you. You can either make yourself useful and help me, or 
        you can be left out here in the desert, where I doubt you'll last long." 
        
        "What is it?" you ask.
        
        "There's slaves in some kind of barbaric tribe just up the hill, and God created me to remove injustice 
        from this earth. Help me, or leave me alone."
        Do you: 
        
        OPTION A:
            Help the cowboy with his mission, which is potentially dangerous. 
        OPTION B:
            Decline and look for a safer alternative to explore this timeline.
        
        Make our choice.
        """
        print(story)

        userChoice = input().lower()

        if userChoice == "a":
            story = """
            The cowboy thanks you, and you both go to sleep. In the morning, the cowboy outlines his plan, and you spend 
            the next couple of months prepping. 
            
            When it's time, you storm the camp and free all the slaves, with you and the cowboy suffering no injuries. 
            
            He thanks you and gives you a half-smile, which is the most emotion you've seen from him in months. One of 
            the women you freed runs up to the cowboy and throws her arms around his neck. "I always knew you'd come!" 
            
            You feel pride in what you've done, and make your way back to the arrival area. You find yourself back in 
            the time machine, and one of the scientists asks, "How was it?"
            
            "You might want to sit down for this," you reply.
            
            THE END.
            """
            print(story)
        else:
            story = """
            A soft purring sound drags you out of your blissful dreaming, and you swat at the direction of the noise, 
            thinking you're back at home with your cats. When you realize where you are, you bolt upright and find 13 
            mutated looking cougars staring at you. 
            
            You try your best to fight them.
            
            Let's just say you've never been a good fighter.

            THE END.
            """
            print(story)


