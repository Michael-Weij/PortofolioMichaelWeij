# Portfolio for the Minor Applied Data Science
### Michael Weij
### 18095593


## Index
- [Obligatory Criteria](#obligatory-criteria)
  - [Datacamp](#datacamp)
  - [Reflection and evaluation](#Reflection-and-evaluation)
- [Research Project](Research-Project)
# Obligatory Criteria


## Datacamp

[Introduction to Python](https://www.datacamp.com/statement-of-accomplishment/course/554729f2a11878960f7f3d97ca8c6178b644af7c) 

[Intermediate Python](https://www.datacamp.com/statement-of-accomplishment/course/0eb5f1987025547f325a9e355e09e5a80e7ac7bc) 

[Python Data Science Toolbox (Part 1)](https://www.datacamp.com/statement-of-accomplishment/course/53e82e830bc63d8fc671ddfd7814a478f8f046ab) 

[Python Data Science Toolbox (Part 2](https://www.datacamp.com/statement-of-accomplishment/course/78d8b2ad92768a2dbc2d6e4c158da8e3e22b046f) 

[Statistical Thinking in Python (Part 1)](https://www.datacamp.com/statement-of-accomplishment/course/48ea6cdef8cb819dbda46449238284414ed7bc47) 

[Supervised Learning with scikit-learn](https://www.datacamp.com/statement-of-accomplishment/course/85a331c3b32926601c03f50639c91554f44232c1) 

[Linear Classifiers in Python](https://www.datacamp.com/statement-of-accomplishment/course/e2dc07fcf6efe15ec097fdb76364fd5907bfc1b6)

[Introduction to Data Visualization with Matplotlib](https://www.datacamp.com/statement-of-accomplishment/course/dba41fa3c43486e93d92d434825ab11509ee5123) 

[cleaning Data in Python](https://www.datacamp.com/statement-of-accomplishment/course/8c5f0e48ef1c8c064b6e7d8e98f520453bcef507)

[Model Validation in Python](https://www.datacamp.com/statement-of-accomplishment/course/abc435b7514dc2d7c9d814966626efbb58d81d22)

[Machine Learning for time Series Data in Python](https://www.datacamp.com/statement-of-accomplishment/course/a1a264caed39c084ed05bab5ecab202e7690224c)

[Exploratory Data Analysis in Python](https://www.datacamp.com/statement-of-accomplishment/course/faa0836de8991f9eb06f70f0c8dfcd755c184a54) 

[Data manipulation with pandas](https://www.datacamp.com/statement-of-accomplishment/course/d1d0f8fd5574c94a9bfa094b117a6fca931613e9) 

[Manipulating Time Series Data in Python](https://www.datacamp.com/statement-of-accomplishment/course/65939c0efcc9f8a5a5e6026fd67b1a198be4fa62)

[Joining Data with pandas](https://www.datacamp.com/statement-of-accomplishment/course/7e3e95de91fc7f0c7ad089d7b8eaf096452bc1e1) 

[Cleaning Data in Python](https://www.datacamp.com/statement-of-accomplishment/course/8c5f0e48ef1c8c064b6e7d8e98f520453bcef507) 

[Time series Analysis in Python](https://www.datacamp.com/statement-of-accomplishment/course/040e699f0facaeed1e061d7d916734d7ac7e4b79) 


## Reflection and evaluation

### Reflection on own contribution to the project

#### Situation

#### Task

#### Action

#### Results

#### Reflection

### Reflection on own learning objectives.
#### Situation

#### Task

#### Action

#### Results

#### Reflection
 
### Evaluation on the group project as a whole.
#### Situation

#### Task

#### Action

#### Results

#### Reflection
 
## Research Project
Pipeline:
Gap creation
Data saving
Imputing KNMI Data
HotDeck
Imputing with Hotdeck
Implemented SoftImpute
Implemented LOCF 

## Predective Analytics
Havent done alot in this field 

## Domain knowledge
Read Literature
[Recurrent Neural Networks for Multivariate Time Series with Missing Values](https://www.nature.com/articles/s41598-018-24271-9)

[Flexible Imputation of missing Data](https://stefvanbuuren.name/fimd//)\
read the first part of the book: Part I: The basics

[Imputation of Clinical covariates in Time Series](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/Imputation%20of%20clinical%20covariates%20in%20time%20series.pdf)


## Data preprocessing
In the beginning albert and i started working with the Factory Zero house data and looking for a method to decide which house was the most complete with the least amount of data missing. The method we came up with was calculating the standard deviation over the timestamps and sorting it from there. We found out that house 054 had the least amount of data missing and decided this was the house we are gonna create the gaps in and impute.

For the impution method Hotdeck we needed to find suitable donors. We where using patern matching to look what was the best donor and impute it but if we did this over the 100+ houses it would never finish before the end of the year so we had to preselect a few donors before the patern matching. I wrote a few scoreboards to look which donor to use for  alklimaHeatpump op_mode, smartmeter power and temperature. For the ratio and interval data we used the average that came closest to the data what was going to be imputed. Because op_mode was nominal data we calculated the percentage of how many times each mode was active and looked for similar percentages in the other houses to select the donor.

[Scoreboard used for HotDeck](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Notebooks/scoreboard.ipynb)

## Communication

### Paper
When my other two group members started writing the paper. I was still trying to get resuls from a few imputation methods. After i was done getting results i started to make a LaTex template in Overleaf. In the end i converted the whole paper to LaTex and formatted the whole paper so it could be accepted for the CLIMA 2022 Conference. In the end i didn't write alot in the paper i just ended up reviewing and making corrections to the pieces other people wrote.

#### LaTeX 
Here underneath is the LaTeX code used for the template with the Bibliography. In the same folder are the files for the images and files for the Cambria, Cambria Bold and Cambria Italic font used in the template.

[LaTeX Code](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/paper/LaTeX%20Code.tex)

[Bibliography](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/paper/bibliography.bib)

### Presentations

#### Internal Presentations

#### External Presentations

#### Learning Lab
At first i was gonna do the learning lab with Albert about Hotdeck but then we decided it was not that interesting for the other groups. So we decided to delay the learning lab and do it about Hyper Parmeter Tuning because it would be more interesting for the other groups. 


[Learning Lab NoteBook](https://github.com/thuas-imp-2021/Learning-Lab/blob/main/genetic-algorithm.ipynb)\
[Learning Lab Presentation](https://github.com/thuas-imp-2021/Learning-Lab/blob/main/presentation.pdf)





