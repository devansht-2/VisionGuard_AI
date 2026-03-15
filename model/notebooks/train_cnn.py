import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ======================
# SETTINGS
# ======================
IMAGE_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 40

# ======================
# LOAD CSV
# ======================
df = pd.read_csv("D:\\data\\dr_data\\diabetic-retinopathy-detection\\trainLabels.csv")

# Add .jpeg extension
df["image"] = df["image"] + ".jpeg"

# ======================
# TRAIN VALID SPLIT
# ======================
train_df, val_df = train_test_split(
    df,
    test_size=0.2,
    stratify=df["level"],
    random_state=42
)

# Convert labels to string for categorical mode
train_df["level"] = train_df["level"].astype(str)
val_df["level"] = val_df["level"].astype(str)

# ======================
# DATA GENERATORS
# ======================
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_df,
    directory="D:\\data\\dr_data\\diabetic-retinopathy-detection\\train",
    x_col="image",
    y_col="level",
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

val_generator = val_datagen.flow_from_dataframe(
    dataframe=val_df,
    directory="D:\\data\\dr_data\\diabetic-retinopathy-detection\\train",
    x_col="image",
    y_col="level",
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

# ======================
# BUILD SIMPLE CNN
# ======================
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3)),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),

    layers.Dense(5, activation='softmax')
])

# ======================
# COMPILE
# ======================
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ======================
# TRAIN
# ======================
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS
)

# ======================
# SAVE MODEL
# ======================
model.save("dr_model1.keras")

print("Model training completed and saved!")
