document.addEventListener('DOMContentLoaded', function() {
    // Добавляем контейнер для анимации перехода
    const transitionElement = document.createElement('div');
    transitionElement.className = 'page-transition';
    document.body.appendChild(transitionElement);

    // Добавляем прелоадер
    const preloader = document.createElement('div');
    preloader.className = 'preloader';
    preloader.innerHTML = '<div class="preloader-spinner"></div>';
    document.body.appendChild(preloader);

    // Функция для показа прелоадера
    function showPreloader() {
        preloader.classList.remove('hide');
    }

    // Функция для скрытия прелоадера
    function hidePreloader() {
        preloader.classList.add('hide');
    }

    // Обработка загрузки страницы
    window.addEventListener('load', function() {
        // Скрываем прелоадер
        hidePreloader();

        // Добавляем класс loaded к контенту для анимации появления
        const pageContent = document.querySelector('.page-content');
        if (pageContent) {
            pageContent.classList.add('loaded');
        }

        // Добавляем классы для анимированных элементов
        document.querySelectorAll('a:not([href^="#"])').forEach(link => {
            link.classList.add('animated-link');
        });

        document.querySelectorAll('.card').forEach(card => {
            card.classList.add('card-hover');
        });

        document.querySelectorAll('.btn').forEach(btn => {
            btn.classList.add('btn-animated');
        });

        document.querySelectorAll('.nav-link').forEach(item => {
            item.classList.add('menu-item');
            if (item.getAttribute('href') === window.location.pathname) {
                item.classList.add('active');
            }
        });

        // Добавляем анимацию для изображений
        document.querySelectorAll('.product-image, .article-image').forEach(container => {
            container.classList.add('image-hover');
        });
    });

    // Обработка переходов по ссылкам
    document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (link && 
            !link.hasAttribute('target') && 
            !link.hasAttribute('download') && 
            !link.getAttribute('href').startsWith('#') &&
            !link.getAttribute('href').startsWith('tel:') &&
            !link.getAttribute('href').startsWith('mailto:')) {
            
            e.preventDefault();
            const href = link.getAttribute('href');

            // Показываем анимацию ухода
            transitionElement.classList.add('fade-out');

            // Ждем окончания анимации и переходим на новую страницу
            setTimeout(() => {
                window.location.href = href;
            }, 500);
        }
    });

    // Обработка кнопки "назад" в браузере
    window.addEventListener('popstate', function() {
        transitionElement.classList.add('fade-out');
    });

    // Анимация модальных окон
    const modalTriggers = document.querySelectorAll('[data-toggle="modal"]');
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function() {
            const modalId = this.getAttribute('data-target');
            const modal = document.querySelector(modalId);
            if (modal) {
                modal.classList.add('modal-animated');
                setTimeout(() => {
                    modal.classList.add('show');
                }, 10);
            }
        });
    });

    // Закрытие модальных окон
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('hide.bs.modal', function() {
            this.classList.remove('show');
            setTimeout(() => {
                this.classList.remove('modal-animated');
            }, 300);
        });
    });
});
