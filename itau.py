class Fluxo:
    def __init__(self,data, valor):
        self.data = data
        self.valor = valor

json = {'fluxo': [{'data':'14/03/2021', 'valor':2}, {'data':'23/03/1999', 'valor':3}, {'data':'29/03/1965', 'valor':3}]}

ArrayFluxo = []
fluxoCluster = json['fluxo']

def teste_fluxo():
    for i in range(len(fluxoCluster)):
        fluxo = Fluxo(fluxoCluster[i]['data'], fluxoCluster[i]['valor'])
        ArrayFluxo.append(fluxo)
        vetor = ArrayFluxo

    for i in range(len(vetor)):
        if vetor[i].data == json['fluxo'][i]['data']:
            return True
        else:
            return False

print(teste_fluxo())
