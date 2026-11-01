# -*- coding: utf-8 -*-
"""
Full Karl Marx Website Generator
Generates index.html with all required sections, interactive components, 
and precise academic texts in Arabic.
"""
import os

svg_gears_scales = """
<svg viewBox="0 0 400 300" class="w-full h-full object-contain filter drop-shadow-md" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sepiaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#dfb173" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#1f242e" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bronzeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e9cf9b"/>
      <stop offset="50%" stop-color="#c89658"/>
      <stop offset="100%" stop-color="#7a5526"/>
    </linearGradient>
    <linearGradient id="ironGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>
  <!-- Background subtle vignette -->
  <rect width="400" height="300" fill="#181c24" rx="8"/>
  <circle cx="200" cy="150" r="130" fill="url(#sepiaGlow)"/>
  
  <!-- Interlocking Gears (Forces of Production) -->
  <g transform="translate(140, 195)" stroke="#2d3342" stroke-width="1.5">
    <!-- Big Cog -->
    <circle cx="0" cy="0" r="48" fill="url(#bronzeGrad)"/>
    <circle cx="0" cy="0" r="32" fill="#181c24"/>
    <circle cx="0" cy="0" r="16" fill="url(#bronzeGrad)"/>
    <!-- Cog teeth -->
    <path d="M-8,-54 h16 l-2,10 h-12 z" fill="url(#bronzeGrad)"/>
    <path d="M-8,44 h16 l2,10 h-20 z" fill="url(#bronzeGrad)"/>
    <path d="M44,-8 v16 l10,-2 v-12 z" fill="url(#bronzeGrad)"/>
    <path d="M-54,-8 v16 l10,2 v-20 z" fill="url(#bronzeGrad)"/>
    <path d="M30,30 l12,12 -8,8 -12,-12 z" fill="url(#bronzeGrad)"/>
    <path d="M-42,-42 l12,12 -8,8 -12,-12 z" fill="url(#bronzeGrad)"/>
    <path d="M30,-30 l12,-12 8,8 -12,12 z" fill="url(#bronzeGrad)"/>
    <path d="M-42,42 l12,-12 8,8 -12,12 z" fill="url(#bronzeGrad)"/>
  </g>

  <!-- Smaller Interlocking Cog -->
  <g transform="translate(225, 220)">
    <circle cx="0" cy="0" r="32" fill="url(#ironGrad)"/>
    <circle cx="0" cy="0" r="18" fill="#181c24"/>
    <circle cx="0" cy="0" r="8" fill="url(#bronzeGrad)"/>
    <rect x="-4" y="-38" width="8" height="8" fill="url(#ironGrad)"/>
    <rect x="-4" y="30" width="8" height="8" fill="url(#ironGrad)"/>
    <rect x="30" y="-4" width="8" height="8" fill="url(#ironGrad)"/>
    <rect x="-38" y="-4" width="8" height="8" fill="url(#ironGrad)"/>
    <rect x="22" y="22" width="7" height="7" fill="url(#ironGrad)"/>
    <rect x="-29" y="-29" width="7" height="7" fill="url(#ironGrad)"/>
  </g>

  <!-- Classical Balance Scales (Superstructure / Justice / Idea) resting on the material cogs -->
  <g transform="translate(200, 75)">
    <!-- Central Pillar -->
    <rect x="-4" y="0" width="8" height="110" fill="url(#bronzeGrad)"/>
    <polygon points="0,-12 12,0 -12,0" fill="#dfb173"/>
    <circle cx="0" cy="0" r="7" fill="#dfb173"/>
    <rect x="-25" y="105" width="50" height="10" rx="3" fill="url(#bronzeGrad)"/>

    <!-- Balance Beam -->
    <path d="M-90,15 L90,10" stroke="url(#bronzeGrad)" stroke-width="4" stroke-linecap="round"/>
    <circle cx="-90" cy="15" r="4" fill="#dfb173"/>
    <circle cx="90" cy="10" r="4" fill="#dfb173"/>

    <!-- Left Pan (Materials) -->
    <line x1="-90" y1="15" x2="-110" y2="60" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="-90" y1="15" x2="-70" y2="60" stroke="#cbd5e1" stroke-width="1.5"/>
    <path d="M-115,60 Q-90,75 -65,60 Z" fill="url(#bronzeGrad)"/>

    <!-- Right Pan (Ideas) -->
    <line x1="90" y1="10" x2="70" y2="55" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="90" y1="10" x2="110" y2="55" stroke="#cbd5e1" stroke-width="1.5"/>
    <path d="M65,55 Q90,70 115,55 Z" fill="url(#bronzeGrad)"/>
  </g>

  <!-- Decorative Border -->
  <rect x="10" y="10" width="380" height="280" fill="none" stroke="#3f475a" stroke-width="1" rx="4"/>
  <rect x="15" y="15" width="370" height="270" fill="none" stroke="#c89658" stroke-width="0.8" stroke-dasharray="4,3" rx="2"/>
</svg>
"""

