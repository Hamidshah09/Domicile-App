import sys
import inspect
import pyperclip


def print_classes():
    for name, obj in inspect.getmembers(pyperclip.__name__):

        if inspect.isclass(obj):
            print(obj)


print_classes()
