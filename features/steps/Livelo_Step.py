from behave import given, when, then, step
from features.Page.Base_page import Browser
from features.Page.Livelo_pages import LiveloPage

LP = LiveloPage()

@given(u'que acesso a pagina da Livelo')
def step_impl(context):
    LP.go_to_page()

@when(u'seleciono um produto')
def step_impl(context):
    confirm = LiveloPage().procurar_elemento()
    assert confirm
    LP.colocar_elemento_carrinho()

@then(u'o produto selecionado deve ser apresentado no carrinho')
def step_impl(context):
    confirm = LP.verificar_elemento_carrinho()
    LP.browser_clear()
    assert confirm


@when(u'seleciono "{text}"')
def step_impl(context,text):
    confirm = LP.procurar_elemento(name=text)
    assert confirm
    LP.selecionar_Produto(name=text)

@when(u'defino as configuração para "{text}"')
def step_impl(context,text):
    LP.selecionar_opp(vol=text)
    LP.adicionar_elemento_ao_carrinho()

@when(u'defino a quantidade "{text}"')
def step_impl(context,text):
    LP.somar_elemento(QTD=text)


@then(u'o "{text}" deve ser apresentado no carrinho')
def step_impl(context,text):
   LP.verificar_elemento_carrinho(name=text)

@then(u'deve ter a quantidade de "{text}"')
def step_impl(context,text):
    confirm = LP.verificar_QTD(QTD=text)
    LP.browser_clear()
    assert confirm


@when(u'o produto deve ser apresentado no carrinho')
def step_impl(context):
    confirm = LP.verificar_elemento_carrinho(name='Mini Grill e Sanduicheira Philco - Vermelho/Aço')
    assert confirm

@when(u'Removo o Produto do carrinho')
def step_impl(context):
    LP.remover_produto()

@then(u'o produto selecionado não deve ser apresentado no carrinho')
def step_impl(context):
    confirm = LP.verificar_elemento_removido_carrinho()
    LP.browser_clear()
    LP.browser_quit()
    assert confirm
