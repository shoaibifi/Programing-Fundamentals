def func(number_of_class_held,number_of_classes_attend):
    percentage = (number_of_classes_attend *100)/number_of_class_held
    if percentage > 80:
        return print("You are allowed to sit in the exam")
    else :
        return print("You are not allowed")
