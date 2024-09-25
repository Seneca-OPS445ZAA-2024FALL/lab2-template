#!/usr/bin/env python3
# Author: Kamith Balasooriya
# Author ID: bkamith@myseneca.ca
# Date Created: 2024/09/25

import sys


timer = 3


if len(sys.argv) == 2:
    timer = int(sys.argv[1])  


while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
