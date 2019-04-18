#!/usr/bin/env python3
import yaml


def read_data(filename):
    data = None
    with open(filename) as f:
        data = yaml.safe_load(f)

    return data


if __name__ == '__main__':
    x = read_data('2019/apr.yaml')
    print(x)
