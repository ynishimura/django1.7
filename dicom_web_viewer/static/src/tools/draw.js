/**
 * @namespace Tool classes.
 */
dwv.tool = dwv.tool || {};

//! List of colors
dwv.tool.colors = [
    "Yellow", "Red", "White", "Green", "Blue", "Lime", "Fuchsia", "Black"
];

//shape list: to be completed after each tool definition 
dwv.tool.shapes = {};

/**
* @class Drawing tool.
*/
dwv.tool.Draw = function(app)
{
    var self = this;
    // start drawing flag
    var started = false;
    // draw command
    var command = null;
    // draw style
    this.style = new dwv.html.Style();
    // shape name
    this.shapeName = 0;
    // list of points
    var points = [];

    // This is called when you start holding down the mouse button.
    this.mousedown = function(ev){
        started = true;
        // clear array
        points = [];
        // store point
        points.push(new dwv.math.Point2D(ev._x, ev._y));
    };

    // This function is called every time you move the mouse.
    this.mousemove = function(ev){
        if (!started)
        {
            return;
        }
        if( ev._x !== points[0].getX() 
            && ev._y !== points[0].getY() )
        {
            // current point
            points.push(new dwv.math.Point2D(ev._x, ev._y));
            // create draw command
            command = new dwv.tool.shapes[self.shapeName](points, app, self.style);
            // clear the temporary layer
            app.getTempLayer().clearContextRect();
            // draw
            command.execute();
        }
    };

    // This is called when you release the mouse button.
    this.mouseup = function(ev){
        if (started)
        {
            // save command in undo stack
            app.getUndoStack().add(command);
            // merge temporary layer
            app.getDrawLayer().merge(app.getTempLayer());
            // set flag
            started = false;
        }
    };
    
    this.mouseout = function(ev){
        self.mouseup(ev);
    };

    this.touchstart = function(ev){
        self.mousedown(ev);
    };

    this.touchmove = function(ev){
        self.mousemove(ev);
    };

    this.touchend = function(ev){
        self.mouseup(ev);
    };

   // Enable the draw tool
    this.enable = function(value){
        if( value ) {
            this.init();
            dwv.gui.appendDrawHtml();
        }
        else { 
            dwv.gui.clearDrawHtml();
        }
    };
    
    // Handle key down event
    this.keydown = function(event){
        app.handleKeyDown(event);
    };

}; // Draw class

// Set the line color of the drawing
dwv.tool.Draw.prototype.setLineColour = function(colour)
{
    // set style var
    this.style.setLineColor(colour);
};

// Set the shape name of the drawing
dwv.tool.Draw.prototype.setShapeName = function(name)
{
    // check if we have it
    if( !this.hasShape(name) )
    {
        throw new Error("Unknown shape: '" + name + "'");
    }
    this.shapeName = name;
};

dwv.tool.Draw.prototype.hasShape = function(name) {
    return dwv.tool.shapes[name];
};

dwv.tool.Draw.prototype.init = function() {
    // set the default to the first in the list
    var shapeName = 0;
    for( var key in dwv.tool.shapes ){
        shapeName = key;
        break;
    }
    this.setShapeName(shapeName);
    // same for color
    this.setLineColour(dwv.tool.colors[0]);
};

// Add the tool to the list
dwv.tool.tools["draw"] = dwv.tool.Draw;
