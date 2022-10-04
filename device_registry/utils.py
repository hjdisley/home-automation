import os
from supabase import create_client, Client

def db_connect():
    client = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

    return client

