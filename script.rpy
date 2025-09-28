# Character Definitions
define a = Character("Alex", color="#ff6b6b")
define l = Character("Lily", color="#6bff6b")
define r = Character("Ron", color="#6b6bff")
define ro = Character("Rosa", color="#ff6bff")
define m = Character("Mom", color="#ff9966")
define g = Character("Yuuko", color="#f5e502b6")

# Character Images
image alex angry = "images/chs/alex/angry.png"
image alex embarrased = "images/chs/alex/embarrased.png"
image alex laugh = "images/chs/alex/laugh.png"
image alex neutral = "images/chs/alex/neutral.png"
image alex sad = "images/chs/alex/sad.png"
image alex talk = "images/chs/alex/talk.png"
image alex upset = "images/chs/alex/upset.png"
image alex smile = "images/chs/alex/smile.png"

image lily angry = "images/chs/lily/angry.png"
image lily eyes = "images/chs/lily/eyes.png"
image lily laugh = "images/chs/lily/laugh.png"
image lily neutral = "images/chs/lily/neutral.png"
image lily sad = "images/chs/lily/sad.png"
image lily shock = "images/chs/lily/shock.png"
image lily smile = "images/chs/lily/smile.png"
image lily embarrased = "images/chs/lily/embarrassed.png"

image mom angry = "images/chs/mom/angry.png"
image mom annoyed = "images/chs/mom/annoyed.png"
image mom glad = "images/chs/mom/glad.png"
image mom neutral = "images/chs/mom/neutral.png"
image mom sad = "images/chs/mom/sad.png"
image mom smile = "images/chs/mom/smile.png"

image ron angry = "images/chs/ron/angry.png"
image ron boast = "images/chs/ron/boast.png"
image ron laugh = "images/chs/ron/laugh.png"
image ron sad = "images/chs/ron/sad.png"
image ron smile = "images/chs/ron/smile.png"
image ron surprise = "images/chs/ron/surprise.png"
image ron talk = "images/chs/ron/talk.png"

image rosa angry = "images/chs/rosa/angry.png"
image rosa embarassed = "images/chs/rosa/embarassed.png"
image rosa laugh = "images/chs/rosa/laugh.png"
image rosa neutral = "images/chs/rosa/neutral.png"
image rosa sad = "images/chs/rosa/sad.png"
image rosa smile = "images/chs/rosa/smile.png"
image rosa surprised = "images/chs/rosa/surprised.png"

image ghost angry = "images/chs/ghost/angry.png"
image ghost annoyed = "images/chs/ghost/annoyed.png"
image ghost angry_blush = "images/chs/ghost/anygry with blush.png"
image ghost laugh_blush = "images/chs/ghost/blushed laugh.png"
image ghost eyebrow_smile_blush = "images/chs/ghost/eyebro up smile with blush.png"
image ghost eyebrow_up = "images/chs/ghost/eyebro up.png"
image ghost innocent = "images/chs/ghost/innocent.png"
image ghost intimidating_smile_blush = "images/chs/ghost/intimidating smile with blush.png"
image ghost intimidating_smile = "images/chs/ghost/intimidating smile.png"
image ghost laugh = "images/chs/ghost/laugh.png"
image ghost neutral_smile_blush = "images/chs/ghost/neutral smile with blush.png"
image ghost neutral_smile = "images/chs/ghost/neutral smile.png"
image ghost neutral_blush = "images/chs/ghost/neutral with blush.png"
image ghost neutral = "images/chs/ghost/neutral.png"
image ghost oops = "images/chs/ghost/oops.png"
image ghost peek_blush = "images/chs/ghost/peek with blush.png"
image ghost peek = "images/chs/ghost/peek.png"
image ghost sad_stern_blush = "images/chs/ghost/sad stern with blush.png"
image ghost sad_stern = "images/chs/ghost/sad stern.png"
image ghost sad_blush = "images/chs/ghost/sad with blush.png"
image ghost sad = "images/chs/ghost/sad.png"
image ghost smile_blush = "images/chs/ghost/smile with blush.png"
image ghost smile = "images/chs/ghost/smile.png"
image ghost suspicious_smile_blush = "images/chs/ghost/suspicious smile with blush.png"
image ghost suspicious_smile = "images/chs/ghost/suspicious smile.png"
image ghost worried_smile_blush = "images/chs/ghost/worried smile with blush.png"
image ghost worried_smile = "images/chs/ghost/worried smile.png"
image ghost worried_blush = "images/chs/ghost/worried with blush.png"
image ghost worried = "images/chs/ghost/worried.png"
image ghost happy = "images/chs/ghost/smile.png"
image ghost shy = "images/chs/ghost/neutral_blush.png"
image ghost flustered = "images/chs/ghost/smile_blush.png"
image ghost curious = "images/chs/ghost/eyebrow_up.png"

