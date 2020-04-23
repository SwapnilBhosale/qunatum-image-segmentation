import matplotlib.image as mpimg
import numpy as np
import skimage
import defaultdict

def compute_pdfs(imfile, imfile_scrib):
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

rgb = mpimg.imread("test.png")[:,:,:3]
yuv = skimage.color.rgb2yiq(rgb)
print(rgb[0][:])