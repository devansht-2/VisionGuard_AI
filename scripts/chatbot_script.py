stage = input("Enter CNN Prediction (0-4): ")

stages = {
    "0": "No Diabetic Retinopathy detected.",
    "1": "Mild Diabetic Retinopathy.",
    "2": "Moderate Diabetic Retinopathy.",
    "3": "Severe Diabetic Retinopathy.",
    "4": "Proliferative Diabetic Retinopathy."
}

print("\n--- Virtual Retinal Assistant ---\n")

print("Doctor Bot:")
print(f"I have received your retinal screening report. It indicates: {stages.get(stage,'Unknown stage')}")

print("\nI would like to understand how you are feeling.")
print("Are you experiencing blurred vision, floaters, eye strain, or difficulty seeing at night?\n")

while True:
    user = input("Patient: ").lower()

    if "blur" in user or "vision" in user:
        print("\nDoctor Bot:")
        print("Blurred vision can occur when blood sugar affects the small blood vessels in the retina.")
    
    if "pain" in user:
        print("\nDoctor Bot:")
        print("Eye discomfort may occur due to strain or dryness. It is recommended to rest the eyes and maintain hydration.")

    print("\nPrecautions you should follow:")

    print("- Maintain stable blood sugar levels")
    print("- Eat foods rich in Vitamin A, C and Omega-3")
    print("- Include spinach, carrots, oranges, almonds and fish in diet")
    print("- Avoid excessive sugar and processed food")
    print("- Take breaks from screens every 20 minutes")
    print("- Maintain regular sleep schedule")

    print("\nLifestyle Tips:")
    print("- Gentle eye relaxation exercises")
    print("- Regular walking to control diabetes")
    print("- Annual retinal check-ups with an ophthalmologist")

    print("\nType 'exit' to end conversation.\n")

    if user == "exit":
        break