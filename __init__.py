import importlib
import os


files = os.listdir("effective_python/models")
modules = filter(lambda x: x.endswith(".py"), files)
for m in modules:
    importlib.import_module("effective_python.models." + m[0:-3])
