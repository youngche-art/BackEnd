import json

# JSON 데이터를 불러옵니다.
with open('third.json', 'r') as f:
    data = json.load(f)

# "색" 필드를 수정하는 함수
def modify_color_field(item):
    field_name = "색"
    if field_name in item["fields"]:
        field_value = item["fields"][field_name]
        if isinstance(field_value, str):
            # 문자열을 리스트로 변환하여 ["검정", "빨강", "흰색"]와 같은 형태로 변환
            color_list = json.loads(field_value)
            item["fields"][field_name] = color_list
        else:
            print(f"Error: '{field_name}' value is not a string")
    else:
        print(f"Warning: '{field_name}' key not found")


# 수정된 데이터를 새로운 파일에 저장합니다.
with open('seven.json', 'w', encoding='UTF-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
