import  json 
def load_records():
    try:
        with open('records.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

from datetime import datetime

def add_record(weight, body_fat=None):
    records = load_records()  
    new_record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "weight": weight,
        "body_fat": body_fat
    }
    records.append(new_record)   
    with open("records.json", "w") as f:
        json.dump(records, f)

def show_summary(records):
    if len(records) == 0:
        print("No records found")
        return
    
    total = len(records)
    total_weight = 0
    max_weight = records[0]["weight"]  
    min_weight = records[0]["weight"]  
    
    for record in records:
        total_weight += record["weight"]
        if record["weight"] > max_weight:
            max_weight = record["weight"]
        if record["weight"] < min_weight:
            min_weight = record["weight"]
    
    avg_weight = total_weight / total

    print(f"Total records: {total}")
    print(f"Average weight: {avg_weight:.1f} kg")
    print(f"Max weight: {max_weight} kg")
    print(f"Min weight: {min_weight} kg")  
    print("Keep going! Every step counts.")
   
def main():
    while True:
        print("\n=== Health Tracker ===")
        print("1. Add record")
        print("2. View summary")
        print("3. Quit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            try:
                weight = float(input("Enter weight (kg): "))
                add_record(weight)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            records = load_records()
            show_summary(records)
        elif choice == "3":
            break
        else:
            print("Invalid option, try again")

main()