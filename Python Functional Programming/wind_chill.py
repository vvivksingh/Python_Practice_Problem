import math


def calculateTemp_speed(v, t):
    """

    :param v: the wind speed v (in miles per hour),
    :param t:the temperature t (in Fahrenheit)
    :return: the wind chill using formula defined by National Weather services :
    wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    """
    wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print('the windchill index is:', wind_chill)


v = float(input("Input wind speed in km/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
calculateTemp_speed(v, t)