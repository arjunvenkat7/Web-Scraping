# Web-Scraping
Repository for web scraping based projects
So the main idea here is to scrape headlines from news websites wire.in and firstpost.com
Wire doesnt have any restictions on scraping data, since the robots.txt was missing. Firstpost has certain restrictions,
but we will not be accessing those areas.
So I scrape all the headlines adn store it onto a notepad. One reason for doing this is to avoid advertisements and annoying pop ups.
Further updates for this project would be adding news from newsminute.com and quint.in, Once I am done with scraping and handling data
I will be perfroming NLP to analyse the sentiments of news published. Analysis will be extended to website by website.
Visually I can also compare about priorities given to news articles by each website.
Look onto file News_articles.py and News_data for the output obtained.

Update 1:
Added new Web scraping project which I am doing currently
I Am analysing toppings data from a local pizza store's website situated in Tampere Finland. Though I am using slenium actions to change
language, the ouput is still in Finnish. I am looking onto the issue to sort it out.
After fetching the menu, I am performing certain manipulations to take out only the toppings.
Based on my preliminary analysis, the top three most commonly used toppings are

Kinkku - Ham - It is used in 15 different Pizzas
Aurajuusto - Blue Cheese - It is used in 12 different Pizzas
Katkarapu - Shrimp - It is used in 11 differnt Pizzas

Least commonly used toppings:
Chilli Pepper, Banana are used only in one pizza
Note there are additional data to the above list which I will update in next version of the code
For further information lookonto the file pizza.py
