
import time

# Student-Specific Configuration
LAST_NAME = "Resus"
STUDENT_ID = "TUPM-26-4019"
SEED_DIGIT = int(STUDENT_ID[-1])  # 9
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 22
NAME_LENGTH = len(LAST_NAME)  # 5
FAVORITE_ARTIST = "DEFTONES"
ARTIST_LENGTH = len(FAVORITE_ARTIST)  # 8

# Generate base orders using student inputs
base_orders = [(ID_SUM * 5 + i * 13) % 100 for i in range(12)]

# Three input conditions
sorted_orders = sorted(base_orders)
reverse_orders = sorted(base_orders, reverse=True)
random_orders = base_orders.copy()

# Sorting Algorithm Definitions


def bubble_sort(data):
    a, comps, swaps = data.copy(), 0, 0
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comps, swaps


def selection_sort(data):
    a, comps, swaps = data.copy(), 0, 0
    for i in range(len(a) - 1):
        min_idx = i
        for j in range(i + 1, len(a)):
            comps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comps, swaps


def insertion_sort(data):
    a, comps, shifts = data.copy(), 0, 0
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return a, comps, shifts


# Execution & Performance Comparison Report
print("     EXERCISE 3: E-COMMERCE SORTING COMPARISON    ")
print(f"Operator: {LAST_NAME} | ID: {STUDENT_ID}")
print(f"Original Base Orders: {base_orders}")

for condition_name, dataset in [("Sorted", sorted_orders), ("Reverse-Ordered", reverse_orders), ("Random", random_orders)]:
    print(f"\n--- Input Condition: {condition_name} ---")
    for name, func in [("Bubble Sort", bubble_sort), ("Selection Sort", selection_sort), ("Insertion Sort", insertion_sort)]:
        start = time.perf_counter()
        res, comps, movements = func(dataset)
        elapsed = time.perf_counter() - start
        print(
            f"{name:<15} | Comparisons: {comps:<5} | Movements: {movements:<5} | Time: {elapsed:.8f}s")
print("==================================================")
