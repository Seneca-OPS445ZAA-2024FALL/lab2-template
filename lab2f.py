#!/usr/bin/env python3
# Author: Kamith Balasooriya
# Author ID: bkamith@myseneca.ca
# Date Created: 2024/09/25

import sys

if len(sys.argv) != 2:
    print("Usage: ./lab2f.py count")
    sys.exit(1) 
else:
    timer = int(sys.argv[1])

    while timer > 0:
        print(timer)
        timer -= 1

    print("blast off!")
