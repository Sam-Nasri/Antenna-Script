import numpy as np
import math

# Reference angle method

# current_orientation = (1, 1)
# target_orientation = (-1, 1)

# theta1 = math.degrees(math.atan2(current_orientation[1], current_orientation[0]))
# theta2 = math.degrees(math.atan2(target_orientation[1], target_orientation[0]))

# angle = 180 - theta2 + theta1

# Dot product method

# a = current_orientation[0] * target_orientation[0]
# b = current_orientation[1] * target_orientation[1]
# dot_prod = a + b

# dot_prod = numpy.dot(target_orientation, current_orientation)

# mag_a = math.sqrt(current_orientation[0] * current_orientation[0] + current_orientation[1] * current_orientation[1])
# mag_b = math.sqrt(target_orientation[0] * target_orientation[0] + target_orientation[1] * target_orientation[1])

# angle = math.degrees(math.acos((dot_prod)/(mag_a * mag_b)))

# theta1 = math.degrees(math.atan2(current_orientation[1], current_orientation[0]))
# theta2 = math.degrees(math.atan2(target_orientation[1], target_orientation[0]))

# if(current_orientation[0] >= 0 & current_orientation[1] >= 0) and (target_orientation[0] >= )
#     angle = 180 - theta2 + theta1

# **************************************************************************************************

# Cross product method and 3 dimensional vectors

current_orientation = np.array([1, 1, 0])
target_orientation = np.array([-1, 1, 0])

cross = np.cross(current_orientation, target_orientation)  # Calculate the cross product
mag_current = np.linalg.norm(current_orientation)   # Magnitude of current orientation
mag_target = np.linalg.norm(target_orientation) # Magnitude of target orientation

cosine_theta = np.dot(current_orientation, target_orientation) / (mag_current * mag_target)  # Calculate the cosine of the angle between the vectors
angle_degrees = math.degrees(math.acos(cosine_theta))  # Angle value in degrees before direction

# Determine angle direction/sign by checking the sign of the component z
if cross[2] < 0:
    angle = -angle_degrees
else:
    angle = angle_degrees

print("Angle:", angle)