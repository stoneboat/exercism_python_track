def convert(number):

    Is_divisible_by_3 = (number % 3 == 0)
    Is_divisible_by_5 = (number % 5 == 0)
    Is_divisible_by_7 = (number % 7 == 0)

    if (not Is_divisible_by_3) and (not Is_divisible_by_5) and (not Is_divisible_by_7):
        return str(number)
    
    answer_list = []
    if Is_divisible_by_3:
        answer_list.append("Pling")
    if Is_divisible_by_5:
        answer_list.append("Plang")
    if Is_divisible_by_7:
        answer_list.append("Plong")
    
    return "".join(answer_list)
