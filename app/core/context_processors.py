from django.conf import settings

def supabase(request):
    """Add Supabase configuration to template context."""
    return {
        'SUPABASE_URL': settings.SUPABASE_URL,
        'SUPABASE_KEY': settings.SUPABASE_KEY,
    } 