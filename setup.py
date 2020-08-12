from cx_Freeze import setup, Executable

setup(
    name="teste EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("change-route.py")])