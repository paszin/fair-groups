# fair-groups
fair groups during the alterning home-schooling  / faire gruppen für den wechselunterricht


# Input

pupils.csv

```csv
course;pupils
course1;A,B,C,D,E,F
course2;A,B,C,G,H,I
course3;G,H,I,J,K,L
```

# Data Conversion

`course_lookup[course, pupil] binary`


# Conditions

- Every course is split into two courses. (sum of every course is equals 2)
- Every course exists in group A and group B (sum of every course in group A is equals 1, (same for group B))
- Every pupil belongs to group A or group B. (sum of pupils is equals number of pupils?)
- Every pupils belongs to its course (sum equals to lookup)


# Decision Variable

p: pupil

c: course

g: group
`x[p, c, g]`

# Optimization

- All new courses should have almost equal sizes.
- Group A and group B should have almost equal size.
