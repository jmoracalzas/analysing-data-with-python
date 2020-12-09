# Project 1: Analysing data with Python 3 and Microsoft Excel  

## Introduction <br />
This projects was designed to facilitate learning activities. It focuses on utilising basic programming techniques to implement input, output, control flow, GUI development and finally integrating Python 3 and Microsoft Excel.

## Stages <br />
1. *Generation of data*<br />
This part of the project focuses on generating some sample data that will be manipulated at a later stage. This data will be stored in different file formats.

2. *Creation of a basic GUI* <br />
This section of the project will be used to explore the Tkinter module to create a basic GUI.

3. *An introduction to Python 3 and Microsoft Excel* <br />
This final block of the project will be an introduction to manipulating data in Python 3 and exporting the output on to Microsoft Excel.

## Tools and programming languages <br />
1. Python 3
2. Python libraries: Python Standard Library (random), Tkinter, Openpyxl
3. Microsoft Excel and text files

## Status
|**Element**                    |**Main Script**       |**User Interface**|
|:---                           |:---                  |:---              |
|Basic input of parameters      |Complete              |Complete          |
|Generation of interim data     |Complete              |Not applicable    |
|Output creation                |In progress           |Pending           |
|GUI styling                    |Not applicable        |Pending           |
|Customisation of user settings |Pending               |Pending           |
|Code optimisation              |In progress           |Not applicable    |

Output creation will consist of: .txt export (complete), .csv export (pending),  .xml (pending), .json (pending), Microsoft Excel export (complete) and SQLite (pending).

## Documentation <br />
### Requirements
The system must
- allow the user to input some parameters
- generate sample data based on user input
- store the created data in different file formats

### User stories
- As an analyst, I want to set the rules to generate the sample data so that the information is useful to other people
- As a finance professional, I want to choose the type of analysis the software will generate so that I can tailor the outcome
- As a finance professional, I want to easily understand the information provided so that I can use it to generate specific reports

### Conceptual model
- **Potential objects:** Rules, InterimData and Outcome
- **Relationships:** Rules **define** InterimData **builds** Outcome
- **Responsibilities:** *Rules* (holds input, generates data), *InterimData* (holds data, generates dataset), *Outcome* (holds dataset, disseminates report)

### Class diagrams

|**Rules**                     |                                   |
|:---                          |:---                               |
|**Attributes**                |**Responsibilities**               |
|- setNoYears --> integer      | + getNumYears(years)              |
|- setExpLines --> integer     | + getIncLinesMonth()              |
|- setIncLines --> integer     | + getExpLinesMonth()              |
|+ startDate --> date          | + generateReportingDates()        |

<br />

|**InterimData**                        |                                         |
|:---                                   |:---                                     |
|**Attributes**                         |**Responsibilities**                     |
| + expenditureType --> tuple(strings)  |                                         |
| + incomeType --> tuple(strings)       | - generateIncData()                     |
| + costCentre --> tuple(strings)       | - generateVarExp()                      |
| + intData --> list()                  | - generateFixedExp()                    |
|                                       | - appendData()                          | 

The interimDataset will feed from the following information: 1) cost centre and 2) **transaction type** (category, subcategory)<br />
<br />

|**Outcome**                   |                    |
|:---                          |:---                |
|**Attributes**                |**Responsibilities**|
|- setColumns                  |- txtOutput()       |
|                              | + exportReport()   |
