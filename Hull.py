
#  File: Hull.py

#  Description: Finding the smallest convex polygon that will enclose a given set of points

#  Student Name: Abdulateef Oyegbefun

#  Student UT EID: Afo296

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 2/20/2023

#  Date Last Modified:2/20/2023

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    matrix =  [ 
                [1,p.x,p.y],
                [1,q.x,q.y],
                [1,r.x,r.y]
                ]
    value = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])+\
            matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+\
            matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])

    #print(matrix)
    if value>0:
        print('left of liine')
    elif value<0:
        print('right of line')
    else:
        print('on line')
    return None

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    upper_hull=[]
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    for i  in range(3,len(sorted_points)):
        upper_hull.append(sorted_points[i])
        #while len(upper_hull)>=3 and 
    return None

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  return

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list, key= lambda p: p.x)

  
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  

  # get the convex hull

  # run your test cases

  # print your results to standard output

  # print the convex hull

  # get the area of the convex hull

  # print the area of the convex hull


  #print(det(points_list[0], points_list[1], points_list[2]))
  #print(det(points_list[3], points_list[4], points_list[5]))
  #print(det(points_list[6], points_list[7], points_list[8]))
  #print(det(points_list[9], points_list[10], points_list[11]))

if __name__ == "__main__":
  main()