import pygame as pg
import Chessengine

HEIGHT = WIDTH = 512
DIMENTION = 8
SQSIZE = HEIGHT // DIMENTION
FPS = 15
gs = Chessengine.GameEngine()
IMAGES = {}


def loadImages():
    pieces = ['br','bn','bb','bq','bk','bp','wr','wn','wb','wq','wk','wp']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load('./images/' + piece + '.png'), (SQSIZE, SQSIZE))

def main():

    screen = pg.display.set_mode((HEIGHT, WIDTH))
    clock = pg.time.Clock()
    screen.fill(pg.Color("White"))
    running = True
    loadImages()
    SelectSq = ()
    ListTuple = []


    while running == True:
        pg.display.flip()
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
            drawBoard(screen)
            drawPieces(screen, gs)

            #########################
                
            if gs.Wturn == True:# TURNO DAS BRANCAS
               # print(gs.Wturn)
                if event.type == pg.MOUSEBUTTONDOWN:
                
                    if len(ListTuple) < 2:
                        
                        SelectSq = pg.mouse.get_pos() 
                        print("SQ: ", SelectSq)
                        x = SelectSq[0] // 64
                        y = SelectSq[1] // 64
                        #print("click", SelectSq)
                        ListTuple.append((x, y))
                        drawSeq(x, y, screen)
                        movefirst = Chessengine.Move(ListTuple, gs.BOARD)
                        if (movefirst.PieceMov[0] == 'w'):
                            
                            SelectSq = ()
                        else:
                            SelectSq = ()
                            ListTuple = []
                    
                
                   # print(len(ListTuple))
                   # print(ListTuple)
                       

                    elif len(ListTuple) >= 1:
                        SelectSq = pg.mouse.get_pos()
                        x = SelectSq[0] // 64
                        y = SelectSq[1] // 64
                        print(type(ListTuple))
                        ListTuple.append((x, y)) 
                        drawSeq(x, y, screen)
                        print("test", ListTuple)
                        move = Chessengine.Move(ListTuple, gs.BOARD)
                        if (gs.Pieces(move, move.PieceMov) == 1 and move.PieceMov[0] == "w"):
                            
                            print(move.PieceMov)
                            gs.Jogada(move)
                                    


                            #print("before", SelectSq, ListTuple)
                            SelectSq = ()
                            ListTuple = []                              
                        #print("after", SelectSq, ListTuple)
                        else:
                            SelectSq = ()
                            ListTuple.pop(1)


                    #######################################
            elif gs.Wturn == False:# TURNO DAS PRETAS
                #print(gs.Wturn)
                if event.type == pg.MOUSEBUTTONDOWN:
                


                    if len(ListTuple) < 2:
                        SelectSq = pg.mouse.get_pos() 
                        x = SelectSq[0] // 64
                        y = SelectSq[1] // 64
                        #print("click", SelectSq)
                        ListTuple.append((x, y))
                        drawSeq(x, y, screen)
                            
                    
                
                   # print(len(ListTuple))
                   # print(ListTuple)
                       

                    elif len(ListTuple) >= 1:
                        SelectSq = pg.mouse.get_pos()
                        x = SelectSq[0] // 64
                        y = SelectSq[1] // 64
                        ListTuple.append((x, y))
                        drawSeq(x, y, screen)
                        move = Chessengine.Move(ListTuple, gs.BOARD)
                        if (gs.Pieces(move, move.PieceMov) == 1 and move.PieceMov[0] == "b"):
                            print("JB")

                            gs.Jogada(move)
                            #print("before", SelectSq, ListTuple)
                            SelectSq = ()
                            ListTuple = []
                        #print("after", SelectSq, ListTuple)
                        else:
                            SelectSq = ()
                            ListTuple.pop(1)


                    #######################################
            k = pg.key.get_pressed()
            if k[pg.K_LEFT]:
                gs.UndoMove(move)
                gs.Jogada(move)
                SelectSq = ()
                ListTuple = []
                gs.Wturn = not gs.Wturn


                    
                
            

def drawSeq (x, y, screen):
    pg.draw.line(screen, pg.Color("green"), (x * 64, (y * 64 + SQSIZE)), (x * 64 + 64, (y * 64 + SQSIZE)), 3)
        

        
def drawBoard (screen):
    colors = [pg.Color("white"), pg.Color("gray33")]
    for x in range(DIMENTION):
        for y in range(DIMENTION):
            color = colors[((x+y)%2)]
            pg.draw.rect(screen, color, pg.Rect(x*SQSIZE, y*SQSIZE, SQSIZE, SQSIZE))

def drawPieces (screen, gs):
    for x in range(DIMENTION):
        for y in range(DIMENTION):
            piece = gs.BOARD[y][x]
            if piece != "__":
                screen.blit(IMAGES[piece], pg.Rect(x*SQSIZE, y*SQSIZE, SQSIZE, SQSIZE))     
                

if __name__ == "__main__":
    main()