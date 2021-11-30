import matplotlib.pyplot as plt

def suite(zr, zi, cr, ci):
    for n in range(1, 100):
        nzr = zr**2-zi**2+cr
        nzi = 2*zr*zi+ci
        if nzr**2+nzi**2 > 4: return n
        zr = nzr
        zi = nzi
    # if we standed 50 rounds, return -1
    return -1

minx = -1.1
maxx = 1.1
nx = 800
miny = -1.1
maxy = 1.1
ny = 800

# compute steps in x and y
dx = (maxx-minx)/nx
dy = (maxy-miny)/ny

# fill img, with nx rows and ny cols
img = []
for iy in range(ny):
    # compute current y value
    y = miny+iy*dy
    line = []
    for ix in range(nx):
        # compute current y value
        x = minx+ix*dx
        # fill current value
        line.append(suite(x, y, 0.3, 0.5))
    img.append(line)

plt.imshow(img, cmap = plt.cm.get_cmap('plasma'), interpolation='none',
           extent = (minx, maxx, miny, maxy))
plt.savefig("mandelbrot_python.svg")
plt.show()
