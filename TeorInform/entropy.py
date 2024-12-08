from scipy.stats import entropy

P = [[5/250, 1/14, 1/14],
     [89/336, 0, 93/350],
     [5/240, 97/364, 5/240]]


print(sum(entropy(P)))