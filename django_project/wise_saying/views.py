from django.shortcuts import render
from .forms import MemberForm, MemberLoginForm, SayingForm
from django.shortcuts import redirect
from wise_saying.models import Member, Saying, Like

# Create your views here.
def main(request):  # 메인
    if request.session.has_key('member_id'):
        return redirect('home')
    return render(request, 'wise_saying/main.html', {})

def login(request): # 로그인
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

def logout(request): # 로그아웃
    request.session.flush()
    return redirect('main')

def register(request): # 회원 가입
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    form = MemberForm()
    return render(request, 'wise_saying/register.html', {'form': form})


def home(request): # 로그인 후 홈
    if not request.session.has_key('member_id'):
        return redirect('login')

    member_id = request.session['member_id']
    return render(request, 'wise_saying/home.html', {'member_id':member_id})


def post(request): # 명언 보기
    if not request.session.has_key('member_id'):
        return redirect('login')

    member = Member.objects.get(member_id=request.session['member_id'])

    saying = Saying.objects.order_by('?').first() # 랜덤으로 섞은것 중에 첫번째 아이템을 가져옴
    writer = saying.writer
    
    is_like = False
    try:
        liked = Like.objects.get(member=member)
        is_like = True
    except Like.DoesNotExist:
        is_like = False

    contents = saying.contents
    writer_name = member.name
        
    return render(request, 'wise_saying/post.html', {'contents': contents, 'writer_name': writer_name, 'is_like':is_like})


def post_new(request): # 명언 작성
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
    return render(request, 'wise_saying/post_new.html', {'form': form})


def post_me(request): # 내가 작성한 명언
    if not request.session.has_key('member_id'):
        return redirect('login')
    
    member = Member.objects.get(member_id=request.session['member_id'])
    saying_list = Saying.objects.filter(writer=member)

    return render(request, 'wise_saying/post_me.html', {'saying_list': saying_list})



