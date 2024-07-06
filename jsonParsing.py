import json

courses = '{"name":"RahulShetty", "languages":["Java","Python"]}'

# Loads method parse json strings and returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
list_languages=dict_courses['languages']
print(type(list_languages))
print(list_languages[0])
print(dict_courses['languages'][0])


