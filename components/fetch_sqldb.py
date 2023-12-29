def meili_client():
    '''Charger les variable d'environement à partir du fichier .env situé dans le répertoire components, retourne meili_env = URL, 
    meili_key = admin_key de meilisearch, et configure le client meilisearch'''
    from dotenv import load_dotenv
    import os
    import meilisearch
    from sqlalchemy import create_engine, MetaData
    load_dotenv(dotenv_path='components/.env')
    meili_env = os.getenv("meili_client")
    meili_key = os.getenv("meili_key")
    if meili_key == False :
        client = meilisearch.Client(meili_env)
    else :
        client = meilisearch.Client(meili_env, meili_key)
    ''' Configurer l'accés à la data base mysql'''
    db_url = os.getenv("sqldb")
    engine = create_engine(db_url)
    metadata = MetaData()
    return engine, metadata, client


def meilei_add(table, list_col, metadata, engine, client):
    '''table is a string with the name of the table to add, list_col is a list of string representing selected columns to index'''
    import meilisearch
    from sqlalchemy import create_engine, MetaData, Table
    table_obj = Table(table, metadata, autoload_with=engine)
    with engine.connect() as connection :
        result_set = connection.execute(table_obj.select()).fetchall()
        #Fetching all the table is convenient in developpement but inefficient, should be fixed later
    documents = []
    for row in result_set:
        document = {column.name: getattr(row, column.name) for column in table_obj.columns if column.name in list_col}
        documents.append(document)
    #workaround for the food table
    if table == 'food':
        client.index(table).update(primary_key='code')
    client.index(table).add_documents(documents) 

def meili_feed() :
    from components.fetch_sqldb import meilei_add
    #list of retrieved columns
    list_recipes = ['id', 'name', 'budget', 'difficulty', 'food']
    list_articles = ['id', 'title', 'content' ]
    list_food = [ 'code', 'name']
    list_questions = [ 'id', 'question', 'answer', 'url_article']
    #adding table to meili
    meilei_add('recipes', list_recipes)
    meilei_add('articles', list_articles)
    meilei_add('food', list_food)
    meilei_add('questions', list_questions)