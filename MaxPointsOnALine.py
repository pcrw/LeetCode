# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class LinearFx:
    # y = a*x + b
    def __init__(self, aa=0, bb=0):
        self.a = aa
        self.b = bb
    def fx(self, x):
        return self.a*x + self.b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        