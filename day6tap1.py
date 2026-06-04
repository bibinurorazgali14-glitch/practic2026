print("=== ОЛИМПИАДАЛЫҚ ЕСЕПТЕРДІҢ ОРЫНДАЛУ НӘТИЖЕЛЕРІ ===\n")


# 1-ЕСЕП: Екі санның қосындысы (Арифметика)

print("1-Есеп: Екі санның қосындысын табу")
# Тесттік мәлімет: А = 25, B = 75
test_input_1 = "25 75"
print(f"Енгізілген мәлімет: {test_input_1}")

# Алгоритмнің орындалуы
a, b = map(int, test_input_1.split())
sum_result = a + b

print(f"Консольге шыққан жауап: {sum_result}")
print("-" * 50)



# 2-ЕСЕП: Жұп немесе тақ (Шартты оператор)

print("2-Есеп: Санның жұп немесе тақ екенін анықтау [cite: 13]")
# Тесттік мәлімет: N = 42
test_input_2 = 42
print(f"Енгізілген мәлімет: {test_input_2}")

# Алгоритмнің орындалуы
if test_input_2 % 2 == 0:
    odd_even_result = "EVEN"
else:
    odd_even_result = "ODD"

print(f"Консольге шыққан жауап: {odd_even_result}")
print("-" * 50)



# 3-ЕСЕП: Цифрлардың қосындысы (Циклдер)

print("3-Есеп: Санның цифрларының қосындысын табу [cite: 13]")
# Тесттік мәлімет: N = 2026
test_input_3 = "2026"
print(f"Енгізілген мәлімет: {test_input_3}")


sum_digits = 0
for digit in test_input_3:
    sum_digits += int(digit)

print(f"Консольге шыққан жауап: {sum_digits}")
print("-" * 50)



# 4-ЕСЕП: Үш санның ең үлкені (Логикалық іріктеу)

print("4-Есеп: Үш санның ішіндегі ең үлкенін анықтау [cite: 13]")
# Тесттік мәлімет: A = 15, B = 89, C = 47
test_input_4 = "15 89 47"
print(f"Енгізілген мәлімет: {test_input_4}")


numbers = list(map(int, test_input_4.split()))
max_result = max(numbers)

print(f"Консольге шыққан жауап: {max_result}")
print("-" * 50)


# 5-ЕСЕП: Сөзді аударып шығару

print("5-Есеп: Берілген сөзді кері айналдыру")
# Тесттік мәлімет: "ALGORITHMIC" сөзі
test_input_5 = "ALGORITHMIC"
print(f"Енгізілген мәлімет: {test_input_5}")


reversed_result = test_input_5[::-1]

print(f"Консольге шыққан жауап: {reversed_result}")
print("=" * 50)