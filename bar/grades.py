"""
This script creates a bar chart that shows the grades students in two tests.
"""

import random

from matplotlib import pyplot as plt

# generate students labels
students = ['S{}'.format(i) for i in range(11)]
students_numbers = range(len(students))

# generate grades
grades_test1 = [random.randrange(3, 11) for _ in range(11)]
grades_test2 = [random.randrange(3, 11) for _ in range(11)]

width = .3

# plot grades on first test
rects_grades_1 = plt.bar(students_numbers, grades_test1, width, color='y')

# adds a space so the bars a displayed side-by-side
padded_numbers = [n + width for n in students_numbers]

# plot grades on second test
rects_grades_2 = plt.bar(padded_numbers, grades_test2, width, color='b')
# set x-axis from 0 to 11. y-axis from 0 to 11
plt.axis([0, 11, 0, 11])

plt.ylabel('Grades')
plt.ylabel('Students')
plt.title('Students grades on Test 1 and 2')

# displays legend
plt.legend((rects_grades_1[0], rects_grades_2[0]), ('Test 1', 'Test 2'))

# display students labels
plt.xticks(padded_numbers, students)

# display all grades values
plt.yticks(range(11))

plt.savefig('grades.png')
