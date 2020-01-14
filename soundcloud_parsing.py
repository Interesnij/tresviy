# -*- coding: utf-8 -*-
from locale import *
import sys,os

project_dir = '../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import soundcloud
from music.models import *
from datetime import datetime, date, time


client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
page_size = 200
genres_list = SoundGenres.objects.values('name')
genres_list_names = [name['name'] for name in genres_list]

e_rus_list_1 = [
"E-30",
"E-40",
"E-Base",
"E-Cologyk & Evilwave",
"E-Connection",
"E-Force",
"E-Lite feat. T-Pain, Snoop Dogg & Shun Ward",
"E-Magine",
"E-Motion",
"E-Partment",
"E-Rockaz",
"E-Rotic",
"E-Spectro",
"E-Type",
"E.D.B ft. Loco Lopez & Rudy & Nasti",
"E.G. Kight",
"E.K.O feat. Maya Maman",
"E.M.P. feat. Snoop Dogg",
"E.P.I.C. feat. Julie Thompson",
"E.P.O & BIOJECT",
"E.R.M",
"E.U.",
"E.V.A.",
"E.V.O.r",
"E'voke",
"Ea Kaya",
"Each Our Noise",
"Eagle-Eye Cherry & Darin",
"Eagles",
"Eagles Of Death Metal",
"Eamonn Toal",
"Earl D.",
"Earl Gaines",
"Earl George",
"Earl Grau",
"Earl Juke",
"Earl Kluch",
"Earlly Mac feat. Big Sean",
"Earlwood",
"Earphones",
"Earshot",
"Earsome",
"Earstrip",
"Earth Wind And Fire",
"Earth, Wind & Fire",
"Eartha Kitt",
"East & Atlas",
"East & Young",
"East 17",
"East Clubbers feat. BBK",]

e_rus_list_2 = [
"East Jersey feat. Карина Калашян",
"East Love",
"East Side Beat",
"Eastblock Bitches & Niels Van Gogh",
"Eastern Bloc",
"Eastmask",
"Eastrack",
"Easy M",
"Easy Mental & TeeMur",
"Easy Sleezy",
"Easy Star All Stars",
"EasyTech",
"Eat feat. Mary Boccia",
"Eat More Cake feat. River",
"EAUXMAR",
"Ebru",
"EC Twins",
"Ecaterine",
"Ece Mumay feat. Sadrican Sagdur",
"Eche Palante feat. Rich Simpson",
"Echevo",
"Echo Bass",
"Echo feat. Sanna Martinez",
"Echo Foster feat. Logic MC",
"Echoes",
"Echologist",
"Echos",
"Echosmith",
"Ecke Prenz",
"Eclipse",
"Eco & Brooke Forman",
"Eco & Carly Burns",
"Eco feat. Jennifer Rene",
"Ed Alleyne-Johnson",
"Ed Breezy",
"Ed Drewett",
"Ed Kashinsky",
"Ed Marquis & Axel feat. Emie",
"Ed Prymon",
"Ed Sheeran",
"Edalam & Myf & Cuban Mob",
"Eddi Royal feat. Aspiring",
"Eddie Amado",
"Eddie Bitar",
"Eddie Butler",
"Eddie Caldwell",
"Eddie Cochran",
"Eddie GrandMan",
"Eddie Grant",
"Eddie Harris",]

e_rus_list_3 = [
"Eddie Lung & DJ T.H. feat. Solid Skill",
"Eddie Makabi feat. Einat",
"Eddie Manion",
"Eddie Middle-Line",
"Eddie Murphy",
"Eddie Razaz",
"Eddie Silverton",
"Eddie Thoneick",
"Eddie Writer",
"Eddiejay",
"Eddwingstone",
"Eddy Chrome",
"Eddy Huntington",
"Eddy Rox feat. Ron May",
"Eddy Wata",
"Eddy Watta",
"Eddzaa feat. Verse II",
"EDEN",
"Eden Golan",
"Eden Prince",
"Eden Xo",
"Ederson",
"Edgar",
"EdgarMc",
"Edgars Hudjakovs",
"Edge Of Dawn",
"Edge Of Universe feat. Rob Lear & Leo Diaz",
"Edher Torre",
"Edik Salonikski",
"Edin",
"EDISS & Zhivoy",
"Edith Piaf",
"Edlan & MVE feat. Neil",
"Edlington",
"Edmofo feat. Mitti",
"Edmon Kazaryan",
"Edmonte",
"Edouards",
"Edsilia Rombley",
"Edu Elizondo feat. Ela Llamin",
"EDU",
"Eduardo de la Iglesia",
"Eduardo Ramirez feat. Laura Green",
"EDUKE feat. Tiffany Fred",
"Edurne",
"Edvard Hagerup Grieg",
"Edvard Viber feat. Tiff Lacey",
"Edvin Marton",
"Edward Box",
"Edward Maya",]

e_rus_list_4 = [
"Edward Sanda",
"Edward Sharpe And The Magnetic Zeros",
"Edward Tatiani (Eddie)",
"Edwardo Base feat. Deelyte",
"Edwin Hawkins Singers",
"Edwin Klift",
"Edwin Mccain",
"Edwin Star",
"Edwin Starr",
"Edwyn Collins",
"EDX",
"Edyta Gorniak",
"Eek-A-Mouse",
"Eelke Kleijn",
"Eels",
"Een Stemming",
"Eeva",
"EF1T & Денис Океан",
"Efe Yilmazer feat. TXMIC",
"Efecto Pasillo feat. Juan Magan",
"Efemero",
"Effective Radio",
"Effex & Loco feat. Amperage & Dela K",
"EFGI",
"Efreet feat. Tik & Johnyboy",
"Efremova",
"Eg14N",
"Ega",
"Ege Akkanatli",
"Ege Balkiz",
"Egh feat. Meloe",
"Egine (Иджин)",
"Egma",
"Ego ft. Robert Burian",
"Ego Miss Blinded",
"Egoism",
"Egophonik",
"Egor Gayduchik feat. Ксений Пустовая",
"Egotrip",
"Egzod",
"EH!DE",
"EHI feat. Blen",
"Ehliu",
"Ehren Stowers feat. Emi Jarvi",
"Eifel 65",
"Eiffel 65",
"Eight Ball Down",
"EIGHTEEN",
"Eighth Wonder",
"EightyNineGeeks feat. Amber Noel",]

e_rus_list_5 = [
"Eihelstraat",
"Eik feat. Laika",
"Eila feat. Glance",
"Einer feat. Grom",
"Eirik",
"EirikD",
"Eirikur Hauksson",
"Eisbrecher",
"Eject",
"Ejecta",
"Ejen",
"Ejen & Lunna",
"Ejons",
"Ekali",
"Ekaterina Teras",
"Ekaterina-M",
"Ekko & Myxe",
"Eklo",
"Ekow feat. Snoop Dogg & Kylian Mash",
"Ekowraith",
"Ektor Pan",
"EkzOoo & Allside",
"El 3Mendo",
"El Alfa",
"El Baile",
"El Capon",
"EL Cata",
"El Chicano",
"El Chombo",
"El Coyote The Show feat. Farruko & Tito El Bambino",
"El D & Tessa B",
"El Ed Harris feat. Ly-Club",
"El Fox",
"El Freaky feat. De La Ghetto & Paty Cantu",
"EL Joy (Spirit Tag)",
"EL Mas Fino & Sergio Requena",
"El Mimi",
"El Mukuka feat. Alan Thompson",
"El Pasador",
"El Percal",
"El Polaco",
"El Profesor",
"El Proyecto",
"EL Radu",
"El Ray",
"El Rico",
"El Rocha & Jose MC & Raro Bone & DJ Dever",
"El Shalom",
"El Speaker feat. Leila Lanova",
"El Sueno De Morfeo",]

e_rus_list_6 = [
"El Viejin",
"El. Train & Barney Artist",
"EL’MAN feat. Andro",
"EL'DO",
"El'man",
"Ela Rose",
"Ela Rose & David Deejay",
"Ela Van Wolf",
"Elada",
"Eladio Carrion & Bad Bunny",
"Elaine Faye",
"Elaiza",
"Elatex",
"ELCAMINO",
"Eldar",
"Eldark",
"ElDera",
"Elderbrook",
"Eldo",
"Eldor Q feat. Martinez Live Sax",
"Eldrine",
"Ele7en feat. Amanda Wilson",
"Electric Guest",
"Electric Guitars",
"Electric Lady Lab",
"Electric Light Orchestra",
"Electric Moonlight",
"Electric Pulse",
"Electric Six",
"Electric Starlet feat. Justina Valentine",
"Electric Stiletto",
"Electric Wire Hustle feat. Kimbra",
"Electrick Village",
"Electrix",
"Electrixx",
"Electro Tango",
"Electro Velvet",
"Electro-Light & Tobu feat. Anna Yvette",
"Electrokid",
"Electromagnetic Blaze feat. Foster",
"Electrosila и Планка",
"Electrostel",
"Electrovamp",
"Eleftheria Eleftheriou",
"Eleftherios Mukuka & Adam Cooper feat. Lu Gari & Layth Sidiq",
"Elefunt's Groove",
"Elektra",
"Elektrik Bet",
"Elektronomia & Stahl",
"Elements",]

e_rus_list_7 = [
"Elements Of Life",
"Elen Levon",
"Elena feat. Absolute",
"Elena feat. Danny Mazo",
"Elena feat. Danny Mazzo",
"Elena feat. Glance",
"Elena feat. SoulJay, Khazin & Ozlam",
"Elena Gheorghe",
"Elena Ionescu feat. SuperChill",
"Elena Paparizou",
"Elena Presti",
"Elena Risteska",
"Elena Tsagkrinou",
"Eleni Foureira",
"Elenowen",
"Eleonora",
"Eleonora Espago",
"Elephant Man",
"Elephante feat. Brandyn Burnette",
"Elephante feat. Jody Brock",
"Elephante feat. Lyon Hart",
"Elephante feat. Matluck",
"Elephante feat. Rumors",
"Elephante feat. Trouze & Damon Sharpe",
"Elettra Lamborghini",
"Elevate The Virus",
"Eleven",
"Elhaida Dani",
"Eli Emmanuel",
"Eli Lieb",
"Eli Rose",
"Eli Rose feat. FouKi",
"Eli Wais",
"Eli Way feat. Cehryl",
"Eli-Ja",
"Eli, Oana Radu feat. Dr. Mako",
"Elian & Frankox feat. Jonny Rose",
"Elian feat. Thedetstrike & Nadya Sumarsono",
"Elian West",
"Eliana Cartella",
"Elianne feat. Connect-R",
"Elias",
"Elias Abbas feat. Keya",
"Elias Bertini",
"Elias Fogg",
"Elida",
"Elieve",
"Eligor & Lilith & Manu Avila",
"Elijah",
"Elijah Blake",]

e_rus_list_8 = [
"Elijah King & Honorebel",
"Elijah Prophet",
"Elijah Woods",
"Eliminate",
"Elin Bergman",
"Elin Lanto",
"Elin Rigby",
"Elin-Khanum",
"Elina Born & Stig Rasta",
"Elina Nechayeva",
"Elio Deejay",
"Elio Foglia",
"Eliot",
"Elis Brooklyn",
"Elis Brooklyn & Dj Nil",
"Elisa",
"Elisabeth Carew",
"Elisavet Spanou",
"Elise Major",
"Eliss Roxx",
"Elissa",
"Elisse",
"Elite Electronic",
"Elitsa Todorova & Stoyan Yankulov",
"Elitt feat. aikko & DommI",
"Elitt feat. DommI & aikko",
"Elix",
"EliXir",
"Eliza",
"Eliza Doolittle",
"Eliza feat. The Kid Ryan & Prince Sole",
"Eliza G",
"Eliza Lacerda",
"Elizabeth Rose",
"Elk Road",
"Ell & Nikki",
"Ella Eyre",
"Ella Fitzgerald",
"Ella Henderson",
"Ella Mai",
"Ella McCarthy",
"Ella Mike",
"Ella Vos",
"Ellapaige",
"Elle Exxe",
"Elle Hollis",
"Elle King",
"Elle Limebear",
"Elle May",
"Elle Varner",]

e_rus_list_9 = [
"Elle Vee",
"Elle Watson",
"Ellei & Eks",
"Ellen Benediktson",
"Ellen Weller",
"Ellen Xylander",
"Elles Bailey",
"Elley Duhe",
"Ellez Marinni",
"Elli feat. Muzza",
"Ellie Drennan",
"Ellie Goulding",
"Ellie Lawson",
"Ellie Lil",
"Ellie Sax",
"Ellie White",
"Ellinor",
"Elliot Berger",
"Elliot Goldenthal",
"Elliot Minor",
"Elliot Sivad feat. Mr. Brook",
"Elliot Trent",
"Elliphant",
"Ellis",
"Ellise",
"ElloXo",
"Elly Ekko",
"Ellys Leon & Garrido",
"Elman",
"Elmars feat. Kati Sound",
"Elmo Magalona",
"Elnur & Samir",
"Elnur Huseynov",
"Elodie",
"Elohim",
"Eloi El",
"Eloise",
"Elomo",
"Eloquentia",
"Elsa & Emilie",
"Elsa Del Mar",
"Elsakova",
"Elton John",
"Elvana Gjata",
"Elviira & Rake",
"Elvin Grey",
"Elvira Ragazza",
"Elvira T",
"Elvirra Strayzi",
"Elvis Costello ft. The Attractions",]

e_rus_list_10 = [
"Elvis Crespo feat. Pitbull",
"Elvis Presley",
"Elvis Se Seun",
"Elvis Vs Jxl",
"Elwina feat. The Phat Mack",
"Elya Chavez",
"Elyar Fox",
"Elypsis & Emma Horan",
"Elyss",
"Elytza",
"Eman B feat. Marcela Ocampo",
"Emanuel Nava & Gabry Ponte",
"Emanuele Braveri & Amo R",
"Emanuele Destino EDM feat. Steven Owner",
"Emarosa",
"Emax & Alesing",
"Embody",
"Embrace One feat. Shaz Sparks",
"EMBRZ",
"Emdee feat. Diane Sullivan",
"Emdeka",
"Emdi feat. Veronica Bravo",
"Emdivity",
"EME & Zeeba",
"Eme Be feat. Fran Leuna & Henry Rou",
"Emeli Sande",
"Emelie Hollow",
"Emerentia",
"Emergency",
"Emerson",
"Emigrant",
"Emii",
"Emil Croff & Trox",
"Emil Friis",
"Emil Lassaria",
"Emil Stabil feat. Gucci Mane",
"Emile Haynie",
"Emile Prud'homme",
"Emiley Stans",
"Emiley Stans feat. Elvin Grey",
"Emilia & Darell",
"Emilia & Lazar",
"Emilia De Poret",
"Emilian",
"Emiliana Torini",
"Emiliana Torrini",
"Emilie Esther",
"Emilie Ramirez",
"Emilio Mercuri",
"Emily Browning",]

e_rus_list_11 = [
"Emily Burns",
"Emily Haines & The Soft Skeleton",
"Emily Hearn",
"Emily Katter feat. Hybrid",
"Emily Osment",
"Emily Roberts & Pyke & Munoz & Stengaard",
"Emily Taylor, Rob Bagshaw, Tara Chinn",
"Emily Vaughn",
"Emily Warren",
"Emin",
"Emina Jahovic",
"Eminem",
"Eminence",
"Emir feat. Tanisha",
"Emir Jey",
"Emis Killa",
"Emjay",
"Emly Clausen",
"EMM",
"Emma Andersson",
"Emma Bale",
"Emma Bates",
"Emma Bunton",
"Emma Carn",
"Emma feat. David Bisbal",
"Emma feat. Izi",
"Emma Gatsby",
"Emma Hewitt",
"Emma Jensen",
"Emma Lock feat. Alexander Turok",
"Emma Lodge feat. Mario Morreti",
"Emma Louise",
"Emma Marrone",
"Emma McGrath",
"Emma Sameth & Jeremy Zucker & Wolfe",
"Emma Steinbakken",
"Emma Stevens",
"Emma Wahlin",
"Emmalyn",
"Emmanuel Jal feat. Nelly Furtado",
"Emmanuel Pahud",
"Emmanuel Sayers",
"Emmelie De Forest",
"Emmure",
"Emmy Skyer",
"Emotion",
"Emotion Machine & Henrik B",
"Emotional Oranges",
"Emotive Tunes feat. Selecta",
"Empathy Test",]

e_rus_list_12 = [
"Emphatic",
"Empire",
"Empire Cast",
"Empire Of The Sun",
"Empress Of",
"Emrah",
"Emran Badalov",
"Emre Cizmeci",
"Emre Colak",
"Emre Madak",
"Emy Care",
"Emzy vs. John Dahlback",
"Emzy vs. Shapeshifters",
"En Jay feat. Flashing Light & Елизавета Патюкова",
"En Vogue",
"Enau",
"Enaya",
"Enca",
"Encore",
"Encure",
"End Of The World feat. Clean Bandit",
"Ende",
"Endless",
"Endless All",
"Endless feat. Allisha Summers",
"Endor",
"Endorphin",
"Enea",
"Eneda Tarifa",
"Eneli",
"Enemy feat. EMBRVCE & ЧеСразу Я",
"Energy Deejays",
"Enfant De Luxe",
"Enformig",
"Engelbert Humperdinck",
"Engin Ozturk",
"Englafjord",
"Eni Koci",
"Enigma",
"Enjoy",
"Enjoy Deejays",
"Enlaced By Tempest",
"Enlarge",
"Ennio feat. Danil",
"Ennio Morricone",
"Eno & Dirty",
"Eno feat. Mero",
"Enpon",
"Enrasta",
"Enrico & Picco feat. Bruno",]

e_rus_list_13 = [
"Enrico Sangiuliano",
"Enrique Iglesias",
"Enrique Morente",
"Enrique Paz",
"Enrique_Iglesias",
"Ensuna",
"Entely",
"Enter Shikari",
"Enterpryse & Deenk",
"Enton Biba",
"Entoniu & Agape",
"Envotion",
"Enya",
"Enzo Darren",
"Enzo Ingrosso feat. Conrad Sewell",
"Enzo Saccone",
"Eowyn",
"Ephese",
"Ephixa & Bossfight",
"Ephwurd feat. DKAY",
"Epic Beat",
"Epica",
"EpicFail",
"Epik feat. Veronica Bravo",
"Epizod",
"Epolets",
"Eptic",
"Equinox",
"Era",
"Era For A Moment",
"Era Istrefi",
"Eran Hersh",
"Eraption",
"Erasure",
"ERCore feat. Sasha Mad",
"Ereez",
"Erene",
"Erez Shitrit",
"Erhan Boraer feat. Mert Kurt & Mustafa Guney",
"Eric B And Rakim",
"Eric Bellinger",
"Eric Benet feat. Lil Wayne",
"Eric Bibb, Rory Block & Maria Muldaur",
"Eric Carmen",
"Eric Carter",
"Eric Chase",
"Eric Chou",
"Eric Clapton",
"Eric Darius",
"Eric Demn",]

e_rus_list_14 = [
"Eric Destler feat. Franka",
"Eric Faria feat. Marta Martins",
"Eric feat. K-Brown",
"Eric feat. Natalia",
"Eric Gales",
"Eric Gemsa",
"Eric Johnson",
"Eric Lindell",
"Eric Lumiere",
"Eric Marienthal",
"Eric Morillo & Andrew Cole feat. Kylee Katch",
"Eric Mykel",
"Eric Paplaya",
"Eric Plust",
"Eric Prydz",
"Eric Reed",
"Eric Roberson feat. Chubb Rock",
"Eric Saade",
"Eric Sanchez",
"Eric Sanicola",
"Eric Senn",
"Eric Turner",
"Eric Tyrell feat. Natasha Burnett",
"Eric Van Basten",
"Eric Vice feat. Outen",
"Eric Williams",
"Eric Zatt feat. DJ Bounce",
"Eric Zayne",
"Erick E",
"Erick Morillo",
"Erick Right",
"Erick Strong",
"Ericka J",
"Ericka Jane",
"Erik Arbores",
"Erik Berglund",
"Erik Hassle",
"Erik Kortiss & Steeve Aston",
"Erik Nielsen",
"Erik Polder feat. V. Ray",
"Erik Rapp",
"Erik Satie",
"Erik Van Tools feat. Stef C",
"Erik Yahnkovf",
"Erik-X",
"Erika and Britten",
"Erika Jayne",
"Erika Ray",
"Erika Selin",
"Erin Bloomer",]

e_rus_list_15 = [
"Erin Christine",
"Erin Jaimes",
"Erin Stevenson feat. Rick Jane",
"Eriq Johnson",
"Erislandy",
"Eritza",
"Erkan Sen feat. Addie Nicole",
"ERKOFF & T-Iron",
"Ermakov",
"Ermal Meta",
"Ermal Meta & Fabrizio Moro",
"Ernest Oh",
"Ernest Saint-Laurent",
"Ernestine Anderson",
"Ernesto Cortazar",
"Ernesto Kohler",
"Ernesto vs Bastian",
"Ernie Gaines feat. Jonny Rose",
"Ernie Halter",
"Ernst Senff Chor feat. Berliner Philharmoniker & Carlo Maria Giulini",
"Erolflynn feat. New Gang",
"Eromin",
"Eros Ramazzotti",
"Erotic Cafe' feat. KG Man",
"Ershov",
"Ersin Ersavas & Omer Bukulmezoglu",
"Eruption",
"Ervin Gonxhi feat. Marin Hoxha & Vinsmoker",
"Erzsebet Csezi",
"ES-MOTEEV & S.n.i.p 31",
"Escala",
"Escalation",
"Escape",
"Escea",
"Escon",
"Escort feat. Meya",
"ESG",
"Eshliview",
"Eskai & Snr feat. Evin Skye",
"ESkeN feat. Денис Маленко (BeLieVe) & Артем Scoop",
"Eskimo Callboy",
"Eskmo feat. White Sea",
"Eslabon Metal",
"Eslix",
"Esma & Lozano",
"Esmee",
"Esotique & Sandra N",
"Espen Lorentzen feat. Sylvi",
"Esperanza Spalding",
"eSQUIRE",]

e_rus_list_16 = [
"Essami",
"Essay feat. Ida Dillan",
"Essco",
"Essenger feat. Lexi Norton",
"Essentials & Influ",
"Essess feat. Brendan Reilly",
"Essie Holt",
"Estate",
"Este Habana",
"ESTEL and Invisible Force",
"Estela Martin",
"Estelle",
"Ester",
"Ester Dean",
"Ester Peony",
"Esther Hart",
"Esther Merino",
"Esther Vallee",
"Esthetix",
"Estigma",
"Estilo Libre feat. DJ Valdi",
"Estinex",
"Estiva",
"Estopa",
"Estradarada",
"Estrella Morente",
"Estro",
"Etania",
"Etasonic",
"ETC!ETC! & Corporate Slackrs feat. Petey Pablo",
"Eteri Toledo",
"Eternity",
"Etham",
"Ether feat. Progley",
"Ethereal Pilgrim",
"Ethernity",
"Etherwood",
"Ethnic Albania",
"Ethno-Jazz Band Iriao",
"Etienne Deleyre",
"Etienne Ozborne",
"Etoile",
"Etostone",
"Etta James",
"Etta Zelmani",
"Euge Groove",
"Eugene Noiz",
"Eugene Radionov feat. DJ MiHaALL",
"Eugene Star feat. DJ Goman",
"Eugent Bushpepa",]

e_rus_list_17 = [
"Euphoria",
"Euphoria DJ's",
"Euphoria Project By Cj Choopa feat. Mc Mad",
"Euphoric",
"Eurithmics",
"Euro Latin Beats",
"Euroband",
"Eurogroove",
"Europe",
"Eurotrash",
"Eurythmics",
"Eva",
"Eva K",
"Eva K. Anderson",
"Eva Kade",
"Eva Loras",
"Eva Parmakova",
"Eva Pavli feat. Miss Angel & Jeremy Lior",
"Eva Pop",
"Eva Rivas",
"Eva Ruiz",
"Eva Rydberg",
"Eva Shaw",
"Eva Simons",
"Eva-Lina",
"Evaluna Montaner",
"Evan Giia",
"Evan Kendricks",
"Evan Klar",
"Evan Pearce",
"Evan Rai",
"Evan Ross feat. T.I",
"Evan Taubenfeld feat. Avril Lavigne",
"Evanescence",
"Evangeline",
"Evdokia Kadi",
"Eve Feat. Alicia Keys",
"Eve feat. Gabe Saporta",
"Eve feat. Konshens",
"Eve feat. Miss Kitty",
"Eve feat. Snoop Dogg",
"Eve feat. Will.I.Am",
"Evelina Sasenko",
"Evelyn feat. J. Worthy",
"Evendeep",
"Event Horizon & Chaotix",
"Everette Harp",
"Everlast",
"Everlight",
"Every Hour Kills",]

e_rus_list_18 = [
"Every Man A King",
"Everyday People",
"Everything But The Girl",
"Eves Karydas",
"Evgen Dia",
"Evgen Fm",
"Evidelle",
"Evident",
"Evie Irie",
"Evii feat. Timati",
"Evil Jokes",
"Evil Nine & Jfb",
"Evilwave feat. Nathan Brumley",
"Evilyn Strange",
"Evix feat. Jake Herring",
"EVO-K vs. AAA",
"Evok & Tellur",
"Evokings",
"Evol Intent feat. Anna Yvette",
"Evridiki",
"Evrim Derin feat. Eser Perkins",
"Evroslav",
"Evrybdy & Milwin feat. Philip Strand",
"Evsy FLVC",
"EvvE",
"EVVY",
"Evy feat. Lokka",
"EVгеника",
"Ewa Farna",
"Ewa feat. Valdy",
"Ewan Lyron & Xander Niels feat. Nathan Brumley",
"Ewert And The Two Dragons & BrainStorm",
"Ex Youth",
"Ex-Melody",
"Ex-Otago",
"Ex-Po",
"Exal feat. Emily Underhill",
"Examination",
"Example",
"Excalibur",
"Excision & The Frim feat. Luciana",
"Execute",
"Exes",
"Eximinds",
"Exis",
"Exit Mars",
"EXO",
"Exo-K",
"Exodus & Luca Debonaire feat. Lux",
"Exolight",]

e_rus_list_19 = [
"Exoplanet",
"Exostate",
"Expl0re",
"Expromt",
"EXSSV & Pixel Terror",
"EXSSV feat. Karra",
"Extrawelt",
"Extreme",
"eXX feat. Laura Luppino",
"EXYT",
"EYA",
"Eye Cue",
"Eye Depth feat. Jasmine Knight",
"EYJEY",
"Eyonics pres. Dreameye",
"Eypor Ingi Gunnlaugsson",
"Eyzzex!",
"EZEE",
"Ezek",
"Ezhovastyle feat. Blxckowl",
"Ezi",
"Ezkiel",
"Ezra Collective feat. Jorja Smith",
"Ezra Vine",
]

litera = SoundSymbol.objects.get(name="E")

count = 0

for tag in e_rus_list_18:
    tracks = client.get('/tracks', q=tag, limit=page_size, linked_partitioning=1)
    if tracks:
        for track in tracks.collection:
            created_at = track.created_at
            created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            if track.description:
                description = track.description[:500]
            else:
                description=None
            try:
                SoundcloudParsing.objects.get(id=track.id)
            except:
                if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                    try:
                        self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                    except:
                        self_tag = SoundTags.objects.create(name=tag, symbol=litera)
                    genre =SoundGenres.objects.get(name=track.genre.replace("'", '') )
                    new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, description=description, duration=track.duration, genre=genre, title=track.title, uri=track.uri, release_year=track.release_year)
                count = count + 1
        while tracks.next_href != None and count < 2000:
            tracks = client.get(tracks.next_href, limit=page_size, linked_partitioning=1)
            for track in tracks.collection:
                created_at = track.created_at
                created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
                if track.description:
                    description = track.description[:500]
                else:
                    description=None
                try:
                    SoundcloudParsing.objects.get(id=track.id)
                except:
                    if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                        try:
                            self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                        except:
                            self_tag = SoundTags.objects.create(name=tag, symbol=litera)
                        genre =SoundGenres.objects.get(name=track.genre.replace("'", '') )
                        new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, description=description, duration=track.duration, genre=genre, title=track.title, uri=track.uri, release_year=track.release_year)
                    count = count + 1
