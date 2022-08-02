def Overheads_functions(forex):
    """
    - This function will find the highest overhead category and its value.
    - This function will return the value in SGD after it is converted using the real-time exchange rate from the API call.
    """
    from pathlib import Path
    import re, csv

    #to instantiate a file path to the current working directory.
    file_jia = Path.cwd()/"project_group"
    file_lu = file_jia/"csv_reports"/"Overheads.csv"
    #to extend the file path to the final text file, where all the computed amounts will be contained in.
    fl_summary = file_jia/"summary_report.txt"
    #to state that highest overhead value is a float
    highestvalue = 0.00
    #to state that the category name is a string
    Category = ""
    with file_lu.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        #to skip the header.
        next(reader)
        for data in reader:
            if float(data[1]) > highestvalue:
                highestvalue = float(data[1])
                Category = data[0].upper()
                
                with fl_summary.open(mode = "w", encoding = "UTF-8", newline = "") as file:
                    Output = f"\n[HIGHEST OVERHEAD] {Category} : SGD{highestvalue:.2f}"
                    file.write(Output)
                    file.close()
    file.close()