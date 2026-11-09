1966 Eliza Chatbot DUE Projekt Feladat 

Katona József N5HB8N

Python 3.13

A projektemben az 1966-ban készült ELIZA chatbotot készítettem újra Python nyelven.
Az ELIZA az egyik első olyan program volt, amely képes volt beszélgetést szimulálni a felhasználóval. Nem használt mai értelemben vett mesterséges intelligenciát, hanem előre megadott szabályok és kulcsszavak alapján válaszolt.
A saját változatom angol nyelven működik, felismer bizonyos mondatmintákat, egyszerű mondatátalakítást végez, és egy korábban említett témát is képes megjegyezni, de a program valójában nem érti a mondatok jelentését

Felhasznált modulok

tkinter: A grafikus felület megjelenítése és az eseménykezelés.

re: Kulcsszavak és mondatminták felismerése reguláris kifejezésekkel.

random: Véletlenszerű válaszok kiválasztása.

KJ_eliza: Saját modul, amely a chatbot működését tartalmazza.

Program működése: 
A programot a main.py futtatásával lehet elindítani.

A program működése viszonylag egyszerű, összesen 5 lépésből áll.
A felhasználó ír egy üzenetet, majd ELIZA, vagyis a KJ_eliza.py modul megvizsgálja azt, és kiválasztja a megfelelő szabályt. Például az „I feel lonely” mondatból kiemeli a „lonely” szót, majd beleilleszti egy kérdésbe: „Why do you feel lonely?”
A program háromféle módszerrel válaszol. Kulcsszavak alapján, például ha a „father” vagy „mother” szót használjuk, akkor a családról kérdez. Mondatátalakítással, például az „I need help” mondatra visszakérdez: „Why do you need help?” Ha pedig semmit sem ismer fel, akkor a random modul segítségével általános válaszokat választ.
Emellett van egy nagyon egyszerű memóriája is. Ha családi témát ismer fel, ezt eltárolja, és később visszautalhat rá.

A grafikus felület csupán a használatot egyszerűsíti, és szebb kinézetet kölcsönöz a programnak.

A program két Python-fájlból áll. A main.py a grafikus felületért felel, a KJ_eliza.py pedig a chatbot működését tartalmazza a KJ_Eliza osztályban.

Amikor a felhasználó ír egy üzenetet, a KJ_send() függvény beolvassa, majd továbbítja a KJ_respond() metódusnak. Itt a strip() eltávolítja a felesleges szóközöket, majd a program megvizsgálja az üzenetet.

Ha családdal kapcsolatos szót talál, akkor ezt a last_topic változóban eltárolja, így később például egy yes vagy no válasznál vissza tud utalni rá.

A KJ_patterns() tartalmazza az előre megadott szabályokat, amelyeket a program a re.search() segítségével ellenőriz. Ha talál egyezést, akkor a random.choice() kiválaszt egy választ.

Ha nem talál egyezést, akkor a re.fullmatch() segítségével bizonyos mondatszerkezeteket is megvizsgál, például az „I feel lonely” mondatot. Az „I want” vagy „I need” kezdetű mondatoknál a KJ_reflect() is működésbe lép, amely a re.findall() segítségével szavakra bontja a szöveget, majd átalakítja a megfelelő névmásokat. A re.sub() ezután rendezi az írásjelek előtti szóközöket.

Ha egyik szabály sem illik az üzenetre, akkor a program egy véletlenszerű általános választ ad. Végül a KJ_respond() visszaküldi a választ a main.py-nak, ahol a KJ_display() megjeleníti azt a beszélgetési ablakban.
