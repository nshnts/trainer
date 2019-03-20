#!/usr/bin/env python3
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


def create_weekly_program(lifts, n_days=4):

    main, accessories = lifts
    if n_days % 2 != 0:
       raise ValueError('Cannot have odd-numbered workouts in a week')

    days = [[] for _ in range(n_days)]

    for i in range(int(n_days / 2)):
       for excs in main:
          idx = np.random.randint(0, len(excs))
          days[i*2].append(excs[idx])

       for excs in accessories:
          idx = np.random.randint(0, len(excs))
          days[i*2 + 1].append(excs[idx])

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

    create_weekly_program(lifts)


if __name__ == '__main__':
    main()
