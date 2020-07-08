# Sympy-GUI (betere naam nodig)
Dit is het repository voor sympy-gui.  
Link naar het ontwerp in Figma (toegang nodig):
https://www.figma.com/file/ctMm3mwTsvBXyXFuvrqtsr/website?node-id=2%3A0
# Downloaden code:
In de map waarin de code moet komen (git maakt daarin een map aan met de naam 'sympy-GUI', met alle bestanden). Vul hierin username en password in:

    git clone https://GitHubUsernamehier:GitHubPasswordHier@github.com/RagnarVdB/sympy-GUI

# Basic git gebruik
Commit maken:

    git add .
    git commit -m "Hier een korte beschrijving van de aanpassingen"
`git add .` voegt alle bestanden uit de actieve dir toe aan de 'staging'. `git commit` maakt dan een commit in het lokale repository van alle 'gestagede' bestanden (dus nog niet op GitHub).

 Bekijk welke bestanden in staging zitten, of verwijder alle bestanden uit staging:

    git status
    git reset

Lokale commits uploaden naar GitHub:

    git push

Nieuwe commits van GitHub (van anderen) naar het lokale repo halen:

    git pull
Als zowel het lokale repo als het GitHub repo nieuwe wijzigingen bevatten kunnen conflicten optreden. Die moet je dan in je editor zelf oplossen en opnieuw een commit maken.
# Virtual environment, python dependencies en Flask
Ga in de server folder.

    cd server
Creëer virtuele omgeving en activeer.


    python -m venv venv
    venv/Scripts/activate
In Visual Studio Code (met Python extensie) kan je de virtuele omgeving ook activeren met `CTRL`+`SHIFT`+`P`, Python: select python interpreter, en dan de interpreter te selecteren in `server\venv\Scripts\python.exe`.

Installeer python dependencies uit requirements:

    pip install -r requirements.txt
Je kan `test.py` uitvoeren om te zien of dependencies correct zijn geïnstalleerd.

## Flask dev-server opstarten:
Met de Flask dev server kan je de code in realtime testen:  
in de server dir moeten omgevingsvariabelen ingesteld worden. Om de hot-reload te activeren moet je ook de omgeving instellen.  
(zorg dat venv is geactiveerd)  
In windows command line:

    set FLASK_APP=main.py
    set FLASK_ENV=development
In Git Bash:

    export FLASK_APP=main.py
    export FLASK_ENV=development

Om de server te starten:

    flask run
De sever start dan op localhost in poort 5500 (default). Openen op:
http://127.0.0.1:5000/

De server zal dan herstarten telkens wanneer het bestand wordt gesaved.
# Vue
Eerst Node en npm installeren:  
https://nodejs.org/en/download/ installeert zowel node als npm.

Vue CLI installeren (als npm geïnstalleerd is):

    npm install -g @vue/cli
Installeren node dependencies: ga in client folder en installeer uit package.json:

    cd client
    npm install
Je kan evt. het project importeren in de vue GUI. lanceer met:

    vue ui
Bij 'import' de juiste map selecteren (client)

## Dev server
De dev server maakt een lokale webserver aan met hotreload, zodat je makkelijk het resultaat kan zien:

Via vue ui: onder 'tasks', start 'serve'.  
Met CLI:

    npm run serve
De app start dan in localhost in de aangegeven poort.
