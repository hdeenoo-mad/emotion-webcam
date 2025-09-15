@echo off
echo ========================================
echo   Lancement de l'application Flask + DeepFace
echo ========================================

REM Activer l'environnement virtuel
call .venv\Scripts\activate

REM Installer les dépendances (si besoin)
pip install -r requirements.txt

REM Lancer le serveur Flask
python server.py

pause
