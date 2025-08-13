import streamlit as st
import json
import time
import random
from PIL import Image

# Data storage files (for initial load and saving)
STUDENTS_FILE = 'students.json'
TEACHERS_FILE = 'teachers.json'
ATTENDANCE_FILE = 'attendance.json'
LOGO_PATH = 'mckvian_logo.jpeg'

# Load data from JSON files or initialize if not found
def load_data(filename, default_data):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)
        return default_data

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Initialize session state variables if they don't exist
if 'students_data' not in st.session_state:
    st.session_state.students_data = load_data(STUDENTS_FILE, {})

if 'teachers_data' not in st.session_state:
    st.session_state.teachers_data = load_data(TEACHERS_FILE, {
        'teacher1': {'name': 'Teacher 1', 'classes': ['CSE', 'CSE-AIML']},
        'teacher2': {'name': 'Teacher 2', 'classes': ['CSE-DS']}
    })

if 'attendance_data' not in st.session_state:
    st.session_state.attendance_data = load_data(ATTENDANCE_FILE, {})

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'login'

if 'logged_in_student_roll' not in st.session_state:
    st.session_state.logged_in_student_roll = None

if 'selected_class' not in st.session_state:
    st.session_state.selected_class = None

if 'attendance_message' not in st.session_state:
    st.session_state.attendance_message = ""

if 'show_attendance_list' not in st.session_state:
    st.session_state.show_attendance_list = False

if 'show_all_students_list' not in st.session_state:
    st.session_state.show_all_students_list = False

# Custom CSS for mobile optimization and color scheme
st.markdown("""
<style>
    .stApp {
        background-color: #FFFFFF; /* White background */
        color: black; /* Set all text to black */
    }
    .stButton>button {
        background-color: #87CEEB; /* Sky Blue */
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #6CA6CD; /* Darker Sky Blue on hover */
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #87CEEB;
        padding: 10px;
        color: black; /* Ensure text input is black */
    }
    .stSelectbox>div>div>div {
        border-radius: 5px;
        border: 1px solid #87CEEB;
        padding: 10px;
        color: black; /* Ensure selectbox text is black */
    }
    .stAlert {
        border-radius: 5px;
    }
    /* Mobile responsiveness */
    @media (max-width: 600px) {
        .stApp {
            padding: 10px;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 10px;
        }
        .stTextInput, .stSelectbox {
            width: 100%;
        }
    }
</style>
""", unsafe_allow_html=True)

# Function to display logo at the top corner
def display_logo():
    try:
        logo = Image.open(LOGO_PATH)
        st.image(logo, width=50)
    except FileNotFoundError:
        st.warning("Logo image not found. Please ensure 'mckvian_logo.jpeg' is in the same directory.")

# --- Login Page ---
def login_page():
    display_logo()
    st.title("MCKVIAN: Smart Attendance System")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Teacher Login", key="teacher_login_btn"):
            st.session_state.current_page = "teacher_dashboard"
            st.rerun()

    with col2:
        if st.button("Student Login", key="student_login_btn"):
            st.session_state.current_page = "student_login"
            st.rerun()

# --- Teacher Dashboard ---
def teacher_dashboard():
    display_logo()
    st.title("MCKVIAN: Smart Attendance System")
    st.header("Teacher Dashboard")

    st.write("Select a class to take attendance.")
    class_options = ["CSE", "CSE-AIML", "CSE-DS"]
    selected_class_display = st.selectbox("", class_options, index=class_options.index(st.session_state.selected_class) if st.session_state.selected_class else 0, key="class_select")

    if selected_class_display != st.session_state.selected_class:
        st.session_state.selected_class = selected_class_display
        st.session_state.attendance_message = f'Selected Class: {st.session_state.selected_class}. Click "Take Attendance" to scan.'
        st.session_state.show_attendance_list = False # Hide list when class changes
        st.session_state.show_all_students_list = False # Hide all students list when class changes

    st.write(st.session_state.attendance_message)

    col_buttons = st.columns(3) # Increased columns for new button
    with col_buttons[0]:
        if st.button("Take Attendance", key="take_attendance_btn"):
            if st.session_state.selected_class:
                st.session_state.attendance_message = f"Scanning for students in {st.session_state.selected_class}..."
                st.session_state.show_attendance_list = False # Hide list during scan
                st.session_state.show_all_students_list = False # Hide all students list during scan
                st.rerun()
                # Simulate delay for scanning
                time.sleep(random.randint(10, 30))

                present_students = []
                # Simulate device detection based on student data
                for roll, student in st.session_state.students_data.items():
                    if student["department"] == st.session_state.selected_class:
                        # Only mark present if student is 'active' (simulated Bluetooth on)
                        if st.session_state.students_data[roll]["attendance"] == "Present (awaiting teacher scan)":
                            present_students.append(roll)
                            st.session_state.students_data[roll]["attendance"] = "Present"
                        else:
                            st.session_state.students_data[roll]["attendance"] = "Absent"

                save_data(STUDENTS_FILE, st.session_state.students_data)

                if present_students:
                    st.session_state.attendance_message = f"Attendance marked for: {len(present_students)} students. (Present: {', '.join([st.session_state.students_data[r]['name'] for r in present_students])})"
                else:
                    st.session_state.attendance_message = "No students found for the selected class."
                st.rerun()
            else:
                st.session_state.attendance_message = "Please select a class first."

    with col_buttons[1]:
        if st.button("View Present Students", key="view_attendance_list_btn"):
            st.session_state.show_attendance_list = not st.session_state.show_attendance_list # Toggle visibility
            st.session_state.show_all_students_list = False # Hide other list
            st.rerun()

    with col_buttons[2]:
        if st.button("View All Students", key="view_all_students_btn"):
            st.session_state.show_all_students_list = not st.session_state.show_all_students_list # Toggle visibility
            st.session_state.show_attendance_list = False # Hide other list
            st.rerun()

    if st.session_state.show_attendance_list:
        display_present_students_list(st.session_state.selected_class)

    if st.session_state.show_all_students_list:
        display_all_students_list(st.session_state.selected_class)

    if st.button("Logout", key="teacher_logout_btn"):
        st.session_state.current_page = "login"
        st.session_state.selected_class = None
        st.session_state.attendance_message = ""
        st.session_state.show_attendance_list = False
        st.session_state.show_all_students_list = False
        st.rerun()

