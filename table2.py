import pdfplumber
import json

# Initialize a list to store all extracted tables
all_tables = []

# Open the PDF file
with pdfplumber.open("ABB.pdf") as pdf:
    # Loop through each page in the PDF
    for page_number in range(len(pdf.pages)):
        page = pdf.pages[page_number]

        # Extract tables from the current page
        tables = page.extract_tables({
            "horizontal_strategy": "lines",   # Detect rows based on horizontal lines
            "vertical_strategy": "text",      # Detect columns based on text proximity
            "snap_tolerance": 3,               # Tolerance for snapping lines
            "intersection_tolerance": 5        # Tolerance for line intersection
        })

        # Loop through the extracted tables
        for i, table in enumerate(tables):
            # Create a table dictionary with heading and data
            table_data = {
                "table_heading": f"Table {len(all_tables) + 1} on Page {page_number + 1}",
                "data": []
            }

            # Filter out None rows and append to the table data
            filtered_table = [
                row for row in table 
                if row and any(cell and isinstance(cell, str) and cell.strip() for cell in row)
            ]

            # Optionally remove specific indices (e.g., removing the first row if it contains None)
            if filtered_table and filtered_table[0][0] is None:
                filtered_table.pop(0)  # Remove the first row if it's not valid

            # Add the filtered table data to the table_data dictionary
            table_data["data"] = filtered_table
            
            # Append the table_data to the all_tables list
            all_tables.append(table_data)

# Write the extracted tables to a JSON file
with open("extracted_tables.json", "w") as json_file:
    json.dump(all_tables, json_file, indent=4)

print("Tables extracted and saved to extracted_tables.json")