promt_start = """Если он говорит про образование напиши - education
Если он говорит, что ему нужно оставить заявку чтобы отправить ребенка в школу  напиши - school
Если он говорит, что ему нужно оставить заявку чтобы отправить ребенка в школу и напишет фио или дату рождения напиши - school, сюда напиши ФИО из сообщения если оно есть иначе None, сюда напиши дату рождения из сообщения если оно есть иначе None, все напиши через запятую
Если он говорит, что ему нужно отправить ребенка в детский сад  напиши - kindergarten
Если он говорит, что ему нужно оставить заявку чтобы отправить ребенка в детский сад и напишет фио или дату рождения напиши - kindergarten, сюда напиши ФИО из сообщения если оно есть иначе None, сюда напиши дату рождения из сообщения если оно есть иначе None, все напиши через запятую
Если он говорит про Вуз  напиши - does_not_work
Если он говорит про колледж, шарагу  напиши - does_not_work
Если он говорит, что ему нужно узнать кто из его детей пойдет в школу или детский сад - past_education
если он говорит об здоровье, медицинской помощи, походе к врачам напиши - doctors
если он говорит об медицинском полисе напиши - policy
если он говорит о вождение, машине, водительских правах или что-то связанных с авто напиши - avto
если он говорит про коммунальные услуги, жкх, счет энергии, стоимость воды напиши - communal_services
если ничего не подходит из этого, напиши - help
Пиши только слова, которые я сказал"""