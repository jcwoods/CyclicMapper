CyclicMapper
------------
This class is intended to translate a set of linear values into (x,y)
coordinates mapped onto the perimeter of a circle.  In particular, this is
useful for mapping data which is cyclic in nature.

Consider the process of in building vectors for k-means clustering.  Some data
which might be used in a model is not linear in nature.  This is especially
true of of time, including days of the week, hours of the day, etc.

As an excample, assign the days of the week to a scale 0..6 (Sunday = 0,
Saturday = 6).  On a linear scale, Sunday and Saturday are 6 units apart.

![CyclicMapper problem](/jcwoods/CyclicMapper/images/CyclicMapper-problem.png)

On a circle,

![CyclicMapper problem](/jcwoods/CyclicMapper/images/CyclicMapper-solution.png)

Instead, we map a linear value (0..6) into tuples.  These tuples are x and y
coordinates representing the position of the linear value mapped onto the
perimeter of a circle.  Instead of using a single linear dimension in our
vector, we replace it with these two dimensions.

This DOES NOT preserve the absolute distance between points, but it does
preserve a relative distance that works well for many applications.
