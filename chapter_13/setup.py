from cx_Freeze import setup, Executable
setup(name='My Game',
      version='0.1',
      description='Beta',
      executables = [Executable("alien_invasion.py")])