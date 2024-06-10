import time

st = time.time()
numbers = []
for i in range(int(1e8)):
    numbers.append(i)
et = time.time()
loop_time = et - st

print(len(numbers))
st = time.time()
numbers_comp = [i for i in range(int(1e6))]
print(len(numbers_comp))
et = time.time()
comp_time = et - st

print(f"loop time = {loop_time}")
print(f"comprehension time = {comp_time}")
