#first task
# 1. Bankomat dasturi (input, if, else)
#     • Foydalanuvchidan bank hisobiga kiritish yoki yechish miqdorini so'rang. Agar hisobda yetarli mablag' bo'lmasa, xato xabarini ko'rsating. Hisob qoldig'ini ekranga chiqaring.
#     • Foydalanuvchidan pin-kod so'rab, to'g'ri kiritsa, "Xush kelibsiz" degan xabarni chiqaring. Aks holda, "Noto'g'ri pin-kod" deb chop eting.


class Bankomat():
    """First assignment"""
    def __init__(self, pin):
        self.__pin = pin
        self.budget = 0

    def add_money(self, sum):
        self.budget = self.budget + sum
        return f"Your budget: {self.budget}"

    def withdraw(self, pin, sum):
        if self.__pin == pin:
            if self.budget >= sum:
                self.budget -= sum
                return f"Successfully. Please take your {sum} money"
            else:
                return 'don`t enough money'
        else:
            return 'Error pin!'
    def get_account(self, pin):
        if self.__pin == pin:
            return f"Your balans: {self.budget}"
        else:
            return f"Error pin code"




# second task
#2. Do'kon hisob-kitobi (input, if, elif, else, for, dictionary)
#    • 5 ta mahsulot nomini va ularning narxlarini lug'atga saqlang. Foydalanuvchidan mahsulot nomini kiriting va uning narxini chop eting. Agar mahsulot ro'yxatda bo'lmasa, "Mahsulot topilmadi" deb ko'rsating.
#     • Har bir mahsulotning sonini so'rang va jami narxni hisoblang. Agar jami narx 100 ming so'mdan oshsa, 10% chegirma qo'llang.

class Market():
    def __init__(self, **products):
        self.products = products

    def get_product(self, **products):
        cost = 0
        text = ''
        for product, quantity in products.items():
            if product in self.products.keys():
                cost = cost + quantity * self.products[product]
            else:
                text =  f"We have not {product}"
        if cost>= 100000:
            cost = cost - (cost*0.1)
            text += f"\nYou have 10% discount. Your shopping {cost}"
        else:
            text += f"Your shopping {cost}"
        return text


# third task
# 3. Student baholari (list, for, if-elif-else)
#     • 10 ta o'quvchining baholarini ro'yxat sifatida saqlang. Har bir bahoni tekshiring va "O'tdi" yoki "O'tmadi" natijasini chop eting.
#     • Foydalanuvchidan baholar kiriting va o'rtacha bahoni hisoblab, chiqaring. Agar o'rtacha baho 80 dan yuqori bo'lsa, "A'lochi", 50-80 oralig'ida bo'lsa "Yaxshi", 50 dan past bo'lsa "Yomon" deb chop eting.

class Student():
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def check_mark(self):
        if self.mark > 100 or self.mark < 0:
            return 'Error'
        elif self.mark >= 60:
            return 'Passed'
        else:
            return 'Failed'

    def set_mark(self, *mark):
        total = sum(mark)
        result = total / len(mark)
        if result > 100 or result < 0:
            return 'Error'
        elif result >= 80:
            return 'Perfect'
        elif result >= 50:
            return 'Good'
        else:
            return 'Bad'




#fourth task
#4. Tug'ilgan kun dasturi (input, if, string)
    # • Foydalanuvchidan tug'ilgan sanasini so'rang. Agar sana bugungi kun bilan bir xil bo'lsa, "Tug'ilgan kuningiz bilan!" deb chiqaring.
    # • Foydalanuvchidan yoshi va ismini so'rang, agar yoshi 18 dan kichik bo'lsa, unga saytdan foydalanish mumkin emasligini bildiring.

import datetime
class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def congratulation(self):
        today = datetime.date.today()
        if self.day == today.day and self.month == today.month:
            return "Happy Birthday!"
        else:
            return 'not bad'

    def check_age(self):
        today = datetime.date.today()
        if today.year - self.year < 18:
            return 'You don`t old enough'
        else:
            return 'You are welcome'


#fifth task
#5. Mehmonxonada xona bron qilish (input, list, for, if-elif-else)
    # • 5 xil turdagi mehmonxona xonalarini ro'yxat sifatida saqlang. Foydalanuvchidan xona turini kiriting va uni bron qiling. Agar xona band bo'lsa, boshqa xonalarni taklif eting.
    # • Foydalanuvchidan bir necha kechaga xona bron qilishni so'rang. Jami narxni hisoblang va ko'rsating. Agar narx 1 milliondan oshsa, 5% chegirma bering.

