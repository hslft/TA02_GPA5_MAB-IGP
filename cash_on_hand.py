def coh_function(forex):
    """
    """
    from pathlib import Path
    import re, csv
    file_jia = Path.cwd()/"project_group"
    file_lu = file_jia/"csv_reports"/"Cash on Hand.csv"

    fl_summary = file_jia/"project_group"/"summary_report.txt"

    increment = 0
    deficit = 0
    coh = []

    with file_lu.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for data in reader:
            coh.append(data)
            length = len(coh)
        while increment + 1 < length:
            previous = float((coh[increment][1]))
            current = float(coh[increment + 1][1])
            condition = previous > current

            if condition:
                deficit = previous - current
                with fl_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    Output = (f"\n[CASH DEFICIT] DAY: {coh[increment + 1][0]}, AMOUNT: SGD {(deficit * forex):.2f}")
                    file.write(Output)
                    file.close()
            increment += 1
        if deficit == 0:
            with fl_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                Output = (f"\n[CASH SURPLUS] cash on each day is higher than the previous day")
                file.write(Output.upper())
                file.close()
        file.close()