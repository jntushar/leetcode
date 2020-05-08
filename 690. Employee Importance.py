"""

You are given a data structure of employee information, which includes the employee's unique id, his importance value and
his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]],
and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1,
the relationship is not direct.

Now given the employee information of a company, and an employee id,
you need to return the total importance value of this employee and all his subordinates.

"""

"""---SOLUTION---"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        hmap = {}
        for i in range(len(employees)):
            hmap[employees[i].id] = employees[i]

        def importance(employee_id):

            for sub in hmap[employee_id].subordinates:
                hmap[employee_id].importance += importance(sub)

            return hmap[employee_id].importance

        return importance(id)