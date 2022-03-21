# cma-scraper

Creating a function to search the Cleveland Museum of Art collections (https://www.clevelandart.org/art/collection/search) and return a data frame with the author, title, accession number, and url of the object page. Additionally, the scraper saves the data frame as a csv file based on the search term(s) entered.

Examples:
scrape_cma("cezanne")
0	Paul Cézanne (French, 1839-1906)	The Brook, c. 1895-1900	1958.20	https://www.clevelandart.org/art/1958.20
1	Paul Cézanne (French, 1839-1906)	Mount Sainte-Victoire, c. 1904	1958.21	https://www.clevelandart.org/art/1958.21
2	Paul Cézanne (French, 1839-1906)	The Pigeon Tower at Bellevue, 1890	1936.19	https://www.clevelandart.org/art/1936.19
...
cma_cezanne.csv

scrape_cma("french tapestry")
...
30	Flanders, late 16th century	Gideon Selecting his Army, late 1500s	1949.230	https://www.clevelandart.org/art/1949.230
31	Gobelins Manufactory (France, Paris, est. 1662...	Fire Screen Panel and Frame, c. 1775	1942.821	https://www.clevelandart.org/art/1942.821
32	Jacques Neilson and 3 others	Fire Screen Panel, c. 1775	1942.821.a	https://www.clevelandart.org/art/1942.821.a
33	Josef Frank (Swedish, born Austria, 1885-1967)...	Flora [II], c. 1925-30	1937.185	https://www.clevelandart.org/art/1937.185
...
cma_french tapestry.csv
