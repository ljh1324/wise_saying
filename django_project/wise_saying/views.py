from django.shortcuts import render
from .forms import MemberForm, MemberLoginForm, SayingForm
from django.shortcuts import redirect
from wise_saying.models import Member, Saying

# Create your views here.
def main(request):
    return render(request, 'wise_saying/main.html', {})

def login(request):
    if request.method == "POST":
        form = MemberLoginForm(request.POST)
        #print("test2")
        member_id = form['member_id'].value()
        password = form['password'].value()
        #print(member_id)
        #print(password)

        try:
            member = Member.objects.get(member_id=member_id)
            if password == member.password:
                request.session['member_id'] = member_id
                return redirect('home')

        except Member.DoesNotExist:
            member = None

        #print(member.password)
        """
        if form.is_valid():
            print("test")
            # .is_valid() 를 통해서 검증에 통과한 값은 cleaned_data 변수명으로 사전타입 으로 제공된다.
            member_id = form.cleaned_data['member_id']
            request.session['member_id'] = member_id
            return redirect('home')
        """
    form = MemberLoginForm()
    return render(request, 'wise_saying/login.html', {'form': form})

def logout(request):
    request.session.flush()
    return redirect('main')

def register(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    form = MemberForm()
    return render(request, 'wise_saying/register.html', {'form': form})


def home(request):
    if not request.session.has_key('member_id'):
        return redirect('login')

    member_id = request.session['member_id']
    return render(request, 'wise_saying/home.html', {'member_id':member_id})


def post_new(request):
    if not request.session.has_key('member_id'):
        return redirect('login')

    if request.method == "POST":
        form = SayingForm(request.POST)
        
        if form.is_valid():
            saying = form.save(commit=False)
            member = Member.objects.get(member_id=request.session['member_id'])
            saying.writer = member
            saying.save()
            return redirect('home')
            
    form = SayingForm()
    return render(request, 'wise_saying/register.html', {'form': form})


def my_post(request):
    if not request.session.has_key('member_id'):
        return redirect('login')
    
    member = Member.objects.get(member_id=request.session['member_id'])
    saying_list = Saying.objects.filter(writer=member)

    return render(request, 'wise_saying/my_post.html', {'saying_list': saying_list})



