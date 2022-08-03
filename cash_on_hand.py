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
    summary = file_jia/"project_group"/"summary_report.txt"

    #create 2 variables to be referred to at any point of the function.
    increase = 0
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
            #to assign the length of the empty list to the variable of "length".
            length = len(coh)
        #to look through all the days in the CSV file, from the first day until the last day.
        while increase + 1 < length:
            #to assign the previous day value to the variable of "previous".
            previous = coh[increase][1]
            #to assign the current day value to the variable of "current".
            current = coh[increase + 1][1]
            #to ensure that the previous day value is a float and assign that to the vraiable of "PREVIOUS".
            PREVIOUS = float(previous)
            #to ensure that the current day value is a float and assign that to the variable of "CURRENT".
            CURRENT = float(current)
            #to make the scenerio of previous day value being more then current day value.
            scenario = PREVIOUS > CURRENT

            #if the scenario is met.
            if scenario:
                #deficit will be calculated by taking previous day value minus current day value.
                deficit = PREVIOUS - CURRENT
                #create "append" object to append data to the end of a line.
                with summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    #to assign the final output that will be displayed in the summary_report to the variable of 'Output' on a new line.
                    Output = (f"\n[CASH DEFICIT] DAY: {coh[increase + 1][0]}, AMOUNT: SGD {(deficit * forex):.2f}")
                    #to write the output to summary_output and convert them to uppercase.
                    file.write(Output)
                    #to close the file (summary_report).
                    file.close()
            #to add 1 to the index value and iterate until final value.
            increase += 1
        #if there is no deficit
        if deficit == 0:
            #create "append" object to append data to the end of a line.
            with summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                #to assign the final output that will be displayed in the summary_report to the variable of 'Output' on a new line.
                Output = (f"\n[CASH SURPLUS] cash on each day is higher than the previous day")
                #to write the output to summary_output and convert them to uppercase
                file.write(Output.upper())
                #to close the file (summary_report).
                file.close()
        #to close the file (file_lu).
        file.close()