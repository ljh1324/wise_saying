from django.shortcuts import render
from .forms import MemberForm, MemberLoginForm, SayingForm
from django.shortcuts import redirect
from wise_saying.models import Member, Saying, Like
from django.http import HttpResponse

import json

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
        like = Like.objects.get(member=member, saying=saying)
        is_like = True
    except Like.DoesNotExist:
        is_like = False

    contents = saying.contents
    writer_name = member.name
        
    #return render(request, 'wise_saying/post.html', {'contents': contents, 'writer_name': writer_name, 'is_like':is_like})
    saying_id = saying.id
    return render(request, 'wise_saying/post.html', {'contents': contents, 'writer_name': writer_name, 'is_like':is_like, 'saying_id':saying_id})


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
    #saying_list = Saying.objects.select_related().filter(writer=request.session['member_id'])  오직 아이디 값으로만 접근 가능 writer=id
    print(saying_list)
    return render(request, 'wise_saying/post_me.html', {'saying_list': saying_list})


def post_like(request): # 내가 작성한 명언
    if not request.session.has_key('member_id'):
        return redirect('login')
    
    member = Member.objects.get(member_id=request.session['member_id'])
    #like_list = Like.objects.filter(member=member)
    '''
    like_list = Like.objects.filter(member=member).values('saying')
    saying_list = []
    print(saying_list)
    for like in like_list:
        saying_id = like['saying']
        saying = Saying.objects.get(id=saying_id)
        saying_list.append(saying)
    print(saying_list)
    '''
    #saying_list = Saying.objects.filter(member=member).values('saying__contents')

    like_list = Like.objects.filter(member=member).values('saying')
    saying_list = Saying.objects.filter(id__in=like_list)

    print(saying_list)
    return render(request, 'wise_saying/post_like.html', {'saying_list': saying_list})


# Create your views here.
def like(request):
    if request.method == 'POST' and request.is_ajax():
        saying_id = request.POST.get('saying_id', None)
        is_like = request.POST.get('is_like', None)

        print(saying_id)
        print(is_like)

        is_like = (is_like == 'true')
        print(is_like)

        if is_like:
            member = Member.objects.get(member_id=request.session['member_id'])
            saying = Saying.objects.get(id=saying_id)
            try:
                like = Like.objects.get(member=member, saying=saying)
                like.delete()
            except Like.DoesNotExist:
                pass
        else:
            member = Member.objects.get(member_id=request.session['member_id'])
            saying = Saying.objects.get(id=saying_id)
            like = Like(member=member, saying=saying)
            like.save()

        return HttpResponse("Success")

    else:
        return redirect('home')
