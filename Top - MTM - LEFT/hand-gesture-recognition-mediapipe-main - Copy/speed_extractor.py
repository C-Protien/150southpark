

import csv
import time

import pandas as pd
import math
# Open the CSV file
Count = 0
with open('Heatmap.csv', 'r') as file:

    reader = csv.reader(file)
    #Converting to List
    rows = [row for row in reader]

    #resetting Pointer to zero
    file.seek(0)

    #Counting number of rows
    for row in reader:
        if any(row):
            Count += 1
#     print(Count)
# print(rows)


#Calculating Time Difference
rows[0].append('Time Difference')
for i in range(1,Count-1):
    # Subtract 2 from the value in the third column, second row
    rows[i+1].append(str(float(rows[i+1][2]) -float(rows[i][2])))

#Distance_Travelled
rows[0].append('Distance Travelled (inch)')
for i in range (1,Count-1):
    x_differ = float(rows[i+1][0])-float(rows[i][0])
    y_differ = float(rows[i + 1][1]) - float(rows[i][1])
    pix_dis = math.sqrt(x_differ**2 + y_differ**2)
    real_distance = pix_dis * 0.580110497#inches
    rows[i+1].append(str(real_distance))

df = pd.DataFrame(rows)
#
# # Add the modified column to the DataFrame
# # df[3] = df[2]
#
# # Save the DataFrame to a new CSV file
df.to_csv('Time_Difference_Extractor.csv', index=False, header=False)

time.sleep(1)
#Totals
# Open the CSV file
with open('Time_Difference_Extractor.csv') as csv_file:
    reader = csv.reader(csv_file)
    rows = [row for row in reader]

    csv_file.seek(0)
    # Skip the header row
    header = next(reader)
    header = next(reader)

    # Define the column to sum
    time_column = 3
    real_distance_column = 4

    # Sum the values in the column
    time_total = sum(float(row[time_column]) for row in reader)



    csv_file.seek(0)
    header = next(reader)
    header = next(reader)
    distance_total = sum(float(row[real_distance_column]) for row in reader)

#appending heads
rows[0].append('Total Time')
rows[0].append('Total Distance (foot)')
rows[0].append('Total Distance (m)')
rows[0].append('Speed (feet/sec)')
rows[0].append('Speed (m/sec)')

#appending data
rows[1].append(str(time_total))
rows[1].append(str(distance_total*0.0833333))
rows[1].append(str(distance_total*0.0254))
rows[1].append(str(float(distance_total*0.0833333/time_total)))
rows[1].append(str(float((distance_total*0.0254/time_total))))


df = pd.DataFrame(rows)


# Save the DataFrame to a new CSV file
df.to_csv('Time_Difference_Extractor.csv', index=False, header=False)