svg_factory_coins = """
<svg viewBox="0 0 400 300" class="w-full h-full object-contain filter drop-shadow-md" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="smokeGlow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#a82828" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#181c24" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="goldCoin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fae3a2"/>
      <stop offset="50%" stop-color="#c89658"/>
      <stop offset="100%" stop-color="#80531c"/>
    </linearGradient>
    <linearGradient id="brickGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4a2222"/>
      <stop offset="100%" stop-color="#241919"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="#181c24" rx="8"/>
  <circle cx="200" cy="120" r="130" fill="url(#smokeGlow)"/>

  <!-- Smoke Plumes -->
  <g fill="#475569" opacity="0.45">
    <ellipse cx="140" cy="70" rx="24" ry="14"/>
    <ellipse cx="155" cy="50" rx="32" ry="18"/>
    <ellipse cx="175" cy="30" rx="40" ry="20"/>
    <ellipse cx="230" cy="75" rx="20" ry="12"/>
    <ellipse cx="250" cy="55" rx="28" ry="16"/>
  </g>

  <!-- 19th Century Factory Silhouette -->
  <g fill="url(#brickGrad)" stroke="#1a1d24" stroke-width="1.5">
    <!-- Factory Body -->
    <polygon points="70,210 70,140 120,110 170,140 170,210"/>
    <polygon points="170,210 170,140 220,110 270,140 270,210"/>
    <rect x="270" y="145" width="60" height="65"/>

    <!-- Chimneys -->
    <polygon points="110,120 115,75 130,75 135,120"/>
    <polygon points="195,120 200,65 215,65 220,120"/>
    <polygon points="280,145 284,85 296,85 300,145"/>

    <!-- Factory Windows -->
    <g fill="#f8fafc" opacity="0.15">
      <rect x="85" y="150" width="12" height="18" rx="2"/>
      <rect x="105" y="150" width="12" height="18" rx="2"/>
      <rect x="135" y="150" width="12" height="18" rx="2"/>
      <rect x="185" y="150" width="12" height="18" rx="2"/>
      <rect x="205" y="150" width="12" height="18" rx="2"/>
      <rect x="235" y="150" width="12" height="18" rx="2"/>
      <rect x="285" y="160" width="14" height="20" rx="2"/>
    </g>
  </g>

  <!-- Ground Line -->
  <rect x="50" y="210" width="300" height="4" fill="#3f475a"/>

  <!-- Stacked Gold Coins (Surplus Value Extraction) in Foreground -->
  <g transform="translate(230, 185)">
    <!-- Stack 1 (High) -->
    <g transform="translate(60, 0)">
      <ellipse cx="0" cy="20" rx="25" ry="9" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="14" rx="25" ry="9" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="8" rx="25" ry="9" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="2" rx="25" ry="9" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="-4" rx="25" ry="9" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="-10" rx="25" ry="9" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="-16" rx="25" ry="9" fill="url(#goldCoin)" stroke="#dfb173" stroke-width="1"/>
    </g>
    <!-- Stack 2 (Medium) -->
    <g transform="translate(20, 12)">
      <ellipse cx="0" cy="18" rx="22" ry="8" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="12" rx="22" ry="8" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="6" rx="22" ry="8" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="0" rx="22" ry="8" fill="url(#goldCoin)" stroke="#dfb173" stroke-width="1"/>
    </g>
    <!-- Stack 3 (Foreground small) -->
    <g transform="translate(-15, 20)">
      <ellipse cx="0" cy="15" rx="18" ry="7" fill="url(#goldCoin)" stroke="#5c3809" stroke-width="1"/>
      <ellipse cx="0" cy="9" rx="18" ry="7" fill="url(#goldCoin)" stroke="#dfb173" stroke-width="1"/>
    </g>
  </g>

  <!-- Decorative border -->
  <rect x="10" y="10" width="380" height="280" fill="none" stroke="#3f475a" stroke-width="1" rx="4"/>
  <rect x="15" y="15" width="370" height="270" fill="none" stroke="#c89658" stroke-width="0.8" stroke-dasharray="4,3" rx="2"/>
</svg>
"""

