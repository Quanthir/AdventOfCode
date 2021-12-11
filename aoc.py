#!/usr/bin/env python3

import argparse
import os
from template import solution
from importlib import import_module

START_YEAR = 2015
CURRENT_YEAR = 2021
MAX_DAY = 25


class tc:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ULINE = '\033[4m'

def get_dir(year, day):
    """ Returns the dir of given year and day
    """
    year_dir = os.path.join(os.curdir, str(year))
    day_dir = os.path.join(year_dir, str(day).zfill(2))
    return year_dir, day_dir

def create_new_day(year, day):
    """ Creates new day for the given year
    """
    year_dir, day_dir = get_dir(year, day)

    if not os.path.isdir(year_dir):
        os.mkdir(year_dir)

    if day == 0:
        days = [int(x) for x in filter(os.path.isdir, os.listdir(year_dir))]
        days.sort()
        day = days[-1]

        if day >= MAX_DAY:
            return False, f'Cannot create new day because the days for {year} already reached maximum {MAX_DAY}'

    day_dir = os.path.join(year_dir, str(day).zfill(2))

    if not os.path.isdir(day_dir):
        os.mkdir(day_dir)
    else:
        return False, f'{day_dir} is already created before! Override is not implemented yet!'
    
    for file in ['input.txt', 'challenge.txt', 'solution.py']:
        with open(os.path.join(day_dir, file), 'w') as f:
            pass
    
    with open(os.path.join(day_dir, 'solution.py'), 'w+') as f:
        f.write(solution.replace('<year>', str(year)).replace('<day>', str(day)))
    
    os.system(f'chmod +x {day_dir}/solution.py')
    
    return True, f'{tc.BLUE} {day_dir}{tc.ENDC} folder has been created and ready to use.'
        
def run(year, day, parser):
    _, folder = get_dir(year, day)

    if not os.path.isdir(folder):
        parser.error(f'Directory does not exists: {folder}')
        return

    mod = import_module(f'{year}.{str(day).zfill(2)}.solution', __name__)
    klass = getattr(mod, 'Solution')
    solution = klass(folder)
    print(
        f'{tc.HEADER}Advent of Code Code Challenge '+
        f'{{ year => {tc.GREEN + tc.ULINE + str(year) + tc.ENDC + tc.HEADER}, '+
        f'day => {tc.GREEN + tc.ULINE + str(day).zfill(2) + tc.ENDC + tc.HEADER} }}{tc.ENDC}'
    )
    print(f'Solution Part {tc.BLUE}[1]{tc.ENDC}: {tc.GREEN}{solution.part1()}{tc.ENDC}')
    print(f'Solution Part {tc.BLUE}[2]{tc.ENDC}: {tc.GREEN}{solution.part2()}{tc.ENDC}')

def info(year, day, parser):
    _, folder = get_dir(year, day)
    if not os.path.isdir(folder):
        parser.error(f'Directory does not exists: {folder}')
        return
    
    with open(f'{folder}/challenge.txt') as f:
        print(f.read())
        

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solutions by Gökhan Öztürk')
    parser.add_argument('year', metavar='year', type=int, default=CURRENT_YEAR, help='Event year')
    parser.add_argument('day', metavar='day', type=int, default=0, help='Event day')
    parser.add_argument('-c', '--create', action='store_true', help='Creates a new day')
    parser.add_argument('-r', '--run', action='store_true', help='Runs the given day in the given year.')
    parser.add_argument('-i', '--info', action='store_true', help='Prints the challenge info of given year and day.')

    args = parser.parse_args()
    
    if not args.create and args.year < START_YEAR or args.year > CURRENT_YEAR:
        parser.error(f'Year cannot be lower than {START_YEAR} or greater than {CURRENT_YEAR}')
        return
    
    if (not args.create and args.day < 1) or args.day > MAX_DAY:
        parser.error(f'Day cannot be lower than 1 or greater than {MAX_DAY}')
        return
    
    if args.create:
        res, text = create_new_day(args.year, args.day)
        if not res:
            parser.error(text)
        else:
            print(text)
        return
    
    if args.run:
        run(args.year, args.day, parser)
        return
    
    if args.info:
        info(args.year, args.day, parser)
    

if __name__ == '__main__':
    main()
