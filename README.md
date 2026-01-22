# Food choices during pregnancy: evidence from 63,405 Danish women

This is a repository of code associated with the publication: **Food choices during pregnancy: evidence from 63,405 Danish women** by Erica Elizabeth Eberl, Anne Ahrendt Bjerregaard, Arnór Ingi Sigurdsson, Siddhi Yash Jain, Ann-Marie Hellerung Christiansen, Charlotta Granström, Matthew Paul Gillum, Thorhallur Ingi Halldórsson, Simon Rasmussen, Sjurdur Frodi Olsen, Ruth J.F. Loos, and Marta Guasch-Ferré.

## DNBCFoodTextClassifier
As a part of this study, we developed **[DNBCFoodTextClassifier](https://huggingface.co/arnorsig/danish-food-classification)**, which is a [RøBÆRTa-base](https://huggingface.co/DDSC/roberta-base-danish) model fine-tuned for **multi-label classification of food entities from Danish text**. It has been trained to recognise **17 major categories** and **62 subcategories** of food items from Danish text using data from the Danish National Birth Cohort (DNBC). Specifically, this model was trained on a dataset consisting of 38,936 free-text responses to questions regarding specific foods that were introduced and avoided during pregnancy and tested on an additional 4326 responses from the same cohort.

### Classification scheme

**Major Categories:** 17 major food categories of foods and beverages, e.g. Dairy, Fruits, Vegetables and legumes, etc.

**Subcategories:** 62 specific food categories that were combined to create the 17 major food categories, e.g. Flavoured milks, Berries, Tropical fruits, Leaf and stem vegetables, etc.


## Explore the Model’s Performance

Explore the model’s performance using an interactive Shiny application:  
[DNBCFoodTextClassifier Shiny App](https://cbmr-rmpp.shinyapps.io/DNBCFoodTextClassifier/)

Here you can find the performance metrics for predicting different categories and additional plots with prediction scores and feature importance.


## Using the DNBCFoodTextClassifier

To use the model on your own data, you can follow the guide in our GitHub docs: [https://loosteam.github.io/DNBC_PregnancyFoodChoices](https://loosteam.github.io/DNBC_PregnancyFoodChoices/)

The example data, configuration files and and helper scripts can be found in the repository in the folder [prediction_tutorial](prediction_tutorial/) 

## Data preparation scripts


## Contact