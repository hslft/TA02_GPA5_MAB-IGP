def profitloss_function(forex):
  from pathlib import Path
  import re, csv
  file_path = Path.cwd()/"project_group"/"csv_reports"/"Profit_Loss.csv"
  fp_summary = Path.cwd()/"project_group"/"summary_report.txt"
  increase = 0
  lack = 0
  profitloss = []
  with file_path.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for value in reader:
      profitloss.append(value)
    length = len(profitloss)
    while increase + 1 < length:
      converted1 = float((profitloss[increase][4]))
      converted2 = float(profitloss[increase + 1][4])
      condition = converted1 > converted2
      if condition:
        lack = converted1 - converted2
        with fp_summary.open(mode="a",encoding="UTF-8",newline="") as file:
          message = f"\n[Profit Deficit] Day: {profitloss[increase + 1][0]}, AMOUNT: SGD{(lack):.2f}"