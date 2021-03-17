from Estudo.Python.Classes.Trabalho import *

class Funcionario:
    trabalho = Trabalho
    def __init__(self,nome, trabalho):
        self.trabalho = trabalho
        self.nome = nome

    def getNome(self):
        return self.nome

    def getTrabalho(self):
        return self.trabalho.getArea()

    def calcularSalario(self):
        self.salario = self.trabalho.getHora()*self.trabalho.getValorHora()
        return self.salario
        
