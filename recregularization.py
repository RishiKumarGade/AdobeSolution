from PIL import Image
import numpy as np

from PIL import Image, ImageDraw
image_path = "solution/rec.png"
image = Image.open(image_path).convert("RGB")

image_array = np.array(image)

black = [0, 0, 0]

black_pixels = np.argwhere(np.all(image_array == black, axis=-1))

lowest_x = np.min(black_pixels[:, 1]) 
lowest_y = np.min(black_pixels[:, 0]) 
highest_x = np.max(black_pixels[:, 1])
highest_y = np.max(black_pixels[:, 0])

# Print the results
print(f"Lowest x: {lowest_x}")
print(f"Lowest y: {lowest_y}")
print(f"Highest x: {highest_x}")
print(f"Highest y: {highest_y}")

coordinates = [(lowest_x, lowest_y), (highest_x, lowest_y), (highest_x, highest_y),(lowest_x, highest_y)]


import matplotlib.pyplot as plt
import matplotlib.patches as patches

x_coords, y_coords = zip(*coordinates)
x_min, x_max = min(x_coords), max(x_coords)
y_min, y_max = min(y_coords), max(y_coords)

width = x_max - x_min
height = y_max - y_min

fig, ax = plt.subplots()

rectangle = patches.Rectangle((x_min, y_min), width, height, linewidth=2, edgecolor='black', facecolor='none')

ax.add_patch(rectangle)

ax.set_xlim(x_min - 10, x_max + 10)
ax.set_ylim(y_min - 10, y_max + 10)  
ax.set_aspect('equal')
ax.axis('off')

plt.gca().invert_yaxis()  
plt.show()
