# Тут мы рассматриваем пример увеличения фотографии или обьекта изображения.
import cv2

img = cv2.imread('Open_CV/kartinki-vyzdoravlivaj-1.jpg')
print(img.shape)

img = cv2.resize(img, (1000, 1000))
print(img.shape)

cv2.imshow('Result', img)
cv2.waitKey(0)