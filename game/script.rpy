# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Willa")
define boy = Character("Caro")
define impostor = Character("Psyde")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room
    # play music "bgmusic.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show boy neutral: 
        zoom 2.5
    boy "This is not good."

    hide boy neutral

    show evil surprise: 
        zoom 2.5

    impostor "Hold on - I believe that the Witch is dead, correct?\nIn that case, aren’t we free to leave?"

    hide evil surprise 

    show boy neutral: 
        zoom 2.5

    boy "Nope. Check out the door."

    hide boy neutral

    show mc: 
        zoom 2.5

    mc "Oh my gosh, what...is that?\nHang on a second. Is that alive?"

    hide mc 

    show evil surprise: 
        zoom 2.5

    impostor "Just look at the way it’s pulsating. I bet this the\ncurse she had mentioned, before...you know.\nYou killed her."

    hide evil surprise
    show boy : 
        zoom 2.5
    boy "How did you manage to do that, anyways?"
    hide boy
    
    show mc: 
        zoom 2.5 
    
    mc "I have no idea…it all happened so fast.\n I… I was so scared.\n It was all instinct…"

    hide mc  
    show boy happy: 
        zoom 2.5
        
    boy " Right. I thought I was done for.\n Good thing you got her. \nWould’ve been nice if you were a little faster though."

    hide boy happy
    show evil frowning: 
        zoom 2.5
    impostor "'Would have been nice' is a gross understatement.\nThe curse was completed on time.\n The die has been cast."
    hide evil frowning    
    show mc: 
        zoom 2.5
    mc "Is the curse just keeping us from leaving?"
    hide mc 
    show boy angry: 
        zoom 2.5
    boy "Just keeping us from leaving?\n This is a Witch’s Potion Room, buddy.\n Not exactly a place you want to hang out in.\n I’ve been trapped here for years, until you came along."
    hide boy angry
    show mc surprised: 
        zoom 2.5 
    mc "At least it’s not the curse she placed on our village!\n The plague she created was horrific…\nIt caused so much pain. We lost so many people."
    hide mc surprised
    show boy neutral: 
        zoom 2.5
    boy "Yeah, not that I disagree, but it did start in this\n room right here. Homegrown."
    hide boy neutral
    show evil smile: 
        zoom 2.5
    impostor "In any case, we should look around.\n The Witch did mention that she intended\n to imprison us for the “rest of eternity”.\n I would prefer that did not happen."
    hide evil smile
    show boy angry: 
        zoom 2.5 
    boy "Guess we have all the time in the world\n to look for an exit then. I’m going to head to\n the potion shelf and look for any clues."
    hide boy angry
    show evil peeved: 
        zoom 2.5 
    impostor "I refuse to stay here any longer.\n That… creature by the door is frightening.\n I wonder if her Familiar had something to do with it."
    hide evil peeved
    show mc surprised: 
        zoom 2.5
    mc "Familiar? With?"
    hide mc surprised
    show boy neutral: 
        zoom 2.5
    boy "There’s no way one mage has enough magical power\n to carry out the type of curses that this Witch did.\n She had an assistant, like all mages\n worth their salt do."
    hide boy neutral
    show mc surprised: 
        zoom 2.5
    mc "Wouldn’t we have seen the assistant then?\n When she died?"
    hide mc surprised
    show evil frowning: 
        zoom 2.5 
    impostor "Witches and their familiars don’t\n have the same close relationship they did\n in years past."
    impostor "I expect to see the familiar soon, however.\n I trust you can handle it!"
    hide evil frowning
    show boy happy: 
        zoom 2.5
    boy "Yeah. Even though I’ve been imprisoned here for months,I haven’t seen the Familiar.\n I’m sure it’ll pop up sometime though."
    hide boy happy
    show mc: 
        zoom 2.5 
    mc "Um, right. I can look around the door then.\n Hopefully there’s another way out…"
    hide mc
    show evil smiling: 
        zoom 2.5
    impostor "I’m intrigued by the glass sculptures\n at the other end of the room.\n I surmise that they might have something that can help us."
    hide evil smiling
    show boy happy: 
        zoom 2.5
    boy "I'll be at potions."
    hide boy happy
    show mc happy: 
        zoom 2.5
    mc "Right then. I’d better start looking around."
    hide mc happy
    return