import os

hair_cards = ""
for i in range(1, 21):
    hair_cards += f"""
          <div class="service-card work-item" data-cat="hair" style="padding: 12px;">
            <div style="border-radius: var(--radius-sm); overflow: hidden; height: 280px; margin-bottom: 12px; border: 1px solid var(--border-gold);">
              <img src="assets/portfolio_full/hair_{i}.jpg" alt="Работа парикмахера {i}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <span class="service-badge">Окрашивание & Стрижки</span>
            <h3 class="serif-title" style="font-size: 1.1rem; margin-top: 6px;">Работа мастера #{i}</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted);">Сложное окрашивание, стрижка и авторская укладка.</p>
          </div>"""

brovi_cards = ""
for i in range(1, 16):
    brovi_cards += f"""
          <div class="service-card work-item" data-cat="brows" style="padding: 12px;">
            <div style="border-radius: var(--radius-sm); overflow: hidden; height: 280px; margin-bottom: 12px; border: 1px solid var(--border-gold);">
              <img src="assets/portfolio_full/brovi_{i}.jpg" alt="Оформление бровей {i}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <span class="service-badge">Брови & Ресницы</span>
            <h3 class="serif-title" style="font-size: 1.1rem; margin-top: 6px;">Работа бровиста #{i}</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted);">Архитектура, окрашивание хной и ламинирование.</p>
          </div>"""

massage_cards = ""
for i in range(1, 16):
    massage_cards += f"""
          <div class="service-card work-item" data-cat="massage" style="padding: 12px;">
            <div style="border-radius: var(--radius-sm); overflow: hidden; height: 280px; margin-bottom: 12px; border: 1px solid var(--border-gold);">
              <img src="assets/portfolio_full/massage_{i}.jpg" alt="Массаж и Уход {i}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <span class="service-badge">Массаж & Косметология</span>
            <h3 class="serif-title" style="font-size: 1.1rem; margin-top: 6px;">Результат процедуры #{i}</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted);">Скульптурный лифтинг-массаж лица и уход за телом.</p>
          </div>"""

nail_cards = ""
for i in range(1, 16):
    nail_cards += f"""
          <div class="service-card work-item" data-cat="nail" style="padding: 12px;">
            <div style="border-radius: var(--radius-sm); overflow: hidden; height: 280px; margin-bottom: 12px; border: 1px solid var(--border-gold);">
              <img src="assets/portfolio_full/nail_{i}.jpg" alt="Nail Сервис {i}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <span class="service-badge">Nail Сервис</span>
            <h3 class="serif-title" style="font-size: 1.1rem; margin-top: 6px;">Маникюр & Дизайн #{i}</h3>
            <p style="font-size: 0.82rem; color: var(--text-muted);">Аппаратный маникюр и стойкое покрытие Gel Polish.</p>
          </div>"""

full_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Работы мастеров — Салон красоты "Эгоистка" (Колпино)</title>
  <meta name="description" content="Полное портфолио работ мастеров салона красоты Эгоистка в Колпино: более 66 реальных фотографий окрашивания, массажа, ухода, маникюра, бровей. Телефон: +7 (812) 935-45-90.">
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="style.css">
  <script src="app.js" defer></script>
