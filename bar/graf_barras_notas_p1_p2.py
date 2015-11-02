import random

from matplotlib import pyplot as plt

alunos = ['A{}'.format(i) for i in range(11)]
num_alunos = range(len(alunos))
notas_p1 = [random.randrange(3, 11) for _ in range(11)]
notas_p2 = [random.randrange(3, 11) for _ in range(11)]

width = .3

plt.bar(num_alunos, notas_p1, width, color='y')
plt.bar([n + width for n in num_alunos], notas_p2, width, color='b')
plt.ylabel('Notas')
plt.title('Notas dos alunos nas P1 e P2')
plt.xticks([n + width for n in num_alunos], alunos)
plt.axis([0, 11, 0, 11])
plt.savefig('b.png')
