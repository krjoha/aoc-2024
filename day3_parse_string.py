import re

def parse_math_expression(math_expression: str) -> int:
    multiply_matches = list(re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", math_expression))

    result = 0
    for multiply_match in multiply_matches:
        result += int(multiply_match.group(1)) * int(multiply_match.group(2))
    
    return result

if __name__ == "__main__":
    with open("data/day3.txt") as f:
        math_expression = "do()" + "".join(f.read().replace("\n", ""))
        clean_exp = ""
        for segment in math_expression.split("don't()"):
            clean_exp += segment[segment.find("do()"):]
        result = parse_math_expression(clean_exp)
        print(result)
