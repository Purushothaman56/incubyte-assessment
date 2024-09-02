def add(input_string: str = "") -> int:
    striped_input = input_string.strip()
    result = 0
    delimeter_list = [","]
    negatives = []

    if not striped_input:
        return result
    
    input_array = striped_input.split("\n")
    if delimeter_list[0] not in input_array[0].strip() \
        and not all(i.isdigit() for i in input_array[0].strip()[1:]):
        delimeter_string = input_array[0]
        while "[" in delimeter_string and "]" in delimeter_string:
            delimeter = delimeter_string[:delimeter_string.find("]")+1]
            delimeter = delimeter.replace("/", "")
            delimeter = delimeter.replace("[", "")
            delimeter = delimeter.replace("]", "")
            delimeter_list.append(delimeter)
            delimeter_string = delimeter_string[delimeter_string.find("]")+1:]
        else:
            delimeter = delimeter_string.strip()
            delimeter = delimeter.replace("/", "")
            delimeter_list.append(delimeter) if delimeter else ""
        input_array = input_array[1:]

    for item in input_array:
        for delimeter in delimeter_list:
            item = item.replace(delimeter, " ")
        numbers = [int(i.strip()) for i in item.split() if i.strip()]
        for num in numbers:
            if num < 0:
                negatives.append(num)
            elif num > 1000:
                continue
            else:
                result += num

    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    return result
