# 🐾 VetSahayak - Veterinary Doctor Bot

VetSahayak is a simple, interactive **veterinary assistant web app** built with **Streamlit**.
It helps pet owners by providing:

* ✅ **Symptom Checker** – Identify possible health issues for pets based on entered symptoms
* 📖 **Pet Care FAQs** – Quick answers to common pet care questions (feeding, vaccination, grooming, exercise)
* 🚨 **Emergency First Steps** – Immediate actions for common emergencies (bleeding, poisoning, choking, fracture)

---

## 🚀 Features

* **Symptom Checker**

  * Select an animal from the dataset
  * Enter symptoms (comma-separated)
  * Get matched symptoms, severity (dangerous or not), and advice

* **Pet Care FAQs**

  * Ask common questions (feeding, vaccination, exercise, grooming)
  * Get instant answers from a predefined FAQ dataset

* **Emergency Help**

  * Enter an emergency issue (bleeding, poisoning, choking, fracture)
  * Receive immediate first-aid steps before visiting a vet

---

## 🛠️ Installation & Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/vetsahayak.git
   cd vetsahayak
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   pip freeze > requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure

```
.
├── app.py                # Main Streamlit app
├── utils.py              # Core logic: FAQs, Emergency steps, Symptom checker
├── symptoms_data.csv     # Dataset of animals & symptoms
├── all_animals_faqs.csv  # Extended FAQs dataset
└── README.md             # Project documentation
```

---

## 📊 Dataset

* **`symptoms_data.csv`** – Contains animal names, symptoms, and severity markers.
* **`all_animals_faqs.csv`** – Additional FAQ questions and answers for pet care.

---

## 🐕 Supported Use Cases

* Urban & rural pet owners
* Guidance for pet first-aid and emergency handling
* Quick information about vaccinations, feeding, grooming, and exercise

---

## ⚠️ Disclaimer

This tool is **not a substitute for professional veterinary care**.
Always consult a qualified veterinarian for diagnosis and treatment.

---

# 🛣️ Roadmap for Future Enhancements

The current version of **VetSahayak** is **rule/pattern-based** (no ML yet), but the code and CSVs are already structured to support gradual upgrades toward a more intelligent assistant.

---

## Current State

* App built in **Streamlit** with three features via `utils.py`:

  * FAQ answers via keyword matching
  * Emergency steps via keyword matching
  * Symptom checker via substring/rule-based matching on `symptoms_data.csv`
* A rich FAQs CSV (`all_animals_faqs.csv`) exists and can be leveraged as a knowledge base for retrieval-based search.

---

## 🔄 Enhancement Phases

### **Phase 1: Data Cleaning & Structuring**

* Normalize column names (`AnimalName` → `animalname`, `symptom1..n`).
* Fix typos (e.g., “appettite” → “appetite”) and remove duplicates.
* Standardize `all_animals_faqs.csv` to replace the in-code FAQ dictionary.
* Create **train/dev/test splits** for FAQ intents and symptom labels.

---

### **Phase 2: NLU for Intents & Entities**

* Train a lightweight **intent classifier** (baseline: sklearn or small transformer).

  * High-level intents: `Symptom Check`, `FAQ`, `Emergency`.
  * Sub-intents: vaccination, diet, deworming, etc.
* Add **entity extraction** for:

  * Animal names (dictionary from CSV).
  * Symptom tokens (regex/dictionary).
* Expose functions:

  * `predict_intent(text)` → intent label
  * `parse_entities(text)` → detected animals + symptoms

---

### **Phase 3: Retrieval over FAQs (RAG)**

* Build embeddings for **Question + Answer + Animal** fields in `all_animals_faqs.csv`.
* Store in **FAISS/Chroma** index and implement:

  * `retrieve(query, top_k=3)` → top FAQ rows.
* Return retrieved answers + related Q/As as suggestions.
* Optionally, add an **LLM rewriter** for more natural answers grounded in retrieved rows.

---

### **Phase 4: Symptom Checker Model**

* Train a **risk classifier** from `symptoms_data.csv`:

  * Input: concatenated symptoms text + animal.
  * Output: `Dangerous = Yes/No`.
* Baseline: **TF-IDF + Logistic Regression**, later expand to per-animal features.
* Expose function:

  * `predict_risk(animal, free_text_symptoms)`
* Combine ML risk prediction with rule matcher as an **ensemble** for better reliability.

---

### **Phase 5: App Refactor**

* Add a **Router**:

  * Every query → `predict_intent + parse_entities`
  * Route to **FAQ retriever / Emergency / Symptom checker**
* Keep existing tabs, but introduce a **single “Ask Anything” box** that auto-routes.
* Replace `utils.get_faq_answer` with retriever-backed function.

---

### **Phase 6: Evaluation Loop**

* Log queries, predicted intents, answers, and confidence scores.
* Review **low-confidence / no-answer cases** weekly to add paraphrases and improve labels.
* For symptoms: measure **precision/recall on Dangerous label**.
* Maintain rule-based emergency triggers (e.g., *inability to urinate*).

---

### **Phase 7: Safety & Guardrails**

* Always include **“consult a vet” disclaimer** for emergencies.
* Avoid **dosage recommendations**.
* If LLM generation is added, constrain outputs to **retrieved facts only**.
* Escalate to vet automatically on **red-flag symptoms** or **low confidence**.

---

### **Phase 8: Optional Fine-Tuning**

* Consider fine-tuning only if needed for **tone/style** consistency.
* Keep facts outside the model (via retrieval), so updates remain easy.
* Build a small **human-edited dataset** for supervised fine-tuning.

---

## ✅ Deliverables Checklist

* `data/` module with cleaned CSVs + splits
* `nlu.py` → `predict_intent`, `parse_entities`
* `retriever.py` → build index, retrieve answers
* `models.py` → `predict_risk`
* Refactored `app.py` with unified query box

---


