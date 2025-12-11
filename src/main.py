import streamlit as st
import time
from puzzle_generator import generate_puzzle
from tracker import SessionTracker
from adaptive_engine import AdaptiveEngine

st.set_page_config(
    page_title="Math Adventures - Adaptive Learning",
    page_icon="🧮",
    layout="wide"
)

def initialize_session_state():
    """Initialize all session state variables if they don't exist."""
    
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    
    if 'tracker' not in st.session_state:
        st.session_state.tracker = SessionTracker()
    
    if 'engine' not in st.session_state:
        st.session_state.engine = None
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = None
    
    if 'current_answer' not in st.session_state:
        st.session_state.current_answer = None
    
    if 'current_difficulty' not in st.session_state:
        st.session_state.current_difficulty = 'medium'
    
    if 'question_start_time' not in st.session_state:
        st.session_state.question_start_time = None
    
    if 'awaiting_answer' not in st.session_state:
        st.session_state.awaiting_answer = False
    
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""
    
    if 'questions_completed' not in st.session_state:
        st.session_state.questions_completed = 0

initialize_session_state()


st.title("Math Adventures")
st.subheader("AI-Powered Adaptive Learning Prototype")

with st.sidebar:
    st.header("Session Setup")
    name = st.text_input("Enter your name:", value=st.session_state.user_name)
    if name:
        st.session_state.user_name = name
    
    initial_difficulty = st.selectbox(
        "Choose starting difficulty:",
        options=['easy', 'medium', 'hard'],
        index=1 
    )
    
    if st.button("Start New Session", type="primary"):
        st.session_state.tracker = SessionTracker()
        st.session_state.engine = AdaptiveEngine(initial_difficulty)
        st.session_state.current_difficulty = initial_difficulty
        st.session_state.initialized = True
        st.session_state.questions_completed = 0
        st.session_state.awaiting_answer = False
  
        question, answer = generate_puzzle(initial_difficulty)
        st.session_state.current_question = question
        st.session_state.current_answer = answer
        st.session_state.question_start_time = time.time()
        st.session_state.awaiting_answer = True
        
        st.success(f"Session started! Good luck, {name}! 🎉")
        st.rerun()
    
    if st.session_state.initialized and st.session_state.engine:
        st.divider()
        st.metric(
            label="Current Skill Score",
            value=f"{st.session_state.engine.get_skill_score():.0f}/100"
        )
        st.metric(
            label="Questions Completed",
            value=st.session_state.questions_completed
        )

if not st.session_state.initialized:
    st.info("👈 Enter your name and click 'Start New Session' to begin!")
    st.markdown("---")
    st.markdown("""
    ### About This App
    
    This adaptive learning system helps children practice basic math skills.
    
    **How it works:**
    - Answer math questions at your level
    - The AI tracks your performance (correctness & speed)
    - Questions automatically get harder or easier based on how you're doing
    - Uses a machine learning-inspired skill score system
    
    **Features:**
    - ✅ Three difficulty levels: Easy, Medium, Hard
    - ✅ Real-time performance tracking
    - ✅ Adaptive difficulty adjustment
    - ✅ Session statistics and analysis
    """)

else:    
    difficulty_emoji = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}
    st.markdown(f"### Current Level: {difficulty_emoji[st.session_state.current_difficulty]} {st.session_state.current_difficulty.upper()}")
    
    if st.session_state.awaiting_answer:
        st.markdown(f"## Question {st.session_state.questions_completed + 1}")
        st.markdown(f"### {st.session_state.current_question}")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            user_answer = st.number_input(
                "Your answer:",
                value=None,
                step=1,
                format="%d",
                key=f"answer_input_{st.session_state.questions_completed}"
            )
        
        with col2:
            st.write("")
            st.write("")  
            submit_button = st.button("Submit Answer", type="primary")
        
        if submit_button and user_answer is not None:
            time_taken = time.time() - st.session_state.question_start_time
            is_correct = (user_answer == st.session_state.current_answer)
            
            st.session_state.tracker.add_attempt(
                question=st.session_state.current_question,
                user_answer=user_answer,
                correct_answer=st.session_state.current_answer,
                time_taken=time_taken,
                difficulty=st.session_state.current_difficulty
            )
                        
            st.session_state.engine.update_skill_score(
                is_correct=is_correct,
                time_taken=time_taken,
                current_difficulty=st.session_state.current_difficulty
            )
            
            next_difficulty = st.session_state.engine.get_next_difficulty()
            st.session_state.current_difficulty = next_difficulty
            if is_correct:
                st.success(f"✅ Correct! The answer is {st.session_state.current_answer}")
                st.balloons()
            else:
                st.error(f"❌ Not quite. The correct answer is {st.session_state.current_answer}")
            
            st.info(f"⏱️ Time taken: {time_taken:.1f} seconds")
            if next_difficulty != st.session_state.current_difficulty:
                if next_difficulty == 'hard':
                    st.success("🎉 Great job! Moving to HARD level!")
                elif next_difficulty == 'easy':
                    st.info("💪 Let's practice some easier questions!")
                else:
                    st.info(f"📊 Adjusting to {next_difficulty.upper()} level")
            
            st.session_state.questions_completed += 1
            question, answer = generate_puzzle(next_difficulty)
            st.session_state.current_question = question
            st.session_state.current_answer = answer
            st.session_state.question_start_time = time.time()
            
            # Short delay for feedback, then continue
            time.sleep(1)
            st.rerun()

if st.session_state.initialized and st.session_state.questions_completed > 0:
    st.markdown("---")
    st.header("📊 Session Summary")
    
    summary = st.session_state.tracker.get_summary()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Questions", summary['total_questions'])
    
    with col2:
        st.metric("Correct Answers", summary['correct'])
    
    with col3:
        st.metric("Accuracy", f"{summary['accuracy']:.1f}%")
    
    with col4:
        st.metric("Avg Time", f"{summary['avg_time']:.1f}s")
    
    st.subheader("Questions by Difficulty")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🟢 Easy", summary['difficulty_counts']['easy'])
    with col2:
        st.metric("🟡 Medium", summary['difficulty_counts']['medium'])
    with col3:
        st.metric("🔴 Hard", summary['difficulty_counts']['hard'])
    
    recommended = st.session_state.engine.get_recommended_level()
    st.info(f"💡 **Recommended level for next session:** {recommended.upper()}")
    
    with st.expander("📝 View Recent Attempts"):
        recent_attempts = st.session_state.tracker.get_recent_results(10)
        for i, attempt in enumerate(reversed(recent_attempts)):
            status = "✅" if attempt['is_correct'] else "❌"
            st.write(f"{status} **Q{len(recent_attempts)-i}:** {attempt['question']} → Your answer: {attempt['user_answer']} | Time: {attempt['time_taken']:.1f}s | Level: {attempt['difficulty']}")
