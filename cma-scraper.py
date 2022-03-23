import pandas as pd
import requests
from bs4 import BeautifulSoup as bs4

def scrape_cma():
    text = input("Enter your search term or terms:")
    url = "https://www.clevelandart.org/art/collection/search?search=" + str(text)
    response = requests.get(url)
    html_string = response.text
    document = bs4(html_string, "html.parser")
    
    search_results = document.find_all("div", attrs={"class": "search-result grid-item"})
    search_results_artists = document.find_all("div", attrs={"class": "artists"})
    search_results_titles = document.find_all("div", attrs={"class": "artwork-title"})
    search_results_accession = document.find_all("span", attrs={"class": "accession-number"})
    
    artist_list =[]
    for artist in search_results_artists:
        artists_contents = artist.text
        artist_list.append(artists_contents)
    
    title_list = []
    for title in search_results_titles:
        titles_contents = title.text
        title_list.append(titles_contents)
    
    accession_number = []
    for accession in search_results_accession:
        accession_content = accession.text
        accession_number.append(accession_content)
    
    item_url = []
    for item in accession_number:
        item_url.append("https://www.clevelandart.org/art/" + str(item))
    
    df = pd.DataFrame(list(zip(artist_list,title_list,accession_number,item_url)), columns =["Artist","Title","Accession","URL"])
    df.to_csv("cma_"+str(text)+".csv")
    
    print(df)

scrape_cma()
