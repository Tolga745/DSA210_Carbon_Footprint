import csv
from datetime import datetime
import os

# Constants
EMISSION_FACTOR = 2.31  # kg CO2 per liter of gasoline
DATA_FILE = "commute_data.csv"

def calculate_co2(fuel_consumption):
    return fuel_consumption * EMISSION_FACTOR

def calculate_fuel_used(distance_km, fuel_efficiency):
    # Fuel efficiency is in liters per 100 km
    return (distance_km * fuel_efficiency) / 100

def collect_daily_data():
    # Ask user for trip direction
    trip_direction = input("Enter trip direction (1 for Home to Campus, 2 for Campus to Home): ")
    if trip_direction == "1":
        direction_label = "Home to Campus"
    elif trip_direction == "2":
        direction_label = "Campus to Home"
    else:
        print("Invalid input. Please enter 1 or 2.")
        return
    
    # Collect user input for trip details
    trip_duration = input("Enter trip duration (minutes): ")
    distance_km = float(input("Enter distance traveled (km): "))
    fuel_efficiency = float(input("Enter your car's average fuel consumption (liters per 100 km): "))
    traffic_condition = input("Enter traffic condition (low/moderate/high): ").lower()
    
    # Calculate fuel used and CO2 emissions
    fuel_used = calculate_fuel_used(distance_km, fuel_efficiency)
    co2_emissions = calculate_co2(fuel_used)
    
    # Prepare data row
    data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "departure_time": datetime.now().strftime("%H:%M"),
        "trip_direction": direction_label,
        "trip_duration": trip_duration,
        "distance_km": distance_km,
        "fuel_efficiency_l_per_100km": fuel_efficiency,
        "fuel_used_l": fuel_used,
        "traffic_condition": traffic_condition,
        "day_of_week": datetime.now().strftime("%A"),
        "co2_emissions_kg": co2_emissions
    }
    
    # Save to CSV
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()  # Write header if file is new
        writer.writerow(data)
    
    print("Data saved successfully!")

if __name__ == "__main__":
    collect_daily_data()