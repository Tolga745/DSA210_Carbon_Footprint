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

---
