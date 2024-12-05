input = open(r"day05\\input.txt", "r")
input = input.read().split('\n')

SUM_OF_MIDDLE_PAGE_NUMBERS_CORRECTLY_ORDERED = 0
SUM_OF_MIDDLE_PAGE_NUMBERS_INCORRECTLY_ORDERED = 0
RULES = []
UPDATES = []

# parse input
instructions_rules = True
for line in input:
    if line != '' and instructions_rules:
        RULES.append(line.split('|'))
    elif line != '' and not instructions_rules:
        UPDATES.append(line.split(','))
    else:
        instructions_rules = False

def get_relevant_rules(update):
    relevant_rules = []
    for page in update:
        for rule in RULES:
            if page in rule:
                relevant_rules.append(rule)
    return relevant_rules

def get_middle_item_of_list(update):
    return int(update[len(update)//2])

def reorder_update(update: list[str], relevant_rules: list[list[str]]):
    for rule in relevant_rules:
        # ignore rule if not both rule values are in the current update
        if rule[0] not in update or rule[1] not in update:
            continue
        # if rule is followed do nothing
        elif update.index(rule[0]) < update.index(rule[1]):
            continue
        # otherwise fix the rule by swapping the entries
        else:
            idx_x, idx_y = update.index(rule[0]), update.index(rule[1])
            if update[idx_y] == update[idx_x]:
                print(update[idx_y], update[idx_x])
            update[idx_y], update[idx_x] = update[idx_x], update[idx_y]     
    return update

# Work through all the updates
for update in UPDATES:
    # get relevant rules for each update
    relevant_rules = get_relevant_rules(update)
    rule_followed = True
    for rule in relevant_rules:
        # ignore rule if not both rule values are in the current update
        if rule[0] not in update or rule[1] not in update:
            continue
        # if rule is followed do nothing
        elif update.index(rule[0]) < update.index(rule[1]):
            pass
        # otherwise change flag and break
        else:
            rule_followed = False
            break
    if rule_followed:
        SUM_OF_MIDDLE_PAGE_NUMBERS_CORRECTLY_ORDERED += get_middle_item_of_list(update)
    else:
        # it only works if I do it a few times LMAO
        update = reorder_update(update, relevant_rules)
        update = reorder_update(update, relevant_rules)
        update = reorder_update(update, relevant_rules)

        SUM_OF_MIDDLE_PAGE_NUMBERS_INCORRECTLY_ORDERED += get_middle_item_of_list(update)

print("Sum of Middle Pages Numbers which are correctly ordered: (Star #1)")
print(SUM_OF_MIDDLE_PAGE_NUMBERS_CORRECTLY_ORDERED)

print("Sum of Middle Pages Numbers which are INcorrectly ordered: (Star #2)")
print(SUM_OF_MIDDLE_PAGE_NUMBERS_INCORRECTLY_ORDERED)