

class Nodo():
    def __init__(self, dado=None):
        self.__dado = dado
        self.__anterior = None
        self.__posterior = None
    
    @property
    def dado(self):
        return self.__dado
    
    @dado.setter
    def dado(self, dado):
        self.__dado = dado

    @property
    def anterior(self) -> 'Nodo':
        return self.__anterior
    
    @anterior.setter
    def anterior(self, anterior: 'Nodo'):
        self.__anterior = anterior

    @property
    def posterior(self) -> 'Nodo':
        return self.__posterior
    
    @posterior.setter
    def posterior(self, posterior: 'Nodo'):
        self.__posterior = posterior


class Cursor():
    def __init__(self):
        self.__nodo_atual = None
        self.__posicao = None
    
    @property
    def nodo_atual(self) -> Nodo:
        return self.__nodo_atual
    
    @nodo_atual.setter
    def nodo_atual(self, nodo: Nodo):
        self.__nodo_atual = nodo

    @property
    def posicao(self) -> Nodo:
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao: int):
        self.__posicao = posicao

    def avancar_k_posicoes(self, k:int):
        pass

    def retroceder_k_posicoes(self, k:int):
        pass

    def ir_para_o_primeiro(self):
        pass

    def ir_para_o_ultimo(self):
        pass


nodo = Nodo()
print(nodo.dado)
