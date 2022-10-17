from math import *
from itertools import permutations, chain


'''
The three aspects of the time series behavior [value, trend, and seasonality] are expressed as three types of exponential smoothing, so Holt-Winters is called triple exponential smoothing. The model predicts a current or future value by computing the combined effects of these three influences.
The Class takes six positional arguments:
series : the list of values.
season_len : the number of values to complete one season.
alpha, beta, gamma : arbitrary numbers between 0 and 1.
npredict : number of predicted data.
Usage :
data = [0, 5, 3, 9, 8 ............ ]
pred = HoltWinters(series=data, season_len=25, alpha=0.5, beta=0.5, gamma=0.5, npredict=6)
print(pred.predict())
'''


class HoltWinters:
    r'''Holt-Winters triple smooth exponential method.'''
    def __init__(self, series, season_len, alpha, beta, gamma, npredict):
        self.series = series
        self.season_len = season_len
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.npredict = npredict


    # appling the equations of prediction
    def fit(self, series):
        beta = self.beta
        alpha = self.alpha
        gamma = self.gamma
        season_len = self.season_len
        seasonals = self._initial_seasonal(series)
        # initial values
        predictions = []
        smooth = series[0]
        trend = self._initial_trend(series)
        predictions.append(smooth)
        for i in range(1, len(series)):
            value = series[i]
            previous_smooth = smooth
            seasonal = seasonals[i % season_len]
            smooth = alpha * (value - seasonal) + (1 - alpha) * (previous_smooth + trend)
            trend = beta * (smooth - previous_smooth) + (1 - beta) * trend
            seasonals[i % season_len] = gamma * (value - smooth) + (1 - gamma) * seasonal
            predictions.append(smooth + trend + seasonals[i % season_len])
        self.trend_ = trend
        self.smooth_ = smooth
        self.seasonals_ = seasonals
        self.predictions_ = predictions
        return self.predictions_, self.seasonals_, self.smooth_, self.trend_


    # find the initial trend Coefficient
    def _initial_trend(self, series):
        season_len = self.season_len
        total = 0.0
        for i in range(season_len):
            total += (series[i + season_len] - series[i]) / season_len
        trend = total / season_len
        return trend


    # find the initial seasons Coefficients
    def _initial_seasonal(self, series):
        season_len = self.season_len
        n_seasons = len(series) // season_len
        season_averages = []
        for j in range(n_seasons):
            start_index = season_len * j
            end_index = start_index + season_len
            s_average = sum(series[start_index:end_index]) / season_len
            season_averages.append(s_average)
        # print(season_averages)
        seasonals = []
        seasons = range(n_seasons)
        index = [a * season_len for a in seasons]
        # print(index)
        for i in range(season_len):
            seasonal = sum([series[a + i] - j for a, j in zip(index, season_averages)]) / n_seasons
            seasonals.append(seasonal)
        # print(len(seasonals))
        return seasonals


    # prediction method
    def predict(self):
        predictions = self.fit(self.series)[0]
        original_series_len = len(self.series)
        for i in range(original_series_len, original_series_len + self.npredict):
            m = i - original_series_len + 1
            prediction = self.smooth_ + m * self.trend_ + self.seasonals_[i % self.season_len]
            predictions.append(prediction)
        return predictions


def linspace(start, stop, n):
    h = (stop - start) / (n - 1)
    x = []
    for i in range(n):
        y = start + h * i
        x.append(y)
    return x


def parameters(series, season_len, itr, n_p):
    r'''devide the series to training series and test series'''
    train, test = [], []
    n_seasons = len(series) / season_len
    n_train = None
    if int(n_seasons) == n_seasons : n_train = n_seasons - 1
    else: n_train = n_seasons - (n_seasons - int(n_seasons))
    # appending training series items
    for i in range(int(n_train) * season_len):
        train.append(series[i])
    # appending test series items
    for i in range (len(train), len(series), 1):
        test.append(series[i])
    # searching for Coefficients alpha, beta and gamma using iteration method
    mrs, exe = [], []
    # iterate over the space between 0 aand 1 using iter space
    its = linspace(0, 1, itr)
    pa = [i for i in permutations(its, 3)]
    for i in pa:
        c = HoltWinters(series=train, season_len=season_len, alpha=i[0], beta=i[1], gamma=i[2], npredict=len(test)+1)
        x = c.predict()
        exe.append(x)
    for i in range(len(exe)):
        dif = [a - b for a, b in zip(exe[i], series)]
        mrs.append(sqrt(sum([a**2 for a in dif])/len(dif)))
    # separate the values
    ind = mrs.index(min(mrs))
    npa = pa[ind]
    alp, bet, gam = npa[0], npa[1], npa[2]
    # separate the prediction
    p = HoltWinters(series=series, season_len=season_len, alpha=alp, beta=bet, gamma=gam, npredict=n_p)
    xx = p.predict()
    [xx.pop(0) for i in range(len(series))]
    # add the predictions to the original series
    series = list(chain(series, xx))
    return alp, bet, gam, xx, series

