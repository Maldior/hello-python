# A sample module to test importing functions"

def score_calculator(seconds_played, obstacles_cleared):
    return seconds_played * obstacles_cleared 

def hi_score_checker(current_score, hi_score):
    if current_score >= hi_score:
        print('NEW HIGH-SCORE: ' + str(current_score))
    else:
        print('Score: ' + str(current_score))
        