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

![CyclicMapper problem](https://github.com/jcwoods/CyclicMapper/blob/master/images/CyclicData-problem.png?raw=true)

On a circle,

![CyclicMapper solution](https://github.com/jcwoods/CyclicMapper/blob/master/images/CyclicData-solution.png?raw=true)

Instead, we map a linear value (0..6) into tuples.  These tuples are x and y
coordinates representing the position of the linear value mapped onto the
perimeter of a circle.  Instead of using a single linear dimension in our
vector, we replace it with these two dimensions.

This DOES NOT preserve the absolute distance between points, but it does
preserve a relative distance that works well for many applications.


Usage
------------
```python
from cyclicmapper import CyclicMapper

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday' ]

# map days of the week to integer values
days_dict = {}
for v,d in enumerate(days):
    days_dict[d] = v

cm = CyclicMapper(len(days), r = 1)

for d in days:
    xy = cm.getTuple(days_dict[d])
    print('{0:s}: {1:s}'.format(d, str(xy)))
```

This produces the output:

```
CyclicMapper$ python test.py 
Sunday: (1.0, 0.0)
Monday: (0.6234898018587336, 0.7818314824680298)
Tuesday: (-0.22252093395631434, 0.9749279121818236)
Wednesday: (-0.900968867902419, 0.43388373911755823)
Thursday: (-0.9009688679024191, -0.433883739117558)
Friday: (-0.2225209339563146, -0.9749279121818236)
Saturday: (0.6234898018587334, -0.7818314824680299)
```

