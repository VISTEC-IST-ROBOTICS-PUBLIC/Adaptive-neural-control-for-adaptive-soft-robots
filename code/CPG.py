
import math
from matplotlib import pyplot as plt

class CPG():
    def __init__(self,WeightH1_H1 = 1.4,WeightH2_H2 = 1.4,BiasH1 = 0.0,BiasH2 = 0.0,MI = 1.1):
        self.MI = MI
        self.WeightH1_H1 = WeightH1_H1
        self.WeightH2_H2 = WeightH2_H2
        self.BiasH1 = BiasH1
        self.BiasH2 = BiasH2
        self.activityH1 = 0
        self.activityH2 = 0
        self.WeightH1_H2 = 0.18 + self.MI
        self.WeightH2_H1 = -(0.18 + self.MI) 
        self.outputH1 = 0.01
        self.outputH2 = 0.01

    def _update(self,mi):
        self.WeightH1_H2 = 0.18 + mi
        self.WeightH2_H1 = -(0.18 + mi) 

        self.activityH1 = self.WeightH1_H1 * self.outputH1 + self.WeightH1_H2 * self.outputH2 + self.BiasH1
        self.activityH2 = self.WeightH2_H2 * self.outputH2 + self.WeightH2_H1 * self.outputH1 + self.BiasH2

        self.outputH1 = math.tanh(self.activityH1)
        self.outputH2 = math.tanh(self.activityH2)

        return self.outputH1

if __name__ == '__main__':
    cpg = CPG()
    data =[]
    for i in range(100):
        data1 = cpg._update()
        data.append(data1)
    plt.plot(data)
    plt.show()