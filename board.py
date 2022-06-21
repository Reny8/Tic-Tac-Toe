class Board:
    def __init__(self):
        self.row1 = ['_','_','_']
        self.row2 = ['_','_','_']
        self.row3 = ['_','_','_']
        self.map = [self.row1, self.row2,self.row3]

    def show_board(self):
        for map in self.map:
            print(f'  '.join(map))
            
 
              

        
            

