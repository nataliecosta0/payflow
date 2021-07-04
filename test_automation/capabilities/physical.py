# Android environment
from os.path import abspath

"""
Inicializar capabilities no device fisico
"""
def desired_caps(app_path, app_name, device_name, platform_name, platform_version):
    """
    Inicializa as capabilities para um device real
    """
    return {
        'deviceName': device_name,
        'platformName': platform_name,
        #'appPackage': '',
        'platformVersion': platform_version,
        #'appActivity': '.MainActivity',
        'app': abspath('{}{}').format(app_path, app_name),
        'noReset': True
    }