# Background Images
image bedroom day = "images/bg/pra_a1_day2.png"
image bedroom evening = "images/bg/pra_a1_evening1.png"
image bedroom night lightson = "images/bg/pra_a1_night1_lights.png"
image bedroom dark = "images/bg/pra_a1_night1.png"
image classroom day = "images/bg/classroom day.png"
image classroom out opendoor = "images/bg/classroom out opendoor.png"
image hallway day = "images/bg/hallway day.png"
image hallway evening = "images/bg/hallway evening.png"
image hallway night = "images/bg/hallway night.png"
image school gate evening open = "images/bg/school gate evening open.png"
image school gate latevening close = "images/bg/school gate latevening close.png"
image school gate morning = "images/bg/school gate morning.png"
image school stairs day = "images/bg/school stairs day.png"

# Character Positions
transform alex_left:
    xalign 0.4 yalign 1.5 zoom 0.25

transform lily_center:
    xalign 0.2 yalign 1.5 zoom 0.25

transform ron_right:
    xalign 0.7 yalign 1.5 zoom 0.25

transform rosa_far_right:
    xalign 0.9 yalign 1.5 zoom 0.25

transform mom_pos:
    xalign 0.7 yalign 1.4 zoom 0.6

transform ghost_pos:
    xalign 0.7 yalign 0.8 zoom 0.5

# Game Variables
default day = 1
default ghost_trust = 0
default friendship = {"lily": 0, "ron": 0, "rosa": 0}
default discovered_clues = 0
default bravery = 0
default romance_route = False

# Sound Definitions - ADDED MISSING FOOTSTEPS
define audio.main_theme = "audio/music/main_theme.ogg"
define audio.school_day = "audio/music/school_day.ogg"
define audio.mystery = "audio/music/mystery.ogg"
define audio.ghost_theme = "audio/music/ghost_theme.ogg"
define audio.romantic = "audio/music/romantic.ogg"
define audio.sad_moment = "audio/music/sad_moment.ogg"
define audio.climax = "audio/music/climax.ogg"
define audio.happy_end = "audio/music/happy_end.ogg"

define audio.door_open = "audio/sfx/door_open.ogg"
define audio.door_close = "audio/sfx/door_close.ogg"
define audio.ghost_appear = "audio/sfx/ghost_appear.ogg"
define audio.ghost_vanish = "audio/sfx/ghost_vanish.ogg"
define audio.heartbeat = "audio/sfx/heartbeat.ogg"
define audio.school_bell = "audio/sfx/school_bell.ogg"
define audio.footsteps = "audio/sfx/footsteps.ogg"  # ADDED THIS LINE
define audio.scream = "audio/sfx/scream.ogg"  # ADDED FOR PANIC SCENE

