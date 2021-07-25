

class Nodo:
    def __init__(self, id:int, dado=None, anterior=None, posterior=None):
        self.__id = id
        self.__dado = dado
        self.__anterior = anterior
        self.__posterior = posterior

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
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


class Cursor:
    def __init__(self, nodo_atual = None):
        self.__nodo_atual = nodo_atual
        self.__posicao = -1
    
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


class ListaEncadeada:
    def __init__(self) -> None:
        self.__conta_id = 0
        self.__tamanho = 0
        self.__cabeca = Nodo(id=0)
        self.__rabo = Nodo(id=-1)
        self.__cabeca.posterior = self.__rabo
        self.__rabo.anterior = self.__cabeca
        self.__cursor = Cursor(nodo_atual=self.__rabo)
    
    def esta_vazia(self) -> bool:
        return self.__tamanho == 0

    def __len__(self):
        return self.__tamanho

    def inserir_depois_de(self, dado, anterior:Nodo):
        self.__conta_id += 1
        posterior = anterior.posterior
        novo_nodo = Nodo(id=self.__conta_id, dado=dado, anterior=anterior, posterior=posterior)
        anterior.posterior = novo_nodo
        posterior.anterior = novo_nodo
        self.__tamanho += 1

    def inserir_antes_de(self, dado, posterior:Nodo):
        self.__conta_id += 1
        anterior = posterior.anterior
        novo_nodo = Nodo(id=self.__conta_id, dado=dado, anterior=anterior, posterior=posterior)
        anterior.posterior = novo_nodo
        posterior.anterior = novo_nodo
        self.__tamanho += 1

nodo = Nodo()
print(nodo.dado)
