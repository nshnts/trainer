#!/usr/bin/env python3
import ui
import numpy as np


def generate_program(lifts):
    # Assumes there are only two sections in the lifts:
    #   -- Main Lifts
    #   -- Accessories

    program = {}
    for section in lifts:
        program[section['type']] = []

    for section in lifts:
        type = section['type']
        color = section['color']

        for lift, excs in section['exercises'].items():
            idx = np.random.randint(0, len(excs))
            program[type].append(excs[idx])

    main, accessories = program.values()
    diff = len(main) - len(accessories)
    if diff > 0:
        accessories.append(' ' * diff)
    elif -diff > 0:
        main.append(' ' * -diff)

    indent = ' ' * 10
    column_a, column_b = [section['type'] for section in lifts]

    print()
    ui.info(ui.green, (indent + '{:20}' + (' ' * 10)).format(column_a), ui.yellow, column_b)
    for x, y in zip(main, accessories):
        s = indent + '{:20} ' + (' ' * 10) + '{:20}'
        ui.info(s.format(x, y))
    print()

def main():

    lifts = [
        # main lifts
        {
            'type': 'Main Lifts',
            'color': ui.green,
            'exercises': {
                'squat'    : [ 'Squat', 'Front Squat', 'Pause Squat', 'Pause Front Squat'   ],
                'dl'       : [ 'Deadlift', 'Romanian Deadlift', 'Single-Leg Deadlift'       ],
                'bench'    : [ 'Bench', 'DB Bench', 'CG Bench', 'Pause Bench'               ]
            }
        },

        #accessories
        {
            'type': 'Accessories',
            'color': ui.yellow,
            'exercises': {
                'back'     : [ 'T-Bar Row', 'DB Row', 'Pull-Up', 'Power Clean'              ],
                'shoulder' : [ 'Press', 'DB Press', 'Seated Press', 'Front Raise'           ],
                'bi'       : [ 'EZ-Bar Curl', 'DB Curl', 'BB Curl', 'Hammer Curl'           ],
                'tri'      : [ 'Dip', 'LTE', 'DB LTE', 'Ring Push-Up'                       ],
                'abs'      : [ 'Torque', 'Hanging Leg Raise', 'Sit-Up', 'Plank'             ]
            }
        }
    ]

    generate_program(lifts)


if __name__ == '__main__':
    main()
