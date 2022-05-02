from requests import get

data = get('https://opentdb.com/api.php?amount=20').json()

qn_type = []
question_data = []
for i in data['results']:
    question_data.append(i)
    qn_type.append(i['type'])


