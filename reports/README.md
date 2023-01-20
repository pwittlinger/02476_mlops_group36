---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

--- Group 36 ---

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

--- s194727, s212460, s220051 ---

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

--- We used the HuggingFace transformers framework for doing text summarization. Specifically, we used a pre-trained Pegasus model and fine-tuned it on additional data. Pegasus is using the tokenizer library to process the input data. ---

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development enviroment, one would have to run the following commands*
>
> Answer:

--- As we needed to add new dependecies, we would install them in a specific environment created for the project, we would then list them into the requirements.txt file that we would update every time a new library was needed or every time one would not be needed anymore. To get a complete copy of our development enviroment, one would have to run the following commands : pip install -r requirements.txt.
This should be run in a new environment to ensure only the necessary packages are installed, as well as keeping versioning correct.---

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

--- From the cookiecutter template we have instantiated all the folders (docs, models, notebooks, references, reports, src, tests folder). We have removed the notebooks and references folder because we did not need them in our project. We have added a tests folder that contains unit tests for the project. ---

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

--- We did not implement any specific rules for code quality, however we made sure to follow good coding practices and we peer-reviewed each other's code in order to ensure readability. Good formating is especially important in big projects when several members will go over one's code and will have to easily understand it. These practices also ensure consistency along the project. Moreover, our code was checked with black, an python auto-formatter which is pep8 compliant.---

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement?**
>
> Answer:

--- We have skeletons for 3 tests, however these have not been implemented fully.
The idea is to check the input (shape, exists) to ensure reproducible results. For the model the idea would be to check for correct hyperparameters instantiation. ---

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> **Answer length: 100-200 words.**
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

--- The total coverage is 100% - which seems great to report if it wasn't for the fact that our tests are not properly implemented. It is not testing out entire code-base, and the tests
that we do have are very rudamentary (e.g. check shape of the data, is the model loaded correctly), thus coverage is not a meaningful metric in our project.
Moreover, if there are errors in the code that we have not written tests on, this will not be reported on the coverage report. Exactly these parts of our codebase,however, are more prone to error if nobody took responsibility of maintaining them. ---

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

--- We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in addition to the main branch. We also split the code into different features and although the branches did ot necessarily reflect individual features, they mainly focused on sparate aspects of the project. Then once a feature was complete by a team member, a PR would be issued and review by the other members in order to be merged with the main branch. In the last stage of the project, we realized that the full scale of our project was not realistic and we decided to make a "Lite" version which would include the Minimum Viable Product. ---

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

--- We marginally made use of version control in our project for training and testing data. This also helped improve reproducibility of model training. It was also convenient to have because Github cannot host the data, and our instantiated model is too large to save on github as well. Given the time we would like to expand the usage of DVC by adding data to our GCP buckets generated by the requests our model receives. Ideally, this would then retrigger the fine-tuning process and host a new version of our parametrized model on DVC   ---

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

--- We have several Github Actions setup, which includes code formatting (using isort, black, and flake8) in order to ensure readability and adherence to good coding practice.
Furthermore, we also integrated our unit-tests into an action, but since our unit tests are limited, the results are not very meaningful.  At first we ran these tests only on Python 3.8, but expanded this later to test from python 3.7 - 3.10.
Lastly, we set up a CI pipeline, which automatically builds a Docker Container and pushes that to the GCP Container registry, whenever a push is made on the main-branch. Ideally, this would then automatically deploy the newest (tested) version of our container, thus providing our app with the latest release.
In order to use that we needed to authenticate GCP with GitHub using Secrets (with the corresponding Access tokens)---

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

--- question 12 fill here ---

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

--- question 13 fill here ---

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

--- question 14 fill here ---

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

--- For our project, we mostly used Docker for inference and deployement. We used Docker to make predictions and handle curl requests and we also deployed it on GCP. ---

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

--- Most of the coding was relatively trivial and did not require heavy debugging. This also means that we did not profile our code. This would have been very useful if we had included much more code and loads of functions. In that case profiling can become necessary for later debugging. ---

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

--- The GCP services that we have used are: GCP Bucket, GCP Container Registry and GCP Cloud Run. Our Bucket is used for data storage, and we pull our trained model from there whenever we deploy a Docker Container. The Container Registry hosts the Containers we have build as described in Question 11
 and Cloud Run is for---

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 50-100 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

--- We have not made use of the Compute Engine during our project. We would primarily use it for model training in combination with GPU support.
For deploying the model we prefer the Cloud Run, as we do not need to manage the VMs ourself. ---

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

--- question 19 fill here ---

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

--- question 20 fill here ---

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

--- question 21 fill here ---

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

--- We managed to deploy our model locally. Given either a string on a curl request or a file containing said string, it will return a summarization of the string.
  *curl --header "Content-Type: application/json" --request POST --data '{"content":"string"}' http://127.0.0.1:8000/bert*---

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

--- We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could measure the performance in terms of rouge score, as well as the general usage of our model. This would inform us about the needs of our users, which would lead us to consider additional features.
  Moreover, we would like to know statistics on the input of our users, so we can see if there is a data drift (e.g. longer texts, different languages). ---

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

--- Two out of the three students barely used any credits on their accounts since only some testing was done. However the third group member spend around ---

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

--- question 25 fill here ---

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

--- The most important challenge of this project was the management. We had a hard time distributing the tasks and communicating together. We also had the misfortune of losing a group member the last week of the course. All of that led to our group having to reduce the initial scope of the project. However, on the technical plane, we did not encouter tools that were of great challenge.   ---

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

--- Student s212460 took care of initializing the Github repository and setting up the cookie cutter project. Student s220051 was in charge of fine tunig the model and the hyperparameters. Student s194727 take over the responsibility of assembling and containerizing the project in order to deploy it. Moreover, all members contributed somewhat equally in coding and publishing code in the Github repository. ---
