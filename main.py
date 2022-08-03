from pathlib import Path
#to import CSV.
import csv

#to extend the file path to the final text file, where all the computed amounts will be contained in.
file_path = Path.cwd()/"summary_report.txt"
#to create the new file.
file_path.touch()

#to check if the file exists (for self-check)
print(file_path.exists())

#to import all the other python files as modules
import api, cash_on_hand, overheads, profit_loss
def main():
  """
  - This function would import all the other python files as modules.
  - This function acts as the coordinating program to execute each python file (the functions).
  """
  forex = api.api_function()
  overheads.overheads_function(forex)
  cash_on_hand.coh_function(forex)
  profit_loss.profit_loss_function(forex)
  
main()
