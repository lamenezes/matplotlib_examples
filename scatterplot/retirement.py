from collections import OrderedDict
import csv
from matplotlib import pyplot as plt

labels = []
years = []
benefits_by_year = OrderedDict()

with open('retirement.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # throws out the CSV header
    for year, type, total_years, gender, _, _, _, benefit in reader:
        benefit = benefit.replace(',', '.')

        # if the year is not in the dictionary adds it with a default value of 0
        benefits_by_year.setdefault(year, 0)
        benefits_by_year[year] += float(benefit)

    years = benefits_by_year.keys()
    benefits = benefits_by_year.values()
    plt.scatter(years, benefits)

    # set the chart title
    plt.title('Retirement benefit (k R$) over the years')

    plt.xlabel('Year')
    # shows all the years from 1996 to 2014, displaying them vertically
    plt.xticks(range(1996, 2014), rotation='vertical')

    plt.ylabel('Total benefit (k R$)')

    plt.savefig('retirement_expenses.png')
