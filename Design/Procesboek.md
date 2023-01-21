Procesboek: Programmeerproject Wouter Bant 13176676

Week 1:

Ik begon met het kijken met de lectures van week 1: HTML, CSS, Git en Python Recap. In het college van git werden veel dingen verteld die ik nog niet wist. Ik had namelijk nog nooit met git gewerkt. 

Verder heb ik deze week de opdracht search gedaan. Hier kwam ik vrij snel uit met behulp van de aantekening bij het college van HTML en CSS. In het begin wist ik niet helemaal meer hoe ik de gebruiker naar een bepaald link kon sturen, maar na het bekijken van mijn aantekening zag ik dat dit kon door middel van name attribute toe te voegen aan de input fields met type text. Deze name attribute moet dan overeen komen met het eerste wat je ziet na google.com in de url als je iets zoekt.

Ook had ik alvast geprobeerd om de basis Django templates te renderen. Dit lukte mij niet meteen, in mijn code editor werd aangegeven dat de modules van django die geïmporteerd worden niet bestaan. Ik had deze error gegoogled en ik vond op stack overflow dat je dit probleem kan voorkomen door een virtual environment te gebruiken. Ik had hier nog nooit van gehoord maar deze video: <https://www.youtube.com/watch?v=jBzwzrDvZ18&list=WL&index=2&t=20799s>

hielp mij daarbij. Toen ik de virtualenvironment had gedownload bleek het dat ik alle packages die ik al op mijn laptop had gedownload nog een keer moest downloaden in deze virtual environment, maar toen ik dit had gedaan werkte alles.

Week 2:

Ik heb deze week niet alleen het college van Django gekeken maar ook de colleges: SQL, Javascript, User Interfaces, Testing CI/CD en Scalability and Security. Ik heb al deze colleges gekeken omdat ik vrij snel klaar was met de opdrach van deze week: wiki. Er waren wel 2 dingen die me aardig wat tijd kosten om op te lossen/vinden. Dit waren: - een error op de index.html pagina. Dit bleek te komen doordat ik een nieuwe pagina had gemaakt met een lege titel en de manier waarop ik een url maakte voor een nieuwe pagina was de startpagina + /titel dus het probleem was dat die naar dezelfde pagina wees en leeg was. Om dit probleem heb ik deze begin pagina een if statement in de for loop geplaatst die checked of het artikel die in de lijst geplaatst zou moeten worden niet leeg is. Hierna deed de beginpagina het wel weer. Ook was ik vergeten hoe ik de input van een form naar een functie kon sturen na het submitten. Ik vond op internet dat dit kan met action="{% url 'save\_edit' %}" in de form tag te zetten en in urls.py path("save\_edit/", views.save\_edit, name="save\_edit") te zetten en in views.py je functie alsvolgt te beginnen: def save\_edit(request):

`    `if request.method == 'POST':

De belangrijkste dingen uit de colleges die ik heb gekeken zijn: react, hiermee kun je erg flexibel element in de pagina aanpassen. Ik had wel wat ervaring met javascript maar ik wist nooit wat () => syntax betekende, ik heb geleerd dat de gewoon een korte notatie is voor een functie is die geen input parameters heeft. Ook zag ik hoe je met css animaties kan toevoegen, zoals bijvoorbeeld alleen content op de pagina laden die op het scherm te zien is en nieuwe pas te laden als naar beneden gescrolld wordt. Ik had bij programmeren 2 deze week over testen geleerd en in de testing college werd dit nogmaal uitgelegd maar dan specifiek voor django. 

Week 3:

