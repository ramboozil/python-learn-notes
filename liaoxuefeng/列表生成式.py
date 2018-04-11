# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() if isinstance(x, str) else x for x in L1]
print(L2)

a = 3
a, b = 1, a
print('a=', a, '\n''b=', b)
