#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:52:04 2017

@author: Hudson
"""

x = int(input("Enter a number of seconds\n"))
if 60 <= x < 3600:
    print("There are", x//60, "minutes in", x, "seconds")
elif 3600 <= x < 86400:
    print("There are", x//3600, "hours in", x, "seconds")
elif x >= 86400:
    print("There are", x//86400, "days in", x, "seconds")
else:
    print("Error")
