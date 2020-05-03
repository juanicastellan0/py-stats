from correlation import Correlation


def ej1():
    busy_people = [1, 2, 3, 4, 5]
    task_duration = [8, 7, 5, 5, 2]
    correlation = Correlation(
        'Diagrama de dispersión \nde duración de la tarea según el número de personas ocupadas',
        {'xlabel': 'Personas ocupadas', 'ylabel': 'Duración de la tarea'}
    )
    correlation.set_data(busy_people, task_duration)
    correlation.calc_corr_values_and_conclude()
    correlation.show_plot(6, 10)


def ej2():
    costs = [11, 10, 14, 13, 12, 20, 21, 15, 22, 18, 19, 16]
    sales = [19, 15, 20, 14, 16, 33, 32, 18, 29, 22, 23, 20]
    correlation = Correlation(
        'Diagrama de dispersión de las ventas según los costos',
        {'xlabel': 'Costos', 'ylabel': 'Ventas'}
    )
    correlation.set_data(costs, sales)
    correlation.calc_corr_values_and_conclude()
    correlation.show_plot(25, 35)


def ej3():
    people_with_high_pressure = [15, 13, 10, 27, 20, 5, 8, 31, 78, 22]
    over_weight = [75, 86, 88, 125, 75, 30, 47, 150, 114, 68]
    correlation = Correlation(
        'Diagrama de dispersión \nde cantidad de personas con presión arterial alta según el sobrepeso',
        {'xlabel': 'Cantidad de personas con presión alta', 'ylabel': 'Sobrepeso'}
    )
    correlation.set_data(people_with_high_pressure, over_weight)
    correlation.calc_corr_values_and_conclude()
    correlation.show_plot(100, 160, 20, 5)


def ej5():
    math = [6, 4, 8, 5, 6, 7, 5, 10, 5, 4]
    music = [2, 5, 5, 6, 7, 6, 7, 9, 10, 10]
    correlation = Correlation(
        'Diagrama de dispersión \nde las notas de 10 alumnos en matemática y en música',
        {'xlabel': 'Notas de matemática', 'ylabel': 'Notas de música'}
    )
    correlation.set_data(math, music)
    correlation.calc_corr_values_and_conclude()
    correlation.show_plot(10, 10)


ej1()
ej2()
ej3()
ej5()
