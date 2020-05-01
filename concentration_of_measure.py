import numpy as np

n_dim = 1
for i in range(10):
	n_dim = 10**i
	r_list = []
	for _ in range(1000):
		s = np.random.normal(0, 1, n_dim)
		r = np.sqrt((s**2).mean())
		r_list.append(r)

	import matplotlib.pyplot as plt
	plt.hist(r_list, density=True, bins=30)
	plt.ylim(0, 150)
	plt.xlim(0, 2)
	plt.title(i)
	plt.show()