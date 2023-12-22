workflows, string_parts = open("./input/day19.txt", "r").read().split("\n\n")

workflows = workflows.split("\n")
string_parts = string_parts.split("\n")

rules = {}

for workflow in workflows:
    rule_id, rules_arr = workflow.split("{")
    rules_arr = rules_arr[:-1].split(",")

    formated_rule = {"rules": []}
    for r in rules_arr:
        if r.find(":") != -1:
            apply, result = r.split(":")
            if apply.find(">") != -1:
                pr, v = apply.split(">")
                formated_rule["rules"].append(
                    {
                        "type": ">",
                        "value": int(v.strip()),
                        "param": pr,
                        "output": result,
                    }
                )
            elif apply.find("<") != -1:
                pr, v = apply.split("<")
                formated_rule["rules"].append(
                    {
                        "type": "<",
                        "value": int(v.strip()),
                        "param": pr,
                        "output": result,
                    }
                )

        else:
            formated_rule["output"] = r.strip()
    rules[rule_id.strip()] = formated_rule


parts = []
for part in string_parts:
    part = part[1:-1].split(",")
    dict = {}
    for x in part:
        id, value = x.split("=")
        dict[id] = int(value)
    parts.append(dict)


def check_rule(current_rules, parts_to_eval):
    for r in current_rules["rules"]:
        if r["param"] in parts_to_eval:
            if r["type"] == ">":
                if parts_to_eval[r["param"]] > r["value"]:
                    if r["output"] in rules:
                        return check_rule(rules[r["output"]], parts_to_eval)
                    else:
                        return r["output"]
            elif r["type"] == "<":
                if parts_to_eval[r["param"]] < r["value"]:
                    if r["output"] in rules:
                        return check_rule(rules[r["output"]], parts_to_eval)
                    else:
                        return r["output"]
    if current_rules["output"] in rules:
        return check_rule(rules[current_rules["output"]], parts_to_eval)
    return current_rules["output"]


accepted = []

for part in parts:
    state = check_rule(rules["in"], part)
    if state == "A":
        accepted.append(part)


acc = 0
for i in accepted:
    total = 0
    for k, v in i.items():
        total += v
    acc += total

print("Part 1: ", acc)

