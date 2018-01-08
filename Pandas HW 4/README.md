
#Heroes of Pymoli Data Analysis

##Observations

    * Males are the largest percentage of players and purchasers
    * Purchases made by 20 - 29 year old players are larger than all other age groups combined
    * The most popular items are below average cost, with the exception of Distribution Axe (dataset 1) that is the most profitable item as well

#Import Data


```python
import pandas as pd
import os
import json

purchase_data = os.path.join("Resources","purchase_data.json")
    
with open(purchase_data) as datafile:
    data = json.load(datafile)
purchase_data_pd = pd.DataFrame(data)    

purchase_data_pd.head()
```


```python
#purchase_data_pd['SN'].nunique()
```

#Player Count


```python
Players = purchase_data_pd ["SN"].value_counts()

TotalPlayers = len (Players)
print("Total Players:  ",TotalPlayers)
```

    Total Players:   573
    

#Purchasing Analysis (Total)


```python
Items = purchase_data_pd ["Item Name"].value_counts()

NumberOfItems = len (Items)
NumberOfPurchases = (len (purchase_data_pd))
TotalRevenue = purchase_data_pd["Price"].sum()
AveragePrice = TotalRevenue/NumberOfPurchases

PurchaseAnalysis = pd.DataFrame({"Number of Unique Items":[NumberOfItems],"Average Price":[AveragePrice],"Number of Purchases":[NumberOfPurchases],"Total Revenue":[TotalRevenue]})

PurchaseAnalysis["Average Price"] = PurchaseAnalysis["Average Price"].map("${0:,.2f}".format)
PurchaseAnalysis["Total Revenue"] = PurchaseAnalysis["Total Revenue"].map("${0:,.2f}".format)

#This command is needed to rearrange the columns in the correct order -- they print out of order otherwise  
PurchaseAnalysis = PurchaseAnalysis[["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"]]    
PurchaseAnalysis



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



#Gender Demographics


```python
Players_df= purchase_data_pd[["SN","Gender","Age"]]
#print (Players_df.shape)
Players_df.drop_duplicates(inplace=True)
#print (Players_df.shape)

total_gender = Players_df["Gender"].count()
male = Players_df["Gender"].value_counts()["Male"]
percent_male = male/total_gender * 100
female = Players_df["Gender"].value_counts()["Female"]
percent_female = female/total_gender * 100
non_gender_specific = total_gender - male - female
percent_ng_specific = non_gender_specific/total_gender * 100

GenderDemo = pd.DataFrame({"Gender":["Male", "Female", "Other/Non-Disclosed"],"Percentage of Players":[percent_male, percent_female, percent_ng_specific],"Total Count":[male, female, non_gender_specific]})


GenderDemo["Percentage of Players"] = GenderDemo["Percentage of Players"].map("{0:,.2f}".format)

GenderDemo

```

    C:\Users\sboxberg\Anaconda3\envs\PythonData\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other/Non-Disclosed</td>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



#Purchasing Analysis (Gender)


```python
male_purchases = purchase_data_pd[purchase_data_pd["Gender"] == "Male"]
female_purchases = purchase_data_pd[purchase_data_pd["Gender"] == "Female"]
other_purchases = purchase_data_pd[purchase_data_pd["Gender"] == "Other / Non-Disclosed"]

male_purchase_count = len (male_purchases)
female_purchase_count = len (female_purchases)
other_purchase_count = len (other_purchases)

male_purchase_ave = male_purchases["Price"].mean()
female_purchase_ave = female_purchases["Price"].mean()
other_purchase_ave = other_purchases["Price"].mean()

male_purchase_total = male_purchases["Price"].sum()
female_purchase_total = female_purchases["Price"].sum()
other_purchase_total = other_purchases["Price"].sum()

male_purchase_norm = male_purchase_total/male
female_purchase_norm = female_purchase_total/female
other_purchase_norm = other_purchase_total/non_gender_specific

GenderPurchase = pd.DataFrame({"Gender":["Male", "Female", "Other/Non-Disclosed"],
                               "Purchase Count":[male_purchase_count, female_purchase_count, other_purchase_count],
                               "Average Purchase Price":[male_purchase_ave, female_purchase_ave, other_purchase_ave],
                               "Total Purchase Value":[male_purchase_total, female_purchase_total, other_purchase_total],
                               "Normalized Totals":[male_purchase_norm, female_purchase_norm, other_purchase_norm]})

# Format
GenderPurchase["Average Purchase Price"] = GenderPurchase["Average Purchase Price"].map("${0:,.2f}".format)
GenderPurchase["Total Purchase Value"] = GenderPurchase["Total Purchase Value"].map("${0:,.2f}".format)
GenderPurchase["Normalized Totals"] = GenderPurchase["Normalized Totals"].map("${0:,.2f}".format)

