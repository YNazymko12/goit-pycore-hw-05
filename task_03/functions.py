#Функція для парсингу рядків логу
def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]

    }

#Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading logs: {e}")
    
    return logs

#Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level']  == level.upper()]

#Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts    

#Функція, яка форматує та виводить результати
def display_log_counts(counts: dict):
    print("Log Level | Count")
    print("----------|------")
    for level, count in counts.items():
        print(f"{level.upper():<9} | {count}")