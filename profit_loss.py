def profit_loss_function(forex): 
    """
    - This function will compute the difference in the net profit between each day.
    - This function will return PROFIT DEFICIT if the net profit value is lower than the previous day.
    - This function will also return the DAY and AMOUNT in SGD if it returns PROFIT DEFICIT.
    - Otherwise, this function will return NET PROFIT SURPLUS, where the net profit on each day is higher than the previous day.
    """
    from pathlib import Path
    #to import CSV
    import csv
    
    #to instantiate a file path to the current working directory and extend it to the respective CSV file.
    file_lu = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
    #to extend the file path to the final text file, where all the computed amounts will be contained in.
    summary = Path.cwd()/"summary_report.txt"

    ##create "read" object to read through file_lu.
    with file_lu.open(mode="r",encoding="UTF-8") as file:
        #instantiate a reader object.
        reader = csv.reader(file)
        #create 2 empty lists to store appended values for the day & profit and loss respectively.
        DAY = []
        PL = []
        #to skip the header.
        next(reader)
        for profits in reader:
            #to assign the day value to the variable of "day" and ensure that it is a float.
            day = float(profits[0])
            #to assign the profits and loss value to the variable of "pl" and ensure that it is a float.
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
                file.close()
        length += 1
    if length == 0:
        with summary.open(mode="a",encoding = "UTF-8",newline="") as file:
            statement2 = (f"\n[PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")       
            file.write(statement2) 
            file.close()
