def overheads_functions(forex):
    """
    """
    from pathlib import Path
    import re, csv

    file_home = Path.cwd()/"project_group"
    file_path = file_home/"csv_reports"/"Overheads.csv"
    print(file_path.exists())