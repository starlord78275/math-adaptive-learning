import time

class SessionTracker:
    """
    Tracks user performance during a learing session.
    Store all the attempts and calculates statistics.

    """
    def __init__(self):
        """Initialize an empty tracker"""
        self.attempts = []

    def add_attempt(self, question, user_answer, correct_answer, time_taken, difficulty):
        """
        add a new attempt to the tracker.

        Args:
            question (str): The math question asked
            user_answer (int): what the user answerd
            correct-answer (int): the correct answer
            time_taken (float): Seconds taken to answer
            difficulty (str): 'easy', 'medium', or 'hard'
        """
        is_correct = (user_answer == correct_answer)

        attempt = {
            'question': question,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
            'time_taken': time_taken,
            'difficulty': difficulty
        }

        self.attempts.append(attempt)
    
    def get_recent_results(self, n=5):
        """
        GEt the last n attempts.

        Args:
            n (int): Number of recent attempts to return

        Returns: 
            list: Last n attempts (or fewer if not enough attempts yet)

        """

        return self.attempts[-n:] if len(self.attempts) >= n else self.attempts
    
    def get_summary(self):
        """
        Calculate session statistics.

        Returns:
            dict: Statistics about the session
        """

        if len(self.attempts) == 0:
            return {
                'total_questions': 0,
                'correct': 0,
                'accuracy': 0.0,
                'avg_time': 0.0,
                'difficulty_counts': {'easy': 0, 'medium': 0, 'hard': 0}
            }
        correct_count = sum(1 for attempt in self.attempts if attempt['is_correct'])
        accuracy = (correct_count / len(self.attempts)) * 100
        total_time = sum(attempt['time_taken'] for attempt in self.attempts)
        avg_time = total_time / len(self.attempts)
        difficulty_counts = {
            'easy': 0,
            'medium': 0,
            'hard': 0
        }
        for attempt in self.attempts:
            difficulty_counts[attempt['difficulty']] += 1
        
        return {
            'total_questions': len(self.attempts),
            'correct': correct_count,
            'accuracy': accuracy,
            'avg_time': avg_time,
            'difficulty_counts': difficulty_counts
        }
    def get_all_attempts(self):
        """
        Get all attempts made in this session.

        Returns:
            list: All attempt records
        """
        return self.attempts