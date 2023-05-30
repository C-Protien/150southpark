

import csv
from datetime import datetime
import subprocess



# Open the input and output files
with open(r"C:\Users\91999\Downloads\IGF.csv", 'r') as input_file, open(r'C:\Users\91999\Downloads\output.csv', 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        # Write the header row to the output file
        header = next(csv_reader)
        csv_writer.writerow(header)

        # Initialize variables to store clubbed values
        last_value = None
        clubbed_values = []

        # Process each row
        for row in csv_reader:
            # If the value in the second column is the same as the last row, add it to the clubbed values
            if row[1] == last_value:
                clubbed_values.append(row)
            else:
                # If the clubbed values list is not empty, subtract the first value from the last value and write it to the output file
                if clubbed_values:
                    first_value = datetime.strptime(clubbed_values[0][0], '%Y-%m-%d %H:%M:%S')
                    last_value = datetime.strptime(clubbed_values[-1][0], '%Y-%m-%d %H:%M:%S')
                    time_diff = last_value - first_value
                    time_diff_str = str(time_diff.total_seconds())
                    csv_writer.writerow([time_diff_str] + clubbed_values[-1][1:])

                # Reset the clubbed values list and add the current row's value to it
                clubbed_values = [row]
                last_value = row[1]

        # Process the last clubbed values
        if clubbed_values:
            first_value = datetime.strptime(clubbed_values[0][0], '%Y-%m-%d %H:%M:%S')
            last_value = datetime.strptime(clubbed_values[-1][0], '%Y-%m-%d %H:%M:%S')
            time_diff = last_value - first_value
            time_diff_str = str(time_diff.total_seconds())
            csv_writer.writerow([time_diff_str] + clubbed_values[-1][1:])


with open(r"C:\Users\91999\Downloads\output.csv", 'r') as input_file, open(r'C:\Users\91999\Downloads\Final_output.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    header = next(csv_reader)
    header.append('Cycle Time (min)')  # add new column header
    csv_writer.writerow(header)

    sequence = 1
    cycle_times = []
    clubbed_values = []
    for row in csv_reader:
        clubbed_values.append(row)
        if len(clubbed_values) == 3:

            cycle_time = float(clubbed_values[0][0]) +float(clubbed_values[1][0]) + float(clubbed_values[2][0])
            cycle_time = float(cycle_time)/60
            cycle_times.append(cycle_time)
            clubbed_values = []

            row.append("Cycle Time {}".format(sequence) )
            sequence += 1
            row.append(cycle_time)
            csv_writer.writerow(row)


            # print(cycle_time)
        else:
            continue