# THE GAME STARTS HERE
label start:
    play music main_theme fadein 3.0
    scene bedroom day with fade
    
    "Monday morning. The day everything changed..."
    
    show alex upset at alex_left
    a "Ugh, why do mornings exist? It's unnatural."
    
    play sound audio.door_open  # CHANGED TO audio.door_open
    show mom annoyed at mom_pos with dissolve
    m "Alex! You're going to be late again! And it's the school anniversary today!"
    
    menu:
        "Groan dramatically":
            show alex sad at alex_left
            a "Five more minutes... the world can wait..."
            show mom angry at mom_pos
            m "No it cannot! Up you get!"
            $ bravery -= 1
            
        "Jump up energetically":
            show alex smile at alex_left
            a "Anniversary? That sounds important! I'm up!"
            show mom smile at mom_pos
            m "That's my responsible child!"
            $ bravery += 1
            
        "Ask about the anniversary":
            show alex talk at alex_left
            a "What's special about today?"
            show mom neutral at mom_pos
            m "They're unveiling a memorial for... well, you'll see."
            $ discovered_clues += 1

    # SCHOOL GATE - MEETING FRIENDS
    scene school gate morning open with fade
    play music school_day
    play sound audio.school_bell  # CHANGED TO audio.school_bell
    
    show lily neutral at lily_center
    show ron boast at ron_right
    
    l "Alex! Over here! You'll never believe what Rosa found!"
    r "Yeah, it's way cooler than another boring ceremony!"
    
    show alex talk at alex_left with moveinleft
    a "What's up? Did she finally find proof the principal is a robot?"
    
    show ron laugh at ron_right
    r "Better! She found old records showing the memorial is wrong! There's a missing student!"
    
    menu:
        "Get excited about the mystery":
            show alex smile at alex_left
            a "A cover-up? This is like a detective story!"
            $ friendship["ron"] += 2
            $ bravery += 1
            
        "Be skeptical":
            show alex neutral at alex_left
            a "Probably just bad record-keeping. Those old files are a mess."
            show lily sad at lily_center
            l "You have no sense of adventure!"
            $ friendship["lily"] -= 1
            
        "Focus on the memorial":
            show alex talk at alex_left
            a "What do you know about this memorial anyway?"
            show lily shock at lily_center
            l "It's for a student who died in a fire. Yuuko, I think her name was."
            $ discovered_clues += 2

    # ROSA'S DRAMATIC ENTRANCE
    play sound audio.door_open  # CHANGED TO audio.door_open
    show rosa surprised at rosa_far_right with moveinright
    ro "The plot thickens! I found the original incident report!"
    
    show alex neutral at alex_left
    a "And? What does it say?"
    
    show rosa neutral at rosa_far_right
    ro "The fire was ruled accidental, but there were... discrepancies. Witnesses saw someone start it intentionally."
    
    menu:
        "Dive into investigation mode":
            a "This is huge! We need to find out the truth!"
            show rosa smile at rosa_far_right
            ro "Finally! Someone who gets it!"
            $ friendship["rosa"] += 2
            $ discovered_clues += 1
            
        "Suggest caution":
            a "Maybe we should leave this alone. Sounds dangerous."
            show rosa angry at rosa_far_right
            ro "Typical! Always playing it safe!"
            $ friendship["rosa"] -= 1
            
        "Make a joke":
            show alex laugh at alex_left
            a "So our school has a murder mystery? Do we get detective badges?"
            show ron laugh at ron_right
            r "I call being the comic relief sidekick!"
            $ friendship["ron"] += 1

    # FIRST GHOST ENCOUNTER
    scene hallway evening with fade
    play music mystery fadein 2.0
    play sound audio.footsteps  # CHANGED TO audio.footsteps
    
    "After school, I realized I left my project in the storage room..."
    "The halls were empty. Too empty."
    
    show alex upset at alex_left
    a "Okay, just grab it and go. No exploring."
    
    scene bedroom dark with fade
    play sound audio.door_open  # CHANGED TO audio.door_open
    "The storage room was freezing. And... was someone whispering?"
    
    show alex shock at alex_left
    a "Hello? Is someone there?"
    
    play sound audio.ghost_appear  # CHANGED TO audio.ghost_appear
    show ghost neutral at ghost_pos with hpunch
    g "You can see me?"
    
    menu:
        "Panic and run":
            play sound audio.heartbeat  # CHANGED TO audio.heartbeat
            show alex upset at alex_left
            a "Nope! Not today! Ghosts are above my pay grade!"
            hide ghost with dissolve
            $ ghost_trust -= 2
            jump panic_ending
            
        "Stay and talk":
            show alex talk at alex_left
            a "You're... not exactly solid. Are you Yuuko?"
            g "You know my name? It's been so long..."
            $ ghost_trust += 2
            jump ghost_conversation
            
        "Try to be funny":
            show alex laugh at alex_left
            a "Are you here to complain about the memorial? I hear it's inaccurate."
            show ghost smile at ghost_pos
            g "You're... different. Most people scream."
            $ ghost_trust += 1

