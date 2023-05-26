with open('artists.txt', encoding='UTF-8', mode='r') as file:
    artists = file.read()
    # print(artists)
# with open("article.txt", mode='a+', encoding='UTF-8') as file:
#     file.write(artists)
# result = open("article.txt", encoding='UTF-8')
# print(result.read)
with open('article-part.txt', encoding='Utf-8') as file:
    article_part = file.read()
    # print(article_part) 
with open("article.txt", mode='r', encoding='UTF-8') as file:
    file.seek(0)
    content = file.read()
    # print(content)
    content = content.splitlines()
    content[3] = article_part
    content = '\n'.join(content)
    print(content)
with open("article.txt", mode='w', encoding='UTF-8') as file:
    file.write(content)



# keywords = "#İntibahDövrü #AvropaMədəniyyəti #RenesansArtistləri #Mikelancelo #Botiçelli"

# article_part += "\n\nAçar sözlər: " + keywords

# with open("article.txt", "w", encoding="utf-8") as file:
#     file.write(article_part)
    
# article_part += "\n\nAçar sözlər: " + keywords