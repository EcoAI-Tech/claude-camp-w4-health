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

def show_summary(records):
    if len(records) == 0:
        print("暂无记录")
        return
    
    total = len(records)
    total_weight = 0
    max_weight = records[0]["weight"]  # 先假设第一条最重
    min_weight = records[0]["weight"]  # 先假设第一条最轻
    
    for record in records:
        total_weight += record["weight"]
        if record["weight"] > max_weight:
            max_weight = record["weight"]
        if record["weight"] < min_weight:
            min_weight = record["weight"]
    
    avg_weight = total_weight / total

    print(f"总记录天数：{total}")
    print(f"平均体重：{avg_weight:.1f} kg")
    print(f"最重：{max_weight} kg")
    print(f"最轻：{min_weight} kg")  

add_record(70.5, 18.2)
add_record(69.8, 17.9)
add_record(71.2)
records = load_records()
show_summary(records)     