label ghost_conversation:
    show alex neutral at alex_left
    a "The records say you died in the fire. But there's more to the story, isn't there?"
    
    show ghost sad at ghost_pos
    g "I stayed to make sure everyone else got out. The principal... he started the fire to cover up his experiments."
    
    menu:
        "Express sympathy":
            show alex sad at alex_left
            a "That's horrible! You were a hero!"
            show ghost sad_blush at ghost_pos
            g "A hero who's been forgotten for 70 years..."
            $ ghost_trust += 2
            
        "Ask for proof":
            show alex talk at alex_left
            a "How do I know you're telling the truth?"
            show ghost angry at ghost_pos
            g "Check the basement. His lab is still there. The evidence is there."
            $ discovered_clues += 1
            
        "Offer help":
            show alex smile at alex_left
            a "I'll help you get justice. Your sacrifice shouldn't be forgotten."
            show ghost smile_blush at ghost_pos
            g "You'd do that? For me?"
            $ ghost_trust += 3
            $ romance_route = True

    g "Three days until the anniversary. The veil between worlds will be thin."
    g "Choices will have to be made. Sacrifices..."
    
    play sound audio.ghost_vanish  # CHANGED TO audio.ghost_vanish
    hide ghost with dissolve
    "She faded away, leaving me with more questions than answers."
    
    scene bedroom night lightson with fade
    show alex neutral at alex_left
    a "Sacrifices... what did she mean? And why do I feel like I'm part of this now?"
    
    $ day += 1
    jump day_2

label day_2:
    scene bedroom day with fade
    play music school_day
    
    show alex neutral at alex_left
    a "Day 2. Do I tell the others about Yuuko? Do I investigate alone?"
    
    menu:
        "Tell Lily - she's trustworthy":
            jump tell_lily
        "Tell Ron - he'd love this":
            jump tell_ron
        "Investigate alone - keep it secret":
            jump investigate_alone

label tell_lily:
    scene school stairs day with fade
    
    show lily neutral at lily_center
    show alex talk at alex_left
    
    a "Lily, I need to tell you something incredible..."
    
    "I explained everything. Yuuko, the cover-up, the upcoming anniversary."
    
    show lily shock at lily_center
    l "Yuuko... my grandmother mentioned her! She said Yuuko was brave but... troubled."
    
    menu:
        "Ask for details":
            a "Troubled how? This could be important!"
            show lily sad at lily_center
            l "She said Yuuko had a crush on the principal. Maybe that's why she stayed?"
            $ discovered_clues += 2
            $ friendship["lily"] += 2
            
        "Suggest teaming up":
            a "Help me investigate. We can uncover the truth together."
            show lily smile at lily_center
            l "Okay! But if we find actual ghosts, you're going first!"
            $ bravery += 1
            
        "Warn her about danger":
            a "Actually, this might be too risky. Maybe you should stay out of it."
            show lily angry at lily_center
            l "I can handle myself! Stop treating me like a child!"
            $ friendship["lily"] -= 1

    jump investigation_time

