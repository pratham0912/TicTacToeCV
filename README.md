# Tic Tac Toe with OpenCV

A live Tic Tac Toe game implemented in **Python** using **OpenCV**. The game runs on a **webcam feed**, allowing two players to click on the cells to place **O** and **X**. The game includes winner and tie detection, click-blocking after game over, and a reset option.

---

## **Features**

- 3×3 Tic Tac Toe grid drawn dynamically on live webcam feed  
- Click to place **O** or **X** in empty cells  
- Automatic winner detection for rows, columns, and diagonals  
- Tie detection when all cells are filled  
- Game reset with **`r`** key  
- Quit the game with **`q`** key  
- Blocks further clicks after the game ends  

---

## **How to Run**

1. Ensure you have **Python 3** installed.  
2. Install OpenCV:

```bash
pip install opencv-python
