class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for item in operations:
            try:
                n = int(item)
                record.append(n)
            except:
                if item == "+":
                    orig = record.pop()
                    new = orig + record[-1]
                    record.append(orig)
                    record.append(new)
                if item == "D":
                    new = record[-1] * 2
                    record.append(new)
                if item == "C":
                    record.pop()
        return sum(record)