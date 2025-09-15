#!/bin/bash
echo "========================================"
echo "  Lancement de l'application Flask + DeepFace"
echo "========================================"

# Vérifier si l'environnement virtuel existe
if [ ! -d ".venv" ]; then
  echo ">>> Création d'un environnement virtuel..."
  python3 -m venv .venv
fi

# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances
echo ">>> Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

# Cas spécial pour Mac M1/M2 (Apple Silicon)
if [[ $(uname -m) == "arm64" ]] && [[ $(uname) == "Darwin" ]]; then
  echo ">>> Mac M1/M2 détecté : installation de TensorFlow optimisé..."
  pip install tensorflow-macos tensorflow-metal
fi

# Lancer le serveur Flask
echo ">>> Démarrage du serveur Flask..."
python server.py
