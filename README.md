# Color-Quantizer
Color quantization is the process of reducing number of colors used in an image while trying to maintain the visual appearance of the original image.  In gen- eral, it is a form of cluster analysis, if each RGB color value is considered as a coordinate triple in the 3D colorspace

## K-Means Algorithm

1. Convert input image to a matrix of pixels.
2. Pick K initial colors to begin quantization by clicking on the image or randomly. 
3. Implement K-Means Algoritm. Repeat followings 10 times.
   - Assign each pixel to closest clusters by comparing their R, G, B values.
   - Find clusters' new R, G, B values by getting means of assigned pixels' values.
            
## How to Run?

In order to run color quantizer, execute the following from the command line:


>python3 colorQuantizer.py [IMG] [K] [TYPE]
    

WHERE
1. **IMG** : Path of image want to be quantized.
2. **K** : Number of colors in an image we want to quantize.
3. **TYPE** : Type of selecting cluster centers.
    - **1** for choosing cluster centers by clicking on photo.
    - **2** for choosing cluster centers randomly.
    
    For example, if you want to quantize **cat.png** into **8** colors, by choosing **random** cluster centers. You have to execute following command: \textbf{python3 colorQuantizer.py cat.png 8 2 }

>python3 colorQuantizer.py cat.png 8 2
