# OpenCV-Basics


Points to remember in OpenCV :


Various color channels(color spaces)

GrayScale/ B&w = single channels
RGB/BGR   = R G B
HSV    = Hue Saturation Value/intensity
CMK    = CYAN Magenta Yellow
CMYK = CYAN Magenta Yellow Key



Inter Polattion methods 

INTER_LINEAR 
INTER_NEAREST
INTER_AREA              -               SHRINKING
INTER_CUBIC             -               ZOOMING
INTER_LANCZOS4


Transformations :
Scaling     -  we make use of cv2.resize()
Rotation    -  we make use of cv2.getrotationalmatrix2D() and cv2.warpAffine()
Affine        
Perspective 


segmentation : Dividing images into various regions
Thresholding is the basic form of segmentation



OTSU's binaraization: In many cases we can't judge the threshold value correctly so OSTU binarization techinque findes that optimal
threshold value in the given image(used in case of bi-modal images - consists of two components fore-ground component andback-ground component)


Adaptive Thresholding: Whereas the conventional thresholding operator uses a global threshold for all pixels, 
adaptive thresholding changes the threshold dynamically over the image. 
This more sophisticated version of thresholding can accommodate changing lighting conditions in the image
e.g. those occurring as a result of a strong illumination gradient or shadows.

mean adaptive thresholding : threshold value is the mean of neighbourhood area.
gaussian adaptive thresholding :  threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.


kerenel and convolution :

kernel is the matrix being applied to the input image 
convolution is the opertaion being performed on the input image through the kernel


Low-Pass Filters :

These low pass filters are applied to filter the high-frequency components such as edges and noise from the input image

These Low-pass filters are capabale of doing 
Blurring 
Denoising
Smoothing

Median pass flters :

Median pass filters are used to efficiently to remove the salt and pepper noise

High Pass filters :

The high pass filters are used for edge detection in the input images 

various high pass filters are 

laplacian
sobel
scharr