svg_alienation = """
<svg viewBox="0 0 400 300" class="w-full h-full object-contain filter drop-shadow-md" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="cageGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8b1e1e" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#181c24" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="50%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="#181c24" rx="8"/>
  <circle cx="200" cy="150" r="120" fill="url(#cageGlow)"/>

  <!-- Expressionist Swirls in Background (Emotional human alienation) -->
  <path d="M120,80 Q200,40 280,100 T180,240" fill="none" stroke="#8b1e1e" stroke-width="26" opacity="0.3" stroke-linecap="round"/>
  <path d="M150,110 Q240,160 220,240" fill="none" stroke="#1e3a5f" stroke-width="22" opacity="0.4" stroke-linecap="round"/>

  <!-- Melancholic Trapped Human Silhouette -->
  <g transform="translate(200, 155)">
    <!-- Head tilted down -->
    <ellipse cx="0" cy="-28" rx="16" ry="19" fill="#0d0f12"/>
    <!-- Neck -->
    <rect x="-6" y="-12" width="12" height="12" fill="#0d0f12"/>
    <!-- Slumped Shoulders and Torso -->
    <path d="M-36,25 C-36,-4 -15,-6 0,-6 C15,-6 36,-4 36,25 L28,65 L-28,65 Z" fill="#0d0f12"/>
  </g>

  <!-- Victorian Birdcage Overlay -->
  <g transform="translate(200, 140)">
    <!-- Hanging Ring & Finial -->
    <circle cx="0" cy="-90" r="10" fill="none" stroke="#c89658" stroke-width="3"/>
    <polygon points="0,-80 8,-72 -8,-72" fill="#dfb173"/>
    <ellipse cx="0" cy="-70" rx="18" ry="6" fill="#c89658"/>

    <!-- Dome Top -->
    <path d="M-65, -10 C-65,-60 65,-60 65,-10" fill="none" stroke="url(#barGrad)" stroke-width="3"/>

    <!-- Vertical Bars -->
    <line x1="-55" y1="-10" x2="-55" y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>
    <line x1="-37" y1="-35" x2="-37" y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>
    <line x1="-18" y1="-50" x2="-18" y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>
    <line x1="0"   y1="-55" x2="0"   y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>
    <line x1="18"  y1="-50" x2="18"  y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>
    <line x1="37"  y1="-35" x2="37"  y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>
    <line x1="55"  y1="-10" x2="55"  y2="85" stroke="url(#barGrad)" stroke-width="2.5"/>

    <!-- Horizontal Support Bands -->
    <path d="M-66,-10 Q0,5 66,-10" fill="none" stroke="#c89658" stroke-width="3"/>
    <path d="M-66,40 Q0,55 66,40" fill="none" stroke="#c89658" stroke-width="3"/>

    <!-- Cage Base -->
    <ellipse cx="0" cy="85" rx="72" ry="16" fill="#1e232d" stroke="#c89658" stroke-width="3"/>
    <rect x="-70" y="85" width="140" height="8" rx="2" fill="#c89658"/>
  </g>

  <!-- Decorative border -->
  <rect x="10" y="10" width="380" height="280" fill="none" stroke="#3f475a" stroke-width="1" rx="4"/>
  <rect x="15" y="15" width="370" height="270" fill="none" stroke="#c89658" stroke-width="0.8" stroke-dasharray="4,3" rx="2"/>
</svg>
"""

