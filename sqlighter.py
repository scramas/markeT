import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):

        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()

            return bool(len(result))

    def add_subscriber(self, user_id, status = True):

        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES(?,?)", (user_id,status))


    def add_tovar(self,link,img,price,name,magazin):

        with self.connection:
            return self.cursor.execute("INSERT INTO `tovar` (`link`, `img`,`price`, `name`,`magazin`) VALUES(?,?,?,?,?)", (link, img,price,name,magazin,))

    def add_kazan(self, link, img, price, name):
        with self.connection:
            return self.cursor.execute("INSERT INTO `kazan` (`link`, `img`,`price`, `name`) VALUES(?,?,?,?)",
                                       (link, img, price, name,))

    def add_ozon(self, link, img, price, name):
        with self.connection:
            return self.cursor.execute("INSERT INTO `ozon` (`link`, `img`,`price`, `name`) VALUES(?,?,?,?)",
                                       (link, img, price, name,))


    def keys_subscriber(self, key,id_user):

            with self.connection:
                return self.cursor.execute("INSERT INTO keys (key,user_id) VALUES(?,?)", (key,id_user))





    def select_token(self):

        with self.connection:
            return self.cursor.execute("select token from config ").fetchone()




    def select_link_status0_lenta(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_lenta where status=0").fetchall()


    def select_caption_lenta(self):

            with self.connection:
                return self.cursor.execute("select getDescriptions from news_lenta where status=0" ).fetchall()



    def select_link_for_text_lenta(self, text):
            with self.connection:
                return self.cursor.execute("select getLinks from news_lenta where getDescriptions=?", (text,)).fetchall()



    def keys_exists(self, user_id, key):
        """Проверяем, есть ли уже ключ в базе"""
        with self.connection:
            return  self.cursor.execute('SELECT key FROM keys WHERE user_id = ? and key=?', (user_id,key,)).fetchall()

    def user_id(self, user_id):
        """Проверяем, есть ли уже ключ в базе"""
        with self.connection:
            return  self.cursor.execute('SELECT id FROM keys WHERE user_id = ? ', (user_id,)).fetchone()



    def select_user_keys(self,user_id):

        with self.connection:
            return self.cursor.execute("select key from keys where user_id=?",(user_id)).fetchall()

    def select_user(self):

        with self.connection:
            return self.cursor.execute("select * from subscriptions").fetchall()







    def select_link_status0_Kommersant(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_kommersant where status=0").fetchall()



    def select_caption_Kommersant(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_kommersant where status=0").fetchall()



    def select_link_for_text_Kommersant(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_kommersant where getDescriptions=?", (text,)).fetchall()






    def select_link_status0_interfax(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_interfax where status=0").fetchall()



    def select_caption_interfax(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_interfax where status=0").fetchall()



    def select_link_for_text_interfax(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_interfax where getDescriptions=?", (text,)).fetchall()




    def select_link_status0_regnum(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_regnum where status=0").fetchall()



    def select_caption_regnum(self):

        with self.connection:
            return self.cursor.execute("select getHeadlines from news_regnum where status=0").fetchall()



    def select_link_for_text_regnum(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_regnum where getHeadlines=?", (text,)).fetchall()






    def select_link_status0_m24(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_m24 where status=0").fetchall()



    def select_caption_m24(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_m24 where status=0").fetchall()



    def select_link_for_text_m24(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_m24 where getDescriptions=?", (text,)).fetchall()



    def select_link_status0_rt(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_rt where status=0").fetchall()



    def select_caption_rt(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_rt where status=0").fetchall()



    def select_link_for_text_rt(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_rt where getDescriptions=?", (text,)).fetchall()

    def select_link_for_text_rbc(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_rbc where getDescriptions=?", (text,)).fetchall()


    def select_link_status0_pravda(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_pravda where status=0").fetchall()



    def select_caption_pravda(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_pravda where status=0").fetchall()



    def select_link_for_text_pravda(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_pravda where getDescriptions=?", (text,)).fetchall()




    def select_link_status0_N(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_N where status=0").fetchall()

    def select_link_status0_rbc(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_rbc where status=0").fetchall()



    def select_caption_N(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_N where status=0").fetchall()



    def select_link_for_text_N(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_N where getDescriptions=?", (text,)).fetchall()

    def select_link_status0_ria(self):

        with self.connection:
            return self.cursor.execute("select getLinks from news_ria where status=0").fetchall()

    def select_caption_ria(self):

        with self.connection:
            return self.cursor.execute("select getDescriptions from news_ria where status=0").fetchall()

    def select_link_for_text_ria(self, text):
        with self.connection:
            return self.cursor.execute("select getLinks from news_ria where getDescriptions=?", (text,)).fetchall()


    def select_keys(self, id_user):

            with self.connection:
                return self.cursor.execute("select key from keys where user_id=?", (id_user,)).fetchall()

    def select_id(self, id_user):

            with self.connection:
                return self.cursor.execute("select id from subscriptions where user_id=?", (id_user,)).fetchone()
    def update_subscription(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def select_caption_rbc(self):
            with self.connection:
                return self.cursor.execute("select getDescriptions from news_rbc where status=0" ).fetchall()






    def delete_news_rbc(self):
        with self.connection:
            return self.cursor.execute("delete from news_rbc ").fetchall()

    def delete_news_ria(self):
            with self.connection:
                return self.cursor.execute("delete from news_ria ").fetchall()

    def delete_news_regnum(self):
        with self.connection:
            return self.cursor.execute("delete from news_regnum ").fetchall()

    def delete_news_pravda(self):
        with self.connection:
            return self.cursor.execute("delete from news_pravda ").fetchall()

    def delete_news_rt(self):
        with self.connection:
            return self.cursor.execute("delete from news_rt ").fetchall()

    def delete_news_interfax(self):
        with self.connection:
            return self.cursor.execute("delete from news_interfax ").fetchall()

    def delete_news_lenta(self):
        with self.connection:
            return self.cursor.execute("delete from news_lenta ").fetchall()

    def delete_news_m24(self):
        with self.connection:
            return self.cursor.execute("delete from news_m24 ").fetchall()

    def delete_news_kommersant(self):
        with self.connection:
            return self.cursor.execute("delete from news_kommersant ").fetchall()

    def delete_news_N(self):
        with self.connection:
            return self.cursor.execute("delete from news_N ").fetchall()

    def delete_keys(self,user_id,key):
        with self.connection:
            return self.cursor.execute("delete from keys where  user_id = ? and key=?", (user_id,key,)).fetchall()



    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()