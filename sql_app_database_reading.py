import mysql.connector
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from mysql.connector import Error

from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button


### Ideas ###
 # Button groups?
 # array/list of buttons for ids



import time

def create_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("sql3.freemysqlhosting.net", "sql3410985", "UAJI17ZhCS","sql3410985")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


pin13_on = """
UPDATE
    lights
SET
    activated = 1
WHERE
    id = 1
"""

pin13_off = """
UPDATE
    lights
SET
    activated = 0
WHERE
    id = 1
"""



def get_Table():
    light_id_table = execute_query(connection,"SELECT id FROM lights")



class ArdApplication(FloatLayout):

    def __init__(self):
        super(ArdApplication, self).__init__()


        count = 0
        x = [1, 2, 3]
        for num in range(len(x)):
            self.test = Button(text=str(x[num]), pos_hint = {'x':.1,'y':count/10}, size_hint = (.1,.1))
            self.add_widget(self.test)
            count += 1


    def process_switch(instance, id):
        pass

    def turn_on(instance):
        execute_query(connection, pin13_on)

    def turn_off(instance):
        execute_query(connection, pin13_off)

class Arduino2App(App):

    def build(self):

        Ard = ArdApplication()
        return Ard

if __name__ in ('__main__', '__android__'):
    Arduino2App().run()

