# Problem
    I want to check all houses that are for sold in my city.
    I want informations about it, like: price, number of rooms, number of bathroom, number of garage, etc

# How i solved it
 - Where to find these infos?
 I will use www.vivareal.com.br, a big real state site here in Brazil

 1) Inspected how information is structured in Vivareal's site
 2) Using 'requests' module, accessed it 
 3) Using some logic, processed the info and saved it to a datafram
 3) Using some logic, crawled all pages that have the results i want to
 4) saved all the gathered data to a csv file