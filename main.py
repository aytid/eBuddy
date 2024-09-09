import streamlit as st

# App Title
st.title("eBuddy Webapp!")

# Menu Options
menu_options = ["Home", "Attendance", "SGPA", "Contact"]
selected_option = st.selectbox("Select an Option", menu_options)

# Home Page
if selected_option == "Home":
    st.header("Welcome to eBuddy - Your Attendance and CGPA Companion")
    c1, c2, c3 = st.columns(3)
    c1.markdown("### Know your attendance status before and after bunking classes!")
    c2.markdown("### Estimate your SGPA for an expected CGPA!")
    c3.markdown("### Track your academic performance easily!")

# Attendance Page
elif selected_option == "Attendance":
    st.header("Attendance Tracker")

    # Input Fields for Attendance
    total_classes = st.number_input("Enter Total Number of Classes", min_value=1)
    classes_present = st.number_input("Enter Number of Classes Present", min_value=0)

    if total_classes > 0:
        # Current Attendance Calculation
        current_attendance = round((classes_present / total_classes) * 100, 2)
        st.info(f"Your Current Attendance: **{current_attendance}%**")

        # Bunking Calculation
        st.subheader("BUNK Meter")
        bunk_classes = st.number_input("Enter Number of Classes to Bunk", min_value=0)
        if bunk_classes > 0:
            new_total = total_classes + bunk_classes
            new_attendance = round((classes_present / new_total) * 100, 2)
            st.info(f"Your Attendance after Bunking: **{new_attendance}%**")

        # Target Attendance Calculation
        target_attendance = st.number_input("Enter Your Target Attendance", min_value=0)
        if target_attendance > 0:
            x = 0
            while round(((classes_present + x) / (total_classes + x) * 100), 2) < target_attendance:
                x += 1
            st.success(f"To achieve {target_attendance}% attendance, attend {x} more classes!")

# SGPA Estimator Page
elif selected_option == "SGPA":
    st.header("SGPA Estimator")

    # Input Fields for SGPA Calculation
    current_cgpa = st.number_input("Enter Your Current CGPA", format="%.2f")
    num_semesters = st.number_input("Enter Number of Semesters Completed", min_value=1, format="%i")
    target_cgpa = st.number_input("Enter Your Target CGPA After This Semester", format="%.2f")

    if num_semesters > 0 and current_cgpa > 0 and target_cgpa > 0:
        required_sgpa = 0
        estimated_cgpa = round(((num_semesters * current_cgpa) + required_sgpa) / (num_semesters + 1), 2)

        while estimated_cgpa < target_cgpa:
            required_sgpa += 0.01
            estimated_cgpa = round(((num_semesters * current_cgpa) + required_sgpa) / (num_semesters + 1), 2)

        required_sgpa = round(required_sgpa, 2)
        if required_sgpa > 10:
            st.error("It is not possible to reach your expected CGPA!")
        else:
            st.success(f"You need to score a minimum of **{required_sgpa} SGPA** in your next semester.")

# Contact Page
elif selected_option == "Contact":
    st.header("Connect with Me and Stay Updated!")
    st.markdown("""
        - **[LinkedIn](https://www.linkedin.com/in/rohan-aditya-thirumala-6b8228264/)** - Let's network and connect professionally!
        - **[GitHub](https://github.com/aytid)** - Check out my projects and contributions to the tech community.
        - **[Instagram](https://www.instagram.com/)** - Follow my journey and personal updates.
        - **Email** - Drop me a message anytime at adityathirumala20@gmail.com.
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.write("~ Rohan Aditya Thirumala")
