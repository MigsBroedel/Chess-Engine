
# sistema de turnos - switchs e ifs, assim como mudar as cores e log p facilitar testes - feito
# regras de cada peça - feito
# movlog
# undo move -  meio feito, precisa do movlog pra funcionar direito
# verificar check e checkmate
# melhorar performance e legibilidade


#ERRO = X e Y invertidos na função piece


# next steps, pensar em regras das peças, maybe a function que vc passa a peça, a posição, o alvo e a posição e define se pode ou não, isso poderia ser usado até para peças brancas comerem brancas ou pretas
# talvez um switch case 
DIMENTION = 8
MovLogone = ()
MovLogoneS = ()

class GameEngine:
    def __init__ (self):
        self.BOARD = [['br','bn','bb','bq','bk','bb','bn','br'], #Board of the game
                      ['bp','bp','bp','bp','bp','bp','bp','bp'], # Pieces: Rook:r, Knight:n, Bishop:b, Queen:q, King:k, Pawn:p
                      ['__','__','__','__','__','__','__','__'], # White: w, Black: b
                      ['__','__','__','__','__','__','__','__'],
                      ['__','__','__','__','__','__','__','__'],
                      ['__','__','__','__','__','__','__','__'],
                      ['wp','wp','wp','wp','wp','wp','wp','wp'],
                      ['wr','wn','wb','wq','wk','wb','wn','wr']
                    ]
        self.Wturn = True

    def Jogada (self, Move):
      print("call")
      print(Move.PieceMov[0])
      self.MovLogone = (Move.Startx, Move.Starty)
      self.MovLogoneS = (Move.Endx, Move.Endy)
     # print(type(Tempc), Tempc)
      #print(type(Move.Endx), Move.Endx, Move.Endy)
      #print(type(Move.Startx), Move.Startx, Move.Starty)
      self.BOARD[Move.Startx][Move.Starty] = "__"
      self.BOARD[Move.Endx][Move.Endy] = Move.PieceMov
      self.Wturn = not self.Wturn
      #print(self.BOARD)
    
    def UndoMove (self, Move):
      Move.Endx = self.MovLogone[0]
      Move.Endy = self.MovLogone[1]
      Move.Startx = self.MovLogoneS[0]
      Move.Starty = self.MovLogoneS[1]



    def Pieces (self, Move, piece):
       if piece[1] == "p" and piece[0] == "w":
          if (Move.Endy == Move.Starty): # verifica se esta se mexendo na vertical
             if (Move.Endx == Move.Startx - 1): # verifica se o peão se move apenas uma casa por vez
              print("y y y deu certo whi ")
              return 1
          else: 
             print("x x x errou whi")
             return 0
       elif piece[1] == "p" and piece[0] == "b":
          if (Move.Endy == Move.Starty): # verifica se esta se mexendo na vertical
             if (Move.Endx == Move.Startx + 1): # verifica se o peão se move apenas uma casa por vez
              print("y y y deu certo bl")
              return 1
          else: 
             print("x x x errou bl")
             return 0
          
           #####
       elif piece[1] == "r" and piece[0] == "w":
          if (Move.Endy == Move.Starty or Move.Endx == Move.Startx): # verifica se esta se mexendo na vertical
              print("y y y deu certo whi ")
              return 1
          else: 
             print("x x x errou whi")
             return 0
       elif piece[1] == "r" and piece[0] == "b":
          if (Move.Endy == Move.Starty or Move.Endx == Move.Startx): # verifica se esta se mexendo na vertical
              print("y y y deu certo bl")
              return 1
          else: 
             print("x x x errou bl")
             return 0
         
         ###
       elif piece[1] == "b" and piece[0] == "w":
          direcoes = ([-1, 1], [-1, -1], [1, 1], [1, -1])
          for dir in direcoes:
            i = 1
            while i <= 8:
             nx = Move.Starty + i
             ny = Move.Startx + i
             mx = Move.Starty - i
             my = Move.Startx - i
             i += 1
             if (Move.Endx == ny and Move.Endy == nx):
              print("y y y deu certo whi ")
              return 1
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo whi ")
              return 1
             elif (Move.Endx == my and Move.Endy == nx):
              print("y y y deu certo whi ")
              return 1                              
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo whi ")
              return 1               
             else: 
               print("x x x errou whi")
               return 0
       
       elif piece[1] == "b" and piece[0] == "b":
          direcoes = ([-1, 1], [-1, -1], [1, 1], [1, -1])
          for dir in direcoes:
            i = 1
            while i <= 8:
             nx = Move.Starty + i
             ny = Move.Startx + i
             mx = Move.Starty - i
             my = Move.Startx - i
             i += 1
             if (Move.Endx == ny and Move.Endy == nx):
              print("y y y deu certo bl ")
              return 1
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo bl ")
              return 1
             elif (Move.Endx == my and Move.Endy == nx):
              print("y y y deu certo bl ")
              return 1                              
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo bl ")
              return 1               
             else: 
               print("x x x errou bl")
               return 0
       ###

       elif piece[1] == "q" and piece[0] == "w":
         direcoes = ([-1, 1], [-1, -1], [1, 1], [1, -1])
         if (Move.Endy == Move.Starty or Move.Endx == Move.Startx): # verifica se esta se mexendo na vertical
              print("y y y deu certo whi ")
              return 1

         elif Move.Endy != Move.Starty or Move.Endx != Move.Startx:
          for dir in direcoes:
            i = 1
            while i <= 8:
             nx = Move.Starty + i
             ny = Move.Startx + i
             mx = Move.Starty - i
             my = Move.Startx - i
             i += 1
             if (Move.Endx == ny and Move.Endy == nx):
              print("y y y deu certo whi ")
              return 1
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo whi ")
              return 1
             elif (Move.Endx == my and Move.Endy == nx):
              print("y y y deu certo whi ")
              return 1                              
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo whi ")
              return 1               
         else: 
            print("x x x errou whi")
            return 0
         
       elif piece[1] == "q" and piece[0] == "b":
         direcoes = ([-1, 1], [-1, -1], [1, 1], [1, -1])
         if (Move.Endy == Move.Starty or Move.Endx == Move.Startx): # verifica se esta se mexendo na vertical
              print("y y y deu certo bl ")
              return 1

         elif Move.Endy != Move.Starty or Move.Endx != Move.Startx:
          for dir in direcoes:
            i = 1
            while i <= 8:
             nx = Move.Starty + i
             ny = Move.Startx + i
             mx = Move.Starty - i
             my = Move.Startx - i
             i += 1
             if (Move.Endx == ny and Move.Endy == nx):
              print("y y y deu certo bl ")
              return 1
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo bl ")
              return 1
             elif (Move.Endx == my and Move.Endy == nx):
              print("y y y deu certo bl ")
              return 1                              
             elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo bl ")
              return 1               
         else: 
            print("x x x errou bl")
            return 0
         
         ###
       elif piece[1] == "n" and piece[0] == "w":
         ny1 = [[(Move.Starty + 2), (Move.Startx + 1)],
                [(Move.Starty - 2), (Move.Startx + 1)],
                [(Move.Starty + 2), (Move.Startx - 1)], 
                [(Move.Starty - 2), (Move.Startx - 1)], 
                [(Move.Starty + 1), (Move.Startx + 2)], 
                [(Move.Starty - 1), (Move.Startx + 2)], 
                [(Move.Starty + 1), (Move.Startx - 2)], 
                [(Move.Starty - 1), (Move.Startx - 2)]]
                
         for n in ny1:
           if (Move.Endy == n[0] and Move.Endx == n[1]):
             print("y y y deu certo whi ")
             return 1

         print("x x x deu errado whi")
         return 0
       
       elif piece[1] == "n" and piece[0] == "b":
         ny1 = [[(Move.Starty + 2), (Move.Startx + 1)],
                [(Move.Starty - 2), (Move.Startx + 1)],
                [(Move.Starty + 2), (Move.Startx - 1)], 
                [(Move.Starty - 2), (Move.Startx - 1)], 
                [(Move.Starty + 1), (Move.Startx + 2)], 
                [(Move.Starty - 1), (Move.Startx + 2)], 
                [(Move.Starty + 1), (Move.Startx - 2)], 
                [(Move.Starty - 1), (Move.Startx - 2)]]
                
         for n in ny1:
           if (Move.Endy == n[0] and Move.Endx == n[1]):
             print("y y y deu certo bl ")
             return 1

         print("x x x deu errado bl")
         return 0
       ###

       elif piece[1] == "k" and piece[0] == "w":
        nx = Move.Starty + 1
        ny = Move.Startx + 1
        mx = Move.Starty - 1
        my = Move.Startx - 1
        direcoes = ([-1, 1], [-1, -1], [1, 1], [1, -1])
        for dir in direcoes:
            if (Move.Endy == Move.Starty + 1 or Move.Endx == Move.Startx + 1 or Move.Endy == Move.Starty - 1 or Move.Endx == Move.Startx - 1): # verifica se esta se mexendo na vertical ou horizontal apenas 1 casa
              print("y y y deu certo whi ")
              return 1
            elif (Move.Endx == ny and Move.Endy == nx):
              print("y y y deu certo whi ")
              return 1
            elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo whi ")
              return 1
            elif (Move.Endx == my and Move.Endy == nx):
              print("y y y deu certo whi")
              return 1                              
            elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo whi ")
              return 1               
            else: 
              print("x x x errou whi")
            return 0
        
       elif piece[1] == "k" and piece[0] == "b":
        nx = Move.Starty + 1
        ny = Move.Startx + 1
        mx = Move.Starty - 1
        my = Move.Startx - 1
        direcoes = ([-1, 1], [-1, -1], [1, 1], [1, -1])
        for dir in direcoes:
            if (Move.Endy == Move.Starty + 1 or Move.Endx == Move.Startx + 1 or Move.Endy == Move.Starty - 1 or Move.Endx == Move.Startx - 1): # verifica se esta se mexendo na vertical ou horizontal apenas 1 casa
              print("y y y deu certo bl ")
              return 1
            elif (Move.Endx == ny and Move.Endy == nx):
              print("y y y deu certo bl ")
              return 1
            elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo bl ")
              return 1
            elif (Move.Endx == my and Move.Endy == nx):
              print("y y y deu certo bl ")
              return 1                              
            elif (Move.Endx == my and Move.Endy == mx):
              print("y y y deu certo bl ")
              return 1               
            else: 
              print("x x x errou bl")
            return 0

       
                            
       
         
       
             
             
          



class Move:
   def __init__(self, ListTuple, board):
     # print("Class Created")
      self.Startx = ListTuple[0][1]
      self.Starty = ListTuple[0][0]
      self.PieceMov = board[self.Startx][self.Starty] # piece str
      if (len(ListTuple) > 1): # assim a função consegue pegar os numeros de array so com a primeira parte da lista de tuplas, usado para desenhar as linhas e setar regras no main
        self.Endx = ListTuple[1][1] # cordinates
        self.Endy = ListTuple[1][0]
        self.PieceCap = board[self.Endx][self.Endy] # piece str
      #print(self.PieceMov, self.PieceCap)

      
  