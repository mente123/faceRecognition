import cv2
face_cascade = cv2.CascadeClassifier('.xml file to be inserted which contain face datas')

def detect():
    cap = cv2.VideoCapture(0)
    
    while True:
        _,img = cap.read()
        
        gray = cv2.cvtColor(img, cv2.Color_BGR2GRAY)
        face = face_cascade.detextMultiScale(gray, 1.1, 5)  # parameters ( scale, scale factor, faces to be detectes)
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2) #create a rectangle around a face with tickness, color
        cv2.imshow("Face Detect", img)

        if cv2.waitkey(1) == 27:
            break
    cap.release()
    
detect()