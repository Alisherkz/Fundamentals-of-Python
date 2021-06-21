from sys import argv

script_name, job_time, mon_time, prize = argv
print(f"называние скрипта {script_name}")

result = (int(job_time) * int(mon_time)) + int(prize)
print(f"за месяц вы получаете: {result}")