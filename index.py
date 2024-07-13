import math

points = [(2, 3), (5, 7), (1, 1), (4, 2), (6, 9)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

print("Tüm mesafeler:", distances)

min_distance = min(distances)
print("Minimum mesafe:", min_distance)