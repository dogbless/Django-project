############
polls views
############

@login_required(login_url="/user_auth/") 
def index(request):
    #return HttpResponse("Hello world. You're at the polls index.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/poll.html", context)

This function types out "your're at the polls index, orders the questions by the published date and returns the html file for the polls interface.


def detail(request, question_id):
     question = get_object_or_404(Question, pk=question_id)
     return render(request, "polls/detail.html", {"question": question})


This function returns the detail.html



@login_required(login_url="/accounts/login/")   
def vote(request, question_id):
   question =get_object_or_404(Question, pk=question_id)
   try:
       selected_choice = question.choice_set.get(
           pk = request.POST['choice']
       )
   except (KeyError, Choice.DoesNotExist):
       
       return render(request, 'polls/details.html',{
           'question': question,
           'error message': "you didn't select a choice."
       })
   else:
       selected_choice.votes +=1
       selected_choice.save()



       return HttpResponseRedirect(
           reverse('polls:results', args=(question_id,))
       )

This function lets ths user vote for the option they want.




def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question':question})


This function allows for the results to get shown via the resutls.html page


