from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileRecordForm
from .models import FileRecord

def create_file_record(request):
    if request.method == 'POST':
        form = FileRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('file_record_list')
    else:
        form = FileRecordForm()
    
    return render(request, 'create_file_record.html', {'form': form})

@permission_required('app_name.can_edit_file_record', raise_exception=True)
def edit_file_record(request, pk):
    file_record = get_object_or_404(FileRecord, pk=pk)
    if request.method == 'POST':
        form = FileRecordForm(request.POST, instance=file_record)
        if form.is_valid():
            form.save()
            return redirect('file_record_list')
    else:
        form = FileRecordForm(instance=file_record)
    
    return render(request, 'edit_file_record.html', {'form': form})
