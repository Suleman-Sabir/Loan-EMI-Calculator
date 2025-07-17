import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Attendance Tracker", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🎓 Attendance Tracker")
page = st.sidebar.radio("Go to", [
    "🏠 Dashboard",
    "➕ Add Student",
    "📚 Add Subject",
    "📝 Mark Attendance",
    "📊 View Attendance",
    "⬇️ Download Report"
])

# --- Dashboard ---
if page == "🏠 Dashboard":
    st.title("📋 Attendance Tracker Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📘 Total Subjects", "0")
    with col2:
        st.metric("👨‍🎓 Total Students", "0")
    with col3:
        st.metric("📝 Records Taken", "0")
    st.markdown("---")
    st.info("Use the sidebar to navigate between different sections of the Attendance Tracker.")

# --- Add Student ---
elif page == "➕ Add Student":
    st.title("➕ Add New Student")
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("Enter Student ID")
    with col2:
        student_name = st.text_input("Enter Student Name")
    if st.button("Add Student"):
        st.success(f"Student '{student_name}' with ID '{student_id}' added successfully!")

# --- Add Subject ---
elif page == "📚 Add Subject":
    st.title("📚 Add New Subject")
    subject = st.text_input("Enter Subject Name")
    if st.button("Add Subject"):
        st.success(f"Subject '{subject}' added successfully!")

# --- Mark Attendance ---
elif page == "📝 Mark Attendance":
    st.title("📝 Mark Attendance")
    st.date_input("Select Date", value=datetime.today())
    subject = st.selectbox("Select Subject", ["Math", "Science", "English"])
    st.markdown("### 👨‍🎓 Select Present Students")
    students = ["Ali", "Sana", "Ahmed", "Zara"]
    selected = st.multiselect("Mark Present", students)
    if st.button("Submit Attendance"):
        st.success("Attendance marked successfully!")

# --- View Attendance ---
elif page == "📊 View Attendance":
    st.title("📊 View Attendance Records")
    st.selectbox("Select Subject", ["Math", "Science", "English"])
    st.date_input("Filter by Date")
    st.markdown("#### Attendance Table (Preview Only)")
    st.dataframe({
        "Student": ["Ali", "Sana", "Ahmed"],
        "Subject": ["Math", "Math", "Math"],
        "Date": ["2025-07-17"]*3,
        "Status": ["Present", "Absent", "Present"]
    })

# --- Download Report ---
elif page == "⬇️ Download Report":
    st.title("⬇️ Download Attendance Report")
    st.info("Click below to download the attendance report (demo button).")
    st.download_button("📥 Download CSV", data="Name,Subject,Date,Status", file_name="report.csv")
