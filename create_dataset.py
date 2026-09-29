import pandas as pd
import numpy as np

# For reproducible results
np.random.seed(42)

# Machine IDs
machines = [f"M{i:03d}" for i in range(1, 31)]

# Machine categories
categories = [
    "CNC Machine",
    "Conveyor",
    "Press Machine",
    "Lathe",
    "Milling Machine",
    "Robotic Arm"
]

# Assign categories to machines
machine_category = {
    machine: categories[i % len(categories)]
    for i, machine in enumerate(machines)
}

records = []

# Generate maintenance records
for machine in machines:

    category = machine_category[machine]

    # Base characteristics of each machine
    base_downtime = np.random.uniform(6, 18)
    base_production = np.random.randint(700, 1400)

    for event in range(6):

        # Maintenance date
        date = (
            pd.Timestamp("2025-01-01")
            + pd.Timedelta(days=np.random.randint(0, 365))
        )

        # Some machines improve slightly after maintenance,
        # while some continue to have higher downtime.
        if machine in ["M005", "M011", "M017", "M023", "M029"]:
            improvement = event * 1.2
        elif machine in ["M003", "M009", "M015", "M021", "M027"]:
            improvement = -event * 0.5
        else:
            improvement = 0

        downtime = max(
            1,
            base_downtime - improvement + np.random.normal(0, 2.5)
        )

        # Production volume
        production = max(
            300,
            base_production + np.random.normal(0, 120)
        )

        # Failure count
        failure_count = max(
            0,
            int(np.random.poisson(2))
        )

        # Add record
        records.append([
            machine,
            category,
            date,
            round(downtime, 2),
            round(production),
            failure_count
        ])


# Create DataFrame
df = pd.DataFrame(
    records,
    columns=[
        "Machine_ID",
        "Machine_Category",
        "Maintenance_Date",
        "Downtime_Hours",
        "Production_Volume",
        "Failure_Count"
    ]
)

# Sort by machine and maintenance date
df = df.sort_values(
    ["Machine_ID", "Maintenance_Date"]
).reset_index(drop=True)

# Save dataset
df.to_csv(
    "manufacturing_maintenance_data.csv",
    index=False
)

# Display information
print("==========================================")
print("MANUFACTURING DATASET CREATED")
print("==========================================")

print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 10 records:")
print(df.head(10))

print("\nMachine categories:")
print(df["Machine_Category"].value_counts())

print("\nDataset saved as:")
print("manufacturing_maintenance_data.csv")