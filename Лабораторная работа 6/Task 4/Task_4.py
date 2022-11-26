import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimeter = ',', new_line ='\n') -> list[dict]:
    with open(filename) as f:
        table = []
        for index, line in enumerate(f):
            fields = line.strip(new_line).split(delimeter)
            if index == 0:
                heads = fields
                continue
            table.append({})
            for i, _ in enumerate(heads):
                table[-1][heads[i]] = fields[i]
    return table


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
