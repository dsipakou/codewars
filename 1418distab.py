class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = {}
        dishes = []
        for order in orders:
            if order[2] not in dishes:
                dishes.append(order[2])
            if int(order[1]) not in d:
                d[int(order[1])] = {}
            d[int(order[1])][order[2]] = d[int(order[1])].get(order[2], 0) + 1
        dishes.sort()
        output = [["Table"] + dishes]
        for i in sorted(d):
            cur_table = [str(i)]
            for idx in range(len(dishes)):
                cur_table.append(str(d[i].get(dishes[idx], 0)))
            output.append(cur_table)
        return output
                
