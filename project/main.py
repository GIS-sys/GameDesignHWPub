from displayer import Displayer
from engine import Engine


if __name__ == "__main__":
    engine = Engine()
    displayer = Displayer(engine)
    displayer.run()

