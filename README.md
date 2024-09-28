# Allgemeine Hinweise

Das README dient der Dokumentation der Artefakte, die während des Projektes entstehen. Es ersetzt nicht den
wissenschaftlichen Projektbericht (siehe moodle). Dieser sollte im Reporsitory mit aufgenommen werden.

# Einführung und Ziele

## Aufgabenstellung

Das Projekt: User Story Generator Das Projekt User Story Generator hat das Ziel, ein System zu entwickeln welches
mithilfe eines Large Language Models (LLM) automatisch User Stories. Die User Stories werden aus
Personas/Problembeschreibungen generiert. Die Personas/Problembeschreibungen werden als PDF-Datei bereitgestellt und
können über eine benutzerfreundliche Oberfläche in Form einer Webseite oder Mobile-App hochgeladen werden. Dabei soll
das LLM lokal auf dem Host laufen, d.h. es dürfen keine externen Ressourcen wie LLM aus dem Internet benutzt werden.

## Qualitätsziele

Ziel ist es eine funktionierende und benutzerfreundliche Software dem Kunden bereitzustellen

# Randbedingungen

- [x] Das LLM soll lokal laufen
- [x] Personas/Problembeschreibungen sollen als PDF hochgeladen werden
- [x] Es soll möglich sein mehrere PDF-Dokumente gleichzeitig hochzuladen
- [x] Manuelle Texteingabe der Persona/Problembeschreibung
- [x] Hochgeladene PDF-Dokumente werden als verfügbar angezeigt
- [x] Hochgeladene PDF-Dokumente können selektiert und extrahiert oder gelöscht werden
- [x] Verfügbare Personas/Problembeschreibungen können inspiziert und bei Bedarf per Auswahl gelöscht werden
- [x] Generieren von User Stories durch verfügbare Persona/Problembeschreibung
- [x] Webseite als GUI für die Benutzer
- [x] Erneutes Generieren von vorhandenen User Stories
- [ ] Erneutes Generieren von vorhandenen User Stories mit Angabe was nicht passt
- [x] User Stories können einzeln selektiert und gelöscht werden
- [x] User Stories als Ergebnisse per TXT-Datei herunterladen können
- [x] Erstellen von Tests (PyTest und Selenium) mit unterschiedlicher Coverage auf Funktion

## Fachlicher Kontext

