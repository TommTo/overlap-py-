# Per artikel een variabele
doc1 = "riot police in georgia used pepper spray and water cannon against protesters who turned out on the streets of tbilisi after the government suspended moves to join the european union forty three people were arrested at the demonstrations in the capital on thursday night the government said crowds turned out after prime minister irakli kobakhidze said his government would drop its pursuit of eu membership until the end of 2028 a move criticised by more than 100 diplomats on friday as unconstitutional kobakhidze had accused the bloc of blackmail after eu legislators called for last months parliamentary elections in georgia to be rerun they cited significant irregularities since 2012 georgia has been governed by georgian dream a party which critics say has tried to move the country away from the eu and closer to russia the party claimed victory in last months election but opposition mps are boycotting the new parliament alleging fraud while the countrys president salome zurabishvili has called the oneparty parliament unconstitutional on thursday the european parliament backed a resolution describing the election as the latest stage in georgias worsening democratic crisis and saying that the ruling party was fully responsible it expressed particular concern about reports of voter intimidation vote buying and manipulation and harassment of observers the european parliament also urged sanctions against georgias prime minister and other highlevel officials including the billionaire founder of the governing party bidzina ivanishvili following the resolution georgias prime minister said his government had decided not to bring up"
doc2 = "amid the monstrous heaps of twisted metal pools of congealed oil and walls pockmarked by shrapnel one incongruous detail catches my eye patches of snow inside a thermal power station with another ukrainian winter arriving the vast turbine hall is full of activity engineers dwarfed by the enormous scale of the place repairing what they can removing what they cant after a recent russian air strike hit this facility for security reasons were not allowed to say where we are or when the visit occurred nor can we describe the extent of the damage or whether the plant is still working russia were told collects every scrap of information in order to draw up its next target list on thursday moscow mounted its second mass attack on ukraines energy infrastructure in less than two weeks ten such attacks this year have placed an enormous burden on the entire energy system before the first of this months attacks on 17 november ukraine had already lost 9gw of generation capacity thats about half of the power consumed during last winters peak heating season weve been asked not to say if the plant we visited was among the latest targets on thursday but like others across the country this decadesold facility has suffered multiple drone and missile strikes since vladimir putin launched his fullscale invasion in february 2022 theres evidence of russias destructive intent everywhere in one corner of the turbine hall under a gaping hole in the roof workers warm their hands"
doc3 = "for the first time in almost a decade mps will vote on friday on giving terminally ill adults in england and wales the right to have an assisted death while its something that remains illegal in most countries more than 300 million people now live in countries which have legalised assisted dying canada australia new zealand spain and austria have all introduced assisted dying laws since 2015 when uk mps last voted on the issue some allowing assisted death for those who are not terminally ill the proposed bill in england and wales comes with safeguards supporters say will make it the strictest set of rules in the world with patients needing the approval of a high court judge critics on the other hand say changing the law would be a dangerous step that would place the vulnerable at risk they argue the focus should be on improving patchy access to palliative care ahead of fridays vote we look at assisted dying laws in north america europe and australasia across the us assisted dying which some critics prefer to call assisted suicide is legal in 10 states as well as in washington dc oregon was one of the first places in the world to offer help to die for some patients in 1997 and so has more than 25 years experience it has become the model on which other us assisted dying laws have been framed in oregon assisted dying is open to terminally ill mentally competent adults expected to"
doc4 = "how a rarelyseen drawing of the three graces by raphael reveals the eras ideas about nudity modesty shame and the artists genius its part of an exhibition drawing the italian renaissance at the kings gallery buckingham palace of drawings from 1450 to 1600 the biggest of its kind ever shown in the uk a wandering lobster and a sturdy ostrich feature among the 150 chalk metalpoint and ink drawings on show at drawing the italian renaissance at the kings gallery buckingham palace created by renaissance giants such as leonardo da vinci michelangelo raphael and titian often in preparation for larger painted tableaux the works are thought to have entered the royal collection in the 17th century under charles ii several as gifts for more than 30 of them its their first time ever on public display rarely shown due to their fragility these fascinating drawings which at the time were beginning to be recognised as artworks in their own right make up the broadest exhibition of italian drawings from 1450 to 1600 ever shown in the uk rarer still than these animal studies are the drawings of female nudes outnumbered by a factor of three by an abundance of naked men the male body is this absolute focus of creativity explained renaissance historian maya corry discussing the exhibition on bbc radio 4s front row in october this is a christian society and its the male body not the female body thats made in gods image leonardo da vincis vitruvian man"
doc5 = "nell diamond ceo of hill house shares how her small business skyrocketed to global success with a simple singular product at the height of the covid19 pandemic hill house homes nap dress became more than just a piece of clothing it was a symbol of comfort and versatility for a world in flux what started as a directtoconsumer bedding and home business in 2016 had grown into a fashion movement reflecting how a single dress could adapt to your body over the years and transform depending on the demands of the day the company introduced the nap dress in 2019 a design that leaned into the idea of smocked fabric from the 1950s and reimagined it with modern universal appeal it didnt take long for the dress now with over 50 designs to go viral on social media and become common in many closets around the world our crazy growth happened from 2019 to 2020 right in the middle of quarantine and while i was pregnant with twins ceo nell diamond tells the bbc i could obviously see how much the business was changing internally from the sales volume but one really pivotal moment for me was working from home sitting in my bedroom in new york city and looking out the window to see someone walking down the street wearing one of our dresses entrepreneurship can feel really lonely and insular so to realise that people know about your little project is incredibly rewarding ill never forget that moment"

