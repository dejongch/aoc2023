from operator import gt, lt
import re
from typing import Callable
from functools import cache

workflows: dict[str, Callable[[dict[str, int]], str]] = {}
parts: list[dict[str, int]] = []

operators = {
    ">": gt,
    "<": lt
}

check_regex = r"([xmas])([<>])(\d*):([a-zA-Z]+)"
workflow_regex = r"(.*){(.*)}"
def get_workflow_function(workflow_string: str)->Callable[[dict[str, int]], str]:
    work_flow_parts = workflow_string.split(",")
    checks_strings = work_flow_parts[:-1]
    else_destination = work_flow_parts[-1]
    checks = []
    for checks_string in checks_strings:
            part_cat, workflow_operator, workflow_value, destination = re.match(check_regex, checks_string).groups()
            workflow_value = int(workflow_value)
            def check(part, workflow_operator=workflow_operator, part_cat=part_cat, workflow_value=workflow_value):
                return operators[workflow_operator](part[part_cat], workflow_value)
            checks.append((check, destination))
    def perform_workflow(part: dict[str, int])-> str:        
        for check, destination in checks:
            if check(part):
                return destination
        return else_destination
    return perform_workflow

def parse_part(part_string: str)->dict[str, int]:
    x, m, a, s = [
        int(value[1]) for value in
            [value_string.split("=") for value_string in part_string[1:-1].split(",")]
    ]
    return {
        "x": x,
        "m": m,
        "a": a,
        "s": s
    }

        

with open("input.txt", 'r') as file:
    checking_workflows = True
    for line in file:
        line = line.strip()
        if not line:
            checking_workflows = False
        else:
            if checking_workflows:
                name, details = re.match(workflow_regex, line).groups()
                workflows[name] = get_workflow_function(details)
            else:
                parts.append(parse_part(line))


def validate_part(part: dict[str, int])->str:
    current_workflow = "in"
    
    while True:
        current_workflow = workflows[current_workflow](part)
        if current_workflow in ["A", "R"]:
            return current_workflow


def get_sum_of_accept_parts()->int:
    total = 0
    for part in parts:
        if validate_part(part) == "A":
            total+= sum(part.values())
    return total

print(get_sum_of_accept_parts())

        