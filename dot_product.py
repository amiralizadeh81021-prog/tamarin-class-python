# dot_product.py
# محاسبه ضرب نقطه‌ای دو بردار

x = [0.30, 0.60, 0.10]
y = [0.50, 0.10, 0.40]

total = 0.0
n = len(x)

for i in range(n):
    total += x[i] * y[i]

print("ضرب نقطه‌ای x و y:", total)