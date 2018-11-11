<p align="center">
  <img width="400" height="200" src="https://user-images.githubusercontent.com/25025173/48309312-c7419d80-e5a9-11e8-9f1f-d8db31396eeb.gif">
</p>

T-rex run or dinausaur game is an endless runner game that everyone known as "easter egg" when your connection down. This game is simple infinite runner, which you either jump or duck to avoid obstacle. The controls are really simple but the idea of putting this kind of "kill time" game is really intriguing. This game is perfect environment to implement an AI with [Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) method. Let's dive into my approach on it.

### Environment and AI
I used the game directly from browser game as environment rather than i make the game myself. I use [pyscreenshot](https://pypi.org/project/pyscreenshot/) to capture the game and [pyautogui](https://pyautogui.readthedocs.io/en/latest/) to input actions to the game.The actions that agent can do is long jump, duck, and do nothing. To implement DQN we should determine reward and punishment, here is what i do:
1. Get punished if "GAME OVER" logo detected.
2. Increase reward in each action

Before feeding to the brain, i would like to preprocess the screen with edge detection to reduce unnecessary feature.
<p align="center">
  <img width="400" height="200" src="https://user-images.githubusercontent.com/25025173/48309928-1db4d900-e5b6-11e8-9e66-6ad538899c5e.png">
</p>
<p align="center">Edge detector using <a href="https://opencv.org/">opencv</a></p>

I fed the processed image into CNN with the output represent the action. I use experience replay algorithm so the agent can learn the environment better. 

## Result
Here is the result after 6 hour training

<p align="center">
  <img width="400" height="200" src="https://user-images.githubusercontent.com/25025173/48310063-720d8800-e5b9-11e8-986e-4ede699878f7.png">
</p>
<p align="center">Average executed action per run</p>


### Requirement
1. opencv 3.4.3.18 
2. pyautogui 0.9.38 
3. pyscreenshot 0.4.2 
4. pytorch 0.4.1

### How to run

Step 1 : Open t-rex run game 

Step 2 : Change `bbox` on `t_rex_env.py` to fit your game window

Step 3 : Run `t_rex_env.py`
