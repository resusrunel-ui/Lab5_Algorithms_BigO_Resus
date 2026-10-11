

# Student-Specific Configuration
LAST_NAME = "Resus"
STUDENT_ID = "TUPM-26-4019"
SEED_DIGIT = int(STUDENT_ID[-1])  # 9
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 22
NAME_LENGTH = len(LAST_NAME)  # 5
FAVORITE_ARTIST = "DEFTONES"
ARTIST_LENGTH = len(FAVORITE_ARTIST)  # 8

# 1. Generate Dataset A and Dataset B (Sorted Ascending)
department_a = sorted([(ID_SUM * i + SEED_DIGIT) for i in range(1, 6)])
department_b = sorted([(ARTIST_LENGTH * i + NAME_LENGTH) for i in range(1, 6)])

# 2. Merge Sorted Lists (Two-Pointer Technique)


def merge_sorted_lists(list_a, list_b):
    merged = []
    i = j = 0
    comparisons = 0
    while i < len(list_a) and j < len(list_b):
        comparisons += 1
        if list_a[i] <= list_b[j]:
            merged.append(list_a[i])
            i += 1
        else:
            merged.append(list_b[j])
            j += 1
    while i < len(list_a):
        merged.append(list_a[i])
        i += 1
    while j < len(list_b):
        merged.append(list_b[j])
        j += 1
    return merged, comparisons


consolidated_dataset, comp_count = merge_sorted_lists(
    department_a, department_b)

# Output Consolidated Report
print("    EXERCISE 2: ENROLLMENT CONSOLIDATION REPORT   ")
print(f"Operator: {LAST_NAME} | ID: {STUDENT_ID}")
print(f"Department A Dataset: {department_a}")
print(f"Department B Dataset: {department_b}")
print(f"Consolidated Dataset: {consolidated_dataset}")
print(
    f"Records Before: {len(department_a) + len(department_b)} | After: {len(consolidated_dataset)}")
print(f"Comparison Count During Consolidation: {comp_count}")
print("==================================================")
