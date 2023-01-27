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
    "height": ['2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m'],
    "weight": ['80kg', '70kg', '690kg', '73kg', '60kg', '70kg', '80kg', '88kg', '74kg'],

})

final_result = df_student.groupby("teacher").apply(lambda x: {
    "teacher": x.name,
    "school": df_teacher.loc[df_teacher["name"] == x.name, "school"].values[0],
    "married": str(df_teacher.loc[df_teacher["name"] == x.name, "married"].values[0]),
    "students": [{**row.to_dict()} for i, row in x.iterrows()]
}).tolist()

Json_string = json.dumps(final_result, indent=4, sort_keys=True)
print(Json_string)
