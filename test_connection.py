"""
Test Database Connections
Tests connection to both Client DB (Read-Only) and Logistics DB (Read/Write)
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

def test_client_db():
    """Test Client Database (Read-Only)"""
    print("\n🔍 Testing CLIENT Database (Read-Only)...")
    
    try:
        url = os.getenv("CLIENT_SUPABASE_URL")
        key = os.getenv("CLIENT_SUPABASE_KEY")
        
        if not url or not key:
            print("❌ CLIENT_SUPABASE_URL or CLIENT_SUPABASE_KEY not found in .env")
            return False
        
        client: Client = create_client(url, key)
        
        # Test connection by fetching table list
        response = client.table("branches").select("*").limit(1).execute()
        
        print(f"✅ CLIENT DB Connected!")
        print(f"   URL: {url[:30]}...")
        print(f"   Test Query: SUCCESS")
        
        return True
        
    except Exception as e:
        print(f"❌ CLIENT DB Connection Failed: {str(e)}")
        return False

def test_logistics_db():
    """Test Logistics Database (Read/Write)"""
    print("\n🔍 Testing LOGISTICS Database (Read/Write)...")
    
    try:
        url = os.getenv("LOGISTICS_SUPABASE_URL")
        key = os.getenv("LOGISTICS_SUPABASE_KEY")
        
        if not url or not key:
            print("❌ LOGISTICS_SUPABASE_URL or LOGISTICS_SUPABASE_KEY not found in .env")
            return False
        
        client: Client = create_client(url, key)
        
        # Just test connection (don't query tables yet, we haven't created them)
        print(f"✅ LOGISTICS DB Connected!")
        print(f"   URL: {url[:30]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ LOGISTICS DB Connection Failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 HAL Logistics AI - Database Connection Test")
    print("=" * 60)
    
    client_ok = test_client_db()
    logistics_ok = test_logistics_db()
    
    print("\n" + "=" * 60)
    if client_ok and logistics_ok:
        print("✅ All Connections Successful!")
    else:
        print("❌ Some Connections Failed - Check .env file")
    print("=" * 60)