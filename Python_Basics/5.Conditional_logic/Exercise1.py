is_magician = 1
is_expert = 1


if not(is_magician):
    print("You need magic powers")
elif is_magician and not is_expert:
    print("At least you're getting there")
else:
    print("You are a master magician")