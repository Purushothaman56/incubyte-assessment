def add(input_str: str) -> int:
    result = 0
    delimeters = [","]
    negatives = []

    if not input_str.strip():
        return result

    if "\n" not in input_str or "//" not in input_str:
        numbers_str = input_str
    else:
        delimeter_str = input_str[input_str.find("//")+2:]
        numbers_str = input_str[:input_str.find("//")] + delimeter_str[delimeter_str.find("\n")+1:]
        delimeter_str = delimeter_str[:delimeter_str.find("\n")]
        while "[" in delimeter_str and "]" in delimeter_str:
            delimeter = delimeter_str[delimeter_str.find("[")+1:delimeter_str.find("]")]
            delimeters.append(delimeter)
            delimeter_str = delimeter_str[delimeter_str.find("]")+1:]
        else:
            delimeter = delimeter_str.strip()
            if delimeter:
                delimeter = delimeter.replace("/", "")
                delimeters.append(delimeter)

    delimeters = delimeters[1:] if len(delimeters) > 1 else delimeters
    for delimeter in delimeters:
        numbers_str = numbers_str.replace(delimeter, " ")

    for item in numbers_str.split():
        if item.strip():
            try:
                num = int(item.strip())
                if num < 0:
                    negatives.append(num)
                elif num <= 1000:
                    result += num
            except ValueError as e:
                raise ValueError(
                    f"Invalid input format: {input_str}"
                    f"Error detail: {e}"
                )

    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    return result
