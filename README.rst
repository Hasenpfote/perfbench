|License| |Build Status| |PyPI version| |Pyversions|

perfbench
=========

About
-----

perfbench measures execution time of code snippets with Timeit and uses
Plotly to visualize the results.

Feature
-------

-  It is possible to select measurement modes.
-  It is possible to switch between layout sizes dynamically.
-  It is possible to switch between axes scales dynamically.
-  It is possible to switch between subplots dynamically.
-  The result of the benchmark can be saved locally as a html.
-  The result of the benchmark can be saved locally as a png. **Requires
   installation of**\ `orca <https://github.com/plotly/orca>`__\ **.**
   **When not to use the function, you do not need to install orca
   separately.**

Compatibility
-------------

perfbench works with Python 3.5 or higher.

Dependencies
------------

-  `tqdm <https://github.com/tqdm/tqdm>`__\ (4.6.1 or higher.)
-  `cerberus <https://github.com/pyeve/cerberus>`__\ (1.1 or higher.)
-  `plotly <https://github.com/plotly/plotly.py>`__\ (3.0.0 or higher)
-  `notebook <https://github.com/jupyter/notebook>`__\ (6.0 or higher.)
-  `ipywidgets <https://github.com/jupyter-widgets/ipywidgets>`__\ (7.2
   or higher.)

Installation
------------

::

   pip install perfbench

Usage
-----

**Plotting a single figure.**
`Here <https://plot.ly/~Hasenpfote/8/perfbench-demo1/>`__ is the
demonstration.

.. code:: python

   import numpy as np
   from perfbench import *


   bm = Benchmark(
       datasets=[
           Dataset(
               factories=[
                   lambda n: np.random.uniform(low=-1., high=1., size=n).astype(np.float64),
               ],
               title='float64'
           )
       ],
       dataset_sizes=[2 ** n for n in range(26)],
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
   )
   bm.run()
   bm.plot()

.. figure:: https://raw.githubusercontent.com/Hasenpfote/perfbench/master/docs/plotting_a_single_figure.png
   :alt: plot1

   plot1

**Plotting multiple plots on a single figure.**
`Here <https://plot.ly/~Hasenpfote/9/perfbench-demo2/>`__ is the
demonstration.

.. code:: python

   import numpy as np
   from perfbench import *


   bm = Benchmark(
       datasets=[
           Dataset(
               factories=[
                   lambda n: np.random.uniform(low=-1., high=1., size=n).astype(np.float16),
               ],
               title='float16'
           ),
           Dataset(
               factories=[
                   lambda n: np.random.uniform(low=-1., high=1., size=n).astype(np.float32),
               ],
               title='float32'
           ),
           Dataset(
               factories=[
                   lambda n: np.random.uniform(low=-1., high=1., size=n).astype(np.float64),
               ],
               title='float64'
           )
       ],
       dataset_sizes=[2 ** n for n in range(26)],
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
           ),
       ],
       xlabel='dataset sizes',
       title='around vs rint',
   )
   bm.run()
   bm.plot()

.. figure:: https://raw.githubusercontent.com/Hasenpfote/perfbench/master/docs/plotting_multiple_plots_on_a_single_figure.png
   :alt: plot2

   plot2

.. figure:: https://raw.githubusercontent.com/Hasenpfote/perfbench/master/docs/switching_between_subplots.png
   :alt: plot2

   plot2

**Switching between layout sizes.**

.. code:: python

   import numpy as np
   from perfbench import *


   bm = Benchmark(
       datasets=[
           Dataset(
               factories=[
                   lambda n: np.random.uniform(low=-1., high=1., size=n).astype(np.float64),
               ],
               title='float64'
           )
       ],
       dataset_sizes=[2 ** n for n in range(26)],
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

.. figure:: https://raw.githubusercontent.com/Hasenpfote/perfbench/master/docs/switching_between_layout_sizes.png
   :alt: plot3

   plot3

**Save as a html.**

.. code:: python

   # same as above
   bm.save_as_html(filepath='/path/to/file')

**Save as a png.**

.. code:: python

   # same as above
   bm.save_as_png(filepath='/path/to/file', width=1280, height=960)

**Other**
`Here <https://github.com/Hasenpfote/perfbench/tree/master/example>`__
are a few examples.

License
-------

This software is released under the MIT License, see LICENSE.

.. |License| image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: https://github.com/Hasenpfote/fpq/blob/master/LICENSE
.. |Build Status| image:: https://travis-ci.com/Hasenpfote/perfbench.svg?branch=master
   :target: https://travis-ci.com/Hasenpfote/perfbench
.. |PyPI version| image:: https://badge.fury.io/py/perfbench.svg
   :target: https://badge.fury.io/py/perfbench
.. |Pyversions| image:: https://img.shields.io/pypi/pyversions/perfbench.svg?style=flat
   :target: https://img.shields.io/pypi/pyversions/perfbench.svg?style=flat
