# Security-System-with-Object-Detection-and-Notification
# Human Face Detection and Notification System

## Introduction
This project implements a human face detection system using Python's OpenCV library. When a human face is detected by a live camera feed, the system sends a notification to a Telegram bot. It serves as an IoT-based project designed to demonstrate integration between image processing and real-time notifications.
---

## Components Required
- A computer with Python installed (for development and running the code)
- USB or built-in webcam
- Telegram bot account for sending notifications

---

## Setting Up the Telegram Bot
1. Create a new Telegram bot using BotFather.
2. Save the bot token provided by BotFather.
3. Obtain the `chat_id` using Telegram API by sending a message to the bot and retrieving updates.

---

## Image Processing
- The Haar Cascade Classifier is used for detecting faces in a live video feed.
- Real-time detection is implemented using OpenCV's `cv2.CascadeClassifier`.

---

## Sending Notifications
- A notification is sent to the Telegram bot when a face is detected.
- The system ensures a delay of 5 seconds before sending another notification.

---

## Integration and Main Script
The project integrates image processing and Telegram bot notifications into a unified system.


## Conclusion
The project demonstrates the effective integration of real-time image processing and IoT notification systems. It highlights the potential of combining OpenCV and Telegram for practical applications.

---

## Libraries Used
- OpenCV
- Requests

---

## How to Run
1. Install the required libraries:
   ```
   pip install opencv-python requests
   ```
2. Replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` in the code with your Telegram bot details.
3. Run the `image_processing.py` script.
4. Ensure the webcam is connected and functioning.
5. Monitor the Telegram bot for notifications.
