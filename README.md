# Sympy-GUI (betere naam nodig)
Dit is het repository voor sympy-gui.

# Installatie code en dependencies
## downloaden code:
In de map waarin de code moet komen (git maakt daarin een map aan met de naam 'sympy-GUI', met alle bestanden). Vul hierin username en password in:

    git clone https://GitHubUsernamehier:GitHubPassword@github.com/RagnarVdB/sympy-GUI
## venv en python dependencies
Ga in de server folder.

    cd server
Creëer virtuele omgeving en activeer.

    python -m venv venv
    venv/Scripts/activate
Installeer python dependencies uit requirements:

    pip install -r requirements.txt
Je kan `main.py` uitvoeren om te zien of dependencies correct zijn geïnstalleerd.


## Installeren Vue
Eerst Node en npm installeren:
https://nodejs.org/en/download/  
installeert zowel node als npm.

Vue CLI installeren (als npm geïnstalleerd is):

    npm install -g @vue/cli
Installeren node dependencies: ga in client folder en installeer uit package.json:

    cd client
    npm install
Je kan evt. het project importeren in de vue GUI. lanceer met:

    vue ui
Bij 'import' de juiste map selecteren (client)

### Dev server
De dev server maakt een lokale webserver aan met hotreload, zodat je makkelijk het resultaat kan zien:

Via vue ui: onder 'tasks', start 'serve'.  
Met CLI:

    npm run serve
De app start dan in localhost in de aangegeven poort.
