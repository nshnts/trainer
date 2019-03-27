#!/usr/bin/env python3
import argparse
import numpy as np


class Color:

    use_colors = True
    GREEN = '\033[92m'    if use_colors else ''
    YELLOW = '\033[93m'   if use_colors else ''
    RED = '\033[91m'      if use_colors else ''
    BOLD = '\033[1m'      if use_colors else ''
    UNDERLINE = '\033[4m' if use_colors else ''
    END = '\033[0m'       if use_colors else ''


def get_optimal_align_size(lifts):

    lengths = [[[len(z) for z in y] for y in x] for x in lifts]
    return max(sum(sum(lengths, []), [])) + 3 # pad with extra 3 spaces


def get_lifts_for_day(lifts):
    x = []
    for excs in lifts:
        idx = np.random.randint(0, len(excs))
        x.append(excs[idx])
    return x


def this_lift_has_fixed_rep(lift):
    ret = None
    rep = None
    if isinstance(lift, tuple):
        ret, rep = lift
    else:
        ret = lift
    return ret, rep


def day_program(lifts, mode):

    is_main_mode = mode == 'm'
    indent = ' ' * 10
    align = get_optimal_align_size(lifts)
    print()
    print(Color.GREEN + indent + ('Main Day' if is_main_mode else 'Accessory Day') + Color.END)
    for lift in get_lifts_for_day(lifts[0] if is_main_mode else lifts[1]):
        x, rep = this_lift_has_fixed_rep(lift)
        if rep is None:
            rep = np.random.randint(1, 4) * 4 if is_main_mode else 10
        print(indent + ('{:' + str(align) + '}').format(x) + '  ' +
              '[ {:2} ]'.format(rep))
    print()


def create_weekly_program(lifts, n_days=4):

    is_main_mode = True
    main_mode = 'm'
    accessory_mode = 'a'

    for i in range(n_days):
        day_program(lifts, main_mode if is_main_mode else accessory_mode)
        is_main_mode = not is_main_mode


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

    lifts =  [
        [ # main lifts
            ( 'Squat', 'Front Squat', 'Pause Squat', 'Pause Front Squat' ), # squat
            ( 'Deadlift', 'Romanian Deadlift', 'Stiff-Legged Deadlift'   ), # deadlift
            ( 'Bench', ('DB Bench', 8), 'CG Bench', 'Pause Bench'        ), # bench
            ( 'T-Bar Row', 'Pull-Up'                                     )  # pull
        ],
        [ # accessories
            ( 'Press', 'DB Press', 'Seated Press', 'Front Raise'        ), # shoulder
            ( 'EZ-Bar Curl', 'DB Curl', 'BB Curl', 'Hammer Curl'        ), # bi
            ( 'Dip', 'LTE', 'DB LTE', 'Push-Up'                         ), # tri
            ( 'DB Row', ('Power Clean', 4)                              ), # pull
            ( 'Torque', 'Hanging Leg Raise', 'Sit-Up', 'Plank'          )  # abs
        ]
    ]

    if args.mode == 'w':
        create_weekly_program(lifts)
    else:
        day_program(lifts, args.mode)


if __name__ == '__main__':

    main()
