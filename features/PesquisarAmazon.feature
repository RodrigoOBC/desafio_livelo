#language: pt

Funcionalidade: Gerenciar Pedido
  Sou um cliente e desejo gerenciar o carrinho de compra
  Adcionado, removendo e atualizando meu carrinho

  Cenario: Adicionar produto ao carrinho
    Dado que acesso a pagina da Livelo
    Quando seleciono um produto
    Entao o produto selecionado deve ser apresentado no carrinho


  Esquema do Cenário: Adicionar "<produto>" ao carrinho
    Dado que acesso a pagina da Livelo
    Quando seleciono "<produto>"
    E defino as configuração para "<voltagem>"
    E defino a quantidade "<QTD>"
    Entao o "<produto>" deve ser apresentado no carrinho
    E deve ter a quantidade de "<QTD>"
    Exemplos:
      | produto                                         | voltagem | QTD |
      | Mini Grill e Sanduicheira Philco - Vermelho/Aço | 110v     | 5   |


  Cenario: Remover produto do carrinho
    Dado que acesso a pagina da Livelo
    Quando seleciono um produto
    E o produto deve ser apresentado no carrinho
    E Removo o Produto do carrinho
    Entao o produto selecionado não deve ser apresentado no carrinho