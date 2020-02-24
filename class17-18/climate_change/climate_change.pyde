import csv
import random

background_color = 32
text_color = 255

def setup():
    global lstheader
    
    global columns
    global lstheader
    global colname
    colname = 'cold_days'
    
    lstheader = []
    file = open("data/aggregate_montreal_climate.csv", 'r')
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    header = reader.next()
    columns = {}
    for colname in header:
        columns[colname] = []
        lstheader.append(colname)
    print(header)
    for row in reader:
        for i in range(len(row)):
            columns[header[i]].append(row[i])
    file.close()
    size(1000, 1000)
    
    background(background_color)
    

    #global columns
        
    

    if len(lstheader)!=0:
        for i in range(3):
            lstheader.pop(0)
        # lstheader.pop(0)
        # lstheader.pop(0)
        # lstheader.pop(0)
    print(lstheader)
    print(colname)
    
def buttons():
    global colname
    
    global bcolor
    bcolor="250"
    textSize(14)    
    for i in range(len(lstheader)):
        fill(250, 250, 250)
        rect(i*110+30,height-45,100,30,7) 
        fill(bcolor)
        textAlign(LEFT)  
        text(lstheader[i], i*110+45, height-25)
        if mousePressed and mouseButton == LEFT and  mouseX>i*110+30 and mouseX<i*110+30+100 and mouseY>height-45 and mouseY<height-45+50:
            colname = lstheader[i]
            bcolor = "0"
            fill(245, 161, 66)
            rect(i*110+30,height-45,100,30,7)
            fill(250,250,0)
            text(lstheader[i], i*110+45, height-25)
        
    #print(colname) 
             

       
def draw():
    global columns
    global colname
    
    idx = frameCount % len(columns['year'])
    if idx == 0:
        background(0)
        return
    
    noStroke()
    fill(background_color, background_color, background_color, 5)
    rect(0, 0, width, height)
    strokeWeight(0)
    
    
    #print(columns['year'][idx])
    pushMatrix()
    translate(0, height)
    scale(1, -1)
    translate(width * .05, width * 0.1)
    scale(.9, .8)
    
    
    #colname = 'cold_days'
    
    the_col = columns[colname]
    bottom_range = min(the_col)
    top_range = max(the_col)
    left_range = min(columns['year'])
    right_range = max(columns['year'])
    
    current_year = columns['year'][idx]
    frac_t = (current_year - left_range) / (right_range - left_range)
    stroke(frac_t * 255, 
           192, 
           (1 - frac_t) * 255) 
    
    scale(width / (right_range - left_range), height / (top_range - bottom_range))
    translate(-left_range, -bottom_range)
    
    for i in range(3):
        line(columns['year'][idx-1],
            the_col[idx-1],
            columns['year'][idx],
            the_col[idx])
    popMatrix()
    
    noStroke()
    fill(background_color)
    rect(0, 0, width, 50)
    fill(text_color)
    textSize(30)
    textAlign(CENTER)
    fill(background_color)
    
    rect(0, height - 80, width, 35)
    fill(text_color)
    text(int(columns['year'][idx]), width / 2, height - 50)
    textAlign(CENTER)
    text(colname, width/2, 20)
    buttons()