label tell_ron:
    scene classroom day with fade
    
    show ron smile at ron_right
    show alex talk at alex_left
    
    a "Ron, remember all those ghost stories you love? Well..."
    
    show ron surprise at ron_right
    r "NO WAY! A real ghost? And a murder cover-up? This is the best day ever!"
    
    menu:
        "Channel his enthusiasm":
            a "I need your ghost-hunting expertise! What's the plan?"
            show ron boast at ron_right
            r "First, we need equipment! EMF readers! Spirit boxes! Snacks!"
            $ discovered_clues += 1
            
        "Keep him focused":
            a "This is serious! People died! Well, a person died."
            show ron neutral at ron_right
            r "Right, right. Serious business. But still... awesome serious business."
            $ bravery += 1
            
        "Regret your decision":
            a "Maybe this was a mistake. You're not taking this seriously."
            show ron sad at ron_right
            r "Hey, I can be serious! Watch me be serious!"
            $ friendship["ron"] -= 1

    jump investigation_time

label investigate_alone:
    scene hallway day with fade
    play music mystery
    
    show alex neutral at alex_left
    a "Better to handle this alone. No need to endanger anyone else."
    
    "I decided to check the school basement. Yuuko said the evidence was there."
    
    scene bedroom dark with fade
    play sound audio.door_open  # CHANGED TO audio.door_open
    "The basement was exactly as creepy as you'd expect. And cold. Very cold."
    
    play sound audio.ghost_appear  # CHANGED TO audio.ghost_appear
    show ghost worried at ghost_pos with dissolve
    g "You came back. And you're alone. That's... brave. Or foolish."
    
    menu:
        "Ask about the principal":
            a "What was he experimenting with? Why start a fire?"
            show ghost angry at ghost_pos
            g "He was trying to cheat death. I was... collateral damage."
            $ discovered_clues += 2
            
        "Express concern for her":
            show alex sad at alex_left
            a "You've been alone all this time. That must have been terrible."
            show ghost sad_blush at ghost_pos
            g "You're the first person to care in 70 years..."
            $ ghost_trust += 2
            
        "Make a dark joke":
            show alex laugh at alex_left
            a "So the principal was basically a budget Dr. Frankenstein?"
            show ghost laugh at ghost_pos
            g "With worse fashion sense, yes."
            $ ghost_trust += 1

    jump investigation_time

label investigation_time:
    scene school gate evening open with fade
    
    "The investigation revealed startling truths..."
    
    if discovered_clues >= 3:
        show alex talk at alex_left
        a "The principal was experimenting with occult rituals! Yuuko was his test subject!"
        "He started the fire to cover his failures. Yuuko's sacrifice was meant to be forgotten."
        $ bravery += 2
        
    elif friendship["lily"] >= 2:
        show lily neutral at lily_center
        show alex neutral at alex_left
        l "My grandmother's diary mentions secret meetings between Yuuko and the principal."
        l "She loved him. He used that. The fire was... convenient for him."
        $ discovered_clues += 3
        
    else:
        show alex sad at alex_left
        a "The more I learn, the darker this gets. Why would someone do this?"
        $ bravery -= 1

    # YUUKO'S EMOTIONAL APPEARANCE
    play music ghost_theme
    play sound audio.ghost_appear  # CHANGED TO audio.ghost_appear
    show ghost sad at ghost_pos with dissolve
    
    g "Now you know the truth. The real question is... what will you do with it?"
    
    menu:
        "Promise justice":
            show alex determined at alex_left
            a "I'll make sure everyone knows what really happened. I promise."
            show ghost smile_blush at ghost_pos
            g "Your determination... it gives me hope."
            $ ghost_trust += 2
            
        "Ask what she wants":
            show alex talk at alex_left
            a "What outcome would give you peace? Just tell me."
            show ghost neutral at ghost_pos
            g "I want the truth known. But I also want... to not be alone anymore."
            $ romance_route = True
            
        "Express fear":
            show alex upset at alex_left
            a "I'm scared. This is bigger and darker than I imagined."
            show ghost worried at ghost_pos
            g "Fear is natural. Courage is moving forward despite it."
            $ bravery += 1

    $ day += 1
    jump day_3

