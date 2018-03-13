from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
print(digits.data.shape)
print(digits.target.shape)
print(digits.images.shape)
plt.matshow(digits.images[0])
plt.show()
