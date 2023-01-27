import pandas as pd #dependency
import numpy as np #dependency
import json
df_teacher = pd.DataFrame({

    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp",
    "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
    "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m'],
    "weight": ['80kg', '70kg', '690kg', '73kg', '60kg', '70kg', '80kg', '88kg', '74kg']
})

result = []

# group the student dataframe by teacher
grouped_students = df_student.groupby("teacher")


# iterate through the groups
for teacher, group in grouped_students:
    # get the relevant information from the teacher dataframe
    teacher_info = df_teacher[df_teacher["name"] == teacher]
    school = teacher_info["school"].values[0]
    married = str(teacher_info["married"].values[0])

    # create a dictionary for the students in the group
    students = [{"student": row["name"], "age": row["age"], "height": row["height"]} for i, row in group.iterrows()]

    # add the teacher information and students to the final result
    result.append({"teacher": teacher, "school": school, "married": married, "Students": students})

Json_string = json.dumps(result, indent=4, sort_keys=True)
# print(Json_string)





