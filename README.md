# ✋🎛️ Hand Gesture-Based Volume Control

## 🌟 Overview ✨
The **Hand Gesture-Based Volume Control** project enables users to 🎚️ control or adjust the system volume using simple 🤌 hand gestures. By leveraging **🤖 MediaPipe** for hand tracking and **🔊 PyCaw** for audio control, this project showcases an intuitive, touch-free way to manage 🔈 volume levels. The program 📹 captures hand movements through a 📷 webcam and maps the distance between specific ✋ hand landmarks to adjust the 🎶 volume.

---

## 🛠️ Features 🔧🌟
- **🙌 Touch-Free Volume Control**: Adjust the 🔉 volume of your system by simply moving your 🤏 fingers.
- **⏱️ Real-Time Hand Tracking**: Tracks ✋ hand gestures with high accuracy using 🤖 MediaPipe.
- **📊 Interactive Visual Feedback**: Displays volume percentage 🔢 and real-time 🎥 visual indicators for user interaction.
- **⚡ Performance Metrics**: Displays 🕒 FPS (frames per second) to monitor application performance.

---

## 🖥️ Technologies Used 💻🔍🛠️
- **🐍 Python**: Programming language used for development.
- **🤖 MediaPipe**: For ✋ hand landmark detection and tracking.
- **🔊 PyCaw**: For accessing and controlling system 🎵 audio endpoints.
- **📷 OpenCV**: For 📹 webcam access and 🖼️ image processing.
- **📐 NumPy**: For mathematical operations like 📉 interpolation.

---

## 📥 Installation 📦⚙️
1. 🧪 Clone this repository:
   ```bash
   git clone https://github.com/Tejasva-Maurya/Hand-Gesture-Volume-Control.git
   cd Hand-Gesture-Volume-Control
   ```
2. 📦 Install the required dependencies:
   ```bash
   pip install opencv-python mediapipe pycaw numpy comtypes
   ```
3. ▶️ Run the program:
   ```bash
   python main.py
   ```

---

## 🛠️ How It Works 🧠🤹‍♂️

1. **📷 Webcam Input**: The program captures 📹 video frames using OpenCV.
2. **✋ Hand Tracking**: 🤖 MediaPipe detects and tracks hand 🖖 landmarks in the video stream.
3. **🤏 Gesture Detection**:
   - Detects the position of the 👍 thumb and 🖕 index finger.
   - Calculates the distance between these two fingers.
   - Interpolates the distance to map it to a 🔈 volume range.
4. **🎚️ Volume Control**:
   - Uses 🔊 PyCaw to adjust the system 🔈 volume based on the calculated distance.
5. **🎥 Visual Feedback**:
   - Displays a 📏 rectangle representing the current 🔊 volume level.
   - Shows 🕒 FPS and other interactive 🎨 elements for user feedback.

---

## 🧩 Code Explanation 📝🔍
### 🧱 Key Components 🔑🛠️

#### 1. **✋ Hand Tracking**
- `detector = htm.handDetector(maxhands=1, detectionCon=0.8, trackingCon=0.8)`
  - Initializes the ✋ hand detection module with parameters for 🎯 accuracy and tracking 🔗 confidence.
- `lmList = detector.findPosition(img, draw=False)`
  - Extracts the list of ✋ hand landmarks detected in the 🎥 frame.

#### 2. **🔢 Volume Calculation**
- `length = math.hypot(x2 - x1, y2 - y1)`
  - Calculates the 📏 Euclidean distance between the 👍 thumb and 🖕 index finger.
- `vol = np.interp(length, [30, 300], [minVol, maxVol])`
  - Maps the 🤌 finger distance to the system 🔈 volume range using 📉 interpolation.

#### 3. **🎛️ Volume Adjustment**
- `volume.SetMasterVolumeLevel(vol, None)`
  - Adjusts the system 🎶 volume using 🔊 PyCaw.

#### 4. **📊 Visual Feedback**
- Displays the 🎚️ volume bar and percentage 🔢 on the 🖥️ screen.
- Highlights the interaction point between 🤏 fingers with 🎨 colored circles.

---

## 💡 Use Cases 🔍💡
- **♿ Accessibility**: Provides an alternative input method for individuals with limited mobility.
- **🧼 Touch-Free Interaction**: Useful in scenarios where physical interaction with devices is inconvenient or unhygienic.
- **🎮 Gaming and Multimedia**: Offers a modern, intuitive way to control 🔊 audio during 🎮 gaming or media playback.

---

## 🚀 Future Potential 🔮🚀
1. **🙌 Multi-Gesture Support**:
   - Implement additional gestures for functionalities like ▶️ play, ⏸️ pause, or 🌞 brightness adjustment.
2. **🎙️ Voice Command Integration**:
   - Combine with 🎤 voice commands for a multimodal 🎛️ interaction system.
3. **💻 Cross-Platform Compatibility**:
   - Extend support to 🖥️ macOS and 🐧 Linux systems.
4. **🔍 Advanced Tracking**:
   - Use depth sensors for more accurate ✋ hand tracking in 🌑 low-light conditions.
5. **📝 Customizable Gesture Library**:
   - Allow users to define and train their own ✋ gestures.

---

## ⚠️ Limitations ⚡⚠️
- Relies on adequate 🌞 lighting for accurate ✋ hand tracking.
- Requires a high-quality 📷 webcam for optimal performance.
- May not work seamlessly in environments with 🎨 complex backgrounds.

---

## 📜 License ⚖️📄📝
This project is licensed under the MIT License. Feel free to use, modify, and distribute the software according to the terms of this license.

---

## 🙏 Acknowledgments 🙌📚🎓
- [🤖 MediaPipe Documentation](https://ai.google.dev/edge/mediapipe/solutions/guide)
- [🔊 PyCaw Documentation](https://github.com/AndreMiras/pycaw)
- 📷 OpenCV and 🐍 Python communities for extensive support and resources.

