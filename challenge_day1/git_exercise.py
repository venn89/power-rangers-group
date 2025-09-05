import anan
import betija
import Nohemi
import Kiavash
import Vanessa
import andre

def team_intro():
    print("This is Team PowerRangers. We are:")
    print(anan.get_name())
    print(betija.get_name())
    print(Nohemi.get_name())
    print(Kiavash.get_name())
    print(Vanessa.get_name())
    print(andre.get_name())

def story():
    all_paragraphs = [
        anan.paragraphs[0],
        betija.paragraphs[0],
        Nohemi.paragraphs[0],
        Kiavash.paragraphs[0],
        Vanessa.paragraphs[0],
        andre.paragraphs[0],
        anan.paragraphs[1],
        betija.paragraphs[1],
        Nohemi.paragraphs[1],
        Kiavash.paragraphs[1],
        Vanessa.paragraphs[1],
        andre.paragraphs[1],
        anan.paragraphs[2],
        betija.paragraphs[2],
        Nohemi.paragraphs[2],
        Kiavash.paragraphs[2],
        Vanessa.paragraphs[2],
        andre.paragraphs[2]
    ]
    for p in all_paragraphs:
        print(p)

if __name__ == "__main__":
    team_intro()
    story()
    