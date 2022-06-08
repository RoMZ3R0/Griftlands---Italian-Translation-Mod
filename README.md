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
* <b>README.md</b> - <i>questo file</i>
* <b>modinit.lua</b> - <i>file di configurazione della mod</i>
* <b>icon.png</b> - <i>icona della mod per lo Steam Workshop</i>
* <b>it.po</b> - <i>file contenente il testo del gioco (codifica UTF-8)</i>

### Struttura del file <i>it.po</i>
Ogni oggetto di testo del gioco è descritto nel file 4 stringhe, come nell'esempio seguente:
1. <code>#. ACHIEVEMENT.ARCHENEMY.DESC</code>
2. <code>msgctxt "ACHIEVEMENT.ARCHENEMY.DESC"</code>
3. <code>msgid "Get {1} people to hate you in campaign or brawl."</code>
4. <code>msgstr "Fai in modo che {1} {1*persona|persone} ti {1*odi|odino} in una campagna o in una rissa."</code>

Le stringhe #1 e #2 <u>non devono</u> essere modificate durante la traduzione. La stringhe #3 (msgid) e #4 (msgstr) corrispondono rispettivamente al testo originale in inglese ed a quello tradotto. Il testo ed i numeri presenti tra parentesi graffe rapprentano le variabili di gioco. Nell'esempio sopra riportato la stringa #4 potrà assumere la seguente sintassi a seconda del numero di persone che dovremo fare in modo ci odino:
* frase al singolare, <i>"Fai in modo che 1 persona ti odi in una campagna o in una rissa."</i>
* frase al plurale, <i>"Fai in modo che 4 persone ti odino in una campagna o in una rissa."</i>

Prendiamo un altro esempio:
1. <code>#. ATTACK.ACCELERANT_PLUS2.DESC</code>
2. <code>msgctxt "ATTACK.ACCELERANT_PLUS2.DESC"</code>
3. <code>msgid "Apply {1} {SCORCHED} and {2} {BURN} to <#UPGRADE>all enemies.</>"</code>
4. <code>msgstr "Applica {1} {SCORCHED} e {2} {BURN} a <#UPGRADE>tutti i nemici.</>"</code>

### Per una traduzione coerente
Collaborare a più mani ad una traduzione può essere molto complicato, c'è il rischio di adottare stili ed idee 
