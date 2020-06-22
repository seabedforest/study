"""
请排列出所有扑克牌(大小王不算,使用列表存储)
["红桃","黑桃","方片","梅花"]
["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
"""
playing_card_color=["红桃","黑桃","方片","梅花"]
playing_card_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
playing_card = [(r , c) for r in playing_card_color for c in playing_card_number]
print(playing_card)