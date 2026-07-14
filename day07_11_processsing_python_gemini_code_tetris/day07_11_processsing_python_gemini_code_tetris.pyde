#day07_11_processsing_python_gemini_code_tetris
#prompt for gemini「想要寫一個processing python mode 的可以模仿「俄羅斯方塊」的遊戲 請給我程式!」
# 遊戲視窗與網格設定
grid_w = 10      # 網格寬度（10格）
grid_h = 20      # 網格高度（20格）
block_size = 30  # 每格的像素大小

# 定義 7 種經典方塊形狀 (X, Y 座標偏移量)
SHAPES = [
    [[0,0], [1,0], [2,0], [3,0]], # I
    [[0,0], [0,1], [1,1], [2,1]], # J
    [[2,0], [0,1], [1,1], [2,1]], # L
    [[1,0], [2,0], [1,1], [2,1]], # O
    [[1,0], [2,0], [0,1], [1,1]], # S
    [[1,0], [0,1], [1,1], [2,1]], # T
    [[0,0], [1,0], [1,1], [2,1]]  # Z
]

# 方塊顏色 (RGB)
COLORS = [
    (0, 255, 255),   # 青色 I
    (0, 0, 255),     # 藍色 J
    (255, 165, 0),   # 橘色 L
    (255, 255, 0),   # 黃色 O
    (0, 255, 0),     # 綠色 S
    (128, 0, 128),   # 紫色 T
    (255, 0, 0)      # 紅色 Z
]

def setup():
    size(grid_w * block_size, grid_h * block_size)
    frameRate(60)
    global board, current_shape, current_color, current_x, current_y, game_over, score, fall_timer
    
    # 初始化遊戲板 (0 表示空格，非 0 表示已有方塊的顏色索引)
    board = [[0] * grid_w for _ in range(grid_h)]
    
    score = 0
    game_over = False
    fall_timer = 0
    
    # 產生第一個方塊
    spawn_piece()

def draw():
    global fall_timer, game_over
    background(40)
    
    if game_over:
        fill(255, 0, 0)
        textSize(32)
        textAlign(CENTER, CENTER)
        text("GAME OVER", width/2, height/2)
        textSize(20)
        text("Score: " + str(score), width/2, height/2 + 40)
        return

    # 繪製已固定的方塊堆
    draw_board()
    
    # 繪製當前控制的方塊
    draw_current_piece()
    
    # 控制方塊自然下落的速度 (每 30 幀下落一格)
    fall_timer += 1
    if fall_timer >= 30:
        move_piece(0, 1)
        fall_timer = 0

def spawn_piece():
    global current_shape, current_color, current_x, current_y, game_over
    shape_idx = int(random(len(SHAPES)))
    
    # 複製方塊座標，避免修改到原始的 SHAPES 列表
    current_shape = [list(p) for p in SHAPES[shape_idx]]
    current_color = COLORS[shape_idx]
    
    # 初始位置 (畫面上方中央)
    current_x = grid_w // 2 - 2
    current_y = 0
    
    # 如果一出生就碰撞，代表遊戲結束
    if check_collision(current_shape, current_x, current_y):
        game_over = True

def draw_board():
    for r in range(grid_h):
        for c in range(grid_w):
            if board[r][c] != 0:
                fill(*board[r][c])
                stroke(0)
                rect(c * block_size, r * block_size, block_size, block_size)
            else:
                # 繪製背景網格線
                stroke(60)
                noFill()
                rect(c * block_size, r * block_size, block_size, block_size)

def draw_current_piece():
    fill(*current_color)
    stroke(0)
    for p in current_shape:
        x = (current_x + p[0]) * block_size
        y = (current_y + p[1]) * block_size
        # 確保只畫在遊戲區域內
        if y >= 0:
            rect(x, y, block_size, block_size)

def move_piece(dx, dy):
    global current_x, current_y
    if not check_collision(current_shape, current_x + dx, current_y + dy):
        current_x += dx
        current_y += dy
        return True
    
    # 如果試圖向下移動卻碰撞了，說明方塊落地了，需要固定它
    if dy > 0:
        lock_piece()
        clear_lines()
        spawn_piece()
    return False

def check_collision(shape, nx, ny):
    for p in shape:
        cx = nx + p[0]
        cy = ny + p[1]
        # 檢查是否超出邊界
        if cx < 0 or cx >= grid_w or cy >= grid_h:
            return True
        # 檢查是否與已經固定的方塊重疊
        if cy >= 0 and board[cy][cx] != 0:
            return True
    return False

def lock_piece():
    for p in current_shape:
        cx = current_x + p[0]
        cy = current_y + p[1]
        if cy >= 0:
            board[cy][cx] = current_color

def rotate_piece():
    global current_shape
    # 方塊旋轉矩陣公式: (x, y) -> (-y, x) 
    # 這裡以 2x2 的中心進行簡單旋轉
    new_shape = []
    for p in current_shape:
        # 以 (1.5, 1.5) 作為旋轉中心點（適用於 4x4 區塊）
        nx = round(1.5 - (p[1] - 1.5))
        ny = round(1.5 + (p[0] - 1.5))
        new_shape.append([int(nx), int(ny)])
        
    # 如果旋轉後不會碰撞，才允許旋轉
    if not check_collision(new_shape, current_x, current_y):
        current_shape = new_shape

def clear_lines():
    global board, score
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = grid_h - len(new_board)
    
    # 在頂部補上空行
    for _ in range(lines_cleared):
        new_board.insert(0, [0] * grid_w)
        
    board = new_board
    score += lines_cleared * 100

def keyPressed():
    if game_over:
        return
    if keyCode == LEFT:
        move_piece(-1, 0)
    elif keyCode == RIGHT:
        move_piece(1, 0)
    elif keyCode == DOWN:
        move_piece(0, 1)
    elif keyCode == UP:
        rotate_piece()
