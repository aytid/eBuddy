import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Menu options
menu_options = ["Home", "Attendance", "SGPA", "Contact"]
st.title("Hi There!")
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
	st.title("GPA graphs")
	n=st.number_input("Enter number of semesters held",min_value=1, format="%i")
	l1=[]
	for i in range(n):
		input_value = st.number_input(f'Enter Semester {i+1} SGPA', key=f'input_{i+1}')
		l1.append(input_value)

	l2=[]
	avg=0
	for i in range(n):
		for j in range(i+1):
			avg+=l1[j]
		avg=avg/(j+1)
		l2.append(avg)
		avg=0
		
	semesters = [i+1 for i in range(len(l1))]
	plt.plot(semesters, l1,label='SGPA',marker='o',color='r')
	plt.plot(semesters, l2,label='CGPA',marker='o',color='k')
	plt.xlabel('Semester')
	plt.ylabel('GPA')
	plt.xticks(np.arange(1,n+1,1))
	plt.title('Semester SGPAs and CGPAs')
	plt.legend()
	st.pyplot(plt)

elif s == "Contact":
	st.markdown("""<a href='https://github.com/aytid'>Github</a>""", unsafe_allow_html=True)
	st.write("adityathirumala20@gmail.com")
	st.markdown("""<a href='https://www.linkedin.com/in/thirumala-rohanaditya-6b8228264'>LinkedIn Profile</a>""", unsafe_allow_html=True)


st.write('\n\n')
st.write("~Rohan Aditya Thirumala")