#Needed to rearrange the columns
GenderPurchase = GenderPurchase[["Gender", "Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
GenderPurchase
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other/Non-Disclosed</td>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



#Age Demographics


```python
bins = [0, 10, 14, 19, 24, 29, 34, 39, 999]
bin_names = ['<10', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40+']

#Added the extra cutting of Player data due to the stupid normalization total :)

purchase_data_pd["Age Group"] = pd.cut(purchase_data_pd["Age"], bins, labels=bin_names)
Players_df["Age Group"] = pd.cut(Players_df["Age"], bins, labels=bin_names)

purchase_groups_by_age = purchase_data_pd.groupby("Age Group")
players_groups_by_age = Players_df.groupby ("Age Group")

PurchaseCount = purchase_groups_by_age["Age Group"].count()
PlayerCount = players_groups_by_age["Age Group"].count()

TotalPurchase = purchase_groups_by_age["Price"].sum()
AveragePurchasePrice = TotalPurchase/PurchaseCount

NormalizedTotal = TotalPurchase/PlayerCount

PurchaseAnalysisAge = pd.DataFrame({"Purchase Count":PurchaseCount,
                                    "Average Purchase Price": AveragePurchasePrice, "Total Purchase Value":TotalPurchase,
                                   "Normalized Totals":NormalizedTotal})

PurchaseAnalysisAge["Average Purchase Price"] = PurchaseAnalysisAge["Average Purchase Price"].map("${0:,.2f}".format)
PurchaseAnalysisAge["Total Purchase Value"] = PurchaseAnalysisAge["Total Purchase Value"].map("${0:,.2f}".format)
PurchaseAnalysisAge["Normalized Totals"] = PurchaseAnalysisAge["Normalized Totals"].map("${0:,.2f}".format)

#Needed for correct column arrangement on output
PurchaseAnalysisAge = PurchaseAnalysisAge [["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
PurchaseAnalysisAge

```

    C:\Users\sboxberg\Anaconda3\envs\PythonData\lib\site-packages\ipykernel_launcher.py:7: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      import sys
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10 - 14</th>
      <td>31</td>
      <td>$2.70</td>
      <td>$83.79</td>
      <td>$4.19</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.20</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$4.89</td>
    </tr>
  </tbody>
</table>
</div>



#Top Spenders


```python
purchase_groups_by_name = purchase_data_pd.groupby("SN")
```


```python
TotalPurchase_by_name = purchase_groups_by_name["Price"].sum()
PurchaseCount_by_name = purchase_groups_by_name["SN"].count()
AveragePrice_by_name = TotalPurchase_by_name/PurchaseCount_by_name

TopSpenders = pd.DataFrame({"Purchase Count":PurchaseCount_by_name,
                            "Average Purchase Price": AveragePrice_by_name,
                            "Total Purchase Value":TotalPurchase_by_name})

TopSpenders.sort_values("Total Purchase Value", ascending=False, inplace = True)

#order
TopSpenders=TopSpenders[["Purchase Count","Average Purchase Price", "Total Purchase Value"]]

#format
TopSpenders["Average Purchase Price"] = TopSpenders["Average Purchase Price"].map("${0:,.2f}".format)
TopSpenders["Total Purchase Value"] = TopSpenders["Total Purchase Value"].map("${0:,.2f}".format)


TopSpenders.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



#Most Popular Items


```python
purchase_groups_by_ID = purchase_data_pd.groupby("Item ID")

TotalPurchase_by_ID = purchase_groups_by_ID["Price"].sum()
PurchaseCount_by_ID = purchase_groups_by_ID["Item ID"].count()
ItemName_by_ID = purchase_groups_by_ID["Item Name"].first()
Price_by_ID = purchase_groups_by_ID["Price"].sum()/purchase_groups_by_ID["Price"].count()

#I struggled to get the Item Name and Price to pull in.  I finally decided to do that silly operation on price and the .first
#on ItemName to get it so I could add it to my dataframe correctly.  I'm sure I'm missing something obvious, but after hours
#of struggles, I was pretty pumped that I was able to figure out a workaround. :)

TopPurchases = pd.DataFrame({"Item Name": ItemName_by_ID,
                             "Purchase Count": PurchaseCount_by_ID, "Item Price":Price_by_ID,
                            "Total Purchase Value":TotalPurchase_by_ID})

#Need to sort the list for the final section first before formating -- just capturing an extra copy now before I format
TopPurchases_by_Value = TopPurchases.sort_values(["Total Purchase Value"], ascending = False)

TopPurchases.sort_values(["Purchase Count", "Total Purchase Value"], ascending=[False,False], inplace = True)


#order
TopPurchases=TopPurchases[["Item Name","Purchase Count", "Item Price","Total Purchase Value"]]

#format
TopPurchases["Item Price"] = TopPurchases["Item Price"].map("${0:,.2f}".format)
TopPurchases["Total Purchase Value"] = TopPurchases["Total Purchase Value"].map("${0:,.2f}".format)

TopPurchases.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>



#Most Profitable Items


```python
#order
TopPurchases_by_Value=TopPurchases_by_Value[["Item Name","Purchase Count", "Item Price","Total Purchase Value"]]

#format
TopPurchases_by_Value["Item Price"] = TopPurchases_by_Value["Item Price"].map("${0:,.2f}".format)
TopPurchases_by_Value["Total Purchase Value"] = TopPurchases_by_Value["Total Purchase Value"].map("${0:,.2f}".format)

TopPurchases_by_Value.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


