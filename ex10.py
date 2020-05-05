tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
cat_food = "A large amount of cat food"
fishies = "Too many fishies"
catnip = "Lovely lovely catnip"
grass = "you gotta shit somewhere \n \tI need Grass"
fat_cat = """
I'll do a list:
\t* {}
\t* {}
\t* {}\n\t* {}
""".format(cat_food, fishies, catnip, grass)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
