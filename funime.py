import random
import art
from pyfiglet import Figlet
from pyfiglet import figlet_format

def main():
    while True:
        print(art.text2art("Welcome  to  Funime! "))
        print("- 1 for Snake Water Gun\n- 2 for Mathquizz\n- 3 for FLAMES\n- 4 for Magic 8 Ball")
        user_input_game = game()
        if user_input_game ==1:
            snake()
        elif user_input_game==2:
            Mathquiz()
        elif user_input_game==3:
            FLAMES()
        elif user_input_game==4:
            Magicball()
        else:
            continue
        ask = input("Do you want to continue playing? y/n: ").lower()
        print("To exit anytime in game press [ctrl+c] ")
        if ask in ["no" ," n"]:
            break



def game():
    try:
        x=int(input("Click ctrl+c to exit \nWhich game would you like to play ? :" ))
        if x not in [1,2,3,4]:
            raise Exception()

    except (ValueError , Exception):
        print("please Enter a value in 1 , 2 , 3 ,4")
    else:
        return x


def snake():
    figlet = Figlet()
    fonts = figlet.getFonts()
    art = figlet_format(" Snake water gun " , font ="slant" , width = 200  )
    print(art)
    user_choice = input("SELECT 'w' for water, 's' for snake, 'g' for gun \n")
    laptop_choice= random.choice(["s","w","g"])
    if user_choice==laptop_choice:
        print("Tied")
    elif winner(user_choice,laptop_choice):
        print("Congrats You won!!")
    else:
        print("Oops You Lost!")


def winner(p1,p2):
    if (p1=="g" and p2=="s") or (p1=="s" and p2=="w") or(p1=="w" and p2=="g"):
        return True



def Mathquiz():
    figlet = Figlet()
    fonts = figlet.getFonts()
    art = figlet_format("Maths  Quizz " , font ="slant" , width = 200 )
    print(art)
    lvl = get_level()
    num_correct = generate_integer(lvl)
    print('Score:', num_correct)

def get_level():
    #loop starts
    while True:
        try:
            i = int(input('Level: '))
            if i not in range(1,4):
                raise ValueError
            else:
                return i
        except ValueError:
            continue

def generate_integer(level):
    score = 0
    if level == 1:
        for _ in range(10):
            a = random.randint(0,9)
            b = random.randint(0,9)
            attempt = 0
            while True:
                if attempt == 3:
                    print((f'{a} + {b} = {a+b}'))
                    break
                i = int(input(f'{a} + {b} = '))
                if i == a + b:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempt += 1
        return score
    elif level == 2:
        for _ in range(10):
            a = random.randint(10,99)
            b = random.randint(10,99)
            attempt = 0
            while True:
                if attempt == 3:
                    print((f'{a} + {b} = {a+b}'))
                    break
                i = int(input(f'{a} + {b} = '))
                if i == a + b:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempt += 1
        return score
    else:
        for _ in range(10):
            a = random.randint(100, 999)
            b = random.randint(100, 999)
            attempt = 0
            while True:
                if attempt == 3:
                    print((f'{a} + {b} = {a+b}'))
                    break
                i = int(input(f'{a} + {b} = '))
                if i == a + b:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempt += 1
    return score

def FLAMES():
    figlet = Figlet()
    fonts = figlet.getFonts()
    art = figlet_format(" -_FLAMES -_" , font ="slant" , width = 200 )
    print(art)
    rel= flames()
    print("Relationship status is :", rel)



def flames(n):
    n1=input("Enter 1st name : ")
    n2=input("Enter 2nd name : ")
    print("\nFLAMES : \nF - Friends\nL - Love\nA - Affection\nM - Marriage\nE - Enemy\nS - Siblings\n")
    con =n1+n2
    for i in con:
        if con.count(i)!=1:
            con=con.replace(i,"")

    n=len(con)%6


    if n ==1:
        return "Friends"
    elif n==2:
        return "Love"
    elif n==3:
        return "Affection"
    elif n==4:
        return "Marriage"
    elif n==5:
        return "Enemy"
    elif n==6:
        return "Siblings"

def Magicball():
    figlet = Figlet()
    fonts = figlet.getFonts()
    art = figlet_format(" * Magic Ball *" , font ="slant" , width = 200 )
    print(art)

    answerNumber = random.randint(1, 9)
    if answerNumber == 1:
        print('Magic 8 Ball says : It is certain')
    elif answerNumber == 2:
        print('Magic 8 Ball says : It is decidedly so')
    elif answerNumber == 3:
        print('Magic 8 Ball says : Yes')
    elif answerNumber == 4:
        print('Magic 8 Ball says : Reply hazy try again')
    elif answerNumber == 5:
        print('Magic 8 Ball says : Ask again later')
    elif answerNumber == 6:
        print('Magic 8 Ball says : Concentrate and ask again')
    elif answerNumber == 7:
        print('Magic 8 Ball says : My reply is no')
    elif answerNumber == 8:
        print('Magic 8 Ball says : Outlook not so good')
    elif answerNumber == 9:
        print('Magic 8 Ball says : Very doubtful')



if __name__=="__main__":
    main()














