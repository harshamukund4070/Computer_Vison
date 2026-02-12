import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# -------------------------------------------------
# 1️⃣ Check current working directory
# -------------------------------------------------
print("Current Working Directory:")
print(os.getcwd())

print("\nFiles inside this folder:")
print(os.listdir())

# -------------------------------------------------
# 2️⃣ Read Image (Use exact file name)
# -------------------------------------------------
image = cv2.imread("Input_Activity-1.png")   # <-- Keep your original name

# -------------------------------------------------
# 3️⃣ Check if image loaded
# -------------------------------------------------
if image is None:
    print("\n❌ ERROR: Image not found!")
    print("Make sure image is inside same folder as this Python file.")
    exit()
else:
    print("\n✅ Image loaded successfully!")

# -------------------------------------------------
# 4️⃣ Convert to Grayscale
# -------------------------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -------------------------------------------------
# 5️⃣ Apply Threshold Segmentation
# -------------------------------------------------
ret, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# -------------------------------------------------
# 6️⃣ Save Output Image
# -------------------------------------------------
cv2.imwrite("Output_Activity-1.png", segmented)
print("✅ Output image saved as Output_Activity-1.png")

# -------------------------------------------------
# 7️⃣ Display Images
# -------------------------------------------------
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Segmented Image")
plt.imshow(segmented, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()
