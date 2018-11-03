#!/usr/bin/env python3
# awsmsg.py
# программа, которая генерирует псевдослучайные истории
# версия 0.1

import random

# имена (кто?)
names1 = ["Тимофей","Оксана","Ярик","Толян","Лысый",
		"Наталя","Тёма","Олежка","Диана",
		"Димас","Лёха","Джеки Софт","Шмара","Нубас","Костян","твоя мамаша"]
# имена (у кого?)
names2 = ["Тимофея","Оксаны","Ярика","Толяна","Лысого",
		"Натали","Тёмы","Олежки","Дианы",
		"Димаса","Лёхи","Джеки Софта","Шмары","Нубаса","Костяна","твоей мамаши"]

storys = ["история","кулстори","тема","ситуация"]

whathpnds = ["случилась","произошла","приключилась","была"]

artcs = ["слегка","довольно-таки","достаточно","более-менее","очень"]

# время
times = ["вчера","сегодня","только что","пару минут назад","с утра пораньше",
		"прошлой зимой","прошлым летом","очень давно","только что","хуй знает когда",
		"на прошлой неделе","во вторник","в субботу","на Новый год","на день рождения твоей мамаши"]

# место (где?)
places = ["в туалете","на вейп-выставке","на берегу неба","в Жмеринском лесу","на какой-то движухе",
		"на притоне","в школе","в универе","на рейве","на концерте Infant Annihilator",
		"в генделе","в баре","в Ашане","возле АТБ","на Колибрисе",
		"у Лысого на даче","у Ярика дома","у Тимофея на кухне","у Дианы с Димасом",
		"в Виннице","во Львове","в Одессе","хуй его знает где","в чёрной дыре",
		"возле шаурмешной","возле Электронмаша","в какой-то глубокой жопе","на свадьбе","на похоронах",
		"в вейп-кафе","на поляне КПИ","у Лёхи на балконе","на пивном заводе","в вагоне метро"
		"в Харькове","на крыше дамбы","на вершине Эвереста","в пиццерии","в 'Пивоваре'"]

# как именно?
howexactly = ["грубо","бодро","плотно","сочно","люто",
		"спокойно","комфортно","напряжённо","весело","неплохо",
		"нормально","неожиданно","специально","интересно","стрёмно",
		"плохо","загадочно","жёстко","печально","прекрасно",
		"неумолимо","неуклюже","забавно","прикольно","сипло",
		"волшебно","иронично","идеально","хорошо","тупо",
		"жизненно","именно","качественно","зачётно","ужасно",
		"хуй знает как","топово","занятно","замечательно","странно",
		"клёво","всрато","потешно","няшно"]
		
# какая именно?
howexactly2 = ["грубая","бодрая","плотная","сочная","лютая",
		"спокойная","комфортная","напряжённая","веселая","неплохая",
		"нормальная","неожиданная","специальная","интересная","стрёмная",
		"плохая","загадочная","жёсткая","печальная","прекрасная",
		"неумолимая","неуклюжая","забавная","прикольная","сиплая",
		"волшебная","ироничная","идеальная","хорошая","тупая",
		"жизненная","красивая","качественная","зачётная","ужасная",
		"хуй знает какая","топовая","занятная","замечательная","странная",
		"клёвая","всратая","потешная","няшная"]

# что делал/а?
didwhatm = ["лежал","валялся","сидел","сидел на кортах","сидел на жопе ровно",
		"танцевал","умирал","курил вейп","мешал жижу","тусил",
		"употреблял наркотики","бухал","залипал","играл в Hearthstone","гамал",
		"занимался непонятно чем","ничего не делал","плакал","рыдал","умилялся котикам",
		"кусал себя","смотрел смешные картинки","грустил","курил сигу","стоял",
		"делал дырки в фольге","мутил замуты","жрал пирожок","ел борщ","пил кофей",
		"хавал ништяки","шморгал носом","смеялся","снимал блог","спал",
		"втычил","подгорал","рисовал хуй","продавал гараж","лабал на гитаре"]

