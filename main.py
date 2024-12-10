import cv2

def main():
    # Start capturing from the webcam (0 is usually the default webcam)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Show the frame in a window
        cv2.imshow("Live Camera Feed", frame)

        # Press 'q' to quit the live feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
