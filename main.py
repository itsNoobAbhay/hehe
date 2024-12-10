import cv2
import numpy as np
import streamlit as st

# Set up the Streamlit page
st.title("Live Camera Feed with OpenCV")

# Open the webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    st.error("Could not open webcam.")
else:
    st.info("Press 'q' to quit.")

    # Loop to continuously get frames from the webcam
    while True:
        ret, frame = cap.read()
        
        if not ret:
            st.error("Failed to capture image.")
            break
        
        # Optional: Draw a rectangle or any other shape on the frame
        # Rectangle coordinates (x, y, width, height)
        start_point = (100, 100)
        end_point = (300, 300)
        color = (0, 255, 0)  # Green rectangle
        thickness = 2
        cv2.rectangle(frame, start_point, end_point, color, thickness)

        # Convert the frame to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the image in Streamlit
        st.image(frame_rgb, channels="RGB", use_column_width=True)

        # Close the camera feed if 'q' is pressed (optional)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release the camera when done
    cap.release()
