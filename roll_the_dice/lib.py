# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for roll_the_dice Project
"""

from os.path import split
import pandas as pd
import random


def roll(num):
    return random.randint(1, num)


if __name__ == '__main__':
    print('Rolled the dice')

