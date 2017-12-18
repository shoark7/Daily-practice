"""Transitive reload function implementations

    If you want to reload modules, there are imp.reload in python 3.
    But you need to be aware that imp.reload reloads requested module itself,
    not modules that this module imports.

    So we need to implement that functions by ourselves, and I suggest you 3 versions:
        1. Recursive call v1
        2. Recurvise call v2
        3. Stack call


    These 3 versions are worth checking out.
    Awesome I guess.
"""
from imp import reload
import importlib
import sys
import types


def status(module):
    print('Reloading {}'.format(module.__name__))


def try_reload(module):
    try:
        reload(module)
    except:
        print('FAILED {}'.format(module.__name__))


# Way 1
def transitive_reload_1(module, visited):
    if module not in visited:
        status(module)
        try_reload(module)
        visited[module] = True
        for attr in module.__dict__.values():
            if isinstance(attr, types.ModuleType):
                transitive_reload_1(attr, visited)


def reload_all_1(*args):
    visited = {}
    for arg in args:
        if isinstance(arg, types.ModuleType):
            transitive_reload_1(arg, visited)


# Way 2
def transitive_reload_2(objects, visited):
    for obj in objects:
        if isinstance(obj, types.ModuleType) and obj not in visited:
            status(obj)
            try_reload(obj)
            visited.add(obj)
            transitive_reload_2(obj.__dict__.values(), visited)


def reload_all_2(*args):    # Question! : Can you guess why we need to pack args???
    transitive_reload_2(args, set())


# Way 3
def transitive_reload_3(modules, visited):
    while modules:
        next = modules.pop()
        status(next)
        try_reload(next)
        visited.add(try_reload)
        modules.extend(x for x in next.__dict__.values()
                       if isinstance(x, types.ModuleType) and x not in visited)


def reload_all_3(*modules):   # Question! : Can you guess whey we need to pack args???
    transitive_reload_3(list(modules), set())


def tester(reloader, module_name):
    if len(sys.argv) > 1:
        module_name = sys.argv[1]
    module = importlib.import_module(module_name)
    reloader(module)


if __name__ == '__main__':
    tester(reload_all_1, 'transitive_reload_171218')
    tester(reload_all_2, 'transitive_reload_171218')
    tester(reload_all_3, 'transitive_reload_171218')
