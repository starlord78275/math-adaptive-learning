```markdown
#  Math Adventures – Adaptive Learning

An AI-powered adaptive math learning prototype that adjusts question difficulty in real time based on learner performance. Designed for children aged 5–10 to practice basic arithmetic while staying in their optimal challenge zone.

Repository: https://github.com/starlord78275/math-adaptive-learning.git

##  Objective

This project implements a minimal adaptive learning system that:

- Generates simple math puzzles at three difficulty levels (Easy, Medium, Hard).
- Tracks learner performance (correctness and response time).
- Automatically adapts the next question’s difficulty using a lightweight ML-inspired model.
- Provides an end-of-session performance summary with key metrics.

The focus is on the **adaptive logic and reasoning**, not on complex UI or visuals. [file:1]

## 🏗 Project Structure

```
math-adaptive-learning/
├── README.md
├── requirements.txt
└── src/
    ├── main.py              # Streamlit app (UI + orchestration)
    ├── puzzle_generator.py  # Math puzzle generator by difficulty
    ├── tracker.py           # Session performance tracking
    └── adaptive_engine.py   # ML-style adaptive engine (skill score)
```

### Core Components

| Component           | Description                                                           |
|---------------------|-----------------------------------------------------------------------|
| `puzzle_generator`  | Generates arithmetic questions for Easy / Medium / Hard levels       |
| `tracker`           | Logs each attempt and computes summary statistics                    |
| `adaptive_engine`   | Maintains a skill score and selects the next difficulty level        |
| `main` (Streamlit)  | User interaction, question loop, feedback, and summary presentation  | [file:1]

##  Adaptive Logic (ML-Inspired)

The adaptive engine uses a **reinforcement-style skill score model**:

- Each learner has a **skill score** in the range 0–100.
- The score is updated after every question using:
  - **Correctness** (right/wrong).
  - **Response time** relative to a difficulty-specific threshold.

Typical reward / penalty scheme:

- Correct and fast → larger positive update (strong mastery signal).
- Correct but slow → smaller positive update.
- Wrong but fast → moderate penalty (possible guessing).
- Wrong and slow → larger penalty (clear struggle).

The updated skill score is then mapped to discrete difficulty levels:

- 0–34 → Easy  
- 35–69 → Medium  
- 70–100 → Hard  

This creates a simple, interpretable, ML-style adaptation loop that personalizes difficulty during the session. [file:1]

## 🖥 User Flow (Streamlit App)

1. Learner enters their **name** and chooses an initial **difficulty** (Easy/Medium/Hard).
2. The app presents a math puzzle at the current difficulty.
3. The learner submits an answer.
4. The system:
   - Measures response time.
   - Checks correctness.
   - Updates the skill score and selects the next difficulty.
   - Logs the attempt to the session tracker.
5. The next question is generated at the new difficulty level.
6. A live session summary is shown with accuracy, average time, and difficulty distribution. [file:1]

##  Metrics Tracked

The session tracker aggregates:

- Total questions attempted.
- Number of correct answers and accuracy (%).
- Average response time (seconds).
- Number of questions per difficulty level.
- Skill score and recommended level for the next session. [file:1]

## Installation and Usage

### Prerequisites

- Python 3.8+  
- pip

### Setup

```
git clone https://github.com/starlord78275/math-adaptive-learning.git
cd math-adaptive-learning
pip install -r requirements.txt
```

### Run the Application

```
streamlit run src/main.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

##  Design Rationale

- **ML-inspired skill score** instead of pure fixed rules:
  - Closer to real adaptive learning systems.
  - Provides continuous adaptation rather than hard thresholds.
  - Easy to extend later with supervised models using logged data.

- **Modular structure**:
  - Separates puzzle generation, tracking, adaptive logic, and UI.
  - Makes the code easier to understand, test, and explain in a technical note. [file:1]

##  Possible Future Work

- Persist user profiles and skill scores across sessions.
- Add more math topics (fractions, word problems, etc.).
- Visualize skill progression over time.
- Train a supervised model on collected session logs to replace manual rewards.
- Add a teacher/parent dashboard for monitoring progress. [file:1]

##  Author

**Your Name (starlord78275)**  
Adaptive Learning Assignment – Math Adventures Prototype
```
