# -*- coding: utf-8 -*-
import os

def generate_site():
    from generate_full_website import (
        svg_gears_scales,
        svg_factory_coins,
        svg_alienation,
        svg_class_struggle
    )

    file_path = "/home/dhiaborgi/.gemini/antigravity/scratch/karl-marx-website/index.html"
    
    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>كارل ماركس: تشريح التاريخ ورأس المال | موسوعة توثيقية نقدية</title>
  <meta name="description" content="موقع أكاديمي توثيقي شامل عن الفيلسوف والاقتصادي كارل ماركس: سيرته، مؤلفاته، مفاهيمه المركزية، خطه الزمني، وأقواله الموثقة.">

  <!-- Google Fonts: Cairo, Tajawal, Amiri -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;500;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">

  <!-- FontAwesome 6 Free CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            marx: {{
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
              textBody: '#cbd5e1',
              textMuted: '#8e9baa'
            }}
          }},
          fontFamily: {{
            cairo: ['Cairo', 'sans-serif'],
            tajawal: ['Tajawal', 'sans-serif'],
            amiri: ['Amiri', 'serif']
          }}
        }}
      }}
    }}
  </script>

  <style>
    :root {{
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
    }}

    body {{
      background-color: var(--bg-primary);
      color: var(--text-body);
      font-family: 'Cairo', 'Tajawal', sans-serif;
      overflow-x: hidden;
      line-height: 1.8;
      scroll-behavior: smooth;
    }}

    ::selection {{
      background-color: #8b1e1e;
      color: #f0ece1;
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 9px;
    }}
    ::-webkit-scrollbar-track {{
      background: #121417;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #2d3342;
      border-radius: 4px;
      border: 2px solid #121417;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #c89658;
    }}

    /* Parchment Card Aesthetic */
    .parchment-box {{
      background-color: #efe8d8;
      background-image: 
        radial-gradient(#d6cbaf 15%, transparent 16%),
        radial-gradient(#d6cbaf 15%, transparent 16%);
      background-size: 60px 60px;
      background-position: 0 0, 30px 30px;
      color: #2a2217;
      border: 3px double #9e8156;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.45), inset 0 0 40px rgba(184, 155, 114, 0.35);
      position: relative;
    }}
    .parchment-box::before, .parchment-box::after {{
      content: '';
      position: absolute;
      width: 18px;
      height: 18px;
      border-style: solid;
      border-color: #8b1e1e;
      pointer-events: none;
    }}
    .parchment-box::before {{
      top: 6px;
      right: 6px;
      border-width: 2px 2px 0 0;
    }}
    .parchment-box::after {{
      bottom: 6px;
      left: 6px;
      border-width: 0 0 2px 2px;
    }}

    /* Vintage Concept Card Hover Effects */
    .vintage-concept-card {{
      background: linear-gradient(145deg, #1f242e 0%, #171a21 100%);
      border: 1px solid #2d3342;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }}
    .vintage-concept-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, #c89658, transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }}
    .vintage-concept-card:hover {{
      transform: translateY(-5px);
      border-color: #c89658;
      box-shadow: 0 14px 30px rgba(0,0,0,0.55), 0 0 20px rgba(200, 150, 88, 0.2);
    }}
    .vintage-concept-card:hover::before {{
      opacity: 1;
    }}
    .vintage-concept-card.active-card {{
      border-color: #a82828;
      box-shadow: 0 0 25px rgba(168, 40, 40, 0.35);
    }}
    .vintage-concept-card.active-card::before {{
      background: linear-gradient(90deg, transparent, #a82828, transparent);
      opacity: 1;
    }}

    /* Navigation Active Underline Indicator */
    .nav-tab-link {{
      position: relative;
      transition: color 0.25s ease;
    }}
    .nav-tab-link::after {{
      content: '';
      position: absolute;
      bottom: -4px;
      left: 50%;
      transform: translateX(-50%) scaleX(0);
      width: 85%;
      height: 2.5px;
      background: #c89658;
      transition: transform 0.25s ease;
      border-radius: 2px;
    }}
    .nav-tab-link.active-nav {{
      color: #c89658;
      font-weight: 700;
    }}
    .nav-tab-link.active-nav::after {{
      transform: translateX(-50%) scaleX(1);
    }}

    /* Background Manuscript Pattern */
    .bg-manuscript-grid {{
      background-image: radial-gradient(rgba(45, 51, 66, 0.45) 1px, transparent 1px);
      background-size: 24px 24px;
    }}

    /* Glow Elements */
    .radial-red-glow {{
      background: radial-gradient(circle, rgba(168, 40, 40, 0.28) 0%, rgba(18, 20, 23, 0) 70%);
    }}
    .radial-gold-glow {{
      background: radial-gradient(circle, rgba(200, 150, 88, 0.18) 0%, rgba(18, 20, 23, 0) 70%);
    }}

    /* Book Card 3D Tilt Effect */
    .book-card {{
      transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }}
    .book-card:hover {{
      transform: translateY(-6px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6), 0 0 20px rgba(139, 30, 30, 0.2);
      border-color: #c89658;
    }}

    /* Timeline Line Glow */
    .timeline-path {{
      background: linear-gradient(180deg, #c89658 0%, #a82828 50%, #c89658 100%);
    }}
    .timeline-dot {{
      transition: all 0.3s ease;
    }}
    .timeline-item:hover .timeline-dot {{
      transform: scale(1.3);
      box-shadow: 0 0 16px #c89658;
    }}

    /* Modal Animation */
    .modal-backdrop {{
      background-color: rgba(10, 12, 15, 0.85);
      backdrop-filter: blur(8px);
    }}

    /* Toast Notification */
    #copyToast {{
      transition: opacity 0.3s ease, transform 0.3s ease;
    }}
  </style>
</head>
<body class="bg-[#121417] text-[#cbd5e1] font-cairo antialiased selection:bg-[#8b1e1e] selection:text-[#f0ece1]">

  <!-- Top Reading Progress Indicator -->
  <div id="scrollProgressBar" class="fixed top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-[#c89658] via-[#a82828] to-[#c89658] z-50 origin-right" style="transform: scaleX(0);"></div>

  <!-- ========================================== -->
  <!-- 1. STICKY NAVBAR                           -->
  <!-- ========================================== -->
  <header id="mainHeader" class="sticky top-0 z-40 bg-[#121417]/95 backdrop-blur-md border-b border-[#2d3342] transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Right: Brand Title -->
      <a href="#hero" class="flex items-center gap-3.5 group">
        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-[#8b1e1e] to-[#3a0d0d] border border-[#c89658]/40 flex items-center justify-center text-[#f0ece1] shadow-lg group-hover:border-[#c89658] transition-colors">
          <i class="fa-solid fa-feather-pointed text-[#c89658] text-lg"></i>
        </div>
        <div class="flex flex-col">
          <span class="text-base sm:text-lg font-bold text-[#f0ece1] tracking-wide group-hover:text-[#c89658] transition-colors">
            كارل ماركس: تشريح التاريخ ورأس المال
          </span>
          <span class="text-xs text-[#8e9baa] hidden md:block">
            دراسة توثيقية ونقدية (1818 – 1883)
          </span>
        </div>
      </a>

      <!-- Center: Navigation Tabs (Desktop) -->
      <nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-sm font-medium">
        <a href="#hero" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2 active-nav" data-section="hero">الرئيسية</a>
        <a href="#biography" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="biography">السيرة والمسار</a>
        <a href="#works" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="works">المؤلفات والنظريات</a>
        <a href="#concepts" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="concepts">مفاهيم مركزية</a>
        <a href="#timeline" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="timeline">الخط الزمني</a>
        <a href="#quotes" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="quotes">أقوال موثقة</a>
        <a href="#documentaries" class="nav-tab-link text-[#cbd5e1] hover:text-[#c89658] py-2" data-section="documentaries">مكتبة الوثائقيات</a>
      </nav>

      <!-- Left: Utility Controls & Mobile Menu Toggle -->
      <div class="flex items-center gap-3">
        <!-- Language Switcher Pill -->
        <div class="flex items-center bg-[#1a1d24] border border-[#2d3342] rounded-full p-1 text-xs font-semibold">
          <span class="px-2.5 py-1 rounded-full bg-[#8b1e1e] text-[#f0ece1] shadow-sm cursor-default">AR</span>
          <button onclick="toggleLangNotice()" class="px-2.5 py-1 text-[#8e9baa] hover:text-[#f0ece1] transition-colors" title="النسخة الإنجليزية">EN</button>
        </div>

        <!-- Quick Jump to Concept Button -->
        <a href="#concepts" class="hidden sm:inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] text-xs text-[#c89658] hover:text-[#dfb173] font-medium transition-all">
          <i class="fa-solid fa-shapes"></i>
          <span>المفاهيم</span>
        </a>

        <!-- Mobile Menu Toggle Button -->
        <button id="mobileMenuBtn" aria-label="فتح القائمة الرئيسية" class="lg:hidden p-2.5 rounded-lg bg-[#1a1d24] text-[#cbd5e1] border border-[#2d3342] hover:text-[#c89658] focus:outline-none transition-colors">
          <i class="fa-solid fa-bars text-lg"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Navigation Drawer -->
    <div id="mobileDrawer" class="hidden lg:hidden bg-[#161920] border-b border-[#2d3342] px-6 py-5 shadow-2xl transition-all">
      <nav class="flex flex-col gap-3 text-base">
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
          <span>مفاهيم مركزية</span> <i class="fa-solid fa-angle-left text-xs opacity-50"></i>
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

  <!-- Multilingual Info Notice Banner -->
  <div id="langNotice" class="hidden bg-[#8b1e1e] text-[#f0ece1] text-xs py-2 px-4 text-center border-b border-[#a82828] relative">
    <span>هذا الموقع مُصمم باللغة العربية الفصحى مع المصطلحات الفلسفية الأصلية بالألمانية والإنجليزية لتوثيق فكر ماركس بدقة أكاديمية.</span>
    <button onclick="toggleLangNotice()" class="absolute left-4 top-2 text-[#f0ece1] hover:opacity-75 font-bold">✕</button>
  </div>

  <main class="relative z-10 bg-manuscript-grid">

    <!-- ========================================== -->
    <!-- SECTION A: HERO & OVERVIEW                 -->
    <!-- ========================================== -->
    <section id="hero" class="relative pt-10 pb-16 lg:py-20 overflow-hidden border-b border-[#2d3342]">
      <!-- Ambient Lighting -->
      <div class="radial-red-glow absolute -top-20 -right-20 w-[550px] h-[550px] rounded-full pointer-events-none filter blur-3xl opacity-60"></div>
      <div class="radial-gold-glow absolute bottom-0 left-0 w-[450px] h-[450px] rounded-full pointer-events-none filter blur-3xl opacity-35"></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Hero Main Grid: Left Portrait/Overview, Right Parchment Quote & Timeline preview -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
          
          <!-- Column 1: Karl Marx Portrait & Identity (7 Cols) -->
          <div class="lg:col-span-7 flex flex-col md:flex-row items-center gap-6 lg:gap-8">
            
            <!-- Marx Portrait with Engraving/Atmospheric Frame -->
            <div class="relative w-56 sm:w-64 md:w-72 flex-shrink-0 group">
              <!-- Revolutionary red flare backdrop -->
              <div class="absolute inset-0 bg-gradient-to-t from-[#8b1e1e]/60 via-[#a82828]/20 to-transparent rounded-2xl transform rotate-1 group-hover:rotate-0 transition-transform duration-500"></div>
              
              <!-- Silhouette & Etching Frame -->
              <div class="relative rounded-2xl overflow-hidden border-2 border-[#c89658]/40 shadow-2xl bg-[#1a1d24]">
                <!-- Etched Marx Portrait -->
                <div class="relative aspect-[3/4] w-full overflow-hidden bg-[#161920]">
                  <!-- SVG/Image Render -->
                  <img src="assets/hero-mockup.jpg" 
                       alt="بورتريه كارل ماركس (1818 - 1883)" 
                       onerror="this.onerror=null; this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Karl_Marx_001.jpg/800px-Karl_Marx_001.jpg';" 
                       class="w-full h-full object-cover object-top filter grayscale contrast-125 brightness-95 group-hover:scale-105 transition-transform duration-700">
                  <!-- Sepia / Revolutionary red vignette overlay -->
                  <div class="absolute inset-0 bg-gradient-to-t from-[#121417] via-transparent to-[#8b1e1e]/20 mix-blend-multiply pointer-events-none"></div>
                  <!-- Vintage grain line -->
                  <div class="absolute inset-0 border border-[#c89658]/30 rounded-2xl pointer-events-none"></div>
                </div>

                <!-- Portrait Bottom Badge -->
                <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-[#121417] via-[#121417]/90 to-transparent p-3 text-center">
                  <span class="text-xs text-[#c89658] font-bold tracking-wider">KARL HEINRICH MARX</span>
                </div>
              </div>

              <!-- Decorative Brass Corner Rivets -->
              <div class="absolute -top-2 -right-2 w-4 h-4 rounded-full bg-[#c89658] border-2 border-[#121417] shadow-sm"></div>
              <div class="absolute -bottom-2 -left-2 w-4 h-4 rounded-full bg-[#8b1e1e] border-2 border-[#121417] shadow-sm"></div>
            </div>

            <!-- Identity Text -->
            <div class="flex-1 text-center md:text-right">
              <!-- Period Badge -->
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#c89658]/50 text-xs text-[#c89658] font-bold mb-3 shadow-inner">
                <i class="fa-regular fa-calendar-check text-[#c89658]"></i>
                <span>1818 – 1883</span>
              </div>

              <!-- Title -->
              <h1 class="text-4xl sm:text-5xl xl:text-6xl font-black text-[#f0ece1] tracking-tight leading-tight mb-3">
                كارل ماركس (1818 – 1883)
              </h1>

              <!-- Subtitle -->
              <p class="text-lg sm:text-xl font-bold text-[#c89658] mb-4">
                فيلسوف واقتصادي وصحفي ثوري ألماني
              </p>

              <!-- Summary Paragraph -->
              <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed mb-6 text-justify sm:text-right">
                لم يكن مجرد باحث في برج عاجي، بل كرّس حياته لتشريح آليات النظام الرأسمالي وفهم القوانين الاقتصادية والاجتماعية التي تحرك حركة التاريخ البشري. شكلت كتاباته وتحليلاته النقدية أحد أكثر المشاريع الفكرية تأثيراً في القرنين التاسع عشر والعشرين، ولا تزال مفاهيمه تُناقش وتُختبر في علم الاجتماع والاقتصاد المعاصر حتى اليوم.
              </p>

              <!-- Action Links -->
              <div class="flex flex-wrap items-center justify-center md:justify-start gap-3.5">
                <a href="#biography" class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-lg bg-gradient-to-r from-[#8b1e1e] to-[#a82828] hover:from-[#a82828] hover:to-[#dc2626] text-[#f0ece1] font-bold text-sm shadow-lg shadow-[#8b1e1e]/30 transition-all transform hover:-translate-y-0.5">
                  <i class="fa-solid fa-book-open-reader"></i>
                  <span>ابدأ الرحلة الفكرية</span>
                </a>
                <a href="#works" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-[#222731] hover:bg-[#2d3342] border border-[#3f475a] text-[#f0ece1] hover:text-[#c89658] font-semibold text-sm transition-all">
                  <i class="fa-solid fa-scroll"></i>
                  <span>استكشف المؤلفات</span>
                </a>
              </div>
            </div>

          </div>

          <!-- Column 2: Featured Parchment Quote Card & Fast Timeline (5 Cols) -->
          <div class="lg:col-span-5 flex flex-col gap-6">
            
            <!-- Parchment Quote Box (Directly inspired by the screenshot) -->
            <div class="parchment-box rounded-xl p-6 sm:p-8 shadow-2xl">
              <!-- Quill watermark / icon -->
              <div class="flex justify-between items-center mb-3 border-b border-[#9e8156]/40 pb-2">
                <span class="text-xs font-bold text-[#8b1e1e] tracking-wider uppercase font-sans">الأطروحة الحادية عشرة</span>
                <i class="fa-solid fa-quote-right text-[#8b1e1e] text-2xl opacity-80"></i>
              </div>

              <!-- Quote Content -->
              <blockquote class="font-amiri text-xl sm:text-2xl font-bold leading-relaxed text-[#2a2217] my-3 text-center">
                «إن الفلاسفة لم يفعلوا غير تفسير العالم بطرق مختلفة، ولكن المهم هو تغييره.» — أطروحات حول فيورباخ (1845)
              </blockquote>

              <!-- Citation Source -->
              <div class="text-center font-bold text-xs text-[#6b5a45] mt-3 pt-2 border-t border-[#9e8156]/30">
                — الأطروحة الحادية عشرة من أطروحات حول فيورباخ (1845)
              </div>

              <!-- Quick Buttons inside Parchment -->
              <div class="mt-6 flex flex-col sm:flex-row gap-2.5">
                <a href="#biography" class="flex-1 text-center py-2.5 px-4 rounded bg-[#8b1e1e] hover:bg-[#a82828] text-[#f0ece1] font-bold text-sm shadow-md transition-colors">
                  ابدأ الرحلة
                </a>
                <a href="#biography" class="flex-1 text-center py-2.5 px-4 rounded border border-[#9e8156] hover:bg-[#dfb173]/30 text-[#2a2217] font-bold text-sm transition-colors">
                  قراءة السيرة
                </a>
              </div>
            </div>

            <!-- Mini Interactive Timeline Quick-Bar (Inspired by right side of mockup) -->
            <div class="bg-[#1a1d24]/90 rounded-xl p-4 border border-[#2d3342] shadow-xl">
              <div class="flex items-center justify-between mb-3 text-xs font-bold text-[#c89658] border-b border-[#2d3342] pb-2">
                <span><i class="fa-solid fa-timeline ml-1.5"></i> الخط الزمني السريع</span>
                <a href="#timeline" class="text-[#8e9baa] hover:text-[#f0ece1] transition-colors">عرض الكل ←</a>
              </div>
              <div class="grid grid-cols-5 gap-2 text-center">
                <a href="#timeline-1818" class="p-2 rounded bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] hover:border-[#c89658] transition-all">
                  <div class="text-xs font-black text-[#c89658]">1818</div>
                  <div class="text-[10px] text-[#8e9baa] truncate">الولادة</div>
                </a>
                <a href="#timeline-1844" class="p-2 rounded bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] hover:border-[#c89658] transition-all">
                  <div class="text-xs font-black text-[#c89658]">1844</div>
                  <div class="text-[10px] text-[#8e9baa] truncate">إنجلز</div>
                </a>
                <a href="#timeline-1848" class="p-2 rounded bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] hover:border-[#a82828] transition-all">
                  <div class="text-xs font-black text-[#a82828]">1848</div>
                  <div class="text-[10px] text-[#8e9baa] truncate">البيان</div>
                </a>
                <a href="#timeline-1867" class="p-2 rounded bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] hover:border-[#c89658] transition-all">
                  <div class="text-xs font-black text-[#c89658]">1867</div>
                  <div class="text-[10px] text-[#8e9baa] truncate">رأس المال</div>
                </a>
                <a href="#timeline-1883" class="p-2 rounded bg-[#222731] hover:bg-[#2d3342] border border-[#2d3342] hover:border-[#c89658] transition-all">
                  <div class="text-xs font-black text-[#c89658]">1883</div>
                  <div class="text-[10px] text-[#8e9baa] truncate">الرحيل</div>
                </a>
              </div>
            </div>

          </div>

        </div>

        <!-- ========================================== -->
        <!-- QUICK CONCEPT CARDS ROW (Exact to Mockup)  -->
        <!-- ========================================== -->
        <div class="mt-14 pt-10 border-t border-[#2d3342]/70">
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-3">
              <span class="w-3 h-3 rounded-full bg-[#8b1e1e] animate-pulse"></span>
              <h2 class="text-xl sm:text-2xl font-bold text-[#f0ece1]">مفاهيم مركزية</h2>
            </div>
            <span class="text-xs text-[#8e9baa]">اضغط على أي بطاقة لاستعراض الشرح والنموذج الفكري</span>
          </div>

          <!-- 4 Vintage Concept Cards Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            
            <!-- Card 1: المادية التاريخية -->
            <div onclick="openConceptModal('historical-materialism')" class="vintage-concept-card rounded-xl p-4 flex flex-col group">
              <div class="h-44 w-full rounded-lg overflow-hidden bg-[#181c24] mb-3 flex items-center justify-center p-2 border border-[#2d3342]/60 group-hover:border-[#c89658]/60 transition-colors">
                {svg_gears_scales}
              </div>
              <div class="text-center py-1">
                <h3 class="text-base font-bold text-[#f0ece1] group-hover:text-[#c89658] transition-colors">المادية التاريخية</h3>
                <span class="text-[11px] text-[#8e9baa] font-mono">Historical Materialism</span>
              </div>
            </div>

            <!-- Card 2: فائض القيمة -->
            <div onclick="openConceptModal('surplus-value')" class="vintage-concept-card rounded-xl p-4 flex flex-col group">
              <div class="h-44 w-full rounded-lg overflow-hidden bg-[#181c24] mb-3 flex items-center justify-center p-2 border border-[#2d3342]/60 group-hover:border-[#c89658]/60 transition-colors">
                {svg_factory_coins}
              </div>
              <div class="text-center py-1">
                <h3 class="text-base font-bold text-[#f0ece1] group-hover:text-[#c89658] transition-colors">فائض القيمة</h3>
                <span class="text-[11px] text-[#8e9baa] font-mono">Surplus Value / Mehrwert</span>
              </div>
            </div>

            <!-- Card 3: الاغتراب -->
            <div onclick="openConceptModal('alienation')" class="vintage-concept-card rounded-xl p-4 flex flex-col group">
              <div class="h-44 w-full rounded-lg overflow-hidden bg-[#181c24] mb-3 flex items-center justify-center p-2 border border-[#2d3342]/60 group-hover:border-[#c89658]/60 transition-colors">
                {svg_alienation}
              </div>
              <div class="text-center py-1">
                <h3 class="text-base font-bold text-[#f0ece1] group-hover:text-[#c89658] transition-colors">الاغتراب</h3>
                <span class="text-[11px] text-[#8e9baa] font-mono">Alienation / Entfremdung</span>
              </div>
            </div>

            <!-- Card 4: صراع الطبقات -->
            <div onclick="openConceptModal('class-struggle')" class="vintage-concept-card rounded-xl p-4 flex flex-col group">
              <div class="h-44 w-full rounded-lg overflow-hidden bg-[#181c24] mb-3 flex items-center justify-center p-2 border border-[#2d3342]/60 group-hover:border-[#c89658]/60 transition-colors">
                {svg_class_struggle}
              </div>
              <div class="text-center py-1">
                <h3 class="text-base font-bold text-[#f0ece1] group-hover:text-[#c89658] transition-colors">صراع الطبقات</h3>
                <span class="text-[11px] text-[#8e9baa] font-mono">Class Struggle / Klassenkampf</span>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION B: BIOGRAPHY & LIFE TRAJECTORY     -->
    <!-- ========================================== -->
    <section id="biography" class="py-16 lg:py-24 border-b border-[#2d3342] bg-[#161920]/60">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Section Header -->
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#8b1e1e] text-xs text-[#c89658] font-bold mb-3">
            <i class="fa-solid fa-scroll text-[#8b1e1e]"></i>
            <span>المسار التاريخي والإنساني</span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-[#f0ece1] tracking-tight mb-4">
            السيرة والمسار الحياتي
          </h2>
          <p class="text-sm sm:text-base text-[#8e9baa]">
            محطات حافلة بين المنافي الأوروبية، الكفاح الفكري، والملاحقة السياسية في سبيل تفكيك قوانين حركة المجتمع البشري.
          </p>
        </div>

        <!-- 4 Detailed Biography Cards (2x2 Grid) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8">
          
          <!-- Bio Card 1 -->
          <div class="bg-[#222731] border border-[#2d3342] hover:border-[#c89658]/60 rounded-xl p-6 sm:p-8 relative overflow-hidden transition-all duration-300 shadow-xl group">
            <div class="absolute top-0 right-0 w-2 h-full bg-gradient-to-b from-[#c89658] to-transparent"></div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-md bg-[#1a1d24] border border-[#2d3342] text-xs font-bold text-[#c89658]">
                1818 – 1843
              </span>
              <div class="w-10 h-10 rounded-full bg-[#1a1d24] flex items-center justify-center text-[#c89658] border border-[#2d3342]">
                <i class="fa-solid fa-graduation-cap"></i>
              </div>
            </div>
            <h3 class="text-xl font-bold text-[#f0ece1] mb-3 group-hover:text-[#c89658] transition-colors">
              النشأة والبدايات الأكاديمية (ترير وبرلين)
            </h3>
            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify">
              وُلد في ترير البروسية لأسرة من الطبقة الوسطى. درس القانون في بون ثم الفلسفة والتاريخ في برلين. انضم لحلقة "الهيغليين الشبان" وتأثر بالجدل الهيغلي قبل نقده وتحويله من المثالية المجردة إلى الواقع المادي.
            </p>
            <div class="mt-5 pt-4 border-t border-[#2d3342] flex items-center gap-3 text-xs text-[#8e9baa]">
              <i class="fa-solid fa-landmark text-[#c89658]"></i>
              <span>جامعة برلين • حلقة الهيغليين الشبان • أطروحة دكتوراه يينا</span>
            </div>
          </div>

          <!-- Bio Card 2 -->
          <div class="bg-[#222731] border border-[#2d3342] hover:border-[#8b1e1e] rounded-xl p-6 sm:p-8 relative overflow-hidden transition-all duration-300 shadow-xl group">
            <div class="absolute top-0 right-0 w-2 h-full bg-gradient-to-b from-[#8b1e1e] to-transparent"></div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-md bg-[#1a1d24] border border-[#2d3342] text-xs font-bold text-[#a82828]">
                1844
              </span>
              <div class="w-10 h-10 rounded-full bg-[#1a1d24] flex items-center justify-center text-[#a82828] border border-[#2d3342]">
                <i class="fa-solid fa-handshake"></i>
              </div>
            </div>
            <h3 class="text-xl font-bold text-[#f0ece1] mb-3 group-hover:text-[#a82828] transition-colors">
              شراكة العمر مع فريدريك إنجلز (باريس 1844)
            </h3>
            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify">
              بعد مصادرة صحيفته السياسية، غادر لباريس والتقى برفيق دربه إنجلز؛ لتنشأ أعمق شراكة فكرية وإنسانية في التاريخ الحديث حيث دعمه إنجلز فكرياً ونقدياً ومادياً لمواصلة أبحاثه.
            </p>
            <div class="mt-5 pt-4 border-t border-[#2d3342] flex items-center gap-3 text-xs text-[#8e9baa]">
              <i class="fa-solid fa-pen-nib text-[#a82828]"></i>
              <span>مقهى دي لا ريجانس • صحيفة الحوليات الألمانية الفرنسية • رفاق السلاح</span>
            </div>
          </div>

          <!-- Bio Card 3 -->
          <div class="bg-[#222731] border border-[#2d3342] hover:border-[#c89658]/60 rounded-xl p-6 sm:p-8 relative overflow-hidden transition-all duration-300 shadow-xl group">
            <div class="absolute top-0 right-0 w-2 h-full bg-gradient-to-b from-[#c89658] to-transparent"></div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-md bg-[#1a1d24] border border-[#2d3342] text-xs font-bold text-[#c89658]">
                1849 – الستينيات
              </span>
              <div class="w-10 h-10 rounded-full bg-[#1a1d24] flex items-center justify-center text-[#c89658] border border-[#2d3342]">
                <i class="fa-solid fa-house-chimney-crack"></i>
              </div>
            </div>
            <h3 class="text-xl font-bold text-[#f0ece1] mb-3 group-hover:text-[#c89658] transition-colors">
              سنوات المنفى وشظف العيش (لندن)
            </h3>
            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify">
              طُرد من فرنسا وبلجيكا وبروسيا، فاستقر لاجئاً مجرداً من الجنسية في لندن عام 1849. عاشت عائلته في فقر مدقع بحي سوهو، وفقد أطفالاً بسبب المرض وشح الموارد، بينما كان يقضي نهاره في غرفة القراءة بالمتحف البريطاني يدوّن أبحاثه الاقتصادية.
            </p>
            <div class="mt-5 pt-4 border-t border-[#2d3342] flex items-center gap-3 text-xs text-[#8e9baa]">
              <i class="fa-solid fa-book text-[#c89658]"></i>
              <span>حي سوهو بلندن • قاعة القراءة بالمتحف البريطاني • التضحية العائلية</span>
            </div>
          </div>

          <!-- Bio Card 4 -->
          <div class="bg-[#222731] border border-[#2d3342] hover:border-[#8b1e1e] rounded-xl p-6 sm:p-8 relative overflow-hidden transition-all duration-300 shadow-xl group">
            <div class="absolute top-0 right-0 w-2 h-full bg-gradient-to-b from-[#8b1e1e] to-transparent"></div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-md bg-[#1a1d24] border border-[#2d3342] text-xs font-bold text-[#a82828]">
                1864 – 1883
              </span>
              <div class="w-10 h-10 rounded-full bg-[#1a1d24] flex items-center justify-center text-[#a82828] border border-[#2d3342]">
                <i class="fa-solid fa-bullhorn"></i>
              </div>
            </div>
            <h3 class="text-xl font-bold text-[#f0ece1] mb-3 group-hover:text-[#a82828] transition-colors">
              النشاط العمالي والرحيل
            </h3>
            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify">
              ساهم في تأسيس "جمعية الشغيلة العالمية" (الأممية الأولى) عام 1864. توفي بمركبته في 14 مارس 1883 ودُفن في مقبرة هايغيت بلندن بحضور قلة من رفاقه، قبل أن ينتشر أثره في كل قارات الأرض.
            </p>
            <div class="mt-5 pt-4 border-t border-[#2d3342] flex items-center gap-3 text-xs text-[#8e9baa]">
              <i class="fa-solid fa-monument text-[#a82828]"></i>
              <span>الأممية الأولى • مقبرة هايغيت • «يا عمال العالم اتحدوا»</span>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION C: MAJOR WORKS                     -->
    <!-- ========================================== -->
    <section id="works" class="py-16 lg:py-24 border-b border-[#2d3342]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Header -->
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#c89658] text-xs text-[#c89658] font-bold mb-3">
            <i class="fa-solid fa-book-bookmark text-[#c89658]"></i>
            <span>الإنتاج النظري والتحليلي</span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-[#f0ece1] tracking-tight mb-4">
            أهم المؤلفات والنظريات
          </h2>
          <p class="text-sm sm:text-base text-[#8e9baa]">
            ثلاثية تأسيسية أعادت صياغة فلسفة التاريخ، وفككت بنية الإنتاج الرأسمالي المعاصر.
          </p>
        </div>

        <!-- 3 Major Works Structured Cards -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-7">
          
          <!-- Book 1: البيان الشيوعي -->
          <div class="book-card bg-[#222731] border border-[#2d3342] rounded-xl overflow-hidden flex flex-col justify-between shadow-xl">
            <div>
              <!-- Header Banner -->
              <div class="h-32 bg-gradient-to-r from-[#4a1010] to-[#8b1e1e] p-6 flex flex-col justify-between relative">
                <span class="text-xs font-mono text-[#fae3a2] tracking-wider uppercase">Manifest der Kommunistischen Partei</span>
                <div class="flex items-center justify-between">
                  <span class="px-2.5 py-1 rounded bg-[#121417]/80 text-[#f0ece1] text-xs font-bold border border-[#c89658]/40">عام 1848</span>
                  <i class="fa-solid fa-fire text-2xl text-[#f0ece1]/70"></i>
                </div>
              </div>

              <!-- Body -->
              <div class="p-6">
                <h3 class="text-2xl font-bold text-[#f0ece1] mb-2 font-cairo">البيان الشيوعي (1848)</h3>
                <div class="text-xs text-[#c89658] font-semibold mb-4">كارل ماركس وفريدريك إنجلز • لندن</div>

                <p class="text-sm text-[#cbd5e1] leading-relaxed text-justify mb-5">
                  صاغه ماركس وإنجلز عشية ثورات أوروبا؛ ليرسم ملامح الصراع الطبقي بين البرجوازية والبروليتاريا بعبارته: «إن تاريخ كل مجتمع إلى يومنا هذا لم يكن سوى تاريخ صراع الطبقات».
                </p>

                <div class="bg-[#1a1d24] p-3.5 rounded-lg border border-[#2d3342] text-xs text-[#8e9baa] mb-4">
                  <strong class="text-[#f0ece1] block mb-1"><i class="fa-solid fa-key text-[#c89658] ml-1"></i> الأطروحة الجوهرية:</strong>
                  انقسام المجتمع الحديث إلى معسكرين متعاديين، وحتمية تجاوز النظام البرجوازي عبر وعي الطبقة العاملة المنظم.
                </div>
              </div>
            </div>

            <!-- Footer Action -->
            <div class="px-6 pb-6 pt-2 border-t border-[#2d3342]/60">
              <button onclick="toggleWorkDetail('work1')" class="w-full py-2.5 px-4 rounded-lg bg-[#1a1d24] hover:bg-[#2d3342] border border-[#3f475a] text-[#c89658] hover:text-[#dfb173] text-xs font-bold transition-colors flex items-center justify-center gap-2">
                <span>استكشف تفاصيل الأثر التاريخي</span>
                <i class="fa-solid fa-chevron-down text-[10px]"></i>
              </button>
              <div id="work1-detail" class="hidden mt-3 text-xs text-[#cbd5e1] bg-[#121417] p-3 rounded border border-[#2d3342] leading-relaxed">
                تُرجم إلى أكثر من 100 لغة واعتُبر أكثر الوثائق السياسية قراءة وتأثيراً في التاريخ، ونُشر في خضم "ربيع الشعوب" 1848.
              </div>
            </div>
          </div>

          <!-- Book 2: رأس المال -->
          <div class="book-card bg-[#222731] border border-[#2d3342] rounded-xl overflow-hidden flex flex-col justify-between shadow-xl">
            <div>
              <!-- Header Banner -->
              <div class="h-32 bg-gradient-to-r from-[#2c1d0e] to-[#7a4e1b] p-6 flex flex-col justify-between relative">
                <span class="text-xs font-mono text-[#fae3a2] tracking-wider uppercase">Das Kapital: Kritik der politischen Ökonomie</span>
                <div class="flex items-center justify-between">
                  <span class="px-2.5 py-1 rounded bg-[#121417]/80 text-[#f0ece1] text-xs font-bold border border-[#c89658]/40">المجلد الأول 1867</span>
                  <i class="fa-solid fa-scale-balanced text-2xl text-[#f0ece1]/70"></i>
                </div>
              </div>

              <!-- Body -->
              <div class="p-6">
                <h3 class="text-2xl font-bold text-[#f0ece1] mb-2 font-cairo">رأس المال: نقد الاقتصاد السياسي (المجلد الأول 1867)</h3>
                <div class="text-xs text-[#c89658] font-semibold mb-4">المجلد الأول 1867 (أكمله إنجلز لاحقاً) • هامبورغ</div>

                <p class="text-sm text-[#cbd5e1] leading-relaxed text-justify mb-5">
                  دراسته الاقتصادية الأضخم التي فككت بدقة مفهوم السلعة، القيمة التبادلية، وأصل استخلاص الربح من قوة العمل (تولى إنجلز نشر المجلدين الثاني والثالث بعد رحيله).
                </p>

                <div class="bg-[#1a1d24] p-3.5 rounded-lg border border-[#2d3342] text-xs text-[#8e9baa] mb-4">
                  <strong class="text-[#f0ece1] block mb-1"><i class="fa-solid fa-key text-[#c89658] ml-1"></i> الأطروحة الجوهرية:</strong>
                  رأس المال ليس شيئاً مادياً مجرداً بل علاقة اجتماعية قائمة على امتصاص وقت العمل غير مدفوع الأجر وتحويله إلى تراكم دائم.
                </div>
              </div>
            </div>

            <!-- Footer Action -->
            <div class="px-6 pb-6 pt-2 border-t border-[#2d3342]/60">
              <button onclick="toggleWorkDetail('work2')" class="w-full py-2.5 px-4 rounded-lg bg-[#1a1d24] hover:bg-[#2d3342] border border-[#3f475a] text-[#c89658] hover:text-[#dfb173] text-xs font-bold transition-colors flex items-center justify-center gap-2">
                <span>استكشف تفاصيل الأثر التاريخي</span>
                <i class="fa-solid fa-chevron-down text-[10px]"></i>
              </button>
              <div id="work2-detail" class="hidden mt-3 text-xs text-[#cbd5e1] bg-[#121417] p-3 rounded border border-[#2d3342] leading-relaxed">
                قضى ماركس أكثر من عقدين في مكتبة المتحف البريطاني يحلل التقارير الإحصائية للمصانع الإنجليزية ليؤسس نظرية القيمة النقدية الدقيقة.
              </div>
            </div>
          </div>

          <!-- Book 3: الأيديولوجيا الألمانية -->
          <div class="book-card bg-[#222731] border border-[#2d3342] rounded-xl overflow-hidden flex flex-col justify-between shadow-xl">
            <div>
              <!-- Header Banner -->
              <div class="h-32 bg-gradient-to-r from-[#172338] to-[#1e3a5f] p-6 flex flex-col justify-between relative">
                <span class="text-xs font-mono text-[#fae3a2] tracking-wider uppercase">Die deutsche Ideologie</span>
                <div class="flex items-center justify-between">
                  <span class="px-2.5 py-1 rounded bg-[#121417]/80 text-[#f0ece1] text-xs font-bold border border-[#c89658]/40">1845 – 1846</span>
                  <i class="fa-solid fa-brain text-2xl text-[#f0ece1]/70"></i>
                </div>
              </div>

              <!-- Body -->
              <div class="p-6">
                <h3 class="text-2xl font-bold text-[#f0ece1] mb-2 font-cairo">الأيديولوجيا الألمانية (1845 - 1846)</h3>
                <div class="text-xs text-[#c89658] font-semibold mb-4">ماركس وإنجلز • بروكسل</div>

                <p class="text-sm text-[#cbd5e1] leading-relaxed text-justify mb-5">
                  العمل التأسيسي الذي أعلن قطيعته مع المثالية الفلسفية ووضع اللبنات الأولى للمادية التاريخية.
                </p>

                <div class="bg-[#1a1d24] p-3.5 rounded-lg border border-[#2d3342] text-xs text-[#8e9baa] mb-4">
                  <strong class="text-[#f0ece1] block mb-1"><i class="fa-solid fa-key text-[#c89658] ml-1"></i> الأطروحة الجوهرية:</strong>
                  ليست الأفكار هي التي تصنع الواقع وتحدد التاريخ، بل الشروط المادية وعلاقات الإنتاج الواقعية هي التي تولد الأفكار والأيديولوجيا.
                </div>
              </div>
            </div>

            <!-- Footer Action -->
            <div class="px-6 pb-6 pt-2 border-t border-[#2d3342]/60">
              <button onclick="toggleWorkDetail('work3')" class="w-full py-2.5 px-4 rounded-lg bg-[#1a1d24] hover:bg-[#2d3342] border border-[#3f475a] text-[#c89658] hover:text-[#dfb173] text-xs font-bold transition-colors flex items-center justify-center gap-2">
                <span>استكشف تفاصيل الأثر التاريخي</span>
                <i class="fa-solid fa-chevron-down text-[10px]"></i>
              </button>
              <div id="work3-detail" class="hidden mt-3 text-xs text-[#cbd5e1] bg-[#121417] p-3 rounded border border-[#2d3342] leading-relaxed">
                لم يُنشر العمل كاملاً في حياة المؤلفين، وتركه ماركس «لنقد الفئران القارض» بعدما حقق هدفه الأساسي بتصفية الحساب مع ضميرهما الفلسفي السابق.
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION D: CORE CONCEPTS (INTERACTIVE)     -->
    <!-- ========================================== -->
    <section id="concepts" class="py-16 lg:py-24 border-b border-[#2d3342] bg-[#161920]/70">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Header -->
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#8b1e1e] text-xs text-[#c89658] font-bold mb-3">
            <i class="fa-solid fa-atom text-[#8b1e1e]"></i>
            <span>المنظومة المفاهيمية</span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-[#f0ece1] tracking-tight mb-4">
            مفاهيم مركزية
          </h2>
          <p class="text-sm sm:text-base text-[#8e9baa]">
            المفاتيح النظرية الأربعة التي شيد عليها ماركس مشروعه لتفكيك الاقتصاد السياسي وحركة المجتمعات.
          </p>
        </div>

        <!-- 4 Core Concepts Accordion & Cards -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          <!-- Concept 1: المادية التاريخية -->
          <div class="bg-[#222731] border border-[#2d3342] rounded-xl p-6 sm:p-8 hover:border-[#c89658] transition-all shadow-xl">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-12 h-12 rounded-lg bg-[#1a1d24] border border-[#c89658]/40 flex items-center justify-center text-[#c89658] flex-shrink-0 text-xl">
                <i class="fa-solid fa-gears"></i>
              </div>
              <div>
                <span class="text-xs text-[#c89658] font-mono font-bold">Concept 01</span>
                <h3 class="text-xl sm:text-2xl font-bold text-[#f0ece1]">المادية التاريخية (Historical Materialism)</h3>
              </div>
            </div>

            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify mb-6">
              رؤية ترى أن حركة التاريخ تقودها شروط الإنتاج المادي لا الأفكار المجردة؛ فالبنية التحتية (علاقات وقوى الإنتاج) هي التي تحدد البنية الفوقية (القوانين، والسياسة، والدين، والفكر).
            </p>

            <!-- Visual Model: Base vs Superstructure -->
            <div class="bg-[#181c24] border border-[#2d3342] rounded-lg p-4 mb-4">
              <div class="text-xs font-bold text-[#c89658] mb-2 flex items-center gap-2">
                <i class="fa-solid fa-diagram-project"></i>
                <span>النموذج التحليلي: البنية الفوقية مقابل البنية التحتية</span>
              </div>
              <div class="space-y-2">
                <!-- Superstructure -->
                <div class="p-2.5 rounded bg-[#2a3140] border border-[#3f475a] text-center">
                  <div class="text-xs font-bold text-[#f0ece1]">البنية الفوقية (Superstructure)</div>
                  <div class="text-[11px] text-[#cbd5e1]">القوانين • الدولة • الدين • الفلسفة • الثقافة والوعي</div>
                </div>
                <!-- Determinant Arrow -->
                <div class="text-center text-[#c89658] text-xs font-bold">
                  ▲ مشروطة ومحددة ماديّاً بواسطة ▼
                </div>
                <!-- Base -->
                <div class="p-2.5 rounded bg-[#3b2323] border border-[#8b1e1e] text-center">
                  <div class="text-xs font-bold text-[#f0ece1]">البنية التحتية الاقتصادية (Economic Base)</div>
                  <div class="text-[11px] text-[#e2dac6]">قوى الإنتاج (الآلات، الموارد) + علاقات الإنتاج (الملكية، الطبقات)</div>
                </div>
              </div>
            </div>

            <button onclick="openConceptModal('historical-materialism')" class="text-xs font-bold text-[#c89658] hover:text-[#dfb173] flex items-center gap-1.5 transition-colors">
              <span>عرض تفاصيل المفهوم في نافذة موسعة</span>
              <i class="fa-solid fa-arrow-left"></i>
            </button>
          </div>

          <!-- Concept 2: فائض القيمة -->
          <div class="bg-[#222731] border border-[#2d3342] rounded-xl p-6 sm:p-8 hover:border-[#8b1e1e] transition-all shadow-xl">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-12 h-12 rounded-lg bg-[#1a1d24] border border-[#8b1e1e]/60 flex items-center justify-center text-[#a82828] flex-shrink-0 text-xl">
                <i class="fa-solid fa-coins"></i>
              </div>
              <div>
                <span class="text-xs text-[#a82828] font-mono font-bold">Concept 02</span>
                <h3 class="text-xl sm:text-2xl font-bold text-[#f0ece1]">فائض القيمة (Surplus Value)</h3>
              </div>
            </div>

            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify mb-6">
              الفارق بين القيمة التي يخلقها العامل خلال ساعات عمله والأجر الفعلي الذي يتلقاه للبقاء حياً، وهو الفائض الذي يستحوذ عليه الرأسمالي ويمثل جوهر التراكم والربح.
            </p>

            <!-- Visual Model: Surplus Value Equation -->
            <div class="bg-[#181c24] border border-[#2d3342] rounded-lg p-4 mb-4">
              <div class="text-xs font-bold text-[#a82828] mb-2 flex items-center gap-2">
                <i class="fa-solid fa-calculator"></i>
                <span>مخطط ساعات يوم العمل (8 ساعات عمل مثلاً):</span>
              </div>
              <div class="grid grid-cols-12 gap-1 h-9 rounded overflow-hidden text-center text-[10px] font-bold">
                <!-- Necessary Labor Time -->
                <div class="col-span-4 bg-[#2b3a4a] text-[#93c5fd] flex items-center justify-center px-1">
                  عمل ضروري (أجر العامل: 3 ساعات)
                </div>
                <!-- Surplus Labor Time -->
                <div class="col-span-8 bg-[#8b1e1e] text-[#f0ece1] flex items-center justify-center px-1">
                  عمل فائض غير مدفوع (فائض القيمة للرأسمالي: 5 ساعات)
                </div>
              </div>
              <div class="mt-2 text-[11px] text-[#8e9baa] text-center">
                معدل الاستغلال = وقت العمل الفائض ÷ وقت العمل الضروري = 166%
              </div>
            </div>

            <button onclick="openConceptModal('surplus-value')" class="text-xs font-bold text-[#c89658] hover:text-[#dfb173] flex items-center gap-1.5 transition-colors">
              <span>عرض تفاصيل المفهوم في نافذة موسعة</span>
              <i class="fa-solid fa-arrow-left"></i>
            </button>
          </div>

          <!-- Concept 3: الاغتراب -->
          <div class="bg-[#222731] border border-[#2d3342] rounded-xl p-6 sm:p-8 hover:border-[#c89658] transition-all shadow-xl">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-12 h-12 rounded-lg bg-[#1a1d24] border border-[#c89658]/40 flex items-center justify-center text-[#c89658] flex-shrink-0 text-xl">
                <i class="fa-solid fa-user-lock"></i>
              </div>
              <div>
                <span class="text-xs text-[#c89658] font-mono font-bold">Concept 03</span>
                <h3 class="text-xl sm:text-2xl font-bold text-[#f0ece1]">الاغتراب (Alienation)</h3>
              </div>
            </div>

            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify mb-6">
              حالة انفصال العامل عن نتاج عمله وعن ذاته وتحوله إلى مجرد ترس في آلة بدلاً من أن يكون العمل فعلاً حراً يعبر عن الإنسانية.
            </p>

            <!-- 4 Dimensions of Alienation -->
            <div class="grid grid-cols-2 gap-2 text-xs mb-4">
              <div class="bg-[#181c24] p-2.5 rounded border border-[#2d3342]">
                <strong class="text-[#f0ece1] block">1. عن نتاج العمل:</strong>
                <span class="text-[#8e9baa] text-[11px]">السلعة المصنوعة تقف أمامه كقوة غريبة ومسيطرة.</span>
              </div>
              <div class="bg-[#181c24] p-2.5 rounded border border-[#2d3342]">
                <strong class="text-[#f0ece1] block">2. عن عملية الإنتاج:</strong>
                <span class="text-[#8e9baa] text-[11px]">العمل ليس إشباعاً لحاجة بل شقاء مفروض قهراً.</span>
              </div>
              <div class="bg-[#181c24] p-2.5 rounded border border-[#2d3342]">
                <strong class="text-[#f0ece1] block">3. عن جوهر الإنسانية:</strong>
                <span class="text-[#8e9baa] text-[11px]">تجريد الإنسان من نشاطه الإبداعي وتحويله لحيواني.</span>
              </div>
              <div class="bg-[#181c24] p-2.5 rounded border border-[#2d3342]">
                <strong class="text-[#f0ece1] block">4. عن رفاق العمل:</strong>
                <span class="text-[#8e9baa] text-[11px]">تحويل العلاقات الإنسانية لتنافس عدائي على البقاء.</span>
              </div>
            </div>

            <button onclick="openConceptModal('alienation')" class="text-xs font-bold text-[#c89658] hover:text-[#dfb173] flex items-center gap-1.5 transition-colors">
              <span>عرض تفاصيل المفهوم في نافذة موسعة</span>
              <i class="fa-solid fa-arrow-left"></i>
            </button>
          </div>

          <!-- Concept 4: صراع الطبقات -->
          <div class="bg-[#222731] border border-[#2d3342] rounded-xl p-6 sm:p-8 hover:border-[#8b1e1e] transition-all shadow-xl">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-12 h-12 rounded-lg bg-[#1a1d24] border border-[#8b1e1e]/60 flex items-center justify-center text-[#a82828] flex-shrink-0 text-xl">
                <i class="fa-solid fa-link-slash"></i>
              </div>
              <div>
                <span class="text-xs text-[#a82828] font-mono font-bold">Concept 04</span>
                <h3 class="text-xl sm:text-2xl font-bold text-[#f0ece1]">صراع الطبقات (Class Struggle)</h3>
              </div>
            </div>

            <p class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed text-justify mb-6">
              التناقض الجذري بين طبقة تملك وسائل الإنتاج وطبقة لا تملك إلا بيع قوة عملها، وهو التناقض الذي يمثل محرك التحولات التاريخية الكبرى.
            </p>

            <!-- Historical Progression Banner -->
            <div class="bg-[#181c24] border border-[#2d3342] rounded-lg p-3 text-xs mb-4 space-y-2">
              <div class="text-xs font-bold text-[#c89658]">المسار الجدلي للتشكيلات الاجتماعية:</div>
              <div class="flex items-center justify-between text-[11px] text-[#cbd5e1] flex-wrap gap-1">
                <span class="bg-[#222731] px-2 py-1 rounded">العبودية (سادة / عبيد)</span>
                <span>←</span>
                <span class="bg-[#222731] px-2 py-1 rounded">الإقطاع (نبلاء / فلاحون)</span>
                <span>←</span>
                <span class="bg-[#8b1e1e] text-[#f0ece1] px-2 py-1 rounded">الرأسمالية (برجوازية / بروليتاريا)</span>
              </div>
            </div>

            <button onclick="openConceptModal('class-struggle')" class="text-xs font-bold text-[#c89658] hover:text-[#dfb173] flex items-center gap-1.5 transition-colors">
              <span>عرض تفاصيل المفهوم في نافذة موسعة</span>
              <i class="fa-solid fa-arrow-left"></i>
            </button>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION E: TIMELINE (CHRONOLOGICAL)        -->
    <!-- ========================================== -->
    <section id="timeline" class="py-16 lg:py-24 border-b border-[#2d3342]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Header -->
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#c89658] text-xs text-[#c89658] font-bold mb-3">
            <i class="fa-solid fa-hourglass-half text-[#c89658]"></i>
            <span>التعاقب التاريخي التفاعلي</span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-[#f0ece1] tracking-tight mb-4">
            الخط الزمني (1818 – 1883)
          </h2>
          <p class="text-sm sm:text-base text-[#8e9baa]">
            أبرز المحطات المفصلية في مسيرة كارل ماركس من الميلاد في ترير إلى استقراره الأبدي في هايغيت.
          </p>
        </div>

        <!-- Vertical Timeline Container -->
        <div class="relative">
          
          <!-- Central Glowing Line -->
          <div class="absolute right-4 sm:right-1/2 top-4 bottom-4 w-1 bg-gradient-to-b from-[#c89658] via-[#a82828] to-[#c89658] transform sm:translate-x-1/2 rounded-full opacity-60"></div>

          <!-- Timeline Items List -->
          <div class="space-y-10 sm:space-y-12">
            
            <!-- 1818 -->
            <div id="timeline-1818" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <!-- Node Badge / Dot -->
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#c89658] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <!-- Content Card: Right side on desktop -->
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:pr-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#c89658] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#c89658] font-black text-sm font-mono border border-[#c89658]/40 mb-2">1818</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">الولادة في ترير</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1818: ولادته في مدينة ترير بألمانيا.
                  </p>
                </div>
              </div>
            </div>

            <!-- 1841 -->
            <div id="timeline-1841" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#c89658] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:mr-auto sm:pl-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#c89658] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#c89658] font-black text-sm font-mono border border-[#c89658]/40 mb-2">1841</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">الدكتوراه في الفلسفة</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1841: نيل الدكتوراه في الفلسفة من جامعة يينا.
                  </p>
                </div>
              </div>
            </div>

            <!-- 1844 -->
            <div id="timeline-1844" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#8b1e1e] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:pr-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#a82828] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#a82828] font-black text-sm font-mono border border-[#8b1e1e] mb-2">1844</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">اللقاء التاريخي مع إنجلز</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1844: اللقاء الأول بفريدريك إنجلز في باريس.
                  </p>
                </div>
              </div>
            </div>

            <!-- 1848 -->
            <div id="timeline-1848" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#a82828] transform sm:translate-x-1/2 z-20 timeline-dot shadow-lg shadow-[#8b1e1e]"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:mr-auto sm:pl-10 text-right">
                <div class="bg-[#222731] border border-[#8b1e1e] group-hover:border-[#dc2626] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#8b1e1e] text-[#f0ece1] font-black text-sm font-mono mb-2">1848</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">صدور «البيان الشيوعي»</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1848: نشر «البيان الشيوعي» متزامناً مع الثورات العمالية.
                  </p>
                </div>
              </div>
            </div>

            <!-- 1849 -->
            <div id="timeline-1849" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#c89658] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:pr-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#c89658] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#c89658] font-black text-sm font-mono border border-[#c89658]/40 mb-2">1849</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">المنفى اللندني</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1849: لجوؤه واستقراره النهائي في لندن.
                  </p>
                </div>
              </div>
            </div>

            <!-- 1864 -->
            <div id="timeline-1864" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#8b1e1e] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:mr-auto sm:pl-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#a82828] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#a82828] font-black text-sm font-mono border border-[#8b1e1e] mb-2">1864</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">الأممية الأولى</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1864: المساهمة في تأسيس جمعية الشغيلة العالمية (الأممية الأولى).
                  </p>
                </div>
              </div>
            </div>

            <!-- 1867 -->
            <div id="timeline-1867" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#c89658] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:pr-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#c89658] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#c89658] font-black text-sm font-mono border border-[#c89658]/40 mb-2">1867</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">المجلد الأول من «رأس المال»</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1867: نشر المجلد الأول من «رأس المال».
                  </p>
                </div>
              </div>
            </div>

            <!-- 1883 -->
            <div id="timeline-1883" class="timeline-item relative flex flex-col sm:flex-row items-start group">
              <div class="absolute right-2 sm:right-1/2 w-5 h-5 rounded-full bg-[#121417] border-4 border-[#c89658] transform sm:translate-x-1/2 z-20 timeline-dot"></div>
              
              <div class="mr-10 sm:mr-0 sm:w-1/2 sm:mr-auto sm:pl-10 text-right">
                <div class="bg-[#222731] border border-[#2d3342] group-hover:border-[#c89658] rounded-xl p-5 shadow-xl transition-all">
                  <span class="inline-block px-3 py-1 rounded-md bg-[#1a1d24] text-[#c89658] font-black text-sm font-mono border border-[#c89658]/40 mb-2">1883</span>
                  <h3 class="text-lg font-bold text-[#f0ece1] mb-1">الرحيل والخلود</h3>
                  <p class="text-sm text-[#cbd5e1]">
                    1883: وفاته في لندن ودفنه في مقبرة هايغيت.
                  </p>
                </div>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION F: DOCUMENTED QUOTES (INTERACTIVE) -->
    <!-- ========================================== -->
    <section id="quotes" class="py-16 lg:py-24 border-b border-[#2d3342] bg-[#161920]/60">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Header -->
        <div class="text-center max-w-3xl mx-auto mb-12">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#8b1e1e] text-xs text-[#c89658] font-bold mb-3">
            <i class="fa-solid fa-quote-left text-[#8b1e1e]"></i>
            <span>من نصوص المصادر الأصلية</span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-[#f0ece1] tracking-tight mb-4">
            أقوال موثقة
          </h2>
          <p class="text-sm sm:text-base text-[#8e9baa]">
            كلمات صاغت وعي أجيال وأحدثت هزات جذرية في الفكر الإنساني والسياسي.
          </p>
        </div>

        <!-- Interactive Parchment Quote Box -->
        <div class="parchment-box rounded-2xl p-8 sm:p-12 shadow-2xl relative">
          
          <!-- Top Status Bar -->
          <div class="flex items-center justify-between border-b border-[#9e8156]/40 pb-4 mb-6">
            <div class="flex items-center gap-2">
              <i class="fa-solid fa-feather-pointed text-[#8b1e1e]"></i>
              <span id="quoteSourceTag" class="text-xs font-bold text-[#8b1e1e] tracking-wider uppercase">مقدمة «مساهمة في نقد الاقتصاد السياسي» (1859)</span>
            </div>
            <div class="flex items-center gap-1.5" id="quotePillsContainer">
              <!-- Rendered via JS -->
            </div>
          </div>

          <!-- Dynamic Quote Text -->
          <div class="min-h-[160px] flex items-center justify-center py-4">
            <blockquote id="quoteTextDisplay" class="font-amiri text-2xl sm:text-3xl font-bold text-[#2a2217] leading-relaxed text-center transition-all duration-300 transform opacity-100 scale-100">
              «إن نمط إنتاج الحياة المادية يشترط سيرورة الحياة الاجتماعية والسياسية والروحية بوجه عام. ليس وعي الناس هو الذي يحدد وجودهم، بل وجودهم الاجتماعي هو الذي يحدد وعيهم.»
            </blockquote>
          </div>

          <!-- Controls Bar -->
          <div class="mt-8 pt-6 border-t border-[#9e8156]/40 flex flex-col sm:flex-row items-center justify-between gap-4">
            
            <!-- Left: Copy Quote -->
            <button onclick="copyCurrentQuote()" class="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-[#efe8d8] hover:bg-[#e2dac6] border border-[#9e8156] text-[#2a2217] text-xs font-bold transition-all shadow-sm">
              <i class="fa-regular fa-copy text-[#8b1e1e]"></i>
              <span>نسخ الاقتباس</span>
            </button>

            <!-- Center: Counter -->
            <div id="quoteCounter" class="text-xs font-bold text-[#6b5a45] font-mono">
              الاقتباس 1 من 4
            </div>

            <!-- Right: Next / Prev Navigation -->
            <div class="flex items-center gap-2">
              <button onclick="navigateQuote(-1)" aria-label="الاقتباس السابق" class="w-10 h-10 rounded-lg bg-[#8b1e1e] hover:bg-[#a82828] text-[#f0ece1] flex items-center justify-center transition-colors shadow-md">
                <i class="fa-solid fa-chevron-right text-sm"></i>
              </button>
              <button onclick="navigateQuote(1)" aria-label="اقتباس آخر" class="px-5 h-10 rounded-lg bg-[#8b1e1e] hover:bg-[#a82828] text-[#f0ece1] text-xs font-bold flex items-center gap-2 transition-colors shadow-md">
                <span>اقتباس آخر</span>
                <i class="fa-solid fa-chevron-left text-sm"></i>
              </button>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION G: DOCUMENTARY LIBRARY             -->
    <!-- ========================================== -->
    <section id="documentaries" class="py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Header -->
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1a1d24] border border-[#c89658] text-xs text-[#c89658] font-bold mb-3">
            <i class="fa-solid fa-film text-[#c89658]"></i>
            <span>الأرشيف المرئي والوثائقي</span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-[#f0ece1] tracking-tight mb-4">
            مكتبة المرئيات والوثائقيات
          </h2>
          <p class="text-sm sm:text-base text-[#8e9baa]">
            أعمال وثائقية وتحليلات مرئية تتناول بالتشريح حياة ماركس وتأثير نظرياته الاقتصادية المعاصرة.
          </p>
        </div>

        <!-- 2 Responsive Video Cards -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          <!-- Documentary 1: DW عربية -->
          <div class="bg-[#222731] border border-[#2d3342] hover:border-[#8b1e1e] rounded-xl overflow-hidden shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <!-- 16:9 Responsive Video Iframe Wrapper -->
              <div class="relative w-full aspect-video bg-[#0d0f12]">
                <iframe 
                  class="absolute top-0 left-0 w-full h-full border-0"
                  src="https://www.youtube.com/embed/VT1hHwVUmdc" 
                  title="وثائقي كارل ماركس - DW عربية" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen>
                </iframe>
              </div>

              <!-- Content Description -->
              <div class="p-6">
                <div class="flex items-center justify-between mb-3">
                  <span class="px-2.5 py-1 rounded bg-[#8b1e1e]/20 border border-[#8b1e1e] text-[#f0ece1] text-xs font-bold">
                    الوثائقي الرئيسي
                  </span>
                  <span class="text-xs text-[#c89658] font-semibold"><i class="fa-regular fa-clock ml-1"></i> DW عربية</span>
                </div>
                
                <h3 class="text-xl font-bold text-[#f0ece1] mb-2">
                  كارل ماركس.. الفيلسوف الذي تنبأ بأزمات الرأسمالية (DW عربية)
                </h3>
                
                <p class="text-sm text-[#cbd5e1] leading-relaxed text-justify mb-4">
                  وثائقي يتناول حياة ماركس وتحليل أثر أفكاره بعد أكثر من قرن على رحيله.
                </p>
              </div>
            </div>

            <div class="px-6 pb-6 pt-2 border-t border-[#2d3342] flex items-center justify-between text-xs text-[#8e9baa]">
              <span>إنتاج DW الألمانية • مترجم للعربية</span>
              <a href="https://www.youtube.com/watch?v=VT1hHwVUmdc" target="_blank" rel="noopener noreferrer" class="text-[#c89658] hover:underline flex items-center gap-1">
                <span>المشاهدة على YouTube</span>
                <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
              </a>
            </div>
          </div>

          <!-- Documentary 2: Das Kapital Documentary -->
          <div class="bg-[#222731] border border-[#2d3342] hover:border-[#c89658] rounded-xl overflow-hidden shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <!-- 16:9 Responsive Video Iframe Wrapper -->
              <div class="relative w-full aspect-video bg-[#0d0f12]">
                <iframe 
                  class="absolute top-0 left-0 w-full h-full border-0"
                  src="https://www.youtube.com/embed/7X8II6J-6mU" 
                  title="وثائقي قراءة في كتاب رأس المال لكارل ماركس" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen>
                </iframe>
              </div>

              <!-- Content Description -->
              <div class="p-6">
                <div class="flex items-center justify-between mb-3">
                  <span class="px-2.5 py-1 rounded bg-[#c89658]/20 border border-[#c89658] text-[#fae3a2] text-xs font-bold">
                    قراءة في المؤلفات الكبرى
                  </span>
                  <span class="text-xs text-[#c89658] font-semibold"><i class="fa-solid fa-book-open ml-1"></i> كتاب «رأس المال»</span>
                </div>
                
                <h3 class="text-xl font-bold text-[#f0ece1] mb-2">
                  تشريح كتاب «رأس المال»: آليات السلعة وتراكم الثروة
                </h3>
                
                <p class="text-sm text-[#cbd5e1] leading-relaxed text-justify mb-4">
                  دراسة وثائقية وتحليلية معمقة للمفاهيم الاقتصادية التي تضمنها كتاب «رأس المال»، وكيف فكك ماركس وهم السوق الحرة وآليات الأزمات المالية الدورية.
                </p>
              </div>
            </div>

            <div class="px-6 pb-6 pt-2 border-t border-[#2d3342] flex items-center justify-between text-xs text-[#8e9baa]">
              <span>تحليل أكاديمي مصور • نقد الاقتصاد السياسي</span>
              <a href="https://www.youtube.com/watch?v=7X8II6J-6mU" target="_blank" rel="noopener noreferrer" class="text-[#c89658] hover:underline flex items-center gap-1">
                <span>المشاهدة على YouTube</span>
                <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>

  </main>

  <!-- ========================================== -->
  <!-- MODAL: CORE CONCEPT IN-DEPTH VIEWER        -->
  <!-- ========================================== -->
  <div id="conceptModal" class="fixed inset-0 z-50 hidden modal-backdrop flex items-center justify-center p-4 sm:p-6 overflow-y-auto" onclick="closeModalOnBackdrop(event)">
    <div class="bg-[#1a1d24] border-2 border-[#c89658] rounded-2xl max-w-2xl w-full p-6 sm:p-8 shadow-2xl relative my-8 transform transition-all" onclick="event.stopPropagation()">
      
      <!-- Close Button -->
      <button onclick="closeConceptModal()" aria-label="إغلاق النافذة" class="absolute top-5 left-5 w-9 h-9 rounded-full bg-[#222731] hover:bg-[#8b1e1e] border border-[#2d3342] text-[#f0ece1] flex items-center justify-center transition-colors">
        ✕
      </button>

      <!-- Modal Content Header -->
      <div class="flex items-center gap-3.5 mb-4">
        <div id="modalIconContainer" class="w-12 h-12 rounded-xl bg-[#222731] border border-[#c89658] flex items-center justify-center text-[#c89658] text-xl">
          <i class="fa-solid fa-shapes"></i>
        </div>
        <div>
          <span id="modalGermanTerm" class="text-xs text-[#c89658] font-mono font-bold tracking-wider">TERMINOLOGY</span>
          <h3 id="modalTitle" class="text-2xl font-black text-[#f0ece1]">عنوان المفهوم</h3>
        </div>
      </div>

      <!-- Modal Body -->
      <div id="modalBody" class="text-sm sm:text-base text-[#cbd5e1] leading-relaxed space-y-4 my-6 text-justify">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Primary Citation Box -->
      <div id="modalCitation" class="bg-[#222731] p-4 rounded-lg border-r-4 border-[#8b1e1e] text-xs text-[#f0ece1] font-amiri leading-relaxed">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Modal Footer -->
      <div class="mt-6 pt-4 border-t border-[#2d3342] flex justify-end">
        <button onclick="closeConceptModal()" class="px-5 py-2 rounded-lg bg-[#8b1e1e] hover:bg-[#a82828] text-[#f0ece1] text-xs font-bold transition-colors">
          إغلاق النافذة
        </button>
      </div>

    </div>
  </div>

  <!-- Toast Notification for Copy -->
  <div id="copyToast" class="fixed bottom-6 left-6 z-50 hidden bg-[#1a1d24] border border-[#c89658] text-[#f0ece1] px-4 py-3 rounded-xl shadow-2xl flex items-center gap-3 text-xs font-bold">
    <div class="w-6 h-6 rounded-full bg-[#8b1e1e] flex items-center justify-center text-[#fae3a2]">✓</div>
    <span>تم نسخ الاقتباس إلى الحافظة بنجاح!</span>
  </div>

  <!-- Back to Top Button -->
  <button id="backToTopBtn" onclick="scrollToTop()" aria-label="العودة لأعلى الصفحة" class="fixed bottom-6 right-6 z-40 hidden w-11 h-11 rounded-full bg-[#222731] hover:bg-[#8b1e1e] border border-[#c89658]/60 text-[#c89658] hover:text-[#f0ece1] shadow-2xl flex items-center justify-center transition-all transform hover:-translate-y-1">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- ========================================== -->
  <!-- FOOTER                                     -->
  <!-- ========================================== -->
  <footer class="bg-[#0e1013] border-t border-[#2d3342] text-[#8e9baa] text-xs py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8 pb-8 border-b border-[#1f242e]">
        
        <div>
          <div class="flex items-center gap-2 mb-3">
            <i class="fa-solid fa-feather text-[#c89658]"></i>
            <span class="text-sm font-bold text-[#f0ece1]">مشروع توثيق الفكر النقدي</span>
          </div>
          <p class="leading-relaxed">
            منصة بحثية تهدف لتقديم قراءة رصينة في كتابات كارل ماركس وفريدريك إنجلز وتفكيك مفاهيم الاقتصاد السياسي باللغة العربية.
          </p>
        </div>

        <div>
          <h4 class="text-sm font-bold text-[#f0ece1] mb-3">أقسام الملف</h4>
          <ul class="space-y-1.5">
            <li><a href="#hero" class="hover:text-[#c89658] transition-colors">الرئيسية ونبذة المؤلف</a></li>
            <li><a href="#biography" class="hover:text-[#c89658] transition-colors">السيرة والمسار الحياتي</a></li>
            <li><a href="#works" class="hover:text-[#c89658] transition-colors">المؤلفات الأساسية</a></li>
            <li><a href="#concepts" class="hover:text-[#c89658] transition-colors">المفاهيم النظرية الأربعة</a></li>
            <li><a href="#timeline" class="hover:text-[#c89658] transition-colors">الخط الزمني (1818 - 1883)</a></li>
          </ul>
        </div>

        <div>
          <h4 class="text-sm font-bold text-[#f0ece1] mb-3">مراجع وتوثيقات</h4>
          <p class="leading-relaxed mb-3">
            كافة النصوص مقتبسة من الترجمات المعتمدة لأعمال ماركس الكاملة (معهد الماركسية اللينينية، ترجمات فالح عبد الجبار، العفيف الأخضر، وجورج طرابيشي).
          </p>
          <div class="text-[#c89658] font-mono text-[11px]">
            MEGA (Marx-Engels-Gesamtausgabe) Archive Reference
          </div>
        </div>

      </div>

      <div class="flex flex-col sm:flex-row items-center justify-between text-center sm:text-right gap-3">
        <div>
          <span>© 1818 – 1883 كارل ماركس | المشاع الإبداعي الفكري الحر</span>
        </div>
        <div>
          <span class="text-[#c89658]">«إن الحقيقة تحرر، والمهمة هي تغيير العالم»</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- JAVASCRIPT LOGIC                           -->
  <!-- ========================================== -->
  <script>
    // ----------------------------------------------------
    // 1. Quotes Data & Engine
    // ----------------------------------------------------
    const quotesData = [
      {{
        text: "«إن نمط إنتاج الحياة المادية يشترط سيرورة الحياة الاجتماعية والسياسية والروحية بوجه عام. ليس وعي الناس هو الذي يحدد وجودهم، بل وجودهم الاجتماعي هو الذي يحدد وعيهم.»",
        source: "مقدمة «مساهمة في نقد الاقتصاد السياسي» (1859)"
      }},
      {{
        text: "«يا عمال العالم، اتحدوا! فليس لديكم ما تخسرونه سوى أغلالكم.»",
        source: "خاتمة «البيان الشيوعي» (1848)"
      }},
      {{
        text: "«إن نقد الدين يحرر الإنسان ليفكر ويعمل كإنسان استعاد رشده.»",
        source: "مقدمة «نقد فلسفة الحق عند هيغل» (1844)"
      }},
      {{
        text: "«إن الفلاسفة لم يفعلوا غير تفسير العالم بطرق مختلفة، ولكن المهم هو تغييره.»",
        source: "«أطروحات حول فيورباخ» — الأطروحة 11 (1845)"
      }}
    ];

    let currentQuoteIndex = 0;

    function renderQuotesUI() {{
      const textElem = document.getElementById('quoteTextDisplay');
      const sourceElem = document.getElementById('quoteSourceTag');
      const counterElem = document.getElementById('quoteCounter');
      const pillsElem = document.getElementById('quotePillsContainer');

      // Update text with fade effect
      textElem.style.opacity = '0';
      textElem.style.transform = 'translateY(8px)';

      setTimeout(() => {{
        textElem.innerText = quotesData[currentQuoteIndex].text;
        sourceElem.innerText = quotesData[currentQuoteIndex].source;
        counterElem.innerText = `الاقتباس ${{currentQuoteIndex + 1}} من ${{quotesData.length}}`;

        textElem.style.opacity = '1';
        textElem.style.transform = 'translateY(0)';
      }}, 200);

      // Render pills
      pillsElem.innerHTML = '';
      quotesData.forEach((_, idx) => {{
        const dot = document.createElement('button');
        dot.ariaLabel = `الاقتباس رقم ${{idx + 1}}`;
        dot.className = `w-2.5 h-2.5 rounded-full transition-all ${{
          idx === currentQuoteIndex ? 'bg-[#8b1e1e] w-6' : 'bg-[#b89b72] hover:bg-[#8b1e1e]'
        }}`;
        dot.onclick = () => {{
          currentQuoteIndex = idx;
          renderQuotesUI();
        }};
        pillsElem.appendChild(dot);
      }});
    }}

    function navigateQuote(step) {{
      currentQuoteIndex = (currentQuoteIndex + step + quotesData.length) % quotesData.length;
      renderQuotesUI();
    }}

    function copyCurrentQuote() {{
      const currentQuote = quotesData[currentQuoteIndex];
      const copyString = `${{currentQuote.text}} — ${{currentQuote.source}}`;
      
      navigator.clipboard.writeText(copyString).then(() => {{
        const toast = document.getElementById('copyToast');
        toast.classList.remove('hidden');
        setTimeout(() => {{
          toast.classList.add('hidden');
        }}, 3000);
      }}).catch(() => {{
        alert("تم نسخ الاقتباس: " + copyString);
      }});
    }}

    // ----------------------------------------------------
    // 2. Concepts Modal Data & Functions
    // ----------------------------------------------------
    const conceptsData = {{
      'historical-materialism': {{
        title: "المادية التاريخية (Historical Materialism)",
        german: "HISTORISCHER MATERIALISMUS",
        icon: "fa-solid fa-gears",
        body: `
          <p>تُعد <strong>المادية التاريخية</strong> حجر الزاوية في فلسفة ماركس العلمية للتاريخ. جوهر هذا المفهوم هو أن التطور الإنساني لا يقوده التطور المجرد للأفكار أو الروح المطلقة (كما افترض هيغل)، بل تحكمه الشروط المادية لإنتاج وسائل العيش وإعادة إنتاجها.</p>
          <p>تنص النظرية على أن لكل مرحلة تاريخية <strong>بنية تحتية (قاعدة اقتصادية)</strong> تتشكل من قوى الإنتاج (الأدوات، المهارات، والموارد) وعلاقات الإنتاج (علاقات الملكية وتقسيم العمل). هذه البنية التحتية هي التي تحدد وتفرز <strong>البنية الفوقية</strong> المكونة من القوانين، الأنظمة السياسية، العقائد الدينية، والمذاهب الفكرية.</p>
          <p>وعندما تتطور قوى الإنتاج إلى حد يصطدم بعلاقات الإنتاج القائمة التي تتحول إلى قيود كابحة لها، تنفتح مرحلة من الثورات الاجتماعية تؤدي إلى تبدل التشكيلة الاقتصادية بأكملها.</p>
        `,
        citation: "«ليس وعي الناس هو الذي يحدد وجودهم، بل وجودهم الاجتماعي هو الذي يحدد وعيهم.» — نقد الاقتصاد السياسي"
      }},
      'surplus-value': {{
        title: "فائض القيمة (Surplus Value)",
        german: "MEHRWERT / LE CAPITAL",
        icon: "fa-solid fa-coins",
        body: `
          <p><strong>فائض القيمة</strong> هو الاكتشاف الاقتصادي الأبرز لماركس الذي فكك به لغز التراكم الرأسمالي وأصل الربح. أثبت ماركس أن قوة العمل هي السلعة الوحيدة القادرة أثناء استهلاكها على خلق قيمة تفوق قيمتها الخاصة (تكلفة تجديدها وإبقاء العامل حياً).</p>
          <p>يقسم ماركس يوم العمل إلى جزأين: 
          <strong>1. وقت العمل الضروري:</strong> الذي ينتج فيه العامل ما يعادل أجره اليومي الفعلي.
          <strong>2. وقت العمل الفائض:</strong> وفيه يستمر العامل بالإنتاج مجاناً لحساب الرأسمالي دون أي مقابل، وهو المنبع الصافي لفائض القيمة الذي يتحول في السوق إلى ريع وفائدة وربح تجاري وصناعي.</p>
          <p>وبذلك، فإن الربح الرأسمالي في التحليل الماركسي ليس مكافأة على المخاطرة أو التنظيم، بل هو اقتطاع ممنهج لوقت عمل غير مدفوع الأجر مستخلص من طبقة العمال.</p>
        `,
        citation: "«إن رأس المال هو عمل ميت، لا يحيا، مثل مصاص الدماء، إلا بامتصاص العمل الحي، وكلما عاش أكثر امتص قدراً أكبر من العمل.» — رأس المال (المجلد الأول)"
      }},
      'alienation': {{
        title: "الاغتراب (Alienation)",
        german: "ENTFREMDUNG / ALIENATION",
        icon: "fa-solid fa-user-lock",
        body: `
          <p>طوّر ماركس مفهوم <strong>الاغتراب</strong> في «مخطوطات 1844 الفلسفية والاقتصادية»، موضحاً كيف يُحرم الإنسان في ظل النظام الرأسمالي من ماهيته الإنسانية الحرة وتحويله إلى امتداد للآلة وسلعة قابلة للشراء والاستبدال.</p>
          <p>يتجلى الاغتراب في أربعة أبعاد مترابطة:
          <br><strong>• الاغتراب عن نتاج العمل:</strong> السلعة التي يصنعها العامل لا تنتمي إليه بل تصبح قوة مستقلة غريبة تواجهه وتتحكم بمصيره.
          <br><strong>• الاغتراب عن عملية الإنتاج:</strong> العمل لم يعد تحقيقاً للذات وإشباعاً إبداعياً، بل عملاً شاقاً ومملاً يمارسه العامل فقط لتفادي الموت جوعاً.
          <br><strong>• الاغتراب عن النوع الإنساني (Gattungswesen):</strong> افتقاد الإنسان لقدرته على الإبداع الواعي الحر الذي يميزه عن سائر الكائنات الحية.
          <br><strong>• الاغتراب عن البشر الآخرين:</strong> سيادة المنافسة العمياء والتناحر بين العمال على لقمة العيش بدلاً من التضامن والتعاون المشترك.</p>
        `,
        citation: "«كلما زاد العامل من إنتاج الثروة، وكلما زاد إنتاجه قوة وحجماً، ازداد العامل فقراً.» — مخطوطات باريس 1844"
      }},
      'class-struggle': {{
        title: "صراع الطبقات (Class Struggle)",
        german: "KLASSENKAMPF / CLASS STRUGGLE",
        icon: "fa-solid fa-link-slash",
        body: `
          <p>يُمثل <strong>صراع الطبقات</strong> عند ماركس المحرك الديناميكي لتاريخ الحضارات البشرية منذ انتهاء المشاعية البدائية. الصراع ليس عَرَضياً أو نابعاً من سوء نية، بل هو تناقض موضوعي حتمي ينشأ بين طبقة تمتلك وسائل الإنتاج وطبقة محرومة منها وتضطر لبيع قوة عملها للبقاء.</p>
          <p>في المجتمع الرأسمالي، يتبسط الصراع ويتجه للاستقطاب الجذري بين طبقتين رئيسيتين: <strong>البرجوازية (مالكو رأس المال)</strong> و<strong>البروليتاريا (العمال المأجورون)</strong>.</p>
          <p>ويرى ماركس أن هذا التناقض لن يُحل عبر الإصلاحات الترقيعية، بل من خلال الوعي الطبقي المنظم للبروليتاريا الذي يقود لتحويل ثوري يُنهي الملكية الخاصة لوسائل الإنتاج ويؤسس لمجتمع لاطبقي يتحرر فيه الجميع.</p>
        `,
        citation: "«إن تاريخ كل مجتمع إلى يومنا هذا لم يكن سوى تاريخ صراع الطبقات.» — البيان الشيوعي (1848)"
      }}
    }};

    function openConceptModal(conceptKey) {{
      const data = conceptsData[conceptKey];
      if (!data) return;

      document.getElementById('modalTitle').innerText = data.title;
      document.getElementById('modalGermanTerm').innerText = data.german;
      document.getElementById('modalIconContainer').innerHTML = `<i class="${{data.icon}}"></i>`;
      document.getElementById('modalBody').innerHTML = data.body;
      document.getElementById('modalCitation').innerText = data.citation;

      const modal = document.getElementById('conceptModal');
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeConceptModal() {{
      const modal = document.getElementById('conceptModal');
      modal.classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function closeModalOnBackdrop(e) {{
      if (e.target.id === 'conceptModal') {{
        closeConceptModal();
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeConceptModal();
    }});

    // ----------------------------------------------------
    // 3. Work Details Accordion
    // ----------------------------------------------------
    function toggleWorkDetail(id) {{
      const el = document.getElementById(`${{id}}-detail`);
      if (el) {{
        el.classList.toggle('hidden');
      }}
    }}

    // ----------------------------------------------------
    // 4. ScrollSpy & Active Tab Tracking
    // ----------------------------------------------------
    const sections = ['hero', 'biography', 'works', 'concepts', 'timeline', 'quotes', 'documentaries'];
    const navLinks = document.querySelectorAll('.nav-tab-link');
    const scrollProgressBar = document.getElementById('scrollProgressBar');
    const backToTopBtn = document.getElementById('backToTopBtn');

    window.addEventListener('scroll', () => {{
      const scrollPos = window.scrollY;
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;

      // Update progress bar
      if (totalHeight > 0) {{
        const progress = scrollPos / totalHeight;
        scrollProgressBar.style.transform = `scaleX(${{progress}})`;
      }}

      // Back to top button visibility
      if (scrollPos > 400) {{
        backToTopBtn.classList.remove('hidden');
      }} else {{
        backToTopBtn.classList.add('hidden');
      }}

      // ScrollSpy active link
      let currentSectionId = 'hero';
      sections.forEach(secId => {{
        const el = document.getElementById(secId);
        if (el) {{
          const rect = el.getBoundingClientRect();
          if (rect.top <= 120 && rect.bottom >= 120) {{
            currentSectionId = secId;
          }}
        }}
      }});

      navLinks.forEach(link => {{
        if (link.getAttribute('data-section') === currentSectionId) {{
          link.classList.add('active-nav');
        }} else {{
          link.classList.remove('active-nav');
        }}
      }});
    }});

    function scrollToTop() {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // ----------------------------------------------------
    // 5. Mobile Navigation Toggle
    // ----------------------------------------------------
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    mobileMenuBtn.addEventListener('click', () => {{
      mobileDrawer.classList.toggle('hidden');
    }});

    mobileNavLinks.forEach(link => {{
      link.addEventListener('click', () => {{
        mobileDrawer.classList.add('hidden');
      }});
    }});

    function toggleLangNotice() {{
      const banner = document.getElementById('langNotice');
      banner.classList.toggle('hidden');
    }}

    // Initial render
    document.addEventListener('DOMContentLoaded', () => {{
      renderQuotesUI();
    }});
  </script>
</body>
</html>
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"File successfully written to: {file_path}")
    print(f"Total size: {len(html)} bytes")

if __name__ == "__main__":
    generate_site()
