import multiprocessing
from flask import Flask, render_template,request,redirect,Response
from flask_sqlalchemy import SQLAlchemy
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from sqlighter import SQLighter
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from  main import site


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Tovar(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    link=   db.Column(db.String(300), nullable=False)
    img = db.Column(db.String(300), nullable=False)
    name =  db.Column(db.String(300), nullable=False)
    price = db.Column(db.String(300), nullable=False)
    magazin = db.Column(db.String(300), nullable=False)
    def __repr__(self):
        return '<Tovar%r>'% self.id


class site:

    def __init__(self):
        self.session=requests.Session()
        self.session.headers={
            "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        }

    def load_page(self,search):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # user-agent
        options.add_argument(
            "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
        options.headless = False
        driver = webdriver.Chrome(
            executable_path=r"G:\РВ\Individualnoe\chromedriver.exe",
            options=options)

        driver.get(f'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search={search}')
        time.sleep(5)
        src = driver.page_source
        return src
    def parse_page(self,text):
        soup = BeautifulSoup(text, "lxml")
        conteiner = soup.select('div.product-card__wrapper')
        for block in conteiner:
            self.parse_blok(block=block)

    def parse_blok(self,block):

        url_block=block.select_one('a.product-card__main.j-card-link')
        url=url_block.get('href')
        url_img=block.select_one('img.j-thumbnail.thumbnail')
        img='https:'+url_img.get('src')
        url_price=block.select_one('.lower-price')
        price=url_price.text
        url_name=block.select_one('div.product-card__brand-name')
        name=url_name.text
        magazin='wildberries.ru'
        w=Tovar(link=url,img=img,price=price,name=name,magazin=magazin)


        db.session.add(w)
        db.session.commit()
        return redirect('/')






    def run(self,search):
        db.session.query(Tovar).delete()
        db.session.commit()
        text=self.load_page(search=search)
        self.parse_page(text=text)

    def load_page_kazan(self,search):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # user-agent
        options.add_argument(
            "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
        options.headless = False
        driver = webdriver.Chrome(
            executable_path=r"G:\РВ\Individualnoe\chromedriver.exe",
            options=options)

        driver.get(f'https://kazanexpress.ru/search?query={search}')
        time.sleep(5)
        src = driver.page_source
        return src
    def parse_page_kazan(self,text):
        soup = BeautifulSoup(text, "lxml")
        conteiner = soup.select('div.col-mbs-12.col-mbm-6.col-xs-4.col-md-3')
        for block in conteiner:
            self.parse_blok_kazan(block=block)

    def parse_blok_kazan(self,block):

        url_block = block.select_one('a.tap-noselect.noselect')
        url = 'https://kazanexpress.ru/'+url_block.get('href')
        url_img = block.select_one('img.main-card-icon-and-classname-collision-made-to-minimum')
        img = url_img.get('src')
        url_price = block.select_one('span.currency.product-card-price.slightly.medium')
        price = url_price.text
        url_name = block.select_one('div.subtitle.slightly.regular')
        name = url_name.text
        magazin = 'kazanexpress.ru'
        w = Tovar(link=url, img=img, price=price, name=name, magazin=magazin)
        db.session.add(w)
        db.session.commit()
        return redirect('/')

    def run_kazan(self,search):

        text=self.load_page_kazan(search=search)
        self.parse_page_kazan(text=text)

    def load_page_ozon(self,search):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # user-agent
        options.add_argument(
            "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
        options.headless = False
        driver = webdriver.Chrome(
            executable_path=r"G:\РВ\Individualnoe\chromedriver.exe",
            options=options)

        driver.get(f'https://sbermegamarket.ru/catalog/?q={search}')


        time.sleep(5)
        src = driver.page_source
        return src

    def parse_page_ozon(self, text):
        soup = BeautifulSoup(text, "lxml")
        conteiner = soup.select('.catalog-item.ddl_product')
        for block in conteiner:
            self.parse_blok_ozon(block=block)

    def parse_blok_ozon(self, block):


        url_block = block.select_one('a.item-image-block.ddl_product_link')
        url = 'https://sbermegamarket.ru' + url_block.get('href')
        url_img = block.select_one('.lazy-img')
        img = url_img.get('src')
        url_price = block.select_one('.item-price')
        price = url_price.text
        url_name =  block.select_one('div.item-title')
        name = url_name.text
        magazin = 'sbermegamarket.ru'
        w = Tovar(link=url, img=img, price=price, name=name, magazin=magazin)

        db.session.add(w)
        db.session.commit()
        return redirect('/')

    def run_ozon(self,search):

        text = self.load_page_ozon(search=search)
        self.parse_page_ozon(text=text)


@app.route('/',methods=['POST','GET'])
def index():



    if request.method=='POST':

        if request.form['submit'] == 'Поиск':
            search = request.form['ky']

            try:
                pars = site()
                pars.run(search)
                pars.run_kazan(search)
                pars.run_ozon(search)
            except:
                return "При дабовлении аккаунта возникли ошибки!!"

            try:
                tovar = Tovar.query.all()
                return render_template('index.html', tovar=tovar)
            except:
                return "При дабовлении аккаунта возникли ошибки!!"
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)