/**
 * @namespace Image related.
 */
dwv.image = dwv.image || {};

/**
* @class Image Size class. 
* Supports 2D and 3D images.
* @param numberOfColumns The number of columns (number).
* @param numberOfRows The number of rows (number).
* @param numberOfSlices The number of slices (number).
*/
dwv.image.Size = function( numberOfColumns, numberOfRows, numberOfSlices )
{
    // Get the number of columns.
    this.getNumberOfColumns = function() { return numberOfColumns; };
    // Get the number of rows.
    this.getNumberOfRows = function() { return numberOfRows; };
    // Get the number of slices.
    this.getNumberOfSlices = function() { return (numberOfSlices || 1.0); };
};

// Get the size of a slice.
dwv.image.Size.prototype.getSliceSize = function() {
    return this.getNumberOfColumns()*this.getNumberOfRows();
};

// Get the total size.
dwv.image.Size.prototype.getTotalSize = function() {
    return this.getSliceSize()*this.getNumberOfSlices();
};

// Check that coordinates are within bounds.
dwv.image.Size.prototype.checkCoordinates = function( i, j, k ) {
    if( i < 0 || i >= this.getNumberOfColumns() ) throw new Error('Index (i) out of range.');
    else if( j < 0 || j >= this.getNumberOfRows() ) throw new Error('Index (j) out of range.');
    else if( k < 0 || k >= this.getNumberOfSlices() ) throw new Error('Index (k) out of range.');
    return true;
};

/**
* @class Image Spacing class. 
* Supports 2D and 3D images.
* @param columnSpacing The column spacing (number).
* @param rowSpacing The row spacing (number).
* @param sliceSpacing The slice spacing (number).
*/
dwv.image.Spacing = function( columnSpacing, rowSpacing, sliceSpacing )
{
    // Get the column spacing.
    this.getColumnSpacing = function() { return columnSpacing; };
    // Get the row spacing.
    this.getRowSpacing = function() { return rowSpacing; };
    // Get the slice spacing.
    this.getSliceSpacing = function() { return (sliceSpacing || 1.0); };
};

/**
* @class Image class.
* @param size The sizes of the image.
* @param spacing The spacings of the image.
* @param _buffer The image data.
* Usable once created, optional are:
* - rescale slope and intercept (default 1:0), 
* - photometric interpretation (default MONOCHROME2),
* - planar configuration (default RGBRGB...).
*/
dwv.image.Image = function(size, spacing, buffer)
{
    // Rescale slope.
    var rescaleSlope = 1;
    // Rescale intercept.
    var rescaleIntercept = 0;
    // Photometric interpretation (MONOCHROME, RGB...)
    var photometricInterpretation = "MONOCHROME2";
    // Planar configuration for RGB data (0:RGBRGBRGBRGB... or 1:RRR...GGG...BBB...)
    var planarConfiguration = 0;
    
    // original buffer.
    var originalBuffer = buffer.slice();
    
    // data range.
    var dataRange = undefined;
    // histogram.
    var histogram = undefined;
     
    // Get the size of the image.
    this.getSize = function() { return size; };
    // Get the spacing of the image.
    this.getSpacing = function() { return spacing; };
    // Get the data buffer of the image.
    this.getBuffer = function() { return buffer; };
    
    // Get the rescale slope.
    this.getRescaleSlope = function() { return rescaleSlope; };
    // Set the rescale slope.
    this.setRescaleSlope = function(val) { rescaleSlope = val; };
    // Get the rescale intercept.
    this.getRescaleIntercept = function() { return rescaleIntercept; };
    // Set the rescale intercept.
    this.setRescaleIntercept = function(val) { rescaleIntercept = val; };
    // Get the photometricInterpretation of the image.
    this.getPhotometricInterpretation = function() { return photometricInterpretation; };
    // Set the photometricInterpretation of the image.
    this.setPhotometricInterpretation = function(interp) { photometricInterpretation = interp; };
    // Get the planarConfiguration of the image.
    this.getPlanarConfiguration = function() { return planarConfiguration; };
    // Set the planarConfiguration of the image.
    this.setPlanarConfiguration = function(config) { planarConfiguration = config; };

    // Get value at offset. Warning: No size check...
    this.getValueAtOffset = function(offset) {
    	return buffer[offset];
    };
    // Clone the image.
    this.clone = function()
    {
        var copy = new dwv.image.Image(this.getSize(), this.getSpacing(), originalBuffer);
        copy.setRescaleSlope(this.getRescaleSlope());
        copy.setRescaleIntercept(this.getRescaleIntercept());
        copy.setPhotometricInterpretation(this.getPhotometricInterpretation());
        copy.setPlanarConfiguration(this.getPlanarConfiguration());
        return copy;
    };
    // Get the data range.
    this.getDataRange = function() { 
        if( !dataRange ) dataRange = this.calculateDataRange();
        return dataRange;
    };
    // Get the histogram.
    this.getHistogram = function() { 
        if( !histogram ) histogram = this.calculateHistogram();
        return histogram;
    };
};

/**
 * Get the value of the image at a specific coordinate.
 * @param i The X index.
 * @param j The Y index.
 * @param k The Z index.
 * @returns The value at the desired position.
 * Warning: No size check...
 */
