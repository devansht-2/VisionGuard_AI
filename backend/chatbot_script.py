# backend/chatbot_script.py

def get_response(stage, user_message):
    stages = {
        "0": "No Diabetic Retinopathy detected.",
        "1": "Mild Diabetic Retinopathy.",
        "2": "Moderate Diabetic Retinopathy.",
        "3": "Severe Diabetic Retinopathy.",
        "4": "Proliferative Diabetic Retinopathy."
    }

    response = []

    if user_message == "start":
        response.append(f"I have received your retinal screening report. It indicates: {stages.get(stage,'Unknown stage')}")
        response.append("Are you experiencing blurred vision, floaters, eye strain, or difficulty seeing at night?")
        return "\n".join(response)

    user = user_message.lower()

    if "blur" in user or "vision" in user:
        response.append("Blurred vision can occur when blood sugar affects the small blood vessels in the retina.")

    if "pain" in user:
        response.append("Eye discomfort may occur due to strain or dryness. It is recommended to rest the eyes and maintain hydration.")

    response.append("\nPrecautions you should follow:")
    response.append("- Maintain stable blood sugar levels")
    response.append("- Eat foods rich in Vitamin A, C and Omega-3")
    response.append("- Include spinach, carrots, oranges, almonds and fish in diet")
    response.append("- Avoid excessive sugar and processed food")
    response.append("- Take breaks from screens every 20 minutes")
    response.append("- Maintain regular sleep schedule")

    response.append("\nLifestyle Tips:")
    response.append("- Gentle eye relaxation exercises")
    response.append("- Regular walking to control diabetes")
    response.append("- Annual retinal check-ups with an ophthalmologist")

    return "\n".join(response)