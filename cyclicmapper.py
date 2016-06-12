#!/usr/bin/python

import sys
import math

# this class is intended to map a linear set of values into (x,y) coordinates
# translated onto the circumference of a circle.
#
# In particular, this is useful for mapping data which is cyclic in nature.
#
# Consider the geometry of building vectors for k-means clustering.  Some
# data which might be used in a model is not linear in nature.  This is
# especially true of days of the week, hours of the day, etc.  If we assign
# the values 0 to Sunday and 6 to Saturday, (depending on the intent of the
# model!) these days may not be six days apart!
#
# Here, we map a linear value (0..6) into tuples.  These tuples are x and y
# coordinates representing the position of the linear value mapped onto the
# perimeter of a circle.  Instead of using a single linear dimension in our
# vector, we replace it with these two dimensions.
#
# This DOES NOT preserve the absolute distance between points, but it does
# preserve a relative distance that works well for many applications.

class CyclicMapper:
    def __init__(self, maxValue, r = None, c = None, d = None):

        self.twopi = math.pi * 2

        # regardless of the parameter we're given, we will normalize
        # to a radius here.

        if r is not None:
            self.radius = float(r)
        elif c is not None:
            self.radius = float(c) / self.twopi
        #elif d is not None: 
        #    self.radius = float(d)
        else:
            raise RuntimeError('missing required parameter (r, c, or d)')

        self.max_val = float(maxValue)    # highest value to be passed in
        return

    def getTuple(self, val):
        if val < 0 or val >= self.max_val:
            errMsg = 'input value {0:f} outside of range (0, {1:f})'.format(val, self.max_val)
            raise ValueError(errMsg)

        x = math.cos((float(val) / self.max_val) * self.twopi) * self.radius
        y = math.sin((float(val) / self.max_val) * self.twopi) * self.radius
        return (x,y)

def main():
    conv = CyclicMapper( (24 * 7), r=1)

    for line in sys.stdin:
        val = int(line.strip())
        print(str(conv.getTuple(val)))

if __name__ == "__main__":
    main()
    sys.exit(0)
