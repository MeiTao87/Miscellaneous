import cv2
import matplotlib.pyplot as plt

img = cv2.imread('RGB.jpg',-1)
cv2.imshow('cv2_reading',img)

#chaning the color order after cv2.imshow()
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
#plt.xticks([]), plt.yticks([])
plt.title('matplotlib')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
