# categories.py
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Health", "Other"]


def show_categories():
    print("Available Categories:")
    for i in range(len(CATEGORIES)):
        print(i + 1, "-", CATEGORIES[i])


def is_valid_category(category):
    return category.title() in CATEGORIES
