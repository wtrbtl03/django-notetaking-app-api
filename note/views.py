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
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        title = data.get('title')
        body = data.get('body')

        if not title or not body:
            return JsonResponse({"error": "Both 'title' and 'body' are required fields"}, status=400)

        note = Note.objects.create(title=title, body=body)
        return JsonResponse({
            'id': note.id,
            'title': note.title,
            'body': note.body,
            'created_at': note.created_at,
            'updated_at': note.updated_at
        }, status=201)


# Fetch all notes
class FetchAllNotesView(View):
    def get(self, request):
        notes = Note.objects.all()
        notes_list = [{
            'id': note.id,
            'title': note.title,
            'body': note.body,
            'created_at': note.created_at,
            'updated_at': note.updated_at
        } for note in notes]

        if not notes_list:
            return JsonResponse({"error": "No notes found"}, status=404)

        return JsonResponse(notes_list, safe=False, status=200)


# Fetch Note by ID
class FetchNoteView(View):
    def get(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)
        return JsonResponse({
            'id': note.id,
            'title': note.title,
            'body': note.body,
            'created_at': note.created_at,
            'updated_at': note.updated_at
        }, status=200)


# Query Notes by Title Substring
class QueryNotesView(View):
    def get(self, request):
        title_query = request.GET.get('title', '')

        if not title_query:
            return JsonResponse({"error": "Query parameter 'title' is required"}, status=400)

        notes = Note.objects.filter(title__icontains=title_query)
        notes_list = [{'id': note.id, 'title': note.title, 'body': note.body} for note in notes]

        if not notes_list:
            return JsonResponse({"error": "No notes found"}, status=404)

        return JsonResponse(notes_list, safe=False, status=200)


# Update Note
@method_decorator(csrf_exempt, name='dispatch')
class UpdateNoteView(View):
    def put(self, request, note_id):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        note = get_object_or_404(Note, id=note_id)

        title = data.get('title')
        body = data.get('body')

        if not title and not body:
            return JsonResponse({"error": "At least one of 'title' or 'body' must be provided for update"}, status=400)

        note.title = title if title else note.title
        note.body = body if body else note.body
        note.save()

        return JsonResponse({
            'id': note.id,
            'title': note.title,
            'body': note.body,
            'created_at': note.created_at,
            'updated_at': note.updated_at
        }, status=200)
