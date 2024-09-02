def add(input_string: str = "") -> int:
    striped_input = input_string.strip()
    result = 0
    
    if not striped_input:
        return result
    
    numbers = [int(i.strip()) for i in striped_input.split(",") if i.strip().isdigit()]
    for num in numbers:
        result += num
    return result
