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
    # Only Anna's paragraphs
    for p in anan.paragraphs:
        print(p)

if __name__ == "__main__":
    team_intro()
    story()
