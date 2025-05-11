import os
from supabase import create_client, Client

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv('SUPABASE_URL', 'https://ycgxdbgsrwscskgornbgw.supabase.co'),
    os.getenv('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InljZ3hkYmdzcndzY2tnb3JuYmd3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY5NTA1MzAsImV4cCI6MjA2MjUyNjUzMH0.XKvNVn85nWLbm9HM2CiulOCG2Vo0WmSBZ0ibYo_xezI')
)

def get_supabase_client() -> Client:
    """
    Returns the Supabase client instance.
    Make sure to set SUPABASE_URL and SUPABASE_KEY in your environment variables.
    """
    return supabase 