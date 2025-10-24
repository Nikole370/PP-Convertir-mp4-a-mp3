import importlib.util, inspect, pathlib

ruta = 'app.py'
spec = importlib.util.spec_from_file_location('mod', ruta)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

for nombre, func in inspect.getmembers(mod, inspect.isfunction):
    # Asegura que la función fue definida en app.py (no importada)
    if inspect.getsourcefile(func) == str(pathlib.Path(ruta).resolve()):
        doc = inspect.getdoc(func) or "(sin docstring)"
        print(f"\n{nombre}\n{'-'*len(nombre)}\n{doc}")
