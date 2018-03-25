import time
from splinter import Browser
from bs4 import BeautifulSoup
from sys import platform
import pandas as pd


def init_browser():
    if platform == "darwin":
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    else:
        executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    #NASA Mars News
    mars_news = "https://mars.nasa.gov/news/"
    browser.visit(mars_news)
    time.sleep(1)
    html = browser.html
    mars_soup = BeautifulSoup(html, "html.parser")
    title = mars_soup.find(class_="content_title")
    title_text = title.find_all("a")
    news_title=title_text[0].text
    body = mars_soup.find(class_="article_teaser_body")
    news_p = body.text
    mars_data["news_title"]=news_title
    mars_data["news_text"]=news_p

    #JPL Mars Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    browser.click_link_by_partial_text('more info')
    time.sleep(1)
    img_soup = BeautifulSoup(browser.html, "html.parser")
    image = img_soup.find(class_='content_page module')
    images = image.find_all('a')
    featured_image_url=images[1]['href']
    mars_data["featured_image"]="https://www.jpl.nasa.gov"+featured_image_url

    #Mars Weather
    mars_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather)
    html = browser.html
    weather_soup = BeautifulSoup(html, "html.parser")
    tweet = weather_soup.find_all(class_="js-tweet-text-container")
    tweet_text = tweet[0].find("p")
    mars_weather=tweet_text.text
    mars_data["mars_weather"]=mars_weather

    #Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_facts_df=tables[0]
    mars_facts_df.columns=["Fact","Data"]
    mars_facts_df.set_index('Fact', inplace=True)
    html_mars_facts = mars_facts_df.to_html()
    html_mars_facts.replace('\n', '')
    mars_data["mars_facts"]=html_mars_facts

    #Mars Hemispheres
    hemisphere_list = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']
    hemisphere_img_urls = []
    temp_dict = {}
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    for hemisphere in hemisphere_list:
        browser.visit(url)
        html = browser.html
        browser.click_link_by_partial_text(hemisphere)
        time.sleep(3)
        browser.click_link_by_partial_text('Open')
        time.sleep(3)
        img_soup = BeautifulSoup(browser.html, "html.parser")
        image = img_soup.find(class_="wrapper")
        image_list = image.find(class_="wide-image")
        hemisphere_url = 'https://astrogeology.usgs.gov'+image_list["src"]
        temp_dict ={'title':hemisphere+' Hemisphere','img_url':hemisphere_url}
        hemisphere_img_urls.append(temp_dict)
    mars_data["hemisphere_images"]=hemisphere_img_urls

    browser.quit()
    return mars_data

