def profit_loss_function(forex): 
    from pathlib import Path
    import re, csv
    
    file_lu = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
    summary = Path.cwd()/"summary_report.txt"

    with file_lu.open(mode="r",encoding="UTF-8") as file:
        reader = csv.reader(file)
        DAY = []
        PL = []
        next(reader)
        for profits in reader:
            day = float(profits[0])
            pl = float(profits[4]) * forex
            DAY.append(day)
            PL.append(pl)
    length = 0
    for data in range(len(PL) - 1):
        lack = PL[data] - PL[data + 1]
        if lack > 0:
            with summary.open(mode="a",encoding = "UTF-8",newline="") as file:
                statement1 = (f"\n[PROFIT DEFICIT] DAY: {DAY[data + 1]}, AMOUNT: SGD{lack:.2f}")
                file.write(statement1)
            length += 0
    if length == 0:
        with summary.open(mode="a",encoding = "UTF-8",newline="") as file:
            statement2 = (f"\n[PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")       
            file.write(statement2) 
        