Deze week heb ik de e-commerce website gemaakt, hier was ik aardig lang mee bezig. De eerste paar punten gingen wel met kijken naar de lecture notes, maar ik kwam niet uit het plaatsen van bids en dan updaten als iemand een hogere bid doet. Ik had op youtube een video gevonden die de hele opdracht besprak. Met de hulp hiervan heb ik de bids alsnog toe te voegen. Ook liet deze video mij zien dat het beter is om de categoriën van de producten in een verschillend model op te slaan, dit had ik aanvankelijk zelf niet gedaan. Het voordeel hiervan is dat je producten met een dropdown optie een categorie kan geven. Ook zag ik dat het handiger is om de primary key mee te geven als informatie, ik gebruikte hier eerst title voor en toen ik de title niet nodig had maar alleen de huidige bid op het product werd de logica verwarrend en deze was minder verwarrend met de pk.

Ik was na deze opdracht begonnen met mijn proposal. Hier ging ik op zoek en bekeek ik websites die iets soortgelijks doen als wat ik wil doen, namelijk een platform maken waar je video’s kan uploaden en dat de makers van de video’s sommige of alle video’s alleen beschikbaar maken voor betalende gebruikers. Ik heb sites bezocht zoals patreon en youtube. YouTube heeft als grote probleem dat er ook heel veel andere content op staat, dit betekent dat je snel afgeleid wordt. Ook is het moeilijk voor creators om geld te vragen voor sommige video’s. 1 potentieel probleem dat ik kon bedenken is dat het laden van video’s op de site heel lang kan duren. Een oplossing die ik hiervoor heb bedacht is op de overzichtspagina’s alleen de thumbnails te laden van de video’s. Alleen als je op een video klikt wordt deze geladen.

Ook was ik deze week alvast begonnen met het maken van de frontend voor de website. Omdat mijn website ook gebruik maakt van in- en uitloggen heb ik ervoor gekozen om als startpunt de templates van de e-commerce-project te gebruiken. Ik heb de layout.html gemaakt en de css gescheven voor de meest componenten die ik wil gebruiken. Ook heb ik met javascipt een optie gemaakt voor light/dark mode. Ik liep hierbij wel tegen een probleem aan want bij eerder websites die ik had gemaakt kun je in de img tag de src geven en dan wordt de afbeelding geladen. Dit was nu niet het geval. {% static "videos/entries/sun.png" %}

Moest ik in plaats daarvan gebruiken, ook moest ik in de settings.py file STATIC\_URL = '/static/'

toevoegen.

Ik had met de styling een probleem dat er te veel ruimte zat tussen de titel van de pagina en de nav bar. Dit heb ik uiteindelijk kunnen oplossen met.

Ook heb ik 2 uur gedaan om de javascript toe te voegen en te laten werken: eerst het laden van javascript file was enig sinds hetzelfde als de css file; src="{% static 'videos/script.js' %}"

daarna kreeg ik errors omdat de DOM nog niet geladen is dus deed ik de dit na de body. Toen kon ik de afbeelding niet linken in de JS file om dit op te lossen had ik in de html een script gezet zodat ik de paths naar de afbeeldingen kan opslaan en deze kun je wel aanroepen in de JS file. Toen ik dit had werkt het nog steeds niet en na het inspecteren van de JS in de browser bleek dat de file gecachet was ookal zat ik de hele tijd in cognito mode. Om dit op te lossen deed ik control f5 en toen werkte het.

Week 4:

Ik werkte deze week verder aan de frontend. Ik heb toegevoegd dat de website er ook goed uit ziet voor schermen met de grootte van een tablet en telefoon. Hiervoor heb ik de tekst in de navigatie bar veranderd in icons voor kleine schermen.

Ik wist niet zo goed hoe ik het beste videos en afbeeldingen kon opslaan. Daarom had ik met Martijn een afspraak gemaakt om te kijken hoe dit het beste kan. Hij zei dat ik het beste deze bestanden in een map kan opslaan op mijn computer en de locatie naar deze bestanden in de database. Dit heb ik dus ook zo gedaan.

