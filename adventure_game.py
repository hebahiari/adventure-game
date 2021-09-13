import time
import random

# fuction definitoins:

# general functions:


def print_pause(text):
    print(text+"\n")
    time.sleep(2)


def loading():
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")


def riddle(riddle_text, correct_answer, number_of_answers):
    print_pause(riddle_text)
    answer = input("(enter your answer)\n").lower()
    loading()
    if correct_answer in answer:
        return True
    else:
        if number_of_answers == 0:
            try_again(riddle_text, correct_answer, number_of_answers)
        else:
            game_over(correct_answer)


def try_again(riddle_text, correct_answer, number_of_answers):
    print_pause("\nwrong answer! you have one more try!\n")
    number_of_answers += 1
    riddle(riddle_text, correct_answer, number_of_answers)


def play_again():
    reply = input("would you like play again? y/n \n").lower()
    if reply == "y":
        game()
    else:
        exit()


def intro():
    f = random.choice([
        intro1,
        intro2,
        intro3,
    ])

    f()

# game functions:


def intro1():
    print_pause("""           _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \\
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._

    """)
    print_pause("the story of a treasure has been around for centuries ..")
    print_pause("guarded by flames and strong winds ..")
    print_pause("no one who tried to get it made it out alive .. ")
    print_pause("but your village is struggling ..")
    print_pause("and as the keeper of the village .. ")
    print_pause("its your duty to help ..")
    print_pause("today is the day .. you decide to go to the cave")
    print_pause("you walk a long way .. and finally reach your destination")
    print_pause("you stand by the huge rock covering the entrance ..")


def intro2():
    print_pause("""           _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \\
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._

    """)
    print_pause("many years ago, an elder in your village told you a story ..")
    print_pause("the elder spoke of a hidden treasure in a cave ..")
    print_pause("many entered the cave but none returned ..")
    print_pause("a year has passed since the last attempt ..")
    print_pause("the village elders have chosen you this time ..")
    print_pause("it's your turn to make the same journey ..")
    print_pause("you pack your belongings and journey to the cave ..")
    print_pause("but the cave is blocked by a huge rock .. ")
    print_pause("is this the end of your journey?")


def intro3():
    print_pause("""           _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \\
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._

    """)
    print_pause("have you heard of the cave with infinite treasures?")
    print_pause("many in your village have entered the cave ..")
    print_pause("but none have returned ..")
    print_pause("one night when you were asleep ..")
    print_pause("you had a vivid dream of that same cave ..")
    print_pause("it called you by your name ..")
    print_pause("you decide to answer the call.. ")
    print_pause("you set out on what might be your final journey .. ")
    print_pause("but when you reach the cave ..")
    print_pause("you find the entrance blocked ..")
    print_pause("by the biggest rock you have ever seen ..")


def fire_chamber():
    print_pause("a few seconds later you hear a voice .. ")
    print_pause("ANSWER THIS RIDDLE TO ENTER THE FIRST CHAMBER")
    riddle("FEED ME AND I LIVE, WATER ME AND I'LL DIE. WHAT AM I?", "fire", 0)


