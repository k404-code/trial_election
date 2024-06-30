# qr_scanner.py

import cv2
from pyzbar.pyzbar import decode
import time

def main():
    get_studentid()
    
def get_studentid():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    qr_code_data = None
    qr_detected = False

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Decode the QR codes in the frame
        qr_codes = decode(frame)

        if qr_codes and not qr_detected:
            for qr_code in qr_codes:
                # Extract QR code data
                qr_code_data = qr_code.data.decode('utf-8')
                
                # Draw a rectangle around the QR code in the frame
                points = qr_code.polygon
                if len(points) == 4:
                    pts = [tuple(point) for point in points]
                    pts = pts + [pts[0]]
                    for i in range(len(pts) - 1):
                        cv2.line(frame, pts[i], pts[i+1], (0, 255, 0), 2)

                # Display the message near the QR code
                x, y, w, h = qr_code.rect
                cv2.putText(frame, "Voter verified. You can vote.", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Display the frame with the detected QR code and message
                cv2.imshow('QR Code Scanner', frame)

                # Indicate that QR code has been detected
                qr_detected = True
                break

        else:
            # Display the frame without any detected QR code
            cv2.imshow('QR Code Scanner', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # If QR code detected, wait for 5 seconds before breaking the loop
        if qr_detected:
            time.sleep(5)
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

    print(qr_code_data)
    return qr_code_data

if __name__ == '__main__':
    main()
