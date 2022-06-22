# برای لوپ زدن در پایتون از این روش استفاده میکنیم
#
# print("start")
# for i in ["cat", "dog", "caw"]:
#     print("hi")
#     print(i)
#     print("-----")
# print("finish")
#
#
#
# برای اینکه بین اعداد را بگیریم از تک رنج استفاده میکنیم
#
# for nummber in range(1, 10):
#     print(nummber, nummber*nummber)
#
#
#
#
# توابع چیست؟
#
# def jam(x, y):
#     print(x + y)
#
#
# jam(2, 5)
# jam(5, 10)
# jam("ali", "10")
#
#
#
#
# اگر به 2 تا 7 به چیزی بخش پذیر بود یعنی اعداد اول نیست
#
# for n in range(2, 8):
#     if 8 % n == 0:
#        print("bekhater", n, "aval nist")
#
#
# اگر بخش پذیر نبود جواب کاملا مثبت
#
# n = 17
# bolian = True
# for i in range(2, n):
#     if n % i == 0:
#         bolian = False
#
# if bolian:
#     print("ok")
# else:
#     print("not is prime")
#
#
#
#
#
# همان تکنیک بالارو با فانگشن انجام میدیم
#
# datetime : این کد برای زمان اجرای برنامه مان به کار می آید
# int(**0.5)+1 , break : با این کد می توان برنامه را بهینه کرد
# from datetime import datetime
# start = datetime.now()
#
#
# def is_prime(n):
#     bolian = True
#     for i in range(2, n):
#         if n % i == 0:
#             print("check i", i)
#             print("check n", n)
#             print(n % i)
#             bolian = False
#     return bolian
#
#
# last_prime_number = 0
# prime_count = 0
# for i in range(1, 11):
#     if is_prime(i):
#         print(i)
#         prime_count = prime_count + 1
#         last_prime_number = i
#
# end = datetime.now()
# timing = end - start
# print("tedad adad mojod", prime_count)
# print(timing)
# print("finish prime", last_prime_number)
#
#
#
#
#
#
#
# euler project : مسئله اول سایت
#
# def euler3or5(n):
#     if n % 5 == 0 or n % 3 == 0:
#         return True
#
#
# prime_sum = 0
# for i in range(1, 10):
#     if euler3or5(i):
#         prime_sum = prime_sum + i
#
# print(prime_sum)
#
#
#
#
#
#
#
# euler project : مسئله دوم سایت
#
#
#
# def isEvent(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# sum = 0
# first = 1
# seccond = 2
# while (first < 4000000):
#     if isEvent(first):
#         sum = sum + first
#     new = first + seccond
#     first = seccond
#     seccond = new
#
# print(sum)
#
#
#
#
#
#
# آرایه ها ؟
#
# len : این تک برای تعداد گریی آرایه ها می باشد
# append : این تک برای اضاف کردن به آرایه می باشد
# count : این تک تعداد اونی که انتخاب شده را در آرایه می گیرد
# 1:4 : این تک فرمان می دهد که که از مقدار گفته شده
# تا مقدار تعین شده آن را اجرا کند

# a = ["ali", "jadi", "mmd", "mmd", "mania", "reza"]
# print(a.append("mania"))
# print(a)
# print(len(a))
# print(a.count("mania"))
# print(a[1:5])
# print(a[2:])
# print(a[:3])
#
#
#
#
#
#
#
#
#
# for VS while : در حلقه فور فرمان را تا زمانی که
# هر چند بار بهش دستور داده شده اجرا می کند
# ولی در حلقه وایل تا زمانی اجرا می کند که به جواب برسد
#
# حل مسئله رندوم پول دادن در اتاق
# import random
#
#
# otaq = []
# for i in range(0, 50):
#     otaq.append(50)
#
# for beshkan in range(0, 200):
#     for person1 in range(0, 50):
#
#         person2 = random.randrange(0, 50)
#         while otaq[person2] == 0:
#             person2 = random.randrange(0, 50)
#
#         if otaq[person1] != 0:
#             otaq[person1] -= 1
#             otaq[person2] += 1
# print(otaq)
# print(otaq.count(0))
#
#
#
#
#
#
#
#
# آشنایی با دیکشنری؟
#
#
# {} = این مفهوم برای دیکشنری میباشد
# tel[type: kilide] = type: value
# del = تک دل برای حذف هر متغیری به کار می آید
# .get = این متود برای گرفتن ولییو به کار می رود
# .keys = این متود کلید های دیکشنری را می گیرد
# klide in tel = bolian
# .items = این متود آیتم های دیکشنری را میگیرد
#
# اگر 2 مقدار در لوپ اضاف کنیم و در آخر آن متود آیتم بزاریم
# هم کلید و هم ولیو را جداگانه میگیرد
#
# tel = {}
#
# tel["mmd"] = "0939"
# tel["ali"] = "0903"
# tel["mania"] = "0912"
# tel["jadi"] = "003"
#
# del tel["ali"]
# print(tel)
#
# print(tel.get("mmd"))
# print(tel.get("fatemeh"))
#
# print(tel.keys())
#
# print("mmd" in tel)
# for i in tel.items():
#     print(i)
#
# for n, a in tel.items():
#     print(type(n))
#
#
#
#
#
#
#
#
#
#
# تمرین 1
#
# int = این تیجر دو خاصیت دارد یک اینکه استیرینگ را بر می دارد
# و دوم آنکه اعشار را بر میدارد
# zfill = این متود برای استرینگ به کار می آید و
# اجزای استرینگ را از هم جدا میکند
# str = این نوع فرمان هر چه که بهش داده می شود را تبدیل به استرینگ میکند
#
# def sum_ramz(ramz_digits):
#     sum_prime = 0
#     for i in ramz_digits:
#         sum_prime += ramz_digits[i]
#     return sum_prime
#
#
# def is_prime_ok(ramz_digits):
#     if ramz_digits["theri"] + ramz_digits["five"] == 14 and \
#         ramz_digits["one"] == ramz_digits["two"]*2 - 1 and \
#         ramz_digits["fore"] == ramz_digits["two"] + 1 and \
#             ramz_digits["two"] + ramz_digits["theri"] == 10:
#         if sum_ramz(ramz_digits) == 30:
#             return True
#
#
# for ramz in range(0, 100000):
#     this_prime = str(ramz).zfill(5)
#
#     ramz_digits = {}
#     ramz_digits["one"] = int(this_prime[0])
#     ramz_digits["two"] = int(this_prime[1])
#     ramz_digits["theri"] = int(this_prime[2])
#     ramz_digits["fore"] = int(this_prime[3])
#     ramz_digits["five"] = int(this_prime[4])
#     if is_prime_ok(ramz_digits):
#         print(ramz)
#
#
#
#
#
#
#
#
#
#
