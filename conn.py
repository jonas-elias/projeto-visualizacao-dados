import psycopg2
import psutil
import json
from colorama import Fore

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='user',
    password='password',
    options="-c search_path=observabilidade"
)
cursor = conn.cursor()

while True:
    cpu_stats = psutil.cpu_percent(interval=1, percpu=False)
    cpu_usage_json = json.dumps(cpu_stats)
    cursor.execute(f"INSERT INTO cpu_usage (uso_cpu, data) VALUES ('{cpu_usage_json}', CURRENT_TIMESTAMP)")
    conn.commit()
    print(Fore.GREEN + "Inserido com sucesso!")
