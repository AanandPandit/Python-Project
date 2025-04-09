
## Windows Login Attempt Logger & Intruder Capture
This project logs failed login attempts on a Windows 11 machine. If an incorrect PIN/password is entered, the script captures an image using the webcam and saves it to the Desktop.

## Features

✅ Logs both failed login attempts in a log file.

✅ Captures an intruder's image on failed login attempts.

✅ Saves logs in 
```bash
C:\Logon_Capture\login_attempts.log.
```

✅ Works with Windows Task Scheduler to automate execution on Event ID 4625.


## Installation

1. Install Python 3.x (if not installed already). Download from python.org.

2. Install OpenCV for image capture:

```bash
pip install opencv-python
```
3. Clone this repository:

```bash
git clone https://github.com/AanandPandit/Python-Project cd login-attempt-logger
```
4. Move the script to C:\Logon_Capture\:
```bash
mkdir C:\Logon_Capture
copy capture_image.py C:\Logon_Capture\
```

## Setup Windows Task Scheduler

1. Open Task Scheduler (Win + R, type taskschd.msc, press Enter).

2. Click Create Task (right panel).

3. In the General tab:

        Name: Login_Attempt_Logger
        Check Run with highest privileges.

4. In the Triggers tab:

        Click New → Select On an event.
        Log: Security, Source: Microsoft Windows security auditing, Event ID: 4625.

5. In the Actions tab:

        Click New → Select Start a program.
        Program/script: python
        Add arguments: C:\Logon_Capture\capture_image.py

6. Click OK, enter your admin password if prompted.

