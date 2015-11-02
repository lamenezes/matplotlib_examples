from matplotlib import pyplot as plt

languages_fics = [
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
languages_fics = [lf for lf in languages_fics if lf[1] > 100]

languages = [language for language, _ in languages_fics]
fics_count = [count for _, count in languages_fics]

# figure size 800x850
plt.figure(figsize=(8, 8.5), dpi=100)

plt.axis([0, 15, 0, 570000])

rects = plt.bar([i + 0.1 for i, _ in enumerate(languages)], fics_count)
plt.ylabel('# fics')
plt.title('Quantidade de Fanfics de Harry Potter por idioma (fonte: fanfiction.net)')
plt.xticks([i + 0.5 for i, _ in enumerate(languages)], languages, rotation='vertical')

# plot actual value above each bar
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2., height + 10,
             '{}'.format(height), ha='center', va='bottom', size=10)

plt.rc("font", size=10)
plt.savefig('a.png')
