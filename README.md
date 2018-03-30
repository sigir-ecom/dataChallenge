# DataChallenge
Repository for dataChallenge related scripts of Rakuten data challenge: https://sigir-ecom.github.io/data-task.html

Challenge description:
This challenge focuses on the topic of large-scale taxonomy classification where the goal is to predict each product’s category as defined in the taxonomy tree given product's title. The cataloging of product listings through taxonomy categorization is a fundamental problem for any e-commerce marketplace, with applications ranging from personalized search recommendations to query understanding. For example, in the Rakuten.com catalog, “Dr. Martens Air Wair 1460 Mens Leather Ankle Boots” is categorized under the “Clothing, Shoes & Accessories -> Shoes -> Men -> Boots” leaf. However, manual and rule based approaches to categorization are not scalable since commercial product taxonomies are organized in tree structures with three to ten levels of depth and thousands of leaf nodes. Advances in this area of research have been limited due to the lack of real data from actual commercial catalogs. The challenge presents several interesting research aspects due to the intrinsic noisy nature of the product labels, the size of modern eCommerce catalogs, and the typical unbalanced data distribution. 

Dataset details:
As part of this challenge, Rakuten will be releasing 1M product listings in tsv format, including the train (0.8M) and test set (0.2M), consisting of product titles and their corresponding category ID paths. The followings are some examples from the training set,

Title 	CeategoryIdPath

Replacement Viewsonic VG710 LCD Monitor 48Watt AC Adapter 12V 4A   	3292>114>1231

Ka-Bar Desert MULE Serrated Folding Knife  	4238>321>753>3121

5.11 TACTICAL 74280 Taclite TDU Pants, R/M, Dark Navy  	4015>3285>1443>20

Skechers 4lb S Grip Jogging Weight set of 2- Black  	2075>945>2183>3863

The test set will contain only the title field and the goal is to predict the CeategoryIdPath for each title.

Metrics/ Evalutation:

The final evaluation metrics will be micro-Precision, micro-Recall, and micro-F1 on the test set of EXACT CategoryIdPath match. Please note that partial path match does not count as a correct match. 

