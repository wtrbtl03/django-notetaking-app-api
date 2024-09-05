import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Note
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create Note
@method_decorator(csrf_exempt, name='dispatch')
class CreateNoteView(View):
    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title')
        body = data.get('body')
        note = Note.objects.create(title=title, body=body)
        return JsonResponse({'id': note.id, 'title': note.title, 'body': note.body, 'created_at': note.created_at, 'updated_at': note.updated_at}, status=201)

# Fetch all notes
class FetchAllNotesView(View):
    def get(self, request):
        notes = Note.objects.all()
        notes_list = [{'id': note.id, 'title': note.title, 'body': note.body, 'created_at': note.created_at, 'updated_at': note.updated_at} for note in notes]
        return JsonResponse(notes_list, safe=False)
    
# Fetch Note by ID
class FetchNoteView(View):
    def get(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)
        return JsonResponse({'id': note.id, 'title': note.title, 'body': note.body, 'created_at': note.created_at, 'updated_at': note.updated_at})

# Query Notes by Title Substring
class QueryNotesView(View):
    def get(self, request):
        title_query = request.GET.get('title', '')
        notes = Note.objects.filter(title__icontains=title_query)
        notes_list = [{'id': note.id, 'title': note.title, 'body': note.body} for note in notes]
        return JsonResponse(notes_list, safe=False)

# Update Note
@method_decorator(csrf_exempt, name='dispatch')
class UpdateNoteView(View):
    def put(self, request, note_id):
        data = json.loads(request.body)
        note = get_object_or_404(Note, id=note_id)
        note.title = data.get('title', note.title)
        note.body = data.get('body', note.body)
        note.save()
        return JsonResponse({'id': note.id, 'title': note.title, 'body': note.body, 'created_at': note.created_at, 'updated_at': note.updated_at})

