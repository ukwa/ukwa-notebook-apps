UKWA Notebook Apps
==================

This repository contains a set of Jupyter notebooks intended to be hosted as web applications via Voila.

They are for internal/staff use and depend on APIs that are not externally accessible.

Note that Voila does not automatically run-all-cells, but this can be forced by the notebook.

Development
-----------

To work on the notebooks, we can run Jupyter. Set up a virtual environment:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Then run Jupyter.

Alternatively, the notebooks can be developed within a general Jupyter deployment, like the BL Staff JupyterHub.


