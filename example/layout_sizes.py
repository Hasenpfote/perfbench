#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from perfbench import *


def main():
    bm = Benchmark(
        datasets=[
            Dataset(
                factories=[
                    lambda n: np.random.uniform(low=-1., high=1., size=n).astype(np.float64),
                ],
                title='float64'
            )
        ],
        dataset_sizes=[2 ** n for n in range(10)],
        kernels=[
            Kernel(
                stmt='np.around(DATASET)',
                setup='import numpy as np',
                label='around'
            ),
            Kernel(
                stmt='np.rint(DATASET)',
                setup='import numpy as np',
                label='rint'
            )
        ],
        xlabel='dataset sizes',
        title='around vs rint',
        layout_sizes=[
            LayoutSize(width=640, height=480, label='VGA'),
            LayoutSize(width=800, height=600, label='SVGA'),
            LayoutSize(width=1024, height=768, label='XGA'),
            LayoutSize(width=1280, height=960, label='HD 720p'),
        ]
    )
    bm.run()
    bm.plot()


if __name__ == '__main__':
    main()
