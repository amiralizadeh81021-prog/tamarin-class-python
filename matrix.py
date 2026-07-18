def count_multiplications(n):
    multiplication_count = 0  # شمارنده ضرب‌ها

    # ساختار حلقه‌ها مشابه اسلاید
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # در این خط یک ضرب انجام می‌شود
                # c[i][j] += a[i][k] * b[k][j]
                multiplication_count += 1
                
    return multiplication_count

# تست برای مقادیر مختلف n
for n in [6, 7, 8, 9]:
    result = count_multiplications(n)
    print(f"For n = {n}: Scalar Multiplications = {result} (which is {n}^3)")

