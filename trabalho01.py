

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
        # vai para o primeiro nodo da lista
        if self.__lista.esta_vazia():
            self.__posicao = 0
            self.__nodo_atual = self.__lista.rabo   
        else:
            self.__posicao = 1
            self.__nodo_atual = self.__lista.cabeca.posterior

    def ir_para_o_ultimo(self):
        # vai para o ultimo nodo da lista
        if not self.__lista.esta_vazia():
            self.__posicao = self.__lista.tamanho
            self.__nodo_atual = self.__lista.rabo.anterior
        else:
            self.__posicao = 0
            self.__nodo_atual = self.__lista.cabeca

    def avancar_k_posicoes(self, k:int):
        # avanca k posicoes a partir da posicao atual
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
        # retrocede k posicoes a partir da posicao atual
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

    def acessar_atual(self) -> Nodo:
        # retorna o elemento atual sob o cursor
        return self.__cursor.nodo_atual
    
    def esta_vazia(self) -> bool:
        # verifica se a lista esta vazia
        return self.__tamanho == 0

    def __len__(self):
        # retorna o numero de elementos da lista
        return self.__tamanho

    def posicao_de(self, dado):
        # retorna a posicao e o nodo de um valor procurado na lista
        if not self.contem_dado(dado):
            return
        posicao = 1
        proximo_nodo = self.__cabeca.posterior
        while proximo_nodo.dado != None:
            if proximo_nodo.dado == dado:
                return posicao, proximo_nodo
            else:
                posicao += 1
                proximo_nodo = proximo_nodo.posterior

    def inserir_depois_de(self, dado, atual:Nodo):
        # inseri um novo elemento depois da posicao de um outro elemento
        self.__conta_id += 1
        posterior = atual.posterior
        novo_nodo = Nodo(id=self.__conta_id, dado=dado, anterior=atual, posterior=posterior)
        atual.posterior = novo_nodo
        posterior.anterior = novo_nodo
        self.__tamanho += 1
        self.__cursor.avancar_k_posicoes(1)
        
    def inserir_antes_de(self, dado, atual:Nodo):
        # inseri um novo elemento antes da posicao de um outro elemento
        self.__conta_id += 1
        anterior = atual.anterior
        novo_nodo = Nodo(id=self.__conta_id, dado=dado, anterior=anterior, posterior=atual)
        anterior.posterior = novo_nodo
        atual.anterior = novo_nodo
        self.__tamanho += 1
        self.__cursor.retroceder_k_posicoes(1)

    def inserir_depois_do_atual(self, dado):
        # inseri um novo elemento depois da posicao do elemento sob o cursor
        atual = self.acessar_atual()
        self.inserir_depois_de(dado, atual)

    def inserir_antes_do_atual(self, dado):
        # inseri um novo elemento antes da posicao do elemento sob o cursor
        atual = self.acessar_atual()
        self.inserir_antes_de(dado, atual)

    def inserir_por_primero(self, dado):
        # inseri um novo elemento no incio da lista
        self.__cursor.ir_para_o_primeiro()
        atual = self.acessar_atual()
        self.inserir_antes_de(dado, atual)

    def inserir_por_ultimo(self, dado):
        # inseri um novo elemento no fim da lista
        self.__cursor.ir_para_o_ultimo()
        atual = self.acessar_atual()
        self.inserir_depois_de(dado, atual)

    def inserir_na_posicao(self, posicao:int, dado):
        # inseri um novo elemento na posicao desejada
        self.__cursor.ir_para_o_primeiro()
        self.__cursor.avancar_k_posicoes(k=posicao-1)
        self.inserir_antes_do_atual(dado)
        self.__cursor.ir_para_o_primeiro()
        self.__cursor.avancar_k_posicoes(k=posicao-1)

    def deletar_nodo(self, nodo:Nodo):
        # deleta um nodo
        if self.esta_vazia():
            return
        anterior = nodo.anterior
        posterior = nodo.posterior
        anterior.posterior = posterior
        posterior.anterior = anterior
        self.__tamanho -= 1
        nodo.anterior = nodo.posterior = nodo.dado = None

    def deletar_atual(self):
        # deleta um nodo sob o cursor
        if self.esta_vazia():
            return
        atual = self.acessar_atual()
        self.deletar_nodo(atual)
        self.__cursor.ir_para_o_primeiro()

    def deletar_primeiro(self):
        # deleta o primeiro nodo da lista
        if self.esta_vazia():
            return
        self.__cursor.ir_para_o_primeiro()
        self.deletar_atual()

    def deletar_ultimo(self):
        # deleta o ultimo nodo da lista
        if self.esta_vazia():
            return
        self.__cursor.ir_para_o_ultimo()
        self.deletar_atual()

    def deletar_dado(self, dado):
        # deleta o nodo que contem o dado como valor
        if self.esta_vazia():
            return
        _, nodo = self.posicao_de(dado)
        if nodo:
            self.deletar_nodo(nodo)
            self.__cursor.ir_para_o_primeiro()

    def deletar_da_posicao(self, posicao):
        # deleta o nodo da posicao
        self.__cursor.ir_para_o_primeiro()
        self.__cursor.avancar_k_posicoes(k=posicao-1)
        self.deletar_atual()
        self.__cursor.ir_para_o_primeiro()

    def contem_dado(self, dado) -> bool:
        # verifica se a lista contem o dado
        proximo_nodo = self.__cabeca.posterior
        while proximo_nodo.dado != None:
            if proximo_nodo.dado == dado:
                return True
            else:
                proximo_nodo = proximo_nodo.posterior
        return False

    def imprimir_lista(self):
        # imprime a lista
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
    print(f'tamanho da lista: {len(lista)}') 
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_primero(7)
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_primero(6)
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_ultimo(12)
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_primero(4)
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.inserir_por_ultimo(-1)
    lista.imprimir_lista()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    lista.cursor.ir_para_o_primeiro()
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')

    print(f'Contem 5: {lista.contem_dado(5)}')
    print(f'Contem 7: {lista.contem_dado(7)}')
    lista.imprimir_lista()

    lista.inserir_na_posicao(3, 11)
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')
    lista.imprimir_lista()

    lista.deletar_da_posicao(4)
    print(f'Cursor atual: {lista.cursor.nodo_atual.dado}, posicao {lista.cursor.posicao}')
    lista.imprimir_lista()