didwhatw = ["лежала","валялась","сидела","сидела на кортах","сидела на жопе ровно",
		"танцевала","умирала","курила вейп","мешала жижу","тусила",
		"употребляла наркотики","бухала","залипала","играла в Hearthstone","гамала",
		"занималась непонятно чем","ничего не делала","плакала","рыдала","умилялась котикам",
		"кусала себя","смотрела смешные картинки","грустила","курила сигу","стояла",
		"делала дырки в фольге","мутила замуты","жрала пирожок","ела борщ","пила кофей",
		"хавала ништяки","шморгала носом","смеялась","снимала блог","спала",
		"втычила","подгорала","рисовала хуй","продавала гараж","лабала на гитаре"]

# что делали? (множественное число)
didwhatt = ["лежали","валялись","сидели","сидели на кортах",
		"танцевали","умирали","курили вейп","мешали жижу","тусили",
		"употребляли наркотики","подбухивали","залипали","играли в Hearthstone",
		"занимались непонятно чем","плакали","рыдали","умилялись котикам",
		"смотрели смешные картинки","грустили","курили сиги","стояли",
		"жрали пирожки","пили кофей","летали","кружили", "работали",
		"хавали ништяки","шморгали носом","смеялись","снимали видосы","спали",
		"втычили","подгорали","лабали на гитаре"]

# (хотел/а что сделать?)
dowhat = ["полежать","поваляться","посидеть","посидеть на кортах",
		"потанцевать","умереть","покурить вейп","замешать жижу","потусить",
		"въебать наркотиков","забухать","позалипать","поиграть в Hearthstone",
		"позаниматься непонятно чем","поплакать","пофлексить","поумиляться котикам",
		"укусить себя","посмотреть смешные картинки","погрустить","покурить сигу",
		"сделать дырки в фольге","замутить шото мутное","сожрать пирожок","попить кофея",
		"похавать ништяки","пошморгать носом","знатно посмеяться","снять видос","поспать",
		"повтычить","полабать на гитаре"]

# смысл жизни
slife = ["лежать и не двигаться","валяться где попало","сидеть на жопе ровно","не остаться в этой траве",
		"танцевать тектоник","умереть","курить вейп","мешать жижу","тусить и врываться в движ",
		"въебывать наркотики","бухать","залипать во всякую хуйню","писать генераторы историй",
		"хуй","плакать и страдать","низко флексить","умиляться котикам",
		"ненавидеть чёрных","сохранять смешные картинки","ходить в шлёпках","курить сиги",
		"прятать фольгу от мусоров","мутить шото мутное","жрать","выходить на кофей к Ашану",
		"хавать разные ништяки","шморгать носом","смеять с чужого смеха","выкладывать истории в инстаграмме",
		"спать"]

# что-то сделать
dowhatwh = ["что-то придумать","шото подраспетлять","понять","шото решить","ещё постоять",
		"шото поделать","выпить","покурить вейп","позалипать",
		"немедленно умереть","где-то потусить","что-то замутить","пойти похавать","выпить кофея",
		"ещё постоять и понять","повтычить"]

# где? (ограниченный выбор мест)
whereis = ["под столом","на кровати","на толчке","под диваном","на пуфике",
		"на земле","за компом","в стороне от всех","хуй знает где","сбоку",
		"за углом","за стоечкой","перед теликом","в гамаке","на подоконнике",
		"в умывальнике","в мусорном ведре"]

# какие? (мч)
whatkindt = ["грубые","бодрые","плотные","сочные","лютые",
		"спокойные","пьяные","напряжённые","весёлые","упоротые",
		"нормальные","неожиданные","специальные","интересные","стрёмные",
		"рандомные","загадочные","жёсткие","печальные","прекрасные",
		"потешные","неуклюжие","забавные","прикольные","сиплые",
		"волшебные","ироничные","идеальные","хорошие","тупые",
		"злые","отбитые","качественные","зачётные","ужасные",
		"хуй знает какие","топовые","занятные","замечательные","странные",
		"клёвые","всратые","патлатые","убитые","потрёпанные","подгоревшие",
		"хмурые","хуй знает какие","бадяжные","мистические","охуенные","няшные"]

# кто? (мч)
whois = ["молодые персонажи","пассажиры","тела","люди","бомжи",
		"собаки","котейки","пацанчики","подружани","вейперы",
		"мужики с завода","продавцы-консультанты","контент-менеджеры","тайные покупатели","хуй знает кто",
		"модники","клоуны","баттл-рэперы","школьники","школьницы",
		"ребята","веганы","хардкорщики","задроты","азиаты",
		"малые","чуваки","официанты","дурачки","алкаши"]

