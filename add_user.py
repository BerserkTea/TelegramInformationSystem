from multiprocessing.sharedctypes import Value
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import csv

my_database = [['Viktoriia', 'Silaeva', '@SilaevaViktoriia', 'OZ'],
        ['Georgy', ' ', '@GeorgyRus', ' '],
        ['Yana', ' ', '@ZYAZY', 'Mosou'],
        ['Alexander', 'Krivoruchko', ' ', 'Taganrog'],
        ['Yuri', 'Filatov', '@Yrafilatov', ' '],
        ['Marc', 'Scobelev', ' ', ' '],
        ['Ilyas', 'Amirchupanov', '@ailyas80', 'Astrakhan'],
        ['Julia', 'Shurygina',	'@juliawise', 'Moscou'],
        ['Konstantin', 'Stepanov', '@Konstantin_Stepanov_1988',	'Moscou'],
        ['Anton', 'Korolev', '@TonyKorolev', 'Cheboksary'],
        ['Julia', ' ', ' ', 'Murmansk'],
        ['Ivan', 'Cheremisov',	'@cheremisovIvan', ' '],
        ['Dmitry', 'Lopatinsky', '@obezyanoid', 'Saratov'],
        ['Inna', ' ', '@Shvarchik', ' '], 	
        ['Michail',	'Yurkov', '@YurkovMix',	' '],	
        ['Anna', 'Kuchumova', ' ', 'Dmitrov'],
        ['Alexandra', 'K',	' ', 'Brest'],
        ['Denis', ' ', ' ', ' '], 			
        ['John', 'Smith', '@gramenbos', ' '], 	
        ['Anastasiia', 'Venskaiia', ' ', 'Kaluga'],
        ['Viktoriia', ' ', ' ', ' '],		
        ['Roman', 'Rogachev', ' ', 'Tver'],
        ['Dmitryi', 'Spasskich', '@afinaPalladda', ' '],	
        ['Ilya', 'Limakov', '@Limakov777', ' '],	
        ['Pavel', 'Gluchov', '@CovChEGG', 'Novosibirsk'],
        ['Ivan', ' ', '@Ivantaf', ' '], 	
        ['Dmitriy', ' ', '@Dmitriy_GM',	'Saratov'],
        ['Insaf', 'Gimatdinov', ' ', ' '],		
        ['Pavel', 'L', ' ', ' '],		
        ['Irina', 'Kudriaxa', '@irina_kudriaxa', ' '],	
        ['Evgeniy', 'D', '@Slonniikk', ' '],
        ['Anna', ' ', ' '],			
        ['Julia', 'B', '@yulichka_kram', 'Gelendzhik'],
        ['Ivan', 'Andronov', '@berserktea1', 'Moscou'],
        ['Daniil', 'Kobzar', '@Blaky299', ' '],	
        ['Elvira', 'Zagrebneva', '@ZEN_cher', 'Cherepovets'],
        ['Anton', 'Zubarev', '@My_name_is_vezenie', ' '],	
        ['Nadya', 'Gromova', '@NadyaGromova', 'Moscou'],
        ['Anna', 'Kaminskaia', '@anna_kami_rnd', 'Rostov-na-Donu'],
        ['Anna', ' ', '@Gerald_0f_Rivia', 'Krasnodar'],
        ['Sergey', 'Petryakov', '@Petryakov_sergey', ' '],	
        ['Denis', 'Viscount', '@viscountKender', ' '],	
        ['Ivan', ' ', '@Ivanw16', ' '],	
        ['Roman', ' ', '@RamTGM', ' '],	
        ['Q', ' ', '@okeybutwhy', ' '],	
        ['B.B.K.', ' ',	' ', ' '],		
        ['Shavkat', 'Nasimov', '@Nasimoffffff', 'Moscou'],
        ['Sergey', 'Kamyanetsky', '@ksergeyru', 'Moscou']]

k = 1
dict_database = {}
for i in my_database:
    dict_database[k] = i
    k+=1
print(dict_database[5])

def index():
    with open('database.csv', newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        index = len(data) + 1
        return index


# for j in dict_database: 
with open('database.csv', 'w', encoding='UTF-8') as my_file:
    for key, v in dict_database.items():
        my_file.write("{}; {}\n".format(key, v))
#         # writer = csv.writer(my_file)
#           writer.writerows(dict_database)
# print("Oh, well done, mate") 
#     # print(dict_database)   

# username = Update.effective_user.first_name

def write_user():
    id = index()
    name = "kjlk"
    surname = "kffd"
    username = "oijh"
    city = "uhgn"
    with open('database.csv', 'a', encoding='UTF-8') as wu:
        writer = csv.writer(wu)
        wu.write(f'{id};{name},{surname},{username},{city}')
        wu.write(f'\n')
# write_user()

# def write_to_file():
#     id = ui_f.id()
#     name = ui_f.username()
#     surname = ui_f.surname()
#     phone_number = ui_f.phone()
#     comment = ui_f.comments()
       