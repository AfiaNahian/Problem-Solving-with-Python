money=float(input())
note=money
note_100=note/100
note_50=(note%100)/50
note_20=((note%100)%50)/20
note_10=(((note%100)%50)%20)/10
note_5=((((note%100)%50)%20)%10)/5
note_2=(((((note%100)%50)%20)%10)%5)/2

print("NOTAS:")
print(f"{int(note_100)} nota(s) de R$ 100.00")
print(f"{int(note_50)} nota(s) de R$ 50.00")
print(f"{int(note_20)} nota(s) de R$ 20.00")
print(f"{int(note_10)} nota(s) de R$ 10.00")
print(f"{int(note_5)} nota(s) de R$ 5.00")
print(f"{int(note_2)} nota(s) de R$ 2.00")

coin_1=(((((note%100)%50)%20)%10)%5)%2
coin=money*100
coin=(int(coin))
coin_50=(coin%100)/50
coin_25=((coin%100)%50)/25
coin_10=(((coin%100)%50)%25)/10
coin_05=((((coin%100)%50)%25)%10)/5
coin_01=((((coin%100)%50)%25)%10)%5

print(f"MOEDAS:")
print(f"{int(coin_1)} moeda(s) de R$ 1.00")
print(f"{int(coin_50)} moeda(s) de R$ 0.50")
print(f"{int(coin_25)} moeda(s) de R$ 0.25")
print(f"{int(coin_10)} moeda(s) de R$ 0.10")
print(f"{int(coin_05)} moeda(s) de R$ 0.05")
print(f"{int(coin_01)} moeda(s) de R$ 0.01")