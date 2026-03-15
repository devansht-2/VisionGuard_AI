import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ==========================
# 1. Paths
# ==========================
model_path = "src\\aptos_dr_model.keras"
test_csv = "E:\\AI_Project\\Data\\aptos2019-blindness-detection\\test.csv"
test_images_dir = "E:\\AI_Project\\Data\\aptos2019-blindness-detection\\test_images"

# ==========================
# 2. Load Model
# ==========================
model = tf.keras.models.load_model(model_path)
print("Model loaded successfully!")

# ==========================
# 3. Load Test Data
# ==========================
df_test = pd.read_csv(test_csv)
df_test["filename"] = df_test["id_code"] + ".png"

print("Total test images:", len(df_test))

# ==========================
# 4. Image Preprocessing
# ==========================
IMG_SIZE = 224
BATCH_SIZE = 32

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_dataframe(
    df_test,
    directory=test_images_dir,
    x_col="filename",
    y_col=None,  
    target_size=(IMG_SIZE, IMG_SIZE),
    class_mode=None,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# ==========================
# 5. Predictions
# ==========================
pred_probs = model.predict(test_generator)
pred_classes = np.argmax(pred_probs, axis=1)

# ==========================
# 6. Save Results
# ==========================

df_test["prediction"] = pred_classes
df_test.to_csv("test_predictions.csv", index=False)
print("Predictions saved to test_predictions.csv")