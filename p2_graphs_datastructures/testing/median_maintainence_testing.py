import math
import statistics
from p2_graphs_datastructures.testing.median_maintainence_tester import alg
from p2_graphs_datastructures.algorithms.median_maintainence import median_maintainence, load_data


def median(data):
    data = sorted(data)
    n = len(data)

    if n % 2 == 1:
        return data[n//2]
    else:
        return data[n//2 - 1]


def brute_medians(nums):

    medians = []
    processed = []
    for num in nums:

        processed.append(num)
        med = median(processed)
        # med = statistics.median_low(processed)
        medians.append(med)

    return medians


def get_solution(medians):
    median_sum = 0
    for num in medians:
        median_sum += num
    return median_sum % 10000


#  figured out I was confused about taking low medians. Need to make sure I'm taking medians correctly in algo.
# ISSUE I THINK IS THAT ONLY THE MINHEAP SHOULD EVER HAVE A GREATER AMOUNT OF ELEMENTS. MAXHEAP SHOULD NEVER BE > MINHEAP
# --> fixed
# There is an issue with finding min and max elements of the heaps. The heaps aren't always being maintained properly
# No, issue was that I was removing elements from the middle of the heap without maintaining the heap property


# filename = 'p2_graphs_datastructures\\testing\\median_maintainence_test_cases\\input_random_24_320.txt'  # pass
# filename = 'p2_graphs_datastructures\\testing\\median_maintainence_test_cases\\input_random_13_80.txt'  # pass
# filename = 'p2_graphs_datastructures\\testing\\median_maintainence_test_cases\\input_random_25_640.txt'  # fail
filename = 'p2_graphs_datastructures\\testing\\median_maintainence_test_cases\\input_random_21_320.txt'  # fail


nums = load_data(filename)

algo_medians = median_maintainence(nums)
# algo_res = alg(filename)
algo_res = get_solution(algo_medians)
print('algo result:', algo_res)


non_algo_medians = brute_medians(nums)
non_algo_res = get_solution(non_algo_medians)
print('brute force result:', non_algo_res)


# print(len(algo_medians) == len(non_algo_medians))
for i in range(len(algo_medians)):
    if not algo_medians[i] == non_algo_medians[i]:
        print('mismatch at index:', i)
        print('number of elements processed:', len(nums[:i+1]))
        # print('26th element:', sorted(nums[:i+1])[25])
        print('algo median:', algo_medians[i])
        print('non_algo median:', non_algo_medians[i])
        print('standard library low median:',
              statistics.median_low(nums[:i+1]))
        print('numbers processed up to i:')
        print(sorted(nums[:i]))

        break