Om bestanden in de database te zetten heb je een form nodig. Dus ik had ook de upload pagina gemaakt. Ik heb ervoor gekozen om niet de django forms te gebruiken maar gewoon de html form. Dit heb ik gedaan omdat dit makkelijker te stijlen is. Ook deze pagina heb ik responsive gemaakt. Ik zat erg lang met het probleem dat ik de bestanden die de gebruiker gaf niet kon opslaan. Toen ik de documentatie beter las, zag ik dat je niet .POST[‘name’] moet gebruiken voor bestanden maar .FILES[‘name’] toen ik dit had gedaan werkte het precies zoals het zou moeten.

Verder voegde ik hele basis dingen toe die vergelijkbaar zijn met functies die bij de eerdere projecten gebruikt werden. Zoals: comments, likes op video’s een zoek functie die zoekt op de titels van de video’s. Dit ging allemaal vrij soepel omdat ik delen van mijn code van deze projecten kon gebruiken. De rest van de week heb ik besteed aan het mooi afbeelden van de thubnails voor grote en kleine scherms. Hier was ik vrij lang mee bezig, omdat ik niet hetzelfde wilde doen zoals youtube of andere websites maar iets nieuws wilde maken. Alleen de dingen waar ik van dacht dat het mooi zouden maken, maakte het uiteindelijk niet mooier. Ik heb eruiteindelijk voor gekozen om dit vrij simpel te houden, de thumbnails hem ik een kleine border met gecurfde randen en de achtergrond van de figcaption heb ik dezelfde kleur gegeven als de achtergrond van de website. Ik heb bij de functies die ik deze week gemaakt hebt vooral gefocusd op functionaliteit en niet zozeer op de kwaliteit van de code of stijl, dit heb ik gedaan omdat het veel leerzamer is om te werken met databases dan om dingen te stijlen.

Week 5:

Ik begon de week met alle functionaliteiten die ik aanvankelijk bedacht had te implementeren. Ik begon met het maken van de excel naar pdf personelijk trainingschema. Ik heb ervoor gekozen dit niet direct in django te doen, maar eerst te experimenteren in een jupyter notebook. Ik heb veel dingen geprobeerd die op internet stonden, maar niks werkte zoals ik het wilde. Ik moest meerdere dingen samenvoegen, het maken van een pdf, een nieuwe pagina maken en tabellen netjes afbeelden. Toen ik deze 3 dingen had samengevoegd leek het precies hoe ik van te voren had bedacht. Het aanpassen van de gewicht kolom kon blijkbaar erg gemakkelijk met de pandas library. De andere functionaliteiten die ik had toegevoegd waren: een leaderboard, profiel pagina, opslaan van video’s en subsciption pagina. Ook dit ging vrij soepel, leaderboard leek veel op de homepagina maar dan gesorteerd op het aantal likes en aangegeven wat het aantal likes is. Profiel pagina was ik aardig lang mee bezig, niet zozeer dat het niet werkt maar ik vond mijn code veel te ingewikkeld voor iets heel simpels. Ik had namelijk een model gemaakt Profile en deze heeft een foreign key naar User, ook heeft de creator bij videos posted een foreign key naar user en om deze twee met elkaar te linken zodat een gebuiker naar de profiel pagina kan gaan van degene die de video heeft gemaakt die ze nu bekijken. Blijkbaar is er geen directe manier om dit te doen met django models. Ik had met Martijn besproken of ik misschien mijn models anders moest ontwerpen, maar hij zei dat dit goed was dus heb ik er maar niet te veel tijd meer aanbesteed. Subsciption en saved functionaliteit was erg vergelijkbaar dus ik kan veel code hergebruiken. Bij het gesprek met Martijn vroeg ik ook nog wat ik als extra functionaliteiten kon toevoegen en hij zei dat ik me vooral moest focussen op de stijl van de website. Ik vind het zelf moeilijk om te bepalen wat goede stijl is dus heb ik aan andere studenten gevraagd voor advies en ik kreeg vooral te horen dat mijn input forms te groot zijn. Niemand heeft een search balk nodig die een pagina breed is. Ook was de search button verwarrend. Deze dingen heb ik aangepast. Ook heb ik de comment section gestyled, dit was de moeilijkste styling, omdat met grote schermen deze div naast de video past maar bij kleine schermen niet. Bij kleine schermen zou de comment sectie het best passen onderaan de pagina. Hoe ik dit heb opgelost heb is met het maken van 2 divs voor de comment sectie waarbij er altijd maar 1 getoond wordt en welke hang af van de schermgrootte.

