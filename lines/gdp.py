"""
This script generates a chart containing the GDP (Gross Domestic Product)
of some brazilian states.

The data has been extracted from DataSUS: http://www2.datasus.gov.br/DATASUS/index.php
"""

import csv
from matplotlib import pyplot as plt

# {'SP': ([gdp], [years])
with open('gdp_brasil_2000_to_2012.csv') as csvfile:
    rows = list(csv.reader(csvfile, delimiter=';'))
    # remove year from each row
    gdps_by_year = rows[1:]
    states = rows[0][1:]
    years = range(2000, 2013)

    # replace , for . (from 1001,10 to 1000.10)
    gdps_by_year = [map(lambda x: x.replace(',', '.'), gdps[1:]) for gdps in gdps_by_year]
    # transpose the rows, so we can have each row containing the state gdp
    # over the years
    gdps_by_state = list(map(list, zip(*gdps_by_year)))
    # put the data in a dict
    gdps_by_state = {state: gdps_year for state, gdps_year in zip(states, gdps_by_state)}
    selected_states = ('ES', 'SP', 'RJ', 'MG', 'PR', 'BA')
    selected_gdps = {state: gdps_year for state, gdps_year in gdps_by_state.items()
                     if state in selected_states}
    line_styles = ('g-', 'b:', 'r-', 'c:', 'm-', 'k:')
    for line_style, state, row in zip(line_styles, selected_gdps.keys(), selected_gdps.values()):
        plt.plot(years, row, line_style, label=state)
    plt.legend(loc=9)
    plt.xlabel('Years')
    plt.title('GPD (in millions) of brazilian states from 2000 to 2012')
    plt.savefig('gdp.png')
