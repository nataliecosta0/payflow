# Android environment
from os.path import abspath

"""
Inicializar capabilities no device fisico
"""
def desired_caps(app_path, app_name, device_name, platform_name, platform_version, package_name):
    """
    Inicializa as capabilities para um dispositivo físico
    """
    return {
        'deviceName': device_name,
        'platformName': platform_name,
        'appPackage': package_name,
        'platformVersion': platform_version,
        'app': abspath('{}{}').format(app_path, app_name),
        'noReset': True
    }
