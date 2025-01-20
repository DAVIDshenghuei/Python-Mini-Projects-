import time
import random
 
# To get all Divisors of N
def get_divisor(n):
	
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)


if __name__ =='__main__':
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    total = 0
    correct = 0
    questions = []
    # while seconds is less than 60
    while time.time() - start_time <= 60:
        a = random.randint(1, 99)
        op = random.choice(ops)
        if op == '/':
            # if op is '/' then b is a divisor of a
            b = get_divisor(a)
        else:
            b = random.randint(1, 99)
        # Get the correct answer
        a_op_b = '{}{}{}'.format(a, op, b)
        c = eval(a_op_b)

        # Let user input answer
        try:
            ans = input('{} = '.format(a_op_b))
	# the format is a ['+', '-', '*', '/'] b = ans
        except:
            ans = ''
		
        # To check if correct or not
        if time.time() - start_time <= 60: 
            if c == ans:
                print('Correct! Time remain {} seconds.'.format(int(60 - (time.time() - start_time))))
                correct = correct + 1
            else:
                print('Wrong answer! Time remain {} seconds.'.format(int(60 - (time.time() - start_time))))
            total = total + 1
            questions.append('{}={}'.format(a_op_b, ans))

    #check the correct rate
    print('{} questions and your correct rate is {:.2f}%'.format(total, correct / total * 100))
    # Repeat all questions and responses
    for q in questions:
        print(q)
