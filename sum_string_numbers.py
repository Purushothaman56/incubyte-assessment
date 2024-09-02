def add(input_string: str = "") -> int:
    striped_input = input_string.strip()
    result = 0

    if not striped_input:
        return result
    
    input_array = striped_input.split("\n")
    for item in input_array:
        numbers = [int(i.strip()) for i in item.split(",") if i.strip().isdigit()]
        for num in numbers:
            result += num
    return result
