import random
"""
--> asking user how many times he/she wants to flip the coin
    based on that using random function to flip the coin 
    and coin how many times head/tail is obtained and print its percentage
"""
results = {
    'heads': 0,
    'tails': 0,
}
head_tail = list(results.keys())

flip_coin = int(input("Enter number of times you want to flip the coin"))
for i in range(flip_coin):
    results[random.choice(head_tail)] += 1

if __name__ == '__main__':
    print('Heads:', results['heads'], ",", 'Head Percentage: ', (results['heads']/flip_coin*100), '%')
    print('Tails:', results['tails'], ",", 'Tail Percentage: ', (results['tails']/flip_coin*100), '%')