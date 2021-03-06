# This script prompts user for travel data, calculates the compensations per employee per month and writes the
# conclusions to an output file.
#
# Usage:
#     python3 ./travel_compensation.py
#
# Author:
#     Pepijn Clarijs - 29-03-2022


import csv
import os
from datetime import timedelta, date
from pathlib import Path

COMPENSATIONS = {'Bike_short': 0.50,
                 'Bike_far': 1.00,
                 'Bus': 0.25,
                 'Train': 0.25,
                 'Car': 0.10}

NUM_WEEKS_IN_MONTH = 4.5


def find_first_monday(year, month):
    """Finds the date of the first monday of the given month in the given year.

    Args:
        year (int): The year of interest.
        month (int): The month of interest.

    Returns:
            date: The date of the first monday of the given month in the given year.
    """

    d = date(year, month, 7)
    offset = -d.weekday()
    return d + timedelta(offset)


def calc_travel_comp(travel_data_path, save_dir):
    """Calculates the travel compensation given a csv containing employee, transport, distance (km/one way), workdays
    per week, and saves an overview for the compensation for each employee in a csv.

    Args:
        travel_data_path (string): path to CSV file containing travel information: employee, transport,
            distance (km/one way), workdays per week.
        save_dir (string): The path of the directory in which to save the output csv file. This directory must exist
            already.
    """

    # Check if file and destination directory exist.
    tdp = Path(travel_data_path)
    sd = Path(save_dir)
    assert tdp.is_file(), "Sorry, I could not find your file :(. Please check the path that you used as input."
    assert sd.is_dir(), f"The given directory, which is located here: {sd}, does not exist yet. Please create it " \
                        f"before using it in this function."

    # Open the given data file and calculate compensations.
    out_file = os.path.join(sd, "mock_output_travel_compensations.txt")  # TODO: outfile name
    with open(travel_data_path, 'r') as travel_data, open(out_file, 'w') as outf:
        csvreader = csv.reader(travel_data)
        header = next(csvreader)
        in_data = list(csvreader)
        assert len(header) == 4, "The format of the csv file is not as expected. Please check if it contains the " \
                                 "following columns: employee, transport, distance (km/one way), workdays per week."
        csvwriter = csv.writer(outf)

        # Loop over the input data and calculate the output data for each month.
        for month in range(1, 13):
            csvwriter.writerow([f'Month {month}'])
            csvwriter.writerow(['Employee', 'Transport', 'Traveled distance (km/month)', 'Compensation (euro\'s/month)',
                                'payment date'])
            for row in in_data:
                transport = row[1].strip()
                distance = int(row[2].strip())
                num_workdays_pw = float(row[3].strip())
                if transport == 'Bike' and int(distance) < 5:
                    comp_per_km = COMPENSATIONS['Bike_short']
                elif transport == 'Bike' and int(distance) > 5:
                    comp_per_km = COMPENSATIONS['Bike_far']
                else:
                    comp_per_km = COMPENSATIONS[transport]

                # Calculate distance and compensations.
                traveled_distance = distance * num_workdays_pw * NUM_WEEKS_IN_MONTH
                comp_per_month = round(comp_per_km * distance * num_workdays_pw * NUM_WEEKS_IN_MONTH, 2)

                # Find the right pay dates.
                pay_month = month + 1  # The payout is the first monday of the next month.
                pay_year = date.today().year
                if pay_month == 13:
                    pay_month = 1
                    pay_year += 1
                pay_date = find_first_monday(pay_year, pay_month)

                # Write results.
                csvwriter.writerow([row[0].strip(), transport, traveled_distance, comp_per_month, pay_date])

            csvwriter.writerow([])


if __name__ == '__main__':

    # Prompt user for travel data and calculate the compensations.
    in_path = input("Please enter the path to the file containing the travel data: ")
    out_dir = os.path.dirname(in_path)
    try:
        calc_travel_comp(in_path, out_dir)
        print(f"Travel compensations calculated successfully :). The result can be found in this directory: {out_dir}")
    except AssertionError as error:
        print(error)
        print('The travel compensation was not calculated :(.')


