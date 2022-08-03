def coh_function(forex):
    """
    - This function will compute the difference in cash on hand between each day.
    - This function will return CASH DEFICIT if the cash on hand value is lower than the previous day.
    - This function will also return the DAY and AMOUNT in SGD if it returns CASH DEFICIT.
    - Otherwise, this function will return CASH SURPLUS, where the cash on each day is higher than the previous day.
    """
    from pathlib import Path
    #imports regular expression and CSV.
    import re, csv

    #to instantiate a file path to the current working directory.
    file_jia = Path.cwd()/"project_group"
    file_lu = file_jia/"csv_reports"/"Cash on Hand.csv"
    #to extend the file path to the final text file, where all the computed amounts will be contained in.
    fl_summary = file_jia/"project_group"/"summary_report.txt"

    increment = 0
    deficit = 0
    #to create an empty list to store appended values.
    coh = []

    #create "read" object to read through files in file_lu.
    with file_lu.open(mode = "r", encoding = "UTF-8") as file:
        #to instantiate a reader object.
        reader = csv.reader(file)
        #to skip the header.
        next(reader)
        for data in reader:
            coh.append(data)
            length = len(coh)
        while increment + 1 < length:
            previous = float((coh[increment][1]))
            current = float(coh[increment + 1][1])
            scenario = previous > current

            #if the scenario is met
            if scenario:
                #deficit will be calculated by taking previous day value minus current day value
                deficit = previous - current
                #create "append" object to append data to the end of a line.
                with fl_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    #to assign the final output that will be displayed in the summary_report to the variable of 'Output' on a new line.
                    Output = (f"\n[CASH DEFICIT] DAY: {coh[increment + 1][0]}, AMOUNT: SGD {(deficit * forex):.2f}")
                    #to write the output to summary_output and convert them to uppercase.
                    file.write(Output)
                    #to close the file
                    file.close()
            #
            increment += 1
        #if there is no deficit
        if deficit == 0:
            #create "append" object to append data to the end of a line.
            with fl_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                #to assign the final output that will be displayed in the summary_report to the variable of 'Output' on a new line.
                Output = (f"\n[CASH SURPLUS] cash on each day is higher than the previous day")
                #to write the output to summary_output and convert them to uppercase
                file.write(Output.upper())
                #to close the file
                file.close()
        file.close()