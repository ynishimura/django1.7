/**
 * @namespace Tool classes.
 */
dwv.tool = dwv.tool || {};

/**
 * @class Draw ROI command.
 * @param points The points from which to extract the line.
 * @param app The application to draw the line on.
 * @param style The drawing style.
 */
dwv.tool.DrawRoiCommand = function(points, app, style)
{
    var roi = new dwv.math.ROI();
    roi.addPoints(points);

    var lineColor = style.getLineColor();
    var context = app.getTempLayer().getContext();
    
    // command name
    var name = "DrawRoiCommand";
    this.setName = function(str) { name = str; };
    this.getName = function() { return name; };

    // main method
    this.execute = function()
    {
        // style
        context.fillStyle = lineColor;
        context.strokeStyle = lineColor;
        // path
        context.beginPath();
        context.moveTo(
                roi.getPoint(0).getX(), 
                roi.getPoint(0).getY());
        for( var i = 1; i < roi.getLength(); ++i )
        {
            context.lineTo(
                    roi.getPoint(i).getX(), 
                    roi.getPoint(i).getY());
            context.stroke();
        }
        context.closePath();
        context.stroke();
    }; 
}; // DrawRoiCommand class

//Add the shape command to the list
dwv.tool.shapes["roi"] = dwv.tool.DrawRoiCommand;
