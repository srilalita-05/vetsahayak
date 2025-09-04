import streamlit as st
from utils import check_symptoms, get_faq_answer, get_emergency_steps, symptoms_df

st.title("🐾 VetSahayak - Veterinary Doctor Bot")

# Sidebar navigation
menu = ["Symptom Checker", "Pet Care FAQs", "Emergency First Steps"]
choice = st.sidebar.selectbox("Choose a service", menu)

# ------------------ Symptom Checker ------------------
if choice == "Symptom Checker":
    st.header("🐶 Symptom Checker")

    # Get unique animal names from dataset
    animal_list = symptoms_df['animalname'].dropna().unique().tolist()
    animal = st.selectbox("Select Animal", sorted(animal_list))

    symptoms_input = st.text_area(
        "Enter symptoms (comma-separated, e.g., Fever, Vomiting, Lethargy):"
    )
    if st.button("Check"):
        symptoms = [s.strip() for s in symptoms_input.split(",") if s.strip()]
        if not symptoms:
            st.warning("Please enter at least one symptom.")
        else:
            result = check_symptoms(animal, symptoms)
            if result["found"]:
                st.success(f"Matched Symptoms: {', '.join(result['matches'])}")
                st.info(f"Dangerous: {result['dangerous']}")
                st.write(result["message"])
            else:
                st.error(result["message"])

# ------------------ FAQs ------------------
elif choice == "Pet Care FAQs":
    st.header("📖 Pet Care FAQs")
    question = st.text_input("Ask a question (e.g., vaccination, feeding, exercise, grooming):")
    if st.button("Get Answer"):
        st.write(get_faq_answer(question))

# ------------------ Emergency ------------------
elif choice == "Emergency First Steps":
    st.header("🚨 Emergency Help")
    issue = st.text_input("Describe the issue (e.g., bleeding, poisoning, choking, fracture):")
    if st.button("Get Emergency Steps"):
        st.write(get_emergency_steps(issue))
