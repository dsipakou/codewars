class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        output = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                output += 1
        return output
