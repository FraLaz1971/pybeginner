#!/usr/bin/env python3
# shows command line input parameters
# given as program arguments

import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
if (len(sys.argv) < 3) :
    print('input error: wrong number of arguments! Two values needed.')
    print('this program compute n powered to m ')
    print('usage:', sys.argv[0], '<n> <m>')
else:
    print('n^m: ', sys.argv[1]+'^'+sys.argv[2]+' = ',int(sys.argv[1])**int(sys.argv[2]))
