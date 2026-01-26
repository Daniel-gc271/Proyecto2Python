
set /p env_name=Introduce el nombre del entorno virtual de Python:

REM Establecer la política de ejecución en modo Bypass para el proceso actual
powershell -Command "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"

REM Crear el entorno virtual con el nombre proporcionado
python -m venv %env_name%

REM Crear la carpeta 'codigo' dentro del entorno virtual
mkdir "%env_name%\codigo"

REM Crear la carpeta 'recursos' dentro del entorno virtual
mkdir "%env_name%\recursos"

REM Activar el entorno virtual
powershell -ExecutionPolicy Bypass -File "%env_name%\Scripts\Activate.ps1"

pause