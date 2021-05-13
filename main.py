from amplpy import AMPL, Environment, DataFrame
import pandas as pd
import numpy as np
import sys
import os

from ampl_modules.amplcode import AmplCode
import ascii_table
import pandas as pd
import sys

df = pd.read_csv("pupils.csv", delimiter=";")
courses_names = df["course"].tolist()
pupils_names = list(sorted(set(",".join(df["pupils"]).split(","))))



print("Courses:", courses_names)
print("Pupils:", pupils_names)

#courses = list(range(len(courses)))
#pupils = list(range(len(pupils)))


# assignment matrix
assignment = {}
numberOfCourses = {}
for pi, p in enumerate(pupils_names):
    numberOfCourses[pi] = 0;
    for ci, c in enumerate(courses_names):
        assignment[(pi, ci)] = 1 if p in df[df["course"] == c]["pupils"].tolist()[0].split(",") else 0
        numberOfCourses[pi] += assignment[(pi, ci)]



if __name__ == "__main__":
    print("Alternating home schooling")

    print("Setup")

    environment = os.environ.get("AMPL_PATH", "ampl")

    ampl = AMPL(Environment(environment))
    ampl.setOption('solver', 'cplex')

    amplcode = AmplCode.from_file('ampl_template_fair_groups.txt')

    # print("Parameters from AMPL Code:")
    # print(amplcode.get_params())

    amplcode.set_set('pupils', list(range(len(pupils_names))))
    amplcode.set_set('courses', list(range(len(courses_names))))
    amplcode.set_param_data_3d("assignment", assignment.items())
    amplcode.set_param_data("numberOfCourses", numberOfCourses.items())


    amplcode.export("fair_groups_export.txt")

    ampl.eval(amplcode.code)

    ### transform output
    print("Values from Ampl (where x[p, c, g] = 1)")
    print("p,  c,    g")
    values = ampl.getVariable('x').getValues().toPandas()
    data = []
    for key, value in zip(values.index.tolist(), values.values.tolist()):
        if value[0] == 1:
            print(key)
            data.append(key)

    print("Number of Entries", len(data))

    df = pd.DataFrame(data, columns=["pupil", "course", "group"])

    print(df)

    df["pupil_name"] = df["pupil"].apply(lambda p: pupils_names[int(p)])
    df["course_name"] = df["course"].apply(lambda c: courses_names[int(c)])
    df["group"] = df["group"].apply(int)

    print("Pupils in Group 1:", df[df["group"] == 1]["pupil_name"].unique())
    print("Pupils in Group 2:", df[df["group"] == 2]["pupil_name"].unique())

    print("Course and pupils per group")
    for cn in courses_names:
        print(f'{cn}: {len(df[(df["course_name"] == cn) & (df["group"] == 1)])} + {len(df[(df["course_name"] == cn) & (df["group"] == 2)])}')