def water_chamber():
    print_pause("""
                (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
    print_pause("the door slowly starts the move, revealing a dark chamber ..")
    print_pause("you walk inside .. and the rock moves back to lock you in ..")
    print_pause("you see a door.. you knock on it and hear the voice again ..")
    print_pause("I see you've made it into the first chamber, ")
    print_pause("the next one will be harder to get into,")
    print_pause("and if you answer wrong, you will die")
    riddle("""GENTLE ENOUGH TO SOOTHE THE SKIN, HARD ENOUGH TO CRACK ROCKS,
    WHAT AM I?""", "water", 0)


def air_chamber():
    print_pause("""
    _\/_                 |                _\/_
    /o\\             \       /            //o\\
     |                 .---.                |
    _|_______     --  /     \  --     ______|__
            `~^~^~^~^~^~^~^~^~^~^~^~`
""")
    print_pause("the second door opens! ")
    print_pause("you enter the second chamber .. ")
    print_pause("you hear the voice again ..")
    print_pause("good job! you're halfway there .. but it wont be so easy!")
    riddle("""I AM LIGHT AS A FEATHER, BUT NOT EVEN THE STRONGEST MAN IN
    THE WORLD CAN HOLD ME FOR MORE THAN A FEW MINUTES, WHAT AM I?""", "air", 0)


def earth_chamber():
    print_pause("""
                  _
              (`  ).                   _
             (     ).              .:(`  )`.
)           _(       '`.          :(   .    )
        .=(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .+(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.-(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.---.
""")
    print_pause("the wall rips open revealing a huge room!")
    print_pause("you see the treasure on the other side of the room .. ")
    print_pause("while walking towards it, you hear the voice .. ")
    print_pause("NOT YET! YOU HAVE ONE MORE TO SOLVE!")
    riddle("""I AM A MOTHER, FROM A FAMILY OF EIGHT, I SPIN AROUND ALL DAY,
DESPITE MY WEIGHT, HAD A NINTH SIBLING, BEFORE FINDING OUT ITS FAKE,
WHAT AM I?""", "earth", 0)


def you_win():
    print_pause("""
o               .        ___---___                    .
       .              .--\        --.     .     .         .
                    ./.;_.\     __/~ \.
                   /;  / `-'  __\    . \
 .        .       / ,--'     / .   .;   \        |
                 | .|       /       __   |      -O-       .
                |__/    __ |  . ;   \ | . |      |
                |      /  \\_    . ;| \___|
   .    o       |      \  .~\\___,--'     |           .
                 |     | . ; ~~~~\_    __|
    |             \    \   .  .  ; \  /_/   .
   -O-        .    \   /         . |  ~/                  .
    |    .          ~\ \   .      /  /~          o
  .                   ~--___ ; ___--~
                 .          ---         .

""")
    print_pause("I cant believe it .. you did it!")
    print_pause("you can now take the treasure!, you deserve it!")
    print_pause("CONGRATULATIONS!")
    print_pause("""

                                 .__         ._.
 ___.__.  ____   __ __  __  _  __|__|  ____  | |
<   |  | /  _ \ |  |  \ \ \/ \/ /|  | /    \ | |
 \___  |(  <_> )|  |  /  \     / |  ||   |  \ \|
 / ____| \____/ |____/    \/\_/  |__||___|  / __
 \/                                       \/  \/
 """)
    play_again()


def game_over(correct_answer):
    print_pause("WRONG ANSWER!")

    if correct_answer == "fire":
        print_pause("the heat of the sun suddenly becomes unbearable ..")
        print_pause("a flame erupts and you are engulfed in FIRE ..")
        print_pause("you scream and fall to the ground ..")
    elif correct_answer == "water":
        print_pause("the room floods with WATER and you drown!")
    elif correct_answer == "air":
        print_pause("every breath of AIR feels heavier on your lungs ..")
        print_pause("you try your hardest to breathe but you can't ..")
        print_pause("you collapse to the ground and close your eyes ..")
    elif correct_answer == "earth":
        print_pause("the EARTH beneath you begins to tremble ..")
        print_pause("the trembles turn into violent shakes ..")
        print_pause("a large rock falls on you and you are crushed ..")

    print_pause("""
                                                                  ._.
   ____  _____     _____    ____     ____  ___  __  ____  _______ | |
  / ___\ \__  \   /     \ _/ __ \   /  _ \ \  \/ /_/ __ \ \_  __ \| |
 / /_/  > / __ \_|  Y Y  \\  ___/  (  <_> ) \   / \  ___/  |  | \/ \|
 \___  / (____  /|__|_|  / \___  >  \____/   \_/   \___  > |__|    __
/_____/       \/       \/      \/                      \/          \/

 """)
    play_again()

# game:


def game():
    intro()
    fire_chamber()
    water_chamber()
    air_chamber()
    earth_chamber()
    you_win()


game()
