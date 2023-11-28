@echo off
cscript CreateShortcut.vbs start_services.bat "%userprofile%\Desktop\LTIUY - Start app"
echo Iniciando servicios y app
REM python manage.py makemigrations
REM python manage.py migrate
echo Creando base de datos LTIUY y coleccion ltiuy_collection
mongosh --eval "db = connect('mongodb://localhost:27017/LTIUY'); db.createCollection('ltiuy_collection');"
echo Instalando requerimientos...
pip install -r requirements.txt --ignore-installed
playwright install
echo
echo Installer finalizado y requerimientos instalados/actualizados...OK
echo Presione enter para iniciar APIs y App
pause
start start_services.bat
exit