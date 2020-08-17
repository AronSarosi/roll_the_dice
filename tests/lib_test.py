# -*- coding: UTF-8 -*-

# Import from standard library
import os
import roll_the_dice
import pandas as pd
# Import from our lib
from roll_the_dice.lib import roll
import pytest


def test_roll():
    result = roll(6)
    assert len(str(result)) == 1
    assert result >= 1 and result <= 6
