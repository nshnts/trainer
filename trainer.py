#!/usr/bin/env python3
import numpy as np


class Color:
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def generate_program(lifts, workout_name):
    # Assumes there are only two sections in the lifts:
    #   -- Main Lifts
    #   -- Accessories
    indent = ' ' * 10

    print()
    print(' ' * 5 + Color.GREEN + 'Workout ' + workout_name + Color.END)

    program = {}
    for section in lifts:
        program[section['type']] = []

    for section in lifts:
        type = section['type']
        for lift, excs in section['exercises'].items():
            idx = np.random.randint(0, len(excs))
            program[type].append(excs[idx])

    main, accessories = program.values()
    diff = len(main) - len(accessories)
    if diff > 0:
        accessories.extend([ ' ' ] * diff)
    elif -diff > 0:
        main.extend([ ' ' ] * -diff)

    column_a, column_b = [section['type'] for section in lifts]

    print()

    print(indent, ('{:12}' + (' ' * 10)).format(Color.YELLOW + Color.UNDERLINE + column_a+ Color.END),
          ' ' * 9, ('{:12}' + (' ' * 10)).format(Color.YELLOW + Color.UNDERLINE + column_b + Color.END))
    for x, y in zip(main, accessories):
        s = indent + ' {:20} ' + (' ' * 10) + '{:20}'
        print(s.format(x, y))
    print()


def weekly_program(lifts):
    generate_program(lifts, 'A')
    generate_program(lifts, 'B')


def main():

    lifts = [
        # main lifts
        {
            'type': 'Main Lifts',
            'exercises': {
                'squat'    : [ 'Squat', 'Front Squat', 'Pause Squat', 'Pause Front Squat'   ],
                'dl'       : [ 'Deadlift', 'Romanian Deadlift', 'Single-Leg Deadlift'       ],
                'bench'    : [ 'Bench', 'DB Bench', 'CG Bench', 'Pause Bench'               ],
                'back'     : [ 'T-Bar Row', 'DB Row', 'Pull-Up', 'Power Clean'              ],
            }
        },
        #accessories
        {
            'type': 'Accessories',
            'exercises': {
                'shoulder' : [ 'Press', 'DB Press', 'Seated Press', 'Front Raise'           ],
                'bi'       : [ 'EZ-Bar Curl', 'DB Curl', 'BB Curl', 'Hammer Curl'           ],
                'tri'      : [ 'Dip', 'LTE', 'DB LTE', 'Ring Push-Up'                       ],
                'abs'      : [ 'Torque', 'Hanging Leg Raise', 'Sit-Up', 'Plank'             ]
            }
        }
    ]

    weekly_program(lifts)


if __name__ == '__main__':
    main()
