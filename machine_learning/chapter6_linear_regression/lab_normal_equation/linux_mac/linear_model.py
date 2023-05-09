import numpy as np

class LinearRegression(object):
    def __init__(self, fit_intercept=True, copy_X=True):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X

        self._w_hat = None
        self._coef = None
        self._intercept = None
        self._new_X = None

    def fit(self, X, y):
        self._new_X = X

        if self.fit_intercept == True:
            ones = np.ones(len(self._new_X)).reshape(-1, 1)
            self._new_X = np.concatenate((ones, self._new_X), axis=1)
        
        XTX_inverse = np.linalg.inv(self._new_X.T.dot(self._new_X))
        w_hat = XTX_inverse.dot(self._new_X.T).dot(y)

        self._w_hat = w_hat
        self._coef = w_hat[1:]
        self._intercept = w_hat[0]
        
        return self

    def predict(self, X):
        if self.fit_intercept == True:
            ones = np.ones(len(X)).reshape(-1, 1)
            X = np.concatenate((ones, X), axis=1)
        
        return X.dot(self._w_hat)

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

