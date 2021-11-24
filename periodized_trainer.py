#!/usr/bin/env python3
import argparse
import numpy as np


# Program:
#     A year consists of 4 training blocks.
#     Each training block is of 3 month duration.
#     There are two kinds of training blocks - 'Development' and 'Strength'. We alternate between these.
#     Lifts fall under two catgories - 'Main' or 'Accessory'.
#     In a 'Development' block, 'Main' lifts are done for 10 reps (unless stated otherwise).
#     In a 'Strength' block, 'Main' lifts are done for 5 reps (unless stated otherwise).
#     'Accessory' lifts are done for 10 reps (unless stated otherwise).
#     Add clubbell exercise(s) to every training day. Keep it light, but keep it. Shoulders are important!


# Each lift entry is a tuple of main lifts and accessory lifts. 
# You'll notice that some lifts are repeated. It's to make sure it gets picked up more often by the random picker. 
lifts = {
    "squat": (
        ["squat", "squat", "squat", "pause squat", "front squat", "pause front squat"],
        []),
    "deadlift": (
        ["deadlift", "deadlift", "deadlift", "romanian deadlift", "sumo deadlift", "stiff-legged deadlift"],
        []),
    "bench": (
        ["bench", "bench", "bench", "pause bench", "close-grip bench"],
        ["dip", "dip", "dip", "lte", "push-up"]),
    "pull": (
        ["t-bar row", "t-bar row", "pull-up"],
        ["db row", "power clean"])
    }


# these are exercises we must do once per week
# pick one more each group
maintenance_exercises = [
    ["press", "db press"],                                   # shoulders
    ["ez-bar curl", "bb curl", "hammer curl", "db curl"],    # biceps
    ["torque", "hanging leg raise", "plank", "sit-up"],      # abs
    ]

class Color:

    use_colors = True
    GREEN = '\033[92m'    if use_colors else ''
    YELLOW = '\033[93m'   if use_colors else ''
    RED = '\033[91m'      if use_colors else ''
    BOLD = '\033[1m'      if use_colors else ''
    UNDERLINE = '\033[4m' if use_colors else ''
    END = '\033[0m'       if use_colors else ''


def get_lifts_for_day(lifts):
    x = []
    for excs in lifts:
        idx = np.random.randint(0, len(excs))
        x.append(excs[idx])
    return x


def get_random_lift(exercises):
    if not exercises:
        return None
    idx = np.random.randint(0, len(exercises))
    ret = exercises[idx]
    return ret


def this_lift_has_fixed_rep(lift):
    ret = None
    rep = None
    if isinstance(lift, tuple):
        ret, rep = lift
    else:
        ret = lift
    return ret, rep


def print_lift_row(lift, reps, indent):
    align = 25
    sets = "4 x" if reps <= 5 else "3 x"
    print(indent + ('{:' + str(align) + '}').format(lift) + '  ' + sets +
              ' {:2} '.format(reps))    


def day_program(is_development_block, is_squat_day, is_maintenance_day=False):

    main_reps = (10 if is_development_block == True else 5)
    accessory_reps = 10
    maintenance_reps = 10
    
    is_main_mode = is_squat_day
    header_indent = ' ' * 4
    indent = ' ' * 8
    align = 20
    print()
    print(Color.GREEN + header_indent + ('Squat' if is_main_mode else 'Deadlift') + Color.END)
    for group, exercises in lifts.items():
        if is_squat_day and group == "deadlift":
            continue
        elif (not is_squat_day) and group == "squat":
            continue
        elif is_maintenance_day and group not in ["squat", "deadlift"]:
            continue
        elif not exercises:
            continue
        
        main_l = get_random_lift(exercises[0])
        accessory_l = get_random_lift(exercises[1])

        print_lift_row(main_l, main_reps, indent)
        if accessory_l:
            print_lift_row(accessory_l, accessory_reps, indent)

    if is_maintenance_day:
        for exercises in maintenance_exercises:
            random_l = get_random_lift(exercises)
            print_lift_row(random_l, maintenance_reps, indent)
    print()

    
def print_program(is_development_block, is_squat_day):

    # there are 3 training days in a week
    day_program(is_development_block, is_squat_day)
    day_program(is_development_block, not is_squat_day, True)
    day_program(is_development_block, is_squat_day)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--block", default='development', help="development|strength")
    parser.add_argument("-l", "--lift", default='squat', help="squat|deadlift")
    args = parser.parse_args()

    if args.block not in ["development", "strength"]:
        raise ValueError('Invalid training block!')
    if args.lift not in ["squat", "deadlift"]:
        raise ValueError('Invalid main lift!')

    print_program(args.block == "development", args.lift == "squat")


if __name__ == '__main__':

    main()
