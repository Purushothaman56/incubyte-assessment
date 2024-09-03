def add(input_str: str) -> int:
    result = 0
    delimeters = [","]
    negatives = []

    if not input_str.strip():
        return result

    if "\n" not in input_str:
        numbers_str = input_str
    else:
        delimeter_str, numbers_str = input_str.split("\n")
        if "//" in delimeter_str:
            while "[" in delimeter_str and "]" in delimeter_str:
                delimeter = delimeter_str[delimeter_str.find("[")+1:delimeter_str.find("]")]
                delimeters.append(delimeter)
                delimeter_str = delimeter_str[delimeter_str.find("]")+1:]
            else:
                delimeter = delimeter_str.strip()
                if delimeter:
                    delimeter = delimeter.replace("/", "")
                    delimeters.append(delimeter)
        else:
            numbers_str = delimeter_str + " " + numbers_str

    delimeters = delimeters[1:] if len(delimeters) > 1 else delimeters
    for delimeter in delimeters:
        numbers_str = numbers_str.replace(delimeter, " ")

    numbers = []
    for item in numbers_str.split():
        if item.strip():
            try:
                numbers.append(int(item.strip()))
            except ValueError as e:
                raise ValueError(
                    f"Invalid input format: {input_str}"
                    f"Error detail: {e}"
                )

    for num in numbers:
        if num < 0:
            negatives.append(num)
        elif num <= 1000:
            result += num

    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    return result
