def add(input_string: str = "") -> int:
    striped_input = input_string.strip()
    result = 0
    delimeter = ","
    negatives = []

    if not striped_input:
        return result
    
    input_array = striped_input.split("\n")
    if delimeter not in input_array[0].strip() and not input_array[0].strip().isdigit():
        delimeter = input_array[0]
        delimeter = delimeter.replace("/", "")
        delimeter = delimeter.replace("[", "")
        delimeter = delimeter.replace("]", "")
        input_array = input_array[1:]

    for item in input_array:
        numbers = [
            int(i.strip()) for i in item.split(delimeter) if i.strip()
        ]
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
