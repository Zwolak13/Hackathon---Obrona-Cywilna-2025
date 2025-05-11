from supabase_config import get_supabase_client

def test_connection():
    try:
        # Get the Supabase client
        supabase = get_supabase_client()
        
        # Try a simple query to test the connection
        response = supabase.table('_test_connection').select("*").limit(1).execute()
        print("Successfully connected to Supabase!")
        return True
    except Exception as e:
        print(f"Error connecting to Supabase: {str(e)}")
        return False

if __name__ == "__main__":
    test_connection() 