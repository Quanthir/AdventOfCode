#!/usr/bin/env python3

import argparse
from os import error, mkdir
import os
from template import solution

START_YEAR = 2015
CURRENT_YEAR = 2021
MAX_DAY = 25

def create_new_day(year, day):
    """ Creates new day for the given year
    """
    year_dir = os.path.join(os.curdir, str(year))

    if not os.path.isdir(year_dir):
        mkdir(year_dir)

    if day == 0:
        days = [int(x) for x in filter(
            os.path.isdir, os.listdir(year_dir))].sort()
        day = days[-1]

        if day >= MAX_DAY:
            return False, f'Cannot create new day because the days for {year} already reached maximum {MAX_DAY}'

    day_dir = os.path.join(year_dir, str(day).zfill(2))

    if not os.path.isdir(day_dir):
        mkdir(day_dir)
    else:
        return False, f'{day_dir} is already created before! Override is not implemented yet!'
    
    for file in ['input.txt', 'challenge.txt', 'solution.py']:
        with open(os.path.join(day_dir, file), 'w') as f:
            pass
    
    with open(os.path.join(day_dir, 'solution.py'), 'w+') as f:
        f.write(solution.replace('<year>', str(year)).replace('<day>', str(day)))
    
    os.system(f'chmod +x {day_dir}/solution.py')
    
    return True, f'{day_dir} folder has been created and ready to use.'
        
        


def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solutions by Gökhan Öztürk')
    parser.add_argument('year', metavar='year', type=int, default=CURRENT_YEAR, help='Event year')
    parser.add_argument('day', metavar='day', type=int, default=0, help='Event day')
    parser.add_argument('--create', action='store_true', help='Creates a new day. If year is not given, last year is being used.')

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
    

if __name__ == '__main__':
    main()
