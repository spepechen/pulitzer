import csv
import re

winners = list(csv.DictReader(open("split_process.csv", 'rU')))


def stack(rows, col_name):
  stacked = []
  regex = re.compile(col_name + ' \d+')
  key_columns = [key for key in rows[0].keys() if regex.match(key)]
  # key_columns is now 'name 1', 'name 2', 'name 3', etc
  for winner in winners:
    # Get all the names out
    names = [winner[key] for key in key_columns if winner[key]]
    # Remove all of the name columns
    for key in key_columns:
      winner.pop(key, None)
    for name in names:
      new_winner = {}
      for key in winner:
        new_winner[key] = winner[key]
      new_winner['name'] = name.strip()
      stacked.append(new_winner)
    # for key in key_columns:
    #   if winner[key]:
    #     stacked.push(winner)
  return stacked
  
stacked = stack(winners, 'name')

with open('split_process-stacked.csv', 'w') as csvfile:
    fieldnames = ['category', 'publication', 'name', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()
    for row in stacked:
      writer.writerow(row)