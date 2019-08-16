import numpy as np


def mpc(pf, beta):
    pfq = np.sqrt(1-pf**2)
    bus = np.array([[1,   4,   -1,  1,       1,       50,      -50,     50,      -50,         0,        0,      6,      -6],
    [2,   1,    1,   1.05,    0.95,    0,       0,       0,        0,         1.5*beta, 0,    0.5*beta, -0.5*beta],
    [3,   4,    2,   1.05,    0.95,    0,       0,       0,        0,         0,        0,     1.2,     1.2],
    [4,   1,    3,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,      0],
    [5,   1,    4,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,       0],
    [6,   1,    5,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,       0],
    [7,   1,    6,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,       0],
    [8,   1,    7,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,       0],
    [9,   1,    8,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,       0],
    [10,  1,    9,   1.05,    0.95,    0,       0,       0,        0,         0,        0,       0,       0],
    [11,  2,    10,  1.05,    0.95,    0.67*pf, 0,   0.67*pfq,     0,         0,        0,       0,       0],
    [12,  2,    11,  1.05,    0.95,    0.45*pf,  0,  0.45*pfq,     0,         0,        0,       0,       0],
    [13,  2,    3,   1.05,    0.95,    0.89*pf,  0,  0.89*pfq,     0,         0,        0,       0,      0],
    [14,  1,    4,   1.05,    0.95,    0,        0,      0,        0,         0,        0,       0,       0],
    [15,  2,    15,  1.05,    0.95,    0.07*pf,  0,  0.07*pfq,     0,         0.4*beta, 0,       0.1*beta, -0.1*beta],
    [16,  2,    15,  1.05,    0.95,    0.67*pf,  0,  0.67*pfq,     0,         1.5*beta, 0,       0.5*beta, -0.5*beta],
    [17,  1,    4,   1.05,    0.95,    0,        0,       0,       0,         0,        0,       0,       0],
    [18,  2,    20,  1.05,    0.95,    0.45*pf,  0,  0.45*pfq,     0,         2.0*beta, 0,       0.6*beta, -0.6*beta],
    [19,  2,    21,  1.05,    0.95,   2.23*pf,   0,  2.23*pfq,     0,         1.0*beta, 0,       0.3*beta, -.3*beta],
    [20,  2,    19,  1.05,    0.95,   0.45*pf,   0,  0.45*pfq,     0,         0,        0,       0,       0],
    [21,  2,    5,   1.05,    0.95,    0.2*pf,   0,   0.2*pfq,     0,         0,        0,       0,       0],
    [22,  1,    6,   1.05,    0.95,    0,        0,       0,       0,         0,        0,       0,      0],
    [23,  2,    27,  1.05,    0.95,    0.13*pf,  0,  0.13*pfq,     0,         0,        0,       0,       0],
    [24,  2,    28,  1.05,    0.95,    0.13*pf,  0,  0.13*pfq,     0,         0,        0,       0,       0],
    [25,  2,    29,  1.05,    0.95,    0.2*pf,   0,   0.2*pfq,     0,         0,        0,       0,       0],
    [26,  2,    30,  1.05,    0.95,    0.07*pf,  0,  0.07*pfq,     0,         0,        0,       0,       0],
    [27,  2,    7,   1.05,    0.95,    0.13*pf,  0,  0.13*pfq,     0,         0,        0,       0,      0],
    [28,  2,    32,  1.05,    0.95,    0.27*pf,  0,  0.27*pfq,     0,         0,        0,       0,       0],
    [29,  2,    33,  1.05,    0.95,    0.2*pf,   0,   0.2*pfq,     0,         0,        0,       0,       0],
    [30,  1,    8,   1.05,    0.95,    0,        0,       0,       0,         0,        0,       0,      0],
    [31,  2,    35,  1.05,    0.95,    0.27*pf,  0,  0.27*pfq,     0,         0,        0,       0,       0],
    [32,  4,    35,  1.05,    0.95,    0,        0,       0,       0,         0,        0,       1.8,   1.8],
    [33,  2,    35,  1.05,    0.95,    0.45*pf,  0,  0.45*pfq,     0,         0,        0,       0,       0],
    [34,  2,    8,   1.05,    0.95,    1.34*pf,  0,  1.34*pfq,     0,         0,        0,       0,       0],
    [35,  2,    8,   1.05,    0.95,    0.13*pf,  0,  0.13*pfq,     0,         0,        0,       0,       0],
    [36,  2,    8,   1.05,    0.95,    0.67*pf,  0,  0.67*pfq,     0,         0,        0,       0,       0],
    [37,  2,    9,   1.05,    0.95,    0.13*pf,  0,  0.13*pfq,     0,         0,        0,       0,       0],
    [38,  1,    42,  1.05,    0.95,    0,        0,       0,       0,         0,        0,       0,       0],
    [39,  2,    43,  1.05,    0.95,    0.45*pf,  0,  0.45*pfq,     0,         0,        0,       0,       0],
    [40,  2,    43,  1.05,    0.95,    0.2*pf,   0,  0.2*pfq,      0,         0,        0,       0,       0],
    [41,  2,    10,  1.05,    0.95,    0.45*pf,  0,  0.45*pfq,     0,         0,        0,       0,       0],
    [42,  4,    11,  1.05,    0.95,    0,        0,       0,       0,         0,        0,       1.8,   1.8]])

    branch = np.array([[1,    2,   0.259/152.5225,   0.808/152.5225],
    [2,    3,   0.031/152.5225,   0.092/152.5225],
    [3,    4,   0.046/152.5225,   0.092/152.5225],
    [3,    13,  0.092/152.5225,   0.031/152.5225],
    [3,    14,   0.214/152.5225,   0.046/152.5225],
    [4,    5,   0.107/152.5225,   0.183/152.5225],
    [4,   17,  0.336/152.5225,  0.061/152.5225],
    [5,   6,   0.015/152.5225,   0.031/152.5225],
    [5,   21,  0.061/152.5225,   0.015/152.5225],
    [6,   7,   0.031/152.5225,   0.046/152.5225],
    [6,   22,  0.168/152.5225,   0.061/152.5225],
    [7,    8,   0.015/152.5225,   0.015/152.5225],
    [7,   27,  0.076/152.5225,   0.015/152.5225],
    [8,  9,   0.031/152.5225,   0.046/152.5225],
    [8,    30,  0.076/152.5225,   0.015/152.5225],
    [8,   34,  0.244/152.5225,   0.046/152.5225],
    [8,    35,  0.046/152.5225,   0.015/152.5225],
    [8,   36,  0.107/152.5225,   0.031/152.5225],
    [9,    10,  0.015/152.5225,   0.015/152.5225],
    [9,    37,  0.153/152.5225,   0.046/152.5225],
    [10,   11,  0.107/152.5225,   0.076/152.5225],
    [10,   41,  0.229/152.5225,   0.122/152.5225],
    [11,   12,  0.076/152.5225,   0.046/152.5225],
    [11,   42,  0.031/152.5225,   0.015/152.5225],
    [14,   15,  0.107/152.5225,   0.015/152.5225],
    [14,   16,  0.046/152.5225,   0.015/152.5225],
    [17,   18,  0.122/152.5225,   0.092/152.5225],
    [17,   20,  0.214/152.5225,   0.046/152.5225],
    [18,   19,  0.198/152.5225,   0.046/152.5225],
    [22,   23,  0.107/152.5225,   0.031/152.5225],
    [22,   26,  0.046/152.5225,   0.015/152.5225],
    [23,   24,  0.107/152.5225,   0.031/152.5225],
    [24,   25,  0.061/152.5225,   0.015/152.5225],
    [27,   28,  0.046/152.5225,   0.015/152.5225],
    [28,   29,  0.031/152.5225,   0.015/152.5225],
    [30,   31,  0.076/152.5225,   0.015/152.5225],
    [30,  32,  0.076/152.5225,   0.046/152.5225],
    [30,   33,  0.107/152.5225,   0.015/152.5225],
    [37,   38,  0.061/152.5225,   0.015/152.5225],
    [38,   39,  0.061/152.5225,   0.015/152.5225],
    [38,   40,  0.061/152.5225,   0.015/152.5225]])
    return bus, branch