# Write a function that takes a list and performs selection sort and returns a sorted list
import numpy as np

# O(n^2) sorting algorithm as we need two nested for loops over the whole length of the list
def selection_sort(input_list):
    # Copy the list to not change the input
    sorted_list = list(input_list)

    for i in range(len(sorted_list)):
        smallest_index = i
        # Find the current smallest after i
        for j in range(i, len(sorted_list)):
            if sorted_list[j] < sorted_list[smallest_index]:
                smallest_index = j

        # Swap the i-th smallest element with the element at i
        sorted_list[smallest_index], sorted_list[i] = sorted_list[i], sorted_list[smallest_index]

    return sorted_list

def pythons_sort(input_list):
    sorted_list = list(input_list)
    sorted_list.sort()
    return sorted_list

random_list = np.random.randint(-100, 100 + 1, size=2)

selection_sorted_list = selection_sort(random_list)
python_sorted_list = pythons_sort(random_list)

print(f"The random list of numbers generated is {random_list}")
print(f"Our selection sort returned {selection_sorted_list} and python's sort returned {python_sorted_list}")