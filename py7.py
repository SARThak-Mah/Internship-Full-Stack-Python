class studentdata():
    def __init__(self):
        # Clean nested data grid mapping tracking records
        self.student_data = {
            "101": {
                "student_name": "Sarthak Mahurkar", 
                "date_of_birth": "22/2/2006",
                "science": 90, 
                "social_science": 80, 
                "mathematics": 75,
                "hindi": 95, 
                "english": 70, 
                "sanskrit": 80
            },
            "102": {
                "student_name": "Aryan Patil", 
                "date_of_birth": "14/7/2008",
                "science": 90, 
                "social_science": 60, 
                "mathematics": 75,
                "hindi": 55, 
                "english": 60, 
                "sanskrit": 80
            },
            "103": {
                "student_name": "Ojaswi Dhuliya", 
                "date_of_birth": "13/3/2008",
                "science": 80, 
                "social_science": 80, 
                "mathematics": 75,
                "hindi": 90, 
                "english": 70, 
                "sanskrit": 60
            },
            "104": {
                "student_name": "Aadil Pillai", 
                "date_of_birth": "31/9/2008",
                "science": 85, 
                "social_science": 80, 
                "mathematics": 65,
                "hindi": 95, 
                "english": 80, 
                "sanskrit": 50
            },
            "105": {
                "student_name": "Annaya sharma", 
                "date_of_birth": "8/12/2006",
                "science": 90, 
                "social_science": 80, 
                "mathematics": 75,
                "hindi": 95, 
                "english": 70, 
                "sanskrit": 80
            },
            "106": {
                "student_name": "Anushka shinde", 
                "date_of_birth": "2/5/2008",
                "science": 90, 
                "social_science": 80, 
                "mathematics": 75,
                "hindi": 95, 
                "english": 70, 
                "sanskrit": 80
            }
        }
        
    def get_student_data(self):
        return self.student_data

class result(studentdata):
    def __init__(self, roll_number):
        self.status = False
        self.roll_number = roll_number
        super().__init__() # Safe Single Inheritance call
        self.s_d = self.get_student_data()
        
        # Direct membership verification replaces long loops
        if self.roll_number in self.s_d:
            print(f"\n{self.s_d[self.roll_number]['student_name']}")
            print("-" * 100)
            self.status = True
                
    def Done(self):
        return self.status

# --- Main Program Execution Loop ---
print("-------------------------------------------------------")
print("----------------------Welcome to you-------------------")
n = "yes"

while n.lower() != "no":
    print("-------------------------------------------------------")
    r = input("Enter your roll number : ").strip()
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    
    result_obj = result(r)
    popup = result_obj.Done()
    
    if popup:
        print("\tBOARD OF SECONDARY EDUCATION, MAHARASHTRA \n")
        print("\tHIGH SCHOOL CERTIFICATE EXAMINATION 2021 \n") 
        
        s_d = result_obj.get_student_data()
        current_student = s_d[r] # Clean direct O(1) hashing access instead of loop
        
        print(" ROLL NUMBER :", r, "\n")
        print(" STUDENT NAME :", current_student["student_name"], "\n")
        print(" SCHOOL NAME : GOVT. HIGHER SECONDARY SCHOOL INDORE \n")
        print(" STUDENT CLASS : 10th  \n")
        print(" STUDENT STATUS : REGULAR \n")
        print()
        
        print("SUBJECT NAME\tSUBJECT MARKS \n")
        print("Science\t\t", current_student["science"])
        print("Social Science\t", current_student["social_science"])
        print("Mathematics\t", current_student["mathematics"])
        print("Hindi\t\t", current_student["hindi"])
        print("English\t\t", current_student["english"])
        print("Sanskrit\t", current_student["sanskrit"])

        # Calculations nested inside validation scope prevents terminal crashes
        x = (current_student["science"] + current_student["social_science"] + 
             current_student["mathematics"] + current_student["hindi"] + 
             current_student["english"] + current_student["sanskrit"]) / 6
        
        if 40 <= x <= 100:
            Result = "Pass"
            if x >= 70: Grade = "Dist"
            elif x >= 60: Grade = "A"
            elif x >= 50: Grade = "B"
            else: Grade = "C"
        else:
            Grade = "F"
            Result = "Fail"
            
        print("----------------------------------------------------------------------------------------------------")    
        print("Percentage                         ", round(x, 2), "%")         
        print("Grade                              ", Grade)
        print("Result Status                      ", Result)
        print("----------------------------------------------------------------------------------------------------") 
        
    else:
        print("Please enter correct roll number! \n")
        
    n = input("Do want to visit again: \n Type (yes/no) : ").strip()

else:
    print("----------------------------thank for visit---------------------------------")