Toen ik klaar was met stijlen heb ik nog maar wat extra funcionaliteiten toegevoegd die youtube ook heeft: verwijderen van video’s/comments, comments liken, afbeelden van de tijd gepost voor video’s en comments. Hierna had ik niet echt meer inspiratie voor nieuwe tools dus heb ik de functies voor het persoonlijke trainingsschema alvast in mijn project gezet. Dit heb ik niet in views.py gedaan maar in een nieuw bestand utils.py. Dit heb ik gedaan omdat ook zo gedaan werd bij het wiki project en ik dat erg overzichtelijk van. Het echt werkend gemaakt heb ik nog niet gedaan want hiervoor moeten mijn models aangepast worden en allen video's moeten uit de database gehaald worden om het werken te krijgen. Hier ga ik volgende week aan werken.

Bij programmeren 2 hadden we de week hiervoor met flake8 gewerkt. Deze tool checked de stijl van je code. Deze had ik gerund op mijn python files en die heb ik daarmee aangepast

Week 6:

6/12

Gister had ik besproken welke dingen ik nog moet doen voor het project. Het enige waar ik zelf niet aan gedacht had was een alert maken wanneer je niet ingelogd bent. Hier ben ik de dag mee begonnen en kon ik vrij snel fixen. Hierna heb ik de grootste feature van mijn project, de gepersonaliseerde trainingsschema (excel naar pdf), in django werkend gemaakt. Dit kostte me veel meer tijd dan ik had verwacht, want ik dacht: het werkt al in mijn jupyter notebook dus waarom zou het nu niet werken. Het werkte niet omdat: - je de filename moet onthouden en uniek moet zijn, - de file niet in de huidige directory moet opslaan maar in dezelfde map waar ik mijn video's en afbeeldingen opsla en - het linken naar de file om te downloaden niet in de jupyter notebook nodig was. Ik moest de functies aardig wat aanpassen en vooral de laatste stap was ik erg lang mee bezig. Ik heb tientallen stackoverflow pagina's gelezen, meerdere malen de documentatie over mediafiles gelezen maar niks werkte. Toen ik even pauze nam zag ik op social media een video over chatgpt en hoe dit vragen kan beantwoorden. Toen ik deze tool gebruikte, merkte ik dat ik al snel in de juiste richting kwam, want mijn pagina waarop de gebruiker gewicht op kan geven en het schema kan maken had geen errors meer. Ik deed een aantal ik try again en bij de derde keer gaf de tool precies waar ik naar had gezocht: href="{{ MEDIA_URL }}{{scheme}}". Al die tijd had ik dingen geprobeerd met MEDIA_FILES en zelf direct het pad geven, maar dit werkt niet met django.

Ik heb me nog een aantal uur gefocusd op het verbeteren van mijn code in mijn views.py file. Ik heb bijna alle variabelen een duidelijkere naam gegeven en ik heb comments toegevoegd boven elke functie en voor complexe functies heb ik in de functie de verschillende dingen die gedaan worden uitgelegd met behulp van comments.

7/12

Ik begon de dag met het commenten van mijn python en javascript code die ik gister nog niet gecomment had. Ook heb ik mijn python code geordend op functionaliteit: -renders page, - updates info in database, - adds record to database, - removes record from database. Ik had dit ordenen achteraf gezien eerder moeten doen want ik moest telkens in mijn html kijken naar de link, die ik dezelfde naam heb gegeven als de functies. Met het commenten was ik een aardige tijd bezig, omdat ik dit helemaal niet had gedaan toen ik de functies maakte. Ik kwam ook nog een paar urls tegen met functies die ik had gemaakt maar eigenlijk niks deden. Ik snap wel waarom ik deze gemaakt had, maar die funcitonaliteiten had ik al in andere functies verwerkt. Deze heb ik natuurlijk weggehaald. Ook had ik twee urls naar de functie addLike gingen met dezelfde naam alleen de ene neemt de title van de video en de andere de pk. De functie gebruikt title dus dat is de juiste, ik was een beetje verward want degene die de pk gebruikt stond boven die met title, maar django zoek altijd bij het laden van de pagina of er een juiste reverse is en daarom ging het al die tijd wel goed.

