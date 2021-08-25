

class Node:
    def __init__(self, value = None):
        if isinstance(value, int):
            self.value = value
        else:
            print('value not Int (2)')
        self.left_child = None
        self.right_child = None
        self.parent = None # aponta para o pai do No
        self.height = 1 # a altura do no na arvore


class AVLTree:
    
    def __init__(self):
        self.root = None

    def insert(self, value:int):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value:int, cur_node:Node):

        # se o valor a ser inserido for menor que o valor do no atual,
        if value < cur_node.value:
            # e se estiver vazia a posição esquerda do no atual, inseri na esquerda
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
                # apos inserir o novo no eh preciso verificar o balanceamento da arvore
                self._inspect_insertion(cur_node.left_child)

            # se nao, repete o processo com o elemento esquerdo do no atual
            else:
                self._insert(value, cur_node.left_child)

        # se o valor a ser inserido for maior que o valor do no atual, guarda na direita   
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)

        # se o valor nao for nem menor nem maior, então é o igual ao valor do no atual
        else:
            print("Value already in tree!")

    def _inspect_insertion(self, cur_node:Node, node_path = []):
        
        if cur_node.parent == None:
            return
        
        # lista que acumula o caminho dos nodos da folha até a raiz
        # [raiz, ... z, x, y, ...folha]
        node_path = [cur_node] + node_path

        left_height = self._get_height(cur_node.parent.left_child)
        right_height = self._get_height(cur_node.parent.right_child)

        # se o absoluto da diferenca entre a arvore a esquera e a direita do no atual for maior que 1
        # é preciso rebalancear
        if abs(left_height - right_height) > 1:
            node_path = [cur_node.parent] + node_path
            self._rebalance_node(
                node_z=node_path[0],
                node_y=node_path[1],
                node_x=node_path[2],
            )
            return

        # se não for preciso rebalancear, então vamos atualizar a altura do no pai
        new_parent_height = 1 + cur_node.height 

        if new_parent_height > cur_node.parent.height:
            cur_node.parent.height = new_parent_height

        # vamos continuar esse processo recursivamente até a raiz
        self._inspect_insertion(cur_node.parent, node_path)

    def _get_height(self, cur_node:Node):
        
        if cur_node == None:
            return 0
        
        return cur_node.height

    def _rebalance_node(self, node_z:Node, node_y:Node, node_x:Node):

        # LEFT LEFT CASE: se o filho esquerdo de Z for Y, e o filho esquerdo de Y for X,
        # então faz uma rotacao direita em Z
        if node_z.left_child == node_y and node_y.left_child == node_x:
            self._right_rotate(node_z)

        # LEFT RIGHT CASE: se o filho esquerdo de Z for Y, e o filho direito de Y for X,
        # então faz uma rotacao esquerda em Y e rotação direita em Z
        elif node_z.left_child == node_y and node_y.right_child == node_x:
            self._left_rotate(node_y)
            self._right_rotate(node_z)

        # RIGHT RIGHT CASE: se o filho direito de Z for Y, e o filho direito de Y for X,
        # então faz uma rotacao esquera em Z
        elif node_z.right_child == node_y and node_y.right_child == node_x:
            self._left_rotate(node_z)

        # RIGHT LEFT CASE: se o filho direito de Z for Y, e o filho esquerdo de Y for X,
        # então faz uma rotacao direita em Y e rotação esquerda em Z
        elif node_z.right_child == node_y and node_y.left_child == node_x:
            self._right_rotate(node_y)
            self._left_rotate(node_z)

        else:
            raise Exception('_rebalance_node: z, y, x node configuration not recognized!')

    def _left_rotate(self, node_z:Node):
        # 1) guarda o pai de Z
        z_parent = node_z.parent

        # 2) cria um no Y que é o filho direito de Z
        node_y = node_z.right_child

        # 3) Cria um nó auxiliar T2 que recebe o filho esquerdo de Y
        node_t2 = node_y.left_child

        # 4) Faz filho esquerdo de Y receber o no Z
        node_y.left_child = node_z

        # 5) O novo pai de Z vira Y
        node_z.parent = node_y

        # 6) O filho direito de Z recebe a arvore 2
        node_z.right_child = node_t2

        # 7) Caso o a arvore 2 não seja nula, seu pai é Z
        if node_t2 != None:
            node_t2.parent = node_z

        # 8) O novo pai de Y recebe o antigo pai de Z
        node_y.parent = z_parent

        # 9) Se o pai de Y for Nulo então ele é a raiz da arvore
        if node_y.parent == None: 
            self.root = node_y

        # 10) Se não, se por acaso o filho esquerdo do pai de Y for Z, ajustar para Y
        elif node_y.parent.left_child == node_z:
            node_y.parent.left_child = node_y

        # 11) Se não, o filho direito do pai de Y deve ser Y
        else:
            node_y.parent.right_child = node_y

        # a nova altura do nó será: 1 + a maior altura dentre os seus filhos
        node_z.height = 1 + max(self._get_height(node_z.left_child), self._get_height(node_z.right_child))
        node_y.height = 1 + max(self._get_height(node_y.left_child), self._get_height(node_y.right_child))

    def _right_rotate(self, node_z:Node):

        z_parent = node_z.parent 
        node_y = node_z.left_child
        node_t3 = node_y.right_child
        node_y.right_child = node_z
        node_z.parent = node_y
        node_z.left_child = node_t3

        if node_t3 != None:
            node_t3.parent = node_z

        node_y.parent = z_parent

        if node_y.parent == None:
                self.root = node_y
        else:
            if node_y.parent.left_child == node_z:
                node_y.parent.left_child = node_y
            else:
                node_y.parent.right_child = node_y	

        node_z.height = 1 + max(self._get_height(node_z.left_child), self._get_height(node_z.right_child))
        node_y.height = 1 + max(self._get_height(node_y.left_child), self._get_height(node_y.right_child))

    def delete_node(self, value:int):
        if isinstance(value, int):
            node = self.find(value)
        else:
            print(f'delete value not Int: {value}')
        return self._delete_node(node)

    def _delete_node(self, node:Node):
        # previne quebra de codigo caso o No nao exista
        if node == None or self.find(node.value) == None:
            print("Node to be deleted not found in the tree!")
            return None 

        # retorna o elemento com menor valor a partir do no recebido (menor filho)
        def min_value_node(node:Node):
            current = node
            while current.left_child != None:
                current = current.left_child
            return current

        # retorna o numero de filhos de um No especifico (0, 1 ou 2)
        def num_children(node:Node) -> int:
            num_children = 0
            if node.left_child != None:
                num_children += 1
            if node.right_child != None:
                num_children += 1
            return num_children

        # cria uma variavel com pai do No atual
        node_parent = node.parent

        # cria uma variavel com numero de filhos do No atual
        node_children = num_children(node)

        # CASO 1: No sem filhos (folha)
        if node_children == 0:

            if node_parent != None:
                # remove a referencia do No deletado no pai
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                # se No nao tiver pai ele eh a raiz
                # seta a raiz para None
                self.root = None

        # CASO 2: No com 1 filho
        if node_children == 1:

            # encontra o filho do No (verifica se eh left_child ou right_child)
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent!= None:
                # passa o filho (child) do No deletado para o avo
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # altera o pai da child para seu avo
            child.parent = node_parent

        # CASO 3: No com dois filhos
        # Parei aqui
        # tem que descobrir pq essa caralha nao ta funcionando
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            if isinstance(successor.value, int):
                node.value = successor.value
            else:
                print('successor value not Int')
                return

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor.value)

            # exit function so we don't call the _inspect_deletion twice
            return

        if node_parent != None:
            # fix the height of the parent of current node
            node_parent.height = 1 + max(self._get_height(node_parent.left_child), self._get_height(node_parent.right_child))

            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)

    def _inspect_deletion(self, cur_node:Node):

        if cur_node == None:
            return None

        left_height = self._get_height(cur_node.left_child)
        right_height = self._get_height(cur_node.right_child)

        if abs(left_height - right_height) > 1:
            node_y = self.taller_child(cur_node)
            node_x = self.taller_child(node_y)
            self._rebalance_node(cur_node, node_y, node_x)

        self._inspect_deletion(cur_node.parent)

    def find(self, value:int):
        if isinstance(value, int):
            pass
        else:
            print(f'valor do find nao é Int: {value}')

        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value:int, cur_node:Node):
        print(f'entrou: valor:{value}, valor do no: {cur_node.value}')

        if value == cur_node.value:
            return cur_node

        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)

        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node:Node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(f'{cur_node.value}, h = {cur_node.height}')
            self._print_tree(cur_node.right_child)

    def __repr__(self):
        
        if self.root == None:
            return ''
        
        content = '\n' # to hold final string
        cur_nodes = [self.root] # all nodes at current level
        cur_height = self.root.height # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1)) # variable sized separator between elements
        
        while True:
            cur_height += -1
            if len(cur_nodes) == 0:
                break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None,None])
                    continue

                if n.value != None:       
                    buf = ' ' * int((5 - len(str(n.value))) / 2)
                    cur_row += f'{buf}{n.value}{buf}' + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left_child != None:  
                    next_nodes.append(n.left_child)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right_child != None: 
                    next_nodes.append(n.right_child)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)

        return content


if __name__ == '__main__':
    new_tree = AVLTree()

    new_tree.insert(5)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(2)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(3)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(20)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(30)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(15)
    new_tree.print_tree()
    print(new_tree)

    new_tree.delete_node(3)
    new_tree.print_tree()
    print(new_tree)

    new_tree.delete_node(20)
    new_tree.print_tree()
    print(new_tree)
