import streamlit as st

# Set Page Config
st.set_page_config(page_title="eBuddy Web App", layout="wide")

# App Title in Sidebar
st.sidebar.title("eBuddy Navigation")
menu_options = ["Home", "Attendance", "SGPA Estimator", "Contact"]
selected_option = st.sidebar.radio("Select a Page", menu_options)

# Home Page
if selected_option == "Home":
    st.title("eBuddy")
    st.subheader("Simplify Your Academic Life!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("attendance.png", caption="Track Attendance", use_column_width=False, width=150)
        st.markdown("### Know your attendance status before and after bunking!")
    with col2:
        st.image("score.png", caption="Estimate SGPA", use_column_width=False, width=250)
        st.markdown("### Calculate the SGPA needed for your desired CGPA!")

# Attendance Page
elif selected_option == "Attendance":
    st.title("Attendance Tracker")
    st.subheader("Monitor Your Attendance and Plan Ahead")

    # Input Fields
    total_classes = st.number_input("Enter Total Number of Classes", min_value=1, value=50)
    classes_present = st.number_input("Enter Number of Classes Present", min_value=0, value=40)

    if classes_present > total_classes:
        st.error("Classes present cannot exceed total classes!")
    else:
        # Current Attendance
        current_attendance = round((classes_present / total_classes) * 100, 2)
        st.info(f"🎓 Your Current Attendance: **{current_attendance}%**")

        # Bunking Meter
        st.subheader("📉 Bunk Meter")
        bunk_classes = st.number_input("Enter Number of Classes to Bunk", min_value=0)
        if bunk_classes > 0:
            new_total = total_classes + bunk_classes
            new_attendance = round((classes_present / new_total) * 100, 2)
            st.info(f"After bunking {bunk_classes} classes, your attendance would be **{new_attendance}%**.")

            # Target Attendance Calculator after Bunking
            st.subheader("🎯 Target Attendance Calculator")
            target_attendance_bunk = st.number_input(
                "Enter Desired Target Attendance",
                min_value=1,
                max_value=100,
                value=75,
            )
            if target_attendance_bunk > new_attendance:
                x = 0
                while round(((classes_present + x) / (new_total + x) * 100), 2) < target_attendance_bunk:
                    x += 1
                st.success(f"✅ To achieve {target_attendance_bunk}%, you need to attend **{x} more classes**.")
            elif target_attendance_bunk <= new_attendance:
                st.success("Your projected attendance already meets or exceeds your target!")

# SGPA Estimator Page
elif selected_option == "SGPA Estimator":
    st.title("SGPA Estimator")
    st.subheader("Plan Your Next Semester")

    # Input Fields
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

# Contact Page
elif selected_option == "Contact":
    st.title("Connect with Me!")
    st.markdown("""
        ### Stay in Touch:
        - **[LinkedIn](https://www.linkedin.com/in/rohan-aditya-thirumala-6b8228264/)** - Let's network and connect professionally!
        - **[GitHub](https://github.com/aytid)** - Explore my projects.
        - **[Instagram](https://www.instagram.com/)** - Follow my personal journey.
        - **Email** - Reach me at: adityathirumala20@gmail.com
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown("© 2024 **Rohan Aditya Thirumala**")
