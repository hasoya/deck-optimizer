import argparse
from pathlib import Path

from dopt.search.search import Searcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deck Optimizer")
    parser.add_argument("-f", "--file", type=Path, required=True)
    args = parser.parse_args()

    s = Searcher()
    s.load_settings(args.file)

    s.search()

    print("The best deck is")
    print(s.best_deck)
    print("whose probability is")
    print(f"{s.best_prob * 100:.2f}%")

"""     for d, p in s.result.items():
        print(d, p) """
