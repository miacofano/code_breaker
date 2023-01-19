from app.config.mysqlconnection import connectToMySQL
from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#shorthand for database
db = 'codebreaker_database'

#defines the data required for User class
class User:
    def __init__ (self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #static method for validating the user at registration.
    #It starts by searching the database for duplicate emails as well as correct format for emails
    #it then validates the length of first and last name and password
    #it finally validates that the password and confirmation password match
    #if it does not pass is_valid is marked false and an error message is returned
    @staticmethod
    def validate_user_registration(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query,user)
        if len(results) >= 1:
            flash("Email is already taken, please login.","register")
            is_valid = False
        if len(user['user_name']) < 2 and len(user['user_name']) > 12:
            flash("User name must be at least 2 characters and at most 12 characters.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.","register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.","register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password confirmation must match password.","register")
            is_valid = False
        return is_valid

    #saves new user to table
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (user_name, email, password, created_at, updated_at) VALUES (%(user_name)s, %(email)s, %(password)s, NOW(), NOW());"
        result = connectToMySQL(db).query_db(query, data)
        return result

    #gets all information from the users table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    #gets one users information via their id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)
        return cls(result[0])

    #gets one users information via their email
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])