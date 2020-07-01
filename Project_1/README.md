# Project 1: Analysing data with Python 3 and Microsoft Excel  

## Introduction <br>
This projects was designed to facilitate learning activities. It focuses on utilising basic programming techniques to implement input, output, control flow, GUI development and finally integrating Python 3 and Microsoft Excel.

## Stages <br>
1. *Generation of data*<br>
This part of the project focuses on generating some sample data that will be manipulated at a later stage.

2. *Creation of a basic GUI* <br>
This section of the project will be used to explore the Tkinter module to create a basic GUI.

3. *An introduction to Python 3 and Microsoft Excel* <br>
This final block of the project will be an introduction to manipulating data in Python 3 and exporting the output on to Microsoft Excel.

## Tools and programming languages <br>
1. Python 3
2. Microsoft Excel

## Documentation (based on Unified Modeling Language) <br>
### Requirements
The system must
- allow the user to input some parameters
- generate sample data based on user input
- analyse the sample data and output the results

### User stories
- As an analyst, I want to set the rules to generate the sample data so that the information is useful to other people
- As a finance professional, I want to choose the type of analysis the software will generate so that I can tailor the outcome
- As a finance professional, I want to easily understand the information provided so that I can use it to generate specific reports

### Conceptual model
- **Potential objects:** Rules, InterimData and Outcome
- **Relationships:** Rules **define** InterimData **builds** Outcome
- **Responsibilities:** *Rules* (holds input, generates data), *InterimData* (holds data, generates report), *Outcome* (holds report, disseminates report)

### Class diagrams

|**Rules**||
|:---|:---|
|**Attributes**|**Responsibilities**|
|- noYears integer|+ getInputx|
|- expLines integer | + generateData()|
|- incLines integer | |
<br>

|**InterimData**||
|:---|:---|
|**Attributes**|**Responsibilities**|
|- setInterimData|+ getInterimData()|
|- setReportSettings  | + getReportSettings()|
<br>

|**Outcome**||
|:---|:---|
|**Attributes**|**Responsibilities**|
|- setOutcome|+ generateReport()|
| | + sendReport()|

