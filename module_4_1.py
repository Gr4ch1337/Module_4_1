from fake_math import divide as dev_fake
from true_math import divide as dev_true

result_1 = dev_fake(10, 5)
result_2 = dev_fake(10, 0)
result_3 = dev_true(15, 10)
result_4 = dev_true(15, 0)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
