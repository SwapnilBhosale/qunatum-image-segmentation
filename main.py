import matplotlib.image as mpimg
import numpy as np
from skimage import io
from skimage.transform import resize
from collections import defaultdict 


'''def compute_pdfs(imfile, imfile_scrib):
     rgb = mpimg.imread(imfile)[:,:,:3]
     yuv = skimage.color.rgb2yiq(rgb)
     rgb_s = mpimg.imread(imfile_scrib)[:,:,:3]
     yuv_s = skimage.color.rgb2yiq(rgb_s)
     # find the scribble pixels
     scribbles = find_marked_locations(rgb, rgb_s)
     imageo = np.zeros(yuv.shape)
     # separately store background and foreground scribble pixels in the dictionary comps
     comps = defaultdict(lambda:np.array([]).reshape(0,3))
     for (i, j) in scribbles:
          imageo[i,j,:] = rgbs[i,j,:]
          # scribble color as key of comps
          comps[tuple(imageo[i,j,:])] = np.vstack([comps[tuple(imageo[i,j,:])], yuv[i,j,:]])
          mu, Sigma = {}, {}
     # compute MLE parameters for Gaussians
     for c in comps:
          mu[c] = np.mean(comps[c], axis=0)
          Sigma[c] = np.cov(comps[c].T)
     return (mu, Sigma)
'''
img = io.imread('test1.jpg')
print(img.dtype, img.shape)
print(img[0][0:2])
#small_resized = resize(img, (30,30), mode='symmetric', preserve_range=True)

# Write the tinted image back to disk
#io.imsave('test1_scaled.jpg', small_resized)