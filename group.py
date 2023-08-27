import streamlit as st

# Menu options
menu_options = ["Home", "Attendance", "SGPA", "Contact"]
st.title("Online buddy!")
st.title("Your Attendance and CGPA Companion")
# Display the menu
s = st.selectbox("Select an Option", menu_options)

# Handle menu selections
if s == "Home":
    c1, c2, c3 = st.columns([1, 1, 1])
    c1.title("This WebApp is here for YOU!")
    c2.title("You can know attendance before and after bunking class")
    c3.title("You can estimate SGPA for an expected CGPA")

elif s == "Attendance":
    st.title("ATTENDANCE")
    t = st.number_input("Enter total number of classes", min_value=1)
    p = st.number_input("Enter number of classes present", min_value=1)
    st.subheader("Present Attendance")
    a = round((p / t) * 100, 2)
    st.info(f"{a}%")
    st.subheader("BUNK Meter")
    b = st.number_input(" ", min_value=0)
    st.subheader("Attendance after Bunking")
    t += b
    a = round((p / t) * 100, 2)
    st.info(f"{a}%")
    st.subheader("Enter target attendance")
    tg = st.number_input("   ", min_value=0)
    x = 0
    while round(((p + x) / (t + x) * 100), 2) < tg:
        x += 1
    st.success(f"Attend {x} more Classes!!")

elif s == "SGPA":
	st.title("SGPA Estimator")
	c = st.number_input("Enter your present CGPA", format="%f")
	n = st.number_input("Enter number of Semesters held", min_value=1, format="%i")
	e = st.number_input("Enter your target CGPA after this semester", format="%f")
	s = 0
	x = round(((n * c) + s) / (n + 1))
	while x <= e:
		s += 0.01
		x = round(((n * c) + s) / (n + 1), 2)
	s = round(s, 2)
	if s > 10:
		st.error("You cannot reach your expected CGPA!!")
	else:
		st.success(f"You need to score a minimum of {s} SGPA in your next semester")
elif s == "Contact":
	st.markdown("""<a href='https://github.com/aytid'>Github</a>""", unsafe_allow_html=True)
	st.write("adityathirumala20@gmail.com")
	st.markdown("""<a href='https://www.linkedin.com/in/thirumala-rohanaditya-6b8228264'>LinkedIn Profile</a>""", unsafe_allow_html=True)


st.write('\n\n')
st.write("~Rohan Aditya Thirumala")
