import requests as req
import pandas as pd

def get_page(url):
  r1=req.get(url)
  print(r1.status_code)
  df=pd.read_html(r1.content)
  return df[0]

max_num=int(input("Enter Max Page Number :"))
df=pd.DataFrame()
for i in range(1,max_num):
  d1=get_page('https://geckoterminal.com/bsc/tokens?page='+str(i)+'&__cf_chl_captcha_tk__=pmd_jYGzb58LnDrH2EprXHvhQYwcgWgFDYChQMvErV81mN0-1632811904-0-gqNtZGzNAtCjcnBszQgR')
  df=pd.concat([df,d1])
  print(d1)

print(df)
df.to_csv('all_data.csv',index=False)

