import cv2
import requests
import time

# Function to send notification to Telegram bot
def send_notification():
    bot_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    message = 'Human face detected!'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Notification sent successfully!")
        time.sleep(5)  # Delay of 5 seconds before sending the next notification
    else:
        print("Failed to send notification.")

# Initialize the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect human faces in an image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Main function to capture video frames and process them
def main():
    cap = cv2.VideoCapture(0)  # Open the default camera (change the argument if using a different camera)
    
    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            print("Failed to capture frame.")
            break
        
        # Detect faces in the frame
        faces = detect_faces(frame)
        
        # If faces are detected, send a notification
        if len(faces) > 0:
            send_notification()
        
        # Display the frame
        cv2.imshow('Frame', frame)
        
        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
