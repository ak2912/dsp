import csv
with open('emails.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in df[' email']:
        writer.writerow([val])
