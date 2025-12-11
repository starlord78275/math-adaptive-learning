class AdaptiveEngine:
    """
    ML-style adaptive engine using a skill score system.
    This is a reinforcement-learning inspired approach where we maintain
    a numerical skill score and adjust it based on performance.
    """
    
    def __init__(self, initial_difficulty='medium'):
        """
        Initialize the adaptive engine.
        
        Args:
            initial_difficulty (str): Starting difficulty level
        """
        difficulty_to_score = {
            'easy': 25,
            'medium': 50,
            'hard': 75
        }
        
        self.skill_score = difficulty_to_score.get(initial_difficulty, 50)
        self.difficulty_history = [initial_difficulty]
    
    def update_skill_score(self, is_correct, time_taken, current_difficulty):
        """
        Update the skill score based on performance (this is the ML part!).
        
        Args:
            is_correct (bool): Whether the answer was correct
            time_taken (float): Seconds taken to answer
            current_difficulty (str): Current difficulty level
        
        Returns:
            float: Updated skill score
        """
        
        time_thresholds = {
            'easy': 5.0,      
            'medium': 8.0,    
            'hard': 12.0      
        }
        
        threshold = time_thresholds.get(current_difficulty, 8.0)
        
        
        if is_correct:
            if time_taken < threshold:
                score_change = 8
            else:
                score_change = 4
        else:
            if time_taken < threshold:
                score_change = -6
            else:
                score_change = -10
        
        
        self.skill_score += score_change
        self.skill_score = max(0, min(100, self.skill_score))
        return self.skill_score
    
    def get_next_difficulty(self):
        """
        Determine next difficulty based on current skill score.
        This maps the numerical skill score to discrete difficulty levels.
        
        Returns:
            str: 'easy', 'medium', or 'hard'
        """
        if self.skill_score < 35:
            difficulty = 'easy'
        elif self.skill_score < 70:
            difficulty = 'medium'
        else:
            difficulty = 'hard'
        
        self.difficulty_history.append(difficulty)
        
        return difficulty
    
    def get_recommended_level(self):
        """
        Get recommended difficulty for next session based on final skill score.
        
        Returns:
            str: Recommended difficulty level
        """
        if self.skill_score < 35:
            return 'easy'
        elif self.skill_score < 70:
            return 'medium'
        else:
            return 'hard'
    
    def get_skill_score(self):
        """
        Get current skill score.
        
        Returns:
            float: Current skill score (0-100)
        """
        return self.skill_score
    
    def get_difficulty_history(self):
        """
        Get the history of difficulty changes.
        
        Returns:
            list: All difficulty levels used in order
        """
        return self.difficulty_history
