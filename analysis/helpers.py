import numpy as np

def my_train_test_split(dataframe, train_size=0.7, random_state=42):
	"""
	Separa um dataframe em dois. Análogo ao train_test_split do scikit-learn,
	mas usa dataframe
	"""

	np.random.seed(random_state)

	n = len(dataframe)
	n_trues = round(train_size * n)
	n_falses = n - n_trues

	mask_train = [True] * n_trues + [False] * n_falses
	np.random.shuffle(mask_train)

	mask_test = np.invert(mask_train)

	return dataframe[mask_train], dataframe[mask_test]

def train_test_split_masks(n_samples, train_size=0.7, random_state=42):
	"""
	Separa um dataframe em dois. Análogo ao train_test_split do scikit-learn,
	mas usa dataframe
	"""

	np.random.seed(random_state)

	n_trues = round(train_size * n_samples)
	n_falses = n_samples - n_trues

	mask_train = [True] * n_trues + [False] * n_falses
	np.random.shuffle(mask_train)

	mask_test = np.invert(mask_train)

	return mask_train, mask_test