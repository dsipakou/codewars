class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        output = 0
        if len(timeSeries) == 1:
            return duration
        current = timeSeries[0]
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] < duration:
                output += timeSeries[i] - timeSeries[i - 1]
            else:
                output += duration
        return output + duration
