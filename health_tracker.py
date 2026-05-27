import  json 
def load_records():
    try:
        with open('records.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


from datetime import datetime

def add_record(weight, body_fat=None):
    records = load_records()  # 第4步已经帮你写好了
    new_record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "weight": weight,
        "body_fat": body_fat
    }
    records.append(new_record)   # 提示：列表加一个元素用什么方法？
    with open("records.json", "w") as f:
        json.dump(records, f)
      