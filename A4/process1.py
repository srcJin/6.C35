import pandas as pd

# Load the uploaded CSV file
file_path = "process1.csv"
data = pd.read_csv(file_path)

fado_types = ["Abuse of Authority", "Discourtesy", "Offensive Language", "Force"]


# Calculate the most common precinct and rank_incident for each Full Name
data["precinct"] = data.groupby("full_name")["precinct"].transform(
    lambda x: x.mode()[0]
)
data["rank_incident"] = data.groupby("full_name")["rank_incident"].transform(
    lambda x: x.mode()[0]
)
data["shield_no"] = data.groupby("full_name")["shield_no"].transform(
    lambda x: x.mode()[0]
)

# Now we'll pivot the data again with this simplification
simplified_data = pd.DataFrame()

for name, group in data.groupby("full_name"):
    record = {
        "full_name": name,
        "shield_no": group["shield_no"].iloc[0],  # Most common precinct
        "precinct": group["precinct"].iloc[0],  # Most common precinct
        "rank_incident": group["rank_incident"].iloc[0],  # Most common rank_incident
        "mos_age_list": group["mos_age_incident"].unique().tolist(),
    }

    # For each fado type, compile IDs and counts
    for fado_type in fado_types:
        fado_group = group[group["fado_type"] == fado_type]
        record[f"{fado_type}_ids"] = fado_group["unique_mos_id"].tolist()
        record[f"{fado_type}_count"] = len(fado_group)

    record_df = pd.DataFrame([record])

    simplified_data = pd.concat([simplified_data, record_df], ignore_index=True)

# Rename columns to match the requested format more closely
simplified_data.columns = simplified_data.columns.str.replace(" ", "_").str.replace(
    "of_Authority", "of_Authority"
)

# Save the simplified DataFrame to a new CSV file
output_file_path_simplified = "pivoted_data.csv"
simplified_data.to_csv(output_file_path_simplified, index=False)

output_file_path_simplified
