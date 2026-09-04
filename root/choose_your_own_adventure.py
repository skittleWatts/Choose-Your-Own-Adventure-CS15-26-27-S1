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
        Tell the truth that you are a time traveller from hundreds of millions of years in the future. 
    OPTION B:
        Lie and say you do not know why you're not within databases, and convince the clanker you're a citizen. 
    
    Make your selection. 
    """
    print(story)

    userChoice = input().lower()

    if userChoice == "a":
        story = """
        The robot blares again, and you flinch, expecting guns, lasers, or for you to be captured. Instead, 
        it says, "TRUTH DETECTED. TRANSPORTING TO SUPREME LEADER PETER XXI.
        """
        print(story)