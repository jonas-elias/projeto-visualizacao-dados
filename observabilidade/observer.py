import psycopg2
import psutil
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
    cursor.execute(f"INSERT INTO cpu_usage (uso_cpu, data) VALUES ('{cpu_stats}', CURRENT_TIMESTAMP)")
    conn.commit()
    print(Fore.GREEN + "Inserido com sucesso!")
