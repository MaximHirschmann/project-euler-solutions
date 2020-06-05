from numpy.linalg import solve
from numpy import array

with open('storage//102_triangles.txt','r') as f:
    lines = [eval(line) for line in f.readlines()]
    points = [((line[0], line[1]), (line[2], line[3]), (line[4], line[5])) for line in lines]

count = 0
for a, b, c in points:
    # see http://geomalgorithms.com/a06-_intersect-2.html "Intersection of a Ray/Segment with a Triangle"
    # we use the parametric plane equation: P(s,t) = P0 + s*(P1-P0) + t*(P2-P0) and solve for s and t where P(s,t) is the origin (0, 0, 0)
    left = array([[b[0]-a[0], c[0]-a[0]], [b[1]-a[1], c[1]-a[1]]])
    right = array([-a[0], -a[1]])
    s, t = solve(left, right)

    # if these inequalities are true the triangle contains the origin
    if 0 <= s <= 1 and 0 <= t <= 1 and 0 <= s+t <= 1:
        count += 1

print(count)