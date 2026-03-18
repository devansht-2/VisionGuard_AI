# stage = input("Enter CNN Prediction (0-4): ")

# stages = {
#     "0": "No Diabetic Retinopathy detected.",
#     "1": "Mild Diabetic Retinopathy.",
#     "2": "Moderate Diabetic Retinopathy.",
#     "3": "Severe Diabetic Retinopathy.",
#     "4": "Proliferative Diabetic Retinopathy."
# }

# print("\n--- Virtual Retinal Assistant ---\n")

# print("Doctor Bot:")
# print(f"I have received your retinal screening report. It indicates: {stages.get(stage,'Unknown stage')}")

# print("\nI would like to understand how you are feeling.")
# print("Are you experiencing blurred vision, floaters, eye strain, or difficulty seeing at night?\n")

# while True:
#     user = input("Patient: ").lower()

#     if "blur" in user or "vision" in user:
#         print("\nDoctor Bot:")
#         print("Blurred vision can occur when blood sugar affects the small blood vessels in the retina.")
    
#     if "pain" in user:
#         print("\nDoctor Bot:")
#         print("Eye discomfort may occur due to strain or dryness. It is recommended to rest the eyes and maintain hydration.")

#     print("\nPrecautions you should follow:")

#     print("- Maintain stable blood sugar levels")
#     print("- Eat foods rich in Vitamin A, C and Omega-3")
#     print("- Include spinach, carrots, oranges, almonds and fish in diet")
#     print("- Avoid excessive sugar and processed food")
#     print("- Take breaks from screens every 20 minutes")
#     print("- Maintain regular sleep schedule")

#     print("\nLifestyle Tips:")
#     print("- Gentle eye relaxation exercises")
#     print("- Regular walking to control diabetes")
#     print("- Annual retinal check-ups with an ophthalmologist")

#     print("\nType 'exit' to end conversation.\n")

#     if user == "exit":
#         break


from difflib import get_close_matches

# -------------------- STAGE DATA --------------------
stages = {
    "0": "No Diabetic Retinopathy detected.",
    "1": "Mild Diabetic Retinopathy.",
    "2": "Moderate Diabetic Retinopathy.",
    "3": "Severe Diabetic Retinopathy.",
    "4": "Proliferative Diabetic Retinopathy."
}

def get_stage_advice(stage):
    advice = {
        "0": "Maintain healthy lifestyle and yearly checkups.",
        "1": "Control blood sugar and monitor regularly.",
        "2": "Consult an eye specialist soon.",
        "3": "Immediate medical attention required.",
        "4": "Urgent treatment required."
    }
    return advice.get(stage, "Unknown stage")

# -------------------- SYMPTOMS --------------------
symptom_map = {
    "blurred vision": ["blur", "unclear", "foggy"],
    "floaters": ["floaters", "spots", "dots"],
    "night vision issue": ["night", "dark"],
    "eye strain": ["strain", "tired", "pain"]
}

def detect_symptoms(user_input):
    detected = []
    words = user_input.split()

    for symptom, keywords in symptom_map.items():
        for word in words:
            if get_close_matches(word, keywords, n=1, cutoff=0.7):
                detected.append(symptom)
                break

    return detected

# -------------------- TARGETED ADVICE --------------------
def give_targeted_advice(symptoms):
    print("\nDoctor Bot: Based on your symptoms, here are some suggestions:")

    if "blurred vision" in symptoms:
        print("- Control blood sugar strictly")

    if "floaters" in symptoms:
        print("- Monitor sudden increase in floaters")

    if "night vision issue" in symptoms:
        print("- Avoid driving at night")

    if "eye strain" in symptoms:
        print("- Follow 20-20-20 rule")

    print("\nGeneral Precautions:")
    print("- Eat Vitamin A, C rich foods")
    print("- Avoid sugar spikes")
    print("- Regular eye checkups")

    print("\nLifestyle Tips:")
    print("- Daily walking")
    print("- Proper sleep")
    print("- Eye relaxation exercises")

# -------------------- RISK --------------------
def calculate_risk(stage, symptoms):
    score = int(stage) + len(symptoms)

    print(f"\nRisk Score: {score}")

    if score <= 2:
        print("Risk Level: LOW")
    elif score <= 4:
        print("Risk Level: MODERATE")
    else:
        print("Risk Level: HIGH")

    return score

# -------------------- EXIT NLP --------------------
def is_exit(user):
    return any(word in user for word in ["no", "thanks", "thank", "bye"])

def is_yes(user):
    return any(word in user for word in ["yes", "yeah", "yep"])

# -------------------- MAIN --------------------
def chatbot():
    stage = input("Enter CNN Prediction (0-4): ")

    print("\n--- Virtual Retinal Assistant ---\n")
    print(f"Report: {stages.get(stage)}")
    print(get_stage_advice(stage))

    # -------- STEP 1: COLLECT SYMPTOMS --------
    print("\nTell me your symptoms (type 'done' when finished):")

    symptoms_memory = set()

    while True:
        user = input("Patient: ").lower()

        if user == "done":
            break

        detected = detect_symptoms(user)

        if detected:
            for s in detected:
                symptoms_memory.add(s)
                print(f"Doctor Bot: Noted {s}")
        else:
            print("Doctor Bot: Please describe symptoms more clearly")

    # -------- STEP 2: ANALYSIS --------
    if symptoms_memory:
        print(f"\nYou reported: {', '.join(symptoms_memory)}")

    give_targeted_advice(symptoms_memory)
    calculate_risk(stage, symptoms_memory)

    # -------- STEP 3: FOLLOW-UP LOOP --------
    while True:
        print("\nDoctor Bot: Do you need further assistance? (yes/no)")
        user = input("Patient: ").lower()

        if is_exit(user):
            print("\nDoctor Bot: Take care! Stay healthy 👋")
            break

        elif is_yes(user):
            print("\nDoctor Bot: Please tell me more about your concerns.")
            user_input = input("Patient: ").lower()

            detected = detect_symptoms(user_input)

            if detected:
                for s in detected:
                    print(f"Doctor Bot: Noted {s}")
            else:
                print("Doctor Bot: I understand. Please consult a doctor if unsure.")

        else:
            print("Doctor Bot: Please answer with yes or no.")

# -------------------- RUN --------------------
chatbot()