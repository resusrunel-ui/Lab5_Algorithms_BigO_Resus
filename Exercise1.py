
LAST_NAME = "Resus"
STUDENT_ID = "TUPM-26-4019"
SEED_DIGIT = int(STUDENT_ID[-1])  # 9[cite: 16]
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 22
FAVORITE_ARTIST = "DEFTONES"
ARTIST_SUM = sum(ord(c) - ord('A') + 1 for c in FAVORITE_ARTIST.upper())  # 88

# 1. Generate original sorted dataset and rotate it using SEED_DIGIT
original_dataset = list(range(10, 10 + (ID_SUM * 2), 4))
rotation_point = SEED_DIGIT % len(original_dataset)
rotated_dataset = original_dataset[rotation_point:] + \
    original_dataset[:rotation_point]

# Target generation using ID_SUM and ARTIST_SUM
target = rotated_dataset[(ID_SUM + SEED_DIGIT) % len(rotated_dataset)]

# 2. Rotated Binary Search Algorithm


def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1, comparisons

# 3. Linear Search Comparison


def linear_search_count(arr, target):
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return i, comparisons
    return -1, comparisons


index_rotated, comp_rotated = search_rotated(rotated_dataset, target)
index_linear, comp_linear = linear_search_count(rotated_dataset, target)

# Output Results
print("     EXERCISE 1: EMERGENCY DISPATCH REPORT        ")
print(f"Original Dataset: {original_dataset}")
print(f"Rotated Dataset (Index {rotation_point}): {rotated_dataset}")
print(f"Target Incident Value: {target}")
print(
    f"Rotated Binary Search -> Index: {index_rotated} | Comparisons: {comp_rotated}")
print(
    f"Linear Search         -> Index: {index_linear} | Comparisons: {comp_linear}")
print("==================================================\n")
