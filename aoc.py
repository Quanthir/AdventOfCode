import argparse

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solutions by Gökhan Öztürk')
    parser.add_argument('year', metavar='year', type=int, help='Event year')
    parser.add_argument('day', metavar='day', type=int, help='Event day')

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()