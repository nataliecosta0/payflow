from appium import webdriver
from capabilities.physical import desired_caps
from helpers.constants import APPIUM_URL


def define_caps(target: str, app_path: str, app_name: str, device_name: str,
                platform_name: str, platform_version, package_name: str, 
                external_cap={}
            ):
    """
    Gera o capabilities de acordo com os parâmetros inseridos

    Args:
        - target: physical or emulator
        - app_path: diretório do app do projeto
        - app_name: nome do app do projeto
        - device_name: nome do device
        - platform_name: Android ou iOs
        - platform_version: versão que será executado
        - package_name: package do aplicativo

    return:
        - capabilities
    """
    target = eval(target)
    capabilities = target.desired_caps(
        app_path,
        app_name,
        device_name,
        platform_name,
        platform_version,
        package_name
    )
    capabilities.update(external_cap)
    
    return webdriver.Remote(command_executor=APPIUM_URL,
                            desired_capabilities=capabilities)
