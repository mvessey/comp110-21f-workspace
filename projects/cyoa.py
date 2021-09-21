"""Choose your adventure: A Paranormal Ghost Game."""

__author__ = "730409403"

from random import randint
plays: int = 0
player: str = ""
points: int = int(randint(0, 4))
ghost: str = '\U0001F47B'
angry_ghost: str = '\U0001F47F'
death: str = '\U0001F480'


def greet() -> None:
    """Welcome to the Game!"""
    global player
    print("Welcome to my first game. In this game you will be interacting with a ghost via an spirit board. But be sure to be careful, angering the ghost can lead to unfortunate consequences.")
    player = input("What is your name? ")
    print("Thank you for playing, " + player + "!!")


def main() -> None: 
    """Welcome to the Game: Wishes."""
    global points
    greet()
    wishes: str = input("Do you wish to continue? (yes/no/instructions) ")
    if wishes == "no":
        goodbye()
    if wishes == "yes":
        game(points)
    if wishes == "instructions":
        instructions()


def instructions() -> None:
    """Intruction explanation section."""
    print("Instructions: ")
    print("This is a game in which you the player will be interacting with ghosts through a spirit board. To ask questions, simply select the letter ex (a) with the corresponding question you wish to ask. However, be careful about what questions you ask. The ghost may react negatively.")
    print("")
    print("The attitude of the ghost will change throughout the course of your interview, and will be measured through 'action points'. A larger number of action points suggests ghost agitiation, while a smaller number suggests a docile attitude. Keep in mind repeating questions increases ghost agitation.")
    print("The initial attitude of the ghost is random.")
    print("")
    main()


def goodbye() -> None:
    """Message for ending game."""
    print("Maybe you have a skeptical mind, maybe you have skitish demeanor. Regardless of which, perhaps it is best that do not speak with the dead. Who knows how dangerous it could be. ")
    print(" ")
    print("Thank you for playing, " + player + "!")
    print("You have earned: " + str(points) + " action points just by opening up the game")


def game(points: int) -> None:
    """Beginning the Game."""
    print("You are an amature ghost researcher hoping to gather evidence to prove the existance of paranormal activity for your senior year research project. You have collected little to no evidence, and this is mostly a last resort. However, hoping to gather even the slightest bit of evidence, you have found youself sitting in front of an ouji board in a supposedly haunted hotel, ready to begin your final investigation. What question do you want to ask first?")
    print("(a) Is anyone there?")
    print("(b) Come out, come out wherever you are.")
    question_1: str = input("Which do you chose? ")
    print("The board slowly reads out, 'I CAN HEAR YOU'.")
    while points < 10:
        if question_1 == "a":
            points = points + 2
            print("(a) Who is this?")
            print("(b) What is this?")
            print("(c) How did you get here?")
            print("(d) How did you die?")
            question_2: str = input("What do you chose? ")
            if question_2 == "a":
                print("The board writes out 'MARA'")
                points == points + 1
            else:
                if question_2 == "b":
                    print("The board writes out, 'A GIRL'.")
                    points == points + 3
                else:
                    if question_2 == "c":
                        print("The board writes out, 'I THINK I DIED'.")
                        points == points + 2
                    else:
                        print("The board writes out, 'I HIT MY HEAD.'")
                        points = points + 4
        else:
            if question_1 == "b":
                points = points * 2
                print("(a) Who is this?")
                print("(b) What is this?")
                print("(c) How did you get here?")
                print("(d) How did you die?")
                question_2b: str = input("How do you respond? ")
                if question_2b == "a":
                    print("The board writes out 'A GIRL'")
                    points == points + 2
                else:
                    if question_2b == "b":
                        print("The board writes out, 'WHAT DO YOU MEAN?'.")
                        points == points + 4
                    else:
                        if question_2b == "c":
                            print("The board writes out, 'WHY WOULD I TELL YOU?'.")
                            points == points + 3
                        else:
                            print("The board writes out, 'I DO NOT KNOW.'")
                            points = points + 5
    if points < 13:
        question_3: str = input("It is beginning to seem like the ghost is tiring. Hopefully you have answered all of the questions you need for your project. Do you wish to risk one last time? (yes/no) ")
        if question_3 == "yes":
            print("The ghost reveals itself, allowing you to snap a picture for your research paper.")
            print(ghost)
        else:
            print("You put the board away, and manage to leave the hotel with many questions answered.")
    if points >= 13:
        question_3b: str = input("No matter how many questions you ask the ghost will no longer respond. Do you wish to risk one last time? (yes/no) ")
        if question_3b == "yes":
            print("You move to ask a final question and suddenly the lights go out in the room and you see the form of the being you have been talking to, looking quite angry.")
            print(angry_ghost)
            print(death)
        else:
            print("You pack up your things and manage to safetly leave the hotel, maybe without alot of questions answered but at least with your life.")
    print("Action points earned: " + str(points))


if __name__ == "__main__":
    main()