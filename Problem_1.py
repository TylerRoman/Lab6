#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:58:34 2017

@author: Hudson
"""

x = 6
for i in range(x):
    print('*', end='')
    for c in range(i):
        print(' ', end='')
    print('*')