# приветствие
hello = ["'Привет'","'Здорова'","'Вечер в хату'","'Йоу'","'Здрасте'",
		"'Шо ты?'","'Шо ты, голова?'","'Аллоха!'","'Опана'","'Ёб твою мать, кого я вижу'",
		"'Ты хули тут стал?'","'Сап'"]

# пошли (синонимы)
gowhere = ["погнали","двинули","пошагали","попетляли","рванули",
		"полетели","взяли такси","сели в лоховоз","стали ждать маршрутку","вызвали вертолёт",
		"поехали на гироскутерах","упали в телегу","прыгнули в травмай","пошли собирать деньги на бензин"]

# погода (какая?)
weather = ["дождливая","солнечная","просто сок","прикольная","бодрая",
		"лютая","такая шо аж снегом заносило","хуй знает какая","просто охуенная","с грозой и молниями"]

# предметы, вещи
things = ["бутылки вискаря","бокс-моды","флаконы с жижей","трусы твоей мамаши","чикеты",
		"звёзды","астероиды","лучи добра","лучи ненависти","космические корабли",
		"поддоны с цементом","чехлы для айфона","яблочки","акции Microsoft","самооценки","курсы валют",
		"спиннеры с алиекспресс","мёртвые крысы","жевачки 'love is'","пирожки с капустой","маски Гая Фокса"]

# провалились куда?
fall_in = ["в канализацию","в ад","в подвал","в бездну","в чёрную дыру",
		"в вейп-шоп","в хуй","в пизду","в какую-то ебучую шахту","нахуй"]

# ____________________
# основная функция

