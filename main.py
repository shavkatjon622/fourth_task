#first task
# 1. Bankomat dasturi (input, if, else)
#     • Foydalanuvchidan bank hisobiga kiritish yoki yechish miqdorini so'rang. Agar hisobda yetarli mablag' bo'lmasa, xato xabarini ko'rsating. Hisob qoldig'ini ekranga chiqaring.
#     • Foydalanuvchidan pin-kod so'rab, to'g'ri kiritsa, "Xush kelibsiz" degan xabarni chiqaring. Aks holda, "Noto'g'ri pin-kod" deb chop eting.
from pydoc import plain
from traceback import print_tb


# class Bankomat():
#     """First assignment"""
#     def __init__(self, pin):
#         self.__pin = pin
#         self.budget = 0
#
#     def add_money(self, sum):
#         self.budget = self.budget + sum
#         return f"Your budget: {self.budget}"
#
#     def withdraw(self, pin, sum):
#         if self.__pin == pin:
#             if self.budget >= sum:
#                 self.budget -= sum
#                 return f"Successfully. Please take your {sum} money"
#             else:
#                 return 'don`t enough money'
#         else:
#             return 'Error pin!'
#     def get_account(self, pin):
#         if self.__pin == pin:
#             return f"Your balans: {self.budget}"
#         else:
#             return f"Error pin code"




# second task
#2. Do'kon hisob-kitobi (input, if, elif, else, for, dictionary)
#    • 5 ta mahsulot nomini va ularning narxlarini lug'atga saqlang. Foydalanuvchidan mahsulot nomini kiriting va uning narxini chop eting. Agar mahsulot ro'yxatda bo'lmasa, "Mahsulot topilmadi" deb ko'rsating.
#     • Har bir mahsulotning sonini so'rang va jami narxni hisoblang. Agar jami narx 100 ming so'mdan oshsa, 10% chegirma qo'llang.

# class Market():
#     def __init__(self, **products):
#         self.products = products
#
#     def get_product(self, **products):
#         cost = 0
#         text = ''
#         for product, quantity in products.items():
#             if product in self.products.keys():
#                 cost = cost + quantity * self.products[product]
#             else:
#                 text =  f"We have not {product}"
#         if cost>= 100000:
#             cost = cost - (cost*0.1)
#             text += f"\nYou have 10% discount. Your shopping {cost}"
#         else:
#             text += f"Your shopping {cost}"
#         return text



# third task
# 3. Student baholari (list, for, if-elif-else)
#     • 10 ta o'quvchining baholarini ro'yxat sifatida saqlang. Har bir bahoni tekshiring va "O'tdi" yoki "O'tmadi" natijasini chop eting.
#     • Foydalanuvchidan baholar kiriting va o'rtacha bahoni hisoblab, chiqaring. Agar o'rtacha baho 80 dan yuqori bo'lsa, "A'lochi", 50-80 oralig'ida bo'lsa "Yaxshi", 50 dan past bo'lsa "Yomon" deb chop eting.

# class Student():
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#
#     def check_mark(self):
#         if self.mark > 100 or self.mark < 0:
#             return 'Error'
#         elif self.mark >= 60:
#             return 'Passed'
#         else:
#             return 'Failed'
#
#     def set_mark(self, *mark):
#         total = sum(mark)
#         result = total / len(mark)
#         if result > 100 or result < 0:
#             return 'Error'
#         elif result >= 80:
#             return 'Perfect'
#         elif result >= 50:
#             return 'Good'
#         else:
#             return 'Bad'




#fourth task
#4. Tug'ilgan kun dasturi (input, if, string)
    # • Foydalanuvchidan tug'ilgan sanasini so'rang. Agar sana bugungi kun bilan bir xil bo'lsa, "Tug'ilgan kuningiz bilan!" deb chiqaring.
    # • Foydalanuvchidan yoshi va ismini so'rang, agar yoshi 18 dan kichik bo'lsa, unga saytdan foydalanish mumkin emasligini bildiring.

# import datetime
# class Date():
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def congratulation(self):
#         today = datetime.date.today()
#         if self.day == today.day and self.month == today.month:
#             return "Happy Birthday!"
#         else:
#             return 'not bad'
#
#     def check_age(self):
#         today = datetime.date.today()
#         if today.year - self.year < 18:
#             return 'You don`t old enough'
#         else:
#             return 'You are welcome'


