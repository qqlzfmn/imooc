from sklearn.datasets import load_boston

boston = load_boston()
print(boston.data.shape)
data, target = load_boston(return_X_y=True)  # return_X_y=True 参量返回表示是否返回 target（即价格），默认为 False，只返回 data（即属性）
print(data.shape)
print(target.shape)
