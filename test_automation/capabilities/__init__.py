"""
Inicializar capabilities
"""
from appium import webdriver
from capabilities import physical
from helpers.constants import APPIUM_URL


def define_caps(target: str, app_path, app_name, device_name: str, platform_name: str, platform_version, external_cap={}):
    """
    Gerar o capabilities de acordo com os parâmetros inseridos

    Args:
        - target: physical or emulator
        - device_name: nome do device
        - platform_name: Android ou iOs
    return
    """
    target = eval(target)
    capabilities = target.desired_caps(
        app_path, app_name, device_name, platform_name, platform_version
    )
    capabilities.update(external_cap)
    return webdriver.Remote(command_executor=APPIUM_URL, \
        desired_capabilities=capabilities)
