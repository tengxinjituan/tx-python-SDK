#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def randomKey():
    code = ''
    for i in range(16):
        ran1 = random.randint(0,9)
        ran2 = chr(random.randint(65,90))
        add = random.choice([ran1,ran2])
        code = ''.join([code,str(add)])
    return code