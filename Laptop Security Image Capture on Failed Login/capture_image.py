import cv2
import os
import datetime

# Set log file and image save directory
log_file = "C:\\Logon_Capture\\login_attempts.log"
image_dir = os.path.expanduser("~/Desktop")
os.makedirs(image_dir, exist_ok=True) 

def log_attempt(status):
    # Logs login attempts with timestamps
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {status}\n"
    
    with open(log_file, "a") as f:
        f.write(log_entry)

def capture_image():
    # Captures an image using the webcam and saves it to Desktop
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Reduce camera buffer lag
    cam.set(cv2.CAP_PROP_FPS, 30)  # Increase FPS for faster capture

    for _ in range(5):  # Skip initial laggy frames
        cam.read()

    ret, frame = cam.read()
    if ret:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(image_dir, f"wrong_attempt_{timestamp}.jpg")
        cv2.imwrite(filename, frame)

    cam.release()
    cv2.destroyAllWindows()

def handle_failed_attempt():
    # Logs failed attempt and captures an image.
    log_attempt("FAILED LOGIN ATTEMPT")
    capture_image()


# Run the program
if __name__ == "__main__":
    handle_failed_attempt() 


