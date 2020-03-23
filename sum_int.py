def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    merged_intervals = []
    start = intervals[0][0]
    end = intervals[0][1]
    intervals = intervals[1:]
    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            merged_intervals.append((start, end))
            start = interval[0]
            end = interval[1]
    merged_intervals.append((start, end))
    output = 0
    for interval in merged_intervals:
        output += interval[1] - interval[0]
    return output