# --- Function to display present students list ---
def display_present_students_list(selected_class):
    st.subheader(f"Present Students in {selected_class}")
    if not st.session_state.students_data:
        st.info("No student data available.")
        return

    # Filter students by selected class and attendance status
    present_students_in_class = []
    for roll, student_info in st.session_state.students_data.items():
        if student_info["department"] == selected_class and student_info["attendance"] == "Present":
            present_students_in_class.append({
                "Roll Number": roll,
                "Name": student_info["name"]
            })

    if present_students_in_class:
        st.table(present_students_in_class)
    else:
        st.info(f"No students marked 'Present' in {selected_class} yet.")

# --- Function to display all students list ---
def display_all_students_list(selected_class):
    st.subheader(f"All Students in {selected_class}")
    if not st.session_state.students_data:
        st.info("No student data available.")
        return

    # Filter students by selected class
    all_students_in_class = []
    for roll, student_info in st.session_state.students_data.items():
        if student_info["department"] == selected_class:
            all_students_in_class.append({
                "Roll Number": roll,
                "Name": student_info["name"],
                "Attendance Status": student_info["attendance"]
            })

    if all_students_in_class:
        st.table(all_students_in_class)
    else:
        st.info(f"No students found in {selected_class}.")

# --- Student Login Page ---
def student_login_page():
    display_logo()
    st.title("MCKVIAN: Smart Attendance System")
    st.header("Student Login")

    with st.form("student_login_form"):
        name = st.text_input("Name")
        roll_number = st.text_input("Roll Number")
        department = st.selectbox("Department", ["CSE", "CSE-AIML", "CSE-DS"])

        submitted = st.form_submit_button("Login")

        if submitted:
            if not name or not roll_number or not department:
                st.error("All fields are required.")
            elif len(st.session_state.students_data) >= 5:
                st.error("Maximum student limit reached.")
            elif roll_number in st.session_state.students_data:
                st.error("Student with this roll number already exists.")
            else:
                st.session_state.students_data[roll_number] = {
                    'name': name,
                    'department': department,
                    'attendance': 'Not Marked'
                }
                save_data(STUDENTS_FILE, st.session_state.students_data)
                st.session_state.logged_in_student_roll = roll_number
                st.success(f"Student {name} logged in successfully.")
                st.session_state.current_page = "student_dashboard"
                st.rerun()

    if st.button("Back to Login", key="student_login_back_btn"):
        st.session_state.current_page = "login"
        st.rerun()

# --- Student Dashboard ---
def student_dashboard():
    display_logo()
    st.title("MCKVIAN: Smart Attendance System")
    st.header("Student Dashboard")

    if st.session_state.logged_in_student_roll:
        student_info = st.session_state.students_data[st.session_state.logged_in_student_roll]
        st.write(f"Name: {student_info['name']}")
        st.write(f"Roll Number: {st.session_state.logged_in_student_roll}")
        st.write(f"Department: {student_info['department']}")
        st.write(f"Attendance Status: {student_info['attendance']}")

        if st.button("Give Attendance", key="give_attendance_btn"):
            st.write("Attendance button clicked. (Simulated)")
            st.session_state.students_data[st.session_state.logged_in_student_roll]['attendance'] = "Present (awaiting teacher scan)"
            save_data(STUDENTS_FILE, st.session_state.students_data)
            st.rerun()

        if st.button("Logout", key="student_logout_btn"):
            if st.session_state.logged_in_student_roll in st.session_state.students_data:
                del st.session_state.students_data[st.session_state.logged_in_student_roll]
                save_data(STUDENTS_FILE, st.session_state.students_data)
                st.session_state.logged_in_student_roll = None
                st.success("Logged out and data deleted.")
            st.session_state.current_page = "login"
            st.rerun()
    else:
        st.warning("Please log in first.")
        st.session_state.current_page = "login"
        st.rerun()

# --- Page Routing ---
if st.session_state.current_page == 'login':
    login_page()
elif st.session_state.current_page == 'teacher_dashboard':
    teacher_dashboard()
elif st.session_state.current_page == 'student_login':
    student_login_page()
elif st.session_state.current_page == 'student_dashboard':
    student_dashboard()