def makeStory():
	TEXT = ""

	# Эта история произошла буквально вчера.
	TEXT = "Эта " + random.choice(storys) + " " + random.choice(whathpnds) + " " + random.choice(times) + ". "

	# Дело было на рейве. 
	TEXT = TEXT + "Дело было " + random.choice(places) + ". "

	# выбираем имя - если оно женское, то ставим женские глаголы, если мужское - мужские
	NAME_ONE = random.choice(names1)
	if NAME_ONE in ["Оксана","Наталя","Диана","Шмара","твоя мамаша"]:
		tmpstr2 = random.choice(didwhatw)
		tmpstr3 = "очень хотела"
		tmpstr4 = "ей"
		tmpstr5 = "подумала"
		tmpstr6 = "была"
		tmpstr7 = "подумала"
		tmpstr8 = "задержала"
	else:
		tmpstr2 = random.choice(didwhatm)
		tmpstr3 = "очень хотел"
		tmpstr4 = "ему"
		tmpstr5 = "подумал"
		tmpstr6 = "был"
		tmpstr7 = "подумал"
		tmpstr8 = "задержал"

	names1.remove(NAME_ONE)

	# Диана в это время неуклюже умирала на пуфике.
	TEXT = TEXT + NAME_ONE + " в это время " + random.choice(howexactly) + " " + tmpstr2 + " " + random.choice(whereis) + ". " 

	# Вокруг стояли какие-то рандомные контент-менеджеры.
	TEXT = TEXT + "Вокруг " + random.choice(didwhatt) + " какие-то " + random.choice(whatkindt) + " " + random.choice(whois) + ". " 

	tmpstrn1 = random.choice(names1)
	if tmpstrn1 in ["Оксана","Наталя","Диана","Шмара","твоя мамаша"]:
		tmpstrn2 = "запретила"
	else:
		tmpstrn2 = "запретил"

	names1.remove(tmpstrn1)

	# Ярик очень хотел потанцевать, но Олежка ему запретил.
	TEXT = TEXT + NAME_ONE + " " + tmpstr3 + " " + random.choice(dowhat) + ", но " + tmpstrn1 + " " + tmpstr4 + " " + tmpstrn2 + ". "

	# 'Лучше бы я сейчас был возле Ашана' - подумал Димас.
	TEXT = TEXT + "'Лучше бы я сейчас " + tmpstr6 + " " + random.choice(places) + "' - " + tmpstr7 + " " + NAME_ONE + ". "

	# абзац
	TEXT += "\n"

	# персонаж №2
	NAME_TWO = random.choice(names1)
	if NAME_TWO in ["Оксана","Наталя","Диана","Шмара","твоя мамаша"]:
		nametwo1 = "подошла"
		nametwo2 = "поздоровалась она. "
		nametwo3 = " выглядела "
	else:
		nametwo1 = "подошёл"
		nametwo2 = "поздоровался он. "
		nametwo3 = " выглядел "

	names1.remove(NAME_TWO)

	# И тут непонятно откуда подошёл Лысый.
	TEXT = TEXT + "И тут непонятно откуда " + nametwo1 + " " + NAME_TWO + ". "

	# 'Шо ты, голова?' - поздоровался он.
	TEXT = TEXT + random.choice(hello) + " - " + nametwo2

	# Нубас выглядел слегка всрато.
	TEXT = TEXT + NAME_TWO + nametwo3 + random.choice(artcs) + " " + random.choice(howexactly) + ". "

	# абзац
	TEXT += "\n"

	# Оксана и Шмара постояли и поняли, что нужно выпить кофея.
	TEXT = TEXT + NAME_ONE + " и " + NAME_TWO + " постояли и поняли, что нужно " + random.choice(dowhatwh) + ". "

	# персонаж №3
	NAME_THREE = random.choice(names2)

	# И лучше всего это было сделать у Тимофея.
	TEXT = TEXT + "И лучше всего это было сделать у " + NAME_THREE + ". "

	# Ну они и поехали на гироскутерах.
	TEXT = TEXT + "Ну они и " + random.choice(gowhere) + ". "

	#абзац
	TEXT += "\n"

	# Погода была как раз просто охуенная, так что добрались весело.
	TEXT = TEXT + "Погода была как раз " + random.choice(weather) + ", так что добрались " + random.choice(howexactly) + ". "

	# Под падиком у Тёмы залипали контент-менеджеры, но никто не обратил на них внимания.
	TEXT = TEXT + "Под падиком у " + NAME_THREE + " " + random.choice(didwhatt) + " " +  random.choice(whois) + ", но никто не обратил на них внимания. "

	# Наконец-то зашли в дом. Обстановка тут была весьма неплохая - под диваном жрал пирожок котей, а с потолка падали самооценки.
	TEXT = TEXT + "Наконец-то зашли в дом. Обстановка тут была весьма " + random.choice(howexactly2) + " - " + random.choice(whereis) + " " + random.choice(didwhatm) + " котей, а с потолка падали " + random.choice(things) + ". "
	
	# Все вместе поболтали и решили сначала умереть.
	TEXT = TEXT + "Все вместе поболтали и решили сначала " + random.choice(dowhat) + ". "

	# Но внезапно земля ушла из под ног и все провалились в канализацию.
	TEXT= TEXT + "Но внезапно земля ушла из под ног и все провалились " + random.choice(fall_in) + ". "

	#абзац
	TEXT += "\n"

	# персонаж №4
	NAME_FOUR = random.choice(names1)
	if NAME_FOUR in ["Оксана","Наталя","Диана","Шмара","твоя мамаша"]:
		namefour1 = "стояла "
		namefour2 = "сообщила "
		namefour3 = "сказала "
		namefour4 = "неё "
	else:
		namefour1 = "стоял "
		namefour2 = "сообщил "
		namefour3 = "сказал "
		namefour4 = "него "

	# Вокруг было темно, а в центре стоял Лёха.
	TEXT = TEXT + "Вокруг было темно, а в центре " + namefour1 + NAME_FOUR + ". " 

	# .
	TEXT = TEXT + "Сзади " + namefour4 + "были какие-то непонятные " + random.choice(whois) + ", которые " + random.choice(didwhatt) + " и " + random.choice(didwhatt) + ". "

	# 'Вы сюда провалились для того, чтобы я сообщил вам смысл жизни' - сказал Лёха.
	TEXT = TEXT + "'Вы сюда провалились для того, чтобы я " + namefour2 + "вам смысл жизни' - " + namefour3 + NAME_FOUR + ". "

	# Оксана задержала дыхание в ожидании ответа.
	TEXT = TEXT + NAME_ONE + " " + tmpstr8 + " дыхание в ожидании ответа. "

	#абзац
	TEXT += "\n"

	TEXT = TEXT + "'Итак...' - "

	# .
	TEXT = TEXT + "голос звучал " + random.choice(artcs) + " " + random.choice(howexactly) + ". "

	#абзац
	TEXT += "\n"

	TEXT = TEXT + "'смысл жизни - " + random.choice(slife) + "'. "
	
	return TEXT


