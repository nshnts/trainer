#!/usr/bin/env python3
import argparse
import numpy as np


class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def get_optimal_align_size(lifts):

    lengths = [[[len(z) for z in y] for y in x] for x in lifts]
    return max(sum(sum(lengths, []), [])) + 3 # pad with extra 3 spaces


def get_lifts_for_day(lifts):
    x = []
    for excs in lifts:
        idx = np.random.randint(0, len(excs))
        x.append(excs[idx])
    return x


def day_program(lifts, mode):

    is_main_mode = mode == 'm'
    indent = ' ' * 10
    align = get_optimal_align_size(lifts)
    print()
    print(Color.GREEN + indent + ('Main Day' if is_main_mode else 'Accessory Day') + Color.END)
    for x in get_lifts_for_day(lifts[0] if is_main_mode else lifts[1]):
        print(indent + x)
    print()


def create_weekly_program(lifts, n_days=4):

    main, accessories = lifts
    if n_days % 2 != 0:
       raise ValueError('Cannot have odd-numbered workouts in a week')

    days = []

    for i in range(int(n_days / 2)):
       days.append(get_lifts_for_day(main))
       days.append(get_lifts_for_day(accessories))

       diff = len(days[i*2]) - len(days[i*2 + 1])
       if diff > 0:
           days[i*2 + 1].extend([ ' ' ] * diff)
       elif -diff > 0:
          days[i*2].extend([ ' ' ] * -diff)

    indent = ' ' * 10
    align = get_optimal_align_size(lifts)

    s = '\n{}' + ''.join(['{:' + str(align) + '}'] * n_days)
    days_str = [('Day '+str(i+1)) for i in range(n_days)]
    print(Color.GREEN + s.format(indent, *days_str) + Color.END)
    n_rows = len(days[0])
    for row in range(n_rows):
        line = indent
        for day in days:
            s = line + '{:<' + str(align) + '}'
            line = s.format(day[row])
        print(line)
    print('\n')


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", default='w', help="main, accessory or full week schedule")
    args = parser.parse_args()
    if args.mode not in [
            'w', # full week schedule
            'm', # main day
            'a'  # accessory day
    ]:
        raise ValueError('Wrong mode')

    lifts = [
        [ # main lifts
           [ 'Squat', 'Front Squat', 'Pause Squat', 'Pause Front Squat'   ], # squat
           [ 'Deadlift', 'Romanian Deadlift', 'Single-Leg Deadlift'       ], # deadlift
           [ 'Bench', 'DB Bench', 'CG Bench', 'Pause Bench'               ], # bench
           [ 'T-Bar Row', 'DB Row', 'Pull-Up', 'Power Clean'              ]  # pull
        ],
        [ # accessories
            [ 'Press', 'DB Press', 'Seated Press', 'Front Raise'           ], # shoulder
            [ 'EZ-Bar Curl', 'DB Curl', 'BB Curl', 'Hammer Curl'           ], # bi
            [ 'Dip', 'LTE', 'DB LTE', 'Ring Push-Up'                       ], # tri
            [ 'Torque', 'Hanging Leg Raise', 'Sit-Up', 'Plank'             ]  # abs
        ]
    ]

    if args.mode == 'w':
        create_weekly_program(lifts)
    else:
        day_program(lifts, args.mode)


if __name__ == '__main__':

    main()
