export default class Catalog {
  constructor() {
    this.filters = new Map();
    this.sort = 'default';
    this.page = 1;
    this.init();
  }

  init() {
    this.bindEvents();
    this.initRangeSliders();
  }

  bindEvents() {
    // Фильтры
    document.querySelectorAll('.filter-checkbox').forEach(checkbox => {
      checkbox.addEventListener('change', () => this.handleFilterChange());
    });

    // Сортировка
    const sortSelect = document.querySelector('.sort-select');
    if (sortSelect) {
      sortSelect.addEventListener('change', (e) => {
        this.sort = e.target.value;
        this.updateProducts();
      });
    }

    // Пагинация
    document.addEventListener('click', (e) => {
      const pageLink = e.target.closest('.page-link');
      if (pageLink) {
        e.preventDefault();
        this.page = parseInt(pageLink.dataset.page);
        this.updateProducts();
      }
    });
  }

  initRangeSliders() {
    const priceRange = document.querySelector('.price-range');
    if (priceRange) {
      noUiSlider.create(priceRange, {
        start: [0, 1000000],
        connect: true,
        range: {
          'min': 0,
          'max': 1000000
        },
        format: {
          to: value => Math.round(value),
          from: value => parseInt(value)
        }
      });

      priceRange.noUiSlider.on('change', () => {
        const [min, max] = priceRange.noUiSlider.get();
        this.filters.set('price_min', min);
        this.filters.set('price_max', max);
        this.updateProducts();
      });
    }
  }

  async handleFilterChange() {
    // Собираем все активные фильтры
    document.querySelectorAll('.filter-group').forEach(group => {
      const name = group.dataset.filter;
      const checked = Array.from(group.querySelectorAll('input:checked'))
        .map(input => input.value);
      
      if (checked.length) {
        this.filters.set(name, checked);
      } else {
        this.filters.delete(name);
      }
    });

    this.page = 1; // Сброс на первую страницу при изменении фильтров
    await this.updateProducts();
  }

  async updateProducts() {
    const params = new URLSearchParams();
    
    // Добавляем все фильтры в параметры
    this.filters.forEach((value, key) => {
      if (Array.isArray(value)) {
        value.forEach(v => params.append(key, v));
      } else {
        params.append(key, value);
      }
    });

    params.append('sort', this.sort);
    params.append('page', this.page);

    try {
      const response = await fetch(`/api/products/?${params.toString()}`);
      if (!response.ok) throw new Error('Network response was not ok');

      const data = await response.json();
      this.renderProducts(data.products);
      this.renderPagination(data.pagination);
      
      // Обновляем URL с новыми параметрами
      window.history.pushState({}, '', `?${params.toString()}`);
    } catch (error) {
      console.error('Error updating products:', error);
    }
  }

  renderProducts(products) {
    const container = document.querySelector('.products-grid');
    if (!container) return;

    container.innerHTML = products.map(product => `
      <div class="card card-product">
        <div class="card-image">
          <img src="${product.image}" alt="${product.name}">
          ${this.renderProductLabels(product)}
        </div>
        <div class="card-body">
          <h3 class="card-title">${product.name}</h3>
          <div class="card-price">
            <span class="price-current">${this.formatPrice(product.price)}</span>
            ${product.old_price ? `<span class="price-old">${this.formatPrice(product.old_price)}</span>` : ''}
          </div>
          <button class="btn btn-primary add-to-cart" data-product-id="${product.id}">
            В корзину
          </button>
        </div>
      </div>
    `).join('');
  }

  renderProductLabels(product) {
    const labels = [];
    
    if (product.is_new) {
      labels.push('<span class="label label-new">Новинка</span>');
    }
    if (product.discount) {
      labels.push(`<span class="label label-sale">-${product.discount}%</span>`);
    }
    
    return labels.length ? `<div class="card-labels">${labels.join('')}</div>` : '';
  }

  renderPagination(pagination) {
    const container = document.querySelector('.pagination');
    if (!container) return;

    container.innerHTML = `
      <li class="page-item ${pagination.current_page === 1 ? 'disabled' : ''}">
        <a class="page-link" href="#" data-page="${pagination.current_page - 1}">
          Предыдущая
        </a>
      </li>
      ${this.renderPaginationPages(pagination)}
      <li class="page-item ${pagination.current_page === pagination.total_pages ? 'disabled' : ''}">
        <a class="page-link" href="#" data-page="${pagination.current_page + 1}">
          Следующая
        </a>
      </li>
    `;
  }

  renderPaginationPages(pagination) {
    const pages = [];
    const current = pagination.current_page;
    const total = pagination.total_pages;

    // Логика отображения страниц с многоточием
    for (let i = 1; i <= total; i++) {
      if (
        i === 1 ||
        i === total ||
        (i >= current - 2 && i <= current + 2)
      ) {
        pages.push(`
          <li class="page-item ${i === current ? 'active' : ''}">
            <a class="page-link" href="#" data-page="${i}">${i}</a>
          </li>
        `);
      } else if (
        i === current - 3 ||
        i === current + 3
      ) {
        pages.push('<li class="page-item disabled"><span class="page-link">...</span></li>');
      }
    }

    return pages.join('');
  }

  formatPrice(price) {
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: 'UZS'
    }).format(price);
  }
}
