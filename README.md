# libraries

CyclicMapper
------------
This class is intended to map a linear set of values into (x,y) coordinates
translated onto the circumference of a circle.

In particular, this is useful for mapping data which is cyclic in nature.

Consider the geometry of building vectors for k-means clustering.  Some
data which might be used in a model is not linear in nature.  This is
especially true of days of the week, hours of the day, etc.  If we assign
the values 0 to Sunday and 6 to Saturday, (depending on the intent of the
model!) these days may not be six days apart!

Here, we map a linear value (0..6) into tuples.  These tuples are x and y
coordinates representing the position of the linear value mapped onto the
perimeter of a circle.  Instead of using a single linear dimension in our
vector, we replace it with these two dimensions.

This DOES NOT preserve the absolute distance between points, but it does
preserve a relative distance that works well for many applications.
