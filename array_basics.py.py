# array_basics.py
# کار با آرایه‌ها در پایتون

import random

# 1. ایجاد آرایه با مقداردهی اولیه
a = [0.30, 0.60, 0.10]
print("آرایه a:", a)

# 2. ایجاد آرایه با اندازه مشخص و مقدار صفر
n = 5
b = [0.0] * n
print("آرایه b (صفر):", b)

# 3. ایجاد آرایه با مقادیر تصادفی
c = [random.random() for i in range(4)]
print("آرایه c (تصادفی):", c)

# 4. دسترسی و تغییر عناصر
a[1] = 0.99
print("آرایه a بعد از تغییر:", a)

# 5. حلقه زدن روی عناصر
print("عناصر a:")
for v in a:
    print(v)

# 6. محاسبه میانگین
total = sum(a)
avg = total / len(a)
print("میانگین a:", avg)

# 7. پیدا کردن بیشینه
maximum = max(a)
print("بیشینه a:", maximum)

# 8. معکوس‌سازی آرایه
a_reversed = a[::-1]
print("a معکوس:", a_reversed)

# 9. کپی کردن آرایه
copy_a = a[:]
print("کپی a:", copy_a)