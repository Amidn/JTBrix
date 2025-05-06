# src/JTBrix/utils/results.py

def get_combined_results(submitted_results):
    combined = {
        "questions_answers": [],
        "questions_times": [],
        "popup_results": [],
        "text_input_results": [],
        "dob_results": [],
        "dropdown_results": [],
        "finished_flags": []
    }

    for entry in submitted_results:
        for key in combined:
            if key == "finished_flags":
                combined[key].append(entry.get("finished", False))
            else:
                combined[key].extend(entry.get(key, []))

    return combined