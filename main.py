import cv2
from deepface import DeepFace
import webbrowser

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

def music_recomender(text):
    search_address=f'https://open.spotify.com/search/{(text)}%20songs/playlists'
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(search_address)

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam!")

while True:
    ret,frame = cap.read()
    result = DeepFace.analyze(frame, actions = ['emotion'])
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(frame, result['dominant_emotion'], (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
    mood=result['dominant_emotion']
    print(mood)
        
    cv2.imshow('Realtime . . .', frame)
    
    if cv2.waitKey(2) & 0xFF == ord('q') or mood=='happy' or mood=='sad' or mood=='angry' or mood=='surprise':
        music_recomender(mood)
        break


cap.release()
cv2.destroyAllWindows()
        
        