# Griftlands - Italian Translation Mod

<i>Traduzione fan-made del gioco di carte Griftlands (Klei) sviluppata per il Workshop di Steam.</i>

[Link alla mod su Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=2817357554)

### Una breve introduzione...

Dopo aver provato il gioco Griftlands sono rimasto colpito dalla qualità del titolo ed ho pensato meritasse una traduzione in italiano, anche non perfetta, ma che permettesse ai non anglofoni di usufruirne. Ho quindi deciso di accettare la sfida e provarci.

### Stato della traduzione

La traduzione è in corso, tramite l'uso del LLM Gemini 1.5 Flash: non infallibile, ma molto preciso. Richiese quindi una revisione manuale e per questo l'aiuto della community sarà essenziale.

Ho pubblicato la mod alla versione **0.4 beta**, con un po' di anticipo rispetto a quanto programmato. La percentuale di stringhe tradotte è del **52%**. Questa però non corrisponde alla quantità di testo tradotto (che non posso quantificare), ma è molto di più in termini percentuali.

Pubblicherò quasi giornalmente gli aggiornamenti.

**Il motivo della pubblicazione, anche se non completa**, è che sebbene la traduzione sia in corso, se qualcuno avesse intenzione di giocarla, può segnalarmi problemi (non solo errori, ma anche termini da correggere).

Esempi:
- **Mettle**, tradotto in "Tempra", lo devo ancora cambiare manualmente in alcune stringhe
- **Flourish**, tradotto erroneamente in "Fioritura", lo modificherò poi in "Fulgore" (più adatto)
- Ho notato che il LLM ha tradotto qualche variabile quando non avrebbe dovuto. Alcune conversazioni potrebbero quindi avere problemi.

Fatemi avere un feedback! Sfruttate la sezione bug fixes per indicare errori di traduzione o suggerimenti vari.

### Lista e descrizione dei file

* <b>README.md</b> - <i>questo file</i>
* <b>modinit.lua</b> - <i>file di configurazione della mod</i>
* <b>icon.png</b> - <i>icona della mod per lo Steam Workshop</i>
* <b>it.po</b> - <i>file contenente il testo del gioco (codifica UTF-8)</i>

### Struttura del file <i>it.po</i>

Ogni oggetto di testo del gioco è descritto nel file in 4 stringhe, come nell'esempio seguente:

1. <code>#. ACHIEVEMENT.ARCHENEMY.DESC</code>
2. <code>msgctxt "ACHIEVEMENT.ARCHENEMY.DESC"</code>
3. <code>msgid "Get {1} people to hate you in campaign or brawl."</code>
4. <code>msgstr "Fai in modo che {1} {1*persona|persone} ti {1*odi|odino} in una campagna o in una rissa."</code>

Le stringhe #1 e #2 <u>non devono</u> essere modificate durante la traduzione. Le stringhe #3 (msgid) e #4 (msgstr) corrispondono rispettivamente al testo originale in inglese ed a quello tradotto. Il testo ed i numeri presenti tra parentesi graffe rappresentano le variabili di gioco. Nell'esempio sopra riportato la stringa #4 potrà assumere la seguente sintassi a seconda del numero di persone che dovremo fare in modo ci odino:
- frase al singolare, <i>"Fai in modo che 1 persona ti odi in una campagna o in una rissa."</i>
- frase al plurale, <i>"Fai in modo che 4 persone ti odino in una campagna o in una rissa."</i>

Prendiamo un altro esempio:
1. <code>#. ATTACK.ACCELERANT_PLUS2.DESC</code>
2. <code>msgctxt "ATTACK.ACCELERANT_PLUS2.DESC"</code>
3. <code>msgid "Apply {1} {SCORCHED} and {2} {BURN} to <#UPGRADE>all enemies.</>"</code>
4. <code>msgstr "Applica {1} {SCORCHED} e {2} {BURN} a <#UPGRADE>tutti i nemici.</>"</code>

In alcune stringhe possono essere presenti variabili di gioco che si riferiscono ad abilità (es. <code>{SCORCHED}</code> e <code>{BURN}</code>), nonché tag di formattazione del testo (<code><#UPGRADE> </></code>). Le variabili in questione non devono essere modificate/tradotte. Relativamente alle tag, solo il testo compreso tra esse può essere tradotto (es. <i>all enemies.</i> tradotto in <i>tutti i nemici.</i>). Durante la traduzione automatica alcune variabili e tag sono state compromesse. Dovrei averle fixate tutte o quasi.

### Una traduzione coerente
Collaborare a più mani ad una traduzione può essere molto complicato: il rischio di adottare stili diversi da persona a persona è concreto. Cercherò quindi di definire alcune regole, di certo non insidacabili, ma che per ora possano definire una strada comune da percorrere.

Chiunque è interessato a collaborare, mi contatti anche su steam [https://steamcommunity.com/id/romz/](https://steamcommunity.com/id/romz/).

Lo aggiungerò ai collaboratori della mod ed ovviamente ai ringraziamenti.