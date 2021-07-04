"""
Hooks globais
"""
from capabilities import define_caps
from time import sleep


def before_all(context):
    context.target = context.config.userdata.get("target")
    context.app_name = context.config.userdata.get("app")
    context.app_path = context.config.userdata.get("app_path")
    context.name_device = context.config.userdata.get("name_device")
    context.name_platform = context.config.userdata.get("name_platform")
    context.platform_version = context.config.userdata.get("platform_version")


def before_feature(context, feature):
    context.driver = define_caps(
        target=context.target,
        app_name=context.app_name,
        app_path=context.app_path,
        device_name=context.name_device,
        platform_name=context.name_platform,
        platform_version=context.platform_version
    )

def before_scenario(context, scenario):
    ...

def before_step(context, step):
    ...

def after_step(context, step):
    sleep(7)

def after_scenario(context, scenario):
    ...

def after_feature(context, feature):
    ...

def after_all(context):
    ...
