from create_example import create_example
from organize.core import CATEGORIES
from organize.core import organize
from clear import clear
import time

clear("logs")

time_spans = []
amount_tests = int(input("Rounds: "))
amount_files = int(input("Files for each: "))

for i in range(amount_tests):
    create_example("example", amount_files)
    start = time.time()
    organize("example", CATEGORIES)
    end = time.time()
    total_time = f"{end - start:.4}"
    time_spans.append(float(total_time))

print(f"{amount_tests} rounds made.")
print(f"{amount_files} files each round.")

average_time = sum(time_spans) / len(time_spans)
print(f"Average time: {average_time:.4f}")

j = 0
for i in time_spans:
    print(i)
    j += 1
    if j >= 5:
        break