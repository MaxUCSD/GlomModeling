# Project Structure

## Overview
This is just a copy of essentially my notes. 

So far we've got a few things. 
## Directory Structure

```
project/
├── environment.yml
├── README.md
├── manifoldsep/
│   ├── notes.md
│   └── visstuff.ipynb
└── modeling/
    ├── all_vars.png
    ├── docs.md
    ├── glomstatespace.html
    ├── just_concentration.py
    ├── test.py
    └── toymodel_vnoaobglom.py
```

## File Descriptions

### Root Directory
- **environment.yml** - Conda environment specification
- **README.md** - Project documentation

### manifoldsep/
- **notes.md** - Additional project notes
- **visstuff.ipynb** - Visualization notebook

### modeling/
- **all_vars.png** - Plot of each variable (r, c, s) over time in each glomerulus
- **docs.md** - Mathematical notes on the glomerular modeling
- **glomstatespace.html** - Interactive 3D figure of the glomerulus state space
- **just_concentration.py** - File for working with single differential equation (c)
- **test.py** - Random stuff for testing so I don't have to test in a working script
- **toymodel_vnoaobglom.py** - Main script for solving system of differential equations and plotting

## Notes
- The `Stimulus_Screen_Data/` directory is excluded from version control
