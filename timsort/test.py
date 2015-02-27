# -*- coding: utf-8 -*-
import random
import time

from timsort import sort


for _ in range(100000):
    array = [random.randrange(10000) for _ in range(random.randrange(10000))]
    st = time.time()
    sort(array)
    print('My sort time: {0}'.format(time.time()-st))
    st = time.time()
    sorted(array)
    print('Python builtin sort time: {0}'.format(time.time()-st))

#I know, random array's are bad for this...

# Some from CPython:
# My sort time: 0.2569599151611328
# Python builtin sort time: 0.0017349720001220703
# My sort time: 0.026814937591552734
# Python builtin sort time: 0.000347137451171875
# My sort time: 0.28528499603271484
# Python builtin sort time: 0.0016350746154785156
# My sort time: 0.42363786697387695
# Python builtin sort time: 0.0024089813232421875
# My sort time: 0.07357501983642578
# Python builtin sort time: 0.0007359981536865234
# My sort time: 0.072113037109375
# Python builtin sort time: 0.0006880760192871094
# My sort time: 0.1123499870300293
# Python builtin sort time: 0.0009589195251464844


#And PyPy (WTF)
# My sort time: 0.0174520015717
# Python builtin sort time: 0.000556945800781
# My sort time: 0.00606203079224
# Python builtin sort time: 0.000696182250977
# My sort time: 0.0244889259338
# Python builtin sort time: 0.000746011734009
# My sort time: 0.0592520236969
# Python builtin sort time: 0.00103187561035
# My sort time: 0.0628960132599
# Python builtin sort time: 0.00111603736877
# My sort time: 0.0174908638
# Python builtin sort time: 0.000720024108887
# My sort time: 0.00206089019775
# Python builtin sort time: 0.000234842300415
# My sort time: 0.0233130455017
# Python builtin sort time: 0.000836133956909
# My sort time: 0.0181169509888
# Python builtin sort time: 0.000792980194092
# My sort time: 0.0334692001343
# Python builtin sort time: 0.000840902328491
# My sort time: 0.00259709358215
# Python builtin sort time: 0.000266075134277
# My sort time: 0.00976300239563
# Python builtin sort time: 0.000649929046631
# My sort time: 0.00919818878174
# Python builtin sort time: 0.000432014465332
# My sort time: 0.0695259571075
# Python builtin sort time: 0.00101494789124
# My sort time: 0.00786399841309
# Python builtin sort time: 0.000699996948242
# My sort time: 0.0679938793182
# Python builtin sort time: 0.000970840454102
# My sort time: 0.0149910449982
# Python builtin sort time: 0.00062108039856