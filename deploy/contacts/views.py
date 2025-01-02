from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import ContactMessage
from notifications.services import create_message_notification
from catalog.cart import get_or_create_cart
import logging

logger = logging.getLogger(__name__)

def contact_view(request):
    # Получаем корзину
    cart = get_or_create_cart(request)
    
    # Получаем текущий язык из сессии или используем русский по умолчанию
    current_language = request.session.get('language', settings.LANGUAGE_CODE)
    
    # Контактная информация
    contact_info = {
        'address': {
            'ru': 'ул. Бунёдкор, 29, Ташкент, Узбекистан',
            'en': '29 Bunyodkor Street, Tashkent, Uzbekistan',
            'uz': 'Bunyodkor ko\'chasi, 29, Toshkent, O\'zbekiston'
        },
        'phone': '+998 71 123-45-67',
        'email': 'info@afiyat-energy.uz',
        'working_hours': {
            'ru': 'Пн-Пт: 9:00 - 18:00',
            'en': 'Mon-Fri: 9:00 AM - 6:00 PM',
            'uz': 'Du-Ju: 9:00 - 18:00'
        }
    }
    
    context = {
        'cart': cart,  # Добавляем корзину в контекст
        'current_language': current_language,
        'contact_info': contact_info,
        'page_title': {
            'ru': 'Свяжитесь с нами',
            'en': 'Contact Us',
            'uz': 'Biz bilan bog\'laning'
        }[current_language],
        'page_subtitle': {
            'ru': 'Мы всегда готовы ответить на ваши вопросы',
            'en': 'We are always ready to answer your questions',
            'uz': 'Biz sizning savollaringizga javob berishga doimo tayyormiz'
        }[current_language],
        'contact_labels': {
            'address': {
                'ru': 'Адрес',
                'en': 'Address',
                'uz': 'Manzil'
            }[current_language],
            'phone': {
                'ru': 'Телефон',
                'en': 'Phone',
                'uz': 'Telefon'
            }[current_language],
            'email': {
                'ru': 'Электронная почта',
                'en': 'Email',
                'uz': 'Elektron pochta'
            }[current_language]
        },
        'form_placeholders': {
            'name': {
                'ru': 'Ваше имя',
                'en': 'Your name',
                'uz': 'Ismingiz'
            }[current_language],
            'email': {
                'ru': 'Ваш email',
                'en': 'Your email',
                'uz': 'Elektron pochtangiz'
            }[current_language],
            'phone': {
                'ru': 'Ваш телефон',
                'en': 'Your phone',
                'uz': 'Telefon raqamingiz'
            }[current_language],
            'subject': {
                'ru': 'Тема сообщения',
                'en': 'Message subject',
                'uz': 'Xabar mavzusi'
            }[current_language],
            'message': {
                'ru': 'Ваше сообщение',
                'en': 'Your message',
                'uz': 'Xabaringiz'
            }[current_language],
            'submit': {
                'ru': 'Отправить сообщение',
                'en': 'Send message',
                'uz': 'Xabar yuborish'
            }[current_language]
        }
    }
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            subject = request.POST.get('subject', '').strip()
            message = request.POST.get('message', '').strip()

            # Проверяем обязательные поля
            if not all([name, email, subject, message]):
                error_msg = {
                    'ru': 'Пожалуйста, заполните все обязательные поля.',
                    'en': 'Please fill in all required fields.',
                    'uz': 'Iltimos, barcha majburiy maydonlarni to\'ldiring.'
                }[current_language]
                messages.error(request, error_msg)
                context['form_data'] = request.POST
                return render(request, 'contacts/contact.html', context)

            # Проверяем валидность email
            try:
                validate_email(email)
            except ValidationError:
                error_msg = {
                    'ru': 'Пожалуйста, введите корректный email адрес.',
                    'en': 'Please enter a valid email address.',
                    'uz': 'Iltimos, to\'g\'ri elektron pochta manzilini kiriting.'
                }[current_language]
                messages.error(request, error_msg)
                context['form_data'] = request.POST
                return render(request, 'contacts/contact.html', context)

            # Создаем новое сообщение
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )

            # Отправляем уведомление в Telegram
            create_message_notification(contact_message)

            # Отправляем уведомление на email
            try:
                send_mail(
                    f'Новое сообщение от {name}',
                    f'Имя: {name}\nEmail: {email}\nТелефон: {phone}\nТема: {subject}\nСообщение: {message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f'Ошибка отправки email: {str(e)}')

            success_msg = {
                'ru': 'Спасибо! Ваше сообщение успешно отправлено.',
                'en': 'Thank you! Your message has been sent successfully.',
                'uz': 'Rahmat! Xabaringiz muvaffaqiyatli yuborildi.'
            }[current_language]
            messages.success(request, success_msg)
            return redirect('contacts:contact')

        except Exception as e:
            logger.error(f'Ошибка обработки формы: {str(e)}')
            error_msg = {
                'ru': 'Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте позже.',
                'en': 'An error occurred while sending the message. Please try again later.',
                'uz': 'Xabar yuborishda xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko\'ring.'
            }[current_language]
            messages.error(request, error_msg)
            context['form_data'] = request.POST
            return render(request, 'contacts/contact.html', context)

    return render(request, 'contacts/contact.html', context)

def contact_form(request):
    if request.method == 'POST':
        try:
            # Получаем данные из формы
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Создаем новое сообщение
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )

            # Отправляем уведомление в Telegram
            create_message_notification(contact_message)

            return JsonResponse({
                'success': True,
                'message': 'Your message has been sent successfully!'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })
