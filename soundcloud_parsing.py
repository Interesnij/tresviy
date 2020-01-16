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

n_rus_list_1 = [
"N-Chased",
"N-Dubz",
"N-Force",
"N-Sife",
"N-Sync",
"N-Tone feat. Empire",
"N-Trance",
"N-Trigue",
"n!Lay & Забытый Женя",
"N.A.O.M.I. (Наоми)",
"N.E.O.N.",
"N.E.R.D.",
"N.Juravel",
"N.O.Pro",
"N.O.R.E.",
"N.Y. City Beats",
"N'Jastiz",
"N'Pans & L.A.V. Retro",
"N'Playaz",
"N'sync",
"N'time",
"N1NT3ND0",
"N3wport",
"N69",
"Na Palm",
"NA-NO",
"Na1Te",
"Na7halie Sade",
"Naations",
"Naaz",
"Naazuk",
"naBBoo",
"Nabiha",
"Nabil MJ",
"Naccarati feat. Jessica Jolia",
"Nacey feat. Angel Haze",
"Nacho",
"Nacho Chapado",
"Nacho Sotomayour",
"Nacim Ladj",
"NaCl",
"Nadav Guedj",
"Nadeer feat. Natavan Habibi",
"Nadi Jaskin",
"Nadia & Alan Divall",
"Nadia aka Nyjra",
"Nadia Ali",
"Nadia Dorine",
"Nadia Forde",
"Nadia Gattas",]

n_rus_list_2 = [
"Nadia Lengert",
"Nadia Lucy feat. Ali B",
"Nadia Malm",
"Nadia Nair",
"Nadia Oh",
"Nadine",
"Nadine Beiler",
"Nadine Coyle",
"NADIR",
"Nadiya",
"Nadiyah",
"NaDoJo",
"Nadya Vozduh & Jambazi",
"Naela feat. Black M",
"Naestro feat. Balti",
"Nafis",
"Nafta & Ennea",
"Naguale",
"Nahaze feat. Achille Lauro",
"NAIA",
"Naiara Azevedo & DeeJay Momo",
"Naibu",
"Naif",
"Naika",
"Nail Shary",
"Naila",
"NaiLya",
"Naira",
"NAJE",
"Najoua Belyzel",
"Nakash Aziz & Shreya Ghoshal",
"Nakatomi",
"Naked Fish",
"Naked Koala",
"Nakhiya",
"Nakita",
"Naksi",
"Nalin & Kane",
"Nalyro",
"Namara",
"Namaste",
"Namelessgirl",
"Namia",
"Namie Amuro",
"Nana",
"Nancy Wilson",
"Nando Fortunato",
"Nani Killa",
"Nania",
"Nanik",]

n_rus_list_3 = [
"Nano Banani",
"Nanobyte & Mary Lambert",
"Nanoplex",
"NanosauR feat. Dev",
"Nanowar Of Steel",
"Naoki Kenji",
"Naoky ft. Stylove",
"Naomi Lien",
"Naomi Pilgrim",
"Naomi Wang",
"Naomi Wild",
"Napalm Death",
"Napoli",
"Nara",
"Narany",
"Narcotango",
"Narcotic Chill",
"Narcotic Sound",
"Nari",
"Narika",
"Narine",
"NarkoSky",
"Nas",
"Nas Ti",
"Nash Balfas",
"NASH feat. Michele C",
"Nash Overstreet & Sidnie Tipton",
"Nashaz",
"Nashback & Jo Corbo",
"Nashville Cast feat. Christina Aguilera",
"Naskid & Trackstorm feat. Amine",
"Nasled & Lars",
"Nasri",
"Nassi",
"Nassim Al Fakir",
"Nasta Sia",
"Nastasia & Cappucinno",
"Nastika",
"Nastra x Needow",
"Nasty Cherry",
"Nasty Dark",
"Nastya House",
"Nastya Romanova",
"Nastya Shabovich",
"Nastя Lucky",
"Nat 'king' Cole",
"Nat Conway",
"NAT feat. Таисия Вилкова",
"Nat King Cole",
"Nat Slater",]

n_rus_list_4 = [
"Nata Boboc",
"Natacha & David Coroner",
"Natacha feat. David Coroner",
"Natali Imbrulia",
"Natali Song & Кристалл",
"Natali Thanou",
"Natali Yura",
"Natalia Barbu",
"Natalia Clavier",
"Natalia Damini",
"Natalia Gordienko",
"Natalia Jimenez",
"Natalia Kelly",
"Natalia Kills",
"Natalia Lesz",
"Natalia Mejia (Girlicious)",
"Natalia Oreiro",
"Natalie Bassingthwaighte",
"Natalie Cole",
"Natalie Gang",
"Natalie Gauci",
"Natalie Gioia",
"Natalie Goovers",
"Natalie Gotman",
"Natalie Imbruglia",
"Natalie La Rose",
"Natalie Madigan",
"Natalie Major",
"Natalie Merchant",
"Natalie Orlie",
"Natalie Page",
"Natalie Portman",
"Natalie Walker",
"Natalino Nunes",
"Nataly & Ryan",
"Natan",
"Natania",
"Natascha Bessez",
"Natasha Andree",
"Natasha Baccardi",
"Natasha Bedingfield",
"Natasha Mosley ft. Waka Flocka Flame",
"Natasha Rostova",
"Natasha Royce",
"Natasha Slayton",
"Natasha St-Pier",
"Natasha Thomas",
"NataShe & Adriana",
"Nate Ruess",
"Nate VanDeusen feat. Carly Jay",]

n_rus_list_5 = [
"Naten",
"Nathalie Aarts & Kim Lukas",
"Nathalie Page",
"Nathalie Sorce",
"Nathan Ball",
"Nathan C & Kash",
"Nathan Dawe feat. Jaykae",
"Nathan K",
"Nathan Sykes",
"Nathan Trent",
"Nathaniel",
"Nathia Kate feat. Carina",
"Nation 4",
"Native U",
"Natives",
"Naton Wigs",
"Natti Natasha",
"Natty Bong",
"Nature One Inc.",
"Naturtalente",
"Naughty Boy",
"Naughty By Nature",
"Nause",
"Nautilus Pompilius",
"Nav feat. The Weeknd",
"Navai & Bahh Tee",
"Navarra",
"Navarre",
"Navia Robinson",
"NaviBand",
"Navid",
"Navidad Por Bulerias",
"Navii",
"NAVSI100",
"Navvy",
"Naxxos",
"Nay Sean",
"Naya Marie",
"Naya Rivera",
"Nayah",
"Nayala feat. Dan De Leon & Marco Da Silva",
"Nayer",
"Naymada feat. Anivar & Karen Туз",
"Naysu feat. Ngaire Blackman",
"Naza Brothers & Braudt feat. Sharon",
"NAZAMI",
"NaZaNa",
"Nazar Delfino feat. Ethan",
"Nazar Drago",
"Nazareth",]

n_rus_list_6 = [
"Nazaro Ft. VOSSÆ",
"NaЯ",
"Nbdy",
"NBSPLV",
"NCT",
"NCT 127",
"NDR8 & Devan",
"NDS vs. Tom E feat. Ella",
"Ne-Yo",
"Nea Nelson",
"Neal Love",
"Neal Schon",
"NEBA",
"Nebbra feat. The Great Escape",
"Nebenraum feat. Ida Stein",
"Nebesno",
"Nebezao",
"Nebo7",
"Nebster",
"Nebula",
"Nechaev",
"Necro Stellar",
"Necronomidol",
"Necrovist",
"Nector feat. Iman",
"Ned Shepard & Sultan feat. Zella Day & Sam Martin",
"NEEDSHES",
"Needtobreathe",
"Neerah",
"Neev Kennedy",
"Nefera",
"Neffex",
"Negd Pul, Pan & Elkey",
"Negin",
"Negramaro",
"Neha Kakkar",
"NeiDan & Анастасия",
"Neiked",
"Neil Diamond",
"Neil Finn",
"Neil Young",
"Neiokoso",
"NEIR & LIS feat. Kami",
"Nej feat. Zaho",
"Nejee",
"Nejo & Nicky Jam",
"Nejtrino & Baur",
"Nejtrino & Elia",
"Nejtrino & Misha Klein",
"Nekby",]

n_rus_list_7 = [
"NEL",
"Nellie McKay",
"Nello & Aint",
"Nelly feat. 2 Chainz",
"Nelly feat. Chris Brown",
"Nelly feat. Daley",
"Nelly feat. Fabolous & Wiz Khalifa",
"Nelly feat. Florida Georgia Line",
"Nelly feat. Future",
"Nelly feat. Jeremih",
"Nelly Feat. Kelly Rowland",
"Nelly feat. Nelly Furtado",
"Nelly feat. Nicki Minaj & Pharrell",
"Nelly feat. Pharrell & T.I.",
"Nelly feat. Problem & Tyga",
"Nelly feat. T.I.",
"Nelly feat. T.I. & Drumma Boy",
"Nelly feat. Trey Songz",
"Nelly feat. Yo Gotti",
"Nelly Furtado",
"Nelly Mes",
"Nelly RA & Laera",
"Nelson Can",
"Nelson Freitas feat. Juan Magan",
"Nelson Riddle",
"Nelson Rongell",
"Nely Vanessa",
"NemanGrad",
"Nemanja Kostic feat. Renata Glizijan",
"Nemec & VoOne & D-Mas",
"Nemelka",
"Nemesea",
"Nemesis",
"NEMO feat. Sunny Cross",
"Nemowave feat. Sweet Ross",
"Nena",
"Nenna Yvonne",
"Neoclubber",
"Neomaster",
"Neon",
"Neon Dreams",
"Neon Hitch",
"Neon Horse",
"Neon Jungle",
"Neon Light",
"Neon Ninja",
"Neon Tiger",
"Neon Trees",
"Neonov",
"Neoton Familia",]

n_rus_list_8 = [
"Neotune feat. Morano",
"Neoxyne",
"Nephaim & Tyler Ocean",
"Neptune Motion",
"Neptune Project",
"Neptunica",
"Nera",
"Nerak feat. Miyagi & Эндшпиль",
"Nerina Pallot",
"Nermina",
"Nero",
"NeruGadza",
"Nervo",
"Nesco",
"Nesh Core feat. Flora Petnehazy & Zoltan Krix",
"Nesly feat. Cheb Bilal",
"Nessy & Flaip",
"Nessy & Misha Elle",
"NesteA",
"Nestor Torres",
"NeSVETskie",
"Net Brothers feat. Nika Mills",
"Netani",
"Nethracedicon",
"Netsky",
"Netta",
"Netzwerk",
"Neumodel feat. Mary H",
"NEUS",
"Neutralize",
"Nevada & Loote",
"Nevel",
"Nevelik",
"Nevena Bozovic",
"Never Later feat. Dora Pereli",
"Neverest",
"Nevergreen",
"Neverland",
"Neveryon",
"NEVMEWOOD",
"Nevrolog",
"New Baccara",
"New Boyz",
"New Center",
"New Dialogue",
"New Dimension Orchestra",
"New Electronic Symphony",
"New Fresh feat. Alla",
"New Hope Club",
"New In Paris",]

n_rus_list_9 = [
"New Kids On The Block",
"New Order",
"New Order feat. La Roux",
"New Phynix feat. Matthew Steeper",
"New Politics",
"New World Punx feat. Cara Salimando",
"New World Sound",
"New York Moskva",
"New Zealand Shapeshifter",
"Newclaess",
"NewClass",
"NewDay",
"Newik & Dragon S",
"Newkid",
"Newsboys",
"Newton",
"Nexboy",
"Nexeri",
"Nexet & Mic",
"Next feat. Slim",
"Next Habit",
"Next Time",
"Nexx",
"Neylini",
"Nez feat. Schoolboy Q",
"Nezir Kara",
"NeБрат",
"Nghtmre",
"NGTY & Alev",
"Ni Ego",
"Nia Sioux feat. Coco Jones",
"Niall Horan",
"Niamh Kavanagh",
"Nianaro",
"Nibiru",
"Niblewild",
"Nic Billington",
"Nic Chagall & Jonathan Mendelsohn",
"Nicci",
"Nicco",
"Nicholas Black",
"Nicholas Gunn",
"Nicholas Krgovich",
"Nick & Knight",
"Nick Amstok",
"Nick Arbor feat. Alana Aldea",
"Nick Austin",
"Nick Brewer",
"Nick Cannon",
"Nick Carter",]

n_rus_list_10 = [
"Nick Cave And The Bad Seeds",
"Nick Corline",
"Nick Cox feat. Lil Lee",
"Nick Curly & Steffen Deux",
"Nick Da Cruz",
"Nick Doe feat. Louise Golbey",
"Nick Double",
"Nick Drake",
"Nick Fiorucci feat. Joee",
"Nick Fradiani",
"Nick Galea",
"Nick Gardner",
"Nick Havsen",
"Nick Hook feat. 24hrs",
"Nick Jay feat. Melissa Tkautz",
"Nick Jonas",
"Nick Kamarera",
"Nick Kapa feat. Eva",
"Nick Lachey",
"Nick Lawyer",
"Nick Le Funk",
"Nick Marino",
"Nick Martin & LOVRA",
"Nick Martin",
"Nick Minoro feat. Xana",
"Nick Morena",
"Nick Moritz",
"Nick Murphy",
"Nick Novity",
"Nick O'Nill",
"Nick Otronic & High Level feat. Sharon Rupa",
"Nick Peloso",
"Nick Peters",
"Nick Sember",
"Nick Skitz",
"Nick Sky feat. Daisy",
"Nick Straker Band",
"Nick Strand & Mio",
"Nick Talos",
"Nick Thayer & A Skillz",
"Nick Urb",
"Nick V",
"Nick&Jo",
"Nickasaur",
"NickBee",
"Nickelback",
"Nicki French",
"Nicki Minaj",
"Nicklas Sahl",
"Nicko Nikos Ganos",]

n_rus_list_11 = [
"Nickolas Ilnitskiy feat. Влад Дарвин",
"Nicky B feat. Sean Paul & Synthkartell",
"Nicky Blitz",
"Nicky Byrne",
"Nicky feat. Cristina",
"Nicky Jam",
"Nicky Jones & Squad feat. Valentina",
"Nicky Motta feat. HazeUp",
"Nicky Night Time feat. Nat Dunn",
"Nicky Romero",
"Nicky Thomas",
"Nicky Valentine",
"Nicky Welton feat. Marlena",
"Nicky Will feat. Bess Beckmann",
"Nicky YaYa",
"Niclas Danielsen",
"Nico & Vinz",
"Nico De Andrea",
"Nico feat. F.Charm",
"Nico feat. Shobby",
"Nico Otten feat. Crystal Blakk",
"Nico Pellerin Feat. Laura Newman",
"Nico Santos",
"Nicola Fasano",
"Nicola Maddaloni & Crystal Blakk",
"Nicola Robert",
"Nicola Roberts",
"Nicola Veneziani",
"Nicola Zucchi",
"Nicolas Costa feat. Gaela Brown",
"Nicolas Haelg",
"Nicolas Hanning feat. Kyle Pearce",
"Nicolas Hernandez",
"Nicolas Martin",
"Nicolas Prodan",
"Nicolas Tikhonov feat. Ann",
"Nicolaz feat. Angelika Vee",
"Nicole Cherry",
"Nicole Cross",
"Nicole Holness",
"Nicole Kidman",
"Nicole M.Y feat. Andi Vax",
"Nicole Millar",
"Nicole Scherzinger",
"Nicoleta Matei & Vlad Mirita",
"Nicoleta Nuca",
"Nicoline",
"Nicolle",
"Nicu Voicu",
"Nide & DMNM",]

n_rus_list_12 = [
"Niello",
"Niels Brinck",
"Niels Geusebroek",
"Niels Van Gogh",
"Niereich & Linus Quick",
"Nifty",
"Nigar Jamal feat. Berksan",
"Nigel Good",
"Nigel Hard",
"Nigel'",
"Night & Day",
"Night Circus",
"Night Deejay feat. Nicky",
"Night Drive",
"Night Flight",
"Night In Wales",
"Night Ray",
"Night Safari feat. James Newman",
"Night Terrors Of 1927 feat. Tegan & Sara",
"Nightbird",
"Nightgeist",
"Nightstylers feat. Dan Brown",
"Nightwish",
"Niia",
"Niia feat. Jazmine Sullivan",
"Niiko feat. SWAE & Olaf Blackwood",
"Niila",
"Niila & Perttu",
"Nijana",
"Nik & Jay",
"Nik Brinkman feat. Erith",
"Nik Ernst",
"NIK feat. Adamant & Джиос",
"Nik Stazz feat. Владимир Панченко (Faktor-2)",
"Nik Turmalin",
"Nika Bright",
"Nika Dostur (Sofamusic)",
"Nika feat. Vlad Gorbanfeat",
"Nika Kocharov & Young Georgian Lolitaz",
"Nika Lenina feat. Da Kent DJ At Work",
"Nikalas Senteo & T1One",
"Nikasoul",
"Nikelback",
"Nikelle",
"Nikhil Prakash feat. Trianda",
"Niki Safrano",
"Nikice vs. Polina Goudieva",
"NIKIPHOROV",
"Nikita Bend",
"Nikita Bredkas",]

n_rus_list_13 = [
"Nikita Ferra",
"Nikita Jones",
"Nikita Malinin",
"Nikita RIF",
"Nikita Rise & Roman Akrill",
"Nikita Spy",
"Nikitin",
"Nikki Barr",
"Nikki D.",
"Nikki Flores",
"Nikki Jean",
"Nikki Lee",
"Nikki Ponte",
"Nikki Vianna & Matoma",
"Nikki Williams",
"Nikko Culture",
"Nikky Rocket",
"Niklas Aman",
"Niklas Gustavsson",
"Niklas Ibach feat. Dan Reeder",
"Nikless vs. ENV feat. Huntar & Goldzbrough",
"Niko & Emjay",
"Niko De Luka",
"Niko Hinkiladze",
"Niko Noise",
"Niko Spencer feat. Will Diamond",
"Niko The Kid",
"Niko Walters",
"Niko Zografos",
"Nikola feat. Livingstone",
"Nikola Gala",
"Nikolai Lugansky",
"Nikolaj Norlund",
"Nikolay Kempinskiy & Phillipo Blake feat. V.Ray",
"Nikolay Lourens",
"Nikolay Mikryukov",
"Nikolaz & Gant vs. Jerique",
"Nikonn",
"Nikos Ganos",
"Nikos Souliotis & Bo feat. Amaryllis",
"Niks feat. Chroma",
"Nikson",
"Nikstail",
"Niku Feat. Sardi",
"Nila Mania",
"Nile Rodgers & Chic",
"Niletto",
"Nili Brosh",
"Niloo",
"Nils Lofgren",]

