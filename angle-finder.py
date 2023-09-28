import numpy as np
import math

current_orientation = np.array([-1, -1, 0])
target_orientation = np.array([-1, 1, 0])
plane_normal = np.array([0, 0, 1])  # Constant

cross = np.cross(current_orientation, target_orientation)  # Calculate the cross product
dot = np.dot(current_orientation, target_orientation)

direction_dot = np.dot(cross, plane_normal)

angle = math.degrees(math.atan2(direction_dot, dot))

print("Angle:", angle)