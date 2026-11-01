<!DOCTYPE html>
<html lang="ar" dir="rtl" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>كارل ماركس: تشريح التاريخ ورأس المال | دراسة توثيقية وفكرية</title>
  <meta name="description" content="موقع توثيقي وتحليلي شامل عن الفيلسوف والاقتصادي الثوري كارل ماركس: سيرته، مؤلفاته، مفاهيمه المركزية، وخطه الزمني">

  <!-- Google Fonts: Cairo, Tajawal, Amiri -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;500;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">

  <!-- FontAwesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            marx: {
              bg: '#121417',
              bgDark: '#0d0f12',
              slate: '#1a1d24',
              card: '#222731',
              cardHover: '#29303d',
              border: '#2d3342',
              borderLight: '#3f475a',
              red: '#8b1e1e',
              redBright: '#a82828',
              redLight: '#dc2626',
              gold: '#c89658',
              goldLight: '#dfb173',
              goldDark: '#9e6d34',
              parchment: '#f0ece1',
              parchmentDark: '#e2dac6',
              textMuted: '#94a3b8'
            }
          },
          fontFamily: {
            cairo: ['Cairo', 'sans-serif'],
            tajawal: ['Tajawal', 'sans-serif'],
            amiri: ['Amiri', 'serif']
          }
        }
      }
    }
  </script>

  <style>
    /* CSS Variables & Academic Editorial Theme */
    :root {
      --bg-primary: #121417;
      --bg-secondary: #1a1d24;
      --bg-card: #222731;
      --border-color: #2d3342;
      --accent-red: #8b1e1e;
      --accent-red-hover: #a82828;
      --accent-gold: #c89658;
      --accent-gold-light: #dfb173;
      --text-heading: #f0ece1;
      --text-body: #cbd5e1;
      --text-muted: #8e9baa;
      --parchment-bg: #efe8d8;
      --parchment-border: #b89b72;
      --parchment-text: #2a2217;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-body);
      font-family: 'Cairo', 'Tajawal', sans-serif;
      overflow-x: hidden;
      line-height: 1.8;
      selection-background-color: var(--accent-red);
      selection-color: #ffffff;
    }

    ::selection {
      background-color: #8b1e1e;
      color: #f0ece1;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 9px;
    }
    ::-webkit-scrollbar-track {
      background: #121417;
    }
    ::-webkit-scrollbar-thumb {
      background: #2d3342;
      border-radius: 4px;
      border: 2px solid #121417;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #c89658;
    }

    /* Parchment Card Aesthetic */
    .parchment-box {
      background-color: #efe8d8;
      background-image: 
        radial-gradient(#d6cbaf 15%, transparent 16%),
        radial-gradient(#d6cbaf 15%, transparent 16%);
      background-size: 60px 60px;
      background-position: 0 0, 30px 30px;
      color: #2a2217;
      border: 3px double #9e8156;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), inset 0 0 40px rgba(184, 155, 114, 0.35);
      position: relative;
    }

    .parchment-box::before, .parchment-box::after {
      content: '';
      position: absolute;
      width: 18px;
      height: 18px;
      border-style: solid;
      border-color: #8b1e1e;
      pointer-events: none;
    }
    .parchment-box::before {
      top: 6px;
      right: 6px;
      border-width: 2px 2px 0 0;
    }
    .parchment-box::after {
      bottom: 6px;
      left: 6px;
      border-width: 0 0 2px 2px;
    }

    /* Vintage Etching Card */
    .vintage-concept-card {
      background: linear-gradient(145deg, #1f242e 0%, #171a21 100%);
      border: 1px solid #2d3342;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .vintage-concept-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, #c89658, transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .vintage-concept-card:hover {
      transform: translateY(-5px);
      border-color: #c89658;
      box-shadow: 0 12px 30px rgba(0,0,0,0.5), 0 0 20px rgba(200, 150, 88, 0.15);
    }
    .vintage-concept-card:hover::before {
      opacity: 1;
    }
    .vintage-concept-card.active-card {
      border-color: #a82828;
      box-shadow: 0 0 25px rgba(168, 40, 40, 0.3);
    }
    .vintage-concept-card.active-card::before {
      background: linear-gradient(90deg, transparent, #a82828, transparent);
      opacity: 1;
    }

    /* Navigation Active Underline */
    .nav-tab-link {
      position: relative;
      transition: color 0.25s ease;
    }
    .nav-tab-link::after {
      content: '';
      position: absolute;
      bottom: -6px;
      left: 50%;
      transform: translateX(-50%) scaleX(0);
      width: 80%;
      height: 2.5px;
      background: #c89658;
      transition: transform 0.25s ease;
      border-radius: 2px;
    }
    .nav-tab-link.active-nav {
      color: #c89658;
      font-weight: 700;
    }
    .nav-tab-link.active-nav::after {
      transform: translateX(-50%) scaleX(1);
    }

    /* Subtle manuscript backdrop */
    .manuscript-pattern {
      background-image: radial-gradient(rgba(45, 51, 66, 0.4) 1px, transparent 1px);
      background-size: 24px 24px;
    }

    /* Red ambient glow */
    .revolutionary-glow {
      position: absolute;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, rgba(139, 30, 30, 0.25) 0%, rgba(18, 20, 23, 0) 70%);
      filter: blur(50px);
      pointer-events: none;
      z-index: 0;
    }

    /* Modal Backdrop Blur */
    .concept-modal {
      transition: opacity 0.3s ease, transform 0.3s ease;
    }

    /* Animations */
    @keyframes pulseGlow {
      0%, 100% { opacity: 0.25; transform: scale(1); }
      50% { opacity: 0.45; transform: scale(1.05); }
    }
    .animate-pulse-glow {
      animation: pulseGlow 6s infinite ease-in-out;
    }

    @keyframes subtleFloat {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }
    .animate-float {
      animation: subtleFloat 5s infinite ease-in-out;
    }

    /* Timeline styling */
    .timeline-line {
      background: linear-gradient(180deg, #c89658 0%, rgba(200, 150, 88, 0.2) 100%);
    }
  </style>
</head>
<body class="bg-[#121417] text-[#cbd5e1] font-cairo antialiased">

  <!-- Reading Progress Bar -->
  <div id="scrollProgressBar" class="fixed top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-[#c89658] via-[#a82828] to-[#c89658] z-50 origin-right" style="transform: scaleX(0);"></div>

  <!-- ========================================== -->
  <!-- 1. STICKY NAVBAR                           -->
  <!-- ========================================== -->
  <header id="mainHeader" class="sticky top-0 z-40 bg-[#121417]/95 backdrop-blur-md border-b border-[#2d3342] transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Right: Brand & Title -->
      <a href="#hero" class="flex items-center gap-3.5 group">
        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-[#8b1e1e] to-[#421010] border border-[#c89658]/40 flex items-center justify-center text-[#f0ece1] shadow-lg group-hover:border-[#c89658] transition-colors">
          <i class="fa-solid fa-feather-pointed text-[#c89658] text-lg"></i>
        </div>
        <div class="flex flex-col">
          <span class="text-base sm:text-lg font-bold text-[#f0ece1] tracking-wide font-cairo group-hover:text-[#c89658] transition-colors">
            كارل ماركس: تشريح التاريخ ورأس المال
          </span>
          <span class="text-xs text-[#8e9baa] hidden sm:block">
            الأرشيف الفكري والدراسة النقدية (1818 – 1883)
          </span>
        </div>
      </a>

      <!-- Center: Navigation Tabs (Desktop) -->
      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-sm font-medium">
        <a href="#hero" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2 active-nav" data-section="hero">الرئيسية</a>
        <a href="#biography" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="biography">سيرته ومساره</a>
        <a href="#works" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="works">مؤلفاته ونظرياته</a>
        <a href="#concepts" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="concepts">مفاهيم جوهرية</a>
        <a href="#timeline" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="timeline">الخط الزمني</a>
        <a href="#quotes" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="quotes">أقوال موثقة</a>
        <a href="#documentaries" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="documentaries">مكتبة الوثائقيات</a>
      </nav>

      <!-- Left: Utility Controls & Mobile Hamburger -->
      <div class="flex items-center gap-3">
        <!-- Language Switcher Pill -->
        <div class="flex items-center bg-[#1a1d24] border border-[#2d3342] rounded-full p-1 text-xs font-semibold">
          <span class="px-2.5 py-1 rounded-full bg-[#8b1e1e] text-[#f0ece1] shadow-sm cursor-default">AR</span>
          <button onclick="toggleLangNotice()" class="px-2.5 py-1 text-[#8e9baa] hover:text-[#f0ece1] transition-colors" title="النسخة الإنجليزية متوفرة عبر المراجع">EN</button>
        </div>

        <!-- Quick Search / Explore Button -->
        <a href="#concepts" class="hidden sm:inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] text-xs text-[#c89658] hover:text-[#dfb173] font-medium transition-all">
          <i class="fa-solid fa-compass"></i>
          <span>المفاهيم</span>
        </a>

        <!-- Mobile Menu Toggle Button -->
        <button id="mobileMenuBtn" aria-label="فتح القائمة" class="lg:hidden p-2.5 rounded-lg bg-[#1a1d24] text-[#cbd5e1] border border-[#2d3342] hover:text-[#c89658] focus:outline-none">
          <i class="fa-solid fa-bars text-lg"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Navigation -->
    <div id="mobileDrawer" class="hidden lg:hidden bg-[#161920] border-b border-[#2d3342] px-6 py-5 shadow-2xl transition-all">
      <nav class="flex flex-col gap-3.5 text-base">
        <a href="#hero" class="mobile-nav-link text-[#f0ece1] hover:text-[#c89658] py-2 border-b border-[#222731] flex items-center justify-between">
          <span>الرئيسية</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
        <a href="#biography" class="mobile-nav-link text-[#cbd5e1] hover:text-[#c89658] py-2 border-b border-[#222731] flex items-center justify-between">
          <span>السيرة والمسار الحياتي</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
        <a href="#works" class="mobile-nav-link text-[#cbd5e1] hover:text-[#c89658] py-2 border-b border-[#222731] flex items-center justify-between">
          <span>المؤلفات والنظريات</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
        <a href="#concepts" class="mobile-nav-link text-[#cbd5e1] hover:text-[#c89658] py-2 border-b border-[#222731] flex items-center justify-between">
          <span>مفاهيم جوهرية</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
        <a href="#timeline" class="mobile-nav-link text-[#cbd5e1] hover:text-[#c89658] py-2 border-b border-[#222731] flex items-center justify-between">
          <span>الخط الزمني</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
        <a href="#quotes" class="mobile-nav-link text-[#cbd5e1] hover:text-[#c89658] py-2 border-b border-[#222731] flex items-center justify-between">
          <span>أقوال موثقة</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
        <a href="#documentaries" class="mobile-nav-link text-[#cbd5e1] hover:text-[#c89658] py-2 flex items-center justify-between">
          <span>مكتبة الوثائقيات</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
        </a>
      </nav>
    </div>
  </header>

  <!-- Notice Banner (if EN clicked) -->
  <div id="langNotice" class="hidden bg-[#8b1e1e] text-[#f0ece1] text-xs py-2 px-4 text-center border-b border-[#a82828] relative">
    <span>هذا الموقع مُصمم بالعربية الفصحى مع المصطلحات الأصلية بالألمانية والإنجليزية لتوثيق فكر ماركس بدقة أكاديمية.</span>
    <button onclick="toggleLangNotice()" class="absolute left-4 top-2 text-[#f0ece1] hover:opacity-75">✕</button>
  </div>

  <main class="relative z-10">
