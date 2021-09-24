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
    LiveloPage().colocar_elemento_carrinho()

@then(u'o produto selecionado deve ser apresentado no carrinho')
def step_impl(context):
    confirm = LiveloPage().verificar_elemento_carrinho()
    assert confirm

@when(u'seleciono "{text}"')
def step_impl(context,text):
    confirm = LP.procurar_elemento(name=text)
    assert confirm
    LiveloPage().selecionar_Produto(name=text)

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

