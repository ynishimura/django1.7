import dicom
import pylab
filename = "test2.dcm"

ds = dicom.read_file(filename)

img = ds.pixel_array


pylab.imshow(img)
pylab.xticks([])
pylab.yticks([])
pylab.savefig("test2.png",bbox_inches="tight", pad_inches=0.0)