label day_3:
    scene bedroom day with fade
    play music mystery
    
    show alex determined at alex_left
    a "Today's the day. The anniversary. Time to face whatever comes."
    
    "I gathered my courage and my friends. This ends today."
    
    scene hallway night with fade
    play music climax
    play sound audio.heartbeat  # CHANGED TO audio.heartbeat
    
    "The school at night felt different. Alive with memory and anticipation."
    
    show ghost neutral at ghost_pos with dissolve
    g "You came. I wasn't sure you would. Most would have run by now."
    
    menu:
        "I keep my promises" if ghost_trust >= 5:
            a "You deserve justice. And peace. I'm here to help you get both."
            jump high_trust_ending
            
        "The truth needs to come out":
            a "Whatever happens, people need to know what really happened here."
            jump truth_ending
            
        "I'm here for you" if romance_route:
            a "I'm not letting you face this alone. We're in this together."
            jump romance_ending
            
        "I'm terrified but I'm here":
            a "I don't know if I can help, but I have to try."
            jump courage_ending

# ENDINGS WITH PROPER ENDING SCREENS
label high_trust_ending:
    play music romantic
    
    show ghost smile_blush at ghost_pos
    g "Your friendship means everything. But the ritual requires a sacrifice."
    
    show alex smile at alex_left
    a "What if the sacrifice isn't what he intended? What if we rewrite the rules?"
    
    menu:
        "Sacrifice the secret" if discovered_clues >= 5:
            a "What if we let the world know everything? The ultimate truth sacrifice?"
            show ghost laugh at ghost_pos
            g "Exposing him after all these years? That would be justice."
            jump justice_ending
            
        "Sacrifice the loneliness" if ghost_trust >= 7:
            a "What if I share my life with you? You wouldn't be alone anymore."
            show ghost flustered at ghost_pos
            g "You would do that? For me?"
            jump shared_life_ending
            
        "Break the cycle":
            a "What if we destroy the ritual itself? No more sacrifices, ever."
            show ghost eyebrow_up at ghost_pos
            g "Ending this for good? That would be true freedom."
            jump freedom_ending

