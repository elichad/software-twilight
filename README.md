[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/elichad/software-twilight/main?urlpath=apps%2Findex.ipynb)
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

# software-twilight

Software end of project plans


## License
This project is licensed under the CC-BY license. You are free to:
* Share — copy and redistribute the material in any medium or format
* Adapt — remix, transform, and build upon the material for any purpose,
  even commercially.

The licensor cannot revoke these freedoms as long as you follow the license
terms.

The full text of the license can be found [here](https://github.com/elichad/software-twilight/blob/main/LICENSE.md).

## Introduction

Development of software under a fixed-term project should consider several
aspects of ongoing support after the project's end.  There are two main
eventualities:

1. the software's development abruptly ends;
2. there is some end-user support, although there will be no new feature development.

Each of these presents a problem. Ending support reduces the sustainability of the
environment, while ongoing maintenance requires the dedication of further
resources.

Under the software twilight plan, the project's developer will be aware of
necessary considerations.  This repository is intended to be used to assess and
guide a project maintainer in plans for the software's end of life.

We provide a tool to be used, _during the active development phase_, by a
project maintainer to assess and certify support plans for the project once
it will not longer be actively developed.  On completion of a short
questionnaire the user is offered a badge to add tothe repository to signal
to the community when, and how, the software will go gentle into its good
night.

## Available badges

We have badges which look look like and mean the following:
* BADGE1 - we have a (good) plan
* BADGE2 - twilight is coming up at THIS TIME
* BADGE3 - we followed a slightly different decision path

## Question themes

The tool covers a number of themes, including:
* potential funding for ongoing development
* required levels of future support
* deployment infrastructure required
* size of user community
* size of maintainer group
* status of ongoing contact with main developer(s)/development group

## Running

Follow "Launch binder".

## Design

The tool is designed in three parts: 

- The front-end is designed with Jupyer Notebooks. It uses Jupyter Widgets, `appmode` package and `mybinder.org` to display automatically the notebook cells as a web app. 
- The questions and answers are populated by the backend, that provides the appropriate next question based on the answer to the previous one, following a decision tree, until there are no more (relevant) questions to ask.
- Finally, all the answers are processed and one or more badges informing on the end-of-life status of the project are provided in the form of markdown text. A summary of the answers is also provided. This text can be easily pasted into the project README file. 

### Question format

The decision tree is populated from the file `decisions.py`.  This file
has quite customizable entries in the format described below.  This is
initially represented by a serialized Python dictionary.

We have a Python object `Question` which has attributes for the question
text and a dictionary for the answers (and links to each answer's follow-up
question).  Our input file is like:

```python
decision_tree = {
1: Question("Is this a question?", {"Yes": 2, "No", 3}),
2: Question("Is it a good question?", {"Yes": None, "No", 3}),
3: Question("Really!?", {"Yes": None, "No": None})
}
```

`decision_tree` is an object with (contiguous, [1,n]?) numeric identifier
and a `Question` object with question text and answer dictionary.  The
answer dictionary keys are answer text (diplayed) and the value the link to
the question to follow.

In this prototype there is no full decision tree.  We indicate the path to
follow by placing non-supported answers in parentheses.

### Customization of UI

If the UI can be readily customized, we describe here that.

## Further resources

Here we list related resources which may be of interest to the developer
of a sustainable project.  FAIRness, etc.

## Known issues

This is a proof of concept.  It is not complete.  We have a desire that the
following features are implemented:

* Improved decision tree input (not deserialization)
* BUG2
* BUG3
