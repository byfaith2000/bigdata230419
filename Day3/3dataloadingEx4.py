import json
import pandas as pd

obj = """
{"name":"Wes",
 "places_lived":["United States", "Spain", "Germany"],
 "pet": null,
 "siblings":[{"name":"Scott", "age":25, "pet":"Zuko"},
             {"name":"Katie", "age":33, "pet":"Cisco"}]
}
"""

data = json.loads(obj)  # Json.loads()을 이용하여 json 문자열을 파이썬 형태로 변환할 수 있다.
print(data)
print(type(data))
print()

frame = pd.DataFrame(data['siblings'])
print(frame)