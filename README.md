# Pulitzer Prize and Gender

My investigation for the winners of the Pulitzer Prize in its 100-ish-year history. 

"How many female Pulitzer winners are there across its 100-ish-year prize history?"

This June originally I expected I could get the answer via a simple Google search. However, it turned out to be a project involving web scraping, endless data cleaning, analysis and (possibly building a database from scratch), which came along with so much fun and frustration.

The csv here are only some that I generated in the process, because the data cleaning process is iterative. When I found something wrong during my data manipulation phase, I switched back to clean the dataset again (and again). There might be 20 or 30 messy csv lying in my local directory.

The file "stack.py" is generously contributed by Jonathan Soma after he heard me whine desperately for multiple organizations squeezed in same columns. Thanks him so much.

If you are interested in knowing how this came together and the result, you might want to take a look at <a href="https://github.com/spepechen/pulitzer/wiki">my wiki for this project</a>. :)


A Quick Note on What I’ve Learned 
-----

The gender disparity in the profession of news has its root in history, but there seems to be no formal calculation for the gender ratio before 2000. The alternative way digging into this problem is to take a look at the Pulitzer Prize winner list across 100 years, if we arguably take it as it is the awards for the best out of the whole contemporary journalistic works. (Although I know it is not the case, it does not include all genres of news like audio and visual.) In addition, it can answer the other question I care: whether women thrive in this field. (Yes, we all know not all good and powerful journalists get a Pulitzer Prize, but those who get one certainly does a not bad job.) 

Here are three quick facts I learn from my dataset: 

####1. Less than one-fifth unique winners are female. In recent six years, that is since 2010, women still just make up one-third of the winners.

<img align="middle" src="https://github.com/spepechen/pulitzer/blob/master/piechart.png" height="500" width="500" >

####2. The female unique winners to all ratio is getting higher especially after 1970s. The female winners in 1980s is three times higher than 1970s.(Perhaps it has something to do with women right moment.) 
<img align="middle" src="https://github.com/spepechen/pulitzer/blob/master/linechart.png">


####3. <a href ="https://en.wikipedia.org/wiki/Carol_Guzy">Carol Guzy</a>, a female photojournalist, is the only journalist who won pulitzer four times.   

