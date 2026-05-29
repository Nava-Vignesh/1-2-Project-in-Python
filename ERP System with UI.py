import pandas as pd
import streamlit as st

# ==========================================
# 1. CLASS DEFINITION
# ==========================================
class Student:
    def __init__(self, id, name, course, quota, cgpa, dues, fee):
        self.id = id
        self.name = name
        self.course = course
        self.quota = quota
        self.cgpa = cgpa
        self.dues = dues
        self.fee = fee

    def get_details_dict(self):
        return {
            "Roll Number": self.id,
            "Name": self.name,
            "Course": self.course,
            "CGPA": self.cgpa,
            "Quota": self.quota,
            "Total Fee": self.fee,
            "Pending Due": self.dues
        }
         
    def pay_fee_logic(self, amt):
        if amt <= self.dues:
            self.dues -= amt
            return True, f"Fee payment Successful! Remaining Due: ₹{self.dues}"
        else:
            return False, f"Invalid Amount! Enter an amount less than or equal to current dues (₹{self.dues})."

# ==========================================
# 2. RUNTIME STORAGE & GLOBAL LOAD FUNCTIONS
# ==========================================
if 'student_database' not in st.session_state:
    st.session_state.student_database = {}

@st.cache_data
def load_dataframe(file):
    return pd.read_excel(file)

def load_objects_to_memory(file):
    df = pd.read_excel(file)
    for _, row in df.iterrows():
        s_id = str(row['Id'])
        if s_id not in st.session_state.student_database:
            st.session_state.student_database[s_id] = Student(
                id=s_id,
                name=row['Name'],
                course=row['Course'],
                quota=row['Quota'],
                cgpa=float(row['CGPA']),
                fee=float(row['FEES']),
                dues=float(row['DUE'])
            )

# Load data safely
try:
    load_objects_to_memory("testdata.xlsx")
    d = load_dataframe("testdata.xlsx")
except Exception as e:
    st.error("Please place 'testdata.xlsx' in the project root directory.")
    st.stop()

# ==========================================
# 3. CORE PANDAS FUNCTIONS (INDEPENDENT)
# ==========================================
def getlist(course_name):
    filtered_data = d[d["Course"] == course_name]
    return filtered_data[["Id", "Name", "Course", "Quota", "CGPA"]]

def gettoppers(course_name):
    filtered_data = d[d["Course"] == course_name]
    toppers = filtered_data.sort_values(by="CGPA", ascending=False).head(5)
    return toppers[["Id", "Name", "CGPA"]]

# ==========================================
# 4. STREAMLIT FRONTEND LAYOUT
# ==========================================
st.set_page_config(page_title="Student ERP System", layout="wide")
st.title("🎓 Student ERP Dashboard")
st.markdown("---")

# Navigation Sidebar - Simplified to exactly 2 options
menu = st.sidebar.radio("Navigation Menu", [
    "Institute Overview", 
    "Student Portal"
])

# ------------------------------------------
# OPTION 1: INSTITUTE OVERVIEW (Stats + Functions)
# ------------------------------------------
if menu == "Institute Overview":
    st.header("🏛️ Institute Overview & Analytics")
    
    # High-level institutional metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Enrolled Students", len(d))
    col2.metric("Average Institutional CGPA", f"{d['CGPA'].mean():.2f}")
    col3.metric("Total Outstanding Fees", f"₹{d['DUE'].sum():,}")
    
    st.markdown("---")
    
    # Splitting the independent functions into two side-by-side columns
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.subheader("📋 View Student Roster")
        available_branches_list = d["Course"].unique()
        selected_branch_list = st.selectbox("Select Branch to get roster list:", available_branches_list, key="roster_select")
        
        # Trigger independent getlist function
        roster_df = getlist(selected_branch_list)
        st.dataframe(roster_df, use_container_width=True)
        
    with right_col:
        st.subheader("🏆 View Top Performers")
        available_branches_toppers = d["Course"].unique()
        selected_branch_toppers = st.selectbox("Select Branch to view toppers:", available_branches_toppers, key="topper_select")
        
        # Trigger independent gettoppers function
        toppers_df = gettoppers(selected_branch_toppers)
        st.dataframe(toppers_df, use_container_width=True)

# ------------------------------------------
# OPTION 2: STUDENT PORTAL (Profile & Fee Management)
# ------------------------------------------
elif menu == "Student Portal":
    st.header("🗂️ Student Portal & Management")
    
    search_id = st.text_input("Enter Student Roll Number/ID:")
    
    if search_id:
        if search_id in st.session_state.student_database:
            student_obj = st.session_state.student_database[search_id]
            details = student_obj.get_details_dict()
            
            st.success(f"Record found for {details['Name']}!")
            
            # Profile Details Display Grid
            det_col1, det_col2 = st.columns(2)
            with det_col1:
                st.markdown(f"**Roll Number:** {details['Roll Number']}")
                st.markdown(f"**Course/Branch:** {details['Course']}")
                st.markdown(f"**Academic CGPA:** {details['CGPA']}")
            with det_col2:
                st.markdown(f"**Total Institutional Fees:** ₹{details['Total Fee']}")
                # Displays the live dues directly from the object state
                st.info(f"**Current Outstanding Balance Due: ₹{student_obj.dues}**")
            
            st.markdown("---")
            st.subheader("💳 Process Financial Transaction")
            
            # Fee Processing input elements
            pay_amt = st.number_input("Enter fee payment transaction amount (₹):", min_value=0.0, step=500.0)
            
            if st.button("Confirm Fee Payment"):
                if pay_amt > 0:
                    success, message = student_obj.pay_fee_logic(pay_amt)
                    if success:
                        st.success(message)
                        # Reruns the application immediately to update the remaining dues on screen
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter a clear monetary validation value greater than 0.")
        else:
            st.error("Roll Number not found in system database registry logs.")