# language: pt

Funcionalidade: Tela de login

  Cenário: Efetuar o login com suceso atráves do Google
    Dado que clico no botão Entrar com Google
    Quando insiro o usuário e senha 
     | Usuário       | Senha |
     | xxx@gmail.com | xxx   |
    Então a tela home deve ser iniciada