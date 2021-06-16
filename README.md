# CSV_File_Processor
In this project I implement hierarchical clustering to process a stupid but fun CSV file. 
With some modification, this processor can process any real-world data.

Using the publicly available Pokemon stats, I am performing clustering on these stats. Each Pokemon is defined by a row in the data set. Because there are various ways to characterize how strong a Pokemon is, it is often desirable to convert a raw stats sheet into a shorter feature vector. For this project, I will represent a Pokemon's strength by two numbers: "x" and "y". "x" will represent the Pokemon's total offensive strength, which is defined by Attack + Sp. Atk + Speed. Similarly, "y" will represent the Pokemon's total defensive strength, which is defined by Defense + Sp. Def + HP. After each Pokemon becomes that two-dimensional feature vector, you will cluster the first 20 Pokemon with hierarchical agglomerative clustering (HAC).
