# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Meno = Character('Meno', color="#91ffff")
define pov = Character("[povname]", color="#bfa2ffff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg start

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.


    "Is there existence after death?{p=0.5}That is the question that has plagued humanity for centuries."

    "A question that fueled the formation of religions worldwide. Each with an answer of their own."
    "Even those who reject the idea of gods have their own answer to death.{p=1.0}"
    "It is understanble why humanity fears the unknown. To not know what lies ahead for a self-aware species like ourselves;{p=0.5}it's a recipe for existential dread."
    "We must come up with an answer to death, to ease our troubled conscience... Yet we will never know the truth of the matter until our time comes."
    "Now it is time for you to take a bow on the stage of life.{p=1.0}I wonder if the answer is what you'd expect..."
    scene bg whiteout
    with fade
    $ povname = renpy.input("Tell me lost soul, what is your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Quinn"
    pov "I am... [povname]."

    "It is time for me to depart, [povname]. May you find the answers you seek."

    scene bg hospital
    with fade
    pov """
    The room is loud... chaotic. The bed I lay in rattles as they run down the hallway and past the doors.

    The doors swing wildly, the wind brushing past my skin. I can hear as they smack against the walls of the hallway with a bang.

    Loud shouting... I can not make out the words. The voices are distant and muffled. I can barely feel my body anymore.

    What happened? Where am I? I can't recall how I ended up in this place.
    """

    "Hang in there [povname]! The doctor is on their way, we're almost to your room."

    pov """
    Doctor? Is this a hospital? I...

    I don't think I can stay awake for much longer... I'm feeling sleepy.

    I'll rest,{p=0.5}for just a moment.
    """
    scene bg whiteout
    with fade

    pov """
    The loud noise of the world is no more. Everything has gone quiet.
    
    Has everything settled down in the hospital now? 

    I slowly open my eyes to met with a beautiful sparkling night sky. It's unlike any sky I've seen before.

    It's full of color, and there are swirls of galaxies in place of color.

    Hesitantly I push myself up to take a look at my surroundings. This place is no hospital.

    How did I end up here? Is this a dream? Or perhaps I've entered some sort of coma?
    """

    "[povname]."

    pov """
    Someone calls out my name, making me jump. I look around frantically, trying to find the source of the voice.

    Suddenly, pairs of hands appear out of thin air. Each holding a dazzling gem. 

    It's completely unreal, I have to be dreaming! I stare at the hands around me in confusion.
    """

    "Choose."

    "The mysterious voice calls out to me once more."
    
    label choices:
        "Choose a gemstone."
    menu:
        "Opal.":
            jump choices1_a
        
        "Amber (not available)":
            jump choices1_a

        "Azurite (not available)":
            jump choices1_a

        "Aventurine (not available)":
            jump choices1_a
    label choices1_a:
        "Interesting... I hope you don't come to regret your decision."
    pov """
    I reach my hand out towards the one with the opal stone. My skin making contact with the cool object.
    
    Before I can even register what was happening; a flash of light blinded my vision.
    """
    scene bg milkyway world
    with dissolve

    pov """
    When I came back to my senses I was in a bustling city. It was full of architecture unlike any I had seen before. Like something out of a sci-fi or fantasy film.

    That's when I finally noticed the man in front of me.
    """
    show spr meno at right
    Meno "So you've noticed me."
    Meno "Haha, allow me to welcome you to the afterlife [povname].{p=0.5}I'll make sure to prove that you made the right decision choosing me."
    # This ends the game.

    return
