

<center><p>
  <img src="https://img.shields.io/badge/DOWNLOADS-1-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/RELEASE-V1.1-007EC6?style=for-the-badge">
  <img src="https://img.shields.io/badge/LAST%20COMMIT-YESTERDAY-brightgreen?style=for-the-badge">
</center></p>

<h1 align="center">Raft Auto-Fishing Bot</h1>

<p align="center">
  An automated Python bot that handles fishing in Raft, letting you focus on survival and exploration.
</p>

<p align="center">
  <a href="#-about-the-project">About</a> •
  <a href="#-features">Features</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-built-with">Tech Stack</a> •

</p>

---

![Raft Auto-Fishing Bot Demo](https://via.placeholder.com/800x450.gif?text=Fishing+Bot+in+Action!)

## 📖 About The Project

This project was created to automate the repetitive task of fishing in the game *Raft*. By using computer vision to detect the on-screen prompt, this bot allows players to gather a steady supply of food and resources passively. This frees up valuable time for players to manage their raft, explore islands, and advance through the game's story without the constant need to monitor their fishing rod.

---

## ✨ Features

* **Automatic Prompt Detection:** Uses OpenCV to accurately detect the "LMB" fish-bite icon on the screen.
* **Automated Reeling:** Simulates mouse clicks to automatically reel in the fish as soon as it's hooked.
* **Background Operation:** Runs quietly in the background with minimal performance impact.
* **User-Friendly:** Available as a simple, standalone `.exe` file that requires no installation. Just run and play.
* **Customizable:** Key parameters like screen region and detection threshold can be easily adjusted in the source code.

---

## 🚀 Getting Started

You can use this bot either as a simple executable file or by running the source code directly.

### For Users (Recommended)

The easiest way to use the bot is to download the pre-compiled executable.

1.  Go to the [**Releases**](https://github.com/YOUR_USERNAME/Raft-Auto_Fishing-V.1/releases) page of this repository.
2.  Download the latest `.exe` file (e.g., `auto_fishing.exe`).
3.  Run the `.exe` file while *Raft* is running. The bot will start automatically.
4.  To stop the bot, close the command prompt window or end the process in Task Manager.

### For Developers (Running from Source)

If you want to run or modify the source code, follow these steps.

**Prerequisites**
* Python 3.8+
* Pip

**Installation**
1.  Clone the repository to your local machine.
    ```sh
    git clone [https://github.com/YOUR_USERNAME/Raft-Auto_Fishing-V.1.git](https://github.com/YOUR_USERNAME/Raft-Auto_Fishing-V.1.git)
    ```
2.  Navigate to the project directory.
    ```sh
    cd Raft-Auto_Fishing-V.1
    ```
3.  Install the required Python libraries.
    ```sh
    pip install opencv-python pyautogui mss numpy
    ```
4.  Run the script.
    ```sh
    python auto_fishing.py
    ```

---

## 🛠️ Built With

This project was made possible by these amazing libraries:

* [![Python][Python.org]][Python-url]
* [![OpenCV][OpenCV.org]][OpenCV-url]
* [![PyAutoGUI][PyAutoGUI.com]][PyAutoGUI-url]
* [![MSS][MSS.com]][MSS-url]
* [![NumPy][NumPy.org]][NumPy-url]

---

## 📄 License

Distributed under the MIT License.
---
<p align="center">
  Built by <a href="https://github.com/YOUR_USERNAME">Miko Ard</a>
</p>

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[OpenCV.org]: https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/
[PyAutoGUI.com]: https://img.shields.io/badge/PyAutoGUI-3a3a3a?style=for-the-badge
[PyAutoGUI-url]: https://pyautogui.readthedocs.io/
[MSS.com]: https://img.shields.io/badge/MSS-4a4a4a?style=for-the-badge
[MSS-url]: https://python-mss.readthedocs.io/
[NumPy.org]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
