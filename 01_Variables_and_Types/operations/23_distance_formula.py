# -------------------------------------------------
# File Name: 23_distance_formula.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Euclidean (2D/3D), Manhattan, and Chebyshev distance functions.
# -------------------------------------------------

import math


def calculate_distance_2d(x1, y1, x2, y2):
    """Calculate distance between two points in 2D"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def calculate_distance_3d(x1, y1, z1, x2, y2, z2):
    """Calculate distance between two points in 3D"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def calculate_manhattan_distance(x1, y1, x2, y2):
    """Calculate Manhattan distance (taxicab distance)"""
    return abs(x2 - x1) + abs(y2 - y1)


def calculate_chebyshev_distance(x1, y1, x2, y2):
    """Calculate Chebyshev distance (chessboard distance)"""
    return max(abs(x2 - x1), abs(y2 - y1))


# Examples
print("Distance Formula Calculations:")
print("=" * 30)

# 2D Distance
print("2D Distance:")
point1 = (0, 0)
point2 = (3, 4)
distance_2d = calculate_distance_2d(*point1, *point2)
print(f"Distance between {point1} and {point2}: {distance_2d}")
print("This is the classic Pythagorean theorem example")

# More 2D examples
points = [
    ((0, 0), (1, 1)),
    ((2, 3), (5, 7)),
    ((-1, -1), (2, 3)),
    ((10, 20), (13, 24))
]

print("\nMore 2D examples:")
for p1, p2 in points:
    dist = calculate_distance_2d(*p1, *p2)
    print("10s")

# 3D Distance
print("\n3D Distance:")
point3d_1 = (0, 0, 0)
point3d_2 = (1, 1, 1)
distance_3d = calculate_distance_3d(*point3d_1, *point3d_2)
print(f"Distance between {point3d_1} and {point3d_2}: {distance_3d:.4f}")

point3d_3 = (2, 3, 4)
point3d_4 = (5, 6, 7)
distance_3d_2 = calculate_distance_3d(*point3d_3, *point3d_4)
print(f"Distance between {point3d_3} and {point3d_4}: {distance_3d_2:.4f}")

# Manhattan Distance
print("\nManhattan Distance (Taxicab Distance):")
manhattan_dist = calculate_manhattan_distance(0, 0, 3, 4)
print(f"Manhattan distance between (0,0) and (3,4): {manhattan_dist}")
print("Formula: |3-0| + |4-0| = 7")

# Chebyshev Distance
print("\nChebyshev Distance (Chessboard Distance):")
chebyshev_dist = calculate_chebyshev_distance(0, 0, 3, 4)
print(f"Chebyshev distance between (0,0) and (3,4): {chebyshev_dist}")
print("Formula: max(|3-0|, |4-0|) = 4")

# Distance from origin
print("\nDistance from Origin:")
points_from_origin = [(3, 4), (5, 12), (8, 15), (1, 1)]
for x, y in points_from_origin:
    dist = calculate_distance_2d(0, 0, x, y)
    print("10s")

# Midpoint calculation


def calculate_midpoint(x1, y1, x2, y2):
    """Calculate midpoint between two points"""
    return ((x1 + x2) / 2, (y1 + y2) / 2)


print("\nMidpoint Calculations:")
p1 = (2, 4)
p2 = (6, 8)
midpoint = calculate_midpoint(*p1, *p2)
print(f"Midpoint between {p1} and {p2}: {midpoint}")

# Verify midpoint
dist_to_mid1 = calculate_distance_2d(*p1, *midpoint)
dist_to_mid2 = calculate_distance_2d(*p2, *midpoint)
print(f"Distance from {p1} to midpoint: {dist_to_mid1}")
print(f"Distance from {p2} to midpoint: {dist_to_mid2}")

# Circle properties
print("\nCircle Properties:")
center = (0, 0)
radius = 5
point_on_circle = (3, 4)
distance_from_center = calculate_distance_2d(*center, *point_on_circle)
print(
    f"Point {point_on_circle} is on circle with center {center} and radius {radius}")
print(f"Distance from center: {distance_from_center}")
print(f"Is on circle? {abs(distance_from_center - radius) < 0.001}")

# Triangle sides
print("\nTriangle Sides:")
triangle_points = [(0, 0), (4, 0), (2, 3)]
side1 = calculate_distance_2d(*triangle_points[0], *triangle_points[1])
side2 = calculate_distance_2d(*triangle_points[1], *triangle_points[2])
side3 = calculate_distance_2d(*triangle_points[2], *triangle_points[0])
print(f"Triangle points: {triangle_points}")
print(f"Side lengths: {side1:.1f}, {side2:.1f}, {side3:.1f}")

# Verify Pythagorean theorem
print(
    f"\nPythagorean verification: {side3**2:.1f} ≈ {side1**2 + side2**2:.1f}")
