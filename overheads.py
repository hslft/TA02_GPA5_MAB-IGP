
def overheads_function(forex):
    """
    - This function will find the highest overhead category and its value.
    - This function will return the value in SGD after it is converted using the real-time exchange rate from the API call.
    """
    from pathlib import Path
    #to import CSV.
    import csv

    #to instantiate a file path to the current working directory.
    file_jia = Path.cwd()
    file_lu = file_jia/"csv_reports"/"Overheads.csv"
    #to extend the file path to the final text file, where all the computed amounts will be contained in.
    fl_summary = file_jia/"summary_report.txt"

    #create "read" object to read through file_lu.
    with file_lu.open(mode = "r", encoding = "UTF-8") as file:
        #instantiate a reader object.
        reader = csv.reader(file)
        #to skip the header.
        next(reader)
        #to create a variable of "highestvalue"
        highestvalue = 0
        for data in reader:
            #to ensure that the data is a float and assign it to the variable of "DATA".
            DATA = float(data[1])
            #to make the scenario of overheads value being more than 0.00 (highestvalue).
            scenario = DATA > highestvalue
            #if the scenario is met
            if scenario:
                #to assign the overheads value to the variable of 'highestvalue'.
                highestvalue = DATA
                #to assign the category data to the variable of 'Category' and convert them to uppercase.
                Category = data[0].upper()
                #create "append" object and include newline to append data to the end of a line
                with fl_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    #to assign the final output that will be displayed in the summary_report to the variable of 'Output' on a new line.
                    Output = (f"\n[HIGHEST OVERHEAD] {Category} : SGD{highestvalue * forex:.2f}")
                    #to write the output to summary_report.
                    file.write(Output)
                    #to close the file (summary_report).
                    file.close()
    #to close the file (file_lu).
    file.close()