#alle woorden worden in een list gezet.
doc1words = doc1.split()
doc2words = doc2.split()
doc3words = doc3.split()
doc4words = doc4.split()
doc5words = doc5.split()

#Woorden teller voor overeenkomende woorden bij elke loop.
word_counter = 0
word_counter1 = 0
word_counter2 = 0
word_counter3 = 0


print("First we start by comparing each article to the first article:\n")

#artikel 2 vergelijken met artikel 1
for word in doc2words:
    if word in doc1words:
        word_counter +=1


print("Article 2 has", word_counter, "similar words compared to article 1.")


#artikel 3 vergelijken met artikel 1
for word in doc3words:
    if word in doc1words:
        word_counter1 +=1

print("Article 3 has", word_counter1, "similar words compared to article 1")

#artikel 4 vergelijken met artikel 1
for word in doc4words:
    if word in doc1words:
        word_counter2 +=1

print("Article 4 has", word_counter2, "similar words comprated to article 1")

#artikel 5 vergelijken met artikel 1
for word in doc5words:
    if word in doc1words:
        word_counter3 +=1

print("Article 5 has", word_counter3, "similar words compared to aticle 1")

print("Article 3 is the most similar to the first article \n")




print("Now we have removed all the stop words from the first article. \nIn this case we get the following results:\n")

#stap 6
doc1stop = "riot police georgia used pepper spray water cannon protesters turned out streets tbilisi government suspended moves join european union forty three people were arrested demonstrations capital thursday night government crowds turned out prime minister irakli kobakhidze government drop pursuit eu membership end 2028 move criticised 100 diplomats friday unconstitutional kobakhidze accused bloc blackmail eu legislators called last months parliamentary elections georgia rerun cited significant irregularities since 2012 georgia been governed georgian dream party critics say tried move country away eu closer russia party claimed victory last months election but opposition teams boycotting new parliament alleging fraud while countrys president salome zurabishvili called one party parliament unconstitutional thursday european parliament backed resolution describing elections latest stage georgias worsening democratic crisis saying ruling party fully responsible expressed particular concern about reports voter intimidation vote buying manipulation harassment observers european parliament also urged sanctions georgias prime minister other highlevel officials including billionaire founder governing party bidzina ivanishvili following resolution georgias prime minister government decided bring up"
doc1stopwords = doc1stop.split()

stopword_counter = 0
stopword_counter1 = 0
stopword_counter2 = 0
stopword_counter3 = 0

#artikel 2 vergelijken met artikel 1
for word in doc2words:
    if word in doc1stopwords:
        stopword_counter +=1


print("Article 2 has", stopword_counter, "similar words compared to article 1.")


