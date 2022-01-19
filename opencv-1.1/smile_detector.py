import cv2

#face_classifier

face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #haar cascade object detection
smile_detector=cv2.CascadeClassifier("haarcascade_smile.xml")
#video capture using real-time webcam
cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("smile_save.avi",fourcc,20.0,(640,480))
while (True):
    ret,frame=cap.read()
    
    if ret ==True:
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        faces=face_detector.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=7) #'faces storing array of faces location as points means if 1 face the arr of face 1 location if 2 face then arr of 2faces locations and so on'         
        #print(faces)
        
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(37,179,89),3) #it will be coloured frame no the gray one...            
            
            converted_face=frame[y:y+h,x:x+w]  #here we are taking the dimensions of frame of face detector frame by frame by numpy 2d slicing which also forms a image of only the face restricting other back grounds anamolies ....           
            
            sub_gray=cv2.cvtColor(converted_face,cv2.COLOR_BGR2GRAY)
            
            smiles=smile_detector.detectMultiScale(sub_gray,scaleFactor=1.6,minNeighbors=20)
            
            """ for x,y,w,h in smiles:
              cv2.rectangle(converted_face,(x,y),(x+w,y+h),(37,52,179),4) """

            if(len(smiles))>0:
              cv2.putText(frame,"smiling bro",(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(0,0,0))

        out.write(frame)  # to save video
        cv2.imshow("smile_detector",frame)
       
        k=cv2.waitKey(1) & 0xFF
        if k==ord('s'):
            break
    else:
        break 
cap.release()
out.release()
cv2.destroyAllWindows()