label justice_ending:
    scene black with fade
    play music happy_end
    
    "We gathered the whole school. Told Yuuko's story. Exposed the principal's crimes."
    "The memorial was corrected. Yuuko was finally recognized as the hero she was."
    
    show alex smile at alex_left
    show ghost happy at ghost_pos
    a "You're free now. Your sacrifice meant something."
    g "Thank you. For everything."
    
    "Yuuko faded peacefully, her story finally told. Her burden lifted."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: The Truth Shall Set You Free" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "By exposing the decades-old cover-up, you gave Yuuko the recognition she deserved.\nHer sacrifice was no longer in vain, and she found peace in being remembered as a hero." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label shared_life_ending:
    scene black with fade
    play music romantic
    
    "We performed a different ritual. One of connection, not sacrifice."
    "Yuuko remains as part of my life. A presence. A friend. Maybe more."
    
    show alex smile at alex_left
    show ghost smile_blush at ghost_pos
    a "You're not alone anymore. You'll never be alone again."
    g "This... this is better than I ever dreamed."
    
    "Some sacrifices become blessings. Some burdens become gifts."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: A Bond Beyond Death" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "You chose connection over separation, sharing your life with a lonely spirit.\nThe sacrifice was not an ending, but a new beginning—proving that some burdens are lighter when carried together." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label freedom_ending:
    scene black with fade
    play music happy_end
    
    "We destroyed the ritual site. Broke the cycle forever."
    "No more sacrifices. No more ghosts bound against their will."
    
    show alex determined at alex_left
    show ghost smile at ghost_pos
    a "It's over. No one else will suffer like you did."
    g "You've given me the greatest gift. Freedom."
    
    "Yuuko moved on, but her memory lives on in the fixed memorial."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: Breaking the Cycle" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "You refused to continue the chain of sacrifices, destroying the ritual that bound Yuuko.\nIn breaking the cycle, you proved that some traditions deserve to end, and true freedom comes from courage, not compliance." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label truth_ending:
    scene black with fade
    play music happy_end
    
    "I chose truth above all else. The full story came out, no matter the consequences."
    "The school newspaper published everything. The principal's descendants apologized."
    
    show alex neutral at alex_left
    show ghost neutral at ghost_pos
    a "The truth is out. People know what really happened."
    g "After all these years... justice."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: Unburdened by Truth" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "You believed that sunlight is the best disinfectant, exposing the full truth regardless of consequences.\nThe weight of decades of lies was lifted, proving that some sacrifices must be made for transparency." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label romance_ending:
    scene black with fade
    play music romantic
    
    "What started as a mystery became something deeper. Something personal."
    "Yuuko and I found a connection that transcended life and death."
    
    show alex smile at alex_left
    show ghost smile_blush at ghost_pos
    a "I'm glad I found you. Or... you found me."
    g "Maybe we found each other. Some connections are meant to be."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: Love's Eternal Burden" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "In choosing connection over conventional solutions, you embraced a relationship that defies normal boundaries.\nThe sacrifice was giving up a normal life for something extraordinary—proving that love can be the greatest burden and the greatest gift." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label courage_ending:
    scene black with fade
    play music happy_end
    
    "I was terrified, but I faced my fears. That made all the difference."
    "With shaky hands but a determined heart, I helped Yuuko find peace."
    
    show alex smile at alex_left
    show ghost happy at ghost_pos
    a "I was scared, but I'm glad I didn't run."
    g "Courage isn't the absence of fear. It's acting despite it. Thank you."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: Courage in the Face of Fear" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "You proved that bravery isn't about being unafraid, but about doing what's right despite your fears.\nThe sacrifice was your comfort and safety, traded for doing what needed to be done—showing that true courage is a choice made moment by moment." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label panic_ending:
    scene black with fade
    play music sad_moment
    
    "I couldn't handle it. I ran. Like a coward."
    
    show alex sad at alex_left
    a "I'm sorry, Yuuko. I wasn't strong enough."
    
    "The anniversary came and went. The memorial stayed wrong. Yuuko remained forgotten."
    "But sometimes, late at night, I hear whispering from the storage room..."
    "And I wonder what might have been, if I'd been braver."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: The Weight of What Could Have Been" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "Fear won over courage, leaving Yuuko to her lonely fate.\nThe sacrifice you avoided became a different kind of burden—the weight of regret and the haunting knowledge that some opportunities, once lost, can never be reclaimed." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

# ADDITIONAL ENDINGS FOR DIFFERENT PATHS
label abandonment_ending:
    scene black with fade
    play music sad_moment
    
    "In the end, I walked away. Some burdens are too heavy to carry."
    "The school continues, the memorial remains incorrect, and Yuuko... Yuuko waits."
    
    show alex sad at alex_left
    a "It was too much. I had to think of myself first."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: The Easiest Burden" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "You chose self-preservation over intervention, avoiding immediate danger but carrying the knowledge of your inaction.\nSometimes the lightest burden is the one you refuse to pick up—but the weight of what you didn't do can be heavier than any sacrifice." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

label forgotten_ending:
    scene black with fade
    play music sad_moment
    
    "We chose to let the world forget. To bury the truth forever."
    "The sacrifice was memory itself—Yuuko's story, lost to time."
    
    show alex neutral at alex_left
    show ghost neutral at ghost_pos
    a "Some stories are better left untold."
    g "Oblivion... it's peaceful in its own way."
    
    # ENDING SCREEN
    scene black with fade
    show text "Ending Achieved: The Peace of Forgetting" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show text "You chose to sacrifice memory itself, trading truth for peace and letting Yuuko fade into obscurity.\nSome burdens are too heavy to carry forward, and sometimes the kindest sacrifice is letting go of the past entirely." at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return

# FINAL CREDITS SCREEN (OPTIONAL)
label show_credits:
    scene black with fade
    show text "Thank you for playing\n'Burden of the Past'" at truecenter with dissolve
    pause 3.0
    hide text with dissolve
    show text "A story about sacrifices, choices, and the burdens we carry\n\nYour decisions shaped this story.\nWhat other endings await?" at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    return