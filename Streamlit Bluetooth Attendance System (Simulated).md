# Streamlit Bluetooth Attendance System (Simulated)

This is a web-based attendance management system built with Streamlit, designed for teachers to take attendance. Due to the limitations of direct Bluetooth access in web browsers, the Bluetooth device detection is **simulated**.

## Features

*   **Web-based Interface:** Accessible via a web browser.
*   **User Authentication:** Separate login interfaces for teachers and students.
*   **Teacher Interface:**
    *   Select from predefined classes (CSE, CSE-AIML, CSE-DS).
    *   Initiate a simulated Bluetooth scan to detect student presence.
    *   Attendance is marked based on students who have "given attendance" (simulated check-in).
    *   Displays attendance results after a random delay (10-30 seconds).
*   **Student Interface:**
    *   Login with Name, Roll Number, and Department.
    *   Button to "Give Attendance" (simulated check-in).
    *   Student data is deleted upon logout.
*   **Data Persistence:** Student, teacher, and attendance data are stored locally using JSON files, managed via Streamlit's session state for the current session.

## Prerequisites

To run this application, you will need:

*   Python 3.x installed on your system.
*   `pip` (Python package installer).

## Installation and Setup

Follow these steps to set up and run the application:

### 1. Install Python

If you don't have Python installed, download the latest version of Python 3.x from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation, it's recommended to **check the box that says "Add Python to PATH"**.

### 2. Install Required Libraries

Open your Command Prompt (Windows) or Terminal (macOS/Linux) and run the following command to install Streamlit:

```bash
pip install streamlit
```

### 3. Download the Application Files

Download the `app.py`, `students.json`, `teachers.json`, and `attendance.json` files to a folder on your computer. (These files will be provided to you upon completion of the project.)

### 4. Run the Application

Navigate to the directory where you saved the application files using your Command Prompt or Terminal:

```bash
cd path/to/your/application/folder
```

Then, run the Streamlit application:

```bash
streamlit run app.py
```

This will open the application in your default web browser.

## Usage

### Teacher Usage

1.  Click on "Teacher Login".
2.  Select the class you want to take attendance for (CSE, CSE-AIML, or CSE-DS).
3.  Click "Take Attendance". The application will simulate scanning for students.
4.  After a random delay (10-30 seconds), the attendance results will be displayed.
5.  Click "Logout" to return to the login page.

### Student Usage

1.  Click on "Student Login".
2.  Enter your Name, Roll Number, and Department (CSE, CSE-AIML, or CSE-DS).
3.  Click "Login".
4.  On your dashboard, click "Give Attendance". This simulates your check-in for attendance.
5.  Click "Logout" to return to the login page. Your data will be removed from the system upon logout.

## Important Notes on Simulated Bluetooth Detection

*   **Web Browser Limitations:** Web browsers do not allow direct access to Bluetooth for security and privacy reasons. Therefore, this application simulates the Bluetooth detection process.
*   **Student Check-in:** For a student to be marked "Present" by the teacher, they must have clicked the "Give Attendance" button on their student dashboard during the current session.

## Troubleshooting

*   **`streamlit` command not found**: Ensure Streamlit is installed correctly and your Python environment's PATH is configured.
*   **Data not persisting**: Remember that `students.json`, `teachers.json`, and `attendance.json` are used for initial loading. During the application's runtime, data is primarily managed in Streamlit's `st.session_state`. Changes made within the running app will be saved back to the JSON files when `save_data` is called, but `st.session_state` is reset when the browser tab is closed or the app is restarted.

For further assistance, please refer to the Streamlit documentation online.


