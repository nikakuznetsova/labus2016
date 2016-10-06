__author__ = 'Timofey F. Khirianov'


import numpy as np
import random
import matplotlib.pyplot as plt


def get_percentile(values, bucket_number):
    bucket_width = 100/bucket_number
    buckets_left_boundaries = []
    for i in range(bucket_number):
        buckets_left_boundaries.append(np.percentile(values, i*bucket_width))
    if min(values) >= 0:
        buckets_left_boundaries[0] = 0.0
    return buckets_left_boundaries


def get_percentile_number(value, percentiles):
    i = 0
    while i < len(percentiles) and percentiles[i] <= value:
        i += 1
    return i-1


def value_equalization(value, percentiles):
    bucket_index_for_value = get_percentile_number(value, percentiles)
    new_value = percentiles[bucket_index_for_value]
    return new_value


def values_equalization(values, percentiles, add_random=False):
    new_values = [value_equalization(value, percentiles) for value in values]
    return new_values


file = open('img.txt')
data = []
for line in file:
    numbers_in_line = [float(x) for x in line.split()]
    data.append(numbers_in_line)

flatten_image = []
for row in data:
    flatten_image += row

percentiles = get_percentile(flatten_image, 4)

new_data = []
for row in data:
    new_data.append(values_equalization(row, percentiles))


new_flatten_image = []
for row in new_data:
    new_flatten_image += row


#plt.imshow(new_data, cmap=plt.get_cmap('gray'))

plt.hist(new_flatten_image, bins=100)
plt.show()

'''
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]

for x in 2.5, 5.5, 100:
    print(get_percentile_number(x, percentiles))
'''

