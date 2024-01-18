from datetime import datetime

now = datetime.now()

print("Current datetime (before formatting):", now)

formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted datetime:", formatted_time)