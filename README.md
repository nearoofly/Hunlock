# Hunlock
Hunlock est un logiciel conçu pour simuler le déblocage d'un téléphone Android verrouillé via des codes PIN en utilisant ADB (Android Debug Bridge)
---
## 📜 Fonctionnalités
- Tentatives automatiques de déblocage : Teste des codes PIN depuis un fichier texte (`digits.txt`).
- Affichage enrichi : Utilise la bibliothèque `rich` pour un affichage coloré et stylisé.
- Connexion ADB : Interagit avec des appareils Android via ADB (débogage USB requis).
- Validation dynamique : Permet de détecter si l'appareil est déverrouillé avec succès.

---

## 📷 Exemples d'affichage
Voici à quoi ressemble Hunlock lorsqu'il est exécuté :

### 1️⃣ Au lancement :
Le script affiche un hibou stylisé et vos informations personnalisées :

![Hunlock Logo et Présentation](images/launch_screen.png)

---

### 2️⃣ Pendant le processus de déblocage :
Le script tente les codes PIN en affichant les essais en cours. Si le bon code est trouvé, il affiche un message de succès.

![Hunlock Déblocage](images/unlocking_process.png)

---

## 🛠️ Installation
### Étape 1 : Clonez le dépôt
```bash
git clone https://github.com/nearoofly/hunlock.git
cd hunlock

Étape 2 : Installez les dépendances

Assurez-vous d’avoir Python 3 et rich installés :

pip install rich

Étape 3 : Préparez les codes PIN

Créez un fichier digits.txt contenant les codes PIN à tester :

0000
1234
5678
9999

Étape 4 : Connectez votre téléphone Android

	•	Activez le mode développeur et le débogage USB.
	•	Connectez l’appareil à votre ordinateur.

🚀 Exécution

	1.	Lancez le script depuis votre terminal :

python3 hunlock.py


	2.	Le script :
	•	Vérifie si un appareil est connecté via ADB.
	•	Lit les codes PIN dans digits.txt.
	•	Teste chaque code sur le téléphone.
	3.	Si le téléphone est déverrouillé avec succès, le code PIN correct sera affiché.

📂 Structure du projet

Le projet est structuré comme suit :

Hunlock/
├── hunlock.py       # Script principal
├── digits.txt       # Fichier des codes PIN
├── README.md        # Documentation
└── images/          # Dossier contenant les captures d'écran
    ├── launch_screen.png
    ├── unlocking_process.png

🖊️ À propos

	•	Créateur : Wharkly
	•	GitHub : nearoofly (https://github.com/nearoofly)
	•	More tools : https://github.com/nearoofly (https://github.com/nearoofly)

🎨 Personnalisation

Vous pouvez personnaliser l’affichage du script en modifiant :
	•	Le fichier hunlock.py (section display_logo).
	•	Les informations affichées dans le panneau.

📷 Ajout d’images

Pour ajouter vos propres captures d’écran :
	1.	Créez un dossier images/ dans le répertoire du projet.
	2.	Ajoutez vos images (format recommandé : PNG).
	3.	Mettez à jour les liens vers les images dans le README.

Exemple pour capturer l’affichage

Pour capturer le terminal sous Linux (avec Kali) :
	1.	Ouvrez le terminal et exécutez le script.
	2.	Appuyez sur PrtSc (Imprimer écran).
	3.	Collez l’image dans un éditeur (GIMP, Shutter, etc.) et enregistrez-la dans images/.

🤝 Contributions

Les contributions sont les bienvenues ! Pour proposer des modifications :
	1.	Forkez ce dépôt.
	2.	Créez une branche pour votre modification :

git checkout -b feature/your-feature-name


	3.	Soumettez une pull request.

📝 Licence

Ce projet est sous licence Boost Software License 1.0

Vous êtes libre de l’utiliser, de le modifier et de le distribuer tant que vous respectez les termes de la licence.
