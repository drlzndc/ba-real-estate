# BA real estate lab

## About

This module contains data and notebooks used to analyze and model real estate prices in Bosnia and Herzegovina.  

## The Data

The data comes from [OLX.ba](https://olx.ba).  
Original raw data has been anonymized, and unneeded parameters have been removed.  
This processed data is then shared here, in the `data/processed/` folder.

## The Notebooks

The notebooks are meant to be read in the order indicated by their names.  
They perform exploratory data analysis (EDA) on the data, and build a couple of models to try and predict prices.  
Best model(s) are then stored in a shared `models/` folder (up one level), to be used by predictions web app, where users can get predicted price for a given set of features.