#fifth task
#5. Mehmonxonada xona bron qilish (input, list, for, if-elif-else)
    # • 5 xil turdagi mehmonxona xonalarini ro'yxat sifatida saqlang. Foydalanuvchidan xona turini kiriting va uni bron qiling. Agar xona band bo'lsa, boshqa xonalarni taklif eting.
    # • Foydalanuvchidan bir necha kechaga xona bron qilishni so'rang. Jami narxni hisoblang va ko'rsating. Agar narx 1 milliondan oshsa, 5% chegirma bering.

# import datetime
# class Date():
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
# class Hotel():
#     def __init__(self, **rooms):
#         self.rooms = rooms
#
#     def check_room(self, rooms):
#         if rooms in self.rooms.keys():
#             del self.rooms[rooms]
#             return f"Room {rooms} is available"
#         else:
#             return f"Room {rooms} is not available. Try another room: {', '.join(self.rooms.keys())}"
#
#     def book_room(self, **rooms):
#         text = ''
#         cost = 0
#         for rooms, day in rooms.items():
#             if rooms in self.rooms.keys():
#                 cost = cost + self.rooms[rooms] * day
#                 del self.rooms[rooms]
#                 text += f"Room {rooms} is booked"
#             else:
#                 text += f"Room {rooms} is not available. \nTry another room: {', '.join(self.rooms.keys())}"
#         if cost>= 100000:
#             cost = cost - (cost*0.05)
#             text += f"\nYou have 5% discount. Your room cost: {cost}"
#         elif cost == 0:
#             pass
#         else:
#             text += f"\nYour shopping {cost}"
#         return text




# sixth task
#6. Kutubxona tizimi (for, list, dictionary)
    # • Kitoblar ro'yxati va ularning mavjud yoki yo'qligi haqida ma'lumotni lug'atda saqlang. Foydalanuvchidan kitob nomini so'rang va agar kitob mavjud bo'lsa, uni berib yuboring, aks holda boshqa kitoblarni taklif eting.
    # • 5 ta kitob nomini va ularning mualliflarini ro'yxat sifatida saqlang. Foydalanuvchi qaysi muallifning kitoblarini so'rasa, unga shu muallifning kitoblarini ko'rsating.


# class Library():
#     def __init__(self, **books):
#         self.books = books
#
#     def check_book(self, book):
#         for author, books in self.books.items():
#             if book in books:
#                 books.remove(book)
#                 return f"Book {book} is available"
#             else:
#                 return f"Book {book} is not available. Try another book: {', '.join(books)}"
#
#     def author_books(self, author):
#         for author, books in self.books.items():
#             if author == author:
#                 return books
#
# kitob = Library( james_krill = ['Python','JavaScript', 'C#', 'C++', 'Java'])
# print(kitob.author_books('james_krill'))




# seventh task
#7. Reja tuzuvchi dastur (while, input, list)
    # • Foydalanuvchidan rejalari haqida ma'lumot kiritishni so'rang. U kiritgan har bir rejani ro'yxatga qo'shib boring va rejalari tugagandan so'ng, ro'yxatni chop eting.
    # • Foydalanuvchi "chiqish" so'zini yozmaguncha, undan rejalarini kiritishni davom eting. Tugallangandan keyin barcha rejalarning umumiy ro'yxatini ko'rsating.


# class Planner():
#     def __init__(self, name):
#         self.name = name
#
#     def make_plan(self):
#         n = 0
#         plans = []
#         while 1:
#             n += 1
#             plan = input(f'Enter your {n}-plan:(exit for exit) ')
#             if plan == 'exit':
#                 break
#             else:
#                 plans.append(plan)
#                 continue
#         return f"Your plans: {', '.join(plans)}"


#eighth task
#8. Valyuta konvertori (input, if, elif)
    # • Foydalanuvchidan valyuta turi (USD, EUR, GBP) va summani kiriting. Kirilgan summani milliy valyutaga aylantiring. Har bir valyuta uchun turli kurslarni qo'llang.
    # • Foydalanuvchi turli valyutalarda kirilgan summalarni konvertatsiya qilishni so'rasin va yakuniy narxlarni ko'rsating.


# class Convertor():