svg_class_struggle = """
<svg viewBox="0 0 400 300" class="w-full h-full object-contain filter drop-shadow-md" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="struggleGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#a82828" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#181c24" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="skinGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4a5568"/>
      <stop offset="100%" stop-color="#1a202c"/>
    </linearGradient>
    <linearGradient id="chainIron" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e2e8f0"/>
      <stop offset="50%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="#181c24" rx="8"/>
  <circle cx="200" cy="150" r="130" fill="url(#struggleGlow)"/>

  <!-- Radiating Rays of Dawn/Liberation -->
  <g stroke="#c89658" stroke-width="1" opacity="0.25">
    <line x1="200" y1="150" x2="60" y2="30"/>
    <line x1="200" y1="150" x2="110" y2="20"/>
    <line x1="200" y1="150" x2="200" y2="15"/>
    <line x1="200" y1="150" x2="290" y2="20"/>
    <line x1="200" y1="150" x2="340" y2="30"/>
  </g>

  <!-- Left Raised Clenched Worker Fist -->
  <g transform="translate(105, 175)">
    <!-- Arm -->
    <path d="M-30,90 L-10,0 L20,0 L35,90 Z" fill="url(#skinGrad)"/>
    <!-- Clenched Fist -->
    <path d="M-15,0 C-18,-15 -10,-35 8,-35 C24,-35 28,-18 25,0 Z" fill="url(#skinGrad)"/>
    <!-- Knuckles & Thumb -->
    <ellipse cx="6" cy="-28" rx="14" ry="7" fill="#64748b"/>
    <ellipse cx="14" cy="-14" rx="7" ry="10" fill="#475569"/>
  </g>

  <!-- Right Raised Clenched Worker Fist -->
  <g transform="translate(295, 175) scale(-1, 1)">
    <!-- Arm -->
    <path d="M-30,90 L-10,0 L20,0 L35,90 Z" fill="url(#skinGrad)"/>
    <!-- Clenched Fist -->
    <path d="M-15,0 C-18,-15 -10,-35 8,-35 C24,-35 28,-18 25,0 Z" fill="url(#skinGrad)"/>
    <!-- Knuckles & Thumb -->
    <ellipse cx="6" cy="-28" rx="14" ry="7" fill="#64748b"/>
    <ellipse cx="14" cy="-14" rx="7" ry="10" fill="#475569"/>
  </g>

  <!-- Central Reaching Open Hand (Solidarity) -->
  <g transform="translate(200, 190)">
    <path d="M-14,75 L-8,15 L12,15 L18,75 Z" fill="#2d3748"/>
    <path d="M-12,15 L-10,-20 L-4,-25 L-2,15 Z" fill="#4a5568"/>
    <path d="M-2,15 L0,-32 L6,-32 L5,15 Z" fill="#64748b"/>
    <path d="M6,15 L9,-28 L14,-26 L12,15 Z" fill="#4a5568"/>
    <path d="M12,15 L16,-15 L21,-14 L18,15 Z" fill="#2d3748"/>
  </g>

  <!-- Broken Chain Links Shattering Across Middle -->
  <g transform="translate(200, 140)">
    <!-- Shattered Center Link -->
    <path d="M-25,-8 C-15,-20 15,-20 25,-8" fill="none" stroke="url(#chainIron)" stroke-width="7" stroke-linecap="round"/>
    <path d="M-28,12 C-15,22 15,22 28,12" fill="none" stroke="url(#chainIron)" stroke-width="7" stroke-linecap="round"/>
    <!-- Shrapnel / Metal Sparks -->
    <polygon points="0,-5 8,-2 4,4 -3,2" fill="#dfb173"/>
    <polygon points="18,5 24,0 20,-6 14,-2" fill="#dfb173"/>
    <polygon points="-16,-2 -22,-8 -26,-2 -20,4" fill="#dfb173"/>
    <circle cx="3" cy="-14" r="2.5" fill="#f0ece1"/>
    <circle cx="-12" cy="18" r="2" fill="#f0ece1"/>

    <!-- Left Chain Segment -->
    <g transform="translate(-65, 0) rotate(-15)">
      <rect x="-24" y="-12" width="48" height="24" rx="12" fill="none" stroke="url(#chainIron)" stroke-width="6"/>
    </g>
    <!-- Right Chain Segment -->
    <g transform="translate(65, 0) rotate(15)">
      <rect x="-24" y="-12" width="48" height="24" rx="12" fill="none" stroke="url(#chainIron)" stroke-width="6"/>
    </g>
  </g>

  <!-- Decorative border -->
  <rect x="10" y="10" width="380" height="280" fill="none" stroke="#3f475a" stroke-width="1" rx="4"/>
  <rect x="15" y="15" width="370" height="270" fill="none" stroke="#c89658" stroke-width="0.8" stroke-dasharray="4,3" rx="2"/>
</svg>
"""

print("SVG assets generated.")
