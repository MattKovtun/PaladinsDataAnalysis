import os

import matplotlib.pyplot as plt

from src.paladins_api.utils import DATA_DAILY


DATA_DAILY = '../' + DATA_DAILY
file_names = os.listdir(DATA_DAILY)
file_names.sort()

number_of_matches = []

for file in file_names:
    with open(DATA_DAILY + file) as input_file:
        n = int(input_file.readline())
        number_of_matches.append(n)

print(number_of_matches)


plt.figure(figsize=(16, 8))
plt.plot(number_of_matches)
plt.savefig('graphic.png')
plt.show()
