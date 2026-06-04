
print("=== Тапсырма 1: Кері ретпен шығару ===")

text = input("Мәтін енгізіңіз: ")
print("Кері:", text[::-1])


# ТАПСЫРМА 2: Мәтіндегі сөздер санын анықтау

print("\n=== Тапсырма 2: Сөздер санын анықтау ===")

text = input("Мәтін енгізіңіз: ")
words = text.split()
print("Сөздер саны:", len(words))

# ТАПСЫРМА 3: Сөзді басқа сөзбен алмастыру

print("\n=== Тапсырма 3: Сөзді ауыстыру ===")

text = input("Мәтін енгізіңіз: ")
old_word = input("Ауыстырылатын сөз: ")
new_word = input("Жаңа сөз: ")
result = text.replace(old_word, new_word)
print("Нәтиже:", result)


# ТАПСЫРМА 4: Факториал (рекурсия)

print("\n=== Тапсырма 4: Факториал (рекурсия) ===")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("n мәнін енгізіңіз: "))
print(f"{n}! =", factorial(n))

# ТАПСЫРМА 5: Фибоначчи сандары (рекурсия)
print("\n=== Тапсырма 5: Фибоначчи (рекурсия) ===")


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("n мәнін енгізіңіз: "))
print(f"F({n}) =", fibonacci(n))
print("Тізбек:", [fibonacci(i) for i in range(n + 1)])


# ТАПСЫРМА 6: Мәтіндік файлдан оқу

print("\n=== Тапсырма 6: Файлдан оқу ===")


with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Сәлем, бұл бірінші жол.\n")
    f.write("Python тілінде файлмен жұмыс.\n")
    f.write("Үшінші жол осы.\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("Файл мазмұны:")
print(content)

# ТАПСЫРМА 7: Файлдағы жолдар және сөздер санын анықтау

print("\n=== Тапсырма 7: Жолдар және сөздер саны ===")

with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)

print("Жолдар саны:", line_count)
print("Сөздер саны:", word_count)


# ТАПСЫРМА 8: Файлдан оқып өңдеп, жаңа файлға жазу

print("\n=== Тапсырма 8: Файлды өңдеп жаңа файлға жазу ===")

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

processed = content.upper()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(processed)
    f.write(f"\n--- Сөздер саны: {len(content.split())} ---\n")

print("output.txt файлына жазылды!")
print("Мазмұны:")
print(processed)