dwv.image.Image.prototype.getValue = function( i, j, k )
{
    var k1 = k || 0;
    // check size
    //this.size.checkCoordinates( i, j, k1 );
    // return
    return this.getValueAtOffset( i 
            + ( j * this.getSize().getNumberOfColumns() ) 
            + ( k1 * this.getSize().getSliceSize()) );
};

/**
 * Get the value of the image at a specific offset.
 * @param offset The offset in the buffer. 
 * @returns The value at the desired offset.
 * Warning: No size check...
 */
dwv.image.Image.prototype.getRescaledValueAtOffset = function( offset )
{
    return (this.getValueAtOffset(offset)*this.getRescaleSlope())+this.getRescaleIntercept();
};

/**
 * Get the value of the image at a specific coordinate.
 * @param i The X index.
 * @param j The Y index.
 * @param k The Z index.
 * @returns The value at the desired position.
 * Warning: No size check...
 */
dwv.image.Image.prototype.getRescaledValue = function( i, j, k )
{
    return (this.getValue(i,j,k)*this.getRescaleSlope())+this.getRescaleIntercept();
};

/**
 * Calculate the raw image data range.
 * @returns The range {min, max}.
 */
dwv.image.Image.prototype.calculateDataRange = function()
{
    var min = this.getValueAtOffset(0);
    var max = min;
    var value = 0;
    for(var i=0; i < this.getSize().getTotalSize(); ++i)
    {    
        value = this.getValueAtOffset(i);
        if( value > max ) { max = value; }
        if( value < min ) { min = value; }
    }
    return { "min": min, "max": max };
};

/**
 * Calculate the image data range after rescale.
 * @returns The range {min, max}.
 */
dwv.image.Image.prototype.getRescaledDataRange = function()
{
    var rawRange = this.getDataRange();
    return { "min": rawRange.min*this.getRescaleSlope()+this.getRescaleIntercept(),
        "max": rawRange.max*this.getRescaleSlope()+this.getRescaleIntercept()};
};

/**
 * Calculate the histogram of the image.
 * @returns An array representing the histogram.
 */
dwv.image.Image.prototype.calculateHistogram = function()
{
    var histo = [];
    var histoPlot = [];
    var value = 0;
    var size = this.getSize().getTotalSize();
    for(var i=0; i < size; ++i)
    {    
        value = this.getRescaledValueAtOffset(i);
        histo[value] = histo[value] || 0;
        histo[value] += 1;
    }
    // generate data for plotting
    var min = this.getRescaledDataRange().min;
    var max = this.getRescaledDataRange().max;
    for(var j=min; j < max; ++j)
    {    
        value = histo[j] || 0;
        histoPlot.push([j, value]);
    }
    return histoPlot;
};

/**
 * Convolute the image with a given 2D kernel.
 * @param weights The weights of the 2D kernel.
 * @returns The convoluted image.
 * 
 * Note: Uses the raw buffer values.
 */
dwv.image.Image.prototype.convolute = function(weights)
{
    var newImage = this.clone();
    var newBuffer = newImage.getBuffer();

    var side = Math.round(Math.sqrt(weights.length));
    var halfSide = Math.floor(side/2);
    
    var ncols = this.getSize().getNumberOfColumns();
    var nrows = this.getSize().getNumberOfRows();
    
    // go through the destination image pixels
    for (var y=0; y<nrows; y++) {
        for (var x=0; x<ncols; x++) {
            var dstOff = y*ncols + x;
            // calculate the weighed sum of the source image pixels that
            // fall under the convolution matrix
            var newValue = 0;
            for (var cy=0; cy<side; cy++) {
                for (var cx=0; cx<side; cx++) {
                    var scy = y + cy - halfSide;
                    var scx = x + cx - halfSide;
                    if (scy >= 0 && scy < nrows && scx >= 0 && scx < ncols) {
                        var srcOff = scy*ncols + scx;
                        var wt = weights[cy*side+cx];
                        newValue += this.getValueAtOffset(srcOff) * wt;
                    }
                }
            }
            newBuffer[dstOff] = newValue;
        }
    }
    return newImage;
};

/**
 * Transform an image using a specific operator.
 * @param operator The operator to use when transforming.
 * @returns The transformed image.
 * 
 * Note: Uses the raw buffer values.
 */
dwv.image.Image.prototype.transform = function(operator)
{
    var newImage = this.clone();
    var newBuffer = newImage.getBuffer();
    for(var i=0; i < this.getSize().getTotalSize(); ++i)
    {   
        newBuffer[i] = operator( newImage.getValueAtOffset(i) );
    }
    return newImage;
};

/**
 * Compose this image with another one and using a specific operator.
 * @param rhs The image to compose with.
 * @param operator The operator to use when composing.
 * @returns The composed image.
 * 
 * Note: Uses the raw buffer values.
 */
dwv.image.Image.prototype.compose = function(rhs, operator)
{
    var newImage = this.clone();
    var newBuffer = newImage.getBuffer();
    for(var i=0; i < this.getSize().getTotalSize(); ++i)
    {   
        // using the operator on the local buffer, i.e. the latest (not original) data
        newBuffer[i] = Math.floor( operator( this.getValueAtOffset(i), rhs.getValueAtOffset(i) ) );
    }
    return newImage;
};
