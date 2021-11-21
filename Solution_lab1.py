from tabulate import tabulate
import numpy as np

matrix = np.loadtxt("sol_lab1_input.txt", dtype='i', delimiter=',')

minvals = [min(matrix[i]) for i in range(0, matrix.shape[1])]
maxvals = [max(matrix[i]) for i in range(0, matrix.shape[1])]
vald = max(minvals)

row_avg = [sum(matrix[i] / matrix.shape[0] for i in range(0, matrix.shape[1]))]
row_sum = [sum(matrix[i]) for i in range(0, matrix.shape[1])]
laplas = max(row_avg)

coef_opt = 0.7
hurviz = [0, 0, 0]
for i in range(0, matrix.shape[0]):
    hurviz[i] = coef_opt * minvals[i] + (1 - coef_opt) * maxvals[i]

p = [0.55, 0.3, 0.15]
R = [row_sum[i] * p[i] for i in range(0, matrix.shape[0])]
bayes_laplas = max(R)

print(tabulate(headers=["Можливі стани зовнішнього середовища", "Критерії"],
               tabular_data=[[tabulate(tabular_data=[[100, 80, 50], [90, 90, 70], [60, 70, 80]],
                                       headers=["Конкуренція на тому ж рівні", "Конкуренція трішки посилилась",
                                                "Конкуренція різко посилилась"]
                                       ),
                              tabulate(headers=["Вальда", "Максимальний", "Гурвіца", "Лапласа"],
                                       tabular_data=[[minvals[0], round(laplas[0]), round(hurviz[0], 3), R[0]],
                                                     [minvals[1], round(laplas[1]), round(hurviz[1], 3), R[1]],
                                                     [minvals[2], round(laplas[2]), round(hurviz[2], 3), R[2]]])],
                             ]))

print("\nМожливі альтернативні рішення: \n"
      "\tПродовжити роботу в звичному режим;\n"
      "\tАктивувати рекламну діяльність;\n"
      "\tАктивувати рекламу і знизити ціну.\n"
      )

print("Результати обрахунку: \n"
      f"\tкритерій Вальда: {vald}, стратегія №{np.where(minvals == vald)[0] + 1}\n"
      f"\tкритерій Лапласа: {round(max(laplas), 3)}, стратегія №{np.where(laplas == max(laplas))[0] + 1}\n"
      f"\tкритерій Гурвіца: {round(max(hurviz), 3)}, стратегія №{np.where(hurviz == max(hurviz))[0] + 1}\n"
      f"\tкритерій Байеса-Лапласа: {round(bayes_laplas, 3)}, стратегія №{np.where(R == bayes_laplas)[0] + 1}"
      )
