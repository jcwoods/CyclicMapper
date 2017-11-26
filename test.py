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
