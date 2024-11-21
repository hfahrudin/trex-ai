# T-Rex Run AI with Deep Reinforcement Learning

<p align="center">
  <img width="400" height="200" src="https://user-images.githubusercontent.com/25025173/48309312-c7419d80-e5a9-11e8-9f1f-d8db31396eeb.gif">
</p>

The T-Rex Run, or Dinosaur Game, is a simple yet iconic endless runner game appearing as an Easter egg in Google Chrome when your internet connection is down. Players control a dinosaur, jumping or ducking to avoid obstacles in an infinite desert landscape. This project explores how to train an AI agent to play the game using **Deep Q-Networks (DQN)**, a method in **Deep Reinforcement Learning**.

---

## Why This Approach?

In most reinforcement learning projects, environments often provide state variables directly, such as player position or obstacle distances. While efficient, this approach gives the AI access to "hidden" information unavailable to human players.

Here, I explored a different question: **What if the AI learns to play the game based solely on visual inputs, like humans do?** By capturing and processing screenshots of the game, the AI learns to interpret the environment visually, without relying on direct access to game state variables. This approach provides a more challenging and human-like learning scenario for the agent.

---

## Approach

### Environment Setup

The environment is directly taken from the browser-based game. I used:

- **[PyScreenshot](https://pypi.org/project/pyscreenshot/)**: To capture game visuals in real-time.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)**: To simulate keyboard inputs (e.g., jump, duck).

The agent can perform three actions:  
1. **Jump**  
2. **Duck**  
3. **Do Nothing**

#### Reward Mechanism

To train the AI using **DQN**, I defined rewards and punishments as follows:
1. **Punishment**: If the "GAME OVER" screen is detected, the agent is penalized.  
2. **Reward**: The agent receives incremental rewards for each action that prolongs survival.

#### Visual Preprocessing

Before feeding screenshots into the AI model, they are processed using **edge detection** to remove unnecessary features and highlight obstacles. This step simplifies the environment while retaining essential gameplay elements.

<p align="center">
  <img width="400" height="200" src="https://user-images.githubusercontent.com/25025173/48309928-1db4d900-e5b6-11e8-9e66-6ad538899c5e.png">
</p>
<p align="center">Edge detection using <a href="https://opencv.org/">OpenCV</a></p>

---

### AI Model and Training

I used a **Convolutional Neural Network (CNN)** to process the edge-detected screenshots and predict the optimal action. The agent's training leveraged the **Experience Replay** algorithm, enabling it to store past experiences and learn from them in batches for improved stability and performance.

---

## Results

After approximately **6 hours** of training, the AI began to show noticeable improvements in gameplay. Below is a performance graph showing the average number of actions executed per run over time.

<p align="center">
  <img width="400" height="200" src="https://user-images.githubusercontent.com/25025173/48310063-720d8800-e5b9-11e8-986e-4ede699878f7.png">
</p>
<p align="center">Average actions per run after 6 hours of training</p>

---

## Reflections and Future Improvements

This project was an exciting experiment at the time, but as with any older project, there are potential areas for improvement, such as:

- **Accelerating the Jump Start:** The agent takes time to "get the hang of it" during initial training. Techniques like **curriculum learning** or **behavior cloning** from pre-collected expert data could give the agent a head start.  
- **Optimizing Visual Input:** Modern methods like using **saliency maps** could help the agent focus on the most critical parts of the visual input.  
- **Exploration Strategies:** Introducing more advanced exploration techniques like **epsilon decay scheduling** or **noisy networks** might speed up learning.

Feel free to experiment with these ideas to push the boundaries of this project further!

---

## Requirements

To run this project, you'll need the following dependencies:

1. **OpenCV** (version 3.4.3.18)  
2. **PyAutoGUI** (version 0.9.38)  
3. **PyScreenshot** (version 0.4.2)  
4. **PyTorch** (version 0.4.1)  
---

## How to Run

Follow these steps to set up and run the project:

1. **Open the T-Rex Game**  
   Open Google Chrome and go to **chrome://dino**, or disconnect your internet to access the game.

2. **Adjust the Bounding Box**  
   In `t_rex_env.py`, modify the `bbox` (bounding box) variable to fit your game window's position and size.

3. **Run the Script**  
   Execute the `t_rex_env.py` script to start the game and train the AI:

```bash
python t_rex_env.py
```

---

## License

This project is licensed under the [MIT License](LICENSE).
