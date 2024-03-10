import csv
import json

# Your connections logic
connection_logic = [
    {
        "role": "Inspector",
        "connections": [
            {"to": "Deputy Inspector", "weight": 10},
        ],
    },
    {
        "role": "Deputy Inspector",
        "connections": [
            {"to": "Captain", "weight": 8},
        ],
    },
    {
        "role": "Captain",
        "connections": [
            {"to": "Lieutenant", "weight": 6},
        ],
    },
    {
        "role": "Lieutenant",
        "connections": [
            {"to": "Sergeant", "weight": 4},
        ],
    },
    {
        "role": "Sergeant",
        "connections": [
            {"to": "Detective", "weight": 2},
        ],
    },
    {
        "role": "Detective",
        "connections": [
            {"to": "Police Officer", "weight": 1},
        ],
    },
    {
        "role": "Police Officer",
        "connections": [],
    },
]

# Transform the connection logic into a more accessible format
connections_map = {item["role"]: item["connections"] for item in connection_logic}

# Step 2: Reading from the CSV file and processing the data
nodes = []
links = []  # Initialized to generate meaningful links based on role connections

# Assuming the path is updated to the correct CSV location
csv_file_path = "process2_morethan25.csv"

# Read the CSV data, ensuring correct handling of delimiters and column headers
# Read the CSV data, converting officers to a list for reusability
with open(csv_file_path, mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    officers = list(reader)  # Convert to a list to iterate multiple times

# Generate nodes from officers
for officer in officers:
    # skip Total_Abuse_count > 3 case

    nodes.append(
        {
            "id": officer["full_name"],
            "total_abuse_count": int(officer["Total_Abuse_count"]),
            "rank_incident": officer["rank_incident"],
            "precinct": int(officer["precinct"]),
        }
    )


# Generate links based on precinct and role connections
for officer in officers:
    officer_role = officer["rank_incident"]
    officer_precinct = int(officer["precinct"])
    for connection in connections_map.get(officer_role, []):
        target_role = connection["to"]
        weight = connection["weight"]
        # Find officers in the same precinct with the target role
        for target_officer in [
            o
            for o in officers
            if int(o["precinct"]) == officer_precinct
            and o["rank_incident"] == target_role
        ]:
            links.append(
                {
                    "source": officer["full_name"],
                    "target": target_officer["full_name"],
                    "value": weight,
                }
            )

# Step 3: Writing the processed data to a JSON file
json_data = {"nodes": nodes, "links": links}
json_file_path = "process2_processed2-25.json"
with open(json_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

json_file_path
