import streamlit as st
from streamlit_option_menu import option_menu

s=option_menu(
			menu_title="Main Menu",
			options=["Home","Attendance","SGPA","Contact"],
			icons=["house","person-check-fill","file-earmark-spreadsheet","envelope"],
			menu_icon="list",
			default_index=0,
			orientation="horizontal",
			)
if s=="Home":
	c1,c2,c3=st.columns([1,1,1])
	c1.title("This WebApp is here for YOU!")
	c2.title("You can know attendance before and after bunking class")
	c3.title("You can estimate SGPA for an expected CGPA")	
if s=="Attendance":
	st.title("ATTENDANCE")
	t=st.number_input("Enter total number of classes",min_value=1)
	p=st.number_input("Enter number of classes present",min_value=1)
	st.subheader("Present Attendance")
	a=round((p/t)*100,2)
	st.info(f"{a}%")
	st.subheader("BUNK Meter")
	b=st.number_input(" ",min_value=0)
	st.subheader("Attendance after Bunking")
	t+=b
	a=round((p/t)*100,2)
	st.info(f"{a}%")
	st.subheader("Enter target attendance")
	tg=st.number_input("   ",min_value=0)
	x=0
	while round(((p+x)/(t+x)*100),2)<tg:
		x+=1
	st.success(f"Attend {x} more Classes!!")
	
if s=="SGPA":
	st.title("SPGA Estimator")
	c=st.number_input("Enter your present CGPA",format="%f")
	n=st.number_input("Enter number of Semesters held",min_value=1,format="%i")
	e=st.number_input("Enter your target CGPA after this semester",format="%f")
	s=0
	x=round(((n*c)+s)/(n+1))
	while x<=e:
		s+=0.01
		x = round(((n * c) + s) / (n + 1),2)
	s=round(s,2)
	if s>10:
		st.error("You cannot reach your expected CGPA!!")
	else:
		st.success(f"You need to score minimum of {s} SGPA in your next semester")
if s=="Contact":
	st.write("Mobile: +91 9701343474")
	st.write("Mail: adityathirumala20@gmail.com")
	st.markdown("""<a href='https://www.linkedin.com/in/thirumala-rohanaditya-6b8228264'>LinkedIn Profile</a>""", unsafe_allow_html=True)
st.write('\n\n')
footer_container = st.container()
with footer_container:
    st.write("~Rohan Aditya Thirumala")