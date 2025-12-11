from adaptive_engine import AdaptiveEngine

# Create engine starting at medium
engine = AdaptiveEngine('medium')
print(f"Starting skill score: {engine.get_skill_score()}")

# Simulate some performance
# Good performance - should increase difficulty
engine.update_skill_score(True, 3.0, 'medium')  # Correct, fast
print(f"After correct+fast: {engine.get_skill_score()}")

engine.update_skill_score(True, 4.0, 'medium')  # Correct, fast
print(f"After another correct+fast: {engine.get_skill_score()}")

print(f"Next difficulty: {engine.get_next_difficulty()}")

# Bad performance - should decrease
engine.update_skill_score(False, 10.0, 'hard')  # Wrong, slow
print(f"After wrong+slow: {engine.get_skill_score()}")

print(f"Next difficulty: {engine.get_next_difficulty()}")

print(f"\nDifficulty history: {engine.get_difficulty_history()}")
