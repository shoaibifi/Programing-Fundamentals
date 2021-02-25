### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###def 
def calculateArea(width,length):
     area=length*width 
     return area

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    if plot_width<0 or plot_length<0 or tile_width<0 or tile_length<0:
        return False
    if plot_width%tile_width == 0 and plot_length%tile_length == 0:
        return True
    if plot_width%tile_length == 0 and plot_length%tile_width == 0:
        return True
    if calculateArea(plot_width, plot_length) >= calculateArea(tile_width,tile_length):
        if tile_length>plot_length:
            if plot_width%tile_width == 0 and tile_length%plot_length == 0:
                return True
        if tile_width>plot_width:
            if tile_width%plot_width == 0 and plot_length%tile_length == 0:
                return True
    return False     
              
          
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###

def calculateTiles(plot_width, plot_length,tile_width,tile_length):
    if type(plot_width) is str or type(plot_length) is str or type(tile_width) is str or type(tile_length) is str:
        return "Invalid Input"
    if plot_width==0 or plot_length==0 or tile_width==0 or tile_length==0:
        return None
    if plot_width<0 or plot_length<0 or tile_width<0 or tile_length<0:
        return "Not Possible"
    if checkTilesFit(plot_width,plot_length,tile_width,tile_length)==True:
        return(calculateArea(plot_width,plot_length)/calculateArea(tile_width,tile_length))
    else:
        return "Not Possible"     
        
	
	

#### End OF MARKER



