import streamlit as st

# Set Page Config
st.set_page_config(page_title="eBuddy Web App", layout="wide")

# App Title in Sidebar
menu_options = ["Home", "College Attendance", "SGPA Estimator", "Work from Home%"]
st.title("eBuddy")

# Simple Dropdown Menu for Navigation
selected_option = st.selectbox(
    "Navigate to",
    options=menu_options
)

# Home Page
if selected_option == "Home":
    st.subheader("Simplify Your Academic and Office Life")

# Attendance Page
elif selected_option == "College Attendance":
    st.title("Attendance Tracker")
    st.subheader("Monitor Your Attendance and Plan Ahead")

    total_classes = st.number_input("Enter Total Number of Classes", min_value=1, value=50)
    classes_present = st.number_input("Enter Number of Classes Present", min_value=0, value=40)

    if classes_present > total_classes:
        st.error("Classes present cannot exceed total classes!")
    else:
        current_attendance = round((classes_present / total_classes) * 100, 2)
        st.info(f"🎓 Your Current Attendance: **{current_attendance}%**")

        st.subheader("📉 Bunk Meter")
        bunk_classes = st.number_input("Enter Number of Classes to Bunk", min_value=0)
        if bunk_classes > 0:
            new_total = total_classes + bunk_classes
            new_attendance = round((classes_present / new_total) * 100, 2)
            st.info(f"After bunking {bunk_classes} classes, your attendance would be **{new_attendance}%**.")

            st.subheader("🎯 Target Attendance Calculator")
            target_attendance_bunk = st.number_input(
                "Enter Desired Target Attendance(%)",
                min_value=1,
                max_value=100,
                value=75,
            )
            if target_attendance_bunk > new_attendance:
                x = 0
                while round(((classes_present + x) / (new_total + x) * 100), 2) < target_attendance_bunk:
                    x += 1
                st.success(f"✅ To achieve {target_attendance_bunk}%, you need to attend **{x} more classes**.")
            else:
                st.success("Your projected attendance already meets or exceeds your target!")

# SGPA Estimator Page
elif selected_option == "SGPA Estimator":
    st.title("SGPA Estimator")
    st.subheader("Plan Your Next Semester")

    current_cgpa = st.number_input("Enter Your Current CGPA", min_value=0.0, max_value=10.0, format="%.2f", value=7.5)
    num_semesters = st.number_input("Enter Number of Semesters Completed", min_value=1, format="%i", value=4)
    target_cgpa = st.number_input("Enter Your Target CGPA After This Semester", min_value=0.0, max_value=10.0, format="%.2f", value=8.0)

    if current_cgpa > 0 and target_cgpa > current_cgpa:
        required_sgpa = 0
        estimated_cgpa = round(((num_semesters * current_cgpa) + required_sgpa) / (num_semesters + 1), 2)

        while estimated_cgpa < target_cgpa:
            required_sgpa += 0.01
            estimated_cgpa = round(((num_semesters * current_cgpa) + required_sgpa) / (num_semesters + 1), 2)

        required_sgpa = round(required_sgpa, 2)
        if required_sgpa > 10:
            st.error("😟 It is not possible to reach your target CGPA.")
        else:
            st.success(f"🌟 You need to score at least **{required_sgpa} SGPA** in your next semester.")
    else:
        st.info("Enter valid inputs to estimate your required SGPA.")

# Work from Home % Page
elif selected_option == "Work from Home":
    st.title("Work from Home Calculator")
    st.subheader("Ensure 60% Work from Office")
    
    total_working_days = st.number_input("Total Working Days in Month", min_value=1, value=22)
    leaves_taken = st.number_input("Number of Leaves Taken", min_value=0, value=0)
    wfh_done = st.number_input("Number of WFH Days Already Taken", min_value=0, value=0)

    actual_days = total_working_days - leaves_taken - holidays

    if actual_days <= 0:
        st.error("❌ No valid working days left after excluding leaves and holidays.")
    else:
        max_wfh_allowed = int(0.4 * actual_days)
        remaining_wfh = max(0, max_wfh_allowed - wfh_done)

        st.info(f"📌 You can take **{remaining_wfh}** more WFH days this month to maintain 60% in-office presence.")
        st.caption(f"Note: Based on {actual_days} valid working days.")

# Always Visible Contact Section
st.write("---")
#st.title("Connect with Me!")
st.markdown("""
    ### Connect with Me
    - **[LinkedIn](https://www.linkedin.com/in/rohan-aditya-thirumala-6b8228264/)** - Let's network and connect professionally!
    - **[GitHub](https://github.com/aytid)** - Explore my projects.
    - **[Instagram](https://www.instagram.com/)** - Follow my personal journey.
    - **Email** - Reach me at: adityathirumala20@gmail.com
""", unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown("© 2024 **Rohan Aditya Thirumala**")
