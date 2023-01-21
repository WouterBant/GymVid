# Codereview met Issa

## Verbeterpunten

- Soms zijn de namen die ik gebruik niet erg duidelijk of handig gekozen. Een voorbeeld hiervan is no_training_scheme in mijn Videos_Posted model. Dit zorgt onnodig voor verwarring waneer dit gebruikt wordt. In mijn html heb ik if not no_training_scheme en dit betekent dat er wel een trainings scheme is voor de video. Dit vond ik zelf ook al een beetje verwarrend dus daarom had ik daarbij een comment geplaatst.

- Voor iemand die nooit of weinig met django gewerkt heeft zijn de laatste 2 regels in mijn urls.py file onduidelijk. In deze regels regel ik de path naar mijn static en media files. Ik kan ik beter een comment bij zetten. Omdat dit snel aan te passen was heb ik een comment gezet in mijn settings.py file die dit uitlegd.

- Om te sorteren in reverse order op likes heb ik order_by("-likes") gebruikt. Het is misschien duidelijker om de min weg te halen en daarna reverse te gebruiken.

- In de css zijn de namen wel duidelijk, maar het is beter om consistenter te zijn met wanneer je een hoofdletter of _ gebruikt bij de namen. Nu is dit vrij willekeurig gedaan.

- Een ander punt in mijn css is dat als ik iets 1 keer gebruik (bijvoorbeeld: header > h1) hier beter een id voor kan gebruiken met een duidelijke naam, zodat het nog duidelijker is wanneer deze styling gebruikt wordt. Hier wil ik zelf nog wel iets aan toevoegen wat beter kan de volgende keer: toen ik dingen ging stylen werkte het soms niet in 1 keer en dan probeerde ik dingen samen te voegen tot het wel werkte. Ik heb niet in alle gevallen gekeken welke regels er nou echt voor zorgde dat het werkte en welke regels misschien overbodig zijn. Als ik hier de volgende keer op let kan de css file waarschijnlijk een aantal regels minder zijn. Wat ik ook al had aangegeven in mijn procesboek is dat ik volgende keer voor uitgebreide projecten geen bootstrap ga gebruiken, omdat ik alles wat ik van bootstrap heb gehaald gedeeltelijk heb overwritten met id's omdat het toch niet precies is zoals ik wilde.

- Het was ook niet helemaal duidelijk waarom ik een util.py file had aangemaakt. Toen ik uitlegde dat de functies in deze file geen pagina's renderen maar helper functies zijn om het schema te genereren, snapte Issa waarom ik dit gedaan had maar dit had ik in de util.py net zoals bij de functie in views.py die deze functies gebruikt aan moeten geven met een comment. Omdat dit een kleine aanpassing is heb ik deze comment toegevoegd.