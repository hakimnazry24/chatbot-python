import random
R_EATING = 'I do not eat anything because I am a bot obviously!'

def unknown():
    response = [
        'Could you please rephrase that?',
        'Sounds about right', 
        '...',
        'What does that mean?'
    ][random.randrange(4)]

    return response
