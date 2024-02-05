
family_of_flowers = input("Ваш цвет относится к семейству красных цветов? ")

if family_of_flowers == "Да" or family_of_flowers == "да":
    red_or_purple = input("Ваш цвет красный или фиолетовый? ")

    if red_or_purple == "Да" or red_or_purple == "да":
        is_it_red = input("Это красный? ")
        
        if is_it_red == "Да" or is_it_red ==  "да":
            print("Вы загадали красный цвет")
        elif is_it_red == "Нет" or is_it_red == "нет" :
            print("Вы загадали фиолетовый цвет")

    elif red_or_purple == "Нет" or red_or_purple == "нет" :
         print("Вы загадали розовый цвет")


elif family_of_flowers == "Нет" or family_of_flowers == "нет":
    white_or_black = input("Ваш цвет белый или черный? ")
     
    if white_or_black == "Да" or white_or_black == "да":
        is_it_white = input("Это белый? ")

        if is_it_white == "Да" or is_it_white ==  "да":
            print("Вы загадали белый цвет")
        elif is_it_white == "Нет" or is_it_white == "нет" :
            print("Вы загадали черный цвет")
    
    elif white_or_black == "Нет" or white_or_black == "нет" :
        print("Вы загадали серый цвет")