import datetime
class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
class Hotel():
    def __init__(self, **rooms):
        self.rooms = rooms

    def check_room(self, rooms):
        if rooms in self.rooms.keys():
            del self.rooms[rooms]
            return f"Room {rooms} is available"
        else:
            return f"Room {rooms} is not available. Try another room: {', '.join(self.rooms.keys())}"

    def book_room(self, **rooms):
        text = ''
        cost = 0
        for rooms, day in rooms.items():
            if rooms in self.rooms.keys():
                cost = cost + self.rooms[rooms] * day
                del self.rooms[rooms]
                text += f"Room {rooms} is booked"
            else:
                text += f"Room {rooms} is not available. \nTry another room: {', '.join(self.rooms.keys())}"
        if cost>= 100000:
            cost = cost - (cost*0.05)
            text += f"\nYou have 5% discount. Your room cost: {cost}"
        elif cost == 0:
            pass
        else:
            text += f"\nYour shopping {cost}"
        return text




# sixth task
#6. Kutubxona tizimi (for, list, dictionary)
    # • Kitoblar ro'yxati va ularning mavjud yoki yo'qligi haqida ma'lumotni lug'atda saqlang. Foydalanuvchidan kitob nomini so'rang va agar kitob mavjud bo'lsa, uni berib yuboring, aks holda boshqa kitoblarni taklif eting.
    # • 5 ta kitob nomini va ularning mualliflarini ro'yxat sifatida saqlang. Foydalanuvchi qaysi muallifning kitoblarini so'rasa, unga shu muallifning kitoblarini ko'rsating.


class Library():
    def __init__(self, **books):
        self.books = books

    def check_book(self, book):
        for author, books in self.books.items():
            if book in books:
                books.remove(book)
                return f"Book {book} is available"
            else:
                return f"Book {book} is not available. Try another book: {', '.join(books)}"

    def author_books(self, author):
        for author, books in self.books.items():
            if author == author:
                return books

kitob = Library( james_krill = ['Python','JavaScript', 'C#', 'C++', 'Java'])
print(kitob.author_books('james_krill'))




# seventh task
#7. Reja tuzuvchi dastur (while, input, list)
    # • Foydalanuvchidan rejalari haqida ma'lumot kiritishni so'rang. U kiritgan har bir rejani ro'yxatga qo'shib boring va rejalari tugagandan so'ng, ro'yxatni chop eting.
    # • Foydalanuvchi "chiqish" so'zini yozmaguncha, undan rejalarini kiritishni davom eting. Tugallangandan keyin barcha rejalarning umumiy ro'yxatini ko'rsating.


class Planner():
    def __init__(self, name):
        self.name = name

    def make_plan(self):
        n = 0
        plans = []
        while 1:
            n += 1
            plan = input(f'Enter your {n}-plan:(exit for exit) ')
            if plan == 'exit':
                break
            else:
                plans.append(plan)
                continue
        return f"Your plans: {', '.join(plans)}"


#eighth task
#8. Valyuta konvertori (input, if, elif)
    # • Foydalanuvchidan valyuta turi (USD, EUR, GBP) va summani kiriting. Kirilgan summani milliy valyutaga aylantiring. Har bir valyuta uchun turli kurslarni qo'llang.
    # • Foydalanuvchi turli valyutalarda kirilgan summalarni konvertatsiya qilishni so'rasin va yakuniy narxlarni ko'rsating.


class Convertor():
    def __init__(self, user):
        self.user = user

    def usd_uzs(self, value):
        return 12700 * value

    def eur_uzs(self, value):
        return 13800 * value

    def gbp_uzs(self, value):
        return 16600 * value

#nineth task
#9. Mehmonlar ro'yxati (for, while, list, string)
    # • Foydalanuvchidan mehmonlarning ismini kiriting. Har bir mehmonning ismini teskari tartibda chop eting.
    # • Foydalanuvchidan 5 ta mehmon nomini so'rang, har bir ismni bosh harfi bilan boshlanadigan holatda chop eting (masalan, "ali" -> "Ali").


class Guest():
    def __init__(self, host):
        self.host = host

    def guests_reverse(self, guests): # Guests is list
        return f"Reverse name: {', '.join(guests)[::-1]}"

    def list_guests(self, guests): # Guests is list
        return f"Your guests: {', '.join(guests).title()}"



# tenth task
#10. Sayohat bron qilish tizimi (input, if, elif, list)
    # • 3 ta sayohat turi (ichki, xalqaro, sayohat kreyseri) tanlovini taklif eting. Foydalanuvchidan qaysi turdagi sayohatni tanlashini so'rang va unga kerakli ma'lumotlarni chop eting.
    # • Foydalanuvchiga sayohat uchun 5 ta shaharni tanlash imkoniyatini bering. Tanlangan shaharlar asosida jami narxni hisoblang va sayohat rejasini chop eting.