</head>
<body>

  <!-- Top Contact Bar -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-info">
        <div class="top-bar-item">
          <i class="fas fa-map-marker-alt"></i>
          <span class="address-text">Санкт-Петербург, г. Колпино, ул. Павловская, д. 7, 1-й этаж</span>
        </div>
        <div class="top-bar-item">
          <i class="far fa-clock"></i>
          <span>Ежедневно 10:00 – 21:00</span>
        </div>
      </div>
      <div class="top-bar-info">
        <a href="tel:+78129354590" class="top-bar-item gold-text" style="font-weight: 700;">
          <i class="fas fa-phone-alt"></i> +7 (812) 935-45-90
        </a>
        <div class="social-links">
          <a href="https://vk.com/egoistka_kolpino" target="_blank" class="social-icon" title="ВКонтакте">
            <i class="fab fa-vk"></i>
          </a>
          <a href="https://www.instagram.com/salon_egoistcka" target="_blank" class="social-icon" title="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Header Navigation -->
  <header class="header">
    <div class="container header-inner">
      <a href="index.html" class="logo-brand">
        <span class="logo-title">ЭГОИСТКА</span>
        <span class="logo-sub">САЛОН КРАСОТЫ • КОЛПИНО</span>
      </a>

      <nav>
        <ul class="nav-menu">
          <li><a href="index.html" class="nav-link">Главная</a></li>
          <li><a href="massazh-lica-i-tela.html" class="nav-link">Массаж</a></li>
          <li><a href="services.html" class="nav-link">Услуги и цены</a></li>
          <li><a href="bonusy.html" class="nav-link">Сертификаты</a></li>
          <li><a href="nash-salon.html" class="nav-link">О салоне</a></li>
          <li><a href="raboty.html" class="nav-link active">Работы</a></li>
          <li><a href="contacts.html" class="nav-link">Контакты</a></li>
          <li class="nav-dropdown">
            <a href="#" class="nav-link">Ещё <i class="fas fa-chevron-down" style="font-size: 0.7rem; margin-left: 2px;"></i></a>
            <ul class="dropdown-menu">
              <li class="dropdown-item"><a href="brendy.html"><i class="fas fa-award"></i> Бренды косметики</a></li>
              <li class="dropdown-item"><a href="grafik-otpuskov.html"><i class="far fa-calendar-alt"></i> График отпусков 2026</a></li>
              <li class="dropdown-item"><a href="arenda-rabochego-mesta.html"><i class="fas fa-chair"></i> Аренда рабочего места</a></li>
            </ul>
          </li>
          <li style="width: 100%; margin-top: 10px;">
            <button class="btn-primary btn-dikidi mobile-book-btn" style="width: 100%; justify-content: center;"><i class="far fa-calendar-check"></i> Записаться онлайн</button>
          </li>
        </ul>
      </nav>

      <button class="btn-primary btn-dikidi">
        <i class="far fa-calendar-check"></i> Записаться онлайн
      </button>

      <div class="mobile-toggle">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </header>

  <main>
    <div class="page-hero">
      <div class="container">
        <div class="breadcrumbs">
          <a href="index.html">Главная</a>
          <span>/</span>
          <span style="color: var(--gold-light);">Работы мастеров</span>
        </div>
        <h1 class="page-title serif-title">Портфолио выполненных работ (66 фото)</h1>
        <p class="page-subtitle">Полный каталог оригинальных работ наших мастеров (15+ работ в каждой категории).</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        
        <!-- Interactive Category Filter Tabs -->
        <div class="filter-tabs">
          <button type="button" class="tab-btn active" data-filter="all">Все работы (66)</button>
          <button type="button" class="tab-btn" data-filter="hair">Окрашивание & Стрижки (20)</button>
          <button type="button" class="tab-btn" data-filter="massage">Массаж & Уход (15)</button>
          <button type="button" class="tab-btn" data-filter="nail">Nail Сервис (15)</button>
          <button type="button" class="tab-btn" data-filter="brows">Брови & Ресницы (16)</button>
        </div>

        <div class="services-grid" style="grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));">
          {hair_cards}
          {brovi_cards}
          {massage_cards}
          {nail_cards}
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="logo-title serif-title" style="margin-bottom: 12px;">ЭГОИСТКА</div>
          <p style="color: var(--text-muted); font-size: 0.9rem; max-width: 320px; margin-bottom: 20px;">
            Салон красоты в Колпино. Профессиональный массаж лица и тела, парикмахерские услуги, косметология и эстетический уход.
          </p>
          <div style="font-size: 0.85rem; color: var(--gold-light);">
            📍 г. Колпино, ул. Павловская, д. 7<br>
            📞 +7 (812) 935-45-90
          </div>
        </div>

        <div>
          <h4 class="footer-col-title">Разделы сайта</h4>
          <ul class="footer-links">
            <li><a href="index.html">Главная</a></li>
            <li><a href="massazh-lica-i-tela.html">Массаж лица и тела</a></li>
            <li><a href="services.html">Услуги и цены</a></li>
            <li><a href="bonusy.html">Подарочные сертификаты</a></li>
            <li><a href="nash-salon.html">О салоне</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">Клиентам и партнерам</h4>
          <ul class="footer-links">
            <li><a href="raboty.html">Работы мастеров</a></li>
            <li><a href="brendy.html">Бренды косметики</a></li>
            <li><a href="grafik-otpuskov.html">График отпусков 2026</a></li>
            <li><a href="arenda-rabochego-mesta.html">Аренда рабочего места</a></li>
            <li><a href="contacts.html">Контакты</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">Онлайн-запись</h4>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 16px;">Запишитесь на удобное время через систему DIKIDI.</p>
          <button class="btn-primary btn-dikidi" style="width: 100%; justify-content: center;"><i class="far fa-calendar-check"></i> Записаться в DIKIDI</button>
        </div>
      </div>

      <div class="footer-bottom">
        <div>© 2026 Салон красоты «Эгоистка». Все права защищены.</div>
        <div>г. Колпино, ул. Павловская, д. 7</div>
      </div>
    </div>
  </footer>

  <button class="floating-booking btn-dikidi"><i class="far fa-calendar-check"></i> Записаться онлайн</button>

  <div id="dikidiModal" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="serif-title gold-text" style="font-size: 1.4rem;">Онлайн-запись в салон «Эгоистка»</h3>
        <button class="modal-close">&times;</button>
      </div>
      <div class="modal-body">
        <iframe id="dikidiIframe" src="https://dikidi.net/#widget=51285" title="DIKIDI Booking Widget"></iframe>
      </div>
    </div>
  </div>

</body>
</html>
"""

with open("raboty.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("raboty.html updated successfully with 66 portfolio cards!")
