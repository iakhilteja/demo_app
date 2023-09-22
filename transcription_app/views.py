from django.shortcuts import render, redirect
from django.http import JsonResponse
import glob
import os

def upload_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        audio_list = glob.glob('audio_files/*')
        pk_list = []
        for file in audio_list:
            pk_list.append(int(file.split('.')[0].split('$')[1]))
        
        if len(pk_list)==0:
            pk=1
        else:
            pk_list=sorted(pk_list)
            pk = pk_list[-1]+1
        
        audio_name = audio_file.name.split('.')[0]+'$'+str(pk)+'.'+audio_file.name.split('.')[1]
        filename = os.path.join('audio_files/',audio_name)
        with open(filename, 'wb') as destination_file:
            for chunk in audio_file.chunks():
                destination_file.write(chunk)            
        return redirect('audio_detail', pk=pk)
    return render(request, 'upload_audio.html')

def audio_detail(request, pk):
    audio_list = glob.glob('audio_files/*')
    for file in audio_list:
        if int(file.split('.')[0].split('$')[1])==pk:
            if os.path.exists(file):
                with open(file, 'rb') as file:
                    audio_file = file.read()
                audio = {"audio_file":audio_file,"filename":str(file).split('/')[-1].split('.')[0],"transcript":"","pk":pk}
                break
            else:
                print(f"The file '{file}' does not exist.")
            
    return render(request, 'audio_detail.html', {'audio': audio})

def transcript(request, pk):
    transcript = str(pk)

    return JsonResponse({'transcript': transcript})
