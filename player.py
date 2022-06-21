class Player:
    def __init__(self,name):
        self.player_wins = 0
        self.player_name = name
       

    def row_chosen(self):
        while True:
            row_block = int(input("Pick a row: "))
            if row_block not in [1,2,3]:
                continue 
            else:
                break
        return row_block - 1
    
    def block_chosen(self):
        while True:
            block_choice = int(input("Pick a block in the row: "))
            if block_choice not in [1,2,3]:
                continue
            else:
                break
        return block_choice - 1
    
    
   
    
 