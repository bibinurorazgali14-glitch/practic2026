import json
import os
from datetime import datetime, timedelta

# Деректер файлы
DATA_FILE = "kitaphana_data.json"


# ─────────────────────────────────────────
#  Деректерді жүктеу / сақтау
# ─────────────────────────────────────────

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"books": [], "next_id": 1}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─────────────────────────────────────────
#  Кітаптарды басқару функциялары
# ─────────────────────────────────────────

def add_book(data):
    """Жаңа кітап қосу"""
    print("\n─── Кітап қосу ───")
    title = input("Кітап атауы  : ").strip()
    author = input("Автор        : ").strip()
    genre = input("Жанр         : ").strip()
    year = input("Жыл          : ").strip()

    if not title or not author:
        print("❌ Атауы мен авторы міндетті!")
        return

    book = {
        "id": data["next_id"],
        "title": title,
        "author": author,
        "genre": genre or "—",
        "year": year or "—",
        "status": "available",
        "reader": None,
        "due": None,
    }
    data["books"].append(book)
    data["next_id"] += 1
    save_data(data)
    print(f"✅ «{title}» кітабы тіркелді.")


def list_books(data, filter_status="all", search=""):
    """Кітаптар тізімін шығару"""
    books = data["books"]

    if search:
        q = search.lower()
        books = [b for b in books if q in b["title"].lower() or q in b["author"].lower()]

    if filter_status == "available":
        books = [b for b in books if b["status"] == "available"]
    elif filter_status == "borrowed":
        books = [b for b in books if b["status"] == "borrowed"]

    if not books:
        print("\n📭 Кітап табылмады.")
        return

    print(f"\n{'№':<4} {'Атауы':<25} {'Автор':<20} {'Жанр':<12} {'Жыл':<6} {'Күй':<12} {'Оқырман / Мерзім'}")
    print("─" * 100)
    for b in books:
        status_label = "✅ Қолжетімді" if b["status"] == "available" else "📤 Берілген"
        reader_info = f"{b['reader']} ({b['due']} дейін)" if b["reader"] else ""
        print(
            f"{b['id']:<4} {b['title']:<25} {b['author']:<20} {b['genre']:<12} {b['year']:<6} {status_label:<14} {reader_info}")


def search_books(data):
    """Кітап іздеу"""
    print("\n─── Іздеу ───")
    query = input("Атауы немесе авторы: ").strip()
    list_books(data, search=query)


def borrow_book(data):
    """Кітапты оқырманға беру"""
    print("\n─── Кітапты беру ───")
    list_books(data, filter_status="available")

    try:
        book_id = int(input("\nКітап нөмірін енгізіңіз: "))
    except ValueError:
        print("❌ Қате нөмір.")
        return

    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        print("❌ Кітап табылмады.")
        return
    if book["status"] == "borrowed":
        print(f"❌ Бұл кітап қазір «{book['reader']}» оқырманында.")
        return

    reader = input("Оқырман аты-жөні : ").strip()
    days = input("Неше күнге? (әдепкі 14) : ").strip()
    days = int(days) if days.isdigit() else 14

    due = (datetime.today() + timedelta(days=days)).strftime("%Y-%m-%d")
    book["status"] = "borrowed"
    book["reader"] = reader
    book["due"] = due
    save_data(data)
    print(f"✅ «{book['title']}» кітабы {reader} оқырманына {due} мерзіміне дейін берілді.")


def return_book(data):
    """Кітапты қайтару"""
    print("\n─── Кітапты қайтару ───")
    list_books(data, filter_status="borrowed")

    try:
        book_id = int(input("\nКітап нөмірін енгізіңіз: "))
    except ValueError:
        print("❌ Қате нөмір.")
        return

    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        print("❌ Кітап табылмады.")
        return
    if book["status"] == "available":
        print("ℹ️ Бұл кітап қазір кітапханада.")
        return

    print(f"✅ «{book['title']}» кітабы {book['reader']} оқырманынан қайтарылды.")
    book["status"] = "available"
    book["reader"] = None
    book["due"] = None
    save_data(data)


def delete_book(data):
    """Кітапты жою"""
    print("\n─── Кітапты жою ───")
    list_books(data)

    try:
        book_id = int(input("\nЖою үшін кітап нөмірін енгізіңіз: "))
    except ValueError:
        print("❌ Қате нөмір.")
        return

    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        print("❌ Кітап табылмады.")
        return

    confirm = input(f"«{book['title']}» кітабын жоясыз ба? (иә/жоқ): ").strip().lower()
    if confirm == "иә":
        data["books"].remove(book)
        save_data(data)
        print("✅ Кітап жойылды.")
    else:
        print("Болдырмалды.")


def show_stats(data):
    """Статистика"""
    books = data["books"]
    total = len(books)
    borrowed = sum(1 for b in books if b["status"] == "borrowed")
    available = total - borrowed

    print("\n─── Статистика ───")
    print(f"  Барлық кітап  : {total}")
    print(f"  Қолжетімді    : {available}")
    print(f"  Берілген       : {borrowed}")

    overdue = [b for b in books if
               b["status"] == "borrowed" and b["due"] and b["due"] < datetime.today().strftime("%Y-%m-%d")]
    if overdue:
        print(f"\n⚠️  Мерзімі өткен кітаптар ({len(overdue)}):")
        for b in overdue:
            print(f"   • {b['title']} — {b['reader']} ({b['due']} мерзімі өтті)")


# ─────────────────────────────────────────
#  Басты мәзір
# ─────────────────────────────────────────

def main():
    data = load_data()

    menu = {
        "1": ("Барлық кітаптар тізімі", lambda: list_books(data)),
        "2": ("Кітап іздеу", lambda: search_books(data)),
        "3": ("Кітап қосу", lambda: add_book(data)),
        "4": ("Кітапты беру", lambda: borrow_book(data)),
        "5": ("Кітапты қайтару", lambda: return_book(data)),
        "6": ("Кітапты жою", lambda: delete_book(data)),
        "7": ("Статистика", lambda: show_stats(data)),
        "0": ("Шығу", None),
    }

    print("=" * 40)
    print("   📚 КІТАПХАНА БАСҚАРУ ЖҮЙЕСІ")
    print("=" * 40)

    while True:
        print("\nМӘЗІР:")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("\nТаңдаңыз: ").strip()

        if choice == "0":
            print("Сау болыңыз! 👋")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("❌ Қате таңдау, қайталаңыз.")


if __name__ == "__main__":
    main()