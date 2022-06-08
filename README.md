# Griftlands - Italian Translation Mod
<i>Traduzione fan-made del gioco di carte Griftlands (Klei) sviluppata per il Workshop di Steam.</i>\n
https://steamcommunity.com/sharedfiles/filedetails/?id=2817357554

### Una breve introduzione...
Dopo aver provato il gioco Griftlands sono rimasto colpito dalla qualità del titolo ed ho pensato meritasse una traduzione in italiano, anche non perfetta, ma che permettesse ai non anglofoni di usufruirne. Ho quindi deciso di accettare la sfida e provarci.
Il tempo (il lavoro) è tiranno ed ho quindi pensato di velocizzare il processo di traduzione scriptando "due righe di python" che convertissero il testo tramite la API di Microsoft Bing (un buon compromesso tra qualità e velocità). 
Per motivi legati alla formattazione del testo nel file del gioco, la traduzione è stata effettuata a partire dalla versione spagnola.
La prima versione della traduzione presentava molti errori ed ho dovuto applicare molteplici fix prima di portela pubblicare sul Workshop.
C'è ancora molto da fare ed è un lavoro che non riuscirei a portare a termine da solo.
L'aiuto della community sarà essenziale.

### Lista e descrizione dei file
1. <b>README.md</b> - <i>questo file</i>
2. <b>modinit.lua</b> - <i>file di configurazione della mod</i>
3. <b>icon.png</b> - <i>icona della mod per lo Steam Workshop</i>
4. <b>it.po</b> - <i>file contenente il testo del gioco (codifica UTF-8)</i>

### Struttura del file <i>it.po</i>
Ogni oggetto di testo del gioco è descritto nel file 4 stringhe, come nell'esempio seguente:
* #. ACHIEVEMENT.ARCHENEMY.DESC
* msgctxt "ACHIEVEMENT.ARCHENEMY.DESC"
* msgid "Get {1} people to hate you in campaign or brawl."
* msgstr "Fai in modo che {1} {1*persona|persone} ti {1*odi|odino} in una campagna o in una rissa."

