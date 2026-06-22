class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentctr = Counter(students)
        numstudents = len(students)
        
        for i in range(len(sandwiches)):
            if studentctr[sandwiches[i]] > 0:
                studentctr[sandwiches[i]] -= 1
                numstudents -= 1
            else:
                break
        
        return numstudents