Vanaf nu focus ik me op de kwaliteit van de html pagina's ik begin bij go_to_profile.html. Hier leek niet veel mis mee te zijn, ik had wel 2 keer de style attribute gebruikt maar ik denk dat dit alsnog duidelijker is dat om dit in een css file te doen. Wel zag ik dat de variabele namen erg onduidelijk waren. Ook zag ik dat de functie de de pagina renderd niet goed checked of de user al de gebruiker volgd, hierdoor werkte de unsubscribe button niet meer. Deze dingen had ik toen gefixt. Ook miste er een if statements zodat iedereen die de profielpagina bezocht de video's van de creator kon verwijderen en niet alleen de creator zelf.

Toen ging ik naar de index.html file. Hier was het gewoon een kwestie van variabele namen verduidelijken, maar de filter optie deed het niet meer. Dit kwam doordat de filter functie ook de index.html laat maar dan met minder videos en daar had ik de naam niet aangepast naar de nieuwe, maar toen ik dat wel deed werkte het weer. Dit heb ik voor de ander html files ook meerdere keren gehad. Voor de overige files waren de verandering niet zo heel spectaculair, vooral identatie. Ik was hier redelijk lang mee bezig want elke keer toen ik dacht dat het eigenlijk niet beter kon, vond ik iets wat ik toch anders duidelijker vind. Nu heb ik alleen nog een aantal lijnen in mijn html files staan die ik te lang vind, maar dit komt overmorgen goed want dan ga ik de inline styling die er nog is weghalen en in een apart css file doen.

9/12

Vandaag was eigenlijk het plan om alleen de inline styling en overbodige css weg te halen. Ik deed dit pagina voor pagina, maar eigenlijk overal heb ik nog wat styling aangepast. Op de main page vond ik de margin tussen de video's te klein op andere pagina's waren er een aantal buttons die nog geen hover effect hadden, ik vond het vreemd dat op je profielpagina ook de naam van de creator van de video werd laten zien en op de leaderboard pagina was de margin tussen de video's juist weer te groot. Dus ik was een stuk langer bezig met het stylen dan ik vooraf had voorzien. Ook was de scheme pagina die ik 3 dagen geleden gemaakt nog niet responsive, dit heb ik ook meteen meegepakt. De grootste aanpassing die ik heb gemaakt is bij het uploaden bij de optional scheme een template te plaatsen die gebruikt moet worden om de excel file goed te kunnen verwerken. Ook heb ik de filter optie gecenterd.

Het was dus het plan om met minder css de dag te eindigen. Dit is niet gelukt, ik begon met iets meer dan 500 regels en nu heb ik er bijna 700. De styling vind ik nu wel een stuk beter, het is voornamelijk beter zichtbaar op mobiele telefoons. Vooral doordat ik light en dark mode heb en ook wil dat het responsive is moest ik aantal wat keren op 3 verschillende plekken een id of class in de css file maken en variabele definiëren voor de kleuren.

10/12

Ik begon de dag met het verwijderen van onnodige css. Toen ik keek of de pagina's niet waren veranderd, zag ik dat ik de inlog en registration pagina helemaal nog niet had gestyled. Ik heb deze pagina's gestyled en responsive gemaakt. Ook vond ik de search bar niet mooi voor kleine scherms dus die heb ik ook aangepast.

