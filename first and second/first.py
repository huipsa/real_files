cook_book = {}
with open("recipes.txt", "r", encoding="utf-8") as lines:
    last_key = ""
    for line in lines:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and "|" not in line:
            cook_book[line] = []
            last_key = line
        elif line and "|" in line:
             name, qt, msure = line.split(" | ")
             cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))
             