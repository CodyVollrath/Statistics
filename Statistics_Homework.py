import math
class StatisticsHomework:

    def __init__(self, n: int, mean : float, standard_deviation: float, confidence: float):
        ZCMap = {
            0.70 : 1.04,
            0.75 : 1.15,
            0.80 : 1.28,
            0.85 : 1.44,
            0.90 : 1.645,
            0.92 : 1.75,
            0.95 : 1.96,
            0.96 : 2.05,
            0.98 : 2.33,
            0.99 : 2.58
        }

        self.__n = n
        self.__mean = mean
        self.__standard_deviation = standard_deviation
        self.__zc = ZCMap[confidence]
    
    def answerPartA(self):
        e = self.__calculate_e(self.__zc, self.__standard_deviation, self.__n)
        min = self.__mean - e
        max = self.__mean + e
        print(f'Lower Limit: {min}\nUpper Limit: {max}\nMargin of Error: {e}\n')

    def answerPartD(self, e):
        n = self.__calculate_n(self.__zc, self.__standard_deviation, e)
        print(f'Number of elements: {n}')
    
    def __calculate_n(self, zc, standard_deviation,e):
        internal_function = (zc * standard_deviation)/e
        return round(pow(internal_function,2))
    
    def __calculate_e(self,zc,standard_deviation,n):
        return round((zc*standard_deviation)/math.sqrt(n),2)

test = StatisticsHomework(n = 45, mean = 6.88, standard_deviation = 1.998, confidence = 0.90)
test.answerPartA()
test.answerPartD(0.35)
