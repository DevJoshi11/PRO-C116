import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
        "Sun",
        (20,300),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Mercury",
        (100,240),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Venus",
        (180,260),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Earth",
        (290,270),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Moon",
        (315,160),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Mars",
        (380,250),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )


cv2.putText(img,
        "Jupiter",
        (575,370),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Saturn",
        (760,300),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Uranus",
        (965,300),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.putText(img,
        "Neptune",
        (1110,300),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255,255,255)
        )

cv2.imwrite("Solar_planets.jpg",img)

cv2.imshow("Display Image", img)

cv2.waitKey(0)