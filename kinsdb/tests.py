def makeWordCloud(contents):
    nlp = Okt()
    wordText=""
    for t in contents:
        wordText += str(t) + " "

    # 명사만 추출
    nouns = nlp.nouns(wordText)
    # 추출
    count = Counter(nouns)
    wordInfo = dict()
    # 가장 빈도수 높은거 100개만 고름
    for tags, counts in count.most_common(100):
        if(len(str(tags)) > 1):
            wordInfo[tags] = counts

    filename = os.path.join(STATIC_DIR, 'images/wordcloud01.png')
    taglist = pytagcloud.make_tags(dict(wordInfo).items())
    pytagcloud.create_tag_image(taglist, filename, size = (800, 600), fontname = 'Korean', rectangular = False)

    webbrowser(img) 