#artikel 3 vergelijken met artikel 1
for word in doc3words:
    if word in doc1stopwords:
        stopword_counter1 +=1

print("Article 3 has", stopword_counter1, "similar words compared to article 1")

#artikel 4 vergelijken met artikel 1
for word in doc4words:
    if word in doc1stopwords:
        stopword_counter2 +=1

print("Article 4 has", stopword_counter2, "similar words comprated to article 1")

#artikel 5 vergelijken met artikel 1
for word in doc5words:
    if word in doc1stopwords:
        stopword_counter3 +=1

print("Article 5 has", stopword_counter3, "similar words compared to aticle 1")

print("Article 2 is the most similar to the first article. \n")


# step 8 
print("Now we are going to repeat the results and divide them by the number of characters of the document we are comparing to. (also known as: relative overlap): \n")
#Woorden teller voor overeenkomende woorden bij elke loop.
word_counter = 0
word_counter1 = 0
word_counter2 = 0
word_counter3 = 0



#artikel 2 vergelijken met artikel 1
for word in doc2words:
    if word in doc1words:
        word_counter +=1


#len() functie pakt de lengde van de string variabele. 
print("Article 2 has a relative overlap of", word_counter/len(doc2), "compared to article 1.")


#artikel 3 vergelijken met artikel 1
for word in doc3words:
    if word in doc1words:
        word_counter1 +=1

print("Article 3 has a relative overlap of", word_counter1/len(doc3), "compared to article 1")

#artikel 4 vergelijken met artikel 1
for word in doc4words:
    if word in doc1words:
        word_counter2 +=1

print("Article 4 has a relative overlap of", word_counter2/len(doc4), "comprated to article 1")

#artikel 5 vergelijken met artikel 1
for word in doc5words:
    if word in doc1words:
        word_counter3 +=1

print("Article 5 has a relative overlap of", word_counter3/len(doc5), "compared to aticle 1")

print("Article 3 is the most similar to the first article \n")




print("Now we have removed all the stop words from the first article. \nIn this case we get the following results:\n")

#stap 6
doc1stop = "riot police georgia used pepper spray water cannon protesters turned out streets tbilisi government suspended moves join european union forty three people were arrested demonstrations capital thursday night government crowds turned out prime minister irakli kobakhidze government drop pursuit eu membership end 2028 move criticised 100 diplomats friday unconstitutional kobakhidze accused bloc blackmail eu legislators called last months parliamentary elections georgia rerun cited significant irregularities since 2012 georgia been governed georgian dream party critics say tried move country away eu closer russia party claimed victory last months election but opposition teams boycotting new parliament alleging fraud while countrys president salome zurabishvili called one party parliament unconstitutional thursday european parliament backed resolution describing elections latest stage georgias worsening democratic crisis saying ruling party fully responsible expressed particular concern about reports voter intimidation vote buying manipulation harassment observers european parliament also urged sanctions georgias prime minister other highlevel officials including billionaire founder governing party bidzina ivanishvili following resolution georgias prime minister government decided bring up"
doc1stopwords = doc1stop.split()

stopword_counter = 0
stopword_counter1 = 0
stopword_counter2 = 0
stopword_counter3 = 0

#artikel 2 vergelijken met artikel 1
for word in doc2words:
    if word in doc1stopwords:
        stopword_counter +=1


print("Article 2 has a relative overlap of", stopword_counter/len(doc2), "compared to article 1.")


#artikel 3 vergelijken met artikel 1
for word in doc3words:
    if word in doc1stopwords:
        stopword_counter1 +=1

print("Article 3 has a relative overlap of", stopword_counter1/len(doc3), "compared to article 1")

#artikel 4 vergelijken met artikel 1
for word in doc4words:
    if word in doc1stopwords:
        stopword_counter2 +=1

print("Article 4 has a relative overlap of", stopword_counter2/len(doc4), "comprated to article 1")

#artikel 5 vergelijken met artikel 1
for word in doc5words:
    if word in doc1stopwords:
        stopword_counter3 +=1

print("Article 5 has a relative overlap of", stopword_counter3/len(doc5), "compared to aticle 1")

print("Article 2 is the most similar to the first article. \n")
