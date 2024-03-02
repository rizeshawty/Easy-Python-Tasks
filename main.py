import matplotlib.pyplot as plt #для графиков
import scipy.stats as sps #для математических функций
import numpy as np #для базовых вычислений

massivchik = [
    30.050, 30.050, 30.100, 30.090, 30.140, 30.230,
    30.110, 30.150, 30.090, 30.130, 30.150, 30.070,
    30.130, 30.130, 30.170, 30.070, 30.110, 30.110,
    30.130, 30.150, 30.040, 30.150, 30.080, 30.130,
    29.970, 30.120, 30.110, 30.170, 30.030, 30.090,
    30.010, 30.190, 30.150, 30.110, 30.070, 30.090,
    30.110, 30.130, 30.090, 30.130, 30.130, 30.090,
    30.070, 30.210, 30.110, 30.070, 30.110,
    30.170, 30.120, 30.180, 30.090, 30.050
]

Srednearifm_X = np.mean(massivchik) #среднее арифмитическое
Srednekvad_Sx = np.std(massivchik) #среднеквадратичное отклонение
TochkiArray_N = len(massivchik) #кол-во точек в массиве
Bins_n = 10 #бины (размер синих столбцов в гистограмме)
Razmah = max(massivchik) - min(massivchik) #вычисление размаха для шагов разбиения
Steps_h = Razmah / Bins_n #шаги разбиения для теор.частоты

#p.s на 3, т.к в нормальном распределении 99.7% значений лежат в пределах трех среднеквадратических отклонений от среднего
DiapozonX_gauss = np.arange(Srednearifm_X - 3 * Srednekvad_Sx, Srednearifm_X + 3 * Srednekvad_Sx, 0.001) #диапазон по "X" (оранжевая линия от и до куда)

z_gauss = [float((i - Srednearifm_X) / Srednekvad_Sx) for i in DiapozonX_gauss] #массив аргументов функции Лапласа Z для плотности вероятности
PlotnostVeroyaJ_gauss = sps.norm.pdf(z_gauss) #j(z) - функция плотности вероятности (Лапласа)
Chastota_gauss = [float(TochkiArray_N * Steps_h / Srednekvad_Sx * i) for i in PlotnostVeroyaJ_gauss] #массив теоретической частоты
Veroyatnost_gauss = [float(i / TochkiArray_N) for i in Chastota_gauss] #массив теоретической вероятности

plt.hist(massivchik, bins=Bins_n, edgecolor='black', weights=np.ones_like(massivchik) / TochkiArray_N) #гистограмма (по значениям)
plt.plot(DiapozonX_gauss, Veroyatnost_gauss) #график по координатам
plt.show() #вывод