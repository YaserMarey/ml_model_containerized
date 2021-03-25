import pickle

import numpy as np
import sklearn.datasets as datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def fit():
    house = datasets.load_boston()
    train_x, test_x, train_y, test_y = train_test_split(house.data, house.target, test_size=0.2, random_state=1)
    lr = LinearRegression()
    lr.fit(train_x, train_y)
    pickle.dump(lr, open('.\models\lr_reg_boston.p', 'wb'))
    return


def predict(x_to_predict):
    lm_pickled = pickle.load(open(".\models\lr_reg_boston.p", "rb"))
    result = lm_pickled.predict(np.reshape(x_to_predict, (1, -1)))
    return result

if __name__ == "__main__":
    fit()
    house_to_evaluate = [0.62739, 0., 8.14, 0., 0.538, 5.834, 56.5, 4.4986, 4., 307., 21., 395.62, 8.47]
    price = predict(house_to_evaluate)
    print(f"result of predciton of {house_to_evaluate} is {str(price[0])} 1000s USD")
