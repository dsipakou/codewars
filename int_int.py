class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i_a = 0
        i_b = 0
        output = []
        while i_a < len(A) and i_b < len(B):
            a_s = A[i_a][0]
            a_e = A[i_a][1]
            b_s = B[i_b][0]
            b_e = B[i_b][1]
            if a_s > b_e:
                i_b += 1
            elif b_s > a_e:
                i_a += 1
            else:
                output.append([max(a_s, b_s), min(a_e, b_e)])
                if a_e > b_e:
                    i_b += 1
                else:
                    i_a += 1
        return output
