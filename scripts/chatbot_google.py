import google.generativeai as genai

genai.configure(api_key="AIzaSyCiNtCSITjEl3DPykX1n8C2_XBp757k8eQ")

model = genai.GenerativeModel("models/gemini-2.5-pro")

stage = input("Enter CNN Prediction (0-4): ")

stage_desc = {
    "0": "No Diabetic Retinopathy detected.",
    "1": "Mild Diabetic Retinopathy.",
    "2": "Moderate Diabetic Retinopathy.",
    "3": "Severe Diabetic Retinopathy.",
    "4": "Proliferative Diabetic Retinopathy."
}

report = stage_desc.get(stage, "Unknown stage")

system_prompt = f"""
You are a virtual retinal health assistant.

A CNN model analyzed the patient's retinal scan and produced this report:
{report}

Start the conversation by saying:
"I have received your retinal screening report."

Then ask the patient about their symptoms.

Provide helpful guidance including:
- eye health precautions
- lifestyle improvements
- diet suggestions for diabetic patients
- when to consult an ophthalmologist

Do not prescribe medicines. Give general guidance only.
"""

chat = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]},
    {"role": "model", "parts": ["Hello, I have received your retinal screening report. How are your eyes feeling today?"]}
])

print("\n--- Virtual Retinal Assistant ---\n")

while True:
    user = input("Patient: ")

    if user.lower() == "exit":
        break

    response = chat.send_message(user)

    print("\nDoctor Bot:", response.text)