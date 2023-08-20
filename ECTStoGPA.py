"""

             /\_/\
            (  ･ω･)
|-----------U--BW--U----------|
|       MMXXIII_VIII_XX       |
|           Convert           |
|         ECTS credits        |
|            to GPA           |
|_____________________________|
            |     |
            |     |
             U   U

"""


# Grade and Credit value Validators

def grade_input_validator():
    grade_dict = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "E": 1.0, "F": 0.0}
    done = False
    while not done:
        try:
            grade_letter = input("Enter your ECTS grade (A/B/C/D/E/F) : ")
            grade = grade_letter.strip().upper()
            if grade in grade_dict:
                return grade
                done = True
            else:
                print("Enter a valid ECTS grade (A/B/C/D/E/F)")
        except ValueError:
            print("Enter a valid ECTS grade (A/B/C/D/E/F)")


def credit_input_validator():
    done = False
    while not done:
        try:
            ects_value = input("Enter ECTS credit : ")
            if len(ects_value.strip()) >= 0:
                ects_credit = float(ects_value)
                if ects_credit >= 0:
                    done = True
                    return ects_credit
                else:
                    print("The ECTS credit should be a positive value")
            else:
                print("Invalid input.. Please try again !")
        except ValueError:
            print("A number required ...")


# Main

print(f"Welcome to ECTS to GPA converter ....")

grade_dict = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "E": 1.0, "F": 0.0}
each_ects_value = 0
total_credits = 0
ects_value = 0
gpa = 0
done = False
while not done:
    module = input("Enter module name (enter 0 to finish): ")
    if module == "0":
        done = True
    else:
        ects_grade = grade_input_validator()
        ects_credit_value = credit_input_validator()
        each_ects_value = grade_dict[ects_grade] * ects_credit_value
        ects_value += each_ects_value
        total_credits += ects_credit_value
gpa = ects_value/total_credits
final_gpa = round(gpa, 2)

print(f"Your GPA is {final_gpa} ")