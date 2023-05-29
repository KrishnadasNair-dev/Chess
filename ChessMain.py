import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['bN', 'bQ', 'bK',
              'bB', 'bR', 'bp',
              'wN', 'wQ', 'wK',
              'wB', 'wR', 'wp']
    
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("./images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))
    

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    validMoves = gs.getValidMoves()
    moveMade = False
    clock.tick(MAX_FPS)
    updateDisplay(screen, gs)
    while running:
        for e in p.event.get():      
            
            if e.type == p.QUIT:
                running = False
                
            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                startSq = (row, col)
                cells = gs.displayPossibleMoves(row, col, validMoves)
                highlight_cells(screen, cells, gs.board)
                
            if e.type == p.MOUSEBUTTONUP:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                endSq = (row, col)
                if startSq != endSq:
                    move = ChessEngine.Move(startSq, endSq, gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        updateDisplay(screen, gs)
                
            if e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    updateDisplay(screen, gs)
            
            if moveMade:
                validMoves = gs.getValidMoves()
                moveMade = False

def highlight_cells(screen, cells, board):
    drawBoard(screen)
    for cell in cells:
         p.draw.rect(screen, (0, 240, 0, 0), p.Rect(cell[1]*SQ_SIZE, cell[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    drawPieces(screen, board)
    p.display.update() 
                      
def updateDisplay(screen, gs):
    drawGameState(screen, gs)
    p.display.flip()


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
def drawPieces(screen, board): 
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "__":
                screen.blit(IMAGES[piece],  p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)
    

if __name__ == '__main__':
    main()
    
    
    