comandas = []
clientes = []
produtos = ['Cerveja', 'água', 'batata', 'whisky']
valor_pagar = 0

def guardar_nome(): 
    ad = input('Digite seu nome: ')
    clientes.append(ad)

def pedido():
    for i in range(5):
        
        esc = input('Digite oqr vc precisa consumir: ')
        
        if esc == 'Cerveja':
            comandas.append(esc)
        elif esc == 'água':
            comandas.append(esc)
        elif esc == 'batata':
            comandas.append(esc)
        else:
            print('Digite algo do nosso cárdapio por favor:')

def consumido():
    guardar_nome()
    pedido()
    valor_pagar = len(comandas)*3.5
    
    for i in comandas:
        
        print(f'A soma dos valores de {i} são 3.5 para cada unidade')     
        
    print(f'Nome do cliente: ', clientes[0])
    print('..........................')
    print(f'Produtos consumidos: ', comandas)
    print(f'Valor total {valor_pagar}')
    

consumido()
