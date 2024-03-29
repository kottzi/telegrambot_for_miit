import telebot

from telebot import types

bot = telebot.TeleBot('5036206527:AAFf_C4IMcRyzG4kGuweMls0bGIiz2UlVPU')

@bot.message_handler(commands=['start'])
# ---------------------------------------------------------------------------

def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_1 = types.KeyboardButton("📖Категории")
    start_2 = types.KeyboardButton("📨Поддержка")

    markup.add(start_1, start_2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!✋\nЯ - <b>{1.first_name}</b>, помогу тебе с поступлением в МИИТ🎓".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup
                     )


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '📖Категории':

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('🎓Коротко об ИУЦТ', callback_data='1')
            item2 = types.InlineKeyboardButton('📚Специальности ИУЦТ', callback_data='2')
            item3 = types.InlineKeyboardButton('📃Документы', callback_data='3')
            item4 = types.InlineKeyboardButton('☎️ Контакты', callback_data='4')
            item5 = types.InlineKeyboardButton('💯Проходные баллы', callback_data='5')
            item6 = types.InlineKeyboardButton('🧧Приём на обучение иностранных граждан', callback_data='6')
            item7 = types.InlineKeyboardButton('⏳Сроки зачисления', callback_data='7')
            item8 = types.InlineKeyboardButton('🏬Предоставление общежития', callback_data='8')
            item9 = types.InlineKeyboardButton('🏥Медицина', callback_data='9')
            item10 = types.InlineKeyboardButton('🏅Индивидуальные достижения', callback_data='10')
            item11 = types.InlineKeyboardButton('📋Целевое обучение', callback_data='11')
            item12 = types.InlineKeyboardButton('💳Платное обучение, стоимость', callback_data='12')
            item_back = types.InlineKeyboardButton('🔚Вернуться в главное меню', callback_data='13')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item_back)

            bot.send_message(message.chat.id, '🔔Какие категории вас интересуют?',
                             reply_markup=markup
                             )

        elif message.text == "📨Поддержка":
            bot.send_message(message.chat.id, " Если возникли какие-либо вопросы, напишите вот сюда:" +
            "@Vitro665, @Nicktelega, @sealex1, @kottzi")

        elif message.text == '📘Специалитет':
            bot.send_message(message.chat.id, '23.05.04 Эксплуатация железных дорог')

        elif message.text == '📗Бакалавриат':
            bot.send_message(message.chat.id,
                             '01.03.02 Прикладная математика и информатика\n09.03.01 Информатика и вычислительная техника\n' +
                             '09.03.02 Информационные системы и технологии\n10.03.01 Информационная безопасность\n' +
                             '20.03.01 Техносферная безопасность\n23.03.01 Технология транспортных процессов\n38.03.02 Менеджмент')

        elif message.text == '📕Магистратура':
            bot.send_message(message.chat.id,
                             '01.04.02 Прикладная математика и информатика\n09.04.01 Информатика и вычислительная техника\n' +
                             '10.04.01 Информационная безопасность\n20.04.01 Техносферная безопасность\n23.04.01 Технология транспортных процессов\n' +
                             '23.04.02 Наземные транспортно-технологические комплексы\n38.04.02 Менеджмент')

        elif message.text == '🩺Мед. осмотр':

            medview = types.ReplyKeyboardMarkup(resize_keyboard=True)
            medviewdoctors = types.KeyboardButton('👨🏻‍⚕️Список врачей')
            medviewanalysis = types.KeyboardButton('🩸Список анализов')
            back_1 = types.KeyboardButton('🔙Вернуться к медецине')
            medview.add(medviewdoctors, medviewanalysis, back_1)

            bot.send_message(message.chat.id,
                             'В качестве документа, подтверждающего прохождение медицинского осмотра и необходимых лабораторных исследований, может быть предоставлена справка формы 086/у или АКУ-22.',
                             reply_markup=medview
                             )

        elif message.text == '👨🏻‍⚕️Список врачей':
            bot.send_message(message.chat.id,
                             'Медицинский осмотр должен включать в себя следующих врачей-специалистов:\n 🔹 Терапевт;\n 🔹 Невролог;\n 🔹 Оториноларинголог;\n 🔹 Офтальмолог;\n 🔹 Хирург.')

        elif message.text == '🩸Список анализов':
            bot.send_message(message.chat.id,
                             'Медицинский осмотр должен включать в себя следующие лабораторные инструментальные исследования:\n 🔹 Клинический анализ крови (гемоглобин, цветной показатель, эритроциты, тромбоциты, лейкоциты, лейкоцитарная формула, СОЭ);\n 🔹 Клинический анализ мочи (удельный вес, белок, сахар, микроскопия осадка);\n 🔹 Цифровая флюорография или рентгенография в 2-х проекциях (прямая и правая боковая) легких.')

        elif message.text == '🗳Как прикрепиться?':
            bot.send_message(message.chat.id,
                             'Для прикрепления к поликлинике университета всем студентам первого курса при заселении в общежитие необходимо иметь следующие документы:\n 🔹 Паспорт (копия);СНИЛС (копия);\n 🔹 Полис обязательного медицинского страхования (ОМС) (копия);\n 🔹 Копия первой страницы паспорта одного из родителей и номер его (ее) телефона - для несовершеннолетних лиц (младше 18 лет);\n 🔹 Заполненные и подписанные заявления на прикрепление к поликлинике РУТ (МИИТ), которые можно скачать в личном кабинете на сайте университета (логин и пароль для авторизации выдают при подаче документов в приемной комиссии).')

        elif message.text == '📱Контакты':

            medcontacts = types.ReplyKeyboardMarkup(resize_keyboard=True)
            mednumber = types.KeyboardButton('☎️Номер телефона')
            medmail = types.KeyboardButton('📧Электронная почта')
            back_1 = types.KeyboardButton('🔙Вернуться к медецине')
            medcontacts.add(mednumber, medmail, back_1)

            bot.send_message(message.chat.id,
                             'Адрес: 127055, г. Москва, ул. Новосущевская, д. 18\n\nДни приема: понедельник – пятница с 9:00 до 15:00',
                             reply_markup=medcontacts
                             )

        elif message.text == '☎️Номер телефона':
            bot.send_message(message.chat.id, 'Регистратура - +7(499)978-63-35\nОхрана - +7(499)978-03-73')

        elif message.text == '📧Электронная почта':
            bot.send_message(message.chat.id, 'Электронная почта:\npolyclinic@miit.ru')

        elif message.text == '🔙Вернуться к медецине':
            medicine = types.ReplyKeyboardMarkup(resize_keyboard=True)

            med_view_info = types.KeyboardButton('🩺Мед. осмотр')
            med_attach_info = types.KeyboardButton('🗳Как прикрепиться?')
            med_contacts = types.KeyboardButton('📱Контакты')
            Return2 = types.KeyboardButton('🔙Вернуться к категориям')

            medicine.add(med_view_info, med_attach_info, med_contacts, Return2)

            bot.send_message(message.chat.id, '✅Что именно вас интересует?',
                             reply_markup=medicine
                             )
        elif message.text == '📋Контракт':
            bot.send_message(message.chat.id,
                             'Договор об образовании заключается в простой письменной форме между университетом и зачисляемым на обучение.\n' +
                             'Сведения, указанные в договоре об оказании платных образовательных услуг, соответствуют информации, размещенной на официальном сайте университета.\n\n' +
                             'Подробнее вы можете ознакомиться по ссылке ниже:\nhttps://www.miit.ru/sveden/paid_edu')

        elif message.text == '💵Цена':
            bot.send_message(message.chat.id,
                             'Стоимость обучения по специальностям (специализациям), направлениям (профилям) и формам обучения для поступающих, размещена на странице «План приёма»\n\n' +
                             'Подробнее вы можете ознакомиться по ссылке ниже:\nhttps://www.miit.ru/sveden/paid_edu')

        elif message.text == 'Информация о сроках зачисления на бюджетную основу обучения':
            bot.send_message(message.chat.id, 'Этапы зачисления на бюджетную основу обучения: '
                                                     '\n 1)размещение списков поступающих на официальном сайте и (или) в электронной информационной системе – 27 июля. '
                                                     '\n 2) 3 августа – день завершения приёма заявлений о согласии на зачисление от лиц,' +
                             'включенных в списки поступающих на основные конкурсные места и желающих быть зачисленными на основном этапе зачисления.')

        elif message.text == 'Информация о сроках зачисления на целевую основу обучения':
            bot.send_message(message.chat.id, '28 июля – день завершения приёма заявлений о согласии на зачисление от лиц, поступающих без вступительных испытаний, поступающих на места в пределах квот..')

        elif message.text == 'Информация о сроках зачисления на “квотную” основу обучения':
            bot.send_message(message.chat.id, '28 июля – день завершения приёма заявлений о согласии на зачисление от лиц, поступающих без вступительных испытаний, поступающих на места в пределах квот. ')

        elif message.text == 'Информация о сроках зачисления на платную основу обучения':
            bot.send_message(message.chat.id, 'Этапы зачисления на платную основу обучения:'
                                                      '\n 1) 12 июля – издаётся приказ (приказы) о зачислении поступающих, предоставивших согласие на зачисление не позднее 9 июля'
                                                      '\n 2) 30 июля – издаётся приказ (приказы) о зачислении поступающих, предоставивших согласие на зачисление не позднее 28 июля'
                                                      '\n 3) 19 августа – издаётся приказ (приказы) о зачислении поступающих, предоставивших согласие на зачисление не позднее 16 августа'
                                                      '\n 4) 26 августа – издаётся приказ (приказы) о зачислении поступающих, предоставивших согласие на зачисление не позднее 24 августа')

        elif message.text == '🏬Приемная комиссия':
            bot.send_message(message.chat.id, 'Центральная приёмная комиссия\n\nТелефон: +7 495 260-23-32\n\nE-mail: pk@rut-miit.ru\n\nРежим работы:' +
            ' Понедельник-пятница с 09:30 до 16:30, Суббота с 09:30-14:30 (вторая половина июня-первая половина августа)\n\n127994, г. Москва, ул. Новосущёвская, д. 22 (ГУК №3, кабинет 3316)')

        elif message.text == '🏢ИУЦТ':
            bot.send_message(message.chat.id, 'Институт управления и цифровых технологий, ИУЦТ\n\nТелефон: +7 495 684-21-21\n\nE-mail: info@miit.ru\n\n' +
                             'Сайт:  https://imiit.ru\n\n127055, г. Москва, ул Образцова, д. 9, стр. 9')

        elif message.text == '📗Бакалавриaт':
            bot.send_message(message.chat.id, 'При приёме на обучение по программам бакалавриата, программам специалитета поступающему может быть начислено за индивидуальные достижения не более 10 баллов суммарно.\n\n' +
                             '10 баллов начисляется: \n🔸 Чемпионам Олимпийских игр \n🔸 За аттестат с отличием \n🔸 Победителям Всероссийского конкурса «Транспорт будущего»\n\n' +
                             '7 или 5 баллов начисляется: \n🔸 Призёрам Всероссийского конкурса «Транспорт будущего» \n🔸 Призёрам первой степени конкурса «3D БУМ» \n\n' +
                             'Более подробно на сайте: https://miit.ru/page/136668')

        elif message.text == '📘Магистратурa':
            bot.send_message(message.chat.id, 'При приёме на обучение по программам магистратуры поступающему может быть начислено за индивидуальные достижения не более 100 баллов суммарно.\n\n' +
                             '🔸 50 баллов начисляется победителям всероссийской олимпиады студентов «Я – профессионал» по направлению «Транспорт»\n\n' +
                             '🔸 50 баллов начисляется призёрам всероссийской олимпиады студентов «Я – профессионал» по направлению «Транспорт»\n\n' +
                             '🔸 30 за наличие статей, опубликованных под авторством поступающего, в изданиях, входящих в базы Scopus и (или) Web of Science')

        elif message.text == '📨Как подать заявку':
            bot.send_message(message.chat.id, 'Вот, что тебе нужно сделать: \n Шаг 1. Указать в личном деле о необходимости предоставления о необходимости предоставления общежития при условии поступления за счёт бюджета.' +
                                              '\n Шаг  2. Открыть личный кабинет. В зависимости от решения комиссии вскоре будет сформирован ордер на заселение в общежитие.')

        elif message.text == '🏬О общежитиях':
            bot.send_message(message.chat.id, '🔹1-ое общежите находится по адресу: 103055, г. Москва, 2-й Вышеславцев пер., д. 17 Телефон: +7 (495) 684-29-52\n\n' +
                             '🔹2-ое общежите находится по адресу:101475, г. Москва, ул. Образцова, д. 22 Телефон: +7 (495) 689-25-33\n\n' +
                             '🔹3-ое общежите находится по адресу:129323, г. Москва, ул. Снежная, д. 16, корпус 3 Телефон: +7 (499) 189-37-27\n\n' +
                             '🔹4-ое общежите находится по адресу:127322, г. Москва, Огородный проезд, д. 25/20 Телефон: +7 (495) 618-92-24\n\n' +
                             '🔹5-ое общежите находится по адресу:129301, г. Москва, ул. Космонавтов, д. 11 Телефон: +7 (495) 683-27-78\n\n' +
                             '🔹6-ое общежите находится по адресу:129347, г. Москва, ул. Палехская, д. 145 Телефон: +7 (499) 182-34-72\n\n' +
                             '🔹7-ое общежите находится по адресу:Московская область, Раменский район, пос. Кратово, ул. Симбирская, д. 13 Телефон: +7 (498) 483-15-27\n\n' +
                             '🔹8-ое общежите находится по адресу:125635, г. Москва, Новая улица, д. 4 Телефон: +7 (499) 905-31-00\n\n' +
                             '🔹9-ое общежите находится по адресу:г. Москва, ул. Бутырская, д. 79, подъезд 2\n\n' +
                             '🔹10-ое общежите находится по адресу:г. Москва, ул. Судостроительная, д. 32, корпус 2 Телефон: +7 (499) 618-52-80\n\n' +
                             '🔹11-ое общежите находится по адресу:г. Москва, ул. 2-й Южнопортовый проезд, д. 5, корпус 2 Телефон: +7 (495) 958-95-36\n\n')

        elif message.text == '📑Документы для общежития':
            bot.send_message(message.chat.id, '1) Ордер\n\n2) паспорт и его копия (в т.ч. страницы с пропиской)\n\n' +
                             '3) Медицинская справка о состоянии здоровья из поликлиники по месту жительства\n\n' +
                             '4) Три фотографии (3x4, цветные, матовые)\n\n5) Лицам мужского пола (кроме проживающих в Московской области)' +
                             'необходимо иметь на руках приписное свидетельство, а также следует предварительно сняться с воинского учёта' +
                             'по месту жительства (для этого необходимо обратиться в свой военкомат с извещением о поступлении в университет,' +
                             'само извещение придёт по почте на адрес, указанный при подаче документов). При наличии военного билета с воинского учета сниматься не надо\n\n' +
                             '6) Согласие на заключение договора найма: документ, с подписью законного представителя (родителя, опекуна) для несовершеннолетних студентов\nСам документ:\n' +
                             'https://www.miit.ru/content/%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B5.docx?id_wm=817375\n\n' +
                             '7) Согласие на персональную обработку данных')

        elif message.text == '📜Инструкция':
            bot.send_message(message.chat.id, 'Как подать документы иностранным гражданам:\n\n1) Необходимо зарегистрироваться на сайте, ввести номер своего мобильного телефона и свою электронную почту.' +
                             'На указанную почту будет направлено письмо с логином и паролем от личного кабинета.\n\n2) Заходим в личный кабинет, переходим во вкладку "Мое поступление",' +
                             'нажимаем на кнопку "Заполнить заявление".\n\n3) В открывшемся окне надо заполнить сведения:\n' +
                             '🔹 Паспорт\n🔹 Образование\n🔹 Адрес\n🔹 Родители\n🔹 Вступительные испытания\n🔹 Специальности\n🔹 Льготы\n🔹 Достижения\n🔹 Прикрепление документов\n\n' +
                             'Инструкцию вы можете прочеесть по ссылке ниже:\nhttps://rut-miit.ru/page/171057')

        elif message.text == '🗃Необходимые документы':
            bot.send_message(message.chat.id, '1) Паспорт\n\n2) Нотариально заверенный перевод паспорта на русский язык (при отсутствии русской страницы в паспорте)\n\n' +
                             '3) Аттестат/диплом и приложение с оценками\n\n4) Нотариально заверенный перевод на русский язык аттестата/диплома и приложения с оценками (при отсутствии русских страниц)\n\n' +
                             '5) Фотография\n\n6) Если абитуриенту нет 18 лет, дополнительно представляется:\n🔹 Свидетельство о рождении\n' +
                             '🔹 Нотариально заверенный перевод на русский язык свидетельства о рождении (при отсутствии русских страниц)\n' +
                             '🔹 Паспорт родителя (матери и отца или законного представителя)\n' +
                             '🔹 Нотариально заверенный перевод на русский язык паспорта одного из родителей или законного представителя (при отсутствии русских страниц)\n\n' +
                             '7) По приезде в РУТ (МИИТ) иностранному студенту необходимо представить в учебный отдел (ауд. 1301) следующие дополнительные документы:\n' +
                             '🔹 Миграционная карта (кроме гр. Беларуси)\n🔹 Копия визы на въезд в Российскую Федерацию (для стран с визовым въездом)\n' +
                             '🔹 Регистрация по месту пребывания\n🔹 Медицинская справка о состоянии здоровья 086/у\n' +
                             '🔹 ВИЧ-сертификат\n🔹 Отрицательный ПЦР-тест на Covid-19, полученный в течение 72 часов после въезда в РФ')

        elif message.text == '📄Информация':
            bot.send_message(message.chat.id, 'Целевое обучение – это обучение на основе договора о целевом обучении, заключенного между гражданином и организацией.')

        elif message.text == '🗃Категории':
            bot.send_message(message.chat.id, '🔹 Федеральными государственными органами, органами государственной власти субъектов Российской Федерации, органами местного самоуправления\n\n' +
                             '🔹 Государственными и муниципальными учреждениями, унитарными предприятиями\n\n🔹 Государственными корпорациями\n\n🔹 Государственными компаниями\n\n' +
                             '🔹 Организациями, включенными в сводный реестр организаций оборонно-промышленного комплекса, формируемый в соответствии с частью 2 статьи 21 Федерального закона' +
                             'от 31 декабря 2014 года N 488-ФЗ "О промышленной политике в Российской Федерации"\n\n🔹 Хозяйственными обществами, в уставном капитале которых присутствует доля' +
                             'Российской Федерации, субъекта Российской Федерации или муниципального образования\n\n🔹 Акционерными обществами, акции которых находятся в собственности или' +
                             'в доверительном управлении государственной корпорации\n\n🔹 Дочерними хозяйственными обществами: государственных компаний; хозяйственных обществ,' +
                             'в уставном капитале которых присутствует доля Российской Федерации, субъекта Российской Федерации или муниципального образования; акционерных обществ,' +
                             'акции которых находятся в собственности или в доверительном управлении государственной корпорации\n\n🔹 Организациями, которые созданы государственными' +
                             'корпорациями или переданы государственным корпорациям в соответствии с положениями федеральных законов об указанных корпорациях')

        elif message.text == '🗃Список необходимых документов':
            bot.send_message(message.chat.id, '🔹 Документ государственного образца об образовании (аттестат, диплом)\n'+
                             '🔹 Документ, удостоверяющий личность и гражданство (паспорт, вид на жительство и так далее)\n' +
                             '🔹 Документ, удостоверяющий личность и гражданство (паспорт, вид на жительство и так далее)\n' +
                             '🔹 Документы, подтверждающие особые права при приёме, при их наличии\n' +
                             '🔹	Документы, подтверждающие индивидуальные достижения, при их наличии\n' +
                             '🔹	СНИЛС (при наличии)\n' +
                             '🔹	Личная фотография размером 3*4\n')

        elif message.text == '📝Как подать документы':
            bot.send_message(message.chat.id, 'Есть 4 варината, как подать документы в МИИИТ:\n\n1) Через личный кабинет rut-miit.ru\n' +
                             '2) Через операторов почтовой связи общего пользования\n3) На портале государственных услуг: https://www.gosuslugi.ru/10077/1\n' +
                             '4) Лично (в приемной комиссии института)')



        elif message.text == '🔙Вернуться к категориям':

            markup = types.InlineKeyboardMarkup(row_width=1)

            item1 = types.InlineKeyboardButton('🎓Коротко об ИУЦТ', callback_data='1')
            item2 = types.InlineKeyboardButton('📚Специальности ИУЦТ', callback_data='2')
            item3 = types.InlineKeyboardButton('📃Документы', callback_data='3')
            item4 = types.InlineKeyboardButton('☎️ Контакты', callback_data='4')
            item5 = types.InlineKeyboardButton('💯Проходные баллы', callback_data='5')
            item6 = types.InlineKeyboardButton('🧧Приём на обучение иностранных граждан', callback_data='6')
            item7 = types.InlineKeyboardButton('⏳Сроки зачисления', callback_data='7')
            item8 = types.InlineKeyboardButton('🏬Предоставление общежития', callback_data='8')
            item9 = types.InlineKeyboardButton('🏥Медицина', callback_data='9')
            item10 = types.InlineKeyboardButton('🏅Индивидуальные достижения', callback_data='10')
            item11 = types.InlineKeyboardButton('📋Целевое обучение', callback_data='11')
            item12 = types.InlineKeyboardButton('💳Платное обучение, стоимость', callback_data='12')
            item_back = types.InlineKeyboardButton('🔚Вернуться в главное меню', callback_data='13')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item_back)

            bot.send_message(message.chat.id, '🔔Какие категории вас интересуют?',
                             reply_markup=markup
                             )

        else:
            bot.send_message(message.chat.id, '❌Такого варианта ответа нет')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1)

                bot.send_message(call.message.chat.id, 'Институт управления и цифровых технологий осуществляет подготовку специалистов' +
                             'бакалавров и магистров в области организации и управления перевозками, менеджмента, транспортной' +
                             'логистики и сервиса, бизнеса пассажирских перевозок, грузовой и коммерческой работы, современных' +
                             'компьютерных технологий, экологической безопасности.\n\nВ институте более 150 профессоров и кандидатов наук,' +
                             'более 3 500 студентов. Функционирует 10 кафедр, из них 7 – выпускающие.\n\nВ учебном процессе используются более' +
                             '30 лабораторий и специализированных лекционных аудиторий, оснащенных самым современным оборудованием.\n\n' +
                             'Созданы и активно функционируют научно - образовательные и учебно-методические центры.' +
                             'Реализуются программы углублённой специализированной подготовки студентов старших курсов по системе «авторских классов».\n\n' +
                             'Институт реализует различные международные программы: двойные дипломы, стажировки, обменные практики и летние школы,' +
                             'сотрудничает с такими крупными компаниями. Активно внедряются дистанционные формы повышения квалификации персонала ОАО «РЖД».' +
                             'Также ведется большая работа по дополнительному профессиональному образованию на железнодорожном транспорте.\n\n' +
                             'Молодежный центр института управления и информационных технологий включает студенческий совет, пресс-центр,' +
                             'творческую мастерскую, спортивные секции, студенческие отряды, профбюро и др.\n\nВыпускники ИУЦТ успешно и плодотворно работают' +
                             'в различных отраслях транспорта, на крупнейших предприятиях ОАО «РЖД», а также в государствах дальнего зарубежья.' +
                             'Немало их трудится в Министерстве транспорта и других учреждениях, организациях и компаниях.' +
                             'Они решают технологические, организационно-управленческие, логистические и экономические задачи, разрабатывают информационные' +
                             'системы и их программное обеспечение.',
                                 reply_markup=markup
                                 )

            elif call.data == '2':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                Return1 = types.KeyboardButton('🔙Вернуться к категориям')
                item1 = types.KeyboardButton('📗Бакалавриат')
                item2 = types.KeyboardButton('📘Специалитет')
                item3 = types.KeyboardButton('📕Магистратура')

                markup.add(item1, item2, item3, Return1)
                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '13':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                start_1 = types.KeyboardButton("📖Категории")
                start_2 = types.KeyboardButton("📨Поддержка")

                markup.add(start_1, start_2)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '9':

                medicine = types.ReplyKeyboardMarkup(resize_keyboard=True)

                med_view_info = types.KeyboardButton('🩺Мед. осмотр')
                med_attach_info = types.KeyboardButton('🗳Как прикрепиться?')
                med_contacts = types.KeyboardButton('Контакты')
                Return2 = types.KeyboardButton('🔙Вернуться к категориям')

                medicine.add(med_view_info, med_attach_info, med_contacts, Return2)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=medicine
                                 )
            elif call.data == '12':

                paid_ed = types.ReplyKeyboardMarkup(resize_keyboard=True)

                contract = types.KeyboardButton('📋Контракт')
                prices = types.KeyboardButton('💵Цена')
                Return2 = types.KeyboardButton('🔙Вернуться к категориям')

                paid_ed.add(contract, prices, Return2)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=paid_ed
                                 )
            elif call.data == '7':

                markup = types.ReplyKeyboardMarkup(row_width=1)

                item1 = types.KeyboardButton('Информация о сроках зачисления на бюджетную основу обучения')
                item2 = types.KeyboardButton('Информация о сроках зачисления на целевую основу обучения')
                item3 = types.KeyboardButton('Информация о сроках зачисления на “квотную” основу обучения')
                item4 = types.KeyboardButton('Информация о сроках зачисления на платную основу обучения')
                item5 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3, item4, item5)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '4':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('🏬Приемная комиссия')
                item2 = types.KeyboardButton('🏢ИУЦТ')
                item3 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '10':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('📗Бакалавриaт')
                item2 = types.KeyboardButton('📘Магистратурa')
                item3 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '8':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('📨Как подать заявку')
                item2 = types.KeyboardButton('🏬О общежитиях')
                item3 = types.KeyboardButton('📑Документы для общежития')
                item4 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3, item4)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '6':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('📜Инструкция')
                item2 = types.KeyboardButton('🗃Необходимые документы')
                item3 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '5':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1)

                bot.send_message(call.message.chat.id, 'Каждый год проходные баллы в институт меняются, но вы можете ознакомится с проходными баллами 2021 года:' +
                '\nhttps://www.miit.ru/admissions/degrees?year=2020&city=1&level=4&training=20773',
                                 reply_markup=markup
                                 )
            elif call.data == '11':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('📄Информация')
                item2 = types.KeyboardButton('🗃Категории')
                item3 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )
            elif call.data == '3':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('🗃Список необходимых документов')
                item2 = types.KeyboardButton('📝Как подать документы')
                item3 = types.KeyboardButton('🔙Вернуться к категориям')

                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, '✅Что именно вас интересует?',
                                 reply_markup=markup
                                 )



    except Exception as e:
        print(repr(e))

# Старт
bot.polling(none_stop=True)

# ---------------------------------------------------------------------------
