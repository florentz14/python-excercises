# -------------------------------------------------
# File Name: 02_activity_selection.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Activity Selection (Interval Scheduling). Maximum non-overlapping activities. Greedy: sort by finish time, pick earliest-finishing compatible. O(n log n).
# -------------------------------------------------

def activity_selection(starts, ends):
    """
    Returns indices of a maximum-size set of non-overlapping activities.
    Inputs: starts[i], ends[i] = start and end time of activity i.
    """
    n = len(starts)
    # Zip (start, end, index) and sort by end time (greedy key)
    activities = list(zip(starts, ends, range(n)))
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end = 0

    for start, end, idx in activities:
        if start >= last_end:
            # No overlap with last selected; add this activity
            selected.append(idx)
            last_end = end

    return selected


if __name__ == "__main__":
    print("=== Greedy Algorithms: Activity Selection ===\n")

    starts = [1, 3, 0, 5, 8, 5]
    ends = [2, 4, 6, 7, 9, 9]

    print("Activities:")
    for i, (s, e) in enumerate(zip(starts, ends)):
        print(f"  Activity {i}: [{s}, {e}]")

    selected = activity_selection(starts, ends)
    print(f"\nMaximum number of activities: {len(selected)}")
    print(f"Selected activities: {selected}")
    for idx in selected:
        print(f"  Activity {idx}: [{starts[idx]}, {ends[idx]}]")
