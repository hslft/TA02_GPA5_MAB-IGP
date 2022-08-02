from pathlib import Path
import csv
house = Path.home()
file_path = house/"project_group"/"summary_report.txt"
file_path.touch()
print(file_path)
print(file_path.exists())