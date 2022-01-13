import requests
import bs4
    

class web_doc_downloader():
    """爬取网页文章

    必要信息:
        [str]: [网页地址]
        [str]: [段落列表地址]
        [str]: [原网页的编码格式]]        
    """
    url = 'http://m.creditsailing.com/ZiWoPingJia/818030.html'
    doc_selector = 'body > div.wrap > div.article > div.content > p'
    source_encoding = 'gb2312'

    def __get_res__(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'}
        res = requests.get(self.url,headers=headers)
        res.encoding = self.source_encoding
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        results = soup.select(self.doc_selector)

        return results

    def download_doc(self):
        """返回网页的文章内容

        """
        res = self.__get_res__()
        text_list = [each.text+'\n' for each in res]
        return text_list

def main():
    wdd = web_doc_downloader()
    wdd.url = input('请输入文章的网址：\n')
    wdd.doc_selector = input('请输入网页的selector：\n')
    wdd.source_encoding = input('请输入原网页的编码：\n')
    content = wdd.download_doc()

    with open('result.txt','w',encoding='utf-8') as f:
        f.writelines(content)

if __name__ == '__main__':
    main()