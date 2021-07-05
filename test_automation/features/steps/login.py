from behave import given, when, then
from modules.page_objects.login_page import PageLogin


@given('que clico no botão Entrar com Google')
def login_with_google(context):
  login = PageLogin(context.driver)
  login.click_login()


@when('insiro o usuário e senha')
def insert_user_and_password(context):
  ...


@then('a tela home deve ser iniciada')
def home_init(context):
  ...