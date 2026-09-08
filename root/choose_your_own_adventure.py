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
        "This is urgent, and we don't have time to escort you out," Peter says to you, "so 
        """
        print(story)