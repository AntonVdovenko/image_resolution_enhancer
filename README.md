# Image Upscaling Service
Simple app to enhance image resolution

## Tools used in this project
* [waifu2x](https://github.com/nagadomi/waifu2x)



## Project structure
```bash
.
├── config                      
├── data            
├── docs                            # documentation for your project
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
```

## Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make activate
make setup
```

## Install new packages
To install new PyPI packages, run:
```bash
poetry add <package-name>
```

## Docker Instructions

### Easy use case
If you dont need/want buil image on your own you can pull image from Docker Hub

```bash
docker pull vdovenkoanton/streamlit-image-upscale
```

### Image Building

Navigate to the project directory
```bash
cd image_resolution_enhancer
```

Build the Docker image
```bash
docker build -t streamlit-image-upscale .
```

### Run container

Only run container with CUDA if you have CUDA Docker Toolkit installed !

Run the Docker container with CUDA support and mount the data directory
```bash
docker run --gpus all -p 8501:8501 -v $(pwd)/data:/app/data streamlit-image-upscale
```

Run the Docker container and mount the data directory
```bash
docker run -p 8501:8501 -v $(pwd)/data:/app/data streamlit-image-upscale
```