n_rus_list_14 = [
"Nils Van Zandt",
"Nilson feat. John Harris",
"Nilufer Yanya",
"Nima feat. Reza Shiri",
"Nima Nesta & Marco G feat. Stephan Pickup",
"Nima Tahmasebi",
"Nimmo",
"Nimo & Capo",
"Nin9",
"Nina Ann",
"Nina Astrom",
"Nina Badric",
"Nina Bogdanova",
"Nina Fame feat. CupcakKe",
"Nina Gartler",
"Nina Kraljic",
"Nina Kray",
"Nina Moiseeva",
"Nina Nastasia",
"Nina Nesbitt",
"Nina Persson",
"Nina Simone",
"Nina Sky",
"Nina Sublatti",
"Nina Van Horn",
"Nina Zilli",
"Nine Inch Nails",
"Nineteen Sines",
"Ninetoes & Fatboy Slim",
"Ninja Coma feat. Диана Сладкая",
"Ninja Tracks",
"Nino Brown feat. T-Pain",
"Nino Katamadze & Insight",
"Nino Prses",
"Nino Ricardo",
"Nino Rota",
"Ninos Hanna",
"Nio Garcia & Arcangel & Young Blade feat. Bryant Myers",
"Nipo",
"Nippandab",
"Nipsey Hussle",
"Niqle Nut",
"Niqo Nuevo feat. Marvin Game",
"Nique, Mark & Prince feat. Delaney Jane",
"Nirah feat. Young",
"Niraj Chohan",
"NiRe AllDai",
"Nirvana",
"Niska feat. Booba",
"Niterockers feat. Andy LaToggo",]

n_rus_list_15 = [
"Niti & Dila",
"Niti feat. Dila",
"Nitrate",
"Nitro",
"Nitro Fun",
"Nitrogods",
"Nitrous Oxide",
"Nitti Gritti",
"Niukid",
"Nive",
"Niviro",
"NiVNAL",
"Nixx feat. Marq Markuz, PG, Батишта",
"Niykee Heaton",
"Nize Noize",
"NJohn & Букатара",
"Njomza",
"NK (Настя Каменских)",
"NKTN",
"Nla feat. Shanell",
"NLSN feat. Dominic Neill",
"NLVi & Mobdog feat. Ericka Hunter",
"NLVi feat. Jonny Rose",
"NMC feat. Tanya R.",
"Nneka",
"No Angels",
"No Artificial Colours & Catchment feat. Alex Mills",
"No Doubt",
"No Frills Twins",
"No Good Crook",
"No Hopes",
"NO ID feat. Stephen Pickup",
"No Idols",
"No Maka",
"No Mana",
"No Mercy",
"No Method",
"No Mondays",
"No Name",
"No Panties Allowed",
"No Requests",
"No Riddim & Megan Lee",
"No Rules",
"No Sleep feat. Gia Koka",
"No Smile Gvng feat. Drenny",
"No Trixx & Adrien Toma feat. Cynthia Brown, Maradja",
"No Wyld feat. KAMAU",
"No-Man",
"No/Me",
"Noa",]

n_rus_list_16 = [
"Noa I Mira Awad",
"Noah Cyrus",
"Noah Kahan",
"Noah Neiman",
"Nobby Reed Project",
"Nobuo Uematsu",
"Nocturn",
"Node & Gilli",
"Nodi Tatishvili & Sophie Gelovani",
"Noe",
"Noee",
"Noel Blanco feat. Eimy Sue",
"Noel Gallagher's High Flying Birds",
"Noel Gitman feat. Buran B",
"Noel Gourdin",
"Noelia",
"Noelia Jay",
"Noella Nix",
"Noemi Perino",
"Noemi Smorra feat. Lena Katina",
"NOEP",
"Nofar Salman",
"Noise Freakz feat. Sarah Whatmore",
"Noise Galleri feat. Yungen",
"Noise Killerz",
"Noise Patrol",
"Noise Zoo feat. Brandon Mignacca",
"Noisecontrollers",
"Noisestorm",
"Noisettes",
"Noisia",
"Noisy Dealer & Arikakito",
"Noita",
"Noize Criminal",
"Noize Generation",
"Noizekik",
"Noizy feat. Ardian Bujupi",
"Noker Meretov",
"Nokturn Es",
"Nola feat. 2 Ляма",
"Nolan Rivera",
"Nolans Stenemberg",
"Nolita",
"Noll",
"Nolove & Deesmi",
"Nomad",
"NomaS & Elize",
"NoMBe",
"Nomera & Вячеслав Никаноров",
"NOMERA feat. Алексей Яшин CASUAL",]

