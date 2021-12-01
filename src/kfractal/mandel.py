import matplotlib.pyplot as plt


def suite(zr, zi, cr, ci):
    for n in range(1, 100):
        nzr = zr ** 2 - zi ** 2 + cr
        nzi = 2 * zr * zi + ci
        if nzr ** 2 + nzi ** 2 > 4:
            return n
        zr = nzr
        zi = nzi
    # if we standed 50 rounds, return -1
    return -1

def plot_mandelbrot(canvas, nx, ny):
    minx, maxx, miny, maxy = canvas
    # compute steps in x and y
    dx = (maxx - minx) / nx
    dy = (maxy - miny) / ny
    # fill img, with nx rows and ny cols
    img = []
    for iy in range(ny):
        # compute current y value
        y = miny + iy * dy
        line = []
        for ix in range(nx):
            # compute current x value
            x = minx + ix * dx
            # fill current value
            line.append(suite(0, 0, x, y))
        img.append(line)
    return img

def plot_julia(canvas, nx, ny, arg1, arg2):
    minx, maxx, miny, maxy = canvas
    # compute steps in x and y
    dx = (maxx - minx) / nx
    dy = (maxy - miny) / ny
    # fill img, with nx rows and ny cols
    img = []
    for iy in range(ny):
        # compute current y value
        y = miny + iy * dy
        line = []
        for ix in range(nx):
            # compute current x value
            x = minx + ix * dx
            # fill current value
            line.append(suite(x, y, arg1, arg2))
        img.append(line)
    return img

def showimg(img, canvas=(-1.1, 1.1, -1.1, 1.1), cmap='plasma', filename='set.svg'):
    plt.imshow(
        img,
        cmap=plt.cm.get_cmap(cmap),
        interpolation="none",
        extent=canvas,
    )
    plt.savefig(filename)
    plt.show()


if __name__ == "__main__":
    canvas = [-1.6, 1.1, -1.1, 1.1]
    nx = 800
    ny = 800
    img = plot_mandelbrot(canvas, nx, ny)
    showimg(img, canvas)


def cmd_mandel():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Generate mandelbrot set.')
    parser.add_argument('--minx', type=float, default=-1.6, help="canvas minimum x")
    parser.add_argument('--maxx', type=float, default=1.1, help="canvas maximum x")
    parser.add_argument('--miny', type=float, default=-1.1, help="canvas minimum y")
    parser.add_argument('--maxy', type=float, default=1.1, help="canvas maximum y")
    parser.add_argument('--width', type=int, default=800, help="image width")
    parser.add_argument('--height', type=int, default=800, help="image height")
    parser.add_argument('--colormap', default="magma", help="matplotlib colormap")
    
    args = parser.parse_args()
    canvas = (args.minx, args.maxx, args.miny, args.maxy)
    
    img = plot_mandelbrot(canvas, args.width, args.height)
    showimg(img, canvas, args.colormap)

def cmd_julia():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Generate julia set.')
    parser.add_argument('number', metavar='N', type=float, help='julia number generator', nargs='*', default=[0.39, 0.03])
    parser.add_argument('--minx', type=float, default=-1.3, help="canvas minimum x")
    parser.add_argument('--maxx', type=float, default=1.3, help="canvas maximum x")
    parser.add_argument('--miny', type=float, default=-1.3, help="canvas minimum y")
    parser.add_argument('--maxy', type=float, default=1.3, help="canvas maximum y")
    parser.add_argument('--width', type=int, default=800, help="image width")
    parser.add_argument('--height', type=int, default=800, help="image height")
    parser.add_argument('--colormap', default="magma", help="matplotlib colormap")
    
    args = parser.parse_args()
    if not len(args.number) == 2:
        raise TypeError(f"julia take 0 or 2 arguments ({len(args.number)} given)")
    canvas = (args.minx, args.maxx, args.miny, args.maxy)
    
    img = plot_julia(canvas, args.width, args.height, args.number[0], args.number[1])
    showimg(img, canvas, args.colormap)
