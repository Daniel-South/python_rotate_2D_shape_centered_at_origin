"""
FILE:   rotate_2D_shape_centered_at_origin.py
TITLE:  Rotate A Shape Centered At The Origin
AUTHOR: Daniel R. South
DATE:   11 Jan 2025

DESCRIPTION:

Use matplotlib to display a 2D shape centered at the origin (0,0)
Use matrix multiplication to rotate the shape around the origin
"""


import numpy as np
import matplotlib.pyplot as plt


# Create a 2x2 square with its center at the origin (0, 0)
# The shape is defined by a list of (x,y) points to set the corners
# (-1,-1), (1,-1), (1,1), (-1,1), (-1,-1)
x_values = np.array([-1,  1, 1, -1, -1])
y_values = np.array([-1, -1, 1,  1, -1])

print(x_values)
print(y_values)

fig1, axs1 = plt.subplots(1, 1, figsize=(3,3))
axs1.set_title("Shape with center at the origin (0,0)")
axs1.set_aspect('equal')

# Plot the original unrotated shape
axs1.plot(x_values, y_values, color='blue')
plt.show()


fig2, axs2 = plt.subplots(1, 1, figsize=(5,5))
axs2.set_aspect('equal')

def add_shape_at_degrees(in_angle, in_color, in_clockwise=True):
    coef1 = 1
    coef2 = -1
    if in_clockwise == False:
        coef1 = -1
        coef2 = 1
        
    theta = np.radians(in_angle)
    print("radians =", round(theta,4))
    
    rotation_matrix = np.array([
        [np.sin(theta), coef1 * np.cos(theta)],
        [np.cos(theta), coef2 * np.sin(theta)]])

    
    # Rotate the shape using vector multiplication (dot products of the vectors)

    xy_rotated = np.dot(rotation_matrix, np.vstack([x_values, y_values]))

    x_vals_rotated = xy_rotated[0, :]
    y_vals_rotated = xy_rotated[1, :]
    print("Rotated x values:", list(map(lambda a: round(a,4), x_vals_rotated)))
    print("Rotated y values:", list(map(lambda a: round(a,4), y_vals_rotated)))

    axs2.plot(x_vals_rotated, y_vals_rotated, color=in_color)


# Add the unrotated shape to the second axis
axs2.plot(x_values, y_values, color='black')

# Add the rotated shapes
add_shape_at_degrees(30, 'red')
add_shape_at_degrees(60, 'green')
add_shape_at_degrees(45, 'blue', False)
axs2.set_title("Rotate +30, +60, and -45 degrees")

# Display the combined graph
plt.show()
