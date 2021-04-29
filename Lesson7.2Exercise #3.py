# Given a 5 element tuple: (4, 30, 2017, 2, 27). Using the string formating print: '2 27 2017 4 30'

numbers=(4, 30, 2017, 2, 27)
print("{n[3]} {n[4]} {n[2]} {n[0]} {n[1]}".format(n=numbers))