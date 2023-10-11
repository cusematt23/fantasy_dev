import json



with open('../CONTEST_DEFS.json') as f:
    data = json.load(f)

print(data['DRAFTKINGS']['NFL']['CLASSIC']['POSITION_MIN'])
print(data['DRAFTKINGS']['NFL']['CLASSIC']['POSITION_MAX'])







