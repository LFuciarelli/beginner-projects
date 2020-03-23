import matplotlib.pyplot as plt


def y(r1, x1):
    """
    :param r1: growth rate r
    :param x1: percentage of the maximum (expressed in decimals) x
    :return: xn+1
    """
    return r1*x1*(1-x1)


r = 0
x = 0.5
track_list_ex = list()
track_list_r = list()
while r <= 4:
    for t in range(0, 400):
        x = y(r, x)
        if t > 335:                     # Allows you to visualize some of the bifurcations (399 - 64 = 335)
            track_list_ex.append(x)     # When r is around 3, the function y() will return two significantly different
            track_list_r.append(r)      # results in t == 348 and t == 349. This causes one bifurcation at this point.
    r += 0.01                           # When r is around 3.5 the same happens, but with y() returning 4 different
    x = 0.5                             # points depending on t and causing 2 bifurcations and so on.

plt.plot(track_list_r, track_list_ex, marker='x', linestyle="None")

plt.xlabel('growth rate')
plt.ylabel('equilibrium population')

plt.title('Period-doubling bifurcation')

plt.show()
