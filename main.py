import math


def arithmetic_mean(x):
    return sum(x) / len(x)


def arithmetic_mean_square(x):
    return sum([_ ** 2 for _ in X]) / len(x)


def variance(mean, mean_square, n):
    return mean_square - mean ** 2


def standart_deviation(d, n):
    return math.sqrt(n / (n - 1) * d)


def quantile():
    return 1.796


def normal_distribution():
    return 2.575


def ans(res):
    return str(round(res, 3))


X = [9.5, 9.5, 11.2, 10.6, 9.9, 11.1, 10.9, 9.8, 10.1, 10.2, 10.9, 11]
confidence_level = 0.9
n = len(X)
mean = arithmetic_mean(X)
mean_square = arithmetic_mean_square(X)
d = variance(mean, mean_square, n)
s = standart_deviation(d, n)
print("Задание 1")
print(*X)
print("n =", n)
print("Доверительная вероятность:", confidence_level)
print()
print("Σxi/n =", ans(mean))
print("Σx²i =", ans(mean_square))
print("D =", ans(d))
print("σ =", ans(s))
print("(1+y)/2 =", (1 + confidence_level) / 2, "  t₀.₉₅(" + str(n - 1) + ") =", quantile())
print(ans(mean), " - ", quantile(), " * ", ans(s), "/√", n, " < m < ", ans(mean), " + ", quantile(),
      " * ", ans(s), "/√", n, sep="")
print("Доверительный интервал: ", ans(mean - quantile() * s / math.sqrt(n)), "< m <",
      ans(mean + quantile() * s / math.sqrt(n)))
print("\n")

n = 100
confidence_level = 0.99
xsum = 76
s = 12
mean = xsum / n
print("Задание 2")
print("n =", n, " Σxi =", xsum, "σ =", s)
print("Доверительная вероятность:", confidence_level)
print("Σxi/n =", ans(mean))
print("t = (1+y)/2 =", (1 + confidence_level) / 2, " Ф(t) =", (1 + confidence_level) / 2, " t =",
      normal_distribution())
print(ans(mean), " - ", normal_distribution(), " * ", ans(s), "/√", n, " < m < ", ans(mean), " + ",
      normal_distribution(),
      " * ", ans(s), "/√", n, sep="")
print("Доверительный интервал: ", ans(mean - normal_distribution() * s / math.sqrt(n)), "< m <",
      ans(mean + normal_distribution() * s / math.sqrt(n)))
