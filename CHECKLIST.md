## Project checklist

Please note that all the lists are *exhaustive* meaning that I do not expect you to have completed very
point on the checklist for the exam.

### Week 1

- [x] Create a git repository
- [x] Make sure that all team members have write access to the github repository
- [x] Create a dedicated environment for you project to keep track of your packages (using conda)
- [x] Create the initial file structure using cookiecutter
- [ ] Fill out the `make_dataset.py` file such that it downloads whatever data you need and
- [x] Add a model file and a training script and get that running
- [x] Remember to fill out the `requirements.txt` file with whatever dependencies that you are using
- [x] Remember to comply with good coding practices (`pep8`) while doing the project
- [x] Do a bit of code typing and remember to document essential parts of your code
- [x] Setup version control for your data or part of your data
- [x] Construct one or multiple docker files for your code
- [x] Build the docker files locally and make sure they work as intended -> (training works assuming data has been downloaded and processed)
- [ ] Write one or multiple configurations files for your experiments
- [x] Used Hydra to load the configurations and manage your hyperparameters
- [ ] When you have something that works somewhat, remember at some point to to some profiling and see if you can optimize your code
- [x] Use wandb to log training progress and other important metrics/artifacts in your code -> (should be checked)
- [ ] Use pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

- [x] Write unit tests related to the data part of your code
- [x] Write unit tests related to model construction
- [ ] Calculate the coverage.
- [x] Get some continues integration running on the github repository
- [x] (optional) Create a new project on `gcp` and invite all group members to it
- [x] Create a data storage on `gcp` for you data
- [ ] Create a trigger workflow for automatically building your docker images
- [ ] Get your model training on `gcp`
- [x] Play around with distributed data loading
- [ ] (optional) Play around with distributed model training
- [ ] Play around with quantization and compilation for you trained models

### Week 3

- [ ] Deployed your model locally using TorchServe
- [ ] Checked how robust your model is towards data drifting
- [x] Deployed your model using `gcp`
- [x] Monitored the system of your deployed model
- [ ] Monitored the performance of your deployed model

### Additional

- [x] Revisit your initial project description. Did the project turn out as you wanted?
- [x] Make sure all group members have a understanding about all parts of the project
- [x] Create a presentation explaining your project
- [x] Uploaded all your code to github
- [ ] (extra) Implemented pre-commit hooks for your project repository
- [ ] (extra) Used Optuna to run hyperparameter optimization on your model

## Exam and Presentation

The exam includes:
*	6 min presentation
*	10 min discussion

For the presentation we are going to keep a fairly strict format to get the exam rolling.

