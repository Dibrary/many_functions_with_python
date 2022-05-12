
from gensim.summarization.summarizer import summarize

my_section = 'eco'
news_list3 = news_dic[my_section] # news_dic 데이터는 gensim_crawling 파일에서 반환되어야 함.
for news_info in news_list3:
    try:
        snews_contents = summarize(news_info['news_contents'], word_count = 20)
    except:
        snews_contents = None

        if not snews_contents:
            news_sentences = news_info['news_contents'].split('.')

            if len(news_sentences) >3:
                snews_contents = '.'.join(news_sentences[:3])
            else:
                snews_contents = '.'.join(news_sentences)
        news_info['snews_contents'] = snews_contents

print('==== 첫 번째 뉴스 원문 ====')
print(news_list3[0]['news_contents'])
print("\n==== 첫 번째 뉴스 요약문 ====")
print(news_list3[0]['snews_contents'])

print('==== 두 번째 뉴스 원문 ====')
print(news_list3[1]['news_contents'])
print("\n==== 두 번째 뉴스 요약문 ====")
print(news_list3[1]['snews_contents'])



