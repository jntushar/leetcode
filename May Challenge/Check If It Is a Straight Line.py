"""

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

"""

"""---SOLUTION---"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Calculating slope of a line
        # m = (y2 - y1)/(x2 - x1)
        try:
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        except:
            return False

        # Calculating Intercept
        # using y = mx+c
        c = coordinates[0][1] - m * coordinates[0][0]

        for i in range(len(coordinates)):
            if coordinates[i][1] != m * coordinates[i][0] + c:
                return False
        return True
