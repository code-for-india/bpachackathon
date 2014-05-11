Voter Analytics for Bangalore
=============================

The aim of this project is to analyze post-poll data of Bangalore, especially in regions where the voter turnout is lower than estimated. Although there can be several discrepancies which leads to low voter turn out such as mistakes in electoral rolls, mismatched voter IDs and missing name in polling days. This project aims to provide a voter analytics system for post-poll analysis.

Project Milestones and Progress
-------------------------------

| Milestones                                  | Status          |
| :-----------------------------------------: | :-------------: |
| Assembly Data Scraping                      | Complete        |
| Assembly Data Analysis                      | Complete        |
| Form 20 CSV Data Scraping                   | Complete        |
| Form 20 CSV Data Analysis                   | Complete        |
| Form 20 PDF Data Scraping                   | Complete        |
| Constituency wise Complete Data Gathering   | Complete        |
| Constituency wise Complete Data Scraping    | Complete        |
| Constituency wise Complete Data Analysis    | Complete        |
| Constituency wise Voter Data Scraping       | Complete        |
| Constituency wise Voter Data Analysis       | Complete        |
| Fuzzy Matching and Anomaly Detection        | Complete        |
| Chloropleth Visualization                   | Complete        |
| Porting project to AWS                      | Complete        |
| Persisting data to backend MySQL db         | Complete        |
| Exposing data through RESTful API           | Complete        |

## Features

### Voter Turnout Analysis on Assembly Constituency Data

This analysis gives a voter turnout for both male and female. The turnout is available for each parliamentary constituency in every district.

### Form 20 Data Analysis

Form 20 gives a deeper view to the electoral data. CEOs publish Form 20 after the election. In this project, we have worked on the 2014 Form 20 data for Hebbal constituency. The data was provided by BPAC.

### Constituency wise Data Analysis

Each constituency can be divided into different parts. Each part have their own polling booth where the number of actual voter turnout and number of registered voters available. For the Hebbal constituency, we have crawled 212 PDFs for each part and gathered registered voter data (male and female) for each part.

### Constituency wise Voter Data Analysis

Along with the registered voter data, each PDF also gives detailed information (Name, Husband/Mother/Fathers Name, Address, Sex and Age) for each voter. We have scraped each PDF file and gathered detailed information on each voter. This data will be used later for anomaly detection by fuzzy matching.

### Fuzzy Matching and Anomaly Detection

Currently undergoing.

### Chloropleth Visualization

Chloropleth is a visulization which shows the density on a map based on pre-defined values. We are aiming to show a constituency wise chloropleth map which will demonstrate the voter turnout area by area e.g. map visualizing total number of male voters, map visualizing total number of female voters, map visualizing total number of voters.
