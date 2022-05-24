import os.path
import time
from string import Template

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

# ===========================

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow', owner='dov')
t.substitute(d)

print(t.safe_substitute(d))

# ==========================

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')  # %d %n %f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
