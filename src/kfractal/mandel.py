"""Mandel Module"""
from argparse import ArgumentParser
import matplotlib.pyplot as plt

def suite(zr, zi, cr, ci, itermax=100):
    """return set"""
    for n in range(1, itermax):
        nzr = zr ** 2 - zi ** 2 + cr
        nzi = 2 * zr * zi + ci
        if nzr ** 2 + nzi ** 2 > 4:
            return n
        zr = nzr
        zi = nzi
    # if we standed 50 rounds, return -1
    return -1


def plot_mandelbrot(canvas, nx, ny):
    """return 2d array [ [], [] ] of mandelbrot"""
    #minx, maxx, miny, maxy = canvas
    # compute steps in x and y
    dx = (canvas[1] - canvas[0]) / nx
    dy = (canvas[3] - canvas[2]) / ny
    # fill img, with nx rows and ny cols
    img = []
    for iy in range(ny):
        # compute current y value
        y = canvas[2] + iy * dy
        line = []
        for ix in range(nx):
            # compute current x value
            x = canvas[0] + ix * dx
            # fill current value
            line.append(suite(0, 0, x, y))
        img.append(line)
    return img


def plot_julia(canvas, nx, ny, arg1, arg2):
    """return 2d array [ [], [] ] of julia"""
    #minx, maxx, miny, maxy = canvas
    # compute steps in x and y
    dx = (canvas[1] - canvas[0]) / nx
    dy = (canvas[3] - canvas[2]) / ny
    # fill img, with nx rows and ny cols
    img = []
    for iy in range(ny):
        # compute current y value
        y = canvas[2] + iy * dy
        line = []
        for ix in range(nx):
            # compute current x value
            x = canvas[0] + ix * dx
            # fill current value
            line.append(suite(x, y, arg1, arg2))
        img.append(line)
    return img


def showimg(img, canvas=(-1, 1, -1, 1), cmap="plasma", filename="set.svg"):
    """show 2d array with matplotlib"""
    plt.imshow(
        img,
        cmap=plt.cm.get_cmap(cmap),
        interpolation="none",
        extent=canvas,
    )
    plt.savefig(filename)
    plt.show()


if __name__ == "__main__":
    mandelcanvas = [-1.6, 1.1, -1.1, 1.1]
    mandelimg = plot_mandelbrot(mandelcanvas, 800, 800)
    showimg(mandelimg, mandelcanvas)


def add_cmdline_args(parser, defaultcanvas):
    """add the arguments in cmd_mandel and cmd_julia"""
    parser.add_argument(
        "--minx", type=float, default=defaultcanvas[0], help="canvas minimum x"
    )
    parser.add_argument(
        "--maxx", type=float, default=defaultcanvas[1], help="canvas maximum x"
    )
    parser.add_argument(
        "--miny", type=float, default=defaultcanvas[2], help="canvas minimum y"
    )
    parser.add_argument(
        "--maxy", type=float, default=defaultcanvas[3], help="canvas maximum y"
    )
    parser.add_argument("--width", type=int, default=800, help="image width")
    parser.add_argument("--height", type=int, default=800, help="image height")
    parser.add_argument("--colormap", default="magma", help="matplotlib colormap")
    return parser


def cmd_mandel():
    """used for the kmandel command"""
    parser = ArgumentParser(description="Generate mandelbrot set.")
    parser = add_cmdline_args(parser, (-1.6, 1.1, -1.1, 1.1))
    args = parser.parse_args()
    canvas = (args.minx, args.maxx, args.miny, args.maxy)

    img = plot_mandelbrot(canvas, args.width, args.height)
    showimg(img, canvas, args.colormap)


def cmd_julia():
    """used for the kjulia command"""
    parser = ArgumentParser(description="Generate julia set.")
    parser.add_argument(
        "number",
        metavar="N",
        type=float,
        help="julia number generator",
        nargs="*",
        default=[0.39, 0.03],
    )
    parser = add_cmdline_args(parser, (-1.3, 1.3, -1.3, 1.3))
    args = parser.parse_args()
    if not len(args.number) == 2:
        raise TypeError(f"julia take 0 or 2 arguments ({len(args.number)} given)")
    canvas = (args.minx, args.maxx, args.miny, args.maxy)

    img = plot_julia(canvas, args.width, args.height, args.number[0], args.number[1])
    showimg(img, canvas, args.colormap)
