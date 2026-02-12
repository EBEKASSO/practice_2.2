import psutil

print(f"Загрузка CPU за 1 сек: {psutil.cpu_percent(interval=1)}%")
print(f"Использование RAM: {psutil.virtual_memory().percent}%")
print(f"Процент использования диска: {psutil.disk_usage('/').percent}%")