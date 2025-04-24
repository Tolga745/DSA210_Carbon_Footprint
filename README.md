# Project: Analyzing the Impact of Departure Time and Traffic Conditions on Commute Carbon Footprint

## Project Idea
In this project, I will analyze how **departure time** and **traffic conditions** impact the **carbon footprint** of my daily commute between home and campus. My goal is to identify patterns and factors that contribute to higher emissions and suggest strategies to reduce my environmental impact. Traffic congestion, especially during rush hour, may significantly increase fuel consumption, leading to higher carbon emissions. By understanding these factors, I can make informed decisions to minimize my carbon footprint.


## Description of Dataset

1. **Fuel Consumption**:  
   - Tracked using a car app (e.g., Fuelio, Drivvo).  
   - Measured in liters per trip.

2. **Traffic Conditions**:  
   - Collected using GPS data from Google Maps.  
   - Metrics: average speed, congestion levels, and trip duration.

3. **Trip Time**:  
   - The exact time it took to get to the destination for each trip to analyze its effect on fuel consumption.

4. **Distance Traveled**:  
   - Recorded using GPS data from Google Maps or a car app.  
   - Measured in kilometers.

5. **Carbon Emissions**:  
   - Calculated using the formula:  
     **CO2 Emissions (kg) = Fuel Consumption (liters) × Emission Factor (kg CO2/liter)**.  
   - The emission factor for gasoline is approximately 2.31 kg CO2/liter.

---

## Plan

### Data Collection
- Data will be collected throughout March and April, maintaining:  
  - A **consistent route** between home and campus.  
  - The **same vehicle** and **driver** (myself).  
- **Sources**:  
  - **Fuel Consumption**: Tracked using a car app.  
  - **Traffic Conditions**: Collected using Google Maps.  
  - **Distance Traveled**: Recorded using GPS data from Google Maps or a car app.  
- To ensure consistency and minimize bias:  
  - Data will be recorded immediately after each trip.  
  - Data will be systematically organized in a spreadsheet or database.  

---

### Data Preparation and Analysis
1. **Data Cleaning**:  
   - Review data for completeness and consistency.  
   - Handle missing or inconsistent data (e.g., days when data collection failed).  

2. **Exploratory Data Analysis (EDA)**:  
   - Identify trends and patterns using statistical methods and visualization techniques.  
   - Examples:  
     - How does departure time affect fuel consumption and carbon emissions?  
     - How do traffic conditions (e.g., congestion levels) impact fuel efficiency and emissions?  
     - Are there differences in emissions between weekdays and weekends?  

3. **Regression Analysis**:  
   - Apply statistical methods to investigate the impact of factors such as:  
     - Departure time on fuel consumption and emissions.  
     - Traffic conditions on fuel efficiency.  

4. **Visualization**:  
   - Create visualizations to communicate findings effectively:  
     - **Line Charts**: Show carbon emissions over time.  
     - **Scatter Plots**: Explore relationships between traffic conditions and emissions.  
     - **Heatmaps**: Visualize how emissions vary by time of day and day of the week.  

# Report
## **Introduction**
The main objective of this project is to analyze the relationship between departure time, traffic conditions, fuel consumption, and travel duration for trips between home and campus. This study aims to determine how these factors, acting as both dependent and independent variables, influence fuel efficiency and carbon emissions. By identifying patterns in traffic congestion and its impact on travel time and fuel usage, the study will provide insights for optimizing departure schedules and route choices. The findings are expected to help reduce fuel consumption, minimize carbon footprint, and improve overall travel efficiency for commuters.

## **Hypothesis**
- Null Hypothesis (H₀): There is no significant relationship between traffic conditions and carbon footprint. Increased traffic congestion does not significantly affect the carbon emissions produced during the trip.

- Alternative Hypothesis (H₁): There is a significant relationship between traffic conditions and carbon footprint. Higher traffic congestion leads to increased carbon emissions due to prolonged idling and inefficient fuel consumption.

 ## **Data Analysis**
 ### **Data Collection** 
From March to April, data was collected using methods below:
- Travel Time and Length: Recorded from Google Maps (My Timeline), capturing the actual duration of each trip between home and campus.
- Traffic Conditions: Categorized based on Google Maps traffic data (e.g., low, moderate, heavy congestion) during the recorded trips.
- Fuel Consumption: Estimated using vehicle onboard diagnostics (OBD-II) data or fuel tracking apps (e.g., Fuelio, Drivvo) to log fuel usage per trip.
- Carbon Footprint: Calculated using standard emissions factors based on fuel consumption data and vehicle type (e.g., gasoline vs. diesel).

### **Dataset** 
- **Trip Direction**: Records whether the trip was from Home to Campus or Campus to Home, enabling analysis of potential directional differences in traffic patterns.

- **Traffic Condition**: Categorized as low, moderate, or high congestion based on real-time traffic data (e.g., Google Maps) to assess its impact on travel efficiency.

- **Travel Duration (minutes)**: Total time taken for each trip, extracted from Google Maps’ My Timeline, to analyze correlations with traffic and fuel efficiency.

- **Distance (km)**: The distance traveled for each trip, used to standardize fuel and emissions calculations.

- **Fuel Efficiency (L/100km)**: Vehicle-specific fuel consumption rate, critical for estimating fuel used and emissions.

- **Fuel Used (Liters)**: Calculated based on distance and fuel efficiency, providing a direct measure of fuel consumption per trip.

- **CO2 Emissions (kg)**: Derived from fuel consumption data using standard emissions factors, quantifying the environmental impact of each trip


### **Data Processing**
 **Data Cleaning**:
- Standardized units (e.g., km, liters, minutes).
- Removed outliers (e.g., trips with implausible fuel efficiency values).

 **Feature Engineering**:
- Peak Hour Flag: Binary column indicating if departure was during rush hours (7–9 AM, 5–7 PM).
- Avg. Speed (km/h): distance_km / (trip_duration / 60).
- CO2 per km: co2_emissions_kg / distance_km.

#### **Visualization** 