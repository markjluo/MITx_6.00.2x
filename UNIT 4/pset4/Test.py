import numpy as np
import matplotlib.pyplot as plt
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

INTERVAL_1 = list(range(1961, 2006))
INTERVAL_2 = list(range(2006, 2016))


class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """

    def __init__(self, filename):
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature

        f.close()

    def get_yearly_temp(self, city, year):
        """
        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]


def generate_models(x, y, degs):
    result = []
    for deg in degs:
        model = np.polyfit(x, y, deg)
        result.append(model)
    return result


# print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2]))


def r_squared(y, estimated):
    sst = 0
    ssr = 0
    mean_y = sum(y)/len(y)
    for e in range(len(y)):
        ssr += (y[e] - estimated[e])**2
        sst += (y[e] - mean_y)**2
    r_sq = 1 - ssr/sst
    return r_sq


def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    for model in models:
        y_est = np.polyval(model, x)
        r_sq = r_squared(y, y_est)

        plt.plot(x, y, 'bo')
        plt.plot(x, y_est, color='r', label=str(len(model)-1)+'st degree polynomial' + '\n' + 'R^2 = ' + str(round(r_sq, 4)))
        plt.title('Temp vs Year')
        plt.xlabel('Year')
        plt.ylabel('Temp (Celsius)')
        plt.legend(loc='best')
        plt.show()


raw_data = Climate('data.csv')
# y = []
# x = INTERVAL_1
# for year in INTERVAL_1:
#     y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
# models = generate_models(x, y, [1])
# evaluate_models_on_training(x, y, models)


x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
for year in x1:
    y.append(raw_data.get_yearly_temp('BOSTON', year).mean())
models = generate_models(x1, y, [1])
evaluate_models_on_training(x1, y, models)