![Fachlicher Kontext](https://github.com/hnuDSMProjekt/24_SoSe_StoryGenerator/assets/102808657/71885145-e271-4645-9c2b-de6c946393d5)

**Erläuterung der externen fachlichen Schnittstellen**

1. Hochladen von PDF Dateien
2. Manuelle Eingabe von Problembeschreibungen/Personas in Textform
3. Generierung von User Stories
4. Anpassung der User Stories

## Technischer Kontext

![Technischer Kontext](data/artefacts/Design/Technischer%20Kontext.png)

**Erläuterung der externen technischen Schnittstellen**

1. Frontend [index.html](templates/index.html)
    - [HTML](templates/index.html)
    - [CSS](static/main.css)

Beschreibung: Das Frontend stellt die Benutzeroberfläche bereit, über die Benutzer mit dem System interagieren können.
Die Benutzer können Problembeschreibungen und Personas als PDF hochladen und sich daraus User Stories generieren lassen.

2. Backend [Server.py](server.py)
    - [Flask](https://flask.palletsprojects.com/en/3.0.x/)

Beschreibung: Das Backend verarbeitet und verwaltet die Benutzeranfragen. Es leitet Anfragen zur PDF-Verarbeitung an
den [manage_text.py](manage_text.py) und zur Generierung von User Stories [LLM.py](llm.py) weiter.

3. Datei Upload [manage_text.py](manage_text.py)
    - PyPDF Library

Beschreibung: Analyse und Auslesen der hochgeladenen PDF-Dateien, um die darin enthaltenen Problembeschreibungen /
Personas zu extrahieren.

4. LLM [llm.py](llm.py)
    - HuggingFace

Beschreibung: Verwendung ein vortrainiertes Large Language Model (LLM) zur Generierung von User Stories.

5. Testing
    - Selenium
    - PyTest

Beschreibung: Automatisierte Tests der Benutzeroberfläche und der Backend-Funktionalitäten, um die Qualität und
Funktionalität des Systems sicherzustellen.

**Mapping fachliche auf technische Schnittstellen**

<img width="800" alt="Schnittstellen" src="https://github.com/hnuDSMProjekt/24_SoSe_StoryGenerator/assets/102808657/ec2b2848-170f-4bdd-9364-167a74a776a2">

# Information zum Setup

Die User Stories werden mit einem LLM generiert. Wir haben uns
für [EM German entschieden](https://huggingface.co/jphme/em_german_leo_mistral). Dieses LLM baut auf dem Open Source
Mistral LLM auf. Für dieses Projekt benutzen wir die GGUF Version. Der direkte Downloadlink
ist [hier](https://huggingface.co/TheBloke/em_german_leo_mistral-GGUF/resolve/main/em_german_leo_mistral.Q6_K.gguf?download=true)
. Das heruntergeladene Modell muss anschließend im /models/ Verzeichnis abgelegt werden. Wir benutzen in diesem Projekt
Python Version 3.11. Dementsprechend setzen wir das Virtual Environment in dem Root Verzeichnis des Ordners mit der
gebrauchten Python Version:

```
cd your/project/here
python3.11 -m venv .
```

[PyToch](https://pytorch.org/get-started/locally/) Version Stable (2.3.1) wurde manuell installiert mit folgendem
Befehl:

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

Zum Schluss die Requirements aus der requierements.txt installieren mit folgendem Befehl:

```
pip3 install -r requirements.txt
```

Sind die Requirements installiert und das richtige Modell entsprechend platziert kann man einen Server auf localhost mit
folgendem Befehl starten:

```
flask --app server.py --debug run
```

Flask startet server.py, welche alle Schnittstellen verbindet. --debug erlaubt Hot Reloading. Das heißt wir können den
Programmcode ändern, speichern und anschließend die Seite einfach neu laden. Ohne --debug müssen wir den Flask Server
jedes Mal neu starten nach einer Änderung im Programmcode.

# Lösungsstrategie

# Bausteinsicht

## Whitebox Gesamtsystem

***Übersichtsdiagramm***

![Component Diagram](data/artefacts/Design/Component%20Diagram.png)

Begründung das zentrale Konzept dieses Projekts ist die Generierung von User Stories für vorgegebene
Problembeschreibungen und Personas mit der Funktionalität eines Large Language Models (LLM). Dem Benutzer wird eine
Website zugänglich gemacht um das Hochladen von Dateien oder durch Eingabe von Texten in einem Textfeld zu vereinfachen.
Dabei können die Benutzer die User Stories individuell konfigurieren und anpassen lassen.

Die User haben folgende Möglichkeiten um mit dem System zu interagieren:

- Generieren
- Aktualisieren
- Selektion Löschen
- Selektion Neu Generieren
- Download

Abbildung: Auszug aus der Website

<img width="800" alt="website 2" src="https://github.com/hnuDSMProjekt/24_SoSe_StoryGenerator/assets/102808657/bebd91af-9cbe-494a-97f5-417de759a398">

### Enthaltene Bausteine

### Backend: LLM

Zweck: Integration und Verwendung des Large Language Models zur Generierung von User Stories

Erfüllte Anforderungen: Automatisierte Generierung von User Stories Risiken: Abhängigkeit von der Qualität der
hochgeladenen PDF-Dateien, Context-Length

### Backend: Server.py

Zweck: Verwaltung und Verarbeitung von Daten zwischen den Komponenten LLM.py - index.html - manage_text.py

Schnittstellen:

- [manage_text.py](manage_text.py)
- [llm.py](llm.py)

Erfüllte Anforderungen: Backend-Infrastruktur Risiken: Performance

### Backend: Manage_text.py:

Zweck: Einlesen und Extrahieren der hochgeladenen PDF-Dateien um darin enthaltenen Problembeschreibungen / Persona Daten
zu extrahieren.

Schnittstellen:

- [Server.py](server.py)

Qualitätsmerkmale: Einlesen und Analyse der PDF-Inhalte

Erfüllte Anforderungen: Auslesen der Daten aus den Problembeschreibungen und Personas

Risiken: Formatierungen, Text und Dateigröße

### Frontend: Index.html

Zweck: Bereitstellung der Benutzeroberfläche (Website) zur Interaktion mit dem System Schnittstellen:

- [Server.py](server.py)

Qualitätsmerkmale: Benutzerfreundlichkeit und einfache Bedienung

Erfüllte Anforderungen: Ermöglichen das PDF Dateien Hochgeladen werden, Text manuell eingefügt werden kann und das User
Stories verwaltet werden kann.

### Frontend: main.css

Zweck: Gestaltung und Design der Website Schnittstellen: [index.html](templates/index.html) Qualitätsmerkmale:
Konsistente und ansprechende Gestaltung

Erfüllte Anforderung: Ansprechende und benutzerfreundliche Website

Risiken: -

### Name Blackbox 1: LLM

*Zweck/Verantwortung*: Integration und Verwendung des LLM zur Generierung von User Stories.

*Schnittstelle(n)*

Aufrufe vom Backend zur Generierung von User Stories.

*(Optional) Qualitäts-/Leistungsmerkmale*

Effiziente und präzise Textgenerierung.

*(Optional) Ablageort/Datei(en)*

src/llm.py

*(Optional) Erfüllte Anforderungen*

Generierung von User Stories.

*(optional) Offene Punkte/Probleme/Risiken*

Abhängigkeit von der Qualität der hochgeladenen PDF-Dateien.

### Name Blackbox 1: Manage Text

*Zweck/Verantwortung*: Bearbeiten von Text und Zwischenspeichern vom Text zur Darstellung auf der Webseite.

*Schnittstelle(n)*

Aufrufe vom Backend zur Bearbeitung oder zum Zwischenspeichern von Text.

*(Optional) Qualitäts-/Leistungsmerkmale*

Bearbeiten/Formatieren von Text aus Eingabe, Extrahieren von Text aus PDF-Dokument, Speichern der Texte in Arrays.

*(Optional) Ablageort/Datei(en)*

src/manage_text.py

*(Optional) Erfüllte Anforderungen*

Extrahieren von Text aus PDF-Dateien

*(optional) Offene Punkte/Probleme/Risiken*

- Abhängigkeit von der Qualität der hochgeladenen PDF-Dateien
- Zugriff auf die Arrays nicht abgekapselt von anderen Benutzern

### Name Blackbox 1: Flask

*Zweck/Verantwortung*: Stellt GUI für die Benutzer bereit, also eine Webseite mit HTML und CSS.

*Schnittstelle(n)*

Stellt APIs bereit. Die Benutzer können so über verschiedene Aktionen Routes aufrufen, die jeweils eine Funktion von
Flask oder den anderen Programmen bieten.

*(Optional) Qualitäts-/Leistungsmerkmale*

Stellt User Interface dar, verbindet alle Funktionen der Programme

*(Optional) Ablageort/Datei(en)*

- src/server.py
- src/template/index.html
- src/statix/main.css

*(Optional) Erfüllte Anforderungen*

- Stellt User Interface dar
- Stellt APIs bereit
- Ruft Infos ab und zeigt diese auf der Webseite dar

*(optional) Offene Punkte/Probleme/Risiken*

- Keine Kapselung der einzelnen Benutzer
- Bei Aktualisierung der Daten muss die komplette Seite neu geladen werden

# Laufzeitsicht

## *Bezeichnung Laufzeitszenario 1*

Laufzeitszenario 1: Hochladen einer PDF-Datei

![LaufzeitSzenario 1 PDF Upload](data/artefacts/Design/LaufzeitSzenario%201%20PDF%20Upload.png)

- hier Besonderheiten bei dem Zusammenspiel der Bausteine in diesem Szenario erläutern

1. Hochladen einer PDF-Datei:
    - Der Benutzer beginnt den Prozess durch das Hochladen einer PDF-Datei über das Frontend
2. Verarbeitung der PDF-Datei:
    - Das Backend empfängt die Datei und ruft die Funktion "/backend/manage/files" auf.
    - Das File manage_text.py extrahiert den Text aus der PDF-Datei mit der Funktion          
      'get_text_from_pdf_file'
    - Anschließend wird der Text dem Backend wieder zurückgegeben
    - Das Backend sendet den bereinigten Text an das Frontend und der Benutzer kann sich den ausgelesenen Inhalt unter '
      ausgelesener Text' auf der Website anzeigen lassen

## *Bezeichnung Laufzeitszenario 2*

Laufzeitszenario 2: User möchte User Story generieren

![Sequenzdiagramm 2 0](data/artefacts/Design/Sequenzdiagramm%202.0.png)

# Verteilungssicht

## Infrastruktur Ebene 1

***Übersichtsdiagramm***

![Deployment Diagramm](data/artefacts/Design/Deployment%20Diagramm.png)

Begründung

Die Verteilung der Komponenten in der Systeminfrastruktur wurde so implementiert um eine klare Trennung der
Verantwortlichkeiten und eine effiziente Nutzung des Gesamtsystem zu gewährleisten. Diese Struktur ermöglicht es durch
eine isolierte und spezialisierte der Komponenten in dem Services isoliert bereitgestellt werden um das Gesamtsystem
bereitzustellen.

Qualitäts- und/oder Leistungsmerkmale

- Skalierbarkeit: Durch die Trennung der Komponenten können diese unabhängig voneinander skaliert werden um mehr
  effizienz zu gewährleisten.
- Wartbarkeit: Durch die klare Trennung der Verantwortlichkeiten wird die Wartung einzelner Komponenten gewährleistet

Zuordnung von Bausteinen zu Infrastruktur

- Client: Der Benutzer interagiert mit der Anwendung über einen Webbrowser. Der Browser sendet HTTP GET und POST
  Anfragen an den Webserver.
- Webserver: Dies ist die Komponente in Form der Gesamten Flask Anwendung, Server.py übernimmt die Koordination der
  Anfragen und Kommunikation der verschiedenen Services
- Services:
    - Manage_text.py: Dies ist ein Service welcher für das Auslesen und Extrahieren der Dateien ist.
    - LLM.py: In diesem Service wird das Sprachmodell verwendet um User Stories zu generieren. Dieser Service wird vom
      Server.py benutzt.

- Datei-Ablage: In der Anwendung selber wird ein Ordner mit src: fileuploads erstellt. Darin werden die Hochgeladenen
  PDF Dateien gespeichert.

# Qualitätsanforderungen

<div class="formalpara-title">

**Weiterführende Informationen**

</div>

Siehe [Qualitätsanforderungen](https://docs.arc42.org/section-10/) in der online-Dokumentation (auf Englisch!).

## Qualitätsbaum

![Qualitätsbaum](https://github.com/hnuDSMProjekt/24_SoSe_StoryGenerator/assets/102808657/769255ce-1944-4a96-9e9f-fd6e3df38699)

| Qualitätsziel          | Überpunkt              | Szenario          | Beispiel          |
|------------------------|------------------------|-------------------|------------------------------------------------------------------------------------------|
| *Analysierbarkeit*     | *Wartbarkeit*          | *User generiert User Story*                 |*Anzeige der generieten User Story im Textfeld*                       |
| *Erweiterbarkeit*      | *Wartbarkeit*          | *Upload einer PDF-Datei*                    |*Hochladen von verschiedenen Dateitypen wie beispielsweise txt.* |
| *Änderbarkeit*         | *Wartbarkeit*          | *Hinzufügen einer Flask Route*              |*Statt User Story zu generieren und regenerieren ist ist jetzt möglich Wörter anzupassen mit regenerieren*   |
| *Interoperabilität*    | *Kompabilität*         | *Flask sendet Daten an Index.html*          |*Flask ruft aus server.py den Text aus manage?text.py ab und gibt ihn an die index.html weiter*  |
| *Korrektheit*          | *Funktionale Eignung*  | *Flask yeigt den Text auf der Webseite an*  |*Der Text wird als String übergeben in einem korrekten Format*  |
| *Zeitverhalten*        | *Effizienz*            | *Benutzer drückt den Buttons Generieren *   |*Generieren einer User Story*  |
| *Fehlervermeidung*     | *Benutzbarkeit*        | *Ein Benutzer möchte eine korrekte Ausgabe einer User Story*  |* Unpassender User Story Output*               |
| *Bedienbarkeit*        | *Benutzbarkeit*        | *Der User bekommt einen Löschen Button*  |*Als Benutzer kann ich unerwünschte Elemente entfernen, bevor ich damit arbeite*  |
| *Fehlertoleranz*       | *Zuverlässigkeit*      | *Der String soll in einer Checkbox angezeigt werden*  |*Der String wird vom LLM an manage?text.py übergeben, wo er dann korrekt formatiert wird*  |

# Risiken und technische Schulden

## Flask

### User IDs

Aktuell bekommen alle Benutzer der Webseite den Zugriff auf den gleichen Inhalt wie die Listen, in denen die
Personas/Problembeschreibungen aufgeführt werden. Es würde sich daher anbieten mit Flask jedem User eine eigene ID zu
vergeben. Damit würden die User individuell abgekapselt werden von den anderen und jeder kann mit seinen eigenen Dateien
und Informationen arbeiten.

### Die Listen für Persona/Problembeschreibung und User Stories

Aktuell werden alle Personas/Problembeschreibungen in der gleichen Liste gespeichert. Genau wie die User Stories in der
gleichen Liste gespeichert werden. Das bringt folgende Probleme mit sich:

- Keine Persistenz: Falls der Host ausfällt und sich Elemente der Listen im Speicher befinden verschwinden diese
- Keine Trennung aller Benutzer: Jeder Benutzer greift gleichermaßen auf alle Liste zu. Das kann zu Komplikationen
  führen beim Daten separieren.
- Ineffizienz: Je nachdem wie viele Benutzer gleichzeitig darauf zugreifen kann es zu starken Verzögerungen kommen und
  es ist generell eine ineffiziente Lösung.

Als Lösung bietet sich an die Listen durch eine Datenbank zu ersetzen (SQLite, MySQL, PostgreSql, ...). Dadurch ist
persistenz gewährleistet (solange die Datenbank auf einem Datenträger initialisiert wurde), man kann Benutzer durch IDs
in den Tables trennen plus der Workload würde von Flask abgenommen und an das Datenbanksystem übergeben werden.

## Responsiveness

Flask stellt aktuell reine HTML und CSS Seiten zur Verfügung. Das hat den Vorteil, dass die Seite sehr effizient und
ressourcenschonend ist. Allerdings ist Sie ohne JavaScript nicht responsive, d.h. wenn Elemente auf der Seite sich
ändern, muss die Seite komplett neu geladen werden.

Es war die Intention dieses Projekt nur mit Python, HTML und CSS zu bewerkstelligen. Das ist der Übersicht geschuldet.
Sollte man das Design der Website zu einem One-Pager umbauen wollen, würde sich z.B. Vue.js anbieten, ein JavaScript
Framework, welches mit dem Vue-Lifecycle die Option bietet nur bestimmte Elemente der Website bei Bedarf neu zu laden.
Wer nicht auf ein JavaScript-Framework ausweichen möchte und eventuelle Update inkompatibilitäten aus dem Weg gehen
will, kann HTMX in Betracht ziehen. HTMX lässt sich in HTML Elemente einbauen und gibt so die Möglichkeit, mit
JavaScript, bestimmte Elemente bei Bedarf neu laden zu können, ohne jedes Mal die komplette Seite zu aktualisieren.

Wurden ein Datenbanksystem implementiert und Elemente der Webseite lassen sich einzeln bei Bedarf aktualisieren, so kann
darüber nachgedacht werden Tables der Datenbank der zugehörigen Benutzer anzeigen zu lassen. Das gibt auch die
Möglichkeit Suchen nochmals zu filtern.

## Large Language Model (LLM)

### GPU oder CPU

Das [LLM](llm.py) ist so konfiguriert, dass alle Berechnungen für die Eingaben mit der CPU getätigt werden (
gpu_layers=0). Sollte dieses Projekt auf einem Host laufen mit einer entsprechend starken GPU (mindestens 8 oder 12GiB
VRam) könnte es Sinn machen die gpu_layers zu aktivieren und konfigurieren. Die Vektorberechnungen mit dem LLM werden
mit einer GPU effizienter gemacht als mit einer CPU. Ausgaben zu bekommen sollte also schneller passieren.

### Ausgabe verfeinern

Es kann in seltenen Fällen vorkommen, dass die Formatierung der Ausgabe nicht passt und das Ergebnis auf der Webseite
nicht korrekt angezeigt wird. Auch kann es in seltenen Fällen vorkommen, dass die User Stories nicht wirklich den
Kontext abdecken oder sich generell als User Stories eignen. Es wurde bereits Unternehmungen gestartet ein Prompt
Engineering durchzuführen, um bessere User Stories generiert zu bekommen. Entsprechende Datensätze zu Personas und
zugehörigen Outputs finden sich [hier](data/artefacts). Wir konnten aber die Qualität der User Stories schon deutlich
durch das Anpassen des Input Prompts von [llm.py](llm.py) steigern und haben das Prompt Engineering verworfen. Sollte es
zu bestimmten Edge Cases kommen, mit minderer Qualität der User Stories, kann entweder der Prompt weiter angepasst
werden, oder tatsächlich ein Prompt Engineering in Betracht gezogen werden.

## Text Management

In [manage_text.py](manage_text.py) wird jeweils die erste Seite eines PDF-Dokuments ausgelesen, um den Text dort zu
extrahieren. Sollte es zukünftig nötig sein mehrere Seiten von einem einzelnen PDF-Dokument auszulesen, kann man den
Programmcode von get_text_from_pdf_file anpassen, um über mehrere Seiten mit einer For-Loop zu iterieren.

## Docker

Zum Zeitpunkt des Erstellens dieses Projekt haben wir uns für Python Version 3.11 entschieden, da dies die neueste
Version ist, die die aktuelle PyTorch Version 2.3.1 unterstützt. Zukünftig kann es aber vorkommen, dass z.B. diese
PyTorch Version auf der [Homepage](https://pytorch.org/get-started/locally/) oder
dem [Archiv](https://pytorch.org/get-started/previous-versions/) nicht mehr verfügbar ist. Gründe dafür können
schwerwiegende Bugs sein oder unzureichende Performance der alten Version bei der Vorstellung einer neuen Version. Hier
würde es sich Anbieten mit Docker zu arbeiten und von diesem Projekt ein entsprechendes Docker Image zu erstellen.
Dieses ist nach dem Erstellen dauerhaft verfügbar und ändert sich nicht mehr. Falls man das Projekt auf einem Host neu
aufsetzen muss, hat man keine Probleme mehrere Python Requirements aufzulösen/beheben die unter Umständen in der Zukunft
miteinander inkompatibel sind. Außerdem ist ein Docker Image in sich selbst gekapselt und hat in der Regel keinen
Zugriff auf den Host. Das bietet zusätzliche Sicherheit im Netzwerk und schützt vor einer Kompromittierung oder einen
unerlaubten Zugriff am Host durch Dritte. Mit Versionierung der Docker Images kann man eine immer funktionierende
Variante dieses Projekt rechnen und dann bei Bedarf Versionen von Python oder den Python Requirements ändern im Falle
von z.B. einer Sicherheitslücke. Anschließend das neue Image mit einer entsprechenden Versioniereng erstellen. I.d.R.
sollten Docker Images nach einem erfolgreichen Erstellen laufen bei einer korrekten Konfiguration. Sollte es zum
Zeitpunkt des Erstellens eines Images schon zu Konflikten kommen wird abgebrochen, bis die Probleme in den Requirements
behoben wurden.

# Glossar

| Begriff        | Definition        |
|----------------|-------------------|
| *LLM* | *Ein Large Language Model um Texte zu generieren* |
| *PyTorch*  | *Wird in Verbindung mit dem LLM benutzt, um Ausgaben zu generieren* |
| *Hugging Face*  | *Eine Platform die Community Driven ist und LLM-Modelle anbietet* |
| *Flask*  | *Ein Python Framework mit welchem sich Webseiten realisieren lassen* |
