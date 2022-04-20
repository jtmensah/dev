import random

from sample_madlibs import hp, code, zombie, hungergames

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()