from page_objects import PageElement, PageObject
from time import sleep

class PageLogin(PageObject):
  """
  Page Objects da tela de login
  """

  btn_login = PageElement(
    xpath='//android.widget.ImageView[@content-desc="Entrar com Google"]'
  )

  def click_login(self) -> None:
    """
    Clica no botão Entrar com Google
    """
    sleep(10)
    self.btn_login.click()