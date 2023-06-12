import matplotlib.pyplot as plt

import pymadng

madng=pymadng.MAD()
madng.loadfile("psb.mad")
madng.MADX.tw.x
plt.plot(madng.MADX.tw.s,madng.MADX.tw.x)
plt.plot(madng.MADX.tw.s,madng.MADX.tw.betx)
plt.plot(madng.MADX.tw.s,madng.MADX.tw.beta11)
plt.plot(madng.MADX.tw.s,madng.MADX.tw.beta22)
madng.MADX.tw.q1
madng.MADX.tw.q2
