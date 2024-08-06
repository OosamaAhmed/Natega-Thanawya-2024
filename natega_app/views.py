 
from django.shortcuts import render
import json

# تحميل بيانات JSON
def load_data():
    with open('data.json') as f:
        return json.load(f)

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('query', '')
    data = load_data()
    results = [record for record in data if query.lower() in str(record).lower()]
    return render(request, 'results.html', {'results': results, 'query': query})