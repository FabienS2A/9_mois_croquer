
from components.fetch_sqldb import meili_client, meilei_add
from components.frontend import run_meilisearch_frontend
import meilisearch
from sqlalchemy import create_engine, MetaData, Table
from flask import Flask, jsonify, request

engine, metadata, client = meili_client()

#list of retrieved columns
list_recipes = ['id', 'name', 'budget', 'difficulty', 'food']
list_articles = ['id', 'title', 'content' ]
list_food = [ 'code', 'name']
list_questions = [ 'id', 'question', 'answer', 'url_article']
#adding table to meili
meilei_add('recipes', list_recipes,metadata, engine, client)
meilei_add('articles', list_articles,metadata, engine, client)
meilei_add('food', list_food,metadata, engine, client)
meilei_add('questions', list_questions,metadata, engine, client)

run_meilisearch_frontend()
