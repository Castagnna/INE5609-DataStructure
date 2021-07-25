

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
    def __init__(self, lista:'ListaEncadeada', nodo_atual:Nodo):
        self.__lista = lista
        self.__nodo_atual = nodo_atual
        self.__posicao = 0
    
    @property
    def nodo_atual(self) -> Nodo:
        return self.__nodo_atual
    
    @nodo_atual.setter
    def nodo_atual(self, nodo: Nodo):
        self.__nodo_atual = nodo

    @property
    def posicao(self) -> int:
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao: int):
        self.__posicao = posicao

    def ir_para_o_primeiro(self):
        if self.__lista.esta_vazia():
            self.__posicao = 0
            self.__nodo_atual = self.__lista.rabo   
        else:
            self.__posicao = 1
            self.__nodo_atual = self.__lista.cabeca.posterior

    def ir_para_o_ultimo(self):
        if not self.__lista.esta_vazia():
            self.__posicao = self.__lista.tamanho
            self.__nodo_atual = self.__lista.rabo.anterior
        else:
            self.__posicao = 0
            self.__nodo_atual = self.__lista.cabeca

    def avancar_k_posicoes(self, k:int):
        if self.__lista.esta_vazia():
            return
        if self.__posicao + k > self.__lista.tamanho:
            self.ir_para_o_ultimo()
            return

        contador = 0
        while contador < k:
            self.__posicao += 1
            contador += 1
            self.__nodo_atual = self.__nodo_atual.posterior

    def retroceder_k_posicoes(self, k:int):
        if self.__lista.esta_vazia():
            return
        if self.__posicao - k < 1:
            self.ir_para_o_primeiro()
            return
            
        contador = 0
        while contador < k:
            self.__posicao -= 1
            contador += 1
            self.__nodo_atual = self.__nodo_atual.anterior


class ListaEncadeada:
    def __init__(self) -> None:
        self.__conta_id = 0
        self.__tamanho = 0
        self.__cabeca = Nodo(id=0)
        self.__rabo = Nodo(id=-1)
        self.__cabeca.posterior = self.__rabo
        self.__rabo.anterior = self.__cabeca
        self.__cursor = Cursor(lista=self, nodo_atual=self.__cabeca)

    @property
    def cabeca(self) -> Nodo:
        return self.__cabeca

    @property
    def rabo(self) -> Nodo:
        return self.__rabo

    @property
    def cursor(self) -> Cursor:
        return self.__cursor

    @property
    def tamanho(self) -> int:
        return self.__tamanho
    
    def esta_vazia(self) -> bool:
        return self.__tamanho == 0

    def __len__(self):
        return self.__tamanho

    def inserir_depois_de(self, dado, atual:Nodo):
        self.__conta_id += 1
        posterior = atual.posterior
        novo_nodo = Nodo(id=self.__conta_id, dado=dado, anterior=atual, posterior=posterior)
        atual.posterior = novo_nodo
        posterior.anterior = novo_nodo
        self.__tamanho += 1
        self.__cursor.avancar_k_posicoes(1)
        
    def inserir_antes_de(self, dado, atual:Nodo):
        self.__conta_id += 1
        anterior = atual.anterior
        novo_nodo = Nodo(id=self.__conta_id, dado=dado, anterior=anterior, posterior=atual)
        anterior.posterior = novo_nodo
        atual.anterior = novo_nodo
        self.__tamanho += 1
        self.__cursor.retroceder_k_posicoes(1)

    def inserir_por_primero(self, dado):
        self.__cursor.ir_para_o_primeiro()
        atual = self.__cursor.nodo_atual
        self.inserir_antes_de(dado, atual)

    def inserir_por_ultimo(self, dado):
        self.__cursor.ir_para_o_ultimo()
        atual = self.__cursor.nodo_atual
        self.inserir_depois_de(dado, atual)

    def deletar_nodo(self, nodo:Nodo):
        if self.esta_vazia():
            return
        anterior = nodo.anterior
        posterior = nodo.posterior
        anterior.posterior = posterior
        posterior.anterior = anterior
        self.__tamanho -= 1
        nodo.anterior = nodo.posterior = nodo.dado = None

    def contem_dado(self, dado) -> bool:
        proximo_nodo = self.__cabeca.posterior
        while proximo_nodo.dado != None:
            if proximo_nodo.dado == dado:
                return True
            else:
                proximo_nodo = proximo_nodo.posterior
        return False

    def imprimir_lista(self):
        proximo_nodo = self.__cabeca.posterior
        contador = 0
        while proximo_nodo.dado != None:
            contador += 1
            dado = proximo_nodo.dado
            print(f'[{contador}º: {dado}] ', end='')
            proximo_nodo = proximo_nodo.posterior
            if contador > 10:
                break
        print()


if __name__ == '__main__':
    lista = ListaEncadeada()
    print(len(lista)) 
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_primero(7)
    print(len(lista))
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_primero(6)
    print(len(lista))
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_ultimo(12)
    print(len(lista))
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_primero(4)
    print(len(lista))
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_ultimo(-1)
    print(len(lista))
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.cursor.ir_para_o_ultimo()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    print(f'Contem 5: {lista.contem_dado(5)}')
    print(f'Contem 7: {lista.contem_dado(10)}')

    lista.imprimir_lista()
