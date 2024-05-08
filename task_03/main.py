from functions import parse_log_line, load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts 
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_03/main.py <path_to_log_file> [log_level]")
        return
    
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    
    if len(sys.argv) > 2:
        log_level = sys.argv[2]
        logs = load_logs(log_file_path)
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nDetails of logs for level '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")



if __name__ == "__main__":
    main()
    