import argparse
import json

from overwatch import Overwatch


def main():
    args = fetch_args()
    player_data = call_overwatch_api(args.tag)
    return_player_data(player_data(mode=args.mode, filter=args.filter))


def fetch_args():
    parser = argparse.ArgumentParser(
        description='Gets arg for battletag and mode.')
    parser.add_argument('-t', '--tag', type=str,
                        help='tag')
    parser.add_argument('-m', '--mode', type=str,
                        help='mode')
    parser.add_argument('-f', '--filter', type=str,
                        help='filter')
    args = parser.parse_args()
    return args


def call_overwatch_api(tag):
    overwatch = Overwatch(battletag=tag)
    return overwatch


def return_player_data(data):
    print(json.dumps(data, indent=4, separators=(",", ";")))


if __name__ == "__main__":
    main()
