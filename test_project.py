from funime import game ,  winner , Magicball , FLAMES , flames

def main():
    test_game()
    test_winner()
    test_MagicBall()



def test_game():
    assert game()== None


def test_winner():
    assert winner("g" ,"s")==True
    assert winner("s" ,"w")==True
    assert winner("w" ,"g")==True


def test_MagicBall(capfd):
    Magicball()
    out, err = capfd.readouterr()
    assert out == 'Magic 8 Ball says : It is certain' or 'Magic 8 Ball says : It is decidedly so' or 'Magic 8 Ball says : Yes' or 'Magic 8 Ball says : Reply hazy try again' or 'Magic 8 Ball says : Ask again later' or 'Magic 8 Ball says : Concentrate and ask again' or 'Magic 8 Ball says : My reply is no' or 'Magic 8 Ball says : Outlook not so good' or 'Magic 8 Ball says : Very doubtful'


if __name__ =="__main__":
    main()