Daarna begon ik met het ordenen en verwijderen van css. Dit was moeilijker dan ik dacht want ik wist niet precies meer waar ik wat had gedaan en had geen comments gebruikt. Zo werkte lange tijd de responsive display van video's niet meer, om dat ik ergens in het midden van de media voor kleine schermen een column class had gemaakt die niet meer werd uitgevoerd omdat ik ook een column class eronder had geplaatst, die zelf eerst weer bovenaan het bestand stond.

Ik merkte dat ik wel een aantal dingen weg zou kunnen halen, een voorbeeld hiervan is dat de gedefineerde kleuren voor labels en de text in de nav bar hetzelfde zijn. Ik heb ervoor gekozen om deze er toch allebei erin te laten. De gedachte hierachter is dat als je toch besluit dat deze twee dingen beter andere kleuren kunnen hebben je dit gemakkelijk kunt aanpassen. Ook heb ik bijna voor elk knopje een verschillend id gemaakt, eerst leek het erop dat ik hier 1 id voor kon maken of iets kon toevoegen aan de button tag css. Ook hier heb ik besloten dit niet te doen want eigenlijk elke button is net iets anders, dit had ik gedaan zodat de button goed eruit ziet op de pagina en plek waar die staat. Wel ben ik tot de conclusie gekomen dat ik in volgende projecten geen bootstrap buttons meer ga gebruiken. Dit was in het begin erg handig want je hebt dan een redelijk goed gestylde button in enkele seconden, maar later toen ik alles zelf ging stylen heb ik de meest styling hiervan niet gebruikt en overwritten met id tags. Had ik zelf mijn buttons gemaakt dan had ik denk ik nu iets minder id tags gebruikt.

Ik heb de css file in 7 delen opgedeeld: light mode, dark mode, small screen, large screen, default tags, id's, classes. En in de small en large screen secties heb ik ook nog verschillende opdelingen gemaakt gebaseerd op wat er gestyled wordt. Dit is ook iets dat ik toekomstige projecten eerder ga doen want het is nu veel overzichtelijker en je kan veel sneller zien hoe je bijvoorbeeld een andere button hebt gestyled.

Toen ik weer op elke pagina keek, merkte ik op dat iemand die niet is ingelogd op een klein scherm nog steeds comments kan liken, dus dit heb ik aangepast. 

Ook heb ik alvast een assesment.md file gemaakt. En goede thumbnails gevonden en op de website gepost. Toen ik nieuwe gebruikers aanmaakte merkte ik dat ik nooit meteen een profile voor hun aanmaakte deze pagina bestond niet. Dit heb ik de views.py aangepast zodat als iemand zich registreerd die ook meteen een profiel krijgt.

11/12

Vandaag heb ik alleen alle pagina's van de website in alle verschillende modes bekeken. Het enige wat ik heb aangepast is de zoek optie. Deze keek of de string die gegeven was letterlijk in de titel van de video zit. Dit heb ik aangepast zodat het niet uit maakt of grote of kleine letters zijn gebruikt.

12/12

Vandaag heb ik een code review gedaan met Issa. Hij wist niet heel veel verbeteringen te noemen, maar toen ik hem door de code zag gaan, zag ik een paar kleine dingen die ik heb aangepast. Zoals een missende witregel en een overbodige komma of een typo in een comment.

Ook heb ik een requirements file toegevoegd, mijn README verbeterd en de tests.py file verwijderd die ik helemaal niet gebruik. Ook heb ik nog een LICENSE.md toegevoegd en een .gitignore

13/12

Vandaag heb ik de REVIEW.md file toegevoegd met de verbeteringen die Issa had genoemd.

14/12

Vandaag heb ik de screencast opgenomen.

15/12

Vandaag heb ik de screencast geëmbed in mijn README en heb ik screenshots toegevoegd. Ook heb ik de database weggehaald van github.

16/12

Vandaag heb ik de beslissingen die ik heb genomen toegevoegd aan ASSESMENT.md. Ook heb ik alles nog een keer gecontroleerd op compleetheid.