import pytest


@pytest.mark.parametrize('execution_number',range(50))
def test_random_list(execution_number):

   import random

   l = [random.randint(0, 101), random.randint(0, 101),random.randint(0, 101),random.randint(0, 101),random.randint(0, 101),random.randint(0, 101),random.randint(0, 101),random.randint(0, 101),random.randint(0, 101),random.randint(0, 101) ]
   l.sort()
   print(l)

   assert len(l) == 10
   assert l[9] < 101
   assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))