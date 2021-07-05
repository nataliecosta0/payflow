from selenium.webdriver.support.ui import WebDriverWait
from ipdb import post_mortem

from capabilities import define_caps


def before_all(context):
    context.userdata = context.config.userdata
    context.target = context.userdata.get("target")
    context.app_name = context.userdata.get("app")
    context.app_path = context.userdata.get("app_path")
    context.name_device = context.userdata.get("name_device")
    context.name_platform = context.userdata.get("name_platform")
    context.platform_version = context.userdata.get("platform_version")
    context.package_name = context.userdata['package_name']


def before_feature(context, feature):
    context.driver = define_caps(
        target=context.target,
        app_name=context.app_name,
        app_path=context.app_path,
        device_name=context.name_device,
        platform_name=context.name_platform,
        platform_version=context.platform_version,
        package_name=context.package_name
    )

    context.wait = WebDriverWait(context.driver, 10)

def before_scenario(context, scenario):
    ...

def before_step(context, step):
    ...

def after_step(context, step):
    if context.config.userdata.get('debug') and step.status == "failed":
        post_mortem(step.exc_traceback)

def after_scenario(context, scenario):
    context.driver.remove_app(context.package_name)

def after_feature(context, feature):
    ...

def after_all(context):
    ...
