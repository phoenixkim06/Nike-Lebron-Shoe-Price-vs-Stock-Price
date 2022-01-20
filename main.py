from selenium import webdriver
from decimal import Decimal
import numpy as np
driver = webdriver.Chrome(executable_path="C:/seleniumdriver1/chromedriver.exe")

#Price X-Path
priceLebron = ['//*[@id="lebron01_mid_532"]/span[10]',
               '//*[@id="lebron02_mid_526"]/span[10]',
               '//*[@id="lebron03_mid_513"]/span[10]',
               '//*[@id="lebron04_mid_501"]/span[10]',
               '//*[@id="lebron5_mid_487"]/span[10]',
               '//*[@id="lebron6_mid_452"]/span[10]',
               '//*[@id="lebron7_mid_411"]/span[10]',
               '//*[@id="lebron8_mid_387"]/span[10]',
               '//*[@id="lebron9_mid_365"]/span[10]',
               '//*[@id="lebron10_mid_315"]/span[10]',
               '//*[@id="lebron11_mid_259"]/span[10]',
               '//*[@id="lebron12_mid_215"]/span[10]',
               '//*[@id="lebron13_mid_169"]/span[10]',
               '//*[@id="lebron14_mid_145"]/span[10]',
               '//*[@id="lebron15_mid_99"]/span[10]',
               '//*[@id="lebron16_mid_59"]/span[10]',
               '//*[@id="lebron17_mid_21"]/span[10]',
               '//*[@id="soldier1_mid_762"]/span[10]',
               '//*[@id="soldier2_mid_745"]/span[10]',
               '//*[@id="soldier3_mid_728"]/span[10]',
               '//*[@id="soldier4_mid_719"]/span[10]',
               '//*[@id="soldier5_mid_710"]/span[10]',
               '//*[@id="soldier6_mid_699"]/span[10]',
               '//*[@id="soldier7_mid_681"]/span[10]',
               '//*[@id="soldier8_mid_660"]/span[10]',
               '//*[@id="soldier9_mid_633"]/span[10]',
               '//*[@id="soldier10_mid_593"]/span[10]',
               '//*[@id="soldier11_mid_569"]/span[10]',
               '//*[@id="soldier12_mid_548"]/span[10]',
               '//*[@id="soldier13_mid_540"]/span[10]',
               '//*[@id="lebron18_mid_3"]/span[10]'
               ]
#Stock-links
stockLebron = ['https://finance.yahoo.com/quote/NKE/history?period1=1065398400&period2=1070582400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1129593600&period2=1134777600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1161043200&period2=1166227200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1192492800&period2=1197676800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1222819200&period2=1228003200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1253750400&period2=1258934400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1285459200&period2=1290643200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1316908800&period2=1322092800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1349222400&period2=1354406400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1378944000&period2=1384128000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1412035200&period2=1417219200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',#finished this one
               'https://finance.yahoo.com/quote/NKE/history?period1=1441843200&period2=1447027200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1484092800&period2=1489276800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1505606400&period2=1510790400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1534809600&period2=1539993600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1566950400&period2=1572134400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1148256000&period2=1149984000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1183334400&period2=1185062400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1207612800&period2=1209340800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1239062400&period2=1240790400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1277078400&period2=1281484800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1307664000&period2=1309392000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1345593600&period2=1347321600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1372377600&period2=1374019200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1403308800&period2=1405036800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1432080000&period2=1433894400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1465603200&period2=1467331200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1495324800&period2=1497052800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1522627200&period2=1524355200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1561075200&period2=1562803200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true',
               'https://finance.yahoo.com/quote/NKE/history?period1=1599782400&period2=1601510400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
               ]
#Stock Prices Before Release
priceLebronBEFORE = ['//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[31]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[37]/td[4]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[33]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[34]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[30]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[27]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[27]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[28]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[30]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[29]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[15]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[14]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[14]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[13]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[36]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[14]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[14]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[12]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[12]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[15]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[14]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[15]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[15]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[13]/td[5]/span',
                     '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[14]/td[5]/span'
                     ]
#Stock Prices After Release
priceLebronAFTER = ['//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span',
                    '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span'
                    ]

#Get shoe price data
shoePrice = []
for i in range(len(priceLebron)):
    driver.get('https://nikelebron.net/releases/')
    price = driver.find_element_by_xpath(priceLebron[i])
    shoePrice.append(price.text)

#Appending Shoe Prices to list & removing $ signs
bad_chars_price = ['$']
test = str(shoePrice)
newShoePrice = []
test = [x.replace("$", '') for x in shoePrice]

#stock before/after prices
finalPriceChangeLebron = []
finalPriceLebronBefore = []
finalPriceLebronAfter = []
for i in range(len(stockLebron)):
    driver.get(stockLebron[i])
    lebronBefore = driver.find_element_by_xpath(priceLebronBEFORE[i])
    lebronAfter = driver.find_element_by_xpath(priceLebronAFTER[i])
    finalPriceLebronBefore.append(lebronBefore.text)
    finalPriceLebronAfter.append(lebronAfter.text)

#turning prices into a float
finalPriceLebronBefore1 = []
finalPriceLebronAfter1 = []
for item in finalPriceLebronBefore:
    finalPriceLebronBefore1.append(float(item))
for item in finalPriceLebronAfter:
    finalPriceLebronAfter1.append(float(item))


#final price % change
for i in range(len(finalPriceLebronAfter1)):
    x = (((finalPriceLebronAfter1[i] - finalPriceLebronBefore1[i]) / finalPriceLebronBefore1[i]) * 100)
    finalPriceChangeLebron.append(x)
decimalLebron = ['%.2f' % elem for elem in finalPriceChangeLebron]
percentChangeLebron = []
for item in decimalLebron:
    percentChangeLebron.append(item)
finalPercentChangeLebron = [float(i) for i in percentChangeLebron]
finalShoePrice = [float(i) for i in test]

#Print the final $/%
print("\nShoe Prices ($):", finalShoePrice)
print("Stock Price Before ($):", finalPriceLebronBefore1)
print("Stock Price After ($):", finalPriceLebronAfter1)
print("Stock Price Percent Change (%):", finalPercentChangeLebron)



import pandas as pd
import matplotlib.pyplot as plt

#Adding data to dataframe
data = {"Shoe Price": finalShoePrice,
        "Stock Price": finalPercentChangeLebron}
df = pd.DataFrame(data, columns=["Shoe Price", "Stock Price"])


#Scatter plot
plt.scatter(df["Shoe Price"], df["Stock Price"], color = 'green')
plt.title('Lebron Shoe Price vs Percent Change in Nike Stock Price', fontsize = 14)
m, b = np.polyfit(df["Shoe Price"], df["Stock Price"], 1)

#Line of Best Fit
print("\nLine of best fit: y =", m, end="")
print("x", "+", b)

#Mean
mean = df.mean(axis = 0)
print("\nMean:")
print(mean)

#Standard Deviation
Standard_Deviation = df.std(axis = 0)
print("\nStandard Deviation:")
print(Standard_Deviation)

#Correlation
correlation = df["Shoe Price"].corr(df["Stock Price"])
print("\ncorrelation =", correlation)
plt.plot(df["Shoe Price"], m*df["Stock Price"]+b)

#Show the Scatter Plot
plt.xlabel('Price', fontsize = 14)
plt.ylabel('Stock Percent Change', fontsize = 14)
plt.grid(True)
plt.show()
