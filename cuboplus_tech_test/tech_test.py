def total_supply_bitcoin():
    block_reward = 50 #initial block reward in BTC
    total_btc_mined = 0 #total of bitcoin mined up to event halving
    percent_mined = 0 #percentage of bitcoin mined

    for i in range(0, 33, 1):
        total_btc_mined += block_reward * 210000
        percent_mined = total_btc_mined * 100 / 21000000
        print(f"Halving Event #{i}")
        print(f"\tTotal Bitcoin Supply: {total_btc_mined:.2f} BTC")
        print(f"\tBlock Reward: {(block_reward * 100000000):.2f} SATS")
        print(f"\tPercentage Mined: {percent_mined:.2f}%\n")
        block_reward = block_reward / 2
total_supply_bitcoin()