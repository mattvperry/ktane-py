from ktane import Module
from ktane.modules import *
from inflection import humanize, underscore

def main():
    modules = get_module_dict()
    print(modules)

def get_module_dict():
    return { humanize_class_name(klass): klass() for klass in Module.__subclasses__() }

def humanize_class_name(klass):
    return humanize(underscore(klass.__name__))