
## Application Architecture Plan

### Kivy Screens:
1.  **Login Screen:**
    *   Two buttons: 'Teacher Login' and 'Student Login'.
    *   Teacher Login: Direct access to teacher dashboard.
    *   Student Login: Input fields for Name, Roll Number, Department.

2.  **Teacher Dashboard:**
    *   Buttons for class selection: 'CSE', 'CSE-AIML', 'CSE-DS'.
    *   Once a class is selected, a 'Take Attendance' button appears.
    *   Displays attendance status for the selected class.

3.  **Student Dashboard:**
    *   Displays logged-in student's Name, Roll Number, Department.
    *   A 'Give Attendance' button.
    *   Displays attendance status for the student.

### Data Flow:
*   User selects login type.
*   Student provides details, which are stored locally upon successful login.
*   Teacher selects class.
*   Teacher initiates Bluetooth scan.
*   Student initiates Bluetooth broadcast/discovery.
*   Attendance is marked based on matching department and detected devices.
*   Attendance status is updated on both teacher and student interfaces.

### Data Storage:
*   **Students:** Store Name, Roll Number, Department, and Attendance Status. A simple JSON file or a lightweight database like SQLite will be used for persistence.
*   **Teachers:** Store Teacher Name (optional, for display purposes) and potentially their associated classes. This can also be a JSON file.
*   **Attendance Records:** Store attendance for each student per class. This will be linked to the student data and updated dynamically.

