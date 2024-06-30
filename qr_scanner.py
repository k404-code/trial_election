import cv2
from pyzbar.pyzbar import decode
import time
import datetime

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
                
                # Validate the student QR code
                if is_valid_student_qr(qr_code_data):
                    # Draw a green rectangle around the QR code in the frame
                    points = qr_code.polygon
                    if len(points) == 4:
                        pts = [tuple(point) for point in points]
                        pts = pts + [pts[0]]
                        for i in range(len(pts) - 1):
                            cv2.line(frame, pts[i], pts[i+1], (0, 255, 0), 2)

                    # Display the message near the QR code
                    x, y, w, h = qr_code.rect
                    cv2.putText(frame, "Voter verified. You can vote.", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    # Draw a red rectangle around the QR code in the frame (invalid QR code)
                    points = qr_code.polygon
                    if len(points) == 4:
                        pts = [tuple(point) for point in points]
                        pts = pts + [pts[0]]
                        for i in range(len(pts) - 1):
                            cv2.line(frame, pts[i], pts[i+1], (0, 0, 255), 2)

                    # Display the message near the QR code
                    x, y, w, h = qr_code.rect
                    cv2.putText(frame, "Invalid QR code. Please try again.", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

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

def is_valid_student_qr(qr_code_data):
    current_year = datetime.datetime.now().year % 100  # Get the last two digits of the current year
    if len(qr_code_data) == 7 and qr_code_data[:2].isdigit() and qr_code_data[2:4].isalpha() and qr_code_data[4:].isdigit():
        year = int(qr_code_data[:2])  # Extract the two-digit year

        if current_year - year in range(1, 3):
            return True
    return False

if __name__ == '__main__':
    main()
