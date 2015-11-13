"""
This script plots a bar chart that shows the amount of Harry Potter
fanfics written by language.

The data has been taken from http://fanficton.net
"""

from matplotlib import pyplot as plt

data = [
    ('Norwegian', 51), ('Japanese', 10), ('Dutch', 850), ('Filipino', 26),
    ('Finnish', 201), ('Danish', 87), ('Portuguese', 22778), ('Bulgarian', 16),
    ('French', 44265), ('Catalan', 64), ('Croatian', 13), ('Latin', 25),
    ('Hebrew', 77), ('Hungarian', 572), ('Hindi', 2), ('Chinese', 164),
    ('Romanian', 16), ('Slovak', 40), ('Indonesian', 2906), ('Estonian', 3),
    ('Greek', 30), ('Farsi', 3), ('Korean', 14), ('Afrikaans', 6), ('Arabic', 6),
    ('Czech', 380), ('Malay', 3), ('Spanish', 49785), ('English', 550206), ('Albanian', 3),
    ('Esperanto', 10), ('Devanagari', 2), ('Polish', 2681), ('Serbian', 4),
    ('Swedish', 951), ('Russian', 851), ('Turkish', 48), ('Italian', 628), ('Icelandic', 6),
    ('German', 13488), ('Vietnamese', 62)
]
fics_by_language = [row for row in data if row[1] > 100]

languages = [language for language, _ in fics_by_language]
languages_nums = [i + 0.1 for i in range(len(languages))]

fics = [count for _, count in fics_by_language]

# set figure size 800x850
plt.figure(figsize=(8, 8.5), dpi=100)

# set x range from 0 to 15 and y range from 0 to 570,000
plt.axis([0, 15, 0, 570000])

rects = plt.bar(languages_nums, fics)
plt.ylabel('# fics')
plt.title('Harry Potter fanfics by language (font: http://fanfiction.net)')

# set x label as the languages. adds 0.5 space between each language
language_nums = [i + 0.5 for i in languages_nums]
plt.xticks(language_nums, languages, rotation='vertical')

# plot actual value above each bar
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2., height + 10,
             '{}'.format(height), ha='center', va='bottom', size=10)

# set font size to 10
plt.rc("font", size=10)

# save chart to fics.png
plt.savefig('fics.png')
