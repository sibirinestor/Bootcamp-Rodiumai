Créer et activer un environnement virtuel :


Cloner le repo : git clione https://github.com/sibirinestor/Bootcamp-Rodiumai.git

Bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
Installer les dépendances :

Bash
pip install -r requirements.txt
Configuration
Créez un fichier .env à la racine du projet en vous basant sur le fichier .env.example :

Bash
cp .env.example .env
Éditez le fichier .env pour y insérer votre clé API RodiumAi :

Extrait de code
RODIUMAI_API_KEY=rd_sk_votre_cle_ici
Utilisation
Lancez le script principal avec la commande suivante :

Bash
python main.py
