# Portfolio for the Minor Applied Data Science
### Michael Weij
### 18095593


## Index
- [Obligatory Criteria](#obligatory-criteria)
  - [Datacamp](#datacamp)
  - [Reflection and evaluation](#Reflection-and-evaluation)
- [Research Project](#research-project)
  -[Research question and the following three subquestions](Research-question-and-the-following-three-subquestions)
  -[Future work](Future-work)
  -[Conclusion](Conclusion)
- [Domain knowledge](#Domain-knowledge)
- [Predictive Analystics](#Predictive-Analystics)
- [Communication](#Communication)
  -[Jira](#Jira)  
  - [Paper](#Paper)
  - [Presentations](#Presentations)
 

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
 
# Research Project
The project was about imputating missing data in building management systems. Because missing data can influence decision making in the end its important to try to fill in these gaps. Depending what is done with the data the method of imputation can differ. Because we didn't know what the end goal of the data was we calculated alot of different statistics on the imputaded data but in the end we settled for 4. Those where RMSE, VE, Kurtosis and Skewness. 

The data that we used for the project existed out of building management system data of hundred-twenty residential Net-Zero energy houses and data of twenty-five weather stations from the Royal Netherlands Meteorological Institute (KNMI).


|     Column   name       |     Dataset    |     Device               |     Unit of measurement    |     Measurement scale    |
|-------------------------|----------------|--------------------------|----------------------------|--------------------------|
|     Temperature         |     KNMI       |     -                    |     C (in 0.1c)            |     Interval             |
|     Global Radiation    |     KNMI       |     -                    |     j per cm²              |     Ratio                |
|     Humidity            |     KNMI       |     -                    |     %                      |     Ratio                |
|     Flow_temp           |     BMS        |     Alklima Heat Pump    |     C                      |     Interval             |
|     op_mode             |     BMS        |     Alklima Heat Pump    |     0-6 modes              |     Nominal              |
|     Power               |     BMS        |     Smartmeter           |     W                      |     Ratio                |
|     C02                 |     BMS        |     C02 Sensor           |     PPM                    |     Ratio                |


We created a pipeline to make it easier for us to evaluate the imputation methods on the same conditions. The pipeline handled the following tasks: creating gaps, imputing the artificial gaps, calculating imputation performance, and storing the evaluation results.


The artificial gap sizes we created for the building management system data:
|     Nr.    |     Min_size    |     Max_size     |     % Of   data    |
|------------|-----------------|------------------|--------------------|
|     1      |     5 min       |     60 min       |     15             |
|     2      |     1 hour      |     6 hours      |     4              |
|     3      |     6 hours     |     24 hours     |     1.5            |
|     4      |     24 hours    |     72 hours     |     0.5            |
|     5      |     72 hours    |     168 hours    |     0.01           |


## Research question and the following three subquestions
- Which imputation techniques should be applied for data imputation in building energy time series data?
  - What imputation methods are known for imputing time series data?
  - Which imputation techniques are best suited for what gap sizes?
  - What imputation techniques are best suited for which types of data?


## Future work
To build upon this research its important that the evaluated data should be less tested on metrics based on error but forecasting using the imputed data. This way its easier to see what effect the imputed data have on the end value and can make it easier to decide why to take a specific imputation method over the other. 

In this data set we only had numerical data and no ordinal data. To get the full vieuw of what imputation method to use for what type of data furthet research is required.


## Conclusion
To answer the first subquestion we read alot of literature on data imputation. After alot of testing we decided to use the following methods:

|     Method                              |     Abbreviation    |     Category          |     Description                                                    |     Library used                 |
|-----------------------------------------|---------------------|-----------------------|--------------------------------------------------------------------|----------------------------------|
|     Last Observation Carried Forward    |     LOCF            |     Simple            |     Use the last cell before the gap to fill a gap.              |     pandas.DataFrame.fillna      |
|     KNN regression                      |     KNN             |     Simple            |     Take the weighted average K-number of nearest neighbours.    |     sklearn.impute.KNNImputer    |
|     GRU RNN                             |     RNN             |     Neural Network    |     RNN   considers past values to impute missing data.            |     torch.nn.GRU                 |
|     Hot deck                            |     HD              |     Statistical       |     Take data from a different unit with a similar trend.        |     None                         |


From the results of both VE and RMSE can be concluded that there is no single best imputation method for all gap sizes and measurement scales. The best method for a gap size is dependent on the measurement scale of the to be imputed data.

We made a guidline for what method to use based on VE:
|                 |     Gap type 1.    |     Gap type 2.    |     Gap type 3.    |     Gap type 4.    |     Gap type 5.    |
|-----------------|--------------------|--------------------|--------------------|--------------------|--------------------|
|     Nominal     |     HD             |     HD             |     HD             |     HD             |     HD             |
|     Ratio       |     HD             |     HD             |     HD             |     HD             |     HD             |
|     Interval    |     RNN            |     RNN            |     RNN            |     RNN            |     RNN            |

We chose VE over RMSE because the focal point of the research was to impute the trends back into data and because RMSE doesnt take time shift in to account we decideded this was best.



# Domain knowledge
Read Literature:

[Recurrent Neural Networks for Multivariate Time Series with Missing Values](https://www.nature.com/articles/s41598-018-24271-9)

[Flexible Imputation of missing Data](https://stefvanbuuren.name/fimd//)

[Imputation of Clinical covariates in Time Series](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/Imputation%20of%20clinical%20covariates%20in%20time%20series.pdf)

[Comparison of different Methods for Univariate Time Series Imputation in R](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/Comparison%20of%20different%20Methods%20for%20Univariate%20Time%20Series%20Imputation%20in%20R.pdf)

[Comparison of imputation methods for missing laboratory data in medicine](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/Comparison%20of%20imputation%20methods%20for%20missing%20laboratory%20data%20in%20medicine.pdf)

[Forecasting residential gas consumption with machine learning algorithms on weather data](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/Forecastingresidentialgasconsumptionwithmachinelearningalgorithmsonweatherdata05-05-19.pdf)

[gaining insights into dwelling characteristics using machine learning for policy making on nearly zero-energy buildings with the use of smart meter and weather data](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/Gaining_insights_into_dwelling_characteristics_usi.pdf)

[A review of hot deck imputation for survey non-response](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/article/A%20review%20of%20hot%20deck%20imputation%20for%20survey%20non-response.pdf)
# Predictive Analystics
In the beginning albert and i started working with the Factory Zero house data and looking for a method to decide which house was the most complete with the least amount of data missing. The method we came up with was calculating the standard deviation between the time of the next datapoint.We calculated this for every house and we found out that house 054 had the least amount of data missing and decided this was the house we are gonna create the gaps in and impute.

Albert made the code to calculate the standard deviation between the time of the next datapoint and gave the following csv file\
[House Scoreboard](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/pythoncode/house_by_overall_std.csv)

## Gap creation
The first gap creation program i wrote\
[Gap creation](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/pythoncode/gap.py)

created gaps in the KNMI data so we could run some imputation tests in the beginning.\
[creating gaps in KNMI data](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/pythoncode/creating%20gaps.py)

## Data saving
I changed the evaluate code so that it was able to save the results it calculated.\
[evaluate](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Notebooks/evaluate.ipynb)\
With the following code we were able to save the results to csv files and graphs where exported to images. Adriaan cleaned up the code in the end.\
[Saving](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Notebooks/saving.ipynb)

## Hotdeck
In the middle of the minor Albert and I started to work on the method HotDeck this was a patern matching algohritm that looked for a donor with the same trend as the data that was going to be imputed. We did alot of research on Hotdeck and finaly started on implenting Hotdeck to the pipleline. Albert did the coding for it because it was out of my league to code the algorythm that did the patern matching. But we discussed alot on how to improve it. 

For the impution method Hotdeck we needed to find suitable donors. We where using patern matching to look what was the best donor and impute it but if we did this over the 100+ houses it would never finish before the end of the year so we had to preselect a few donors before the patern matching. I wrote a few scoreboards to look which donor to use for  alklimaHeatpump op_mode, smartmeter power and temperature. For the ratio and interval data we used the average that came closest to the data what was going to be imputed. Because op_mode was nominal data we calculated the percentage of how many times each mode was active and looked for similar percentages in the other houses to select the donor.

## Imputing with Hotdeck
By using the scoreboard for the donors i tested alot of different houses amount of donors to see what works best and confirm if the donors we selected where actaully the best donors. Selecting donors that where supposed to be good and donors who where supossed to bad i tried to confirm that it works. This testing took quite some time because hotdeck was at this stage not as fast as it is now. This was because Albert was still trying to implement vectorisation to speed up the progress.

[Code to see what donors to use for HotDeck](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Notebooks/scoreboard.ipynb)


## Implemented SoftImpute
Tried a method called Softimpute from the libray Fancyimpute this method didnt seem to get great results so we dropped in the end for the paper.\
[SoftImpute](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Notebooks/softimpute.ipynb)
## Implemented LOCF 
Last Obervation Carried Forward was a simple imputation method that uses either the data before the gap or behind the gap to fill it in. It gave quite good results on the smaller gaps but failed on bigger gaps.\
[LOCF](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Notebooks/fillna.ipynb)

# Communication
## Jira
We used jira to divide the work what was needed to be done. We started with sprints of 2 weeks but later decided that this wasnt long enough and we started doing sprints of around 3  weeks. 
The progress on the Jira board:
![Jira Progress](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/pdfsandimages/WhatsApp%20Image%202022-01-13%20at%2015.44.42.jpeg)
## Paper
When my other two group members started writing the paper. I was still trying to get resuls from a few imputation methods. After i was done getting results i started to make a LaTex template in Overleaf. In the end i converted the whole paper to LaTex and formatted the whole paper so it could be accepted for the CLIMA 2022 Conference. In the end i didn't write alot in the paper i just ended up reviewing and making corrections to the pieces other people wrote.

### LaTeX 
Here underneath is the LaTeX code used for the template with the Bibliography. In the same folder are the files for the images and files for the Cambria, Cambria Bold and Cambria Italic font used in the template.

[LaTeX Code](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/paper/LaTeX%20Code.tex)

[Bibliography](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/paper/bibliography.bib)

## Presentations

### Internal Presentations
[Internal Presentation week 6](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/pdfsandimages/Team%20IMP%20-%20Internal%20presentation%20week6.pdf)
### External Presentations
[External Presentation week 6](https://github.com/Michael-Weij/PortofolioTHUAS/blob/main/code/Team%20IMP%20-%20external%20presentation%20week6.pdf)
### Learning Lab
At first i was gonna do the learning lab with Albert about Hotdeck but then we decided it was not that interesting for the other groups. So we decided to delay the learning lab and do it about Hyper Parameter Tuning because it would be more interesting for the other groups. Adriaan explained me some basic concepts about Hyper parameter tuning and send me some literature to read about it. After that we made presentation and notebook together.

Both the notebook and presentationw we used for the learning lab\
[Learning Lab NoteBook](https://github.com/thuas-imp-2021/Learning-Lab/blob/main/genetic-algorithm.ipynb)\
[Learning Lab Presentation](https://github.com/thuas-imp-2021/Learning-Lab/blob/main/presentation.pdf)





