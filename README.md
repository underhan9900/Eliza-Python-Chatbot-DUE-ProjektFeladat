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