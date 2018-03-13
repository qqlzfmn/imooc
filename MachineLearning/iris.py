from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)
# list(iris.target_names)
