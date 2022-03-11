# Übersetzung ins Deutsche

## Übersetzungsfortschritt

Vorwort:

- [x] A0-preface.mkd

Inhaltskapitel:

- [x] 01-intro.mkd
- [x] 02-variables.mkd
- [x] 03-conditional.mkd
- [x] 04-functions.mkd
- [x] 05-iterations.mkd
- [x] 06-strings.mkd
- [x] 07-files.mkd
- [x] 08-lists.mkd
- [x] 09-dictionaries.mkd
- [x] 10-tuples.mkd
- [x] 11-regex.mkd
- [x] 12-network.mkd
- [x] 13-web.mkd
- [x] 14-objects.mkd
- [x] 15-database.mkd
- [x] 16-viz.mkd

Appendix:

- [x] AA-contrib.mkd
- [x] AB-copyright.mkd

## Allgemeines

- Deutsche Anführungszeichen im Fließtext verwenden: nicht "...", sondern „...“
- Darauf achten, dass in der Übersetzung Backticks (`` ` ``) erhalten bleiben (zur Auszeichnung von Code mit Markdown).
- Eine `.mkd`-Datei muss zwingend mit **zwei** Leerzeilen schließen, damit beim Kompilieren die nächste Kapitelüberschrift als solche erkannt wird.
- Die Zeilen eines Absatzes vorzugsweise zusammenführen.
- Englische Begriffe, für die eine etablierte deutsche Übersetzungen existiert, sollten bei der ersten Einführung des Begriffs in Klammern genannt werden (sofern der englische Begriff auch im Deutschen geläufig ist). Zum Beispiel: `Eine Zeichenkette (englisch *String*) ist eine Folge einzelner Zeichen (englisch *Character*).`

## Übersetzungstabellen

Übersetzungstabellen zum Zwecke einer einheitlichen Übersetzung. Übersetzungen gelten kapitelübergreifend und werden hier nicht doppelt aufgeführt. Bitte die Suchfunktion verwenden. In erster Linie geht es hier um das Festlegen sinnvoller und einheitlicher Indexeinträge. Bitte unbedingt diese Übersetzungen hier verwenden; Änderung nur nach Rücksprache vornehmen.

### Änderungen

Skript für Änderungen:

```
#!/bin/bash

for chapter in *.mkd
do
    sed -i 's/xxx/yyy/g' "$chapter" # escape backslashes
    echo "$chapter"
done
```

Mit Bedacht verwenden und **nicht** für alleinstehende Wörter, also nur für mit Markdown/LaTeX ausgezeichnete Sequenzen wie Indexeinträge.

### Kapitel 1

```
\index{hardware} : \index{Hardware}
\index{hardware!architecture} : \index{Hardware!Architektur}
\index{problem solving} : \index{Problemlösung}
\index{programming language} : \index{Programmiersprache}
\index{language!programming} : \index{Sprache!Programmieren}
\index{script} : \index{Skript}
\index{program} : \index{Programm}
\index{typographical error} : \index{typographischer Fehler}
\index{experimental debugging} : \index{experimentelles Debugging}
\index{random walk programming} : WEG
\index{development plan!random walk programming} : \index{Vorgehensmodell}
\index{bug} : \index{Bug}
\index{central processing unit} : \index{Central Processing Unit}\index{Prozessor}
\index{CPU} : \index{CPU}
\index{compile} : \index{Kompilieren}
\index{high-level language} : \index{High-Level-Sprache}\index{Hochsprache}
\index{interpret} : \index{Interpretieren}
\index{low-level language} : \index{Low-Level-Sprache}\index{Maschinencode}
\index{machine code} : \index{Maschinencode}
\index{main memory} : \index{Hauptspeicher}
\index{parse} : \index{Parsen}
\index{portability} : \index{Portabilität}
\index{print function} : \index{print (Funktion)}
\index{function!print} : \index{Funktion!print}
\index{semantics} : \index{Semantik}
\index{source code} : \index{Quellcode}

```

### Kapitel 2

```
\index{value} : \index{Wert}
\index{type} : \index{Datentyp}
\index{string} : \index{Zeichenkette}
\index{class!str} : \index{Klasse!str}
String : Zeichenkette
\index{quotation mark} : \index{Anführungszeichen}
\index{int type} : \index{Ganzzahl}
\index{class!int} : \index{Klasse!int}
\index{float type} : \index{Gleitkommazahl}
\index{class!float} : \index{Klasse!float}
\index{semantic error} : \index{semantischer Fehler}
\index{error!semantic} : \index{Fehler!semantischer}
\index{error message} : \index{Fehlermeldung}
\index{variable} : \index{Variable}
name : Bezeichner
\index{assignment statement} : \index{Zuweisung}
\index{statement!assignment} : \index{Anweisung!Zuweisung}
\index{keyword} : \index{Schlüsselwort}
\index{underscore character} : \index{Unterstrich}
\index{statement} : \index{Anweisung}
\index{interactive mode} : \index{interaktiver Modus}
\index{script mode} : \index{Skriptmodus}
\index{operator, arithmetic} : \index{Operator!arithmetisch}
\index{arithmetic operator} : \index{arithmetischer Operator}
\index{operand} : \index{Operand}
\index{operator} : \index{Operator}
\index{expression} : \index{Ausdruck}
\index{floating-point division} : \index{Fließkommadivision}
\index{division!floating-point} : \index{Division!Fließkomma}
\index{evaluate} : \index{Auswertung}
**Exercise : **Übung
\index{order of operations} : \index{Auswertungsreihenfolge}
\index{rules of precedence} : \index{Vorrangregeln}
\index{precedence} : \index{Vorrang}
\index{parentheses!overriding precedence} : \index{Klammern!Vorrangregeln überschreiben}
\index{modulus operator} : \index{Modulo (Operator)}
\index{operator!modulus} : \index{Operator!Modulo}
\index{string!operation} : \index{Zeichenkette!Operation}
\index{operator!string} : \index{Operator!Zeichenkette}
\index{divisibility} : \index{Teilbarkeit}
\index{concatenation} : \index{Konkatenation}
\index{keyboard input} : \index{Benutzereingaben}
\index{prompt} : \index{Prompt}
\index{newline} : \index{Newline}
\index{comment} : \index{Kommentar}
\index{syntax error} : \index{Syntaxfehler}
\index{error!syntax} : \index{Fehler!syntax}
\index{exception} : \index{Ausnahme}
\index{exception!ValueError} : \index{Ausnahme!ValueError}
\index{runtime error} : \index{Laufzeitfehler}
\index{error!runtime} : \index{Fehler!Laufzeit}
\index{case-sensitivity, variable names} : \index{Groß-/Kleinschreibung}
Glossary : Glossar
assignment : Zuweisung
\index{assignment} : \index{Zuweisung}
\index{floating-point} : \index{Gleitkommazahl}
\index{integer} : \index{Ganzzahl}
Exercises : Übungen
```

### Kapitel 3

```
Conditional execution : Bedingte Ausführung
\index{boolean expression} : \index{boolescher Ausdruck}
\index{expression!boolean} : \index{Ausdruck!boolescher}
\index{logical operator} : \index{logischer Operator}
\index{operator!logical} : \index{Operator!logischer}
\index{True special value} : \index{True (Wahrheitswert)}
\index{special value!True} : \index{Wert!True}
\index{special value!False} : \index{Wert!False}
\index{False special value} : \index{False (Wahrheitswert)}
\index{bool type} : \index{bool (Datentyp)}
\index{type!bool} : \index{Datentyp!bool}
\index{comparison operator} : \index{Vergleichsoperator}
\index{operator!comparison} : \index{Operator!Vergleich}
\index{and operator} : \index{and (Operator)}
\index{or operator} : \index{or (Operator)}
\index{not operator} : \index{not (Operator)}
\index{Operator!and} : \index{Operator!and}
\index{Operator!or} : \index{Operator!or}
\index{Operator!not} : \index{Operator!not}
\index{conditional statement} : \index{bedingte Anweisung}
\index{statement!conditional} : \index{Anweisung!bedingte}
\index{if statement} : \index{if (Anweisung)}
\index{statement!if} : \index{Anweisung!if}
\index{conditional executions} : \index{bedingte Ausführung}
\index{condition} : \index{Bedingung}
\index{compound statement} : \index{zusammengesetzte Anweisung}
\index{statement!compound} : \index{Anweisung!zusammengesetzte}
\index{pass statement} : \index{pass (Anweisung)}
\index{statement!pass} : \index{Anweisung!pass}
Chevrons : Größer-Zeichen
Alternative execution : Alternative Ausführung
\index{alternative execution} : \index{alternative Ausführung}
\index{else keyword} : \index{else (Schlüsselwort)}
\index{keyword!else} : \index{Schlüsselwort!else}
\index{branch} : \index{Verzweigung}
\index{chained conditional} : \index{verkettete Bedingung}
\index{conditional!chained} : \index{Bedingung!verkettete}
\index{elif keyword} : \index{elif (Schlüsselwort)}
\index{keyword!elif} : \index{Schlüsselwort!elif}
\index{nested conditional} : \index{verschachtelte Bedingung}
\index{conditional!nested} : \index{Bedingung!verschachtelte}
\index{traceback} : \index{Traceback}
\index{short circuit} : \index{verkürzte Auswertung}\index{short circuit}
guardian pattern : Wächter-Muster
\index{guardian pattern} : \index{Wächter-Muster}
\index{pattern!guardian} : \index{Muster!Wächter}
\index{debugging} : \index{Debugging}
\index{whitespace} : \index{Whitespace}
body : Block
\index{body} : \index{Block}
```

### Kapitel 4

```
\index{function call} : \index{Funktionsaufruf}
\index{argument} : \index{Argument}
\index{return value} : \index{Rückgabewert}
\index{type conversion} : \index{Typumwandlung}
\index{conversion!type} : \index{Umwandlung!Datentyp}
\index{int function} : \index{int (Funktion)}
\index{function!int} : \index{Funktion!int}
\index{parentheses!argument in} : \index{Klammern!Argument in}
\index{float function} : \index{float (Funktion)}
\index{function!float} : \index{Funktion!float}
\index{str function} : \index{str (Funktion)}
\index{function!str} : \index{Funktion!str}
\index{math function} : \index{math (Modul)}
\index{module} : \index{Modul}
\index{module object} : \index{Modulobjekt}
\index{dot notation} : \index{Punktnotation}
\index{log function} : \index{log (Funktion)}
\index{function!log} : \index{Funktion!log}
\index{sine function} : \index{sine (Funktion)}
\index{trigonometric function} : \index{trigonometrische Funktion}
\index{sqrt function} : \index{sqrt (Funktion)}
\index{function!sqrt} : \index{Funktion!sqrt}
\index{random number} : \index{Zufallszahl}
\index{deterministic} : \index{deterministisch}
\index{pseudorandom} : \index{pseudozufällig}
\index{random module} : \index{random (Modul)}
\index{module!random} : \index{Modul!random}
\index{random function} : \index{random (Funktion)}
\index{function!random} : \index{Funktion!random}
\index{randint function} : \index{randint (Funktion)}
\index{function!randint} : \index{Funktion!randint}
\index{choice function} : \index{choice (Funktion)}
\index{function!choice} : \index{Funktion!choice}
\index{function} : \index{Funktion}
\index{function definition} : \index{Funktionsdefinition}
\index{definition!function} : \index{Definition!Funktion}
\index{def keyword} : \index{def (Schlüsselwort)}
\index{keyword!def} : \index{Schlüsselwort!def}
\index{parentheses!empty} : \index{Klammern!leer}
\index{parentheses!parameters in} : \index{Klammern!Parameter in}
\index{header} : \index{Funktionskopf}
\index{body} : \index{Funktionsrumpf}
\index{indentation} : \index{Einrückung}
\index{colon} : \index{Doppelpunkt}
\index{ellipses} : \index{Ellipse (Auslassungspunkte)}\index{Auslassungspunkte (Ellipse)}
\index{function object} : \index{Funktionsobjekt}
\index{object!function} : \index{Objekt!Funktion}
\index{parameter} : \index{Parameter}
\index{function parameter} : \index{Funktionsparameter}
\index{function argument} : \index{Funktionsargument}
\index{fruitful function} : \index{Rückgabewert einer Funktion}
\index{void function} : \index{void-Funktion}
\index{function, fruitful} : \index{Funktion mit Rückgabewert}
\index{function, void} : \index{Funktion ohne Rückgabewert, void}
\index{None special value} : \index{None (Wert)}
\index{special value!None} : \index{Wert!None}
\index{function, reasons for} : \index{Funktionen}
\index{flow of execution} : \index{Programmablauf}
import statement : Importanweisung
\index{import statement} : \index{Importanweisung}
\index{statement!import} : \index{Anweisung!import}
\index{pi} : \index{pi (Konstante)}
```

### Kapitel 5

```
\index{iteration} : \index{Iteration}
\index{update} : \index{Aktualisierung}
\index{variable!updating} : \index{Variable!aktualisieren}
\index{initialization (before update)} : \index{Initialisierung}
\index{increment} : \index{Inkrementieren}
\index{decrement} : \index{Dekrementieren}
\index{statement!while} : \index{Anweisung!while}
\index{while loop} : \index{while-Schleife}
\index{loop!while} : \index{Schleife!while}
\index{loop} : \index{Schleife}
\index{infinite loop} : \index{Endlosschleife}
\index{loop!infinite} : \index{Schleife!endlos}
\index{break statement} : \index{break (Anweisung)}
\index{statement!break} : \index{Anweisung!break}
\index{continue statement} : \index{continue (Anweisung)}
\index{statement!continue} : \index{Anweisung!continue}
\index{for statement} : \index{for-Schleife}
\index{statement!for} : \index{Schleife!for}
\index{accumulator!sum} : \index{Akkumulator!Summe}
\index{loop!maximum} : \index{Schleife!Maximum}
\index{loop!minimum} : \index{Schleife!Minimum}
\index{debugging!by bisection} : \index{Debugging!mittels Bisektion}
\index{bisection, debugging by} : \index{Bisektion, Debugging mittels}
\index{accumulator} : \index{Akkumulator}
\index{counter} : \index{Schleifenzähler}
```

### Kapitel 6

```
\index{sequence} : \index{Folge}
\index{character} : \index{Einzelzeichen}\index{Character}
\index{bracket operator} : \index{Indexoperator}\index{Zugriff, indexbasiert}
\index{operator!bracket} : \index{Operator!indexbasierter Zugriff}
\index{index} : \index{Index}
\index{} : \index{} 
\index{index!starting at zero} : \index{Index!beginnt mit Null}
\index{zero, index starting at} : \index{Null, Index beginnt mit}
\index{exception!TypeError} : \index{Ausnahme!TypeError}
\index{TypeError} : \index{TypeError}
\index{len function} : \index{len (Funktion)}
\index{function!len} : \index{Funktion!len}
\index{exception!IndexError} : \index{Ausnahme!IndexError}
\index{IndexError} : \index{IndexError}
\index{index!negative} : \index{Index!negativ}
\index{negative index} : \index{negativer Index}
\index{traversal} : \index{Traversieren}
\index{loop!traversal} : \index{Schleife!Traversieren}
\index{for loop} : \index{for-Schleife}
\index{loop!for} : \index{Schleife!for}
\index{slice operator} : \index{slice-Operator}
\index{operator!slice} : \index{Operator!slice}
\index{index!slice} : \index{Index!slice}
\index{string!slice} : \index{Zeichenkette!slice}
\index{slice!string} : \index{slice!Zeichenkette}
\index{copy!slice} : \index{Kopieren!slice}
\index{slice!copy} : \index{slice!Kopieren}
\index{mutability} : \index{Veränderbarkeit}
\index{immutability} : \index{Unveränderlichkeit}
\index{string!immutable} : \index{Zeichenkette!unveränderlich}
\index{object} : \index{Objekt}
\index{item assignment} : \index{Elementzuweisung}
\index{assignment!item} : \index{Zuweisung!Element}
\index{counting and looping} : \index{Zählen mit Schleifen}
\index{looping and counting} : \index{Schleifen und Zählen}
\index{looping!with strings} : \index{Schleife!mit Zeichenketten}\index{Iteration!durch Zeichenketten}
\index{encapsulation} : \index{Auslagern von Code}
\index{in operator} : \index{in (Operator)}
\index{operator!in} : \index{Operator!in}
\index{boolean operator} : \index{boolescher Operator}
\index{operator!boolean} : \index{Operator!boolescher}
\index{string!comparison} : \index{Zeichenkette!Vergleich}
\index{comparison!string} : \index{Vergleich!Zeichenkette}
\index{method} : \index{Methode}
\index{string!method} : \index{Zeichenkette!Methode}
\index{invocation} : \index{Aufruf einer Methode}
\index{optional argument} : \index{optionales Argument}
\index{argument!optional} : \index{Argument!optional}
\index{count method} : \index{count (Methode)}
\index{method!count} : \index{Methode!count}
\index{format operator} : \index{Formatierungsoperator}
\index{operator!format} : \index{Operator!Formatierung}
\index{format string} : \index{Format-String}
\index{format sequence} : \index{Formatierungszeichen}
format string : Format-String
format sequence : Formatierungszeichen
\index{empty string} : \index{leere Zeichenkette}
format operator : Formatierungsoperator
flag : Flag
\index{flag} : \index{Flag}
item : Element
\index{item} : \index{Element}
\index{search pattern} : \index{Suchmuster}
\index{pattern!search} : \index{Muster!Suche}
\index{slice} : \index{Teilzeichenkette}
\index{string method} : \index{Zeichenkette!Methode}
\index{method!string} : \index{Methode!Zeichenkette}
```

### Kapitel 7

```
\index{file} : \index{Datei}
\index{type!file} : \index{Datentyp!Datei}
\index{persistence} : \index{Persistenz}
\index{secondary memory} : \index{Sekundärspeicher}
\index{file!open} : \index{Datei!öffnen}
\index{open function} : \index{open (Funktion)}
\index{function!open} : \index{Funktion!open}
\index{file handle} : \index{Dateihandler}
\index{file!reading} : \index{Datei!lesen}
file handle : Dateihandler
\index{filter pattern} : \index{Filtermuster}
\index{pattern!filter} : \index{Muster!Filter}
line slicing : Zeilen-Slicing
\index{Quality Assurance} : \index{Qualitätssicherung}
\index{QA} : \index{QS}
\index{try statement} : \index{try (Anweisung)}
\index{statement!try} : \index{Anweisung!try}
\index{exception!IOError} : \index{Ausnahme!IOError}
\index{file!writing} : \index{Datei!schreiben}
\index{close method} : \index{close (Methode)}
\index{method!close} : \index{Methode!close}
\index{repr function} : \index{repr (Funktion)}
\index{function!repr} : \index{Funktion!repr}
\index{string representation} : \index{Stringrepräsentation}
\index{end of line character} : \index{Zeilenendezeichen}
\index{catch} : \index{Auffangen einer Ausnahme}
\index{text file} : \index{Textdatei}
```

### Kapitel 8

```
\index{list} : \index{Liste}
\index{type!list} : \index{Datentyp!Liste}
\index{nested list} : \index{verschachtelte Liste}
\index{list!nested} : \index{Liste!verschachtelt}
\index{empty list} : \index{leere Liste}
\index{list!empty} : \index{Liste!leer}
\index{list!element} : \index{Liste!Element}
\index{access} : \index{Zugriff}
\index{list!index} : \index{Liste!Index}
\index{list!traversal} : \index{Liste!Traversieren}
\index{traversal!list} : \index{Traversieren!Liste}
\index{looping!with indices} : \index{Schleife!mit Indizes}\index{Iteration!mit Indizes}
\index{index!looping with} : \index{Index!mit Schleifen}
\index{item update} : \index{Elementaktualisierung}
\index{update!item} : \index{Aktualisierung!Element}
\index{list!operation} : \index{Liste!Operation}
\index{concatenation!list} : \index{Konkatenation!Liste}
\index{list!concatenation} : \index{Liste!Konkatenation}
\index{repetition!list} : \index{Wiederholung!Liste}
\index{list!repetition} : \index{Liste!Wiederholung}
\index{list!slice} : \index{Liste!slice}
\index{slice!list} : \index{slice!Liste}
\index{list!copy} : \index{Liste!Kopieren}
\index{slice!update} : \index{slice!Aktualisierung}
\index{update!slice} : \index{Aktualisierung!slice}
\index{list!method} : \index{Liste!Methode}
\index{method, list} : \index{Methode!Listen}
\index{append method} : \index{append (Methode)}
\index{method!append} : \index{Methode!append}
\index{extend method} : \index{extend (Methode)}
\index{method!extend} : \index{Methode!extend}
\index{sort method} : \index{sort (Methode)}
\index{method!sort} : \index{Methode!sort}
\index{void method} : \index{void-Methode}
\index{method!void} : \index{Methode!void}
\index{element deletion} : \index{Element löschen}
\index{deletion, element of list} : \index{Löschen, Listenelement}
\index{pop method} : \index{pop (Methode)}
\index{method!pop} : \index{Methode!pop}
\index{del operator} : \index{del (Operator)}
\index{operator!del} : \index{Operator!del}
\index{remove method} : \index{remove (Methode)}
\index{method!remove} : \index{Methode!remove}
\index{list!function} : \index{list!Funktion}
\index{function!list} : \index{Funktion!list}
\index{split method} : \index{split (Methode)}
\index{method!split} : \index{Methode!split}
\index{delimiter} : \index{Delimiter}
\index{join method} : \index{join (Methode)}
\index{method!join} : \index{Methode!join}
\index{string!empty} : \index{Zeichenkette!leer}
\index{aliasing} : \index{Alias}
\index{is operator} : \index{is (Operator)}
\index{operator!is} : \index{Operator!is}
\index{equivalence} : \index{Äquivalenz}
\index{identity} : \index{Identität}
\index{reference!aliasing} : \index{Referenz!Alias}
\index{reference} : \index{Referenz}
\index{list!as argument} : \index{Liste!als Argument}
\index{argument!list} : \index{Argument!Liste}
\index{idiom} : \index{Idiom}
\index{aliasing!copying to avoid} : \index{Alias!Vermeidung durch Kopieren}
\index{copy!to avoid aliasing} : WEG
\index{equivalent} : \index{äquivalent}
\index{identical} : \index{identisch}
```

### Kapitel 9

```
\index{dictionary} : \index{Dictionary}
\index{type!dict} : \index{Datentyp!dict}
\index{key} : \index{Schlüssel}\index{Key}
\index{key-value pair} : \index{Key-Value-Paar}\index{Schlüssel-Wert-Paar}
\index{dict function} : \index{dict (Funktion)}
\index{function!dict} : \index{Funktion!dict}
\index{squiggly bracket} : \index{geschweifte Klammern}
\index{bracket!squiggly} : \index{Klammern!geschweift}
\index{exception!KeyError} : \index{Ausnahme!KeyError}
\index{membership!dictionary} : \index{Zugehörigkeit!Dictionary}
\index{values method} : \index{values (Methode)}
\index{method!values} : \index{Methode!values}
\index{hash table} : \index{Hashtabelle}
\index{set membership} : \index{Menge, Zugehörigkeit}\index{Set, Zugehörigkeit}
\index{membership!set} : \index{Zugehörigkeit!Menge (Set)}
\index{implementation} : \index{Implementation}\index{Implementierung}
\index{histogram} : \index{Histogramm}
\index{frequency} : \index{Häufigkeit}
\index{get method} : \index{get (Methode)}
\index{method!get} : \index{Methode!get}
\index{nested loops} : \index{verschachtelte Schleifen}
\index{loop!nested} : \index{Schleife!verschachtelt}
\index{Romeo and Juliet} : \index{Romeo and Juliet}
\index{dictionary!looping with} : \index{Dictionary!Iteration durch}
\index{looping!with dictionaries} : \index{Schleife!über Dictionary}\index{Iteration!durch Dictionary}
\index{keys method} : \index{keys (Methode)}
\index{method!keys} : \index{Methode!keys}
\index{sanity check} : \index{Plausibilitätsprüfung}
\index{consistency check} : \index{Konsistenzprüfung}
\index{hashtable} : \index{Hashtabelle}
\index{hash function} : \index{Hashfunktion}
\index{lookup} : \index{Lookup}
lookup : Lookup
\index{comparable} : \index{vergleichbar}
\index{parentheses!tuples in} : \index{Klammern!Tupeln innerhalb}
```

### Kapitel 10

```
\index{tuple} : \index{Tupel}
\index{type!tuple} : \index{Datentyp!Tupel}
\index{hashable} : \index{hashbar}
\index{singleton} : \index{Singleton}
\index{tuple!singleton} : \index{Tupel!Singleton}
\index{tuple function} : \index{tuple (Funktion)}
\index{function!tuple} : \index{Funktion!tuple}
\index{tuple!slice} : \index{Tupel!slice}
\index{slice!tuple} : \index{slice!Tupel}
\index{comparison!tuple} : \index{Vergleich!Tupel}
\index{tuple!comparison} : \index{Tupel!Vergleich}
\index{DSU pattern} : \index{DSU-Muster}
\index{pattern!DSU} : \index{Muster!DSU}
\index{decorate-sort-undecorate pattern} : WEG
\index{pattern!decorate-sort-undecorate} : \index{Muster!Decorate-Sort-Undecorate}
\index{keyword argument} : \index{Schlüsselwortargument}
\index{argument!keyword} : \index{Argument!Schlüsselwort}
\index{tuple!assignment} : \index{Tupel!Zuweisung}
\index{assignment!tuple} : \index{Zuweisung!Tupel}
\index{swap pattern} : \index{Swap (Muster)}
\index{pattern!swap} : \index{Muster!Swap}
\index{email address} : \index{E-Mail-Adresse}
\index{items method} : \index{items (Methode)}
\index{method!items} : \index{Methode!items}
\index{traverse!dictionary} : \index{Traversieren!Dictionary}
\index{dictionary!traversal} : \index{Dictionary!Traversieren}
\index{tuple!as key in dictionary} : \index{Tupel!als Schlüssel in Dictionaries}
\index{tuple!in brackets} : \index{Tupel!geklammert}
\index{sorted function} : \index{sorted (Funktion)}
\index{function!sorted} : \index{Funktion!sorted}
\index{reversed function} : \index{reversed (Funktion)}
\index{function!reversed} : \index{Funktion!reversed}
\index{data structure} : \index{Datenstruktur}
\index{shape error} : WEG
\index{error!shape} : WEG
\index{tuple assignment} : \index{Tupelzuweisung}
\index{letter frequency} : \index{Buchstabenhäufigkeit}
\index{frequency!letter} : \index{Häufigkeit!Buchstaben}
```

### Kapitel 11

```
\index{regular expressions} : \index{regulärer Ausdruck}
\index{regex} : \index{Regex}
\index{re module} : \index{re (Modul)}
\index{regex!search} : \index{Regex!search}
\index{string!find} : \index{Zeichenkette!find}
\index{string!startswith} : \index{Zeichenkette!startswith}
\index{wild card} : \index{Wildcard}
\index{regex!wild card} : \index{Regex!Wildcard}
\index{findall} : \index{findall (Methode)}
\index{regex!findall} : \index{Regex!findall}
\index{regex!character sets(brackets)} : \index{Regex!Zeichenklassen}
\index{string!split} : \index{Zeichenkette!split}
\index{regex!parentheses} : \index{Regex!runde Klammern}
\index{parentheses!regular expression} : \index{runde Klammern!regulärer Ausdruck}
\index{grep} : \index{grep}
\index{greedy} : \index{greedy}
\index{greedy matching} : \index{greedy Matching}
```

### Kapitel 12

```
\index{urllib!image} : \index{urllib!Bild}
\index{image!jpg} : \index{Bild!jpg}
\index{time.sleep} : \index{time.sleep (Funktion)}
\index{flow control} : \index{flow control}\index{Flusskontrolle}
\index{binary file} : \index{Binärdatei}\index{binary}
\index{web!scraping} : \index{Web-Scraping}
\index{parsing HTML} : \index{HTML!parsen}
\index{non-greedy} : \index{non-greedy}
\index{port} : \index{Port}
\index{socket} : \index{Socket}
\index{spider} : \index{Spider}
```

### Kapitel 13

```
\index{ElementTree} : \index{ElementTree XML-Parser}
\index{API!key} : \index{API-Schlüssel}
\index{web service} : \index{Webservice}
\index{rate limiting} : WEG
\index{geocoding} : \index{Geocoding}
\index{eXtensible Markup Language} : \index{eXtensible Markup Language (XML)}
```

### Kapitel 14

```
\index{object-oriented} : \index{objektorientiert}
\index{list object} : \index{list (Objekt)}
\index{parsing!HTML} : \index{Parsen!HTML}
\index{class keyword} : \index{class (Schlüsselwort)}\index{Schlüsselwort!class}
\index{construct} : \index{konstruieren}
\index{instance} : \index{Instanz}
\index{class} : \index{Klasse}
\index{dir} : \index{dir (Funktion)}
\index{constructor} : \index{Konstruktor}
\index{destructor} : \index{Destruktor}
\index{object lifecycle} : \index{Lebenszyklus von Objekten}\index{Objekt-Lebenszyklus}
\index{attribute} : \index{Attribut}
\index{child class} : \index{abgeleitete Klasse}
\index{inheritance} : \index{Vererbung}
\index{message} : WEG
\index{parent class} : \index{Basisklasse}
```

### Kapitel 15

```
\index{database} : \index{Datenbank}
\index{database!indexes} : \index{Datenbank!Index}
\index{sqlite3 module} : \index{sqlite3 (Modul)}
\index{module!sqlite3} : \index{Modul!sqlite3}
\index{connect function} : \index{connect (Funktion)}
\index{function!connect} : \index{Funktion!connect}
\index{cursor function} : \index{cursor (Funktion)}
\index{function!cursor} : \index{Funktion!cursor}
\index{constraint} : \index{Constraint}
\index{cursor} : \index{Cursor}
\index{database browser} : \index{Datenbankenbrowser}
\index{foreign key} : \index{Fremdschlüssel}
\index{logical key} : \index{Logischer Schlüssel}
\index{normalization} : \index{Normalisierung}
\index{database normalization} : \index{Datenbanknormalisierung}
\index{primary key} : \index{Primärschlüssel}
\index{relation} : \index{Relation}
```

### Kapitel 16

```
\index{Google!map} : \index{Google!Map}
\index{Visualization!map} : \index{Visualisierung!Map}
\index{cache} : \index{Cache}
\index{Google!page rank} : \index{Google!Page-Ranking}
\index{Visualization!networks} : \index{Visualisierung!Netzwerke}
\index{Visualization!page rank} : \index{Visualisierung!Page-Ranking}
```

### AB-copyright.mkd

```
\index{contributors} : \index{Beiträge}\index{Mitwirkende}
```
