# Hand and Face Detection with Multi-task Functionality

This project leverages advanced computer vision technologies to create a system capable of detecting hand gestures, recognizing faces, identifying emotions and gender, and triggering context-based actions. It's built using TensorFlow, OpenCV, and MediaPipe, combining AI and real-time processing.

## Features

- **Hand Gesture Recognition**: Detects and tracks hand gestures in real-time.
- **Face Detection and Recognition**:
  - Identifies specific individuals from a predefined list.
  - Predicts emotions (e.g., Neutral, Happy).
  - Determines gender classification.
- **Gesture-based Actions**:
  - Maps gestures to specific actions like turning on LEDs or moving forward.
  - Plays personalized music based on recognized faces and emotions.
- **Real-time Processing**: Operates efficiently with live camera input.

## How It Works

1. **Hand Detection**:  
   - Uses MediaPipe to detect hand landmarks.
   - Counts the number of raised fingers and maps gestures to actions.

2. **Face Detection**:  
   - Utilizes OpenCV's Haar Cascade Classifier for face detection.
   - Resizes detected faces for emotion, gender, and individual recognition.

3. **Emotion and Gender Prediction**:  
   - A TensorFlow model predicts emotions and gender.
   - Outputs are mapped to corresponding classes.

4. **Action Mapping**:  
   - Specific gestures trigger corresponding actions.
   - Plays songs personalized for detected individuals when emotions indicate happiness.

## Gesture Mapping

| Gesture | Action          |
|---------|-----------------|
| 0       | STOP            |
| 1       | STOP            |
| 2       | TURN ONE        |
| 3       | LED ON          |
| 4       | BUZZER ON       |
| 5       | FORWARD         |


