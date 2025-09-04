import pandas as pd

# ----------------- Load and Clean Dataset -----------------
symptoms_df = pd.read_csv("symptoms_data.csv")

# Normalize column names
symptoms_df.columns = symptoms_df.columns.str.strip().str.lower()

# Normalize 'animalname' values
if 'animalname' in symptoms_df.columns:
    symptoms_df['animalname'] = symptoms_df['animalname'].str.strip().str.lower()
else:
    raise KeyError("The column 'AnimalName' is missing in the dataset.")

# ----------------- FAQs -----------------
faq_data = {
    "vaccination": "Pets should be vaccinated once a year. Puppies and kittens may need more frequent shots.",
    "feeding": "Feed pets twice a day. Ensure fresh water is always available.",
    "exercise": "Dogs need at least 30 minutes of daily exercise. Cats benefit from playtime.",
    "grooming": "Brush your pet regularly and check for ticks, fleas, and skin issues."
}

def get_faq_answer(question: str) -> str:
    """Return FAQ answer if found, else default message."""
    question = question.lower()
    for key, answer in faq_data.items():
        if key in question:
            return answer
    return "Sorry, I don't have an answer for that yet. Please consult a vet for more details."


# ----------------- Emergency -----------------
emergency_data = {
    "bleeding": "Apply gentle pressure with a clean cloth. Keep the pet calm and take to the vet immediately.",
    "poisoning": "Do NOT induce vomiting unless told by a vet. Take your pet and the substance container to the vet.",
    "choking": "Check the mouth for objects. If safe, remove it. If breathing stops, perform pet CPR and rush to the vet.",
    "fracture": "Keep the pet still, avoid movement of the injured limb, and transport carefully to the vet."
}

def get_emergency_steps(issue: str) -> str:
    """Return emergency steps based on issue."""
    issue = issue.lower()
    for key, steps in emergency_data.items():
        if key in issue:
            return steps
    return "Please keep your pet safe and consult a vet immediately."


# ----------------- Symptom Checker -----------------
def check_symptoms(animal: str, symptom_list: list) -> dict:
    """Check symptoms against dataset and return result."""
    animal = animal.strip().lower()
    symptom_list = [s.strip().lower() for s in symptom_list]

    # Filter matching animal rows
    matched_rows = symptoms_df[symptoms_df['animalname'] == animal]
    if matched_rows.empty:
        return {"found": False, "message": f"No data available for '{animal}'."}

    # Auto-detect symptom columns
    symptom_columns = [col for col in symptoms_df.columns if col.startswith("symptoms")]
    all_symptoms = matched_rows[symptom_columns].values.flatten().tolist()
    all_symptoms = [s.strip().lower() for s in all_symptoms if pd.notna(s)]

    # Fuzzy/partial match: check if user symptom matches any part of known symptoms or vice versa
    matches = []
    for user_symptom in symptom_list:
        for s in all_symptoms:
            if user_symptom in s or s in user_symptom:
                matches.append(s)

    if not matches:
        return {"found": False, "message": "No matching symptoms found in dataset."}

    # Check for danger
    danger_flag = "No"
    for _, row in matched_rows.iterrows():
        if str(row.get("dangerous", "")).strip().lower() == "yes":
            row_symptoms = [str(row[col]).strip().lower() for col in symptom_columns if pd.notna(row[col])]
            if any(user_symptom in rs or rs in user_symptom for rs in row_symptoms for user_symptom in symptom_list):
                danger_flag = "Yes"
                break

    return {
        "found": True,
        "matches": list(set(matches)),
        "dangerous": danger_flag,
        "message": "⚠️ Please consult a vet immediately!" if danger_flag == "Yes" else "🙂 Seems manageable, but keep monitoring your pet."
    }
