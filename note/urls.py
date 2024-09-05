from django.urls import path
from .views import CreateNoteView, FetchNoteView, QueryNotesView, UpdateNoteView, FetchAllNotesView

urlpatterns = [
    path('note/', CreateNoteView.as_view(), name='create_note'),
    path('note/<int:note_id>/', FetchNoteView.as_view(), name='fetch_note'),
    path('note/search/', QueryNotesView.as_view(), name='query_notes'),
    path('note/<int:note_id>/update/', UpdateNoteView.as_view(), name='update_note'),
    path('note/all/', FetchAllNotesView.as_view(), name='fetch_all_notes'),
]
