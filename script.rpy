# The script of the game goes in this file.

# characters
define p = Character("[name]", color='#f6b3ce')
define b = Character("Blue", color='#92a8d1')
define r = Character("Red", color='#c32219')

# character images
image pink = "pink.png"

# backgrounds
image bg pink room = "bg_pink_bedroom.jpg"
image bg street = "bg_street.jpg"

define fadehold = Fade(0.5, 1.0, 0.5)

# The game starts here.  
label start:
    $ name = renpy.input("Please enter your name:", default='Pink', allow=None, exclude='{}', length=15, with_none=None, pixel_width=None, screen='input')
    $ name = name.strip()

    scene bg pink room
    with fade

    # alarm sound goes off

    p "hhhhh"

    #turn alarm off
    
    show pink

    "Ugh. And I was having such a good dream too, I finally met the person of my dreams."

    menu:
        "Stay in bed":
            "My eyes drift back to sleep and hope to dream of her."

            scene black
            with fadehold
            hide pink

            scene bg pink room
            with fade

            "When I woke up again, the school day was already almost over. I open my phone and saw that my friend Blue texted me."

            b "Where are youuuuuuuu{w}
            \nIf you don't come I'll be all alone >:({w}
            \nThere's a new girl and she's cute o-o{w}
            \nDon't know if she's gonna be in any of your classes though >:)"

            "I rolled my eyes at his playboy words."

            p "i slept in"

            b "OH NOW YOU RESPOND -_-{w}
            \nI'm already friends w her hehehehe{w}"

            p "whatever"

            scene black
            "{b}01. That was fast{/b}\nYou missed out on what fate could have given you."

            return

        "Get dressed":
            "I drag my body off my bed and towards my closet. I quickly get dressed so I can make something to eat on my way to school."
            scene black
            with slideawayleft
            jump path1

label path1:
    scene bg street
    with slideawayleft

    "As I walk down the street towards my usual train station, I hear someone running towards me."

    b "[name]!!!"

    with vpunch
    "And all a sudden a body tackles me in a hug. When I finally get released I turn to see Blue, my childhood friend."

    b "Oh my god [name], I'm so happy I caught up with you. Were you gonna leave without me, AGAIN?"

    p "Well you didn't wake up on time and were almost late the last few days, I don't see how today would've
    been any different."

    b "But today I actually woke up to my alarm! And I got ready and caught up with you!"

    # stomach growling sound

    b "I guess I should've eaten something though."

    p "I guess that's as good as it'll get with you. Here, I made extra."

    "I handed Blue a piece of my breakfast and he immediately started eating."

    b "You know you're the best, right?"

    p "Sure."

    "I rolled my eyes and continued walking."

    "Blue's been my best friend since we were kids. He's been there for me through everything, and I for him."

    "We try to walk to school together as often as we can, but Blue always stay up late talking to one of his million girlfriends so I end up walking alone while he either sleeps in or runs to catch up to me."

    p "So which girl were you talking to this time?"

    b "Why do you always assume it's a girl? How do you know I wasn't playing games with Nico again?"

    p "Because you and Nico fought a few days ago and you still refuse to talk to him."

    "Blue let out a sigh and stayed silent when he realized I got him."

    b "Fine! You got me! It was Grace, but it's not for the reason you think it is."

    p "Are you sure about that?"

    b "Yes! She said there's gonna be a new transfer student, and she's gonna be in some of our classes too."

    p ""