import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, TensorDataset, DataLoader
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Set random seed for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# ---------------------------------------------------------
# Simple CO2 Emissions Prediction with PyTorch
# ---------------------------------------------------------

print("------------------------------------------------------")
print("COMMUTE CARBON FOOTPRINT PREDICTION WITH PYTORCH")
print("------------------------------------------------------")

# 1. Data Loading and Preprocessing
print("\n1. Loading and Preprocessing Data...")

# Load data from CSV file
data_file = '../commute_data.csv' 
try:
    df = pd.read_csv(data_file)
    print(f"Successfully loaded data from {data_file}")
except FileNotFoundError:
    print(f"Error: The file {data_file} was not found.")
    print("Please make sure the CSV file is in the correct location.")
    print("Exiting program.")
    exit()
except Exception as e:
    print(f"Error loading data: {str(e)}")
    print("Exiting program.")
    exit()

# Add derived features
df['avg_speed'] = df['distance_km'] / (df['trip_duration'] / 60)
df['co2_per_km'] = df['co2_emissions_kg'] / df['distance_km']
df['direction_binary'] = (df['trip_direction'] == 'Home to Campus').astype(int)

# Extract hour from departure time
df['departure_hour'] = pd.to_datetime(df['departure_time'], format='%H:%M').dt.hour

# Convert traffic condition to text for better display
traffic_map = {0: 'Low', 1: 'Moderate', 2: 'High'}
df['traffic_text'] = df['traffic_condition'].map(traffic_map)

print(f"Loaded {len(df)} commute records")
print(f"Average CO2 emissions: {df['co2_emissions_kg'].mean():.2f} kg")
print(f"CO2 emissions range: {df['co2_emissions_kg'].min():.2f} - {df['co2_emissions_kg'].max():.2f} kg")

# Display average CO2 by traffic condition
traffic_summary = df.groupby('traffic_text')['co2_emissions_kg'].agg(['mean', 'count'])
print("\nAverage CO2 emissions by traffic condition:")
for traffic, (mean, count) in traffic_summary.iterrows():
    print(f"  {traffic} traffic ({count} trips): {mean:.2f} kg")

# 2. Define Neural Network Model
print("\n2. Defining PyTorch Neural Network Model...")

class CarbonFootprintNN(nn.Module):
    """Neural network model for predicting CO2 emissions"""
    
    def __init__(self, input_dim):
        super(CarbonFootprintNN, self).__init__()
        self.layer1 = nn.Linear(input_dim, 32)
        self.layer2 = nn.Linear(32, 16)
        self.layer3 = nn.Linear(16, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)  # Add dropout for regularization
        
    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.dropout(x)
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x

# 3. Data Preparation for PyTorch
print("\n3. Preparing Data for PyTorch...")

# Define features
features = ['traffic_condition', 'trip_duration', 'distance_km', 'fuel_efficiency_l_per_100km']
X = df[features].values
y = df['co2_emissions_kg'].values.reshape(-1, 1)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert to PyTorch tensors
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)

# Create TensorDataset and DataLoader
dataset = TensorDataset(X_tensor, y_tensor)

# Split data into training and testing sets (80/20)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(
    dataset, [train_size, test_size], generator=torch.Generator().manual_seed(42)
)

# Create data loaders
batch_size = 4
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

print(f"Training set size: {len(train_dataset)}")
print(f"Testing set size: {len(test_dataset)}")
print(f"Feature columns: {features}")

print("\n4. Training Neural Network Model...")


input_dim = X_scaled.shape[1]
model = CarbonFootprintNN(input_dim)


criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)

num_epochs = 500
train_losses = []
test_losses = []

for epoch in range(num_epochs):
    model.train()
    train_loss = 0.0
    
    for inputs, targets in train_loader:
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        train_loss += loss.item()
    
    train_loss /= len(train_loader)
    train_losses.append(train_loss)
    
    model.eval()
    test_loss = 0.0
    
    with torch.no_grad():
        for inputs, targets in test_loader:
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            test_loss += loss.item()
    
    test_loss /= len(test_loader)
    test_losses.append(test_loss)

    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}")

print("Training complete!")


print("\n5. Evaluating Model Performance...")


model.eval()
all_predictions = []
all_targets = []

with torch.no_grad():
    for inputs, targets in test_loader:
        outputs = model(inputs)
        all_predictions.extend(outputs.numpy().flatten())
        all_targets.extend(targets.numpy().flatten())

all_predictions = np.array(all_predictions)
all_targets = np.array(all_targets)

mse = np.mean((all_predictions - all_targets) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(all_predictions - all_targets))

y_mean = np.mean(all_targets)
ss_total = np.sum((all_targets - y_mean) ** 2)
ss_residual = np.sum((all_targets - all_predictions) ** 2)
r2 = 1 - (ss_residual / ss_total)

