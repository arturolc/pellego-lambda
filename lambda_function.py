import json
import mysql.connector

def lambda_handler(event, context):
    cnx = mysql.connector.connect(user='admin', password='capstone', host='pellego-db.cdkdcwucys6e.us-west-2.rds.amazonaws.com', database='pellego_database')
    
    return {'statusCode': 200, 'body': json.dumps("Added user to DB") }