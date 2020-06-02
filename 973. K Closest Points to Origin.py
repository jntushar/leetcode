"""

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

"""

"""---SOLUTION 1---"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]


"""---SOLUTION 2---"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        distance = []
        res = []

        for i in points:
            distance.append((i[0] ** 2) + (i[1] ** 2))

        for _ in range(K):
            index = distance.index(min(distance))
            res.append(points[index])
            distance[index] = math.inf

        return res