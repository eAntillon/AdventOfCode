workflows, string_parts = open("./input/day19.txt", "r").read().split("\n\n")

import pprint

p = pprint.PrettyPrinter(indent=4)

workflows = workflows.split("\n")
string_parts = string_parts.split("\n")

rules = {}

for workflow in workflows:
    rule_id, rule = workflow.split("{")
    rules[rule_id] = rule[:-1].split(",")
    for rule in rules[rule_id]:
        r = {
            "param": 
        }
        if rule.find(">") != -1:
            rules[rule_id] = rule.strip()
            break


parts = []
for part in string_parts:
    part = part[1:-1].split(",")
    dict = {}
    for x in part:
        id, value = x.split("=")
        dict[id] = int(value)
    parts.append(dict)

p.pprint(rules)
p.pprint(parts)
    