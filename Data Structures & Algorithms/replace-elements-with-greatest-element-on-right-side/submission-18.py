class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        prev = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            
            maxi = max(prev, maxi)
            prev = arr[i]
            arr[i] = maxi
        arr[-1] = -1
        return arr