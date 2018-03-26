
# 1.
import ex09_module

a = ex09_module.SubDemo(12, 34)
a.hello()
a.bye()
b = ex09_module.SubDemo(56, 78)
b.hello()
b.bye()

# 2. from
from ex09_module import *
from ex09_module import SubDemo

c = SubDemo(11, 22)
c.hello()
c.bye()

# 3. as
import ex09_module as test

d = test.SubDemo(77, 88)
d.hello()
d.bye()

# 4. from as
from ex09_module import SubDemo as test

e = test(99, 00)
e.hello()
e.bye()

