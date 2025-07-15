import pandas as pd

input_file = "file.xlsx"
output_file = "pointcloud_input.txt"
chunksize = 100_000  # Adjust if needed

# Convert Excel to space-separated TXT file
chunks = pd.read_excel(input_file, chunksize=chunksize)

with open(output_file, "w") as f_out:
    for chunk in chunks:
        for _, row in chunk.iterrows():
            f_out.write(f"{row['x']} {row['y']} {row['z']}\n")

print("Conversion to TXT complete.")