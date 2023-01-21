# Assesment: wat niet te missen en besluiten.

## Styling
### Light en dark mode
Voor de alle tekst, buttons, input fields etc. Heb ik ervoor gezorgd dat deze er goed uit zien en passen bij de andere kleuren van deze mode.

### Responsive
Voor elke pagina heb ik ervoor gezorgd dat hij er goed uit ziet voor grote en kleine schermen. Een aantal dingen die ik hiervoor heb gedaan zijn:

- De kopjes in de navigatie bar die voor kleine schermen te lang zijn heb ik niet in een kleinere font gemaakt, maar ik heb deze kopjes in icons veranderd.
- Voor de pagina waar je de video kan zien heb je op grote schermen de comments aan de rechter kan van de video staan. Hier is geen ruimte voor bij kleine scherms, dus dan worden de comments helemaal onderaan de pagina afgebeeld.
- Voor upload fields (login, registration, video upload) is het niet nodig om de volledige breedte te gebruiken van het scherm, dus deze heb ik gecentreerd en kleiner gemaakt. Voor kleine scherms heb je wel de hele breedte nodig. Ook heb ik de font size aangepast zodat het beter leesbaar is. Ook heb ik de buttons groter gemaakt zodat dez makkelijker aan te tikken zijn.
- De zoekbalk is ongeveer hetzelfde als de upload field: voor brede schermen heb je niet de hele breedte nodig en deze heb ik mooi kunnen stylen met de search button aan de rechterkant van de input field met dezelfde borderradius. Voor kleine schermen heb ik geen border radius en de button rechts ernaast gemaakt zodat het makkelijker te bedienen is op kleine telefoons.

### Hover
Voor alles dat klikbaar is heb ik ervoor gezorgd dat er iets van een hover effect is. Voor thumnails is dit opacity en voor knopjes en input fields een alternatieve kleur.

## Functionaliteit
### Video, Thumbnail en Schema upload
Het is mogelijk je eigen video's, thumnails en schema's up te loaden (dus niet alleen urls).

> Dit was veruit de grootste beslissing die ik had genomen. Ik had er simpelweg voor kunnen kiezen om urls op te slaan in de database, maar ik wilde per sé zelf videos op kunnen slaan. Na dit met Martijn besproken te hebben heb ik ervoor gekozen om mediafiles die geüpload worden op te slaan in een folder op mijn computer. Dit is beter dan urls gebruiken, want nu is mijn website niet afhankelijk van videoplatforms zoals YouTube.

### Logica
Voornamelijk op de video pagina is er aardig wat logica: 

- Je kan alleen comments van andere liken (of unliken als je hebt geliked) en je eigen comments kun je verwijderen. Ook kun je je eigen video verwijderen.
- Je kan niet subscriben op jezelf of videos van jezelf opslaan of liken.
- Je kan alleen liken, volgen, videos opslaan, comments en videos posten als je bent ingelogd. Als je niet bent ingelogd staat er boven in het scherm shortcuts naar de login en registration pagina's.
- Er worden berichten gegeven die aangeven wanneer iets er niet is. Bijvoorbeeld bij comments staat er dan: 'There are no comments on this video yet.' en bij je profiel pagina: 'You have not posted any videos.'.

> Ik heb besloten om al deze logica toe te passen, omdat dit het project 'echt' maakt en niet alleen focust op het implementeren van features.

### Schema
Dit is mijn grootste feature. Bij het uploaden van de video kan de gebruiker kiezen om een trainingsschema te uploaden (in excel form). Hier is ook een template voor gegeven waarin staat dat gewichten in fracties van de 1 rep max gegeven moeten worden. Als iemand nu abonneert op de creator van deze video, heeft deze gebruiker toegang tot het schema. Om dit schema te krijgen moet je je 1 rep max geven en dan wordt er berekend hoeveel gewicht je moet doen voor elke oefening. Ook wordt er nog wat persoonlijke informatie afgebeeld in het gegeneerde persoonlijke schema (je naam, datum van downloaden, het gewicht dat je hebt ingevuld, de maker van het schema). Dit uiteindelijke schema krijg je in pdf formaat.

> Ik had ervoor gekozen deze feature eerst te maken in een jupyter notebook, dit kreeg ik snel werkend en dacht ik snel te kunnen toepassen op mijn website. Dit was niet zo makkelijk als ik dacht want de excel file als input geven en de pdf als output geven was moelijker want ik moest nu de locaties van deze files gebruiken om daadwerkelijk de file te kunnen gebruiken. Achteraf gezien is het denk ik verstandig geweest om dit zo te doen want was ik meteen begonnen in Django dan was het moeilijker geweest te zien waar het misging.

## Code kwaliteit
Ik heb flake8 gebruikt om mijn python files te stijlen. Ook heb ik in mijn python files comments toegevoegd zodat elke stap die ik neem duidcelijk is. Ook heb ik de functies geordend op functionaliteit. Let op: de code die de excel converteerd naar pdf staat in de utils.py file, dit heb ik gedaan omdat deze functies niet iets renderen maar er enkel voor zijn om de conversion te maken voor de laatste functie in mijn views.py file.

Voor mijn html files heb ik zo min mogelijk if else statements gebruikt (dus veel nested statements). Op deze manier is de code zo compact mogelijk. Wel heb ik spacing en identatie gebruikt zodat de files goed leesbaar blijven.

Mijn css file heb ik ook geordend en de verschillende groepen benoemd met comments.

> Ik had ervoor gekozen om eerst alle functionaliteit snel te maken en had me niet echt bezig gehouden met code kwaliteit. Dit is iets wat ik de volgende keer wel meteen ga doen, want met de laatste features die ik toevoegde kostte me het aardig wat tijd om bepaalde functies te zoeken en in het geval van de css file wat er ook alweer gestyled werd.