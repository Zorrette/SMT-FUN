#!/usr/bin/env python

# Inspire (a lot) from the Picoctf 2013 Harder Serial

# Damn, you lost THE motivation sentence to survive the LSE !!
# All you remember is some constraint (people use that to remember stuff)
# When you have the serial (the actual interresting part), for even MORE FUN, you can be translate it to a sentence (no space, easy translation), if you think you found it, come to me for reward <3

import sys

def check_serial(serial):
  if (not set(serial).issubset(set(map(str,range(10))))):
    print ("only numbers allowed")
    return False
  if len(serial) != 18:
    return False
  if int(serial[15]) + int(serial[4]) != 14:
    return False
  if int(serial[1]) * int(serial[17]) != 0:
    return False
  if int(serial[15]) / int(serial[6]) != 9:
    return False
  if int(serial[17]) - int(serial[0]) != -2:
    return False
  if int(serial[5]) - int(serial[17]) != 9:
    return False
  if int(serial[15]) - int(serial[1]) != 3:
    return False
  if int(serial[1]) * int(serial[10]) != 48:
    return False
  if int(serial[8]) + int(serial[13]) != 7:
    return False
  if int(serial[0]) * int(serial[8]) != 4:
    return False
  if int(serial[4]) * int(serial[11]) != 25:
    return False
  if int(serial[8]) + int(serial[9]) != 2:
    return False
  if int(serial[12]) - int(serial[13]) != -3:
    return False
  if int(serial[9]) % int(serial[16]) != 0:
    return False
  if int(serial[14]) * int(serial[16]) != 2:
    return False
  if int(serial[7]) - int(serial[4]) != 4:
    return False
  if int(serial[6]) + int(serial[0]) != 3:
    return False
  if int(serial[2]) - int(serial[16]) != -1:
    return False
  if int(serial[4]) - int(serial[6]) != 4:
    return False
  if int(serial[5]) * int(serial[11]) != 45:
    return False
  if int(serial[10]) % int(serial[15]) != 8:
    return False
  if int(serial[11]) / int(serial[3]) != 1:
    return False
  if int(serial[13]) - int(serial[14]) != 4:
    return False
  if int(serial[16]) + int(serial[17]) != 2:
    return False
  return True


key =    []
print ''.join(map(str,key))
print check_serial(map(str,key))
