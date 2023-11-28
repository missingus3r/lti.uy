@echo off
start /min cmd /k python apis\Login.py
start /min cmd /k python apis\PortalAcademico.py
start /min cmd /k python apis\Moodle.py
start /min cmd /k python apis\Eventos.py
start /min cmd /k python apis\Git.py
start /min cmd /k python apis\Edu.py
start /min cmd /k python apis\HashCreds.py
start /min cmd /k python apis\Notificaciones.py
start /min cmd /k python apis\Optativas.py
start /min cmd /k python apis\VME.py
start /min cmd /k python apis\EspacioColaborativo.py
start /min cmd /k python apis\Pinecone_query.py

echo APIs iniciadas...OK
REM echo Iniciando main App - Para detener presionar Ctrl+C
rem python manage.py runserver
pause
echo Deteniendo APIs...
taskkill /IM python.exe /F
taskkill /IM cmd.exe /F
echo APIs detenidas con exito...OK
echo Enter para salir
pause
exit