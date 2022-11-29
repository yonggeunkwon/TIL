import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)  # 정수들이 __init__()으로 전달된다.
print(purse)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print('Total value:', purse.value())
print('Weight:', purse.weightInGrams(), 'grams')
print()

coinjar = wizcoin.WizCoin(13, 0, 0)  # 정수들이 __init__()으로 전달된다.
print(coinjar)
print('G:', coinjar.galleons, 'S:', coinjar.sickles, 'K:', coinjar.knuts)
print('Total value:', coinjar.value())
print('Weight:', coinjar.weightInGrams(), 'grams')

