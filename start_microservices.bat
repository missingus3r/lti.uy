@echo off
pip install --no-cache-dir -r requirements.txt 
start cmd /k python APIS\Login.py
start cmd /k python APIS\PortalAcademico.py
start cmd /k python APIS\Moodle.py
