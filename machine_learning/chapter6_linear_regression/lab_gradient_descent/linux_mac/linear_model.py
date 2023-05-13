import numpy as np


class LinearRegressionGD(object):
    def __init__(self, fit_intercept=True, copy_X=True,
                            eta0=0.001, epochs=1000, weight_decay=0.9):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self._eta0 = eta0
        self._epochs = epochs

        self._cost_history = []

        self.theta = None
        self._coef = None
        self._intercept = None
        self._new_X = None
        self._w_history = []
        self._weight_decay = weight_decay

    def cost(self, h, y):
        return (1/(2*len(y))) * np.sum((h-y)**2)

    def hypothesis_function(self, X, theta):
        return X.dot(theta)

    def gradient(self, X, y, theta):
        m = len(y)
        predictions = self.hypothesis_function(X, theta)
        gradient = []

        # for i in range(theta.size):
        #     partial_marginal = X[:, i]
        #     errors_xi = (predictions - y) * partial_marginal
        #     gradient.append((1 / m) * errors_xi.sum())
        # return np.array(gradient)
        return (1 / m) * (X.dot(theta) - y).dot(X)

    def fit(self, X, y):
        self._new_X = X
        
        if self.fit_intercept == True:
            ones = np.ones(len(self._new_X)).reshape(-1, 1)
            self._new_X = np.concatenate((ones, self._new_X), axis=1)
        
        theta = np.ones(self._new_X.shape[1])

        for epoch in range(self._epochs):

            gradient = self.gradient(self._new_X, y, theta).flatten()
    
            theta = theta - self._eta0 * gradient

            if epoch % 100 == 0:
                self._w_history.append(theta)
                cost = self.cost(
                    self.hypothesis_function(self._new_X, theta), y)
                self._cost_history.append(cost)
            self._eta0 = self._eta0 * self._weight_decay

        self.theta = theta
        self.coef = theta[1:]
        self.intercept = theta[0]

        return self

    # 마지막
    def predict(self, X):
        if self.fit_intercept == True:
            ones = np.ones(len(X)).reshape(-1, 1)
            X = np.concatenate((ones, X), axis=1)
    
        return X.dot(self.theta)

    @property
    def coef(self):
        return self._coef
    
    @coef.setter
    def coef(self, value):
        self._coef = value

    @property
    def intercept(self):
        return self._intercept
    
    @intercept.setter
    def intercept(self, value):
        self._intercept = value

    @property
    def weights_history(self):
        return np.array(self._w_history)

    @property
    def cost_history(self):
        return self._cost_history
