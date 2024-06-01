# Kmean-applying

Kmean on real dataset

**Content list**

1. [Dataset](#about-dataset)
2. [Algorithm](#about-the-algorithm)

# About dataset

## Information

[<span style="color: #E6FF94">Dataset source</span>](https://archive.ics.uci.edu/dataset/553/clickstream+data+for+online+shopping)

The dataset contains information on clickstream from online store offering clothing for pregnant women
## Feature
|Name|type|Description|
|-|-|-|
|Year|Date|2008|
|Month|Date|From April to August|
|Order|Integer|Sequence of clicks during one session|
|Country|Categorical|Variable indicating the country of origin of the IP address|
|Session ID|Integer|Variable indicating session ID (short record)|
|Page 1 (main category)|Categorical|Concerns the main product category|
|Page 2 (clothing model)|Categorical|Contains information about the code for each group (217 product)|
|Colour|Categorical|Colour of product|
|Location|Categorical|Photo location on the page, the screen has been dividend into six part|
|Model photography|Categorical|Variable with two categories|
|Price|Integer|Price in USD|
|Price 2|Binary|Variable informing whether the price of a particular product is higher than the average price for the entire product category|
|Page|Integer|Page number within the e-store website (1-5)

There are two Feature to notice that ```clothing model``` and ```price```

# About the algorithm

>K-means


