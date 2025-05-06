import os
import json
import csv
import yaml

def save_structured_output(structured_output: dict, save_path: str, name: str):
    """
    Save the structured output to TXT, YAML, and CSV formats.
    If the file doesn't exist, it creates one. Otherwise, it appends.
    """

    # --- TXT ---
    txt_path = os.path.join(save_path, f"{name}.txt")
    if not os.path.exists(txt_path):
        with open(txt_path, "w") as f:
            f.write("--- First Entry ---\n")
    with open(txt_path, "a") as f_txt:
        f_txt.write("\n--- New Entry ---\n")
        json.dump(structured_output, f_txt, indent=2)
        f_txt.write("\n")

    # --- JSON ---
    json_path = os.path.join(save_path, f"{name}.json")
    if not os.path.exists(json_path):
        with open(json_path, "w") as f_json:
            json.dump([structured_output], f_json, indent=2)
    else:
        with open(json_path, "r+") as f_json:
            try:
                data = json.load(f_json)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []
            data.append(structured_output)
            f_json.seek(0)
            json.dump(data, f_json, indent=2)
            f_json.truncate()

    # --- YAML ---
    yml_path = os.path.join(save_path, f"{name}.yml")
    if not os.path.exists(yml_path):
        with open(yml_path, "w") as f:
            yaml.dump(structured_output, f, sort_keys=False)
    else:
        with open(yml_path, "a") as f_yml:
            yaml.dump(structured_output, f_yml, sort_keys=False)
            f_yml.write("\n")

    # --- CSV ---
    csv_path = os.path.join(save_path, f"{name}.csv")
    csv_exists = os.path.exists(csv_path)
    with open(csv_path, "a", newline='') as f_csv:
        writer = csv.writer(f_csv)
        if not csv_exists:
            writer.writerow([
                "participant_first_name", "participant_surename_name", "age",
                "country", "native_language", "experiment_start", "experiment_duration_sec",
                "completed", "execution_order", "SetCode",
                "Answer1", "Answer2", "Answer3",
                "Time1", "Time2", "Time3", "Popup"
            ])
        for block in structured_output["blocks"]:
            row = [
                structured_output.get("participant_first_name", ""),
                structured_output.get("participant_surename_name", ""),
                structured_output.get("age", ""),
                structured_output.get("country", ""),
                structured_output.get("native_language", ""),
                structured_output.get("experiment_start", ""),
                structured_output.get("experiment_duration_sec", ""),
                structured_output.get("completed", ""),
                " | ".join(structured_output.get("execution_order", [])),
                block.get("SetCode", ""),
                *(block.get("answers", []) + [""] * (3 - len(block.get("answers", [])))),
                *(block.get("times", []) + [""] * (3 - len(block.get("times", [])))),
                block.get("popup", "")
            ]
            writer.writerow(row)