n_rus_list_17 = [
"NOMNOM",
"NoMosk & Roman Messer feat. Christina Novelli",
"Nomy feat. Alexander Tidebrink",
"Nomyn",
"NoName feat. Phoelix",
"Nonamerz И Maestro A-Sid",
"None",
"NonGrata feat. Витя Сенс",
"Noniyr",
"Nonis G",
"Nonono",
"Nonsens",
"Nonstop",
"Noonie Bao",
"Nopassport",
"Nopopstar Ft. Sevenever",
"Nora En Pure",
"Nora Hilton",
"Nora Istrefi",
"Norah Jones",
"Nordean feat. Zoe Badwi",
"Nordic Union",
"Norell",
"Noriel",
"Norlie & KKV",
"Norma John",
"Normal'ный",
"Norman Doray",
"Norman Greenbaum",
"Normani",
"North & South feat. Barak Levy",
"North Base",
"North Coast Vibes",
"North Elements feat. Melman",
"North Side",
"North Way",
"Northlane",
"Northumbria",
"Northway",
"Norwood & Hills",
"Nosfe feat. Ruby",
"Nostalgia",
"Nostradame Feat. Trooper",
"Not Profane feat. Sandra Cires",
"Not Your Dope feat. Oly",
"Not3s",
"Notaker",
"NOTD & Daya",
"NOTD",
"Note U",]

n_rus_list_18 = [
"NoteМи feat. НепонятыйВами",
"NoteМи feat. оРеХ",
"Nothing But The Beat",
"Nothing But Thieves",
"Nothing Like You",
"Nothing,Nowhere. & Travis Barker",
"Notimes",
"Nourii",
"Nova Casa",
"Nova Discoteque",
"Nova Miller",
"Nova Rockafeller",
"Nova Scotia feat. Aj",
"Novaa",
"Novak",
"Novaspace",
"Novel",
"Novell",
"Novella",
"Novo Amor",
"Novo Menco",
"Now United",
"Now, Now",
"Nowak",
"NowImJoey",
"Nox",
"Noy",
"Noze feat. Riva Starr",
"NoЯ",
"NPans",
"NRD1 feat. Piweer & Chiaro",
"Nreason",
"Nrg Band",
"NRG feat. Stage One",
"NrgMind",
"NSH feat. Charla K",
"NSolo",
"Nstasia feat. Skrillex",
"NTL & Вирус",
"Nu Gianni",
"Nu Jerzey Devil",
"NU SZN & USMAN",
"Nuar",
"Nuclear Fuel",
"Nude",
"Nue",
"Nuelle",
"Nuera feat. Szen",
"Nuestro",
"NuKid",]

n_rus_list_19 = [
"Null Positiv",
"Numall Fix & Freaky DJ's",
"Numan Paul feat. Tina V",
"Numbers",
"Nume",
"Numidia",
"Nuno Resende",
"Nuno Ribeiro feat. David Carreira",
"Nuovo & Jarico",
"Nurettin Colak",
"NURI",
"Nuria Swan",
"Nurii feat. Nathan Brumley",
"Nurkan Pazar",
"Nurko",
"Nusa Derenda",
"NuSound",
"Nuteki",
"Nutone",
"Nuuxs",
"NV feat. Ksenia",
"NVDES",
"NVDREC",
"NVEK",
"NVSTIKV",
"NWYR",
"NxtGen feat. Will.i.Am",
"Nya De La Rubia & Juan Magan",
"Nyagara",
"Nyanda",
"Nycer",
"Nyemiah Supreme",
"Nyla feat. Paul Secondi & Monarques",
"NyLO feat. KYLE & SG Lewis",
"NYMZ & Taylor Felt",
"NyoMii",
"Nysveen & Kristin Seiersten",
"Nytrix",
]

litera = SoundSymbol.objects.get(name="N")

count = 0

for tag in n_rus_list_19:
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
