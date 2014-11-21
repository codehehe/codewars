def grader(score):
    grader = ''
    if score >= 0.9 and score <= 1:
        grader = 'A'
    elif score >= 0.8 and score < 0.9:
        grader = 'B'
    elif score >= 0.7 and score < 0.8:
        grader = 'C'
    elif score >= 0.6 and score < 0.7:
        grader = 'D'
    else:
        grader = 'F'
    return grader

def grader_nice(score):
    ''' 网上一哥们非常漂亮的解决方案 '''
    return 'F' if score > 1 or score < 0.6 else 'ABCD'[int(10 * (0.999 - score))]
