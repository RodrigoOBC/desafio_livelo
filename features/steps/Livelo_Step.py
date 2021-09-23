from behave import given, when, then, step
from features.Page.Base_page import Browser
from features.Page.Livelo_pages import LiveloPage


@given(u'que acesso a pagina da Livelo')
def step_impl(context):
    LiveloPage().go_to_page()

@when(u'seleciono um produto')
def step_impl(context):
    confirm = LiveloPage().procurar_elemento()
    assert confirm
    LiveloPage().colocar_elemento_carrinho()

@then(u'o produto selecionado deve ser apresentado no carrinho')
def step_impl(context):
    confirm = LiveloPage().verificar_elemento_carrinho()
    assert confirm
