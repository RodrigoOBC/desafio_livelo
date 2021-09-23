#language: pt

Funcionalidade: Gerenciar Pedido
  Sou um cliente e desejo gerenciar o carrinho de compra
  Adcionado, removendo e atualizando meu carrinho

  Cenario: Adicionar produto ao carrinho
    Dado que acesso a pagina da Livelo
    Quando seleciono um produto
    Entao o produto selecionado deve ser apresentado no carrinho
