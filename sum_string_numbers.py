def add(input_string: str = "") -> int:
    striped_input = input_string.strip()
    result = 0
    delimeter = ","

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
            int(i.strip()) for i in item.split(delimeter) if i.strip().isdigit()
        ]
        for num in numbers:
            result += num
    return result
