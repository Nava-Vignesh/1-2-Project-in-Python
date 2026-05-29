import pandas as pd

student_database = {}
def load(file):
    df = pd.read_excel(file)
    for _, row in df.iterrows():
            s_id = (row['Id'])
            
            # Instantiating the object and saving it to our database dictionary
            student_database[s_id] = Student(
                id= s_id,
                name=row['Name'],
                course=row['Course'],
                quota = row['Quota'],
                cgpa=float(row['CGPA']),
                fee = float(row["FEES"]),
                dues=float(row['DUE'])
                )
    print(f"System initialized: {len(student_database)} students loaded.")


def getlist(course):
    print(d[d["Course"]==course])
def gettoppers(course):
    print(d[d["Course"]==course].head())


class Student:
    def __init__(self, id, name, course,quota, cgpa, dues,fee):
        self.id = id
        self.name = name
        self.course = course
        self.quota = quota
        self.cgpa = cgpa
        self.dues = dues
        self.fee = fee

    def getdetails():
         id = input("Enter Roll Number: ")
         print(f"Name: {student_database[id].name}")
         print(f"Course: {student_database[id].course}")
         print(f"CGPA: {student_database[id].cgpa}")   
         print(f'Quota: {student_database[id].quota}')
         print(f'FEES: {student_database[id].fee}')
         print(f'DUE: {student_database[id].dues}')
         
    def feepay():
        id = input("Enter Roll Number: ")
        amt = int(input("Enter fee payment amt:"))
        if amt<=student_database[id].dues:
            student_database[id].dues -= amt
            print(f"Fee payment Succesful\n Due Remaining:{student_database[id].dues}")
        else:
            print("Invalid")
    


load("testdata.xlsx")
print(student_database["2025TEST101"].name)
d = pd.read_excel("testdata.xlsx")
print(d[(d["Course"]=="CSM") & (d["Quota"]=="EAPCET")])

getlist("CSM")
gettoppers("CAI")

#Student.getdetails()
#Student.feepay()
#getstats("CSM")
