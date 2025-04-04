import json
import csv
import os

def convert_to_alpaca(data, format_type):
    """
    Converts data into Alpaca format (input, output, context).
    
    Args:
        data: The input data (list of dictionaries or raw text).
        format_type: The format of input data ('txt', 'json', 'csv').
    
    Returns:
        A list of dictionaries in Alpaca format.
    """
    alpaca_data = []
    
    if format_type == "json":
        for item in data:
            alpaca_data.append({
                "input": item.get("input", ""),
                "output": item.get("output", ""),
                "context": item.get("context", "")
            })
    elif format_type == "csv":
        for row in data:
            alpaca_data.append({
                "input": row[0] if len(row) > 0 else "",
                "output": row[1] if len(row) > 1 else "",
                "context": row[2] if len(row) > 2 else ""
            })
    elif format_type == "txt":
        for line in data:
            parts = line.strip().split("|||")  # Assuming '|||' separates input, output, and context
            alpaca_data.append({
                "input": parts[0] if len(parts) > 0 else "",
                "output": parts[1] if len(parts) > 1 else "",
                "context": parts[2] if len(parts) > 2 else ""
            })
    return alpaca_data


def load_data(file_path):
    """Loads data from a given file path based on the file extension."""
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, "json"
    elif ext == ".csv":
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
        return data, "csv"
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.readlines()
        return data, "txt"
    else:
        raise ValueError("Unsupported file format. Use JSON, CSV, or TXT.")


def save_alpaca_data(alpaca_data, output_path="alpaca_output.json"):
    """Saves the converted data in Alpaca format as a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(alpaca_data, f, indent=4)
    print(f"Converted data saved to {output_path}")


if __name__ == "__main__":
    input_file = "data.json"  # Change this to your input file
    data, format_type = load_data(input_file)
    alpaca_data = convert_to_alpaca(data, format_type)
    save_alpaca_data(alpaca_data)