print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f} kg")
print(f"Mean Absolute Error (MAE): {mae:.4f} kg")
print(f"R-squared (R²): {r2:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Training Loss')
plt.plot(test_losses, label='Testing Loss')
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.title('Learning Curves')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('pytorch_learning_curves.png', dpi=300)
plt.close()

plt.figure(figsize=(10, 6))
plt.scatter(all_targets, all_predictions, alpha=0.7)
plt.plot([min(all_targets), max(all_targets)], [min(all_targets), max(all_targets)], 'r--')
plt.xlabel('Actual CO2 Emissions (kg)')
plt.ylabel('Predicted CO2 Emissions (kg)')
plt.title('Predicted vs Actual CO2 Emissions')
plt.grid(True, alpha=0.3)
plt.savefig('pytorch_predictions.png', dpi=300)
plt.close()

print("\n6. Making Predictions with Trained Model...")


def predict_co2(traffic_condition, trip_duration, distance_km, fuel_efficiency):
   
    input_data = np.array([[traffic_condition, trip_duration, distance_km, fuel_efficiency]])
    input_scaled = scaler.transform(input_data)
    input_tensor = torch.tensor(input_scaled, dtype=torch.float32)
    
    model.eval()
    with torch.no_grad():
        prediction = model(input_tensor)
    
    return prediction.item()

test_cases = [
    {"name": "Low Traffic, Short Trip", "traffic": 0, "duration": 35, "distance": 39, "efficiency": 3.5},
    {"name": "Moderate Traffic, Average Trip", "traffic": 1, "duration": 50, "distance": 40, "efficiency": 4.5},
    {"name": "High Traffic, Long Trip", "traffic": 2, "duration": 80, "distance": 41, "efficiency": 5.0}
]

print("Carbon footprint predictions for different scenarios:")
for case in test_cases:
    prediction = predict_co2(
        case["traffic"], 
        case["duration"], 
        case["distance"], 
        case["efficiency"]
    )
    traffic_text = traffic_map[case["traffic"]]
    print(f"\n{case['name']}:")
    print(f"  Traffic: {traffic_text}")
    print(f"  Duration: {case['duration']} minutes")
    print(f"  Distance: {case['distance']} km")
    print(f"  Fuel Efficiency: {case['efficiency']} L/100km")
    print(f"  Predicted CO2 Emissions: {prediction:.2f} kg")

print("\n7. Interactive Prediction")
print("Enter your commute details to predict CO2 emissions:")

try:
    traffic_input = input("Traffic condition (0=Low, 1=Moderate, 2=High): ")
    duration_input = input("Trip duration (minutes): ")
    distance_input = input("Distance (km): ")
    efficiency_input = input("Fuel efficiency (L/100km): ")
    
    traffic = int(traffic_input)
    duration = float(duration_input)
    distance = float(distance_input)
    efficiency = float(efficiency_input)
    
    prediction = predict_co2(traffic, duration, distance, efficiency)
    
    print(f"\nPredicted CO2 emissions: {prediction:.2f} kg")
    
    similar_trips = df[
        (df['traffic_condition'] == traffic) & 
        (df['trip_duration'].between(duration * 0.8, duration * 1.2))
    ]
    
    if len(similar_trips) > 0:
        avg_similar = similar_trips['co2_emissions_kg'].mean()
        print(f"Average CO2 for similar trips in dataset: {avg_similar:.2f} kg")
    else:
        print("No similar trips found in the dataset for comparison")
        
except ValueError:
    print("Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"Error: {str(e)}")

print("\n8. Environmental Impact Estimation")

avg_co2_per_trip = df['co2_emissions_kg'].mean()
daily_commute = avg_co2_per_trip * 2  

student_counts = [1, 100, 1000, 10000]
school_days = 180  

print("\nEstimated yearly CO2 emissions from commuting:")
for count in student_counts:
    yearly_total = daily_commute * count * school_days
    print(f"  {count} students: {yearly_total:.1f} kg ({yearly_total/1000:.1f} metric tons)")

student_count = 10000
yearly_total = daily_commute * student_count * school_days
trees_equivalent = yearly_total / 20  
car_km_equivalent = yearly_total / 0.15  

print(f"\nFor {student_count} students, yearly emissions equivalent to:")
print(f"  - Annual CO2 absorption of {trees_equivalent:,.0f} mature trees")
print(f"  - Driving {car_km_equivalent:,.0f} kilometers")
print(f"  - Driving {car_km_equivalent/40075:.0f} times around the Earth")

print("\n9. Carbon Reduction Strategies")

traffic_means = df.groupby('traffic_condition')['co2_emissions_kg'].mean()
if 0 in traffic_means.index and 2 in traffic_means.index:
    low_traffic_mean = traffic_means[0]
    high_traffic_mean = traffic_means[2]
    reduction = high_traffic_mean - low_traffic_mean
    reduction_percent = (reduction / high_traffic_mean) * 100
    
    print(f"1. Avoiding High Traffic")
    print(f"   Average CO2 in high traffic: {high_traffic_mean:.2f} kg")
    print(f"   Average CO2 in low traffic: {low_traffic_mean:.2f} kg")
    print(f"   Potential reduction: {reduction:.2f} kg ({reduction_percent:.1f}%)")
    
    university_reduction = reduction * 2 * student_count * school_days
    print(f"   If all {student_count} students avoided high traffic conditions:")
    print(f"   Annual reduction: {university_reduction/1000:.2f} metric tons CO2")

print("\n10. Saving the Model")

model_save_path = 'commute_carbon_pytorch_model.pt'
torch.save({
    'model_state_dict': model.state_dict(),
    'input_dim': input_dim,
    'features': features,
    'scaler': scaler
}, model_save_path)

print(f"Model saved to {model_save_path}")
