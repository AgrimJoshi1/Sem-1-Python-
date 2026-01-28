class AgeException(Exception):
    pass 
try: 
    age = int(input())
    if age < 18: 
        raise AgeException('Age is too low to vote')
    else: 
        print('Eligible to vote')
except AgeException as e: 
    print(f'eror: {e}')     