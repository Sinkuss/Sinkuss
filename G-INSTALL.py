import os
import subprocess

def print_menu():
    menu_text = """
░▒█░▒█░▒█▀▀▀█░▒█░▒█░▒█▄░▒█░▒█▀▀▄░▒█▀▀▀█
░▒█▀▀█░▒█░░▒█░▒█░▒█░▒█▒█▒█░▒█░▒█░░▀▀▀▄▄
░▒█░▒█░▒█▄▄▄█░░▀▄▄▀░▒█░░▀█░▒█▄▄█░▒█▄▄▄█
             G-HOUNDS MENU
            Hounds Detections
            
    [1.] - Everything
    [2.] - System Informer
    [3.] - Service execution
    [4.] - Winprefetchview
    [5.] - Journal trace
    [6.] - Easy journal viewer
    [7.] - Usbdeview
    [8.] - Wyjście
    """
    print(menu_text)

def download_and_run_program(url):
    try:
        subprocess.Popen(['curl', '-O', url], shell=True)
    except Exception as e:
        print(f"Błąd podczas pobierania pliku: {e}")

# 

def run_program(choice):
    programs = {
        '1': 'https://www.voidtools.com/Everything-1.4.1.1024.x86-Setup.exe',
        '2': 'https://github.com/winsiderss/si-builds/releases/download/3.0.7432/systeminformer-3.0.7432-setup.exe',
        '3': 'https://github.com/Zack-src/Service-Execution/releases/download/1.0/Service-Execution.exe',
        '4': 'https://www.nirsoft.net/utils/winprefetchview.zip',
        '5': 'https://github.com/ponei/JournalTrace/releases/download/1.0/JournalTrace.exe',
        '6': 'https://cdn.discordapp.com/attachments/1198974260329336842/1198975048619397270/journal-tool.exe?ex=65c0db87&is=65ae6687&hm=ae79581c2d2787ab2e388fb40a5da16baffec641556e1ed9a921f48412929cf0&',
        '7': 'https://www.nirsoft.net/utils/trans/usbdeview_polish.zip',
        # ... (pozostałe opcje)
    }
    program_url = programs.get(choice)
    if program_url:
        download_and_run_program(program_url)
    else:
        print("Nieznany wybór.")

def main():
    while True:
        print_menu()
        choice = input("Wybierz numer programu do uruchomienia: ")
        if choice == '8':
            break
        run_program(choice)

if __name__ == "__main__":
    main()