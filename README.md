# fair-groups
fair groups during the alterning home-schooling  / faire gruppen für den wechselunterricht

This tool enables schools to devide their classes in two equal groups.
The tool optimizes the courses to have almost equal sizes.

# Example

## Input

The input for this program is a csv-file with the columns course and pupils. The pupils are encoded as comma-separated list.

Example:
`pupils.csv`

```csv
course;pupils
course1;A,B,C,D,E,F
course2;A,B,C,G,H,I
course3;G,H,I,J,K,L
course4;A,G,I,D,E
```

## Output

```
Pupils in Group 1: ['A' 'C' 'F' 'I' 'K' 'L']
Pupils in Group 2: ['B' 'D' 'E' 'G' 'H' 'J']
Course and pupils per group
course1: 3 + 3
course2: 3 + 3
course3: 3 + 3
course4: 2 + 3
```

# Getting Started

Download ampl https://ampl.com/try-ampl/download-a-free-demo/

`pip install -r requirements.txt`

set path of ampl binary `export AMPL_PATH=/home/path/to/ampl/`

create `pupils.csv` (e.g. copy from `pupils.example.csv`)

`python main.py`



# Code

## Conditions

## Decision Variable

p: pupil

c: course

g: group
`x[p, c, g]`

## Optimization

- All new courses should have almost equal sizes.
- Group A and group B should have almost equal size.
