
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Language, Lesson, UserProgress, HardwareSystem, HardwareChallenge, HardwareProgress

# Create your views here.
def landing(request):
    return render(request, 'core/landing.html')

@login_required(login_url='login')
def language_list(request):
    languages = Language.objects.all()
    return render(request, 'core/language_list.html', {'languages': languages})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'core/login.html', {'form': form})

@login_required(login_url='login')
def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)
    progress, _ = UserProgress.objects.get_or_create(user=request.user, language=language)
    lessons = language.lessons.all()
    return render(request, 'core/language_detail.html', {
        'language': language,
        'lessons': lessons,
        'progress': progress,
    })

@login_required(login_url='login')
def lesson_detail(request, pk=None, language_pk=None, lesson_order=None):
    if pk is not None:
        lesson = get_object_or_404(Lesson, pk=pk)
        language = lesson.language
    else:
        language = get_object_or_404(Language, pk=language_pk)
        lesson = get_object_or_404(Lesson, language=language, order=lesson_order)

    progress, _ = UserProgress.objects.get_or_create(user=request.user, language=language)

    if request.method == 'POST':
        if progress.current_lesson <= lesson.order:
            progress.current_lesson = lesson.order + 1
            progress.save()

        next_lesson = Lesson.objects.filter(language=language, order__gt=lesson.order).order_by('order').first()
        if next_lesson:
            return redirect('lesson_detail', pk=next_lesson.pk)
        return redirect('language_detail', pk=language.pk)

    all_lessons = Lesson.objects.filter(language=lesson.language).order_by('order')
    prev_lesson = Lesson.objects.filter(language=lesson.language, order__lt=lesson.order).order_by('-order').first()
    next_lesson = Lesson.objects.filter(language=lesson.language, order__gt=lesson.order).order_by('order').first()
    total_lessons = all_lessons.count()
    completed_count = UserProgress.objects.filter(
        user=request.user,
        language=lesson.language,
        current_lesson__gte=lesson.order
    ).count()
    mode_map = {
        'C': 'text/x-csrc',
        'Assembly': 'text/x-asm',
        'Machine Language': 'text/x-asm'
    }
    codemirror_mode = mode_map.get(lesson.language.name, 'text/x-csrc')
    languages = Language.objects.all().order_by('name')
    return render(request, 'core/lesson_detail.html', {
        'lesson': lesson,
        'all_lessons': all_lessons,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
        'total_lessons': total_lessons,
        'completed_count': completed_count,
        'codemirror_mode': codemirror_mode,
        'languages': languages,
    })


@login_required(login_url='login')
def try_it(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    mode_map = {
        'C': 'text/x-csrc',
        'Assembly': 'text/x-asm',
        'Machine Language': 'text/x-asm'
    }
    codemirror_mode = mode_map.get(lesson.language.name, 'text/x-csrc')
    return render(request, 'core/try_it.html', {
        'lesson': lesson,
        'codemirror_mode': codemirror_mode,
    })


@login_required(login_url='login')
def lesson_complete(request, pk):
    if request.method == 'POST':
        lesson = get_object_or_404(Lesson, pk=pk)
        progress, _ = UserProgress.objects.get_or_create(
            user=request.user,
            language=lesson.language,
            defaults={'current_lesson': 0}
        )
        if lesson.order > progress.current_lesson:
            progress.current_lesson = lesson.order
            progress.save()
        next_lesson = Lesson.objects.filter(
            language=lesson.language,
            order__gt=lesson.order
        ).order_by('order').first()
        if next_lesson:
            return redirect('lesson_detail', pk=next_lesson.pk)
        return redirect('language_detail', pk=lesson.language.pk)
    return redirect('lesson_detail', pk=pk)


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            elif password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')
    return render(request, 'core/register.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    return redirect('language_list')

@login_required(login_url='login')
def hardware_list(request):
    systems = HardwareSystem.objects.all().order_by('unlock_order')
    completed_lessons = UserProgress.objects.filter(
        user=request.user,
        current_lesson__gte=5
    ).exists()
    return render(request, 'core/hardware_list.html', {
        'systems': systems,
        'unlocked': completed_lessons
    })

@login_required(login_url='login')
def hardware_detail(request, slug):
    system = get_object_or_404(HardwareSystem, slug=slug)
    challenges = system.challenges.all().order_by('order')
    completed_ids = HardwareProgress.objects.filter(
        user=request.user,
        completed=True
    ).values_list('challenge_id', flat=True)
    return render(request, 'core/hardware_detail.html', {
        'system': system,
        'challenges': challenges,
        'completed_ids': completed_ids,
    })

@login_required(login_url='login')
def hardware_challenge(request, slug, challenge_pk):
    system = get_object_or_404(HardwareSystem, slug=slug)
    challenge = get_object_or_404(HardwareChallenge, pk=challenge_pk, system=system)
    language = request.GET.get('lang', 'c')
    progress, _ = HardwareProgress.objects.get_or_create(user=request.user, challenge=challenge)
    starter_code = challenge.starter_code_asm if language == 'asm' else challenge.starter_code_c
    return render(request, 'core/hardware_challenge.html', {
        'system': system,
        'challenge': challenge,
        'language': language,
        'progress': progress,
        'starter_code': starter_code,
    })

@login_required(login_url='login')
def hardware_complete(request, slug, challenge_pk):
    if request.method == 'POST':
        system = get_object_or_404(HardwareSystem, slug=slug)
        challenge = get_object_or_404(HardwareChallenge, pk=challenge_pk, system=system)
        language = request.POST.get('language', 'c')
        progress, _ = HardwareProgress.objects.get_or_create(user=request.user, challenge=challenge)
        progress.completed = True
        progress.language_used = language
        progress.save()
        next_challenge = HardwareChallenge.objects.filter(system=system, order__gt=challenge.order).order_by('order').first()
        if next_challenge:
            return redirect('hardware_challenge', slug=slug, challenge_pk=next_challenge.pk)
        return redirect('hardware_detail', slug=slug)
    return redirect('hardware_list')


def logout_view(request):
    logout(request)
    return redirect('login')
