from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


class Correlation:
    plot_labels = {
        'xlabel': '',
        'ylabel': '',
    }
    x_data = []
    y_data = []
    pearsonr = 0
    cov = 0
    det_percentage = 0

    def __init__(self, plot_title='', plot_labels=dict):
        self.plot_title = plot_title
        self.plot_labels = plot_labels
        self.corr_sense = ''
        self.corr_type = ''
        self.str_corr_values = ''

    def set_data(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data

    def calc_corr_values_and_conclude(self):
        self.cov = round(np.cov(self.x_data, self.y_data)[0, 1], 3)
        self.corr_sense = 'directa' if self.cov > 0 else 'inversa'

        self.pearsonr = round(stats.pearsonr(self.x_data, self.y_data)[0], 3)
        self.corr_type = self.get_corr_type(self.pearsonr)

        self.det_percentage = round(self.pearsonr ** 2 * 100, 2)

    def show_plot(self, max_x, max_y, concl_x=0.2, concl_y=0.2):
        plt.title(self.plot_title)
        plt.xlabel(self.plot_labels['xlabel'])
        plt.ylabel(self.plot_labels['ylabel'])
        plt.plot(self.x_data, self.y_data, 'ro')
        plt.text(concl_x, concl_y, ' covarianza = ' + str(self.cov) + ' -> Relación ' + self.corr_sense +
                 '\n pearson r = ' + str(self.pearsonr) + ' -> Relación lineal ' + self.corr_type +
                 '\n bondad de ajuste: ' + str(self.det_percentage) + '% de los datos de ' + self.plot_labels['ylabel'] +
                 '\n están totalmente correlacionados con \n los datos de ' + self.plot_labels['xlabel'])
        plt.axis([0, max_x, 0, max_y])
        plt.grid(True)
        plt.show()

    @staticmethod
    def get_corr_type(coefficient):
        if coefficient == 1:
            return 'positiva perfecta'
        if .66 < coefficient < 1:
            return 'positiva intensa'
        if .33 < coefficient < .66:
            return 'positiva moderada'
        if 0 < coefficient < .33:
            return 'positiva débil'
        if -.33 < coefficient < 0:
            return 'negativa débil'
        if -.66 < coefficient < -.33:
            return 'negativa moderada'
        if -1 < coefficient < -.66:
            return 'negativa intensa'
        if coefficient == -1:
            return 'negativa perfecta'
        return