class Tour():
    def __init__(self, turist):
        self.turist = turist

    def book_tour(self):
        tour_type = input('Choose tour(1/internal, 2/external, 3/kreyser):\n>>>')
        if tour_type == '1':
            return f"Your tour internal and 500$"
        elif tour_type == '2':
            return f"Your tour external and 1000$"
        elif tour_type == '3':
            return f"Your tour kreyser and don't know cost"
        else:
            return f"Error"

    def choose_city(self):
        cities = []
        cost = 0
        n = 0
        while 1:
            city = input("Choose city(Tashkent, Dubai, London, Berlin, Pekin), exit:\n>>>")
            if city == 'tashkent':
                cities.append(city)
                cost += 300
            elif city.lower() == 'dubai':
                cities.append(city)
                cost += 1000
            elif city.lower() == 'london':
                cities.append(city)
                cost += 40000
            elif city.lower() == 'berlin':
                cities.append(city)
                cost += 10000
            elif city.lower() == 'pekin':
                cities.append(city)
                cost += 5000
            elif city.lower() == 'exit':
                break
            else:
                print("Wrong city")
        return f"Your tour cost: {cost} $ \n You will go {', '.join(cities).title()}"


#eleventh task
# 11. To’plamlar bilan ishlash (set, list, for, if)
#     • Foydalanuvchidan 10 ta raqam kiriting va ularni setga joylashtiring, unikal raqamlarni chop eting.
#     • Ikkita turli setdagi raqamlarni kiriting va ular orasidagi umumiy raqamlarni chop eting.


class Setnum():
    def __init__(self, name):
        self.name = name
    def unique(self, numbers):
        set_list = set(numbers)
        for number in set_list:
            numbers.remove(number)
        for number in numbers:
            if number in set_list:
                set_list.remove(number)
            else:
                pass
        return set_list
    def joint(self, firstSet, secondSet):
        return firstSet.intersection(secondSet)



#twelveth task
# 12. O'yin dasturi (input, if, while, random)
#     • Foydalanuvchidan 1 dan 100 gacha raqam topish o'yinini taklif eting. Kompyuter tasodifiy raqam tanlasin va foydalanuvchi to'g'ri topguncha urinishlarni davom etsin. Foydalanuvchi har safar noto'g'ri topganda, "katta" yoki "kichik" xabarini ko'rsating.
#     • Foydalanuvchidan 5 ta har xil raqam kiriting va ushbu raqamlar orasidan eng kattasini chop eting.

from random import randint
class Game():
    def computer_guess(self, y):
        """Computer thinks of a number"""
        input(f"Let's play a guessing game!\nI have thought of a number between 1 and {y}.")
        x = randint(1, y)
        attempts = 1
        while True:
            guess = int(input("Try to guess it:\n>>> "))
            if guess == x:
                print(f"Congratulations! I was thinking of the number {x}, and you guessed it in {attempts} attempts.")
                break
            elif guess > x:
                attempts += 1
                print("No, the number I am thinking of is smaller.")
            elif guess < x:
                attempts += 1
                print("No, the number I am thinking of is larger.")
        return attempts

    def check(self, a, b, c, x, y):
        return max(a,b,c,x,y)


#thirteenth task
# 13. Funksiya bilan ishlash (def, input, if, list)
#     • 2 ta sonni qabul qilib, ularning yig'indisini qaytaruvchi funksiya yarating. Foydalanuvchidan sonlarni kiritishini so'rab, natijani chop eting.
#     • Foydalanuvchidan ismlar ro'yxatini qabul qiladigan funksiya yarating va barcha ismlarni bosh harfi katta harf bilan chop eting.


class Little:
    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        return a + b

    def get_name(self):
        names = []
        while 1:
            name = input('Enter the name:(exit)\n>>>')
            if name == 'exit':
                break
            else:
                names.append(name)
        return f"{' ,'.join(names).title()}"



#fourteenth task
# 14. Stringlar bilan ishlash (for, string, if)
#     • Foydalanuvchidan satr kiriting va har bir harfni alohida chiqarib bering.
#     • Foydalanuvchidan satr kiriting va undagi unli harflarni sanab chiqaring.

class Matn():
    def __init__(self, string):
        self.string =string

    def set_str(self):
        for letter in self.string:
            print(letter)

    def vowel_letter(self):
        n = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        for letter in self.string:
            if letter in vowels:
                n += 1
            else:
                pass
        return n

# fifteenth task
# 15. Matn tahlili (string, list, for)
#     • Foydalanuvchidan satr kiriting va unda nechta so'z borligini aniqlang.
#     • Foydalanuvchidan satr kiriting va eng uzun so'zni topib, chop eting.

class Text():
    def __init__(self, string):
        self.string = string.split(' ')

    def count_words(self):
        return len(self.string)

    def max_word(self):
        num = []
        for text in self.string:
            num.append(len(text))
        max_num = max(num)
        ind = num.index(max_num)
        return self.string[ind]