import anna
import beti
import nohemi
import kiavash
import vanessa
import andre

def team_intro():
    print("This is Team PowerRangers. We are:")
    print(anan.get_name())
    print(beti.get_name())
    print(nohemi.get_name())
    print(kiavash.get_name())
    print(vanessa.get_name())
    print(andre.get_name())

def story():
    # Only Anna's paragraphs
    for p in anna.paragraphs:
        print(p)

if __name__ == "__main__":
    team_intro()
    story()
