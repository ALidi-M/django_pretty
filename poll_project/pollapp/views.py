from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse

# Create your views here.
def home(request):

    polls = Poll.objects.all()
    context = { 'polls' : polls}

    return render(request,'myapps/home.html',context)


def create(request):
    
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

            # print(form.cleaned_data['question'])

    else:

        form = CreatePollForm()

    context = {'form': form}

    return render(request, 'myapps/create.html', context)


def vote(request,poll_id):

    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']

        if selected_option == 'option1':
            poll.option_one_count += 1

        elif selected_option == 'option2':
            poll.option_two_count += 1

        elif selected_option == 'option3':
            poll.option_three_count += 1

        else:
            return HttpResponse(status=400,content = 'invalid form entry!!!')
        
        poll.save()

        return redirect('results',poll_id = poll.id)


    context = {'poll':poll}

    return render(request,'myapps/vote.html',context)


def results(request,poll_id):

    poll = Poll.objects.get(pk=poll_id)



    context = { 'poll': poll}

    return render(request,'myapps/results.html',context)