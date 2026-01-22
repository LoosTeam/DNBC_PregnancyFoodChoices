# Food choices during pregnancy: evidence from 63,405 Danish women

This is a repository of code associated with the publication: **Food choices during pregnancy: evidence from 63,405 Danish women** by Erica Elizabeth Eberl, Anne Ahrendt Bjerregaard, Arnór Ingi Sigurdsson, Siddhi Yash Jain, Ann-Marie Hellerung Christiansen, Charlotta Granström, Matthew Paul Gillum, Thorhallur Ingi Halldórsson, Simon Rasmussen, Sjurdur Frodi Olsen, Ruth J.F. Loos, and Marta Guasch-Ferré.

As a part of this study, we developed **[DNBCFoodTextClassifier](https://huggingface.co/arnorsig/danish-food-classification)**, which is a [RøBÆRTa-base](https://huggingface.co/DDSC/roberta-base-danish) model fine-tuned for **multi-label classification of food entities from Danish text**. It has been trained to recognise **17 major categories** and **62 subcategories** of food items from Danish text using data from the Danish National Birth Cohort (DNBC). Specifically, this model was trained on a dataset consisting of 38,936 free-text responses to questions regarding specific foods that were introduced and avoided during pregnancy and tested on an additional 4326 responses from the same cohort.

### Types of classifications

**Major Categories:** 17 major food categories of foods and beverages, e.g. Dairy, Fruits, Vegetables and legumes, etc.

**Subcategories:** 62 specific food categories that were combined to create the 17 major food categories, e.g. Flavoured milks, Berries, Tropical fruits, Leaf and stem vegetables, etc.


## R scripts

## Using DNBCFoodTextClassifier on your own data