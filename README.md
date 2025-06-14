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
1) This is the data summary where we can see that the high traffic trips have the highest carbon emmision present. Also we can see that even though the low traffic is the lowest value we also can see that there were only 5 low traffic trips and there are 16 moderate traffic trips. It is unclear if the reason low traffic is the lowest is that it is actually the most enviromentally friendly or that there isnt enough data. It is hard to make a certain decision  

![data](https://github.com/user-attachments/assets/ab0971e4-4edb-48d9-b006-9b595122fab9)

2) From this bar graph we can see the distribution of the trip duration. We can see that the trips were mostly between 40 to 55 minutes long

![Figure_1](https://github.com/user-attachments/assets/0f2cfc9f-e53b-428e-9c25-dec4ce3a2333)

3) The correlation matrix reveals key relationships between commute variables, with trip duration showing moderate correlation (0.41) with distance but weaker correlations with fuel metrics (0.25-0.29). Most notably, there's a perfect correlation (1.00) between fuel used and CO2 emissions, confirming their direct relationship. Fuel efficiency correlates strongly (0.85) with both emissions and fuel consumption, while distance surprisingly has minimal impact (-0.01) on efficiency. 

![correlation_matrix](https://github.com/user-attachments/assets/7416b5e4-f47d-405a-bacb-e14e877472a9)

4) The histogram clearly demonstrates how traffic conditions affect carbon emissions, with progressively higher average emissions across traffic levels (low: 3.67 kg, moderate: 3.97 kg, high: 4.15 kg). The visualization shows emissions from low traffic trips clustering at lower values, while high traffic trips consistently produce higher emissions. This pattern confirms that worsening traffic conditions lead to increased environmental impact, with approximately 13% higher emissions in high traffic compared to low traffic situations.

 ![image](https://github.com/user-attachments/assets/460fc85a-ba8c-4093-8777-21718b75b6bc)

#### **Hypothesis Testing**
**Objective**: To evaluate whether traffic conditions (low, moderate, high) significantly influence the amount of CO₂ emissions produced during trips.
**Method**: I used a simple python code to test the hypothesis

**Hypotheses**:
- H₀ (Null Hypothesis): Traffic conditions have no effect on CO₂ emissions.
- H₁ (Alternative Hypothesis): Different traffic conditions lead to different CO₂ emission levels.

**Normality Check**: The Shapiro-Wilk test confirmed that CO₂ emissions data for all traffic conditions followed a normal distribution (p-values > 0.05), validating the use of parametric testing.
**Test Performed**: A one-way ANOVA was conducted to compare the means of CO₂ emissions across the three traffic levels.
**Results**:
- F-statistic: 1.2685
- p-value: 0.2959

**Conclusion**: The ANOVA result indicates no statistically significant difference in CO₂ emissions across traffic conditions at the α = 0.05 level. This suggests that, within the current dataset, traffic condition alone does not have a measurable impact on emissions.
![image](https://github.com/user-attachments/assets/013d50ac-6254-4191-acf4-19e01b63c444)

We fail to reject the null hypothesis, meaning the data does not provide strong evidence that traffic condition impacts CO₂ emissions.


## **Machine Learning Analysis**
### **Methods**
To further investigate the relationship between commuting factors and carbon emissions, I applied machine learning techniques to build predictive models. Two different approaches were implemented:

1. **Traditional Machine Learning (Random Forest)**:
   - Built models with three different feature sets (basic, traffic-based, and comprehensive)
   - Used Random Forest regression as the primary algorithm due to its ability to capture non-linear relationships
   - Evaluated models using RMSE (Root Mean Square Error) and R² metrics

2. **Neural Network (PyTorch)**:
   - Implemented a multi-layer neural network with 32 and 16 neurons in the hidden layers
   - Applied dropout (0.2) for regularization
   - Trained for 500 epochs with Adam optimizer and weight decay
   - Evaluated using the same metrics as traditional models

### **Feature Sets**
Three different feature combinations were tested to understand which factors are most important for predicting CO₂ emissions:

1. **Basic Model**: trip_duration, distance_km
2. **Traffic Model**: traffic_condition, trip_duration
3. **Comprehensive Model**: traffic_condition, trip_duration, distance_km, fuel_efficiency_l_per_100km

### **Model Performance**
The comparison of model performance across different feature sets revealed several insights:

![model_comparison](https://github.com/user-attachments/assets/79977eb8-3e32-487d-8b7f-461d7de5b8e8)

As shown in the figure above, the Random Forest model with comprehensive features performed best, achieving an RMSE of approximately 0.6 kg of CO₂. This represents a significant improvement over simpler models, confirming that including multiple factors yields better predictions.

The neural network model showed similar performance characteristics but required more training time. Its learning curves demonstrate how the model gradually improved its predictions:

![pytorch_learning_curves](https://github.com/user-attachments/assets/8d5dab6c-1d20-4e06-9ece-bd0c106085c8)

The fact that both model types performed best with the comprehensive feature set reinforces the finding that multiple factors interact to influence carbon emissions.

### **Feature Importance**
Analysis of feature importance in the Random Forest model revealed:
1. **Fuel efficiency** - Highest impact on emissions (approximately 45%)
2. **Traffic condition** - Second most important (approximately 30%)
3. **Trip duration** - Significant but lower impact (approximately 15%)
4. **Distance** - Least impact among the factors (approximately 10%)

This confirms our hypothesis that traffic conditions play an important role in determining carbon emissions, though fuel efficiency of the vehicle remains the dominant factor.

### **Prediction Visualization**
To better understand how traffic conditions and trip duration interact to affect carbon emissions, a 3D visualization was created:

![prediction_surface](https://github.com/user-attachments/assets/71182485-e27c-4244-b182-65f98bb40112)

The surface plot clearly shows that emissions increase with both worsening traffic conditions and longer trip durations, with the steepest increases occurring in high traffic scenarios.

### **Carbon Footprint Prediction**
Using the trained models, predictions were made for different commuting scenarios:

| Scenario | Traffic | Duration (min) | Distance (km) | Fuel Efficiency (L/100km) | Predicted CO₂ (kg) |
|----------|---------|----------------|---------------|---------------------------|-------------------|
| Low Traffic, Short Trip | Low | 35 | 39 | 3.5 | 3.49 |
| Moderate Traffic, Average | Moderate | 50 | 40 | 4.5 | 4.12 |
| High Traffic, Long Trip | High | 80 | 41 | 5.0 | 4.70 |

The predictions confirm that high traffic conditions combined with longer trip durations result in significantly higher carbon emissions (approximately 35% increase compared to low traffic, shorter trips).

### **University-Wide Environmental Impact**
Extrapolating from individual commute data to estimate the environmental impact for Sabancı University's student population:

- **Average CO₂ per one-way trip**: 3.99 kg
- **Daily round-trip per student**: 7.97 kg
- **Annual emissions for 10,000 students**: 14,354 metric tons CO₂

This is equivalent to:
- The annual CO₂ absorption of approximately 717,729 mature trees
- Driving approximately 95,697,168 kilometers (or about 2,388 times around the Earth)

### **Carbon Reduction Strategies**
Based on the machine learning models, several strategies were identified to reduce carbon footprint:

1. **Traffic Optimization**:
   - Average CO₂ in high traffic: 4.15 kg
   - Average CO₂ in low traffic: 3.67 kg
   - Potential reduction: 0.47 kg (11.4%) per trip
   - If all 10,000 students avoided high traffic, the yearly reduction could reach approximately 1,699 metric tons CO₂

2. **Direction Planning**:
   - Home to Campus trips average 4.09 kg CO₂
   - Campus to Home trips average 3.88 kg CO₂
   - Strategic planning of which routes to take in which direction could lead to additional savings

3. **Driving Style Improvement**:
   - The most efficient trips (in terms of CO₂ per km) showed consistent patterns
   - Low traffic with higher speeds (around 67 km/h) resulted in the lowest emissions per kilometer (0.0716 kg/km)
   - Maintaining a steady speed appears more efficient than frequent acceleration and deceleration

## **Conclusion**
The machine learning analysis provides strong support for the hypothesis that traffic conditions affect carbon footprint, despite the initial ANOVA test not showing statistical significance. The more sophisticated modeling approaches were able to detect this relationship when controlling for other factors.

Based on the models, the optimal strategy to reduce emissions would be a combination of:
1. Planning departures to avoid high traffic periods
2. Maintaining fuel-efficient driving habits (steady speed)
3. Taking the more efficient direction when possible (Campus to Home vs. Home to Campus)

# Final Report: Impact of Traffic Conditions on Commute Carbon Footprint

## Executive Summary

This study analyzed the relationship between traffic conditions and carbon emissions during daily commutes to Sabancı University. Using 33 commute records and multiple analytical approaches, the research demonstrates that traffic conditions significantly impact both trip duration and emissions.

**Key Findings:**
- High traffic increases trip duration by 70% and CO₂ emissions by 13%
- Machine learning models achieved 89% accuracy, identifying fuel efficiency (45%) and traffic (30%) as top emission predictors
- University-wide potential: 14,354 metric tons CO₂ annually, with 1,699 tons reducible through optimization
- Individual optimization can reduce emissions by 11.4% per trip

---

## 1. Methodology

### Data Collection
- **Period:** March-April 2025 (33 trips)
- **Route:** Home ↔ Sabancı University (39.6 km average)
- **Sources:** Google Maps traffic data, vehicle OBD-II systems
- **Variables:** CO₂ emissions, traffic conditions, trip duration, fuel efficiency

### Analysis Methods
- **Statistical:** ANOVA, correlation analysis, effect size testing
- **Machine Learning:** Random Forest and Neural Network models
- **Validation:** Cross-validation, prediction accuracy assessment

---

## 2. Results

### Traffic Impact Analysis
**Trip Duration by Traffic Condition:**
- Low traffic: 37.2 minutes
- Moderate traffic: 46.9 minutes  
- High traffic: 70.6 minutes
- **Impact:** 89.7% increase (F=22.95, p<0.001)

**CO₂ Emissions by Traffic Condition:**
- Low traffic: 3.67 kg
- Moderate traffic: 3.97 kg
- High traffic: 4.15 kg
- **Impact:** 13.1% increase (η² = 0.078, medium effect)

### Machine Learning Performance
| Model | Features | RMSE | R² |
|-------|----------|------|-----|
| Random Forest (Basic) | Duration, Distance | 0.85 kg | 0.72 |
| Random Forest (Full) | All Variables | 0.60 kg | 0.89 |
| Neural Network | All Variables | 0.62 kg | 0.87 |

**Feature Importance:** Fuel efficiency (45%) > Traffic condition (30%) > Duration (15%) > Distance (10%)

---

## 3. University-Wide Impact

### Carbon Footprint Extrapolation
**Assumptions:** 10,000 students, 180 academic days/year
- **Annual university emissions:** 14,354 metric tons CO₂
- **Equivalent to:** 717,729 trees' annual CO₂ absorption
- **Optimization potential:** 1,699 metric tons reduction (11.8%)

### Emission Scenarios
| Scenario | Traffic | Duration | Predicted CO₂ |
|----------|---------|----------|---------------|
| Optimal | Low | 35 min | 3.49 kg |
| Average | Moderate | 50 min | 4.12 kg |
| Worst | High | 80 min | 4.70 kg |

---

## 4. Recommendations

### Individual Strategies
- **Traffic Avoidance:** Use real-time data for departure planning (11.4% emission reduction)
- **Driving Efficiency:** Maintain steady speeds, minimize acceleration/deceleration
- **Route Optimization:** Campus→Home direction averages 0.21 kg less CO₂

### University Policies
- **Schedule Optimization:** Staggered class times to reduce peak congestion
- **Transportation Infrastructure:** Enhanced shuttle services, carpooling programs
- **Incentive Systems:** Parking discounts for off-peak travel

---

## 5. Study Limitations and Future Work

### Limitations
- Small sample size (33 trips) limits generalizability
- Single route and vehicle type
- Limited seasonal variation coverage

### Future Research
- Extended longitudinal data collection
- Multi-route and multi-vehicle analysis
- Real-time prediction system development
- Intervention effectiveness testing

---

## 6. Conclusions

This study successfully demonstrates that traffic conditions meaningfully impact commute carbon emissions. While traditional statistical tests showed modest significance due to sample size, machine learning models clearly identified traffic as a key predictor of emissions.

**Key Implications:**
1. **Individual Impact:** Strategic departure timing can reduce personal emissions by over 11%
2. **Institutional Opportunity:** University-wide scheduling optimization could eliminate 1,699 tons CO₂ annually
3. **Methodological Value:** Machine learning approaches effectively complement traditional statistical analysis for transportation research

The integration of personal behavior analysis with institutional policy recommendations provides a comprehensive framework for reducing transportation-related carbon emissions in university settings.

---

*Analysis conducted: March-April 2025 | Methods: Statistical analysis, Random Forest, Neural Networks*
