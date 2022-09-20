# Ticket Exchange Python script
## Kratki info
Pozdrav ekipa. U mojoj panici i zurbi kreirao sam ovu nesavrsenu i nezavrsenu skriptu, koja do odredene razine funkcionira dovoljno da se uspije ugrabiti karta. Ako netko ima znanja i volje unaprijediti, neka se slobodno posluzi. Skripta vam ulazi sve do plana stadiona, provjeri ima li slobodne sekcije, te ako ima javlja zvucni signal i pop up prozorcic.
## Upute za instalaciju
1. Instalacija Python programskog jezika je relativno jednostavna. Sve sto trebate je otici na sluzbeni website: https://www.python.org/downloads/ , preuzeti instalacijsku datoteku i instalirati.
2. Preuzeti PixelRuler sa stranice te ga instalirati: https://www.pixelruler.de/e/download.htm
3. Preuzeti skriptu i pripadajuce fileove s Google Drive-a i spremiti ih u isti folder: https://drive.google.com/drive/folders/1wbxap8sQMOXxA7rFE1zA7tTpaCfxWA3W?usp=sharing
4. Otici u folder gdje je spremljena skripta, te kliknuti CTRL+SHIFT+ desni klik. Odabrati "Open a PowerShell window here".
5. U konzolu utipkati, sto bi trebalo instalirati sve potrebne module za skriptu:
```
python requirements.py
```

6. Desni klik na script.py i otvoriti u Notepadu ili bilo kojem text editoru. Tamo cete vidjeti sekciju koja izgleda ovako:
```
#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------
MAX_TIME       = 60    # Maximum time in minutes for a script to run
BEEP_DURATION  = 1500  # milliseconds
BEEP_FREQUENCY = 440   # Hz
X_BUY           = 1000; Y_BUY           = 300         # X,Y coordinates of BUY button
X_SELECT        = 1450; Y_SELECT        = 380         # X,Y coordinates of SELECT button
X_CUSTOMER      = 1000; Y_CUSTOMER      = 320         # X,Y coordinates of CUSTOMER button
X_CONTINUE      = 1850; Y_CONTINUE      = 1140        # X,Y coordinates of CONTINUE button
STADIUM_PLAN_X1 = 280; STADIUM_PLAN_Y1  = 400         # X,Y coordinates of UPPER LEFT CORNER OF STADIUM PLAN
STADIUM_PLAN_X2 = 1220; STADIUM_PLAN_Y2 = 1100        # X,Y coordinates of LOWER RIGHT CORNER OF STADIUM PLAN
REFRESH_BUTTON  = "f5"
```
U principu, morate rucno unijeti sve koordinate tipki koje se koriste na Ticket Exchange websiteu. 
X_BUY bi bila X koordinata pixela na ekranu gdje se nalazi tipka BUY. U potrebi da to saznate, otvorite PixelRuler program i stavite ga u gornji lijevi kut vaseg ekrana. Sada kako pomicete mouse, pokazuje vam koordinate gdje se on nalazi. Napravite to za BUY, SELECT, CUSTOMER i CONTINUE tipku. U principu, simulirate vase kliktanje do plana stadiona. 

Da bi skripta znala gdje se nalazi plan stadiona, potrebno je unesti i koordinate stadiona. X1,Y1 predstavljaju gornji lijevi kut stadiona, a X2,Y2 donji desni kut stadiona. Podesite ove koordinate tako da cijeli stadion stane u kvadrat izmedu te dvije tocke. Primjer kako to treba izgledati je "reference.png".
```
STADIUM_PLAN_X1 = 280; STADIUM_PLAN_Y1  = 400         # X,Y coordinates of UPPER LEFT CORNER OF STADIUM PLAN
STADIUM_PLAN_X2 = 1220; STADIUM_PLAN_Y2 = 1100        # X,Y coordinates of LOWER RIGHT CORNER OF STADIUM PLAN
```
Kada ste sve koordinate unesli kako treba, spremite datoteku i zatvorite ju. 

## Upute za koristenje
Skripta vam u potpunosti nece raditi iz prve, to je zbog toga sto ce uci do plana stadiona i uzeti screenshot koji nece biti jednak referenci (reference.png). Pojasnit cu u koracima sto uciniti.

1. Otvoriti browser i otici na stranicu i uci do tamo gdje pise tipka Buy: https://chelseafc.3ddigitalvenue.com/exchange
2. Otici u folder gdje je spremljena skripta, te kliknuti CTRL+SHIFT+ desni klik. Odabrati "Open a PowerShell window here".
3. Smanjiti prozor od PowerShella i staviti ga negdje sa strane, da mis moze sam doci do Buy tipke. 
4. Utipkati:
```
python .\script.py
```
5. Skripta sada krece s radom, ulazi vam sve do plana i rusi se/javlja da je nasla kartu. Sada odite u folder gdje se nalazi skripta, i vidjeti cete "new_screenshot.png". Provjerite je li cijeli stadion u slici. Ako je, izbrisite staru referencu i preimenujte novu sliku u "reference.png".
6. Ponovno pokrenite skriptu unosom: 
```
python .\script.py
```
Sada bi skripta trebala funkcionirati normalno. Da bi je zaustavili pomaknite mis u bilo koji kut ekrana (dok ne nadem nacin za prekinuti skript na normalan nacin :)).
Vrlo lako moguce da sam nesto zaboravio ili nesto zapne, pitajte Filipa da vam da moj broj ili FB pa cu uskociti kad stignem.
