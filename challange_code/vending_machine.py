print(f"\nVending Machine\n------------------------")
amount_due = 50
while(True):
    try: 
        print(f"Amount due: {amount_due}")
        coin_inserted = int(input("\nInsert Coin: "))
        if coin_inserted == 5 or coin_inserted == 1 or coin_inserted == 10 or coin_inserted == 25:
            amount_due = amount_due - coin_inserted
            if amount_due <= 0:
                break
        else:
            continue
    except:
        continue

print(f"\nChange: {amount_due * -1}")
